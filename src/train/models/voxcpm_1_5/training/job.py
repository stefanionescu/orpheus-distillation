"""One training run of one voice."""

from __future__ import annotations

from typing import TYPE_CHECKING
import logging

from torch.optim import AdamW
from tensorboardX import SummaryWriter
from transformers import get_cosine_schedule_with_warmup

from schemas.models.voxcpm_1_5.training import TrainingResult
from src.train.models.voxcpm_1_5.model.config import LoraConfig
from src.train.models.voxcpm_1_5.model.voxcpm import VoxCPMModel
from src.train.models.voxcpm_1_5.training.loop import (
    TrainingContext,
    TrainingProgress,
    run_training_steps,
    install_stop_signal,
)
from src.train.models.voxcpm_1_5.training.batch import build_batch_packer
from src.train.models.voxcpm_1_5.training.dataset import build_loader, build_sampler, read_training_dataset
from src.train.models.voxcpm_1_5.training.devices import read_gpu_report, print_gpu_report
from src.train.models.voxcpm_1_5.training.accelerator import Accelerator, build_accelerator
from src.train.models.voxcpm_1_5.training.checkpoints import read_checkpoint

if TYPE_CHECKING:
    from pathlib import Path

    from torch import nn
    from torch.utils.data import DataLoader

    from schemas.settings import TrainEnvironment
    from schemas.models.voxcpm_1_5.training import LoraSettings, TrainingClip, TrainingSettings

logger = logging.getLogger(__name__)


class TrainingDataError(Exception):
    """The manifest has too few clips of the voice within the token budget to fill one batch."""


def _build_context(settings: TrainingSettings, model: VoxCPMModel, accelerator: Accelerator) -> TrainingContext:
    batch_packer = build_batch_packer(model, accelerator.device)
    folders = settings.folders
    train_dataset = read_training_dataset(
        folders.train_manifest_path, settings.voice, model, settings.max_batch_tokens // settings.batch_size
    )
    train_sampler = build_sampler(train_dataset, accelerator)
    # A loader cannot shuffle an empty dataset, so skip it and raise the same error.
    train_loader = None
    if len(train_dataset) > 0:
        train_loader = build_loader(train_dataset, settings, train_sampler, is_training=True)
    if train_loader is None or len(train_loader) == 0:
        message = (
            f"The manifest {folders.train_manifest_path} keeps {len(train_dataset)} clips of voice {settings.voice}, "
            f"fewer than one batch of {settings.batch_size} on each of {accelerator.world_size} processes"
        )
        raise TrainingDataError(message)
    # DDP broadcasts every registered submodule, so unregister the frozen VAE; the batch packer keeps it.
    model.register_module("audio_vae", None)
    optimizer = _build_optimizer(settings, model, accelerator)
    return TrainingContext(
        model=accelerator.prepare_model(model),
        unwrapped_model=model,
        train_loader=train_loader,
        train_sampler=train_sampler,
        train_size=len(train_dataset),
        val_loader=_build_val_loader(settings, model, accelerator),
        batch_packer=batch_packer,
        optimizer=optimizer,
        scheduler=get_cosine_schedule_with_warmup(optimizer, settings.warmup_steps, settings.steps),
        accelerator=accelerator,
        writer=SummaryWriter(logdir=str(folders.voice_events_folder)) if accelerator.is_main else None,
        settings=settings,
    )


def _build_val_loader(
    settings: TrainingSettings, model: VoxCPMModel, accelerator: Accelerator
) -> DataLoader[TrainingClip] | None:
    if settings.folders.val_manifest_path is None:
        return None
    val_dataset = read_training_dataset(settings.folders.val_manifest_path, settings.voice, model, None)
    if len(val_dataset) == 0:
        logger.info("The validation manifest holds no clip of voice %s, so the run validates nothing", settings.voice)
        return None
    return build_loader(val_dataset, settings, build_sampler(val_dataset, accelerator), is_training=False)


def _build_optimizer(settings: TrainingSettings, model: VoxCPMModel, accelerator: Accelerator) -> AdamW:
    # The vendored forward pass moves each batch to this device.
    model.device = str(accelerator.device)
    if accelerator.is_main:
        print_trainable_parameters(model)
    trainable_parameters = [parameter for parameter in model.parameters() if parameter.requires_grad]
    return AdamW(trainable_parameters, lr=settings.learning_rate, weight_decay=settings.weight_decay)


def read_training_model(base_model_folder: Path, lora: LoraSettings) -> VoxCPMModel:
    """Read the base model with fresh LoRA layers, in training mode, with every other weight frozen.

    Args:
        base_model_folder: Downloaded base model.
        lora: LoRA settings of the run.

    Returns:
        The model.

    """
    lora_config = LoraConfig(
        enable_lm=lora.enable_lm,
        enable_dit=lora.enable_dit,
        enable_proj=lora.enable_proj,
        r=lora.rank,
        alpha=lora.alpha,
        dropout=lora.dropout,
        target_modules_lm=list(lora.target_modules),
        target_modules_dit=list(lora.target_modules),
    )
    logger.info("Reading the base model from %s with LoRA rank %d, alpha %d", base_model_folder, lora.rank, lora.alpha)
    return VoxCPMModel.read_pretrained(base_model_folder, optimize=False, training=True, lora_config=lora_config)


def print_trainable_parameters(model: nn.Module) -> None:
    """Log the count and share of trainable weights.

    Args:
        model: The model.

    """
    trainable = sum(parameter.numel() for parameter in model.parameters() if parameter.requires_grad)
    total = sum(parameter.numel() for parameter in model.parameters())
    logger.info("Training %d of %d weights (%.2f%%)", trainable, total, 100 * trainable / total)


def run_training_job(settings: TrainingSettings, lora: LoraSettings, environment: TrainEnvironment) -> TrainingResult:
    """Train the adapter of one voice from its newest checkpoint until the last step or a stop signal.

    The run uses the CUDA device of its local rank, or the CPU when torch finds none. A manifest with fewer clips of
    the voice than one batch raises TrainingDataError before any step.

    Args:
        settings: Run settings.
        lora: LoRA settings of a fresh run; a resumed run reads its checkpoint weights.
        environment: Distributed layout of the process.

    Returns:
        The last checkpoint, and the signal that stopped the run, if any.

    """
    report = read_gpu_report(environment.local_rank)
    print_gpu_report(report)
    accelerator = build_accelerator(environment, report)
    model = read_training_model(settings.folders.base_model_folder, lora)
    context = _build_context(settings, model, accelerator)
    step = read_checkpoint(model, context.optimizer, context.scheduler, settings.folders.voice_checkpoints_folder)
    progress = TrainingProgress(step=step)
    try:
        with install_stop_signal(progress):
            checkpoint_folder = run_training_steps(context, progress)
    finally:
        if context.writer is not None:
            context.writer.close()
    return TrainingResult(checkpoint_folder=checkpoint_folder, stop_signal=progress.stop_signal)

"""The training steps of one run."""

from __future__ import annotations

import signal
from typing import TYPE_CHECKING, Protocol, cast
import logging
import itertools
import contextlib
from dataclasses import dataclass

import torch

from config.models.voxcpm_1_5.training import MAX_GRAD_NORM, MAX_VAL_BATCHES
from config.models.voxcpm_1_5.checkpoints import STEP_TEMPLATE
from src.train.models.voxcpm_1_5.training.batch import build_total_loss
from src.train.models.voxcpm_1_5.training.checkpoints import write_checkpoint, is_checkpoint_complete

if TYPE_CHECKING:
    from types import FrameType
    from pathlib import Path
    from collections.abc import Mapping, Callable, Iterator, Generator

    from torch import nn
    from torch.optim import Optimizer
    from torch.utils.data import DataLoader
    from torch.optim.lr_scheduler import LRScheduler
    from torch.utils.data.distributed import DistributedSampler

    from schemas.models.voxcpm_1_5.batch import PackedBatch
    from schemas.models.voxcpm_1_5.training import TrainingClip, CollatedBatch, TrainingSettings
    from src.train.models.voxcpm_1_5.model.voxcpm import VoxCPMModel
    from src.train.models.voxcpm_1_5.training.batch import BatchPacker
    from src.train.models.voxcpm_1_5.training.accelerator import Accelerator

STOP_SIGNALS = (signal.SIGINT, signal.SIGTERM)

logger = logging.getLogger(__name__)

run_backward = cast("Callable[[torch.Tensor], None]", torch.Tensor.backward)


class MetricWriter(Protocol):
    """The part of the TensorBoard writer that the loop uses."""

    def add_scalar(self, tag: str, scalar_value: float, global_step: int) -> None:
        """Write a metric value at a step.

        Args:
            tag: Metric name.
            scalar_value: The value.
            global_step: Optimizer steps completed.

        """

    def close(self) -> None:
        """Flush the event file and close it."""


@dataclass
class TrainingProgress:
    """State that changes while a run trains.

    Attributes:
        step: Optimizer steps completed, including those of the resumed checkpoint.
        stop_requested: Whether a signal asked the run to stop after the current step.
        stop_signal: That signal number, or None.

    """

    step: int
    stop_requested: bool = False
    stop_signal: int | None = None

    def request_stop(self, signal_number: int, _frame: FrameType | None) -> None:
        """Record a stop signal. The handler only sets fields, so the loop writes the checkpoint itself.

        Args:
            signal_number: Signal number.
            _frame: Interrupted frame, unused.

        """
        self.stop_requested = True
        self.stop_signal = signal_number


@dataclass(frozen=True)
class TrainingContext:
    """Live objects of one run. They hold torch state, so they stay out of the schemas.

    Attributes:
        model: Model to call: the model itself or its DDP wrapper.
        unwrapped_model: Model without its DDP wrapper, whose weights the checkpoints hold.
        train_loader: Training clip loader.
        train_sampler: Distributed sampler of the process share, or None in a single process.
        train_size: Training clip count, for the epoch metric.
        val_loader: Validation clip loader, or None to skip validation.
        batch_packer: Packer of collated clips into model batches.
        optimizer: The optimizer.
        scheduler: Learning rate scheduler.
        accelerator: Device and rank of the process.
        writer: TensorBoard writer on rank 0, or None on other ranks.
        settings: Run settings.

    """

    model: nn.Module
    unwrapped_model: VoxCPMModel
    train_loader: DataLoader[TrainingClip]
    train_sampler: DistributedSampler[TrainingClip] | None
    train_size: int
    val_loader: DataLoader[TrainingClip] | None
    batch_packer: BatchPacker
    optimizer: Optimizer
    scheduler: LRScheduler
    accelerator: Accelerator
    writer: MetricWriter | None
    settings: TrainingSettings


def _call_model(context: TrainingContext, batch: PackedBatch, progress: float) -> Mapping[str, torch.Tensor | None]:
    with context.accelerator.autocast():
        return cast("Mapping[str, torch.Tensor | None]", context.model(batch, progress=progress))


def _write_step_checkpoint(context: TrainingContext, step: int) -> Path:
    if context.accelerator.is_main:
        return write_checkpoint(
            context.unwrapped_model, context.optimizer, context.scheduler, step, context.settings.folders
        )
    return context.settings.folders.voice_checkpoints_folder / STEP_TEMPLATE.format(step=step)


def _run_step_reports(context: TrainingContext, step: int, metrics: Mapping[str, float]) -> None:
    settings = context.settings
    if context.accelerator.is_main and is_step_due(step, settings.log_interval, settings.steps):
        print_step_metrics(context, step, metrics)
    if is_step_due(step, settings.val_interval, settings.steps):
        run_validation(context, step)
    if step % settings.checkpoint_interval == 0 and step < settings.steps:
        _write_step_checkpoint(context, step)


def is_step_due(step: int, interval: int, last_step: int) -> bool:
    """Tell whether a periodic action runs after a step: every `interval` steps, and after the last step.

    Args:
        step: Optimizer steps completed.
        interval: Steps between two runs of the action.
        last_step: Step count at the end of the run.

    Returns:
        Whether the action runs.

    """
    return step % interval == 0 or step == last_step


def build_batch_iterator(
    loader: DataLoader[TrainingClip], sampler: DistributedSampler[TrainingClip] | None
) -> Iterator[CollatedBatch]:
    """Yield batches without end, starting a new shuffled epoch whenever the loader runs out.

    Args:
        loader: Training loader that yields at least one batch per epoch.
        sampler: Distributed sampler, reseeded each epoch, or None.

    Yields:
        The collated batches.

    """
    for epoch in itertools.count():
        if sampler is not None:
            sampler.set_epoch(epoch)
        yield from cast("Iterator[CollatedBatch]", iter(loader))


def run_micro_steps(context: TrainingContext, batches: Iterator[CollatedBatch], progress: float) -> dict[str, float]:
    """Run the forward and backward passes of the micro-batches of one optimizer step.

    Args:
        context: Live objects of the run.
        batches: Endless training batch iterator.
        progress: Share of the run completed, which the diffusion loss reads.

    Returns:
        The two losses of the last micro-batch.

    """
    settings = context.settings
    accumulation = settings.accumulation_steps
    losses: dict[str, float] = {}
    for index in range(accumulation):
        sync = contextlib.nullcontext() if index == accumulation - 1 else context.accelerator.no_sync()
        with sync:
            outputs = _call_model(context, context.batch_packer(next(batches)), progress)
            loss, losses = build_total_loss(outputs, settings.loss_diff_weight, settings.loss_stop_weight)
            run_backward(context.accelerator.scaler.scale(loss / accumulation))
    return losses


def run_optimizer_step(context: TrainingContext, batches: Iterator[CollatedBatch], step: int) -> dict[str, float]:
    """Run one optimizer step: micro-batches, gradient clip, update, and learning rate step.

    Args:
        context: Live objects of the run.
        batches: Endless training batch iterator.
        step: Optimizer steps completed before this one.

    Returns:
        Step metrics: the two losses, gradient norm, learning rate, and epoch.

    """
    scaler = context.accelerator.scaler
    context.optimizer.zero_grad(set_to_none=True)
    losses = run_micro_steps(context, batches, step / context.settings.steps)
    scaler.unscale_(context.optimizer)
    grad_norm = torch.nn.utils.clip_grad_norm_(context.unwrapped_model.parameters(), max_norm=MAX_GRAD_NORM)
    scaler.step(context.optimizer)
    scaler.update()
    context.scheduler.step()
    clips_seen = (step + 1) * context.settings.accumulation_steps * context.settings.batch_size
    return losses | {
        "grad_norm": float(grad_norm.item()),
        "lr": float(context.scheduler.get_last_lr()[0]),
        "epoch": clips_seen / context.train_size,
    }


def print_step_metrics(context: TrainingContext, step: int, metrics: Mapping[str, float]) -> None:
    """Write the step metrics to the log and TensorBoard.

    Args:
        context: Live objects of the run.
        step: Optimizer steps completed.
        metrics: Step metrics.

    """
    if context.writer is not None:
        for name, value in metrics.items():
            context.writer.add_scalar(f"train/{name}", value, step)
    logger.info("Step %d: %s", step, ", ".join(f"{name}={value:.6g}" for name, value in metrics.items()))


def run_validation(context: TrainingContext, step: int) -> None:
    """Run the validation batches, average the loss across processes, and log it on rank 0.

    Args:
        context: Live objects of the run; nothing runs without a validation loader.
        step: Optimizer steps completed.

    """
    if context.val_loader is None:
        return
    settings = context.settings
    context.model.eval()
    losses: list[torch.Tensor] = []
    with torch.no_grad():
        for batch in itertools.islice(context.val_loader, MAX_VAL_BATCHES):
            outputs = _call_model(context, context.batch_packer(cast("CollatedBatch", batch)), 0.0)
            losses.append(build_total_loss(outputs, settings.loss_diff_weight, settings.loss_stop_weight)[0].detach())
    context.model.train()
    if not losses:
        return
    mean_loss = context.accelerator.all_reduce_mean(torch.stack(losses).mean()).item()
    if context.accelerator.is_main:
        if context.writer is not None:
            context.writer.add_scalar("val/loss/total", mean_loss, step)
        logger.info("Step %d: validation loss %.6g", step, mean_loss)


def run_training_steps(context: TrainingContext, progress: TrainingProgress) -> Path:
    """Run optimizer steps until the last step or a stop signal.

    Before it returns, the loop writes a checkpoint of the last completed step unless one already exists.

    Args:
        context: Live objects of the run.
        progress: Progress that the loop advances and the signal handler sets.

    Returns:
        Folder of the last checkpoint.

    """
    batches = build_batch_iterator(context.train_loader, context.train_sampler)
    logger.info("Training voice %s from step %d to %d", context.settings.voice, progress.step, context.settings.steps)
    while progress.step < context.settings.steps:
        if context.accelerator.is_any_rank_flagged(is_flagged=progress.stop_requested):
            logger.warning("Stopping after step %d on signal %s", progress.step, progress.stop_signal)
            break
        metrics = run_optimizer_step(context, batches, progress.step)
        progress.step += 1
        _run_step_reports(context, progress.step, metrics)
    checkpoint_folder = context.settings.folders.voice_checkpoints_folder / STEP_TEMPLATE.format(step=progress.step)
    if is_checkpoint_complete(checkpoint_folder):
        return checkpoint_folder
    return _write_step_checkpoint(context, progress.step)


def set_stop_action(
    action: Callable[[int, FrameType | None], object] | signal.Handlers, _worker_index: int = 0
) -> None:
    """Set one action for SIGINT and SIGTERM in this process.

    Loader workers start with `SIG_IGN`. Control+C reaches the whole process group, and a worker that dies on it
    makes the main process raise before the loop sees the stop request.

    Args:
        action: Handler of both signals, or `SIG_IGN`.
        _worker_index: Worker index that the loader passes, unused.

    """
    for number in STOP_SIGNALS:
        signal.signal(number, action)


@contextlib.contextmanager
def install_stop_signal(progress: TrainingProgress) -> Generator[None]:
    """Make SIGINT and SIGTERM ask the loop to stop, and restore the earlier handlers on exit.

    The handler only records the request, so the loop writes the checkpoint between two steps, not halfway through one.

    Args:
        progress: Progress whose stop request the handler sets.

    Yields:
        Nothing; the earlier handlers return on exit.

    """
    earlier_actions = {number: signal.getsignal(number) for number in STOP_SIGNALS}
    set_stop_action(progress.request_stop)
    try:
        yield
    finally:
        for number, action in earlier_actions.items():
            signal.signal(number, signal.SIG_DFL if action is None else action)

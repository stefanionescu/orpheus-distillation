"""Checkpoints of a training run: LoRA weights, LoRA config, and training state."""

from __future__ import annotations

import json
import shutil
from typing import TYPE_CHECKING, cast
import logging

import torch
from pydantic import ValidationError
import safetensors.torch

from config.voxcpm_1_5.checkpoints import (
    NEWEST_LINK,
    STEP_PREFIX,
    STEP_TEMPLATE,
    LORA_CONFIG_FILE,
    TRAINING_STATE_FILE,
    OPTIMIZER_STATE_FILE,
    SCHEDULER_STATE_FILE,
    LORA_PARAMETER_MARKER,
    TRAINING_STATE_STEP_KEY,
)
from src.train.voxcpm_1_5.model.lora import COMPILED_SEGMENT, LORA_WEIGHTS_FILE
from src.train.voxcpm_1_5.model.config import LoraConfig
from src.train.voxcpm_1_5.data.manifest import copy_tokenizer_files

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Callable, Sequence

    from torch.optim import Optimizer
    from torch.optim.lr_scheduler import LRScheduler

    from schemas.voxcpm_1_5.training import TrainingFolders
    from src.train.voxcpm_1_5.model.voxcpm import VoxCPMModel

logger = logging.getLogger(__name__)

write_torch_file = cast("Callable[[object, Path], None]", torch.save)
read_torch_file = cast("Callable[..., dict[str, object]]", torch.load)


class CheckpointError(Exception):
    """A checkpoint lacks a file or holds a malformed one, or no voice has a checkpoint."""


def _parse_step(name: str) -> int | None:
    digits = name.removeprefix(STEP_PREFIX)
    if digits == name or not digits.isdigit():
        return None
    return int(digits)


def _create_partial_folder(checkpoint_folder: Path) -> Path:
    partial_folder = checkpoint_folder.with_name(f".{checkpoint_folder.name}.partial")
    # An interrupted write of this step left the folder, and no link names it, so delete it.
    if partial_folder.exists():
        shutil.rmtree(partial_folder)
    partial_folder.mkdir(parents=True)
    return partial_folder


def is_checkpoint_complete(checkpoint_folder: Path) -> bool:
    """Tell whether a checkpoint holds its training state, which a write puts in place last.

    Args:
        checkpoint_folder: Checkpoint folder, which may be missing.

    Returns:
        Whether the folder holds a whole checkpoint.

    """
    return (checkpoint_folder / TRAINING_STATE_FILE).is_file()


def update_newest_link(voice_checkpoints_folder: Path, target_folder: Path) -> None:
    """Point the newest link of a voice at a checkpoint, replacing the link in one rename.

    Args:
        voice_checkpoints_folder: Checkpoints of one voice.
        target_folder: Checkpoint inside it. The link stores its name, so moving the run keeps the link valid.

    """
    newest_link = voice_checkpoints_folder / NEWEST_LINK
    if newest_link.is_dir() and not newest_link.is_symlink():
        shutil.rmtree(newest_link)
    pending_link = voice_checkpoints_folder / f".{NEWEST_LINK}.pending"
    pending_link.unlink(missing_ok=True)
    pending_link.symlink_to(target_folder.name, target_is_directory=True)
    pending_link.replace(newest_link)


def write_checkpoint(
    model: VoxCPMModel, optimizer: Optimizer, scheduler: LRScheduler, step: int, folders: TrainingFolders
) -> Path:
    """Write the checkpoint of a step into its own folder, then point the newest link at it.

    The files go to a hidden sibling folder, one rename turns it into the step folder, and the link moves last. A
    write that fails or dies halfway leaves every earlier step whole.

    Args:
        model: Model without its DDP wrapper.
        optimizer: Optimizer of the run.
        scheduler: Learning rate scheduler.
        step: Optimizer steps completed.
        folders: Run folders, for the checkpoints of the voice and the tokenizer folder.

    Returns:
        The checkpoint folder.

    Raises:
        ValueError: The model has no LoRA config.

    """
    if model.lora_config is None:
        message = "The model has no LoRA layers, so it has no adapter to save"
        raise ValueError(message)
    checkpoint_folder = folders.voice_checkpoints_folder / STEP_TEMPLATE.format(step=step)
    partial_folder = _create_partial_folder(checkpoint_folder)
    # A compiled model adds COMPILED_SEGMENT to its parameter names, and checkpoints store the plain names.
    lora_state = {
        name.replace(COMPILED_SEGMENT, "."): tensor.detach().contiguous()
        for name, tensor in model.state_dict().items()
        if LORA_PARAMETER_MARKER in name
    }
    (partial_folder / LORA_WEIGHTS_FILE).write_bytes(safetensors.torch.save(lora_state))
    (partial_folder / LORA_CONFIG_FILE).write_text(model.lora_config.model_dump_json(indent=2), encoding="utf-8")
    copy_tokenizer_files(folders.tokenizer_folder, partial_folder)
    write_torch_file(optimizer.state_dict(), partial_folder / OPTIMIZER_STATE_FILE)
    write_torch_file(scheduler.state_dict(), partial_folder / SCHEDULER_STATE_FILE)
    state = json.dumps({TRAINING_STATE_STEP_KEY: step})
    (partial_folder / TRAINING_STATE_FILE).write_text(state, encoding="utf-8")
    # A rename cannot replace a folder that holds files, so delete the earlier folder of the step first.
    if checkpoint_folder.exists():
        shutil.rmtree(checkpoint_folder)
    partial_folder.rename(checkpoint_folder)
    update_newest_link(folders.voice_checkpoints_folder, checkpoint_folder)
    logger.info("Wrote checkpoint %s", checkpoint_folder)
    return checkpoint_folder


def read_checkpoint_step(checkpoint_folder: Path) -> int:
    """Read the number of optimizer steps that a checkpoint completed.

    Args:
        checkpoint_folder: Checkpoint folder.

    Returns:
        The step.

    Raises:
        CheckpointError: The training state file is missing or holds no whole step number.

    """
    state_path = checkpoint_folder / TRAINING_STATE_FILE
    try:
        step: object = json.loads(state_path.read_text(encoding="utf-8")).get(TRAINING_STATE_STEP_KEY)
    except (OSError, ValueError, AttributeError) as error:
        message = f"The training state {state_path} is missing or malformed"
        raise CheckpointError(message) from error
    if not isinstance(step, int):
        message = f"The training state {state_path} holds no whole step number"
        raise CheckpointError(message)
    return step


def read_checkpoint(
    model: VoxCPMModel, optimizer: Optimizer, scheduler: LRScheduler, voice_checkpoints_folder: Path
) -> int:
    """Restore the newest checkpoint of a voice into the model, optimizer, and scheduler.

    Args:
        model: Model without its DDP wrapper, already on its device.
        optimizer: Optimizer of the run.
        scheduler: Learning rate scheduler.
        voice_checkpoints_folder: Checkpoints of the voice.

    Returns:
        The step to resume from, or 0 without a checkpoint.

    Raises:
        CheckpointError: The newest checkpoint lacks its weights, or its weights do not fit.

    """
    newest_folder = find_newest_checkpoint(voice_checkpoints_folder)
    if newest_folder is None:
        return 0
    if not (newest_folder / LORA_WEIGHTS_FILE).is_file():
        message = f"The newest checkpoint {newest_folder.resolve()} has no {LORA_WEIGHTS_FILE}"
        raise CheckpointError(message)
    _, skipped_keys = model.read_lora_weights(newest_folder)
    if skipped_keys:
        message = (
            f"The newest checkpoint holds {len(skipped_keys)} weights that the model lacks, such as {skipped_keys[0]}"
        )
        raise CheckpointError(message)
    optimizer.load_state_dict(
        read_torch_file(newest_folder / OPTIMIZER_STATE_FILE, map_location="cpu", weights_only=True)
    )
    scheduler.load_state_dict(
        read_torch_file(newest_folder / SCHEDULER_STATE_FILE, map_location="cpu", weights_only=True)
    )
    step = read_checkpoint_step(newest_folder)
    logger.info("Resuming from step %d of %s", step, newest_folder.resolve())
    return step


def find_newest_checkpoint(voice_checkpoints_folder: Path) -> Path | None:
    """Find the newest checkpoint of a voice: the newest link target, or else the highest complete step folder.

    Without a link, only complete step folders count, so a half written folder never stops a run.

    Args:
        voice_checkpoints_folder: Checkpoints of one voice.

    Returns:
        The checkpoint folder, or None when no complete checkpoint exists.

    """
    newest_link = voice_checkpoints_folder / NEWEST_LINK
    if newest_link.is_dir():
        return newest_link.resolve()
    if not voice_checkpoints_folder.is_dir():
        return None
    steps = {
        _parse_step(folder.name): folder
        for folder in voice_checkpoints_folder.iterdir()
        if is_checkpoint_complete(folder)
    }
    numbered = {step: folder for step, folder in steps.items() if step is not None}
    return numbered[max(numbered)] if numbered else None


def list_voice_checkpoints(checkpoints_folder: Path, voices: Sequence[str]) -> dict[str, Path]:
    """List the newest checkpoint of each voice that has one.

    Args:
        checkpoints_folder: The checkpoints folder of the run, one folder per voice.
        voices: Voices to look for, in order.

    Returns:
        Newest checkpoint per voice, in the order of `voices`.

    Raises:
        CheckpointError: No voice has a checkpoint.

    """
    voice_checkpoints: dict[str, Path] = {}
    for voice in voices:
        checkpoint_folder = find_newest_checkpoint(checkpoints_folder / voice)
        if checkpoint_folder is not None:
            voice_checkpoints[voice] = checkpoint_folder
    if not voice_checkpoints:
        message = f"No voice of {', '.join(voices)} has a checkpoint in {checkpoints_folder}"
        raise CheckpointError(message)
    return voice_checkpoints


def read_lora_config(checkpoint_folder: Path) -> LoraConfig:
    """Read the LoRA config that a checkpoint stores as a flat JSON object.

    Args:
        checkpoint_folder: Checkpoint folder.

    Returns:
        The config.

    Raises:
        CheckpointError: The file is missing, is not a flat object of exactly the config fields, or holds an invalid
            value.

    """
    config_path = checkpoint_folder / LORA_CONFIG_FILE
    try:
        payload: object = json.loads(config_path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        message = f"The LoRA config {config_path} is missing or is not JSON"
        raise CheckpointError(message) from error
    if not isinstance(payload, dict) or set(cast("dict[str, object]", payload)) != set(LoraConfig.model_fields):
        message = (
            f"The LoRA config {config_path} is not a flat object of the fields {', '.join(LoraConfig.model_fields)}"
        )
        raise CheckpointError(message)
    try:
        return LoraConfig.model_validate(payload)
    except ValidationError as error:
        message = f"The LoRA config {config_path} holds an invalid value"
        raise CheckpointError(message) from error

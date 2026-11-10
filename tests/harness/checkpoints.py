"""Checkpoint folders on disk, and the folders and settings of tiny training runs."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

from config.voxcpm_1_5.data import TOKENIZER_FILES, TRAIN_MANIFEST_FILE
from schemas.voxcpm_1_5.training import LoraSettings, TrainingFolders, TrainingSettings
from config.voxcpm_1_5.checkpoints import (
    NEWEST_LINK,
    STEP_TEMPLATE,
    TRAINING_STATE_FILE,
    TRAINING_STATE_STEP_KEY,
)

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Sequence

TINY_BATCH_SIZE = 2
TINY_TOKEN_BUDGET = 1024
TINY_LEARNING_RATE = 1e-3
TINY_LORA_RANK = 2
TINY_LORA_ALPHA = 4
TINY_TARGET_MODULES = ("q_proj", "v_proj", "k_proj", "o_proj")


def write_tokenizer_files(folder: Path) -> Path:
    """Write a placeholder for each tokenizer file that a checkpoint copies.

    Args:
        folder: Where the files go; created when missing.

    Returns:
        The folder.

    """
    folder.mkdir(parents=True, exist_ok=True)
    for filename in TOKENIZER_FILES:
        (folder / filename).write_text("{}", encoding="utf-8")
    return folder


def create_checkpoint_tree(voice_checkpoints_folder: Path, steps: Sequence[int], newest_step: int | None) -> list[Path]:
    """Create step folders that hold only a training state, plus the newest link.

    Args:
        voice_checkpoints_folder: Checkpoints of one voice.
        steps: The step of each folder.
        newest_step: The step the newest link targets, or None for no link.

    Returns:
        The step folders, in `steps` order.

    """
    folders = [voice_checkpoints_folder / STEP_TEMPLATE.format(step=step) for step in steps]
    for step, folder in zip(steps, folders, strict=True):
        folder.mkdir(parents=True)
        (folder / TRAINING_STATE_FILE).write_text(json.dumps({TRAINING_STATE_STEP_KEY: step}), encoding="utf-8")
    if newest_step is not None:
        (voice_checkpoints_folder / NEWEST_LINK).symlink_to(STEP_TEMPLATE.format(step=newest_step))
    return folders


def build_training_folders(run_folder: Path, base_model_folder: Path, *, has_validation: bool) -> TrainingFolders:
    """Build the folders of a training run inside a run folder.

    Args:
        run_folder: Holds the manifests, tokenizer files, checkpoints, and events.
        base_model_folder: The base model folder.
        has_validation: Whether the run reads a validation manifest.

    Returns:
        The folders; validation reuses the training manifest.

    """
    train_manifest_path = run_folder / TRAIN_MANIFEST_FILE
    return TrainingFolders(
        base_model_folder=base_model_folder,
        train_manifest_path=train_manifest_path,
        val_manifest_path=train_manifest_path if has_validation else None,
        tokenizer_folder=write_tokenizer_files(run_folder / "tokenizer"),
        voice_checkpoints_folder=run_folder / "checkpoints",
        voice_events_folder=run_folder / "events",
    )


def build_training_settings(
    folders: TrainingFolders, voice: str, *, steps: int, checkpoint_interval: int
) -> TrainingSettings:
    """Build the settings of a tiny CPU run that logs every step.

    Args:
        folders: The run folders.
        voice: The voice to train.
        steps: Optimizer steps.
        checkpoint_interval: Steps between checkpoints.

    Returns:
        The settings.

    """
    return TrainingSettings(
        voice=voice,
        folders=folders,
        batch_size=TINY_BATCH_SIZE,
        accumulation_steps=1,
        loader_workers=0,
        steps=steps,
        learning_rate=TINY_LEARNING_RATE,
        weight_decay=0.0,
        warmup_steps=0,
        max_batch_tokens=TINY_TOKEN_BUDGET,
        log_interval=1,
        val_interval=steps,
        checkpoint_interval=checkpoint_interval,
        loss_diff_weight=1.0,
        loss_stop_weight=1.0,
    )


def build_tiny_lora_settings() -> LoraSettings:
    """Build small LoRA settings over every layer kind, without dropout.

    Returns:
        The settings.

    """
    return LoraSettings(
        enable_lm=True,
        enable_dit=True,
        enable_proj=True,
        rank=TINY_LORA_RANK,
        alpha=TINY_LORA_ALPHA,
        dropout=0.0,
        target_modules=TINY_TARGET_MODULES,
    )

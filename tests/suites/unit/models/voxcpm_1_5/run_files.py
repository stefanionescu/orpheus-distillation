"""Builders of the files a training run reads and leaves: the base model, the train flags, and checkpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING
from dataclasses import replace

from torch.optim import AdamW
from transformers import get_cosine_schedule_with_warmup

from tests.harness.voices import FIRST_VOICE
from tests.harness.manifests import write_clip_manifest
from tests.harness.checkpoints import TINY_LORA_RANK, TINY_BATCH_SIZE, TINY_LORA_ALPHA, build_training_folders
from config.models.voxcpm_1_5.data import TOKENIZER_FILES
from config.models.voxcpm_1_5.checkpoints import EVENTS_FOLDER, CHECKPOINTS_FOLDER
from tests.suites.unit.models.voxcpm_1_5.builders import (
    HUB_CONFIG_FILE,
    MODEL_SAMPLE_RATE,
    build_tiny_model,
    write_checkpoint_folder,
)
from src.train.models.voxcpm_1_5.training.checkpoints import write_checkpoint

if TYPE_CHECKING:
    from pathlib import Path

    from src.train.models.voxcpm_1_5.model.config import LoraConfig

# Room for the infer command's sample prompts, which the tiny tokenizer splits into one token per character.
LONG_TEXT_POSITIONS = 256
TRAIN_CLIP_SECONDS = 0.01


def write_base_model_folder(folder: Path) -> Path:
    """Write the tiny model as a downloaded base model: the loader files and every tokenizer file.

    The config gives the language model room for the sample prompts. The weights hold no rotary cache, so they still
    fit the longer config.

    Args:
        folder: The base model folder; created when missing.

    Returns:
        The folder.

    """
    folder.mkdir(parents=True, exist_ok=True)
    model = build_tiny_model()
    write_checkpoint_folder(model, folder)
    lm_config = model.config.lm_config.model_copy(update={"max_position_embeddings": LONG_TEXT_POSITIONS})
    config = model.config.model_copy(update={"lm_config": lm_config, "max_length": LONG_TEXT_POSITIONS})
    (folder / HUB_CONFIG_FILE).write_text(config.model_dump_json(), encoding="utf-8")
    for filename in TOKENIZER_FILES:
        tokenizer_path = folder / filename
        if not tokenizer_path.exists():
            tokenizer_path.write_text("{}", encoding="utf-8")
    return folder


def write_voice_checkpoint(checkpoints_folder: Path, voice: str, lora_config: LoraConfig, step: int) -> Path:
    """Write a tiny adapter checkpoint for one voice, as training writes it.

    Args:
        checkpoints_folder: The checkpoints folder of the run, one folder per voice; its parent holds the tokenizer.
        voice: The voice; it names its folder in the checkpoints folder.
        lora_config: The adapter's LoRA layers.
        step: The checkpoint step.

    Returns:
        The checkpoint folder, which the voice's newest link targets.

    """
    model = build_tiny_model(lora_config=lora_config)
    optimizer = AdamW(model.parameters())
    run_folders = build_training_folders(checkpoints_folder.parent, checkpoints_folder.parent, has_validation=False)
    folders = replace(run_folders, voice_checkpoints_folder=checkpoints_folder / voice)
    return write_checkpoint(model, optimizer, get_cosine_schedule_with_warmup(optimizer, 0, step), step, folders)


def write_train_flags(run_folder: Path, steps: int) -> tuple[list[str], Path]:
    """Write the inputs of a tiny train run of the first voice, and build the train command flags that read them.

    Args:
        run_folder: Holds the base model, the manifest, the tokenizer, the checkpoints, and the events.
        steps: Optimizer steps of the run.

    Returns:
        The flags, and the checkpoints of the voice that the run writes.

    """
    folders = build_training_folders(
        run_folder, write_base_model_folder(run_folder / "base_model"), has_validation=False
    )
    write_clip_manifest(
        folders.train_manifest_path, [(FIRST_VOICE, TRAIN_CLIP_SECONDS)] * TINY_BATCH_SIZE, MODEL_SAMPLE_RATE
    )
    flags = [
        "--voice",
        FIRST_VOICE.name,
        "--base-model-folder",
        str(folders.base_model_folder),
        "--train-manifest",
        str(folders.train_manifest_path),
        "--tokenizer-folder",
        str(folders.tokenizer_folder),
        "--checkpoints-folder",
        str(run_folder / CHECKPOINTS_FOLDER),
        "--events-folder",
        str(run_folder / EVENTS_FOLDER),
        "--steps",
        str(steps),
        "--batch-size",
        str(TINY_BATCH_SIZE),
        "--lora-rank",
        str(TINY_LORA_RANK),
        "--lora-alpha",
        str(TINY_LORA_ALPHA),
    ]
    return flags, run_folder / CHECKPOINTS_FOLDER / FIRST_VOICE.name

"""The folder that the publish command uploads.

The folder holds every file that the model loader reads, so a user needs nothing else.
"""

from __future__ import annotations

import shutil
from typing import TYPE_CHECKING
import logging

from config.hub import CARD_FILE
from config.voices import VOICES
from config.voxcpm_1_5.hub import SAMPLES_FOLDER, STAGING_FOLDER, ADAPTERS_FOLDER
from config.voxcpm_1_5.data import TOKENIZER_FILES
from config.voxcpm_1_5.checkpoints import LORA_CONFIG_FILE, TRAINING_STATE_FILE
from src.train.voxcpm_1_5.hub.card import format_card, format_files_table
from src.train.voxcpm_1_5.model.lora import LORA_WEIGHTS_FILE
from src.train.voxcpm_1_5.model.loader import AUDIO_VAE_FILE, MODEL_CONFIG_FILE, MODEL_WEIGHTS_FILES
from src.train.voxcpm_1_5.training.checkpoints import read_lora_config, read_checkpoint_step, list_voice_checkpoints

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Mapping

    from schemas.voxcpm_1_5.publish import PublishRequest

ADAPTER_FILES = (LORA_WEIGHTS_FILE, LORA_CONFIG_FILE, TRAINING_STATE_FILE)

logger = logging.getLogger(__name__)


class PublishError(Exception):
    """A checkpoint, the base model, or the run lacks a file that the repository needs."""


def _copy_required_file(source_path: Path, target_folder: Path) -> None:
    if not source_path.is_file():
        message = f"The published repository needs {source_path}, which does not exist"
        raise PublishError(message)
    shutil.copy2(source_path, target_folder / source_path.name)


def _copy_adapters(voice_checkpoints: Mapping[str, Path], staging_folder: Path) -> dict[str, int]:
    voice_steps: dict[str, int] = {}
    for voice, checkpoint_folder in voice_checkpoints.items():
        adapter_folder = staging_folder / ADAPTERS_FOLDER / voice
        adapter_folder.mkdir(parents=True)
        for filename in ADAPTER_FILES:
            _copy_required_file(checkpoint_folder / filename, adapter_folder)
        voice_steps[voice] = read_checkpoint_step(adapter_folder)
        logger.info("Staged the adapter of voice %s from %s", voice, checkpoint_folder)
    return voice_steps


def _copy_base_model(base_model_folder: Path, staging_folder: Path) -> None:
    weights_paths = [base_model_folder / filename for filename in MODEL_WEIGHTS_FILES]
    weights_path = next((path for path in weights_paths if path.is_file()), None)
    if weights_path is None:
        message = f"The base model {base_model_folder} holds none of {', '.join(MODEL_WEIGHTS_FILES)}"
        raise PublishError(message)
    for source_path in (
        weights_path,
        base_model_folder / MODEL_CONFIG_FILE,
        base_model_folder / AUDIO_VAE_FILE,
    ):
        _copy_required_file(source_path, staging_folder)


def _copy_samples(samples_folder: Path, staging_folder: Path) -> None:
    if not samples_folder.is_dir():
        message = f"The samples folder {samples_folder} does not exist"
        raise PublishError(message)
    target_folder = staging_folder / SAMPLES_FOLDER
    target_folder.mkdir()
    sample_paths = sorted(path for path in samples_folder.iterdir() if path.is_file())
    for sample_path in sample_paths:
        shutil.copy2(sample_path, target_folder / sample_path.name)
    logger.info("Staged %d samples from %s", len(sample_paths), samples_folder)


def write_model_card(staging_folder: Path, request: PublishRequest, voice_steps: Mapping[str, int]) -> Path:
    """Write the model card of the staged repository.

    A missing or malformed LoRA config of the first adapter raises CheckpointError.

    Args:
        staging_folder: Staged repository with the adapters and base model files.
        request: Run and repositories that the card names.
        voice_steps: Optimizer steps per staged voice, in table order.

    Returns:
        The card file.

    """
    first_adapter_folder = staging_folder / ADAPTERS_FOLDER / next(iter(voice_steps))
    weights_filename = next(filename for filename in MODEL_WEIGHTS_FILES if (staging_folder / filename).is_file())
    files_table = format_files_table(weights_filename, has_samples=(staging_folder / SAMPLES_FOLDER).is_dir())
    card_text = format_card(request, read_lora_config(first_adapter_folder), voice_steps, files_table)
    card_path = staging_folder / CARD_FILE
    card_path.write_text(card_text, encoding="utf-8")
    return card_path


def create_staging_folder(request: PublishRequest) -> Path:
    """Create the published repository folder beside the checkpoints, replacing an earlier one.

    A missing required file raises PublishError. No checkpoint of any voice, or a malformed state or LoRA config,
    raises CheckpointError.

    Args:
        request: Folders and repositories of the run.

    Returns:
        The staging folder.

    """
    staging_folder = request.checkpoints_folder.parent / STAGING_FOLDER
    if staging_folder.exists():
        shutil.rmtree(staging_folder)
    staging_folder.mkdir(parents=True)
    voice_steps = _copy_adapters(list_voice_checkpoints(request.checkpoints_folder, tuple(VOICES)), staging_folder)
    _copy_base_model(request.base_model_folder, staging_folder)
    for filename in TOKENIZER_FILES:
        _copy_required_file(request.tokenizer_folder / filename, staging_folder)
    if request.samples_folder is not None:
        _copy_samples(request.samples_folder, staging_folder)
    write_model_card(staging_folder, request, voice_steps)
    logger.info("Staged the repository %s in %s", request.output_repo, staging_folder)
    return staging_folder

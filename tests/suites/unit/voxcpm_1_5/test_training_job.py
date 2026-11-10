"""A training job reads the base model and a voice's manifest, trains its adapter, and resumes from a checkpoint."""

from __future__ import annotations

from typing import TYPE_CHECKING
from dataclasses import replace

import torch
import pytest
import safetensors.torch

from schemas.settings import TrainEnvironment
from tests.harness.voices import FIRST_VOICE, SECOND_VOICE
from config.voxcpm_1_5.data import VAL_MANIFEST_FILE
from tests.harness.manifests import write_clip_manifest
from tests.harness.checkpoints import build_training_folders, build_training_settings, build_tiny_lora_settings
from config.voxcpm_1_5.checkpoints import NEWEST_LINK, STEP_TEMPLATE
from src.train.voxcpm_1_5.model.lora import LORA_WEIGHTS_FILE
from src.train.voxcpm_1_5.training.job import TrainingDataError, run_training_job
from src.train.voxcpm_1_5.data.manifest import write_manifest
from tests.suites.unit.voxcpm_1_5.builders import (
    MODEL_SAMPLE_RATE,
    run_on_cpu,
    build_tiny_model,
    write_checkpoint_folder,
)
from src.train.voxcpm_1_5.training.checkpoints import read_checkpoint_step

if TYPE_CHECKING:
    from pathlib import Path

    from schemas.voxcpm_1_5.training import TrainingResult, TrainingSettings

CLIP_SECONDS = 0.01
SINGLE_PROCESS = TrainEnvironment(hf_token=None, world_size=1, local_rank=0)
MARKED_WEIGHT = 0.5
STEPS = 2
ONE_STEP_CHANGE = 0.01
"""Bounds the change that one AdamW step at the tiny learning rate makes, far below the gap to a fresh adapter."""


def _build_settings(tmp_path: Path, clip_count: int, steps: int, *, has_validation: bool) -> TrainingSettings:
    base_model_folder = tmp_path / "base_model"
    base_model_folder.mkdir(exist_ok=True)
    write_checkpoint_folder(build_tiny_model(), base_model_folder)
    folders = build_training_folders(tmp_path, base_model_folder, has_validation=has_validation)
    clips = [(FIRST_VOICE, CLIP_SECONDS)] * clip_count + [(SECOND_VOICE, CLIP_SECONDS)]
    write_clip_manifest(folders.train_manifest_path, clips, MODEL_SAMPLE_RATE)
    return build_training_settings(folders, FIRST_VOICE.name, steps=steps, checkpoint_interval=1)


def _read_weights(checkpoint_folder: Path) -> dict[str, torch.Tensor]:
    return safetensors.torch.load((checkpoint_folder / LORA_WEIGHTS_FILE).read_bytes())


def _run_job(settings: TrainingSettings) -> TrainingResult:
    with run_on_cpu():
        return run_training_job(settings, build_tiny_lora_settings(), SINGLE_PROCESS)


def test_job_links_last_checkpoint(tmp_path: Path) -> None:
    """The job links its last step's checkpoint as the newest, and reports no stop signal.

    Args:
        tmp_path: The test folder.

    """
    settings = _build_settings(tmp_path, 2, STEPS, has_validation=False)

    result = _run_job(settings)

    voice_checkpoints_folder = settings.folders.voice_checkpoints_folder
    assert result.stop_signal is None
    assert result.checkpoint_folder == voice_checkpoints_folder / STEP_TEMPLATE.format(step=STEPS)
    assert (voice_checkpoints_folder / NEWEST_LINK).resolve() == result.checkpoint_folder.resolve()
    assert read_checkpoint_step(result.checkpoint_folder) == STEPS


def test_job_resumes_from_checkpoint(tmp_path: Path) -> None:
    """A longer second run trains on from the newest checkpoint's weights and step, and leaves that checkpoint as is.

    Args:
        tmp_path: The test folder.

    """
    settings = _build_settings(tmp_path, 2, 1, has_validation=True)
    first_folder = _run_job(settings).checkpoint_folder
    marked = {name: torch.full_like(tensor, MARKED_WEIGHT) for name, tensor in _read_weights(first_folder).items()}
    (first_folder / LORA_WEIGHTS_FILE).write_bytes(safetensors.torch.save(marked))

    result = _run_job(replace(settings, steps=STEPS))

    resumed = _read_weights(result.checkpoint_folder)
    assert result.checkpoint_folder.name == STEP_TEMPLATE.format(step=STEPS)
    assert all(torch.allclose(resumed[name], tensor, atol=ONE_STEP_CHANGE) for name, tensor in marked.items())
    assert all(torch.equal(tensor, marked[name]) for name, tensor in _read_weights(first_folder).items())


def test_one_clip_too_few(tmp_path: Path) -> None:
    """A voice with fewer clips than one batch stops the job before any step.

    Args:
        tmp_path: The test folder.

    """
    with pytest.raises(TrainingDataError):
        _run_job(_build_settings(tmp_path, 1, 1, has_validation=False))


def test_speaker_manifest_raises(tmp_path: Path) -> None:
    """A manifest with Orpheus speakers in place of voices holds no clip of the voice, so the job stops.

    Args:
        tmp_path: The test folder.

    """
    settings = _build_settings(tmp_path, 2, 1, has_validation=False)
    manifest_path = settings.folders.train_manifest_path
    entries = write_clip_manifest(manifest_path, [(FIRST_VOICE, CLIP_SECONDS)] * 2, MODEL_SAMPLE_RATE)
    write_manifest([replace(entry, voice=FIRST_VOICE.speaker) for entry in entries], manifest_path)

    with pytest.raises(TrainingDataError):
        _run_job(settings)


def test_validation_without_voice_skipped(tmp_path: Path) -> None:
    """A validation manifest with no clip of the voice, as a small split leaves, trains without validation.

    Args:
        tmp_path: The test folder.

    """
    settings = _build_settings(tmp_path, 2, 1, has_validation=False)
    val_manifest_path = tmp_path / VAL_MANIFEST_FILE
    write_clip_manifest(val_manifest_path, [(SECOND_VOICE, CLIP_SECONDS)], MODEL_SAMPLE_RATE)
    folders = replace(settings.folders, val_manifest_path=val_manifest_path)

    result = _run_job(replace(settings, folders=folders))

    assert read_checkpoint_step(result.checkpoint_folder) == 1

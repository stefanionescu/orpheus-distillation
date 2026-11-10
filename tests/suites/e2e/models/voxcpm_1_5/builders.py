"""Builders for the VoxCPM 1.5 e2e tests: the GPU check, the base model, and short training runs."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING
from pathlib import Path

import torch
import pytest

from config.hub import REPO_TYPE_MODEL
from src.train.hub import download_snapshot
from schemas.settings import TrainEnvironment
from tests.harness.manifests import write_clip_manifest
from tests.harness.checkpoints import build_training_settings
from tests.harness.environment import CACHE_FOLDER_VARIABLE, read_variable
from config.models.voxcpm_1_5.hub import BASE_MODEL_REPO
from config.models.voxcpm_1_5.data import MANIFESTS_FOLDER, TRAIN_MANIFEST_FILE
from config.models.voxcpm_1_5.lora import (
    LORA_RANK,
    LORA_ALPHA,
    LORA_DROPOUT,
    LORA_ENABLE_LM,
    LORA_ENABLE_DIT,
    LORA_ENABLE_PROJ,
    LORA_TARGET_MODULES,
)
from config.models.voxcpm_1_5.model import MODEL_SAMPLE_RATE
from config.models.voxcpm_1_5.pipeline import CACHE_FOLDER
from schemas.models.voxcpm_1_5.training import LoraSettings, TrainingFolders
from config.models.voxcpm_1_5.checkpoints import EVENTS_FOLDER, CHECKPOINTS_FOLDER
from src.train.models.voxcpm_1_5.training.job import run_training_job
from src.train.models.voxcpm_1_5.model.forward import LOSS_DIFF_KEY, LOSS_STOP_KEY

if TYPE_CHECKING:
    from collections.abc import Iterable, Sequence

    from schemas.voice import Voice
    from schemas.models.voxcpm_1_5.training import TrainingResult, TrainingSettings

ROOT_FOLDER = Path(__file__).resolve().parents[4]
SINGLE_PROCESS = TrainEnvironment(hf_token=None, world_size=1, local_rank=0)

SMOKE_CLIP_COUNT = 4
SMOKE_CLIP_SECONDS = 1.0
SMOKE_STEPS = 10
CHECKPOINT_INTERVAL = 5
RESUMED_STEPS = 2
LOSS_WINDOW_STEPS = 3
"""The steps at each end of a run whose mean loss the smoke test compares, because each diffusion loss draws noise."""

SAMPLE_TRAIN_STEPS = 2
SAMPLE_MAX_PATCHES = 150
"""The most audio patches per sample clip, because a barely trained adapter can run without stopping."""

STEP_LINE = re.compile(r"Step (?P<step>\d+): (?P<metrics>.+)")


def assert_cuda_available() -> None:
    """Fail the test before any download when torch finds no CUDA device, because training needs one."""
    if not torch.cuda.is_available():
        pytest.fail("No CUDA device: the training e2e tests need a CUDA GPU, and torch finds none")


def download_base_model() -> Path:
    """Download the base model from the Hub, or reuse the cached copy.

    The cache is the variable's folder or the pipeline's default cache in the repository, so the e2e suite and the
    pipeline share one download.

    Returns:
        The base model folder.

    """
    cache_folder = read_variable(CACHE_FOLDER_VARIABLE)
    cache_path = ROOT_FOLDER / CACHE_FOLDER if cache_folder is None else Path(cache_folder)
    return download_snapshot(BASE_MODEL_REPO, REPO_TYPE_MODEL, cache_path, None)


def write_smoke_manifest(run_folder: Path, voices: Sequence[Voice]) -> Path:
    """Write a smoke run's training manifest: a few tone clips per voice at the model sample rate.

    Args:
        run_folder: The run folder.
        voices: The clip voices.

    Returns:
        The manifest file.

    """
    manifest_path = run_folder / MANIFESTS_FOLDER / TRAIN_MANIFEST_FILE
    clips = [(voice, SMOKE_CLIP_SECONDS) for voice in voices for _ in range(SMOKE_CLIP_COUNT)]
    write_clip_manifest(manifest_path, clips, MODEL_SAMPLE_RATE)
    return manifest_path


def build_smoke_settings(run_folder: Path, base_model_folder: Path, voice: Voice, steps: int) -> TrainingSettings:
    """Build a one-voice smoke run's settings: the pipeline folders, every step logged, no warmup.

    Args:
        run_folder: The run folder, with the manifest from `write_smoke_manifest`.
        base_model_folder: The base model folder, which also holds the tokenizer files.
        voice: The voice to train.
        steps: The step count at the end of the run.

    Returns:
        The settings.

    """
    folders = TrainingFolders(
        base_model_folder=base_model_folder,
        train_manifest_path=run_folder / MANIFESTS_FOLDER / TRAIN_MANIFEST_FILE,
        val_manifest_path=None,
        tokenizer_folder=base_model_folder,
        voice_checkpoints_folder=run_folder / CHECKPOINTS_FOLDER / voice.name,
        voice_events_folder=run_folder / EVENTS_FOLDER / voice.name,
    )
    return build_training_settings(folders, voice.name, steps=steps, checkpoint_interval=CHECKPOINT_INTERVAL)


def train_smoke_adapter(settings: TrainingSettings) -> TrainingResult:
    """Train an adapter with the train command's LoRA settings, in one GPU process.

    Args:
        settings: The run settings.

    Returns:
        The last checkpoint written.

    """
    lora = LoraSettings(
        enable_lm=LORA_ENABLE_LM,
        enable_dit=LORA_ENABLE_DIT,
        enable_proj=LORA_ENABLE_PROJ,
        rank=LORA_RANK,
        alpha=LORA_ALPHA,
        dropout=LORA_DROPOUT,
        target_modules=LORA_TARGET_MODULES,
    )
    return run_training_job(settings, lora, SINGLE_PROCESS)


def read_logged_losses(messages: Iterable[str]) -> dict[int, float]:
    """Read each step's summed losses from the training loop's metric lines.

    Args:
        messages: The loop's log messages.

    Returns:
        The loss of each logged step.

    """
    losses: dict[int, float] = {}
    for message in messages:
        line = STEP_LINE.fullmatch(message)
        if line is None:
            continue
        metrics = {name: value for name, _, value in (pair.partition("=") for pair in line["metrics"].split(", "))}
        if LOSS_DIFF_KEY in metrics and LOSS_STOP_KEY in metrics:
            losses[int(line["step"])] = float(metrics[LOSS_DIFF_KEY]) + float(metrics[LOSS_STOP_KEY])
    return losses

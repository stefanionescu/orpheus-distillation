"""The infer command writes one sample clip per sample prompt for every voice whose adapter trained."""

from __future__ import annotations

import math
from typing import TYPE_CHECKING, cast

import numpy as np
import soundfile

from src.train.cli import EXIT_SUCCESS
from tests.harness.voices import TABLE_VOICES
from config.models.voxcpm_1_5.hub import SAMPLES_FOLDER
from config.models.voxcpm_1_5.model import MODEL_SAMPLE_RATE
from config.models.voxcpm_1_5.samples import SAMPLE_PROMPTS, SAMPLE_INDEX_START, SAMPLE_FILE_TEMPLATE
from config.models.voxcpm_1_5.inference import TARGET_PEAK
from config.models.voxcpm_1_5.checkpoints import CHECKPOINTS_FOLDER
from src.train.models.voxcpm_1_5.__main__ import main as run_command
from tests.suites.e2e.models.voxcpm_1_5.builders import (
    SAMPLE_MAX_PATCHES,
    SAMPLE_TRAIN_STEPS,
    download_base_model,
    train_smoke_adapter,
    build_smoke_settings,
    write_smoke_manifest,
    assert_cuda_available,
)

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Callable

    from numpy.typing import NDArray

PEAK_TOLERANCE = 1e-3
"""How far the peak read back from a 16-bit clip can sit from the peak that the synthesizer scaled to."""

read_audio_file = cast("Callable[..., tuple[NDArray[np.float32], int]]", soundfile.read)


def _read_clip(sample_path: Path) -> tuple[int, float]:
    audio, sample_rate = read_audio_file(sample_path, dtype="float32")
    return sample_rate, float(np.abs(audio).max(initial=0.0))


def test_infer_writes_voice_samples(tmp_path: Path) -> None:
    """Each voice with a checkpoint gets a clip of each sample prompt at the model sample rate that holds sound.

    The synthesizer scales speech to its target peak and leaves silence silent, so a clip at the target peak holds
    the model's speech.

    Args:
        tmp_path: The run folder.

    """
    assert_cuda_available()
    base_model_folder = download_base_model()
    write_smoke_manifest(tmp_path, TABLE_VOICES)
    for voice in TABLE_VOICES:
        train_smoke_adapter(build_smoke_settings(tmp_path, base_model_folder, voice, SAMPLE_TRAIN_STEPS))
    samples_folder = tmp_path / SAMPLES_FOLDER
    flags = ["--checkpoints-folder", str(tmp_path / CHECKPOINTS_FOLDER), "--base-model-folder", str(base_model_folder)]

    exit_code = run_command(
        ["infer", *flags, "--samples-folder", str(samples_folder), "--max-patches", str(SAMPLE_MAX_PATCHES)]
    )

    assert exit_code == EXIT_SUCCESS
    indices = range(SAMPLE_INDEX_START, SAMPLE_INDEX_START + len(SAMPLE_PROMPTS))
    names = [SAMPLE_FILE_TEMPLATE.format(voice=voice.name, index=index) for voice in TABLE_VOICES for index in indices]
    clips = [_read_clip(samples_folder / name) for name in names]
    assert sorted(path.name for path in samples_folder.iterdir()) == sorted(names)
    assert [sample_rate for sample_rate, _ in clips] == [MODEL_SAMPLE_RATE] * len(names)
    assert all(math.isclose(peak, TARGET_PEAK, abs_tol=PEAK_TOLERANCE) for _, peak in clips)

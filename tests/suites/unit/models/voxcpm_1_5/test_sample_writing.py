"""The infer stage writes one clip per prompt for each voice that has a checkpoint, and skips the others."""

from __future__ import annotations

import wave
from typing import TYPE_CHECKING

from tests.harness.voices import FIRST_VOICE, SECOND_VOICE
from config.models.voxcpm_1_5.samples import SAMPLE_INDEX_START, SAMPLE_FILE_TEMPLATE
from schemas.models.voxcpm_1_5.inference import SampleSettings
from tests.suites.unit.models.voxcpm_1_5.builders import (
    MODEL_SAMPLE_RATE,
    SHORT_MAX_PATCHES,
    run_on_cpu,
    build_lora_config,
    build_sampler_settings,
)
from src.train.models.voxcpm_1_5.inference.samples import write_samples
from tests.suites.unit.models.voxcpm_1_5.run_files import write_voice_checkpoint, write_base_model_folder

if TYPE_CHECKING:
    from pathlib import Path

    from schemas.voice import Voice

PROMPTS = ("hello there", "good night")
VOICE_NAMES = (FIRST_VOICE.name, SECOND_VOICE.name)


def _write_samples(tmp_path: Path, trained_voices: tuple[Voice, ...]) -> list[Path]:
    checkpoints_folder = tmp_path / "run" / "checkpoints"
    for voice in trained_voices:
        write_voice_checkpoint(checkpoints_folder, voice.name, build_lora_config(), 1)
    settings = SampleSettings(voices=VOICE_NAMES, prompts=PROMPTS, sampler=build_sampler_settings(SHORT_MAX_PATCHES))
    with run_on_cpu():
        return write_samples(
            checkpoints_folder, write_base_model_folder(tmp_path / "base_model"), tmp_path / "samples", settings
        )


def _build_sample_names(voice: Voice) -> list[str]:
    return [
        SAMPLE_FILE_TEMPLATE.format(voice=voice.name, index=index)
        for index in range(SAMPLE_INDEX_START, SAMPLE_INDEX_START + len(PROMPTS))
    ]


def test_clip_per_voice_prompt(tmp_path: Path) -> None:
    """Each trained voice reads every prompt into its own WAV file at the model's sample rate.

    Args:
        tmp_path: The test folder.

    """
    sample_paths = _write_samples(tmp_path, (FIRST_VOICE, SECOND_VOICE))

    assert [path.name for path in sample_paths] == _build_sample_names(FIRST_VOICE) + _build_sample_names(SECOND_VOICE)
    for sample_path in sample_paths:
        with wave.open(str(sample_path)) as clip:
            assert clip.getframerate() == MODEL_SAMPLE_RATE


def test_untrained_voice_skipped(tmp_path: Path) -> None:
    """A voice without a checkpoint gets no clip, and the trained voice gets all its clips.

    Args:
        tmp_path: The test folder.

    """
    sample_paths = _write_samples(tmp_path, (SECOND_VOICE,))

    assert [path.name for path in sample_paths] == _build_sample_names(SECOND_VOICE)

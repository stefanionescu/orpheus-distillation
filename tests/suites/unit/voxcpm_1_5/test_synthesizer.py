"""The synthesizer scales audio to a peak and refuses adapters that do not fit."""

from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np
import torch
import pytest

from tests.harness.voices import FIRST_VOICE
from tests.suites.unit.voxcpm_1_5.builders import (
    SHORT_MAX_PATCHES,
    run_on_cpu,
    build_tiny_model,
    build_lora_config,
    write_lora_weights,
    build_sampler_settings,
)
from tests.suites.unit.voxcpm_1_5.run_files import write_voice_checkpoint
from src.train.voxcpm_1_5.inference.synthesizer import Synthesizer, AdapterError, scale_to_peak

if TYPE_CHECKING:
    from pathlib import Path

PEAK = 0.9
OTHER_RANK = 4


def _build_synthesizer(max_patches: int) -> Synthesizer:
    with run_on_cpu():
        model = build_tiny_model(lora_config=build_lora_config()).eval()
    return Synthesizer(model, build_sampler_settings(max_patches))


def test_peak_reaches_target() -> None:
    """The loudest sample reaches the target peak, and the others keep their ratio to it."""
    audio = np.array([0.1, -0.5, 0.25], dtype=np.float32)

    scaled = scale_to_peak(audio, PEAK)

    assert np.allclose(scaled, audio * (PEAK / 0.5))
    assert scaled.dtype == np.float32


def test_silence_stays_silent() -> None:
    """Silence has no peak to scale, so it comes back as silence, not division noise."""
    silence = np.zeros(4, dtype=np.float32)

    assert np.array_equal(scale_to_peak(silence, PEAK), silence)


def test_other_lora_settings_raise(tmp_path: Path) -> None:
    """The synthesizer refuses an adapter of another LoRA rank before it reads the weights.

    Args:
        tmp_path: The test folder.

    """
    other_config = build_lora_config().model_copy(update={"r": OTHER_RANK})
    checkpoint_folder = write_voice_checkpoint(tmp_path / "checkpoints", FIRST_VOICE.name, other_config, 1)

    with pytest.raises(AdapterError, match="LoRA settings"):
        _build_synthesizer(SHORT_MAX_PATCHES).read_adapter(checkpoint_folder)


def test_unknown_weights_raise(tmp_path: Path) -> None:
    """The synthesizer refuses an adapter with weights the model lacks, which belongs to another model.

    Args:
        tmp_path: The test folder.

    """
    checkpoint_folder = write_voice_checkpoint(tmp_path / "checkpoints", FIRST_VOICE.name, build_lora_config(), 1)
    write_lora_weights(
        build_tiny_model(lora_config=build_lora_config()), checkpoint_folder, {"x.lora_A": torch.zeros(1)}
    )

    with pytest.raises(AdapterError, match="weights that the model lacks"):
        _build_synthesizer(SHORT_MAX_PATCHES).read_adapter(checkpoint_folder)

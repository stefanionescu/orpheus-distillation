"""The vendored VoxCPM layers match the recorded outputs on seeded CPU inputs."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

import torch
from torch import nn
import pytest

from tests.suites.unit.models.voxcpm_1_5.builders import (
    LORA_RANK,
    LORA_ALPHA,
    PATCH_SIZE,
    LORA_B_OFFSET,
    QUANTIZER_DIM,
    GUIDANCE_SCALE,
    WAVEFORM_SCALE,
    QUANTIZER_SCALE,
    WAVEFORM_OFFSET,
    SOLVER_TIMESTEPS,
    WAVEFORM_SAMPLES,
    MODEL_SAMPLE_RATE,
    LINEAR_IN_FEATURES,
    LINEAR_INPUT_OFFSET,
    LINEAR_OUT_FEATURES,
    QUANTIZER_LATENT_DIM,
    QUANTIZER_INPUT_OFFSET,
    build_tiny_model,
    reset_random_state,
    build_seeded_tensor,
    build_sampler_inputs,
    build_audio_vae_config,
)
from tests.suites.unit.models.voxcpm_1_5.recording import validate_recording
from src.train.models.voxcpm_1_5.model.modules.layers.lora import LoraLinear
from src.train.models.voxcpm_1_5.model.modules.audiovae.audiovae import AudioVae
from src.train.models.voxcpm_1_5.model.modules.layers.scalar_quantization import ScalarQuantizationLayer

if TYPE_CHECKING:
    from collections.abc import Callable


def _build_lora_linear() -> LoraLinear:
    reset_random_state()
    layer = LoraLinear(base=nn.Linear(LINEAR_IN_FEATURES, LINEAR_OUT_FEATURES), r=LORA_RANK, alpha=LORA_ALPHA)
    with torch.no_grad():
        layer.lora_B.copy_(build_seeded_tensor(tuple(layer.lora_B.shape), LORA_B_OFFSET))
    return layer


def _build_linear_input() -> torch.Tensor:
    return build_seeded_tensor((3, LINEAR_IN_FEATURES), LINEAR_INPUT_OFFSET)


def _build_quantizer() -> ScalarQuantizationLayer:
    reset_random_state()
    return ScalarQuantizationLayer(QUANTIZER_DIM, QUANTIZER_DIM, latent_dim=QUANTIZER_LATENT_DIM, scale=QUANTIZER_SCALE)


def _build_audio_vae() -> AudioVae:
    reset_random_state()
    return AudioVae(config=build_audio_vae_config())


def _build_waveform() -> torch.Tensor:
    return build_seeded_tensor((1, 1, WAVEFORM_SAMPLES), WAVEFORM_OFFSET) * WAVEFORM_SCALE


def test_sampler_matches_recording() -> None:
    """The sampler draws seeded noise, sway-samples the timesteps, and solves with CFG-Zero* to the recorded patch."""
    decoder = build_tiny_model().feat_decoder
    inputs = build_sampler_inputs()

    reset_random_state()
    with torch.inference_mode():
        patch = decoder(
            mu=inputs.mu,
            n_timesteps=SOLVER_TIMESTEPS,
            patch_size=PATCH_SIZE,
            cond=inputs.cond,
            guidance_scale=GUIDANCE_SCALE,
        )

    assert validate_recording(patch, "cfm_sample") == []


def test_lora_linear_adds_update() -> None:
    """An enabled LoRA layer adds its scaled low-rank product to the wrapped linear output."""
    assert validate_recording(_build_lora_linear()(_build_linear_input()), "lora_linear") == []


def test_quantizer_rounds_latents() -> None:
    """The quantizer rounds the projected latents to its scale's levels and projects them back."""
    quantizer = _build_quantizer().eval()

    output = quantizer(build_seeded_tensor((3, QUANTIZER_DIM), QUANTIZER_INPUT_OFFSET))

    assert validate_recording(output, "scalar_quantization") == []


def test_quantizer_passes_gradient() -> None:
    """In training mode the rounding passes the gradient through unchanged, so the input gets the recorded gradient."""
    quantizer = _build_quantizer().train()
    hidden = build_seeded_tensor((3, QUANTIZER_DIM), QUANTIZER_INPUT_OFFSET).requires_grad_()

    run_backward = cast("Callable[[], None]", (quantizer(hidden) ** 2).sum().backward)
    run_backward()

    assert hidden.grad is not None
    assert validate_recording(hidden.grad, "scalar_quantization_input_gradient") == []


def test_vae_encode_matches_recording() -> None:
    """Encoding pads the waveform to a whole hop and returns the recorded latent frames."""
    with torch.no_grad():
        latents = _build_audio_vae().encode(_build_waveform(), MODEL_SAMPLE_RATE)

    assert validate_recording(latents, "audio_vae_encode") == []


def test_vae_decode_matches_recording() -> None:
    """Decoding the waveform's latents returns the recorded waveform."""
    audio_vae = _build_audio_vae()

    with torch.no_grad():
        waveform = audio_vae.decode(audio_vae.encode(_build_waveform(), MODEL_SAMPLE_RATE))

    assert validate_recording(waveform, "audio_vae_decode") == []


def test_vae_rejects_wrong_rate() -> None:
    """Encoding at a sample rate other than the VAE's raises instead of giving wrong latents."""
    with pytest.raises(ValueError, match="Hz"):
        _build_audio_vae().encode(_build_waveform(), MODEL_SAMPLE_RATE // 2)

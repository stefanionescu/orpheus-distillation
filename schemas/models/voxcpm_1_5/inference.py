"""Settings of the infer command."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SamplerSettings:
    """Sampler settings of one inference call.

    Attributes:
        guidance_scale: Classifier-free guidance scale.
        timesteps: Diffusion steps per patch.
        max_patches: Most audio patches that one call produces.

    """

    guidance_scale: float
    timesteps: int
    max_patches: int


@dataclass(frozen=True)
class SampleSettings:
    """What the infer command writes for each voice.

    Attributes:
        voices: Voices to synthesize.
        prompts: Texts that each voice reads.
        sampler: Sampler settings of each call.

    """

    voices: tuple[str, ...]
    prompts: tuple[str, ...]
    sampler: SamplerSettings

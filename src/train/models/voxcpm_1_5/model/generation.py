"""Speech generation from text."""

from __future__ import annotations

from typing import TYPE_CHECKING
from dataclasses import replace

import torch

from src.train.models.voxcpm_1_5.model.dtypes import select_dtype
from src.train.models.voxcpm_1_5.model.inference import DecodeInputs, VoxCPMInferenceMixin

if TYPE_CHECKING:
    from schemas.models.voxcpm_1_5.inference import SamplerSettings

# Cap the audio by text length so a missed stop cannot run to `max_patches`.
PATCHES_PER_TOKEN = 6.0
EXTRA_PATCHES = 10


class VoxCPMGenerationMixin(VoxCPMInferenceMixin):
    """Speech generation in one decoding run, without a voice prompt."""

    @torch.inference_mode()
    def generate(self, target_text: str, settings: SamplerSettings) -> torch.Tensor:
        """Generate the waveform of one text.

        Args:
            target_text: Text to speak.
            settings: Sampler settings. A cap from the text length can lower `max_patches`.

        Returns:
            Waveform at the audio VAE sample rate, shaped (1, samples), on the CPU.

        """
        inputs = self._prepare_generation(target_text)
        target_text_length = len(self.text_tokenizer(target_text))
        max_len = min(int(target_text_length * PATCHES_PER_TOKEN + EXTRA_PATCHES), settings.max_patches)
        latent_pred = self._decode_until_stop(inputs, replace(settings, max_patches=max_len))
        return self.audio_vae.decode(latent_pred.to(torch.float32)).squeeze(1).cpu()

    def _prepare_generation(self, target_text: str) -> DecodeInputs:
        text_token = torch.tensor(self.text_tokenizer(target_text), dtype=torch.long)
        text_token = torch.cat(
            [
                text_token,
                torch.tensor([self.audio_start_token], dtype=torch.int32, device=text_token.device),
            ],
            dim=-1,
        )
        text_length = text_token.shape[0]
        audio_feat = torch.zeros(
            (text_length, self.patch_size, self.audio_vae.latent_dim),
            dtype=torch.float32,
            device=text_token.device,
        )
        text_mask = torch.ones(text_length).type(torch.int32).to(text_token.device)
        audio_mask = torch.zeros(text_length).type(torch.int32).to(text_token.device)
        return DecodeInputs(
            text_tokens=text_token.unsqueeze(0).to(self.device),
            text_mask=text_mask.unsqueeze(0).to(self.device),
            audio_feats=audio_feat.unsqueeze(0).to(self.device).to(select_dtype(self.config.dtype)),
            audio_mask=audio_mask.unsqueeze(0).to(self.device),
        )

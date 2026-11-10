"""Audio VAE that maps waveforms to latent frames and back."""

from __future__ import annotations

import math
from typing import TYPE_CHECKING, cast

from torch import nn
from pydantic import BaseModel
from torch.nn import functional

from src.train.voxcpm_1_5.model.modules.audiovae.decoder import CausalDecoder
from src.train.voxcpm_1_5.model.modules.audiovae.encoder import CausalEncoder

if TYPE_CHECKING:
    from collections.abc import Callable

    import torch

UNCHANNELED_NDIM = 2


class AudioVaeConfig(BaseModel):
    """Audio VAE config, under `audio_vae_config` in `config.json`.

    Attributes:
        encoder_dim: Channels of the first encoder convolution.
        encoder_rates: Downsampling factor per encoder block; their product is the hop length.
        latent_dim: Size of one latent frame.
        decoder_dim: Channels of the first decoder convolution.
        decoder_rates: Upsampling factor per decoder block.
        depthwise: Whether the convolutions are depthwise.
        sample_rate: Waveform sample rate.
        use_noise_block: Whether the decoder adds learned noise.

    """

    encoder_dim: int = 128
    encoder_rates: list[int] = [2, 5, 8, 8]
    latent_dim: int = 64
    decoder_dim: int = 1536
    decoder_rates: list[int] = [8, 8, 5, 2]
    depthwise: bool = True
    sample_rate: int = 16000
    use_noise_block: bool = False


class AudioVae(nn.Module):
    """Causal audio VAE with one latent frame per hop of samples."""

    def __init__(self, config: AudioVaeConfig | None = None) -> None:
        """Build the encoder and the decoder.

        Args:
            config: VAE config, or None for the defaults.

        """
        cast("Callable[[], None]", super().__init__)()
        if config is None:
            config = AudioVaeConfig()
        self.encoder_dim = config.encoder_dim
        self.encoder_rates = config.encoder_rates
        self.decoder_dim = config.decoder_dim
        self.decoder_rates = config.decoder_rates
        self.depthwise = config.depthwise
        self.use_noise_block = config.use_noise_block

        self.latent_dim = config.latent_dim
        self.hop_length = math.prod(config.encoder_rates)
        self.encoder = CausalEncoder(
            config.encoder_dim, config.latent_dim, tuple(config.encoder_rates), depthwise=config.depthwise
        )
        self.decoder = CausalDecoder(
            config.latent_dim,
            config.decoder_dim,
            config.decoder_rates,
            depthwise=config.depthwise,
            use_noise_block=config.use_noise_block,
        )
        self.sample_rate = config.sample_rate
        self.chunk_size = math.prod(config.encoder_rates)

    def decode(self, z: torch.Tensor) -> torch.Tensor:
        """Decode latent frames to a waveform.

        Args:
            z: Latents, shaped (batch, latent_dim, frames).

        Returns:
            Waveform, shaped (batch, 1, frames * hop_length).

        """
        return cast("torch.Tensor", self.decoder(z))

    def encode(self, audio_data: torch.Tensor, sample_rate: int) -> torch.Tensor:
        """Pad a waveform on the right to a whole hop and encode it to its latent means.

        Args:
            audio_data: Waveform, shaped (batch, samples) or (batch, 1, samples).
            sample_rate: Waveform sample rate; it must match the VAE.

        Returns:
            Latents, shaped (batch, latent_dim, frames).

        Raises:
            ValueError: When the sample rate differs from the VAE rate.

        """
        if sample_rate != self.sample_rate:
            message = f"Expected audio at {self.sample_rate} Hz, got {sample_rate} Hz"
            raise ValueError(message)
        if audio_data.ndim == UNCHANNELED_NDIM:
            audio_data = audio_data.unsqueeze(1)
        length = audio_data.shape[-1]
        right_pad = int(math.ceil(length / self.hop_length) * self.hop_length - length)
        audio_data = functional.pad(audio_data, (0, right_pad))
        return cast("dict[str, torch.Tensor]", self.encoder(audio_data))["mu"]

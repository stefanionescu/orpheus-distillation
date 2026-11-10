"""Local diffusion transformer that estimates the velocity of an audio patch."""

from __future__ import annotations

import math
from typing import TYPE_CHECKING, cast, override

import torch
from torch import nn

from src.train.voxcpm_1_5.model.modules.minicpm4.model import MiniCpmModel

if TYPE_CHECKING:
    from collections.abc import Callable

    from src.train.voxcpm_1_5.model.modules.minicpm4.config import MiniCpmConfig

TIMESTEP_SCALE = 1000
SINUSOID_BASE = 10000


class SinusoidalPosEmb(nn.Module):
    """Sinusoidal timestep embedding: sines, then cosines, over geometric frequencies."""

    def __init__(self, dim: int) -> None:
        """Store the embedding size.

        Args:
            dim: Embedding size; it must be even.

        Raises:
            ValueError: When the size is odd.

        """
        cast("Callable[[], None]", super().__init__)()
        self.dim = dim
        if self.dim % 2 != 0:
            message = "SinusoidalPosEmb requires dim to be even"
            raise ValueError(message)

    @override
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Embed timesteps.

        Args:
            x: Timesteps, shaped (batch,) or a scalar.

        Returns:
            Embeddings, shaped (batch, dim).

        """
        if x.ndim < 1:
            x = x.unsqueeze(0)
        half_dim = self.dim // 2
        log_scale = math.log(SINUSOID_BASE) / (half_dim - 1)
        emb = torch.exp(torch.arange(half_dim, dtype=x.dtype, device=x.device) * -log_scale)
        emb = TIMESTEP_SCALE * x.unsqueeze(1) * emb.unsqueeze(0)
        return torch.cat((emb.sin(), emb.cos()), dim=-1)


class TimestepEmbedding(nn.Module):
    """A two-layer SiLU network on a timestep embedding."""

    def __init__(self, in_channels: int, time_embed_dim: int) -> None:
        """Build the two layers.

        Args:
            in_channels: Size of the sinusoidal embedding.
            time_embed_dim: Hidden and output size.

        """
        cast("Callable[[], None]", super().__init__)()
        self.linear_1 = nn.Linear(in_channels, time_embed_dim, bias=True)
        self.act = nn.SiLU()
        self.linear_2 = nn.Linear(time_embed_dim, time_embed_dim, bias=True)

    @override
    def forward(self, sample: torch.Tensor) -> torch.Tensor:
        """Transform a timestep embedding.

        Args:
            sample: Embedding, shaped (batch, in_channels).

        Returns:
            Output, shaped (batch, time_embed_dim).

        """
        return cast("torch.Tensor", self.linear_2(self.act(self.linear_1(sample))))


class VoxCPMLocDit(nn.Module):
    """Diffusion estimator: a bidirectional MiniCPM over the timestep, the previous patch, and the noisy patch."""

    def __init__(self, config: MiniCpmConfig, in_channels: int = 64) -> None:
        """Build the projections, the timestep embeddings, and the transformer.

        Args:
            config: Transformer config, with no token embedding.
            in_channels: Size of one latent frame.

        Raises:
            ValueError: When the config has a vocabulary.

        """
        cast("Callable[[], None]", super().__init__)()
        self.in_channels = in_channels
        self.out_channels = in_channels
        self.config = config

        self.in_proj = nn.Linear(in_channels, config.hidden_size, bias=True)
        self.cond_proj = nn.Linear(in_channels, config.hidden_size, bias=True)
        self.out_proj = nn.Linear(config.hidden_size, self.out_channels, bias=True)

        self.time_embeddings = SinusoidalPosEmb(config.hidden_size)
        self.time_mlp = TimestepEmbedding(in_channels=config.hidden_size, time_embed_dim=config.hidden_size)
        self.delta_time_mlp = TimestepEmbedding(in_channels=config.hidden_size, time_embed_dim=config.hidden_size)

        if config.vocab_size != 0:
            message = "vocab_size must be 0 for local DiT"
            raise ValueError(message)
        self.decoder = MiniCpmModel(config)

    @override
    def forward(
        self,
        x: torch.Tensor,
        mu: torch.Tensor,
        t: torch.Tensor,
        cond: torch.Tensor,
        dt: torch.Tensor,
    ) -> torch.Tensor:
        """Estimate the velocity of a noisy patch.

        Args:
            x: Noisy patch, shaped (batch, in_channels, patch_size).
            mu: Language model state that conditions the patch, shaped (batch, hidden_size).
            t: Timestep per sample, shaped (batch,).
            cond: Previous patch, shaped (batch, in_channels, prefix_length).
            dt: Step to the mean-velocity target in mean mode, else zero, shaped (batch,).

        Returns:
            Velocity, shaped like `x`.

        """
        x = self.in_proj(x.transpose(1, 2).contiguous())

        cond = self.cond_proj(cond.transpose(1, 2).contiguous())
        prefix = cond.size(1)

        t = self.time_embeddings(t).to(x.dtype)
        t = self.time_mlp(t)
        dt = self.time_embeddings(dt).to(x.dtype)
        dt = self.delta_time_mlp(dt)
        t = t + dt

        x = torch.cat([(mu + t).unsqueeze(1), cond, x], dim=1)
        hidden, _ = self.decoder(x, is_causal=False)
        hidden = hidden[:, prefix + 1 :, :]
        hidden = self.out_proj(hidden)
        return hidden.transpose(1, 2).contiguous()

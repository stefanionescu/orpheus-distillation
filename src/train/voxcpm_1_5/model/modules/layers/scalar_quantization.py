"""Scalar quantization bottleneck between the base and residual language models."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast, override

import torch
from torch import nn

if TYPE_CHECKING:
    from collections.abc import Callable


class ScalarQuantizationLayer(nn.Module):
    """Scalar quantization with a straight-through gradient."""

    def __init__(self, in_dim: int, out_dim: int, latent_dim: int = 64, scale: int = 9) -> None:
        """Build the projections into and out of the bottleneck.

        Args:
            in_dim: Input size.
            out_dim: Output size.
            latent_dim: Bottleneck size.
            scale: Quantization levels on each side of zero.

        """
        cast("Callable[[], None]", super().__init__)()
        self.in_dim = in_dim
        self.out_dim = out_dim
        self.latent_dim = latent_dim
        self.scale = scale

        self.in_proj = nn.Linear(in_dim, latent_dim)
        self.out_proj = nn.Linear(latent_dim, out_dim)

    @override
    def forward(self, hidden: torch.Tensor) -> torch.Tensor:
        """Project to the bottleneck, round to the levels, and project back.

        Args:
            hidden: Input, with `in_dim` as its last dimension.

        Returns:
            Output, with `out_dim` as its last dimension.

        """
        hidden = self.in_proj(hidden)
        hidden = torch.tanh(hidden)

        if self.training:
            quantized = torch.round(hidden * self.scale) / self.scale
            hidden = hidden + (quantized - hidden).detach()
        else:
            hidden = torch.round(hidden * self.scale) / self.scale

        return cast("torch.Tensor", self.out_proj(hidden))

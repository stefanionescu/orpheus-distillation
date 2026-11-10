"""Causal encoder of the audio VAE."""

from __future__ import annotations

import math
from typing import TYPE_CHECKING, cast, override

from torch import nn

from src.train.models.voxcpm_1_5.model.modules.audiovae.layers import (
    SnakeActivation,
    CausalResidualUnit,
    build_causal_conv,
)

if TYPE_CHECKING:
    from collections.abc import Callable

    import torch


class CausalEncoder(nn.Module):
    """Downsampling blocks that double the channels, then the latent mean and log variance."""

    def __init__(self, d_model: int, latent_dim: int, strides: tuple[int, ...], *, depthwise: bool) -> None:
        """Build the encoder.

        Args:
            d_model: Channels of the first convolution; each block doubles them.
            latent_dim: Size of one latent frame.
            strides: Downsampling factor per block.
            depthwise: Whether the blocks use depthwise convolutions.

        """
        cast("Callable[[], None]", super().__init__)()
        block: list[nn.Module] = [build_causal_conv(1, d_model, kernel_size=7, padding=3)]
        for stride in strides:
            d_model *= 2
            groups = d_model // 2 if depthwise else 1
            block += [CausalEncoderBlock(output_dim=d_model, stride=stride, groups=groups)]

        self.fc_mu = build_causal_conv(d_model, latent_dim, kernel_size=3, padding=1)
        self.fc_logvar = build_causal_conv(d_model, latent_dim, kernel_size=3, padding=1)
        self.block = nn.Sequential(*block)

    @override
    def forward(self, x: torch.Tensor) -> dict[str, torch.Tensor]:
        """Encode a waveform.

        Args:
            x: Waveform, shaped (batch, 1, samples), padded to a whole hop.

        Returns:
            Last hidden state under `hidden_state`, latent mean under `mu`, and latent log variance under
            `logvar`, each shaped (batch, channels, frames).

        """
        hidden_state = cast("torch.Tensor", self.block(x))
        return {
            "hidden_state": hidden_state,
            "mu": cast("torch.Tensor", self.fc_mu(hidden_state)),
            "logvar": cast("torch.Tensor", self.fc_logvar(hidden_state)),
        }


class CausalEncoderBlock(nn.Module):
    """Dilated residual units on half the output channels, then a strided downsampling convolution."""

    def __init__(self, *, output_dim: int, stride: int, groups: int) -> None:
        """Build the block.

        Args:
            output_dim: Output channels; the block takes half as many in.
            stride: Downsampling factor.
            groups: Convolution groups of the residual units.

        """
        cast("Callable[[], None]", super().__init__)()
        input_dim = output_dim // 2
        self.block = nn.Sequential(
            CausalResidualUnit(input_dim, dilation=1, groups=groups),
            CausalResidualUnit(input_dim, dilation=3, groups=groups),
            CausalResidualUnit(input_dim, dilation=9, groups=groups),
            SnakeActivation(input_dim),
            build_causal_conv(
                input_dim,
                output_dim,
                kernel_size=2 * stride,
                stride=stride,
                padding=math.ceil(stride / 2),
            ),
        )

    @override
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Downsample.

        Args:
            x: Input, shaped (batch, output_dim // 2, frames).

        Returns:
            Output, shaped (batch, output_dim, frames // stride).

        """
        return cast("torch.Tensor", self.block(x))

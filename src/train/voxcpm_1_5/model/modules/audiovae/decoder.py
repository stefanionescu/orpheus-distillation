"""Causal decoder of the audio VAE."""

from __future__ import annotations

import math
from typing import TYPE_CHECKING, cast, override

from torch import nn
from torch.nn.utils import weight_norm

from src.train.voxcpm_1_5.model.modules.audiovae.layers import (
    NoiseBlock,
    SnakeActivation,
    CausalResidualUnit,
    CausalTransposeConv,
    build_causal_conv,
)

if TYPE_CHECKING:
    from collections.abc import Callable

    import torch

OUTPUT_CHANNELS = 1


class CausalDecoder(nn.Module):
    """Upsampling blocks that halve the channels, then a tanh to the waveform."""

    def __init__(
        self,
        input_channel: int,
        channels: int,
        rates: list[int],
        *,
        depthwise: bool,
        use_noise_block: bool,
    ) -> None:
        """Build the decoder.

        Args:
            input_channel: Size of one latent frame.
            channels: Channels after the first convolution; each block halves them.
            rates: Upsampling factor per block.
            depthwise: Whether the convolutions are depthwise.
            use_noise_block: Whether each block adds learned noise after upsampling.

        """
        cast("Callable[[], None]", super().__init__)()
        if depthwise:
            layers: list[nn.Module] = [
                build_causal_conv(input_channel, input_channel, kernel_size=7, padding=3, groups=input_channel),
                build_causal_conv(input_channel, channels, kernel_size=1),
            ]
        else:
            layers = [build_causal_conv(input_channel, channels, kernel_size=7, padding=3)]

        output_dim = channels
        for index, stride in enumerate(rates):
            input_dim = channels // 2**index
            output_dim = channels // 2 ** (index + 1)
            groups = output_dim if depthwise else 1
            layers += [
                CausalDecoderBlock(input_dim, output_dim, stride, groups=groups, use_noise_block=use_noise_block)
            ]

        layers += [
            SnakeActivation(output_dim),
            build_causal_conv(output_dim, OUTPUT_CHANNELS, kernel_size=7, padding=3),
            nn.Tanh(),
        ]
        self.model = nn.Sequential(*layers)

    @override
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Decode latent frames.

        Args:
            x: Latents, shaped (batch, input_channel, frames).

        Returns:
            Waveform in [-1, 1], shaped (batch, 1, samples).

        """
        return cast("torch.Tensor", self.model(x))


class CausalDecoderBlock(nn.Module):
    """Strided transposed convolution that upsamples, optional noise, then dilated residual units."""

    def __init__(
        self,
        input_dim: int,
        output_dim: int,
        stride: int,
        *,
        groups: int,
        use_noise_block: bool,
    ) -> None:
        """Build the block.

        Args:
            input_dim: Input channels.
            output_dim: Output channels.
            stride: Upsampling factor.
            groups: Convolution groups of the residual units.
            use_noise_block: Whether to add learned noise after upsampling.

        """
        cast("Callable[[], None]", super().__init__)()
        layers: list[nn.Module] = [
            SnakeActivation(input_dim),
            weight_norm(
                CausalTransposeConv(
                    input_dim,
                    output_dim,
                    kernel_size=2 * stride,
                    stride=stride,
                    padding=math.ceil(stride / 2),
                    output_padding=stride % 2,
                )
            ),
        ]
        if use_noise_block:
            layers.append(NoiseBlock(output_dim))
        layers.extend(
            [
                CausalResidualUnit(output_dim, dilation=1, groups=groups),
                CausalResidualUnit(output_dim, dilation=3, groups=groups),
                CausalResidualUnit(output_dim, dilation=9, groups=groups),
            ]
        )
        self.block = nn.Sequential(*layers)

    @override
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Upsample.

        Args:
            x: Input, shaped (batch, input_dim, frames).

        Returns:
            Output, shaped (batch, output_dim, frames * stride).

        """
        return cast("torch.Tensor", self.block(x))

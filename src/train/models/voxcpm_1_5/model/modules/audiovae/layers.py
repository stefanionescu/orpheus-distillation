"""Causal convolutions, snake activation, and residual and noise blocks of the audio VAE."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast, override

import torch
from torch import nn
from torch.nn import functional
from torch.nn.utils import weight_norm

if TYPE_CHECKING:
    from collections.abc import Callable

RESIDUAL_KERNEL_SIZE = 7
SNAKE_EPSILON = 1e-9


class CausalResidualUnit(nn.Module):
    """Residual block of two snake-activated causal convolutions, the first one dilated."""

    def __init__(self, dim: int, *, dilation: int, groups: int) -> None:
        """Build the block.

        Args:
            dim: Channels in and out.
            dilation: Dilation of the first convolution.
            groups: Convolution groups of the first convolution.

        """
        cast("Callable[[], None]", super().__init__)()
        pad = ((RESIDUAL_KERNEL_SIZE - 1) * dilation) // 2
        self.block = nn.Sequential(
            SnakeActivation(dim),
            build_causal_conv(
                dim,
                dim,
                kernel_size=RESIDUAL_KERNEL_SIZE,
                dilation=dilation,
                padding=pad,
                groups=groups,
            ),
            SnakeActivation(dim),
            build_causal_conv(dim, dim, kernel_size=1),
        )

    @override
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Add the block output to its input.

        Args:
            x: Input, shaped (batch, dim, frames).

        Returns:
            Output, shaped like the input.

        Raises:
            ValueError: When the block changes the frame count.

        """
        y = cast("torch.Tensor", self.block(x))
        pad = (x.shape[-1] - y.shape[-1]) // 2
        if pad != 0:
            message = f"Residual block returned {y.shape[-1]} frames for {x.shape[-1]} input frames"
            raise ValueError(message)
        return x + y


class SnakeActivation(nn.Module):
    """Snake activation `x + sin(alpha * x) ** 2 / alpha`, with one learned alpha per channel."""

    def __init__(self, channels: int) -> None:
        """Create alpha, set to one.

        Args:
            channels: Channel count.

        """
        cast("Callable[[], None]", super().__init__)()
        self.alpha = nn.Parameter(torch.ones(1, channels, 1))

    @override
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Apply the activation.

        Args:
            x: Input, shaped (batch, channels, ...).

        Returns:
            Output, shaped like the input.

        """
        return apply_snake(x, self.alpha)


def apply_snake(x: torch.Tensor, alpha: torch.Tensor) -> torch.Tensor:
    """Add the periodic snake term to each channel.

    Args:
        x: Input, shaped (batch, channels, ...).
        alpha: Frequency of each channel, shaped (1, channels, 1).

    Returns:
        x plus sin(alpha * x) squared over alpha, in the shape of x.

    """
    shape = x.shape
    x = x.reshape(shape[0], shape[1], -1)
    x = x + (alpha + SNAKE_EPSILON).reciprocal() * torch.sin(alpha * x).pow(2)
    return x.reshape(shape)


class NoiseBlock(nn.Module):
    """Gaussian noise, scaled by a learned pointwise convolution of the input."""

    def __init__(self, dim: int) -> None:
        """Build the scaling convolution.

        Args:
            dim: Channel count.

        """
        cast("Callable[[], None]", super().__init__)()
        self.linear = build_causal_conv(dim, dim, kernel_size=1, bias=False)

    @override
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Add the scaled noise.

        Args:
            x: Input, shaped (batch, dim, frames).

        Returns:
            Input plus noise.

        """
        batch_size, _, frames = x.shape
        noise = torch.randn((batch_size, 1, frames), device=x.device, dtype=x.dtype)
        return x + noise * self.linear(x)


class CausalConv(nn.Conv1d):
    """1D convolution that pads only on the left, so it stays causal."""

    def __init__(self, *args: int, padding: int = 0, **kwargs: int) -> None:
        """Build the convolution.

        Args:
            *args: Positional arguments of `nn.Conv1d`.
            padding: Half the frames to add on the left.
            **kwargs: Keyword arguments of `nn.Conv1d`, without `padding`.

        """
        cast("Callable[..., None]", super().__init__)(*args, **kwargs)
        self.__padding = padding

    @override
    def forward(self, input: torch.Tensor) -> torch.Tensor:
        """Pad on the left and convolve.

        Args:
            input: Input, shaped (batch, channels, frames).

        Returns:
            The output.

        """
        return super().forward(functional.pad(input, (self.__padding * 2, 0)))


class CausalTransposeConv(nn.ConvTranspose1d):
    """1D transposed convolution that trims the right side, so it stays causal."""

    def __init__(self, *args: int, padding: int = 0, output_padding: int = 0, **kwargs: int) -> None:
        """Build the convolution.

        Args:
            *args: Positional arguments of `nn.ConvTranspose1d`.
            padding: Half the frames to trim from the right.
            output_padding: Frames of the trim to keep.
            **kwargs: Keyword arguments of `nn.ConvTranspose1d`, without the paddings.

        """
        cast("Callable[..., None]", super().__init__)(*args, **kwargs)
        self.__padding = padding
        self.__output_padding = output_padding

    @override
    def forward(self, input: torch.Tensor, output_size: list[int] | None = None) -> torch.Tensor:
        """Convolve and trim the right side.

        Args:
            input: Input, shaped (batch, channels, frames).
            output_size: Output size, as `nn.ConvTranspose1d` takes it.

        Returns:
            The output.

        """
        output = super().forward(input, output_size)
        return output[..., : -(self.__padding * 2 - self.__output_padding)]


def build_causal_conv(*args: int, **kwargs: int) -> CausalConv:
    """Build a weight-normalized causal convolution.

    Args:
        *args: Positional arguments of `nn.Conv1d`.
        **kwargs: Keyword arguments of `CausalConv`.

    Returns:
        The convolution.

    """
    return weight_norm(CausalConv(*args, **kwargs))

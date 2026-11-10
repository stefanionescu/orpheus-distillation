"""RMS norm and gated feed-forward layer of MiniCPM4."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast, override

import torch
from torch import nn

if TYPE_CHECKING:
    from collections.abc import Callable

    from src.train.models.voxcpm_1_5.model.modules.minicpm4.config import MiniCpmConfig


class MiniCpmRmsNorm(nn.Module):
    """RMS norm with a learned scale, computed in float32, as in T5."""

    def __init__(self, hidden_size: int, eps: float = 1e-6) -> None:
        """Create the scale, set to one.

        Args:
            hidden_size: Size of the normalized dimension.
            eps: Added to the mean square before the square root.

        """
        cast("Callable[[], None]", super().__init__)()
        self.weight = nn.Parameter(torch.ones(hidden_size))
        self.variance_epsilon = eps

    @override
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
        """Normalize the last dimension.

        Args:
            hidden_states: The input.

        Returns:
            Normalized input in its own dtype, times the scale.

        """
        input_dtype = hidden_states.dtype
        variance = hidden_states.to(torch.float32).pow(2).mean(dim=-1, keepdim=True)
        hidden_states = (hidden_states * torch.rsqrt(variance + self.variance_epsilon)).to(input_dtype)
        return hidden_states * self.weight


class MiniCpmMlp(nn.Module):
    """Gated SiLU feed-forward layer: `down(silu(gate(x)) * up(x))`."""

    def __init__(self, config: MiniCpmConfig) -> None:
        """Build the gate, up, and down projections.

        Args:
            config: Transformer config.

        """
        cast("Callable[[], None]", super().__init__)()
        self.config = config
        self.hidden_size = config.hidden_size
        self.intermediate_size = config.intermediate_size
        self.gate_proj = nn.Linear(self.hidden_size, self.intermediate_size, bias=False)
        self.up_proj = nn.Linear(self.hidden_size, self.intermediate_size, bias=False)
        self.down_proj = nn.Linear(self.intermediate_size, self.hidden_size, bias=False)
        self.act_fn = nn.SiLU()

    @override
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Apply the layer.

        Args:
            x: Input, shaped (..., hidden_size).

        Returns:
            Output, shaped like the input.

        """
        return cast("torch.Tensor", self.down_proj(self.act_fn(self.gate_proj(x)) * self.up_proj(x)))

"""Pre-norm decoder layer of MiniCPM4."""

from __future__ import annotations

import math
from typing import TYPE_CHECKING, cast, override

from torch import nn

from src.train.voxcpm_1_5.model.modules.minicpm4.layers import MiniCpmMlp, MiniCpmRmsNorm
from src.train.voxcpm_1_5.model.modules.minicpm4.attention import MiniCpmAttention

if TYPE_CHECKING:
    from collections.abc import Callable

    import torch

    from src.train.voxcpm_1_5.model.modules.minicpm4.config import MiniCpmConfig
    from src.train.voxcpm_1_5.model.modules.minicpm4.attention import KeyValue, RotaryEmbedding


class MiniCpmDecoderLayer(nn.Module):
    """Pre-norm decoder layer. Under maximal update parametrization, it scales down each residual branch."""

    def __init__(self, config: MiniCpmConfig, layer_index: int) -> None:
        """Build the attention, the feed-forward layer, and their norms.

        Args:
            config: Transformer config.
            layer_index: Index of the layer in its transformer.

        """
        cast("Callable[[], None]", super().__init__)()
        self.hidden_size = config.hidden_size
        self.self_attn = MiniCpmAttention(config=config, layer_index=layer_index)

        self.mlp = MiniCpmMlp(config)
        self.input_layernorm = MiniCpmRmsNorm(config.hidden_size, eps=config.rms_norm_eps)
        self.post_attention_layernorm = MiniCpmRmsNorm(config.hidden_size, eps=config.rms_norm_eps)

        self.scale_depth = config.scale_depth
        self.num_hidden_layers = config.num_hidden_layers
        self.use_mup = config.use_mup

    @override
    def forward(
        self,
        hidden_states: torch.Tensor,
        position_emb: RotaryEmbedding,
        *,
        is_causal: bool,
    ) -> tuple[torch.Tensor, KeyValue]:
        """Run the layer over a whole sequence.

        Args:
            hidden_states: Input, shaped (batch, length, hidden_size).
            position_emb: Rotary cosines and sines of every position.
            is_causal: Whether attention is causal.

        Returns:
            Output, and the keys and values from attention.

        """
        residual = hidden_states
        hidden_states = self.input_layernorm(hidden_states)
        hidden_states, present_key_value = self.self_attn(
            hidden_states=hidden_states,
            position_emb=position_emb,
            is_causal=is_causal,
        )
        hidden_states = self._add_residual(residual, hidden_states)
        return self._run_mlp_block(hidden_states), present_key_value

    def forward_step(
        self,
        hidden_states: torch.Tensor,
        position_emb: RotaryEmbedding,
        position_id: torch.Tensor,
        kv_cache: KeyValue,
    ) -> torch.Tensor:
        """Run the layer for one new position against its KV cache.

        Args:
            hidden_states: Input at the new position, shaped (batch, hidden_size).
            position_emb: Cosines and sines of the new position.
            position_id: New position, a one-element tensor.
            kv_cache: Keys and values of the layer.

        Returns:
            Output, shaped like the input.

        """
        residual = hidden_states
        hidden_states = self.input_layernorm(hidden_states)
        hidden_states = self.self_attn.forward_step(
            hidden_states=hidden_states,
            position_emb=position_emb,
            position_id=position_id,
            kv_cache=kv_cache,
        )
        hidden_states = self._add_residual(residual, hidden_states)
        return self._run_mlp_block(hidden_states)

    def _run_mlp_block(self, hidden_states: torch.Tensor) -> torch.Tensor:
        residual = hidden_states
        hidden_states = self.post_attention_layernorm(hidden_states)
        hidden_states = self.mlp(hidden_states)
        return self._add_residual(residual, hidden_states)

    def _add_residual(self, residual: torch.Tensor, hidden_states: torch.Tensor) -> torch.Tensor:
        if self.use_mup:
            return residual + hidden_states * (self.scale_depth / math.sqrt(self.num_hidden_layers))
        return residual + hidden_states

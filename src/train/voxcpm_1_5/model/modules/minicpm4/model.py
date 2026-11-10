"""MiniCPM4 transformer with a static KV cache for decoding."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast, override

import torch
from torch import nn

from src.train.voxcpm_1_5.model.modules.minicpm4.layers import MiniCpmRmsNorm
from src.train.voxcpm_1_5.model.modules.minicpm4.decoder import MiniCpmDecoderLayer
from src.train.voxcpm_1_5.model.modules.minicpm4.attention import MiniCpmLongRope

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable

    from src.train.voxcpm_1_5.model.modules.minicpm4.cache import StaticKvCache
    from src.train.voxcpm_1_5.model.modules.minicpm4.config import MiniCpmConfig


class MiniCpmModel(nn.Module):
    """MiniCPM decoder layers, a final RMS norm, and their shared rotary embedding."""

    def __init__(self, config: MiniCpmConfig) -> None:
        """Build the embedding, the decoder layers, the final norm, and the rotary embedding.

        Args:
            config: Transformer config; a zero vocabulary size gives an identity embedding.

        """
        cast("Callable[[], None]", super().__init__)()
        self.vocab_size = config.vocab_size
        self.config = config

        if config.vocab_size > 0:
            self.embed_tokens: nn.Module = nn.Embedding(config.vocab_size, config.hidden_size)
        else:
            self.embed_tokens = nn.Identity()

        self.layers = nn.ModuleList(
            [MiniCpmDecoderLayer(config, layer_index) for layer_index in range(config.num_hidden_layers)]
        )

        self.norm = MiniCpmRmsNorm(config.hidden_size, eps=config.rms_norm_eps)
        self.rope_emb = MiniCpmLongRope(config)

        self.kv_cache: StaticKvCache | None = None

    @override
    def forward(
        self,
        inputs_embeds: torch.Tensor,
        *,
        is_causal: bool = True,
    ) -> tuple[torch.Tensor, list[tuple[torch.Tensor, torch.Tensor]]]:
        """Run every layer over a whole sequence.

        Args:
            inputs_embeds: Input, shaped (batch, length, hidden_size).
            is_causal: Whether each position attends only to itself and earlier positions.

        Returns:
            Normalized output, shaped like the input, and the keys and values of every layer.

        """
        position_ids = torch.arange(0, inputs_embeds.size(1), dtype=torch.long, device=inputs_embeds.device)
        position_emb = self.rope_emb(position_ids)
        hidden_states = inputs_embeds

        next_decoder_cache: list[tuple[torch.Tensor, torch.Tensor]] = []

        for decoder_layer in self.layers:
            hidden_states, this_cache = decoder_layer(hidden_states, position_emb, is_causal=is_causal)
            next_decoder_cache.append(this_cache)
        hidden_states = self.norm(hidden_states)
        return hidden_states, next_decoder_cache

    def forward_step(
        self,
        inputs_embeds: torch.Tensor,
        position_id: torch.Tensor,
    ) -> torch.Tensor:
        """Run every layer for one new position against the KV cache.

        Args:
            inputs_embeds: Input at the new position, shaped (batch, hidden_size).
            position_id: New position, a one-element tensor.

        Returns:
            Normalized output, shaped like the input.

        Raises:
            RuntimeError: When the model has no KV cache.

        """
        if self.kv_cache is None:
            message = "KV cache is not setup"
            raise RuntimeError(message)

        position_emb = self.rope_emb(position_id)
        hidden_states = inputs_embeds
        decoder_layers = cast("Iterable[MiniCpmDecoderLayer]", self.layers)

        for i, decoder_layer in enumerate(decoder_layers):
            hidden_states = decoder_layer.forward_step(
                hidden_states,
                position_emb,
                position_id,
                (self.kv_cache.kv_cache[0, i], self.kv_cache.kv_cache[1, i]),
            )

        hidden_states = self.norm(hidden_states)
        return cast("torch.Tensor", hidden_states)

"""Rotary position embedding and grouped-query attention of MiniCPM4."""

from __future__ import annotations

import math
from typing import TYPE_CHECKING, cast, override

import torch
from torch import nn
from torch.nn import functional

if TYPE_CHECKING:
    from collections.abc import Callable

    from src.train.models.voxcpm_1_5.model.modules.minicpm4.config import MiniCpmConfig


type RotaryEmbedding = tuple[torch.Tensor, torch.Tensor]
type KeyValue = tuple[torch.Tensor, torch.Tensor]


class MiniCpmLongRope(nn.Module):
    """LongRoPE rotary embedding: per-frequency factors and one attention scale."""

    def __init__(self, config: MiniCpmConfig) -> None:
        """Precompute the cosines and sines of every position up to the longest context.

        Args:
            config: Transformer config.

        """
        cast("Callable[[], None]", super().__init__)()
        self.config = config
        self.dim = config.kv_channels or config.hidden_size // config.num_attention_heads
        self.base = config.rope_theta
        self.max_position_embeddings = config.max_position_embeddings

        self.short_factor = config.rope_scaling.short_factor
        self.long_factor = config.rope_scaling.long_factor
        self.original_max_position_embeddings = config.rope_scaling.original_max_position_embeddings

        scale = self.max_position_embeddings / self.original_max_position_embeddings
        self.scaling_factor = math.sqrt(1 + math.log(scale) / math.log(self.original_max_position_embeddings))
        inv_freq = 1.0 / (self.base ** (torch.arange(0, self.dim, 2).float() / self.dim))
        self.register_buffer("inv_freq", inv_freq, persistent=False)

        self.max_seq_len_cached = 0

        self.register_buffer("cos_cached", torch.empty(0), persistent=False)
        self.register_buffer("sin_cached", torch.empty(0), persistent=False)

        inv_freq = cast("torch.Tensor", self.inv_freq)
        self._set_cos_sin_cache(
            seq_len=self.max_position_embeddings,
            device=inv_freq.device,
            dtype=torch.float32,
        )

    def _set_cos_sin_cache(self, seq_len: int, device: torch.device, dtype: torch.dtype) -> None:
        self.max_seq_len_cached = seq_len
        inv_freq = cast("torch.Tensor", self.inv_freq)
        t = torch.arange(self.max_seq_len_cached, device=device, dtype=inv_freq.dtype)

        if seq_len > self.original_max_position_embeddings:
            ext_factors = torch.tensor(self.long_factor, dtype=torch.float32, device=device)
        else:
            ext_factors = torch.tensor(self.short_factor, dtype=torch.float32, device=device)

        freqs = torch.mul(
            torch.outer(t, 1.0 / ext_factors).to(device=device),
            inv_freq.to(device=device).to(dtype),
        )

        emb = torch.cat((freqs, freqs), dim=-1)

        self.cos_cached = emb.cos().to(dtype) * self.scaling_factor
        self.sin_cached = emb.sin().to(dtype) * self.scaling_factor

    @override
    def forward(self, position_ids: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        """Look up the cosines and sines of positions.

        Args:
            position_ids: Positions, shaped (length,) or (batch, length).

        Returns:
            Cosines and sines, each shaped like the positions plus a last `head_dim` dimension.

        """
        cos = self.cos_cached[position_ids]
        sin = self.sin_cached[position_ids]
        return cos, sin


class MiniCpmAttention(nn.Module):
    """Grouped-query attention with rotary embeddings, over a whole sequence or one cached step."""

    def __init__(self, config: MiniCpmConfig, layer_index: int) -> None:
        """Build the query, key, value, and output projections.

        Args:
            config: Transformer config.
            layer_index: Index of the layer in its transformer.

        """
        cast("Callable[[], None]", super().__init__)()
        self.config = config
        self.layer_index = layer_index
        self.hidden_size = config.hidden_size
        self.num_heads = config.num_attention_heads
        self.head_dim = (
            config.hidden_size // config.num_attention_heads if config.kv_channels is None else config.kv_channels
        )
        self.num_key_value_heads = config.num_key_value_heads
        self.max_position_embeddings = config.max_position_embeddings

        self.q_proj = nn.Linear(self.hidden_size, self.num_heads * self.head_dim, bias=False)
        self.k_proj = nn.Linear(self.hidden_size, self.num_key_value_heads * self.head_dim, bias=False)
        self.v_proj = nn.Linear(self.hidden_size, self.num_key_value_heads * self.head_dim, bias=False)
        self.o_proj = nn.Linear(self.num_heads * self.head_dim, self.hidden_size, bias=False)

    @override
    def forward(
        self,
        hidden_states: torch.Tensor,
        position_emb: tuple[torch.Tensor, torch.Tensor],
        *,
        is_causal: bool,
    ) -> tuple[torch.Tensor, tuple[torch.Tensor, torch.Tensor]]:
        """Attend over a whole sequence.

        Args:
            hidden_states: Input, shaped (batch, length, hidden_size).
            position_emb: Cosines and sines of the positions.
            is_causal: Whether each position attends only to itself and earlier positions.

        Returns:
            Output, shaped like the input, and the keys and values of this layer for a KV cache.

        """
        bsz, q_len, _ = hidden_states.size()

        query_states = self.q_proj(hidden_states)
        key_states = self.k_proj(hidden_states)
        value_states = self.v_proj(hidden_states)

        query_states = query_states.view(bsz, q_len, self.num_heads, self.head_dim).transpose(1, 2)
        key_states = key_states.view(bsz, q_len, self.num_key_value_heads, self.head_dim).transpose(1, 2)
        value_states = value_states.view(bsz, q_len, self.num_key_value_heads, self.head_dim).transpose(1, 2)

        cos, sin = position_emb

        query_states, key_states = apply_rotary_pos_emb(query_states, key_states, cos, sin)

        # MPS has a bug with non-contiguous tensors: https://github.com/pytorch/pytorch/issues/163597
        query_states = query_states.contiguous()
        key_states = key_states.contiguous()
        value_states = value_states.contiguous()
        attn_output = functional.scaled_dot_product_attention(
            query_states,
            key_states,
            value_states,
            is_causal=is_causal,
            enable_gqa=True,
        )

        attn_output = attn_output.transpose(1, 2).contiguous()
        attn_output = attn_output.reshape(bsz, q_len, self.num_heads * self.head_dim)

        attn_output = self.o_proj(attn_output)

        past_key_value = (key_states, value_states)
        return attn_output, past_key_value

    def forward_step(
        self,
        hidden_states: torch.Tensor,
        position_emb: tuple[torch.Tensor, torch.Tensor],
        position_id: torch.Tensor,
        kv_cache: tuple[torch.Tensor, torch.Tensor],
    ) -> torch.Tensor:
        """Write the key and value of one new position into the cache, then attend from it.

        Args:
            hidden_states: Input at the new position, shaped (batch, hidden_size).
            position_emb: Cosines and sines of the new position.
            position_id: New position, a one-element tensor.
            kv_cache: Keys and values of this layer, shaped (batch, heads, max_length, head_dim).

        Returns:
            Output, shaped like the input.

        """
        bsz, _ = hidden_states.size()

        query_states = self.q_proj(hidden_states)
        key_states = self.k_proj(hidden_states)
        value_states = self.v_proj(hidden_states)

        query_states = query_states.view(bsz, 1, self.num_heads, self.head_dim).transpose(1, 2)
        key_states = key_states.view(bsz, 1, self.num_key_value_heads, self.head_dim).transpose(1, 2)
        value_states = value_states.view(bsz, 1, self.num_key_value_heads, self.head_dim).transpose(1, 2)

        cos, sin = position_emb

        query_states, key_states = apply_rotary_pos_emb(query_states, key_states, cos, sin)

        key_cache, value_cache = kv_cache

        # Index with a tensor: a Python int breaks the full graph that torch.compile captures.
        key_cache[:, :, position_id, :] = key_states
        value_cache[:, :, position_id, :] = value_states

        # scaled_dot_product_attention needs a two-dimensional mask, so give the one query one row.
        attn_mask = (torch.arange(key_cache.size(2), device=key_cache.device) <= position_id).unsqueeze(0)

        # Same MPS bug as in forward.
        query_states = query_states.contiguous()
        key_cache = key_cache.contiguous()
        value_cache = value_cache.contiguous()
        attn_output = functional.scaled_dot_product_attention(
            query_states,
            key_cache,
            value_cache,
            attn_mask=attn_mask,
            enable_gqa=True,
        )

        attn_output = attn_output.transpose(1, 2).contiguous()
        attn_output = attn_output.reshape(bsz, self.num_heads * self.head_dim)
        attn_output = self.o_proj(attn_output)

        return cast("torch.Tensor", attn_output)


def apply_rotary_pos_emb(
    q: torch.Tensor, k: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor
) -> tuple[torch.Tensor, torch.Tensor]:
    """Rotate queries and keys by position in float32, and return them in their own dtype.

    Args:
        q: Queries, shaped (batch, heads, length, head_dim).
        k: Keys, shaped (batch, kv_heads, length, head_dim).
        cos: Cosines, shaped (length, head_dim).
        sin: Sines, shaped (length, head_dim).

    Returns:
        Rotated queries and keys.

    """
    orig_dtype = q.dtype
    q = q.to(torch.float32)
    k = k.to(torch.float32)
    q_embed = (q * cos) + (rotate_half(q) * sin)
    k_embed = (k * cos) + (rotate_half(k) * sin)
    return q_embed.to(orig_dtype), k_embed.to(orig_dtype)


def rotate_half(x: torch.Tensor) -> torch.Tensor:
    """Swap the two halves of the last dimension and negate the new first half.

    Args:
        x: Input with an even last dimension.

    Returns:
        The rotated input.

    """
    x1, x2 = x.chunk(2, dim=-1)
    return torch.cat((-x2, x1), dim=-1)

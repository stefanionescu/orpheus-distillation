"""Static KV cache for decoding one position at a time."""

from __future__ import annotations

import torch


class StaticKvCache:
    """Preallocated keys and values of every layer. A prefill fills it, and each step adds one position."""

    def __init__(
        self,
        num_layers: int,
        max_length: int,
        head_shape: tuple[int, int, int],
        device: torch.device,
        dtype: torch.dtype,
    ) -> None:
        """Allocate the zeroed cache.

        Args:
            num_layers: Decoder layers.
            max_length: Positions the cache holds.
            head_shape: Batch size, key-value heads, and head size.
            device: Cache device.
            dtype: Cache dtype.

        """
        batch_size, num_kv_heads, dim_kv_head = head_shape
        self.max_length = max_length
        self.num_layers = num_layers

        self.kv_cache = torch.zeros(
            2,
            num_layers,
            batch_size,
            num_kv_heads,
            max_length,
            dim_kv_head,
            device=device,
            dtype=dtype,
        )
        self.current_length = 0

    def step(self) -> int:
        """Claim the next position.

        Returns:
            The position, before the cache grows.

        Raises:
            ValueError: When the cache is full.

        """
        if self.current_length >= self.max_length:
            message = "KV cache is full"
            raise ValueError(message)
        position = self.current_length
        self.current_length += 1
        return position

    def fill_caches(self, kv_caches: list[tuple[torch.Tensor, torch.Tensor]]) -> None:
        """Replace the cache contents with the keys and values of a prefill.

        Args:
            kv_caches: Keys and values per layer, each shaped (batch, kv_heads, length, head_dim).

        """
        self.current_length = kv_caches[0][0].size(2)
        self.kv_cache.zero_()
        for i in range(self.num_layers):
            self.kv_cache[0, i, :, :, : self.current_length, :] = kv_caches[i][0]
            self.kv_cache[1, i, :, :, : self.current_length, :] = kv_caches[i][1]

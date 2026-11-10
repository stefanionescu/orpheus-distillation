"""Torch dtypes by their config names."""

from __future__ import annotations

import torch

DTYPES = {
    "bfloat16": torch.bfloat16,
    "bf16": torch.bfloat16,
    "float16": torch.float16,
    "fp16": torch.float16,
    "float32": torch.float32,
    "fp32": torch.float32,
}


def select_dtype(dtype: str) -> torch.dtype:
    """Return the torch dtype for a config name.

    Args:
        dtype: A key of `DTYPES`, such as `bfloat16` or `bf16`.

    Returns:
        The dtype.

    Raises:
        ValueError: When `DTYPES` lacks the name.

    """
    if dtype not in DTYPES:
        message = f"Unsupported dtype: {dtype}"
        raise ValueError(message)
    return DTYPES[dtype]

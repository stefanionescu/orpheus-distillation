"""Mixed precision uses the fastest dtype that the GPU compute capability supports."""

from __future__ import annotations

import torch
import pytest

from src.train.models.voxcpm_1_5.training.devices import select_amp_dtype


@pytest.mark.parametrize(
    ("capability", "dtype"),
    [(None, torch.float32), ((8, 0), torch.bfloat16), ((7, 5), torch.float16)],
    ids=["no-cuda", "ampere", "turing"],
)
def test_dtype_follows_capability(capability: tuple[int, int] | None, dtype: torch.dtype) -> None:
    """The CPU trains in float32, Ampere and newer in bfloat16, and older GPUs in float16.

    Args:
        capability: The compute capability, or None without CUDA.
        dtype: The dtype it selects.

    """
    assert select_amp_dtype(capability) is dtype

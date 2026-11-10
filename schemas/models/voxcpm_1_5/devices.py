"""The GPU that a training command runs on."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GpuReport:
    """Facts of one CUDA device.

    Attributes:
        name: Device name from the driver.
        total_memory_gb: Memory in gigabytes.
        capability: CUDA compute capability as a major and minor version.

    """

    name: str
    total_memory_gb: float
    capability: tuple[int, int]

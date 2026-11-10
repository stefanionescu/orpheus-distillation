"""The CUDA device that a training process runs on."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, cast
import logging

import torch

from schemas.voxcpm_1_5.devices import GpuReport

if TYPE_CHECKING:
    from collections.abc import Callable

BFLOAT_MAJOR_CAPABILITY = 8
BYTES_PER_GB = 1024**3

logger = logging.getLogger(__name__)


class _DeviceProperties(Protocol):
    name: str
    total_memory: int
    major: int
    minor: int


read_device_properties: Callable[[int], _DeviceProperties] = cast(
    "Callable[[int], _DeviceProperties]", torch.cuda.get_device_properties
)


class GpuError(Exception):
    """Training needs a CUDA GPU, and torch finds none."""


def select_amp_dtype(capability: tuple[int, int] | None) -> torch.dtype:
    """Pick the mixed precision dtype of a device.

    Args:
        capability: CUDA compute capability as a major and minor version, or None without CUDA.

    Returns:
        bfloat16 on Ampere and newer GPUs, float16 on older GPUs, float32 without CUDA.

    """
    if capability is None:
        return torch.float32
    # Ampere (sm_80) and newer GPUs compute bfloat16 at full speed.
    return torch.bfloat16 if capability[0] >= BFLOAT_MAJOR_CAPABILITY else torch.float16


def read_gpu_report(device_index: int) -> GpuReport | None:
    """Read the name, memory, and compute capability of one CUDA device.

    Args:
        device_index: Device index on the host, which is the local rank.

    Returns:
        The report, or None when torch finds no CUDA device.

    """
    if not torch.cuda.is_available():
        return None
    properties = read_device_properties(device_index)
    return GpuReport(
        name=properties.name,
        total_memory_gb=properties.total_memory / BYTES_PER_GB,
        capability=(properties.major, properties.minor),
    )


def assert_cuda_available() -> None:
    """Fail when torch finds no CUDA device.

    Raises:
        GpuError: Torch finds no CUDA device.

    """
    if not torch.cuda.is_available():
        message = "Training needs a CUDA GPU, and torch finds none"
        raise GpuError(message)


def print_gpu_report(report: GpuReport | None) -> None:
    """Log the device that the process trains on.

    Args:
        report: CUDA device report, or None on the CPU.

    """
    if report is None:
        logger.warning("No CUDA device; training runs on the CPU in float32")
        return
    major, minor = report.capability
    logger.info("Training on %s, %.1f GB, compute capability %d.%d", report.name, report.total_memory_gb, major, minor)

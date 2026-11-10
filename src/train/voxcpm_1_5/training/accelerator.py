"""Distributed data parallel and mixed precision for one training process."""

from __future__ import annotations

import random
from typing import TYPE_CHECKING, cast
import contextlib

import numpy as np
import torch
from torch import nn
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel

from config.voxcpm_1_5.training import SEED, AMP_ENABLED, DDP_BACKEND, DDP_INIT_METHOD
from src.train.voxcpm_1_5.training.devices import select_amp_dtype

if TYPE_CHECKING:
    from collections.abc import Callable, Generator

    from schemas.settings import TrainEnvironment
    from schemas.voxcpm_1_5.devices import GpuReport

MAIN_RANK = 0

all_reduce = cast("Callable[..., object]", dist.all_reduce)
seed_torch = cast("Callable[[int], object]", torch.manual_seed)


class Accelerator:
    """Device, rank, and gradient scaler of one training process."""

    def __init__(self, device: torch.device, world_size: int, local_rank: int, amp_dtype: torch.dtype | None) -> None:
        """Hold the process facts. A distributed run must join its process group first.

        Args:
            device: Device that the process trains on.
            world_size: Number of processes in the run.
            local_rank: Process index on its host, which is also its CUDA device index.
            amp_dtype: Mixed precision dtype, or None for float32.

        """
        self.device = device
        self.world_size = world_size
        self.local_rank = local_rank
        self.amp_dtype = amp_dtype
        self.rank = dist.get_rank() if dist.is_initialized() else MAIN_RANK
        self.scaler = torch.amp.GradScaler(device.type, enabled=amp_dtype is not None)
        self._parallel_model: DistributedDataParallel | None = None

    @property
    def is_main(self) -> bool:
        """Whether this is rank 0, the only rank that logs metrics and writes checkpoints."""
        return self.rank == MAIN_RANK

    def prepare_model(self, model: nn.Module) -> nn.Module:
        """Move the model to the device, and wrap it in DDP when the run has several processes.

        Args:
            model: Model to train.

        Returns:
            The model to call: the model itself or its DDP wrapper.

        """
        model = model.to(self.device)
        if self.world_size == 1:
            return model
        self._parallel_model = DistributedDataParallel(model, device_ids=[self.local_rank])
        return self._parallel_model

    @contextlib.contextmanager
    def no_sync(self) -> Generator[None]:
        """Skip gradient averaging for the micro-batches before the last one of an optimizer step.

        Yields:
            Nothing; averaging resumes on exit.

        """
        if self._parallel_model is None:
            yield
            return
        with self._parallel_model.no_sync():
            yield

    def autocast(self) -> torch.autocast:
        """Return the autocast context of the mixed precision dtype.

        Returns:
            The context, which does nothing without mixed precision.

        """
        return torch.autocast(self.device.type, dtype=self.amp_dtype, enabled=self.amp_dtype is not None)

    def all_reduce_mean(self, value: torch.Tensor) -> torch.Tensor:
        """Average a tensor across processes, in place.

        Args:
            value: Tensor of this process.

        Returns:
            The same tensor, now holding the mean.

        """
        if dist.is_initialized():
            all_reduce(value, op=dist.ReduceOp.AVG)
        return value

    def is_any_rank_flagged(self, *, is_flagged: bool) -> bool:
        """Tell whether any process set a flag, so every process stops at the same step.

        Args:
            is_flagged: Flag of this process.

        Returns:
            Whether any process set the flag.

        """
        if not dist.is_initialized():
            return is_flagged
        flag = torch.tensor(int(is_flagged), device=self.device)
        all_reduce(flag, op=dist.ReduceOp.MAX)
        return bool(flag.item())


def set_random_seeds(seed: int) -> None:
    """Seed the random generators of Python, NumPy, and torch.

    Args:
        seed: The seed. Each process passes the run seed plus its rank, so processes draw different random numbers.

    """
    random.seed(seed)
    np.random.seed(seed)
    seed_torch(seed)


def build_accelerator(environment: TrainEnvironment, report: GpuReport | None) -> Accelerator:
    """Join the process group of a distributed run, seed the generators, and pick the device and dtype.

    Args:
        environment: Distributed layout of the process.
        report: CUDA device report, or None to train on the CPU.

    Returns:
        The accelerator.

    """
    if environment.world_size > 1 and not dist.is_initialized():
        dist.init_process_group(DDP_BACKEND, init_method=DDP_INIT_METHOD)
    if report is None:
        accelerator = Accelerator(torch.device("cpu"), environment.world_size, environment.local_rank, None)
    else:
        amp_dtype = select_amp_dtype(report.capability) if AMP_ENABLED else None
        device = torch.device("cuda", environment.local_rank)
        accelerator = Accelerator(device, environment.world_size, environment.local_rank, amp_dtype)
    set_random_seeds(SEED + accelerator.rank)
    return accelerator

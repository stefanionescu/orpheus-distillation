"""TensorBoard writer fakes, numbered clips, and the setup of a training command that runs on the CPU."""

from __future__ import annotations

import signal
from typing import TYPE_CHECKING, override
from dataclasses import field, dataclass
from collections.abc import Sized

import torch
from torch.utils.data import Dataset

from schemas.models.voxcpm_1_5.training import TrainingClip
from src.train.models.voxcpm_1_5.commands import train
from src.train.models.voxcpm_1_5.training import job

if TYPE_CHECKING:
    import pytest


class NumberedClips(Dataset[TrainingClip], Sized):
    """Clips whose one text token is their index, so a collated batch shows the order that the sampler drew."""

    def __init__(self, size: int) -> None:
        """Hold the clip count.

        Args:
            size: Number of clips.

        """
        self._size = size

    @override
    def __len__(self) -> int:
        return self._size

    @override
    def __getitem__(self, index: int) -> TrainingClip:
        return TrainingClip(text_tokens=torch.tensor([index]), waveform=torch.zeros(1))


@dataclass
class FakeWriter:
    """A TensorBoard writer that keeps each metric in memory in place of an event file.

    Attributes:
        scalars: Each metric as its tag, value, and step, in write order.

    """

    scalars: list[tuple[str, float, int]] = field(default_factory=list[tuple[str, float, int]])

    def add_scalar(self, tag: str, scalar_value: float, global_step: int) -> None:
        """Keep one metric.

        Args:
            tag: Metric name.
            scalar_value: The value.
            global_step: Optimizer steps completed.

        """
        self.scalars.append((tag, scalar_value, global_step))

    def close(self) -> None:
        """Close nothing."""


class StoppingWriter:
    """A TensorBoard writer that sends SIGTERM at its first metric, as a stop from the shell arrives mid-run."""

    def __init__(self, logdir: str) -> None:
        """Keep no event file.

        Args:
            logdir: The event file folder, which the fake ignores.

        """
        del logdir
        self.is_signalled = False

    def add_scalar(self, tag: str, scalar_value: float, global_step: int) -> None:
        """Send SIGTERM to this process on the first call.

        Args:
            tag: Metric name, which the fake ignores.
            scalar_value: The value, which the fake ignores.
            global_step: Optimizer steps completed, which the fake ignores.

        """
        del tag, scalar_value, global_step
        if not self.is_signalled:
            self.is_signalled = True
            signal.raise_signal(signal.SIGTERM)

    def close(self) -> None:
        """Close nothing."""


def install_stopping_cpu_run(monkeypatch: pytest.MonkeyPatch) -> None:
    """Make the training command run on the CPU in this process, and stop it at its first logged step.

    The CUDA probe passes without a GPU, the job places the model on the CPU, the loader reads clips without worker
    processes, and the metric writer sends the stop signal.

    Args:
        monkeypatch: Restores each replaced name after the test.

    """
    monkeypatch.setattr(torch.cuda, "is_available", lambda: False)
    monkeypatch.setattr(train, "assert_cuda_available", lambda: None)
    monkeypatch.setattr(train, "LOADER_WORKERS", 0)
    monkeypatch.setattr(job, "SummaryWriter", StoppingWriter)

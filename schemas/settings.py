"""Environment of the training process."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TrainEnvironment:
    """Environment of one training process, read once at start.

    Attributes:
        hf_token: Hugging Face token, or None when unset.
        world_size: Process count of the distributed run.
        local_rank: Process index on its host.

    """

    hf_token: str | None
    world_size: int
    local_rank: int

"""The only reader of the training process environment.

A missing or empty variable takes its single-process value, and an invalid one stops the command before any work.
"""

from __future__ import annotations

import os

from schemas.settings import TrainEnvironment

SINGLE_PROCESS_WORLD_SIZE = 1
FIRST_RANK = 0


def _read_count(name: str, default: int, minimum: int) -> int:
    text = os.environ.get(name, "").strip()
    if not text:
        return default
    message = f"{name} must be a whole number of {minimum} or more"
    try:
        count = int(text)
    except ValueError as error:
        raise ValueError(message) from error
    if count < minimum:
        raise ValueError(message)
    return count


def read_environment() -> TrainEnvironment:
    """Read the Hugging Face token and the distributed layout that torchrun sets.

    A WORLD_SIZE below 1 or a LOCAL_RANK below 0 raises ValueError.

    Returns:
        The environment.

    """
    token = os.environ.get("HF_TOKEN")
    return TrainEnvironment(
        hf_token=(token.strip() or None) if token is not None else None,
        world_size=_read_count("WORLD_SIZE", SINGLE_PROCESS_WORLD_SIZE, SINGLE_PROCESS_WORLD_SIZE),
        local_rank=_read_count("LOCAL_RANK", FIRST_RANK, FIRST_RANK),
    )

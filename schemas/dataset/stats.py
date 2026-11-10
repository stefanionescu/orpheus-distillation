"""Totals that a dataset run writes to its stats file."""

from __future__ import annotations

from typing import TYPE_CHECKING
from dataclasses import dataclass

if TYPE_CHECKING:
    from collections.abc import Mapping


@dataclass(frozen=True)
class DatasetStats:
    """Totals of one dataset run. Each field name is a key of the stats file.

    Attributes:
        clip_count: Clip count.
        total_duration_seconds: Length of all clips.
        voices: Voices, in synthesis order.
        clips_per_voice: Clip count per voice.
        duration_per_voice: Seconds of audio per voice.
        shard_count: Shard count.
        prompt_hash: Hash of the prompt list, for resume checks.
        prompt_count: Prompt count, for resume checks.

    """

    clip_count: int
    total_duration_seconds: float
    voices: tuple[str, ...]
    clips_per_voice: Mapping[str, int]
    duration_per_voice: Mapping[str, float]
    shard_count: int
    prompt_hash: str
    prompt_count: int

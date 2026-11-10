"""Run stats sum the clips per voice, decode only well-typed fields, and rewrite the stats file on change."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from src.dataset.stats import (
    read_stats,
    write_stats,
    decode_stats,
    encode_stats,
    format_duration,
    build_dataset_stats,
)
from tests.harness.voices import FIRST_VOICE, SECOND_VOICE
from schemas.dataset.stats import DatasetStats
from tests.harness.records import build_stats, build_record
from schemas.dataset.generation import Clip

if TYPE_CHECKING:
    from pathlib import Path

HOUR_MINUTE_SECOND = 3661.9
PROMPT_HASH = "f" * 64


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("clips_per_voice", {FIRST_VOICE.name: "two"}),
        ("total_duration_seconds", "an hour"),
        ("prompt_hash", 7),
        ("voices", FIRST_VOICE.name),
        ("duration_per_voice", [1.0]),
    ],
    ids=["count-as-text", "seconds-as-text", "hash-as-number", "voices-as-text", "per-voice-as-list"],
)
def test_wrong_type_named(field: str, value: object) -> None:
    """A field of the wrong type fails to decode, and the message names the field.

    Args:
        field: The field with the wrong type.
        value: The wrong value.

    """
    payload = encode_stats(build_stats())
    payload[field] = value

    with pytest.raises(TypeError, match=field):
        decode_stats(payload)


def test_totals_sum_per_voice(tmp_path: Path) -> None:
    """The stats count and sum the clips under each voice in voice order, with zero for a voice without clips.

    Args:
        tmp_path: The test folder.

    """
    records = [build_record(duration=1.0), build_record(duration=2.5)]
    clips = [Clip(key=f"clip_{index}", audio_path=tmp_path, record=record) for index, record in enumerate(records)]

    stats = build_dataset_stats(clips, [SECOND_VOICE, FIRST_VOICE], 1, PROMPT_HASH, 1)

    assert stats == DatasetStats(
        clip_count=2,
        total_duration_seconds=3.5,
        voices=(SECOND_VOICE.name, FIRST_VOICE.name),
        clips_per_voice={SECOND_VOICE.name: 0, FIRST_VOICE.name: 2},
        duration_per_voice={SECOND_VOICE.name: 0.0, FIRST_VOICE.name: 3.5},
        shard_count=1,
        prompt_hash=PROMPT_HASH,
        prompt_count=1,
    )


def test_stats_rewritten_on_change(tmp_path: Path) -> None:
    """The writer skips a stats file that holds the same stats and rewrites one that holds other stats.

    Args:
        tmp_path: The test folder.

    """
    path = tmp_path / "stats.json"
    earlier = build_stats()
    later = build_stats(clips_per_voice=3)
    write_stats(path, earlier)

    assert not write_stats(path, earlier)
    assert write_stats(path, later)
    assert read_stats(path) == later


def test_duration_drops_fraction() -> None:
    """A duration formats as hours, minutes, and whole seconds."""
    assert format_duration(HOUR_MINUTE_SECOND) == "01:01:01"

"""The dataset card fills its size category, voice table, and usage snippets from the run totals."""

from __future__ import annotations

from dataclasses import replace

import pytest

from src.dataset.hub.card import format_card, select_size_category
from tests.harness.voices import FIRST_VOICE, SECOND_VOICE
from tests.harness.records import build_stats
from tests.suites.unit.builders import DATASET_REPO

ROW_START = "<tr><td>"
ROW_END = "</td></tr>"
CELL_BREAK = "</td><td>"


def _read_voice_rows(card: str) -> list[list[str]]:
    rows = [line.strip() for line in card.splitlines() if line.strip().startswith(ROW_START)]
    return [row.removeprefix(ROW_START).removesuffix(ROW_END).split(CELL_BREAK) for row in rows]


@pytest.mark.parametrize(
    ("clip_count", "category"),
    [(999, "n<1K"), (1_000, "1K<n<10K"), (5_000_000, "100K<n<1M")],
    ids=["below-first-bound", "on-a-bound", "past-every-bound"],
)
def test_size_category_follows_clips(clip_count: int, category: str) -> None:
    """The size category is the first one whose bound is above the clip count, or the largest past every bound.

    Args:
        clip_count: The dataset clip count.
        category: The expected size category.

    """
    assert select_size_category(clip_count) == category


def test_card_describes_dataset() -> None:
    """The front matter carries the size category, and the usage snippets load the repository and every shard."""
    card = format_card(replace(build_stats(), clip_count=20_000, shard_count=3), DATASET_REPO)

    assert "  - 10K<n<100K" in card.split("---\n")[1].splitlines()
    assert f'load_dataset("{DATASET_REPO}")' in card
    assert f"https://huggingface.co/datasets/{DATASET_REPO}/resolve/main/shards/shard-{{000000..000002}}.tar" in card


def test_voice_rows_follow_stats() -> None:
    """The voice table has one row per voice in run order with its totals, then the totals of the run."""
    stats = replace(
        build_stats(),
        clip_count=4,
        total_duration_seconds=35.0,
        voices=(SECOND_VOICE.name, FIRST_VOICE.name),
        clips_per_voice={SECOND_VOICE.name: 3, FIRST_VOICE.name: 1},
        duration_per_voice={SECOND_VOICE.name: 30.0, FIRST_VOICE.name: 5.0},
    )

    assert _read_voice_rows(format_card(stats, DATASET_REPO)) == [
        [SECOND_VOICE.name, SECOND_VOICE.speaker, "3", "00:00:30"],
        [FIRST_VOICE.name, FIRST_VOICE.speaker, "1", "00:00:05"],
        ["All", "", "4", "00:00:35"],
    ]


def test_unknown_voice_escaped() -> None:
    """A voice that the voice table lacks fills its row as escaped text with zero totals."""
    stats = replace(build_stats(), voices=("<b>",))

    assert _read_voice_rows(format_card(stats, DATASET_REPO))[0] == ["&lt;b&gt;", "&lt;b&gt;", "0", "00:00:00"]

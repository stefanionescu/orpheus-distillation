"""Dataset card, rendered from `templates/dataset_card.md`."""

from __future__ import annotations

import html
from string import Template
from typing import TYPE_CHECKING
from pathlib import Path
from datetime import UTC, datetime
import dataclasses

from config.audio import SAMPLE_RATE, PCM_CHANNELS, PCM_SAMPLE_WIDTH_BYTES
from config.shards import (
    SHARDS_FOLDER,
    AUDIO_EXTENSION,
    SHARD_EXTENSION,
    RECORD_EXTENSION,
    SHARD_INDEX_WIDTH,
    SHARD_NAME_PREFIX,
)
from config.voices import VOICES
from schemas.record import Record
from src.dataset.stats import format_duration
from config.dataset.hub import SIZE_CATEGORY_BOUNDS

if TYPE_CHECKING:
    from schemas.dataset.stats import DatasetStats


def _format_voice_row(cells: tuple[str, str, str, str]) -> str:
    return "    <tr>" + "".join(f"<td>{html.escape(cell)}</td>" for cell in cells) + "</tr>"


def _format_voice_rows(stats: DatasetStats) -> str:
    """Format one table row per voice in run order, then a totals row.

    Args:
        stats: Run totals.

    Returns:
        HTML rows of the voice table.

    """
    speakers = {voice.name: voice.speaker for voice in VOICES.values()}
    rows = [
        _format_voice_row(
            (
                voice,
                speakers.get(voice, voice),
                f"{stats.clips_per_voice.get(voice, 0):,}",
                format_duration(stats.duration_per_voice.get(voice, 0.0)),
            )
        )
        for voice in stats.voices
    ]
    rows.append(_format_voice_row(("All", "", f"{stats.clip_count:,}", format_duration(stats.total_duration_seconds))))
    return "\n".join(rows)


def select_size_category(clip_count: int) -> str:
    """Select the Hub size category of a dataset from its clip count.

    Args:
        clip_count: Clip count.

    Returns:
        Category of the first bound above the count, or the largest category.

    """
    return next(
        (category for bound, category in SIZE_CATEGORY_BOUNDS if clip_count < bound), SIZE_CATEGORY_BOUNDS[-1][1]
    )


def format_card(stats: DatasetStats, repo: str) -> str:
    """Format the Hub README from the run totals.

    Args:
        stats: Run totals.
        repo: Repository that the card describes.

    Returns:
        Markdown text of the card.

    """
    template = Template((Path(__file__).with_name("templates") / "dataset_card.md").read_text(encoding="utf-8"))
    record_fields = {f"{field.name}_field": field.name for field in dataclasses.fields(Record)}
    last_shard = max(stats.shard_count - 1, 0)
    return template.substitute(
        record_fields,
        size_category=select_size_category(stats.clip_count),
        voice_rows=_format_voice_rows(stats),
        shards_folder=SHARDS_FOLDER,
        shard_count=stats.shard_count,
        shard_range=f"{SHARD_NAME_PREFIX}{{{0:0{SHARD_INDEX_WIDTH}d}..{last_shard:0{SHARD_INDEX_WIDTH}d}}}{SHARD_EXTENSION}",
        audio_extension=AUDIO_EXTENSION,
        record_extension=RECORD_EXTENSION,
        audio_key=AUDIO_EXTENSION.removeprefix("."),
        record_key=RECORD_EXTENSION.removeprefix("."),
        sample_rate_khz=f"{SAMPLE_RATE / 1000:g}",
        channels=PCM_CHANNELS,
        sample_width_bits=PCM_SAMPLE_WIDTH_BYTES * 8,
        repo=repo,
        year=datetime.now(tz=UTC).year,
    )

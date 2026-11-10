"""The prepare stage turns shard clips into training and validation manifests of the kept clips."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING
import dataclasses

import pytest

from config.shards import SHARD_GLOB, AUDIO_EXTENSION
from tests.harness.shards import write_shard, build_clip_members
from tests.harness.voices import FIRST_VOICE, SECOND_VOICE
from tests.harness.records import CLIP_TEXT, CLIP_SECONDS, build_record
from tests.harness.manifests import build_manifest_entry
from config.models.voxcpm_1_5.data import VAL_MANIFEST_FILE, MAX_DURATION_SECONDS, MIN_DURATION_SECONDS
from src.train.models.voxcpm_1_5.data.manifest import ManifestError, write_manifests, build_manifest_stats

if TYPE_CHECKING:
    from pathlib import Path

    from schemas.record import Record
    from schemas.models.voxcpm_1_5.manifest import ManifestFiles

SHARD_NAME = SHARD_GLOB.replace("*", "000000")
CLIP_KEY = "clip_00000"
DROPPED_KEY = "dropped"
KEPT_RECORD = build_record(SECOND_VOICE)
SPLIT_CLIPS = 4
VAL_SPLIT = 0.25
VAL_CLIPS = 1
HALF_HOUR_SECONDS = 1800.0


def _write_dataset(dataset_folder: Path, records: dict[str, Record]) -> None:
    write_shard(dataset_folder / SHARD_NAME, build_clip_members(records))


def _write_manifests(tmp_path: Path, records: dict[str, Record], val_split: float) -> ManifestFiles:
    _write_dataset(tmp_path / "dataset", records)
    return write_manifests(tmp_path / "dataset", tmp_path / "manifests", val_split)


def _read_lines(manifest_path: Path | None) -> list[dict[str, object]]:
    if manifest_path is None:
        return []
    return [json.loads(line) for line in manifest_path.read_text(encoding="utf-8").splitlines()]


def test_kept_text_trimmed(tmp_path: Path) -> None:
    """A kept clip's entry holds its text without the spaces and line breaks around it.

    Args:
        tmp_path: The test folder.

    """
    files = _write_manifests(tmp_path, {CLIP_KEY: build_record(SECOND_VOICE, text=f"  {CLIP_TEXT}\n")}, 0.0)

    assert [line["text"] for line in _read_lines(files.train_manifest_path)] == [CLIP_TEXT]


def test_bound_durations_kept(tmp_path: Path) -> None:
    """A clip exactly as long as the shortest or the longest length that training takes stays in the manifest.

    Args:
        tmp_path: The test folder.

    """
    records = {
        "shortest": build_record(FIRST_VOICE, duration=MIN_DURATION_SECONDS),
        "longest": build_record(FIRST_VOICE, duration=MAX_DURATION_SECONDS),
    }

    files = _write_manifests(tmp_path, records, 0.0)

    durations = [line["duration"] for line in _read_lines(files.train_manifest_path)]
    assert durations == [MIN_DURATION_SECONDS, MAX_DURATION_SECONDS]


@pytest.mark.parametrize(
    "dropped",
    [
        dataclasses.replace(build_record(FIRST_VOICE), speaker=FIRST_VOICE.name),
        build_record(FIRST_VOICE, text="  "),
        build_record(FIRST_VOICE, duration=MIN_DURATION_SECONDS / 2),
        build_record(FIRST_VOICE, duration=MAX_DURATION_SECONDS * 2),
    ],
    ids=["unknown-speaker", "empty-text", "too-short", "too-long"],
)
def test_filtered_clip_dropped(tmp_path: Path, dropped: Record) -> None:
    """A clip training cannot use leaves no entry and no WAV file, and the kept clip remains.

    Args:
        tmp_path: The test folder.
        dropped: The record the filters drop.

    """
    files = _write_manifests(tmp_path, {CLIP_KEY: KEPT_RECORD, DROPPED_KEY: dropped}, 0.0)

    assert [line["voice"] for line in _read_lines(files.train_manifest_path)] == [SECOND_VOICE.name]
    assert not list(tmp_path.joinpath("manifests").rglob(f"{DROPPED_KEY}{AUDIO_EXTENSION}"))


def test_split_repeats_per_seed(tmp_path: Path) -> None:
    """The validation share of the clips leaves training, each clip lands once, and a second run splits the same way.

    Args:
        tmp_path: The test folder.

    """
    records = {f"clip_{index:05d}": build_record(FIRST_VOICE, text=f"text {index}") for index in range(SPLIT_CLIPS)}
    _write_dataset(tmp_path / "dataset", records)

    first = write_manifests(tmp_path / "dataset", tmp_path / "first", VAL_SPLIT)
    second = write_manifests(tmp_path / "dataset", tmp_path / "second", VAL_SPLIT)

    train_texts = [str(line["text"]) for line in _read_lines(first.train_manifest_path)]
    val_texts = [str(line["text"]) for line in _read_lines(first.val_manifest_path)]
    assert len(val_texts) == VAL_CLIPS
    assert sorted(train_texts + val_texts) == sorted(record.text for record in records.values())
    assert val_texts == [line["text"] for line in _read_lines(second.val_manifest_path)]


def test_stale_val_manifest_deleted(tmp_path: Path) -> None:
    """A run without validation deletes an earlier validation manifest, so training cannot read it.

    Args:
        tmp_path: The test folder.

    """
    _write_manifests(tmp_path, {CLIP_KEY: KEPT_RECORD, DROPPED_KEY: KEPT_RECORD}, 0.5)

    files = write_manifests(tmp_path / "dataset", tmp_path / "manifests", 0.0)

    assert files.val_manifest_path is None
    assert not tmp_path.joinpath("manifests", VAL_MANIFEST_FILE).exists()


def test_no_kept_clip_raises(tmp_path: Path) -> None:
    """Shards whose clips all fail the filters stop the prepare stage before it writes a manifest.

    Args:
        tmp_path: The test folder.

    """
    with pytest.raises(ManifestError):
        _write_manifests(tmp_path, {CLIP_KEY: build_record(FIRST_VOICE, text="")}, 0.0)

    assert not list(tmp_path.joinpath("manifests").glob("*.jsonl"))


def test_stats_count_each_voice() -> None:
    """The totals count clips and hours per voice and overall."""
    entries = [build_manifest_entry(FIRST_VOICE, duration=HALF_HOUR_SECONDS)] * 2 + [build_manifest_entry(SECOND_VOICE)]

    stats = build_manifest_stats(entries)

    assert (stats.clip_count, stats.clips_per_voice) == (3, {FIRST_VOICE.name: 2, SECOND_VOICE.name: 1})
    assert stats.hours_per_voice == {FIRST_VOICE.name: 1.0, SECOND_VOICE.name: CLIP_SECONDS / 3600}
    assert stats.hours == (2 * HALF_HOUR_SECONDS + CLIP_SECONDS) / 3600

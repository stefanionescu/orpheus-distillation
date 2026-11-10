"""The training command finds a snapshot's shards and reads each clip as WAV bytes and a record."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING
import logging
import dataclasses

import pytest

from config.shards import SHARD_GLOB, SHARDS_FOLDER, AUDIO_EXTENSION, RECORD_EXTENSION
from src.train.shards import list_shards, read_shard_clips
from tests.harness.shards import write_shard, encode_record, build_clip_members
from tests.harness.voices import FIRST_VOICE, SECOND_VOICE
from tests.harness.records import build_record

if TYPE_CHECKING:
    from pathlib import Path

FIRST_SHARD = SHARD_GLOB.replace("*", "000000")
SECOND_SHARD = SHARD_GLOB.replace("*", "000001")
SORTED_SHARD_COUNT = 7
FIELDS = dataclasses.asdict(build_record(FIRST_VOICE))


def test_shards_folder_wins(tmp_path: Path) -> None:
    """A snapshot with a shards folder reads the shards inside it and ignores TAR files at its root.

    Args:
        tmp_path: The test folder.

    """
    nested_shard = write_shard(tmp_path / SHARDS_FOLDER / SECOND_SHARD, {})
    write_shard(tmp_path / FIRST_SHARD, {})

    assert list_shards(tmp_path) == [nested_shard]


def test_flat_layout_sorted(tmp_path: Path) -> None:
    """A snapshot without a shards folder reads its root shards in name order, whatever order the folder lists.

    Enough shards make a file system that lists names by hash disagree with the name order.

    Args:
        tmp_path: The test folder.

    """
    names = [SHARD_GLOB.replace("*", f"{index:06d}") for index in range(SORTED_SHARD_COUNT)]
    shard_paths = [write_shard(tmp_path / name, {}) for name in reversed(names)]

    assert list_shards(tmp_path) == sorted(shard_paths)


def test_clips_pair_members(tmp_path: Path) -> None:
    """Each clip yields its key, WAV bytes, and record, in shard order.

    Args:
        tmp_path: The test folder.

    """
    records = {"clip_00000": build_record(FIRST_VOICE), "clip_00001": build_record(SECOND_VOICE)}
    members = build_clip_members(records)
    shard_path = write_shard(tmp_path / FIRST_SHARD, members)

    clips = list(read_shard_clips(shard_path))

    assert clips == [(key, members[f"{key}{AUDIO_EXTENSION}"], record) for key, record in records.items()]


def test_orphan_record_skipped(tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
    """The reader skips a record without its WAV member, warns with the clip name, and reads the other clips.

    Args:
        tmp_path: The test folder.
        caplog: Captures log records.

    """
    members = build_clip_members({"clip_00000": build_record(FIRST_VOICE)})
    members[f"orphan{RECORD_EXTENSION}"] = encode_record(build_record(SECOND_VOICE))
    shard_path = write_shard(tmp_path / FIRST_SHARD, members)

    with caplog.at_level(logging.WARNING):
        keys = [key for key, _, _ in read_shard_clips(shard_path)]

    assert keys == ["clip_00000"]
    assert [record.args[0] for record in caplog.records if isinstance(record.args, tuple)] == ["orphan"]


@pytest.mark.parametrize(
    "payload",
    [
        b"{not json",
        b"[]",
        json.dumps({key: FIELDS[key] for key in FIELDS if key != "duration"}).encode(),
        json.dumps(FIELDS | {"text": 3}).encode(),
        json.dumps(FIELDS | {"duration": str(FIELDS["duration"])}).encode(),
    ],
    ids=["not-json", "not-an-object", "missing-field", "text-not-string", "duration-as-text"],
)
def test_bad_record_skipped(tmp_path: Path, payload: bytes) -> None:
    """The reader skips a clip whose record member does not decode to a full record.

    Args:
        tmp_path: The test folder.
        payload: The bad record bytes.

    """
    members = build_clip_members({"clip_00000": build_record(FIRST_VOICE)})
    members[f"clip_00000{RECORD_EXTENSION}"] = payload

    assert list(read_shard_clips(write_shard(tmp_path / FIRST_SHARD, members))) == []


def test_dotfiles_skipped(tmp_path: Path) -> None:
    """Hidden members, such as the metadata files macOS adds to an archive, are no clips.

    Args:
        tmp_path: The test folder.

    """
    members = build_clip_members({"._clip_00000": build_record(FIRST_VOICE)})

    assert list(read_shard_clips(write_shard(tmp_path / FIRST_SHARD, members))) == []

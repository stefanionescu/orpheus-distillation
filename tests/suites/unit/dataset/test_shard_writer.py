"""The shard writer packs clips in order into fixed-size TAR files, with a JSON record per clip."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING
import tarfile
import dataclasses

import pytest

from src.dataset.shards import write_shards
from tests.harness.voices import SECOND_VOICE
from tests.harness.records import write_clip, build_record
from tests.suites.unit.builders import PROMPT

if TYPE_CHECKING:
    from pathlib import Path

    from schemas.dataset.generation import Clip

CLIPS_PER_SHARD = 2
UNICODE_PROMPT = "Café, naïve, 東京."


def _write_clips(tmp_path: Path, count: int) -> list[Clip]:
    return [
        write_clip(tmp_path / "audio", f"clip_{index:05d}", build_record(text=f"{PROMPT} {index}"))
        for index in range(count)
    ]


def _read_members(shard_path: Path) -> list[str]:
    with tarfile.open(shard_path) as archive:
        return archive.getnames()


def test_full_shard_stays_one(tmp_path: Path) -> None:
    """A full shard of clips makes one shard with a WAV and a record per clip, in order.

    Args:
        tmp_path: The test folder.

    """
    shards_folder = tmp_path / "shards"

    shard_count = write_shards(_write_clips(tmp_path, CLIPS_PER_SHARD), shards_folder, CLIPS_PER_SHARD)

    assert shard_count == 1
    assert _read_members(shards_folder / "shard-000000.tar") == [
        "clip_00000.wav",
        "clip_00000.json",
        "clip_00001.wav",
        "clip_00001.json",
    ]


def test_extra_clip_opens_shard(tmp_path: Path) -> None:
    """One clip past a full shard goes alone into a second shard.

    Args:
        tmp_path: The test folder.

    """
    shards_folder = tmp_path / "shards"

    shard_count = write_shards(_write_clips(tmp_path, CLIPS_PER_SHARD + 1), shards_folder, CLIPS_PER_SHARD)

    assert sorted(path.name for path in shards_folder.iterdir()) == ["shard-000000.tar", "shard-000001.tar"]
    assert shard_count == len(list(shards_folder.iterdir()))
    assert _read_members(shards_folder / "shard-000001.tar") == ["clip_00002.wav", "clip_00002.json"]


def test_members_hold_clip_data(tmp_path: Path) -> None:
    """The WAV member holds the file bytes, and the record member holds exactly the record fields, non-ASCII text too.

    Args:
        tmp_path: The test folder.

    """
    clip = write_clip(tmp_path / "audio", "clip_00000", build_record(SECOND_VOICE, text=UNICODE_PROMPT))
    shards_folder = tmp_path / "shards"

    write_shards([clip], shards_folder, CLIPS_PER_SHARD)

    with tarfile.open(shards_folder / "shard-000000.tar") as archive:
        audio_member = archive.extractfile("clip_00000.wav")
        record_member = archive.extractfile("clip_00000.json")
        assert audio_member is not None
        assert record_member is not None
        assert audio_member.read() == clip.audio_path.read_bytes()
        assert json.loads(record_member.read()) == dataclasses.asdict(clip.record)


def test_missing_audio_leaves_nothing(tmp_path: Path) -> None:
    """A clip whose WAV file is gone fails the write and leaves neither a shard nor a temporary file.

    Args:
        tmp_path: The test folder.

    """
    clips = _write_clips(tmp_path, 1)
    clips[0].audio_path.unlink()
    shards_folder = tmp_path / "shards"

    with pytest.raises(FileNotFoundError):
        write_shards(clips, shards_folder, CLIPS_PER_SHARD)

    assert list(shards_folder.iterdir()) == []


def test_existing_shard_refused(tmp_path: Path) -> None:
    """The writer refuses a folder that already holds a shard, so two runs never mix.

    Args:
        tmp_path: The test folder.

    """
    shards_folder = tmp_path / "shards"
    shards_folder.mkdir()
    (shards_folder / "shard-000000.tar").write_bytes(b"")

    with pytest.raises(FileExistsError):
        write_shards(_write_clips(tmp_path, 1), shards_folder, CLIPS_PER_SHARD)

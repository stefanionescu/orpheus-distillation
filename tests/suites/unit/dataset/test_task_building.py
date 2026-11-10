"""A run pairs every prompt with every voice under stable clip numbers and prepares its output folders."""

from __future__ import annotations

from typing import TYPE_CHECKING

from tests.harness.tasks import build_prompt_list
from tests.harness.voices import FIRST_VOICE, SECOND_VOICE, TABLE_VOICES
from src.dataset.generation.tasks import build_tasks, build_output_folders, prepare_output_folders

if TYPE_CHECKING:
    from pathlib import Path

PROMPT_COUNT = 3


def test_clips_numbered_by_prompt(tmp_path: Path) -> None:
    """The clip number counts prompts times voices plus the voice position, and the file name ends with the speaker.

    Args:
        tmp_path: The test folder.

    """
    tasks, pending = build_tasks(build_prompt_list(PROMPT_COUNT), TABLE_VOICES, tmp_path, set())

    assert [task.key for task in tasks] == [f"clip_{number:05d}" for number in range(PROMPT_COUNT * 2)]
    assert [task.voice for task in tasks[:2]] == [FIRST_VOICE, SECOND_VOICE]
    assert tasks[3].audio_path == tmp_path / f"clip_00003_{SECOND_VOICE.speaker}.wav"
    assert pending == tasks


def test_existing_clips_skipped(tmp_path: Path) -> None:
    """An existing clip stays in the task list and leaves the pending list; every other clip is pending.

    Args:
        tmp_path: The test folder.

    """
    existing = {(0, FIRST_VOICE.speaker), (2, SECOND_VOICE.speaker)}

    tasks, pending = build_tasks(build_prompt_list(PROMPT_COUNT), TABLE_VOICES, tmp_path, existing)

    assert len(tasks) == PROMPT_COUNT * len(TABLE_VOICES)
    assert [task.key for task in pending] == ["clip_00001", "clip_00002", "clip_00003", "clip_00004"]


def test_fresh_run_cleans_folder(tmp_path: Path) -> None:
    """A run without resume deletes all earlier output and creates empty folders.

    Args:
        tmp_path: The test folder.

    """
    folders = build_output_folders(tmp_path / "output")
    folders.audio_folder.mkdir(parents=True)
    (folders.audio_folder / "clip_00000_tara.wav").write_bytes(b"old")
    folders.stats_path.write_text("{}", encoding="utf-8")

    prepare_output_folders(folders, resume=False)

    assert sorted(path.name for path in folders.root.iterdir()) == ["audio", "shards"]
    assert list(folders.audio_folder.iterdir()) == []


def test_resume_keeps_audio(tmp_path: Path) -> None:
    """A resumed run keeps the audio and the stats file and deletes the shards, which it writes again.

    Args:
        tmp_path: The test folder.

    """
    folders = build_output_folders(tmp_path / "output")
    folders.audio_folder.mkdir(parents=True)
    folders.shards_folder.mkdir()
    clip_path = folders.audio_folder / "clip_00000_tara.wav"
    clip_path.write_bytes(b"kept")
    (folders.shards_folder / "shard-000000.tar").write_bytes(b"old")
    folders.stats_path.write_text("{}", encoding="utf-8")

    prepare_output_folders(folders, resume=True)

    assert clip_path.read_bytes() == b"kept"
    assert folders.stats_path.exists()
    assert list(folders.shards_folder.iterdir()) == []

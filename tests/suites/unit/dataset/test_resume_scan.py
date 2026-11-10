"""A resumed run lists the earlier run's clips and deletes the unreadable ones, so it synthesizes them again."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.harness.audio import write_wav_file
from tests.harness.tasks import build_generation_tasks
from tests.harness.voices import FIRST_VOICE, SECOND_VOICE, TABLE_VOICES
from tests.suites.unit.builders import TONE_SECONDS
from src.dataset.generation.resume import list_existing_clips

if TYPE_CHECKING:
    from pathlib import Path

PROMPT_COUNT = 2
UNREADABLE = b"not a wav file"


def _write_all_clips(audio_folder: Path) -> None:
    for task in build_generation_tasks(audio_folder, PROMPT_COUNT):
        write_wav_file(task.audio_path, TONE_SECONDS)


def test_clips_listed_by_prompt(tmp_path: Path) -> None:
    """Each clip file maps back to the prompt index and speaker that numbered it.

    Args:
        tmp_path: The test folder.

    """
    _write_all_clips(tmp_path)

    assert list_existing_clips(tmp_path, TABLE_VOICES) == {
        (0, FIRST_VOICE.speaker),
        (0, SECOND_VOICE.speaker),
        (1, FIRST_VOICE.speaker),
        (1, SECOND_VOICE.speaker),
    }


def test_foreign_files_kept(tmp_path: Path) -> None:
    """The scan neither lists nor deletes a file whose name fits no clip of this run, even an unreadable one.

    Args:
        tmp_path: The test folder.

    """
    names = [
        f"00000_{FIRST_VOICE.speaker}.wav",
        f"clip_00001_{FIRST_VOICE.speaker}.wav",
        "clip_00002_stranger.wav",
        f"clip_first_{FIRST_VOICE.speaker}.wav",
    ]
    for name in names:
        (tmp_path / name).write_bytes(UNREADABLE)

    assert list_existing_clips(tmp_path, TABLE_VOICES) == set()
    assert sorted(path.name for path in tmp_path.iterdir()) == sorted(names)


@pytest.mark.parametrize("damage", ["header-only", "truncated"])
def test_unreadable_clip_deleted(tmp_path: Path, damage: str) -> None:
    """The scan deletes a clip with only a header or fewer frames than its header announces, and lists the rest.

    Args:
        tmp_path: The test folder.
        damage: How the clip file is broken.

    """
    _write_all_clips(tmp_path)
    broken_path = tmp_path / f"clip_00002_{FIRST_VOICE.speaker}.wav"
    damaged = {"header-only": b"RIFF", "truncated": broken_path.read_bytes()[:-2]}
    broken_path.write_bytes(damaged[damage])

    existing = list_existing_clips(tmp_path, TABLE_VOICES)

    assert existing == {(0, FIRST_VOICE.speaker), (0, SECOND_VOICE.speaker), (1, SECOND_VOICE.speaker)}
    assert not broken_path.exists()

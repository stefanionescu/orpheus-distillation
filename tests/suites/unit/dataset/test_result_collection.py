"""A resumed run measures each existing clip again from its WAV file, and stops on one it cannot read."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from src.dataset.errors import GenerationError
from tests.harness.audio import write_wav_file
from tests.harness.tasks import build_generation_tasks
from tests.suites.unit.builders import TONE_SECONDS, SILENCE_SECONDS, SILENCE_TOLERANCE_MS
from src.dataset.generation.clips import read_existing_clips

if TYPE_CHECKING:
    from pathlib import Path


def test_existing_clips_measured(tmp_path: Path) -> None:
    """The reader reads only existing clips and builds each record from the task and the measured WAV file.

    Args:
        tmp_path: The test folder.

    """
    tasks = build_generation_tasks(tmp_path, 2)
    existing = tasks[1]
    write_wav_file(existing.audio_path, TONE_SECONDS, silence_seconds=SILENCE_SECONDS)

    clips = read_existing_clips(tasks, {(existing.prompt_index, existing.voice.speaker)})

    assert [clip.key for clip in clips] == [existing.key]
    record = clips[0].record
    assert (record.text, record.speaker, record.voice) == (existing.prompt, existing.voice.speaker, existing.voice.name)
    assert record.duration == TONE_SECONDS + SILENCE_SECONDS
    assert abs(record.leading_silence_ms - SILENCE_SECONDS * 1000) <= SILENCE_TOLERANCE_MS


def test_unreadable_existing_clip_fails(tmp_path: Path) -> None:
    """An existing clip that turns unreadable after the scan stops the run and names the file.

    Args:
        tmp_path: The test folder.

    """
    task = build_generation_tasks(tmp_path, 1)[0]
    task.audio_path.write_bytes(b"not a wav file")

    with pytest.raises(GenerationError, match=task.audio_path.name):
        read_existing_clips([task], {(task.prompt_index, task.voice.speaker)})

"""Clips of a run: new ones from their records, existing ones measured again from disk."""

from __future__ import annotations

import wave
from typing import TYPE_CHECKING

from schemas.record import Record
from src.dataset.errors import GenerationError
from src.dataset.audio.wav import read_wav, get_duration_seconds
from src.dataset.audio.silence import detect_leading_silence_ms
from schemas.dataset.generation import Clip

if TYPE_CHECKING:
    from collections.abc import Set as AbstractSet
    from collections.abc import Sequence

    from schemas.dataset.generation import GenerationTask


def _read_clip(task: GenerationTask) -> Clip:
    """Measure an existing WAV file and build its record.

    Args:
        task: Task whose clip an earlier run wrote.

    Returns:
        The clip.

    Raises:
        GenerationError: The WAV file fails to read after `list_existing_clips` accepted it.

    """
    try:
        audio = read_wav(task.audio_path)
    except (OSError, EOFError, wave.Error) as error:
        message = f"Cannot read the existing clip {task.audio_path}"
        raise GenerationError(message) from error
    record = Record(
        text=task.prompt,
        speaker=task.voice.speaker,
        voice=task.voice.name,
        duration=get_duration_seconds(audio),
        leading_silence_ms=detect_leading_silence_ms(audio.frames, audio.sample_rate),
    )
    return build_clip(task, record)


def build_clip(task: GenerationTask, record: Record) -> Clip:
    """Build the clip of a task, under the task key.

    Args:
        task: Task that wrote the WAV file.
        record: Clip record.

    Returns:
        The clip.

    """
    return Clip(key=task.key, audio_path=task.audio_path, record=record)


def read_existing_clips(tasks: Sequence[GenerationTask], existing_clips: AbstractSet[tuple[int, str]]) -> list[Clip]:
    """Read the clips that a resumed run keeps.

    Args:
        tasks: All tasks of the run.
        existing_clips: Prompt index and speaker of each existing clip.

    Returns:
        The existing clips, in task order.

    """
    return [_read_clip(task) for task in tasks if (task.prompt_index, task.voice.speaker) in existing_clips]

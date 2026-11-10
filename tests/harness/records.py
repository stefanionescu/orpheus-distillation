"""Records and clips with fixed values."""

from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.record import Record
from tests.harness.audio import write_wav_file
from tests.harness.voices import FIRST_VOICE, SECOND_VOICE
from schemas.dataset.stats import DatasetStats
from schemas.dataset.generation import Clip

if TYPE_CHECKING:
    from pathlib import Path

    from schemas.voice import Voice

CLIP_TEXT = "hello there"
CLIP_SECONDS = 1.0


def build_record(voice: Voice = FIRST_VOICE, *, text: str = CLIP_TEXT, duration: float = CLIP_SECONDS) -> Record:
    """Build a clip's record as the dataset command stores it.

    Args:
        voice: The clip's voice; the record stores it and its speaker.
        text: The prompt.
        duration: The clip length in seconds.

    Returns:
        The record, with no leading silence.

    """
    return Record(text=text, speaker=voice.speaker, voice=voice.name, duration=duration, leading_silence_ms=0.0)


def write_clip(audio_folder: Path, key: str, record: Record) -> Clip:
    """Write a real WAV file for a clip and return the clip.

    Args:
        audio_folder: Where the WAV file goes.
        key: The stem of the file and the shard members.
        record: The clip record; its duration sets the tone length.

    Returns:
        The clip.

    """
    audio_path = audio_folder / f"{key}.wav"
    write_wav_file(audio_path, record.duration)
    return Clip(key=key, audio_path=audio_path, record=record)


def build_stats(clips_per_voice: int = 2, *, prompt_hash: str = "0" * 64) -> DatasetStats:
    """Build the stats of a run of the first two voices, one clip per voice and prompt.

    Args:
        clips_per_voice: Clips per voice, one per prompt.
        prompt_hash: The hash of the prompt list.

    Returns:
        The stats.

    """
    voices = (FIRST_VOICE.name, SECOND_VOICE.name)
    return DatasetStats(
        clip_count=clips_per_voice * len(voices),
        total_duration_seconds=clips_per_voice * len(voices) * CLIP_SECONDS,
        voices=voices,
        clips_per_voice=dict.fromkeys(voices, clips_per_voice),
        duration_per_voice=dict.fromkeys(voices, clips_per_voice * CLIP_SECONDS),
        shard_count=1,
        prompt_hash=prompt_hash,
        prompt_count=clips_per_voice,
    )

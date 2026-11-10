"""Tasks, clips, folders, and fingerprint of a dataset run."""

from __future__ import annotations

from typing import TYPE_CHECKING
from dataclasses import dataclass

if TYPE_CHECKING:
    from pathlib import Path

    from schemas.voice import Voice
    from schemas.record import Record


@dataclass(frozen=True)
class GenerationTask:
    """One prompt that one voice reads aloud.

    Attributes:
        key: Stem that names the audio file and the shard members.
        prompt_index: Position in the prompt list.
        prompt: Text to read aloud.
        voice: Voice that reads the prompt.
        audio_path: WAV file to write.

    """

    key: str
    prompt_index: int
    prompt: str
    voice: Voice
    audio_path: Path


@dataclass(frozen=True)
class Clip:
    """A WAV file and the record that goes beside it in a shard.

    Attributes:
        key: Stem of both shard members, equal to the task key.
        audio_path: WAV file on disk.
        record: Record of the clip.

    """

    key: str
    audio_path: Path
    record: Record


@dataclass(frozen=True)
class OutputFolders:
    """Paths that one dataset run writes.

    Attributes:
        root: Output folder that holds the rest.
        audio_folder: Folder of the WAV files.
        shards_folder: Folder of the shards.
        stats_path: Stats file that the run writes at the end.
        fingerprint_path: Fingerprint file that the run writes before its first clip.

    """

    root: Path
    audio_folder: Path
    shards_folder: Path
    stats_path: Path
    fingerprint_path: Path


@dataclass(frozen=True)
class Fingerprint:
    """What a resumed run must match. Each field name is a key of the fingerprint file.

    Attributes:
        prompt_hash: Hash of the prompt list.
        prompt_count: Prompt count.
        voices: Voices, in the order that numbered the clips.

    """

    prompt_hash: str
    prompt_count: int
    voices: tuple[str, ...]

"""Resume checks: the fingerprint matches the earlier run and each existing clip reads."""

from __future__ import annotations

import wave
from typing import TYPE_CHECKING
import hashlib
import logging

from src.dataset.stats import read_stats, read_fingerprint
from src.dataset.errors import GenerationError
from config.dataset.paths import KEY_PREFIX, AUDIO_FILE_GLOB
from src.dataset.audio.wav import read_wav
from schemas.dataset.generation import Fingerprint

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Sequence

    from schemas.voice import Voice
    from schemas.dataset.generation import OutputFolders

logger = logging.getLogger(__name__)


def _parse_clip_name(stem: str, speakers: Sequence[str]) -> tuple[int, str] | None:
    """Read the prompt index and the speaker from a clip file name.

    Args:
        stem: File name without extension, such as `clip_00003_zac`.
        speakers: Speakers, in voice order.

    Returns:
        Prompt index and speaker, or None when the name does not fit this run.

    """
    number, _, speaker = stem.removeprefix(KEY_PREFIX).rpartition("_")
    if not stem.startswith(KEY_PREFIX) or speaker not in speakers or not number.isdigit():
        return None
    prompt_index, voice_index = divmod(int(number), len(speakers))
    if voice_index != speakers.index(speaker):
        return None
    return prompt_index, speaker


def _is_readable_clip(path: Path) -> bool:
    try:
        read_wav(path)
    except (OSError, EOFError, wave.Error):
        return False
    return True


def build_fingerprint(prompts: Sequence[str], voices: Sequence[Voice]) -> Fingerprint:
    """Build the fingerprint that a later `--resume` run must match.

    Args:
        prompts: Prompts after the `--max-prompts` cut.
        voices: Voices, in order.

    Returns:
        Prompt hash, prompt count, and voices in order.

    """
    return Fingerprint(
        prompt_hash=hashlib.sha256("\n".join(prompts).encode("utf-8")).hexdigest(),
        prompt_count=len(prompts),
        voices=tuple(voice.name for voice in voices),
    )


def read_existing_fingerprint(folders: OutputFolders) -> Fingerprint | None:
    """Read the fingerprint of the run that wrote an output folder.

    Without a fingerprint file, fall back to the stats file, which holds the same fields.

    Args:
        folders: Run paths.

    Returns:
        Earlier fingerprint, or None when neither file exists.

    """
    if folders.fingerprint_path.exists():
        return read_fingerprint(folders.fingerprint_path)
    if not folders.stats_path.exists():
        return None
    stats = read_stats(folders.stats_path)
    return Fingerprint(prompt_hash=stats.prompt_hash, prompt_count=stats.prompt_count, voices=stats.voices)


def assert_fingerprint_matches(existing: Fingerprint, current: Fingerprint) -> None:
    """Stop a resumed run whose prompts or voices differ from the earlier run.

    Args:
        existing: Fingerprint of the earlier run.
        current: Fingerprint of this run.

    Raises:
        GenerationError: The prompts, their number, or the voice order changed.

    """
    if (existing.prompt_hash, existing.prompt_count) != (current.prompt_hash, current.prompt_count):
        message = "Resume failed: prompts changed since the last run; run without --resume"
        raise GenerationError(message)
    if existing.voices != current.voices:
        message = (
            f"Resume failed: voice order changed from {', '.join(existing.voices)} to {', '.join(current.voices)}; "
            "run without --resume"
        )
        raise GenerationError(message)


def list_existing_clips(audio_folder: Path, voices: Sequence[Voice]) -> set[tuple[int, str]]:
    """List the clips of an earlier run, deleting unreadable ones so the run synthesizes them again.

    The function ignores and keeps any file whose name does not fit `AUDIO_FILE_TEMPLATE` for this run.

    Args:
        audio_folder: Folder of the WAV files. A missing folder counts as empty.
        voices: Voices, in the order that numbered the clips.

    Returns:
        Prompt index and speaker of each readable clip.

    """
    speakers = [voice.speaker for voice in voices]
    clips: set[tuple[int, str]] = set()
    for audio_path in sorted(audio_folder.glob(AUDIO_FILE_GLOB)):
        clip = _parse_clip_name(audio_path.stem, speakers)
        if clip is None:
            continue
        if _is_readable_clip(audio_path):
            clips.add(clip)
            continue
        logger.warning("Deleting the unreadable clip %s; the run synthesizes it again", audio_path)
        audio_path.unlink()
    return clips

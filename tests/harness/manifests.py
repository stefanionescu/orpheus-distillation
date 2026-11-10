"""Manifest entries with fixed values, and manifests backed by real WAV files."""

from __future__ import annotations

from typing import TYPE_CHECKING

from tests.harness.shards import encode_tone_wav
from tests.harness.records import CLIP_TEXT, CLIP_SECONDS
from schemas.models.voxcpm_1_5.manifest import ManifestEntry
from src.train.models.voxcpm_1_5.data.manifest import write_manifest

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Sequence

    from schemas.voice import Voice


def build_manifest_entry(voice: Voice, *, duration: float = CLIP_SECONDS, text: str = CLIP_TEXT) -> ManifestEntry:
    """Build a manifest entry whose WAV file does not exist.

    Args:
        voice: The clip's voice.
        duration: The clip length in seconds.
        text: The clip text.

    Returns:
        The entry.

    """
    return ManifestEntry(audio=f"{voice.name}.wav", text=text, duration=duration, voice=voice.name)


def write_clip_manifest(
    manifest_path: Path, clips: Sequence[tuple[Voice, float]], sample_rate: int
) -> list[ManifestEntry]:
    """Write a WAV tone per clip and a manifest that lists them.

    Args:
        manifest_path: The manifest file; the WAV files go beside it.
        clips: The voice and length in seconds of each clip.
        sample_rate: The WAV sample rate.

    Returns:
        The manifest entries.

    """
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    entries: list[ManifestEntry] = []
    for index, (voice, seconds) in enumerate(clips):
        audio_path = manifest_path.with_name(f"clip_{index:05d}.wav")
        audio_path.write_bytes(encode_tone_wav(seconds, sample_rate))
        entries.append(ManifestEntry(audio=str(audio_path), text=CLIP_TEXT, duration=seconds, voice=voice.name))
    write_manifest(entries, manifest_path)
    return entries

"""Mono 16-bit PCM WAV files."""

from __future__ import annotations

import wave
from typing import TYPE_CHECKING

from config.audio import PCM_CHANNELS, PCM_SAMPLE_WIDTH_BYTES
from schemas.dataset.audio import PcmAudio

if TYPE_CHECKING:
    from pathlib import Path


def write_wav(audio: PcmAudio, path: Path) -> None:
    """Write the audio through a temporary file, so an interrupted write leaves no partial WAV.

    Args:
        audio: Audio to write.
        path: Target WAV file. The function creates its folder when missing.

    """
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = path.with_name(f"{path.name}.tmp")
    try:
        with temporary_path.open("wb") as handle, wave.open(handle, "wb") as wav_file:
            wav_file.setnchannels(PCM_CHANNELS)
            wav_file.setsampwidth(PCM_SAMPLE_WIDTH_BYTES)
            wav_file.setframerate(audio.sample_rate)
            wav_file.writeframes(audio.frames)
        temporary_path.replace(path)
    finally:
        temporary_path.unlink(missing_ok=True)


def read_wav(path: Path) -> PcmAudio:
    """Read a WAV file and check that it holds every frame its header announces.

    Args:
        path: WAV file to read.

    Returns:
        The audio.

    Raises:
        wave.Error: The file is not a WAV file, or it is truncated.

    """
    with path.open("rb") as handle, wave.open(handle, "rb") as wav_file:
        expected_size = wav_file.getnframes() * wav_file.getsampwidth() * wav_file.getnchannels()
        frames = wav_file.readframes(wav_file.getnframes())
        if len(frames) < expected_size:
            message = f"{path} ends after {len(frames)} of {expected_size} audio bytes"
            raise wave.Error(message)
        return PcmAudio(frames=frames, sample_rate=wav_file.getframerate())


def get_duration_seconds(audio: PcmAudio) -> float:
    """Get the length of mono 16-bit audio from its byte count.

    Args:
        audio: Audio to measure.

    Returns:
        The length in seconds.

    """
    return len(audio.frames) / PCM_SAMPLE_WIDTH_BYTES / audio.sample_rate

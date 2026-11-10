"""Audio builders: silence then a steady tone, as PCM bytes or a WAV file."""

from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np

from config.audio import SAMPLE_RATE
from schemas.dataset.audio import PcmAudio
from src.dataset.audio.wav import write_wav

if TYPE_CHECKING:
    from pathlib import Path

TONE_FREQUENCY_HZ = 440.0
TONE_AMPLITUDE = 16_000


def build_tone(seconds: float) -> np.ndarray[tuple[int], np.dtype[np.int16]]:
    """Build a tone loud enough for the silence detector to call it speech.

    Args:
        seconds: The tone length.

    Returns:
        The samples.

    """
    times = np.arange(round(seconds * SAMPLE_RATE)) / SAMPLE_RATE
    return (np.sin(2 * np.pi * TONE_FREQUENCY_HZ * times) * TONE_AMPLITUDE).astype(np.int16)


def build_silence(seconds: float) -> np.ndarray[tuple[int], np.dtype[np.int16]]:
    """Build digital silence.

    Args:
        seconds: The silence length.

    Returns:
        The zero samples.

    """
    return np.zeros(round(seconds * SAMPLE_RATE), dtype=np.int16)


def build_audio(seconds: float, *, silence_seconds: float = 0.0) -> PcmAudio:
    """Build silence then a tone at the dataset sample rate.

    Args:
        seconds: The tone length.
        silence_seconds: The silence before the tone.

    Returns:
        The PCM audio.

    """
    samples = np.concatenate([build_silence(silence_seconds), build_tone(seconds)])
    return PcmAudio(frames=samples.tobytes(), sample_rate=SAMPLE_RATE)


def write_wav_file(path: Path, seconds: float, *, silence_seconds: float = 0.0) -> PcmAudio:
    """Write silence then a tone as a real WAV file with the dataset writer.

    Args:
        path: The WAV file.
        seconds: The tone length.
        silence_seconds: The silence before the tone.

    Returns:
        The audio in the file.

    """
    audio = build_audio(seconds, silence_seconds=silence_seconds)
    write_wav(audio, path)
    return audio

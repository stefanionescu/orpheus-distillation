"""The silence detector and the WAV reader and writer measure dataset clips."""

from __future__ import annotations

import wave
from typing import TYPE_CHECKING

import numpy as np
import pytest

from config.audio import PCM_SAMPLE_WIDTH_BYTES
from tests.harness.audio import build_tone, build_audio, build_silence, write_wav_file
from tests.harness.voices import FIRST_VOICE
from schemas.dataset.audio import PcmAudio
from src.dataset.audio.wav import read_wav, write_wav, get_duration_seconds
from src.dataset.audio.silence import detect_leading_silence_ms
from tests.suites.unit.builders import CLIP_SECONDS, TONE_SECONDS, CLICK_SECONDS, SILENCE_SECONDS, SILENCE_TOLERANCE_MS

if TYPE_CHECKING:
    from pathlib import Path

LONG_SPEECH_SECONDS = 1.0
"""Speech long enough that the pad before it is under a fifth of the clip."""

OTHER_SAMPLE_RATE = 16_000
"""A rate other than the dataset rate, so code that assumes the dataset rate fails."""


def test_empty_audio_measures_zero() -> None:
    """Audio without samples has no leading silence."""
    assert detect_leading_silence_ms(b"") == 0.0


def test_silent_clip_measures_length() -> None:
    """A clip that never reaches the threshold is silent from start to end."""
    pcm = build_silence(TONE_SECONDS).tobytes()

    assert detect_leading_silence_ms(pcm) == TONE_SECONDS * 1000


def test_silence_before_tone_measured() -> None:
    """The detector finds the start of a tone that follows silence."""
    audio = build_audio(TONE_SECONDS, silence_seconds=SILENCE_SECONDS)

    measured = detect_leading_silence_ms(audio.frames, audio.sample_rate)

    assert abs(measured - SILENCE_SECONDS * 1000) <= SILENCE_TOLERANCE_MS


def test_pad_before_speech_measured() -> None:
    """The pad that a voice asks the server for measures right, even when the speech after it fills the clip."""
    audio = build_audio(LONG_SPEECH_SECONDS, silence_seconds=FIRST_VOICE.prespeech_pad_ms / 1000)

    measured = detect_leading_silence_ms(audio.frames, audio.sample_rate)

    assert abs(measured - FIRST_VOICE.prespeech_pad_ms) <= SILENCE_TOLERANCE_MS


def test_click_before_speech_ignored() -> None:
    """A click shorter than the sustain time does not end the silence; the tone after it does."""
    samples = np.concatenate(
        [
            build_silence(SILENCE_SECONDS),
            build_tone(CLICK_SECONDS),
            build_silence(SILENCE_SECONDS),
            build_tone(TONE_SECONDS),
        ]
    )

    measured = detect_leading_silence_ms(samples.tobytes())

    assert abs(measured - (2 * SILENCE_SECONDS + CLICK_SECONDS) * 1000) <= SILENCE_TOLERANCE_MS


def test_lone_click_ends_silence() -> None:
    """When nothing stays above the threshold for the sustain time, the first loud sample ends the silence."""
    samples = np.concatenate([build_silence(SILENCE_SECONDS), build_tone(CLICK_SECONDS), build_silence(TONE_SECONDS)])

    measured = detect_leading_silence_ms(samples.tobytes())

    assert abs(measured - SILENCE_SECONDS * 1000) <= SILENCE_TOLERANCE_MS


def test_wav_round_trip(tmp_path: Path) -> None:
    """A WAV written into a missing folder reads back with its frames and its own sample rate.

    Args:
        tmp_path: The test folder.

    """
    path = tmp_path / "audio" / "clip.wav"
    audio = PcmAudio(frames=build_audio(TONE_SECONDS).frames, sample_rate=OTHER_SAMPLE_RATE)

    write_wav(audio, path)

    assert read_wav(path) == audio


def test_failed_write_keeps_file(tmp_path: Path) -> None:
    """A write that fails leaves the earlier WAV whole and no temporary file.

    Args:
        tmp_path: The test folder.

    """
    path = tmp_path / "clip.wav"
    earlier = write_wav_file(path, TONE_SECONDS)

    with pytest.raises(wave.Error):
        write_wav(PcmAudio(frames=earlier.frames, sample_rate=0), path)

    assert read_wav(path) == earlier
    assert [item.name for item in tmp_path.iterdir()] == [path.name]


def test_truncated_wav_rejected(tmp_path: Path) -> None:
    """A WAV file shorter than its header announces fails to read.

    Args:
        tmp_path: The test folder.

    """
    path = tmp_path / "clip.wav"
    write_wav_file(path, TONE_SECONDS)
    path.write_bytes(path.read_bytes()[: path.stat().st_size // 2])

    with pytest.raises(wave.Error):
        read_wav(path)


def test_duration_counts_frames() -> None:
    """The duration is the sample count divided by the audio's own sample rate."""
    audio = PcmAudio(
        frames=bytes(OTHER_SAMPLE_RATE * PCM_SAMPLE_WIDTH_BYTES * CLIP_SECONDS), sample_rate=OTHER_SAMPLE_RATE
    )

    assert get_duration_seconds(audio) == CLIP_SECONDS

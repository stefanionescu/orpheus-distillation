"""Leading silence detector that measures how long a clip waits before speech starts."""

from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np

from config.audio import SAMPLE_RATE
from config.dataset.silence import (
    SUSTAIN_MS,
    RMS_WINDOW_MS,
    THRESHOLD_DBFS,
    INT16_FULL_SCALE,
    NOISE_PERCENTILE,
    NOISE_WINDOW_SECONDS,
    THRESHOLD_MULTIPLIER,
)

if TYPE_CHECKING:
    from numpy.typing import NDArray


def _count_window_samples(milliseconds: float, sample_rate: int) -> int:
    return max(1, round(milliseconds / 1000 * sample_rate))


def _build_rms_envelope(signal: NDArray[np.float32], window: int) -> NDArray[np.float32]:
    squares = np.square(signal, dtype=np.float32)
    if squares.size < window:
        return np.full_like(squares, np.sqrt(np.mean(squares, dtype=np.float32)))
    kernel = np.ones(window, dtype=np.float32) / window
    return np.sqrt(np.convolve(squares, kernel, mode="same")).astype(np.float32)


def _find_sustained_onset_index(above: NDArray[np.bool_], sustain: int) -> int | None:
    if above.size < sustain:
        return None
    runs = np.convolve(above.astype(np.int32), np.ones(sustain, dtype=np.int32), mode="valid")
    sustained = np.flatnonzero(runs >= sustain)
    return int(sustained[0]) if sustained.size > 0 else None


def detect_leading_silence_ms(pcm: bytes, sample_rate: int = SAMPLE_RATE) -> float:
    """Estimate the silence before the first sound in mono 16-bit PCM audio.

    The threshold is the larger of `THRESHOLD_DBFS` and a multiple of the noise floor. Speech starts where the RMS
    envelope stays above it for `SUSTAIN_MS`, so a single click does not count. Without such a stretch, the first loud
    sample counts.

    Args:
        pcm: Little-endian PCM samples.
        sample_rate: Samples per second.

    Returns:
        Silence in milliseconds: 0.0 for empty audio, the clip length when nothing is loud enough.

    """
    samples = np.frombuffer(pcm, dtype=np.int16)
    if samples.size == 0:
        return 0.0
    rms = _build_rms_envelope(
        samples.astype(np.float32) / INT16_FULL_SCALE,
        _count_window_samples(RMS_WINDOW_MS, sample_rate),
    )
    # The quiet end of the opening is the noise floor, so a pad shorter than half the opening still counts. An early
    # burst can fill the opening, so the percentile of the whole clip caps the noise floor.
    opening = rms[: max(1, int(NOISE_WINDOW_SECONDS * sample_rate))]
    noise_floor = min(float(np.percentile(opening, NOISE_PERCENTILE)), float(np.percentile(rms, NOISE_PERCENTILE)))
    threshold = max(10 ** (THRESHOLD_DBFS / 20), noise_floor * THRESHOLD_MULTIPLIER)
    above = rms >= threshold
    if not np.any(above):
        return samples.size * 1000 / sample_rate
    onset = _find_sustained_onset_index(above, _count_window_samples(SUSTAIN_MS, sample_rate))
    if onset is None:
        onset = int(np.argmax(above))
    return onset * 1000 / sample_rate

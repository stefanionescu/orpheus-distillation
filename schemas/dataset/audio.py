"""Raw PCM audio."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PcmAudio:
    """Mono 16-bit PCM audio as the Orpheus server streams it.

    Attributes:
        frames: Little-endian PCM samples.
        sample_rate: Samples per second.

    """

    frames: bytes
    sample_rate: int

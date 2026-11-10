"""Record of one clip."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Record:
    """JSON record of one clip in a shard. Each field name is a stored key.

    Attributes:
        text: Prompt that the server read aloud.
        speaker: Orpheus speaker.
        voice: Voice, a key of the voice table.
        duration: Length in seconds.
        leading_silence_ms: Estimated silence before the speech.

    """

    text: str
    speaker: str
    voice: str
    duration: float
    leading_silence_ms: float

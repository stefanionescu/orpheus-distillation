"""Lookups over the voice table in config/voices.py."""

from __future__ import annotations

from typing import TYPE_CHECKING

from config.voices import VOICES

if TYPE_CHECKING:
    from schemas.voice import Voice


def get_voice_for_speaker(speaker: str) -> Voice | None:
    """Find the voice of an Orpheus speaker.

    Args:
        speaker: Speaker name, such as the `speaker` key of a record.

    Returns:
        The voice, or None when no voice has that speaker.

    """
    for voice in VOICES.values():
        if voice.speaker == speaker:
            return voice
    return None

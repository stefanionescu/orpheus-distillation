"""The training command finds the voice of the Orpheus speaker in a shard record."""

from __future__ import annotations

from src.train.voices import get_voice_for_speaker
from tests.harness.voices import TABLE_VOICES


def test_speaker_maps_to_voice() -> None:
    """Each voice table speaker maps back to its voice."""
    assert [get_voice_for_speaker(voice.speaker) for voice in TABLE_VOICES] == list(TABLE_VOICES)

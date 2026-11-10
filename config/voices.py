"""Voice table that both commands share."""

from __future__ import annotations

from schemas.voice import Voice

VOICES: dict[str, Voice] = {
    "female": Voice(
        name="female",
        speaker="tara",
        display_name="Tara",
        temperature=0.55,
        top_p=1.0,
        repetition_penalty=1.7,
        trim_silence=True,
        prespeech_pad_ms=120.0,
    ),
    "male": Voice(
        name="male",
        speaker="zac",
        display_name="Zac",
        temperature=0.55,
        top_p=1.0,
        repetition_penalty=1.8,
        trim_silence=True,
        prespeech_pad_ms=120.0,
    ),
}

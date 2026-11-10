"""One entry of the voice table."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Voice:
    """A voice and its Orpheus sampling settings.

    Attributes:
        name: Voice, the voice table key and the `--voice` value.
        speaker: Orpheus speaker. Clip file names and the record `speaker` key store it.
        display_name: Speaker name on the dataset and model cards.
        temperature: Sampling temperature.
        top_p: Nucleus sampling threshold.
        repetition_penalty: Penalty on repeated tokens.
        trim_silence: Whether the server trims silence around the speech.
        prespeech_pad_ms: Silence that the server keeps before the speech.

    """

    name: str
    speaker: str
    display_name: str
    temperature: float
    top_p: float
    repetition_penalty: float
    trim_silence: bool
    prespeech_pad_ms: float

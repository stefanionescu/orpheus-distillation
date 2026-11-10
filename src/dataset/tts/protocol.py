"""Messages of the Orpheus WebSocket protocol."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Literal, cast
from dataclasses import dataclass

from config.dataset.websocket import (
    MESSAGE_TYPE_KEY,
    REQUEST_TEXT_KEY,
    MESSAGE_ERROR_KEY,
    REQUEST_VOICE_KEY,
    MESSAGE_ERROR_KEYS,
    MESSAGE_ERROR_TYPE,
    SETTINGS_TOP_P_KEY,
    SETTINGS_VOICE_KEY,
    TEXT_ERROR_MARKERS,
    MESSAGE_AUDIO_END_TYPE,
    SETTINGS_TEMPERATURE_KEY,
    SETTINGS_TRIM_SILENCE_KEY,
    SETTINGS_PRESPEECH_PAD_KEY,
    SETTINGS_REPETITION_PENALTY_KEY,
)

if TYPE_CHECKING:
    from collections.abc import Mapping

    from schemas.voice import Voice


@dataclass(frozen=True)
class ServerMessage:
    """A text message from the server, read as an error, the end of the audio, or other.

    Attributes:
        kind: Meaning of the message.
        detail: Error text for an error, else the message text.

    """

    kind: Literal["error", "end", "other"]
    detail: str


def _decode_payload(payload: Mapping[str, object], text: str) -> ServerMessage:
    """Read a JSON object from the server.

    Only an error type or an `error` field marks an error, because informational objects also carry `message` or
    `detail`.

    Args:
        payload: Decoded JSON object.
        text: Raw text frame.

    Returns:
        Kind and detail of the message.

    """
    message_type = str(payload.get(MESSAGE_TYPE_KEY, "")).lower()
    if message_type == MESSAGE_ERROR_TYPE:
        error_detail = next((payload[key] for key in MESSAGE_ERROR_KEYS if key in payload), text)
        return ServerMessage(kind="error", detail=str(error_detail))
    if MESSAGE_ERROR_KEY in payload:
        return ServerMessage(kind="error", detail=str(payload[MESSAGE_ERROR_KEY]))
    if message_type == MESSAGE_AUDIO_END_TYPE:
        return ServerMessage(kind="end", detail=text)
    return ServerMessage(kind="other", detail=text)


def build_request_settings(voice: Voice) -> dict[str, object]:
    """Build the first message of a request: the voice and its sampling settings.

    The server addresses each voice by its name, so the message carries `voice.name`, not the speaker.

    Args:
        voice: Voice that reads the prompt.

    Returns:
        The settings message before JSON encoding.

    """
    return {
        SETTINGS_VOICE_KEY: voice.name,
        SETTINGS_TRIM_SILENCE_KEY: voice.trim_silence,
        SETTINGS_TEMPERATURE_KEY: voice.temperature,
        SETTINGS_TOP_P_KEY: voice.top_p,
        SETTINGS_REPETITION_PENALTY_KEY: voice.repetition_penalty,
        SETTINGS_PRESPEECH_PAD_KEY: voice.prespeech_pad_ms,
    }


def build_text_request(text: str, voice: Voice) -> dict[str, str]:
    """Build the message that carries the prompt to read aloud.

    Args:
        text: Prompt to strip and send.
        voice: Voice that reads the prompt.

    Returns:
        The text message before JSON encoding.

    """
    return {REQUEST_TEXT_KEY: text.strip(), REQUEST_VOICE_KEY: voice.name}


def parse_server_message(text: str) -> ServerMessage:
    """Read one text message from the server.

    Text that is not JSON counts as an error when it mentions an error or a failure.

    Args:
        text: Raw text frame.

    Returns:
        Kind and detail of the message.

    """
    try:
        payload: object = json.loads(text)
    except json.JSONDecodeError:
        is_error = any(marker in text.lower() for marker in TEXT_ERROR_MARKERS)
        return ServerMessage(kind="error" if is_error else "other", detail=text)
    if not isinstance(payload, dict):
        return ServerMessage(kind="other", detail=text)
    return _decode_payload(cast("dict[str, object]", payload), text)

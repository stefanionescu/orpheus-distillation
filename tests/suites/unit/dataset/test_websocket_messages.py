"""The client reads Orpheus server messages and sends its own in protocol order."""

from __future__ import annotations

import json
import asyncio

import pytest

from tests.harness.tts import AUDIO_END, FakeConnection, build_close, cast_connection, build_error_message
from src.dataset.errors import TtsError
from tests.harness.voices import FIRST_VOICE
from config.dataset.server import NORMAL_CLOSE_CODE, ABNORMAL_CLOSE_CODE
from config.dataset.websocket import END_MESSAGE
from src.dataset.tts.protocol import ServerMessage, parse_server_message
from src.dataset.tts.transport import receive_pcm, request_pcm
from tests.suites.unit.builders import PROMPT, AUDIO_FRAME, GOING_AWAY_CODE


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ('{"type": "error", "message": "bad voice"}', ServerMessage(kind="error", detail="bad voice")),
        ('{"type": "ERROR"}', ServerMessage(kind="error", detail='{"type": "ERROR"}')),
        ('{"error": "bad voice"}', ServerMessage(kind="error", detail="bad voice")),
        ('{"type": "audio_end"}', ServerMessage(kind="end", detail='{"type": "audio_end"}')),
        ('{"message": "model loaded"}', ServerMessage(kind="other", detail='{"message": "model loaded"}')),
        ("generation failed", ServerMessage(kind="error", detail="generation failed")),
        ("ready", ServerMessage(kind="other", detail="ready")),
        ('["error"]', ServerMessage(kind="other", detail='["error"]')),
    ],
    ids=[
        "error-type-detail",
        "error-type-without-detail",
        "error-field",
        "audio-end",
        "informational-message",
        "error-text",
        "plain-text",
        "json-list",
    ],
)
def test_server_message_kinds(text: str, expected: ServerMessage) -> None:
    """Each message form reads as an error with its detail, the audio end, or another message.

    Args:
        text: The server text frame.
        expected: How the client reads it.

    """
    assert parse_server_message(text) == expected


def test_frames_collected_until_end() -> None:
    """Binary frames join in order until the end message, and informational text between them drops out."""
    status = '{"type": "status", "message": "synthesizing"}'
    connection = FakeConnection([AUDIO_FRAME, "ready", status, AUDIO_FRAME, AUDIO_END, AUDIO_FRAME])

    assert asyncio.run(receive_pcm(cast_connection(connection))) == AUDIO_FRAME * 2


def test_normal_close_ends_audio() -> None:
    """A normal close after audio ends the request like an end message."""
    connection = FakeConnection([AUDIO_FRAME, build_close(NORMAL_CLOSE_CODE)])

    assert asyncio.run(receive_pcm(cast_connection(connection))) == AUDIO_FRAME


def test_abnormal_close_is_retryable() -> None:
    """An abnormal close before any audio is retryable."""
    connection = FakeConnection([build_close(None)])

    with pytest.raises(TtsError, match="abnormally") as caught:
        asyncio.run(receive_pcm(cast_connection(connection)))

    assert caught.value.is_retryable


def test_late_close_fails() -> None:
    """An abnormal close after audio arrived fails the request without a retry."""
    connection = FakeConnection([AUDIO_FRAME, build_close(ABNORMAL_CLOSE_CODE)])

    with pytest.raises(TtsError, match=str(ABNORMAL_CLOSE_CODE)) as caught:
        asyncio.run(receive_pcm(cast_connection(connection)))

    assert not caught.value.is_retryable


def test_other_close_fails() -> None:
    """A close with a code other than normal or abnormal fails the request without a retry."""
    connection = FakeConnection([build_close(GOING_AWAY_CODE)])

    with pytest.raises(TtsError, match=str(GOING_AWAY_CODE)) as caught:
        asyncio.run(receive_pcm(cast_connection(connection)))

    assert not caught.value.is_retryable


def test_error_message_fails_request() -> None:
    """A server error message fails the request with its text."""
    connection = FakeConnection([AUDIO_FRAME, build_error_message("voice not loaded")])

    with pytest.raises(TtsError, match="voice not loaded") as caught:
        asyncio.run(receive_pcm(cast_connection(connection)))

    assert not caught.value.is_retryable


def test_request_sends_protocol_order() -> None:
    """A request sends the voice settings, then the stripped prompt, then the end message, and returns the audio."""
    connection = FakeConnection([AUDIO_FRAME, AUDIO_END])

    pcm = asyncio.run(request_pcm(cast_connection(connection), f"  {PROMPT}\n", FIRST_VOICE))

    settings, text, end = connection.sent
    assert pcm == AUDIO_FRAME
    assert json.loads(settings) == {
        "voice": FIRST_VOICE.name,
        "trim_silence": FIRST_VOICE.trim_silence,
        "temperature": FIRST_VOICE.temperature,
        "top_p": FIRST_VOICE.top_p,
        "repetition_penalty": FIRST_VOICE.repetition_penalty,
        "prespeech_pad_ms": FIRST_VOICE.prespeech_pad_ms,
    }
    assert json.loads(text) == {"text": PROMPT, "voice": FIRST_VOICE.name}
    assert end == END_MESSAGE

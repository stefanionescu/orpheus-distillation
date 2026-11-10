"""The Orpheus client over a real WebSocket to the fake server: handshake, frames, and retries."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING
import asyncio

from tests.harness.tts import AUDIO_END, FakeSleep
from tests.state.server import ScriptedReply
from tests.harness.audio import build_audio
from tests.harness.server import (
    FakeTtsServer,
    serve_fake_tts,
    build_audio_reply,
    build_rejection_reply,
)
from tests.harness.voices import FIRST_VOICE
from config.dataset.server import TTS_ROUTE
from src.dataset.audio.wav import read_wav
from src.dataset.tts.client import OrpheusClient
from src.dataset.tts.protocol import build_text_request, build_request_settings
from tests.suites.integration.builders import API_KEY

if TYPE_CHECKING:
    from pathlib import Path

    from schemas.record import Record

PROMPT = "Hello there, this is a test."
CLIP_SECONDS = 1.5
BAD_GATEWAY = 502
REJECTIONS = 2
LARGE_CLIP_SECONDS = 25.0
"""A clip whose PCM in one frame exceeds the 1 MiB message limit that websockets sets by default."""


def _synthesize(fake: FakeTtsServer, sleep: FakeSleep, audio_path: Path) -> Record:
    with serve_fake_tts(fake) as server_url:
        client = OrpheusClient(server_url, API_KEY, sleep=sleep)
        return asyncio.run(client.synthesize_clip(PROMPT, FIRST_VOICE, audio_path))


def test_audio_frames_become_clip(tmp_path: Path) -> None:
    """A reply's binary frames become one WAV file of their PCM, and the record has that PCM's length.

    Args:
        tmp_path: The test folder.

    """
    audio_path = tmp_path / "clip.wav"

    record = _synthesize(FakeTtsServer([build_audio_reply(CLIP_SECONDS)]), FakeSleep(), audio_path)

    assert read_wav(audio_path) == build_audio(CLIP_SECONDS)
    assert record.duration == CLIP_SECONDS


def test_bad_gateway_retried(tmp_path: Path) -> None:
    """Handshakes rejected with HTTP 502 take one connection each, then the next connection brings the clip.

    Args:
        tmp_path: The test folder.

    """
    fake = FakeTtsServer([*[build_rejection_reply(BAD_GATEWAY)] * REJECTIONS, build_audio_reply(CLIP_SECONDS)])

    _synthesize(fake, FakeSleep(), tmp_path / "clip.wav")

    assert len(fake.connections) == REJECTIONS + 1
    assert (tmp_path / "clip.wav").is_file()


def test_request_carries_bearer(tmp_path: Path) -> None:
    """The handshake reaches the speech route with the bearer token, and the request sends the voice, then the text.

    Args:
        tmp_path: The test folder.

    """
    fake = FakeTtsServer([build_audio_reply(CLIP_SECONDS)])

    _synthesize(fake, FakeSleep(), tmp_path / "clip.wav")

    [connection] = fake.connections
    assert (connection.path, connection.authorization) == (TTS_ROUTE, f"Bearer {API_KEY}")
    assert [json.loads(message) for message in connection.messages] == [
        build_request_settings(FIRST_VOICE),
        build_text_request(PROMPT, FIRST_VOICE),
    ]


def test_large_frame_arrives_whole(tmp_path: Path) -> None:
    """A clip that arrives as one frame past the library's default message limit becomes a whole WAV file.

    Args:
        tmp_path: The test folder.

    """
    audio = build_audio(LARGE_CLIP_SECONDS)
    audio_path = tmp_path / "clip.wav"

    _synthesize(FakeTtsServer([ScriptedReply(status=None, frames=(audio.frames, AUDIO_END))]), FakeSleep(), audio_path)

    assert read_wav(audio_path) == audio

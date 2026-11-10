"""The client retries a failed request once per connection attempt, with backoff, and nowhere else."""

from __future__ import annotations

from typing import TYPE_CHECKING
import asyncio

import pytest
from websockets.exceptions import InvalidMessage

from tests.harness.tts import (
    AUDIO_END,
    FakeSleep,
    FakeConnector,
    build_close,
    build_rejection,
    build_error_message,
)
from src.dataset.errors import TtsError
from tests.harness.audio import build_audio
from tests.harness.voices import FIRST_VOICE
from config.dataset.server import CONNECT_ATTEMPTS, BACKOFF_BASE_SECONDS
from src.dataset.audio.wav import read_wav
from src.dataset.tts.client import OrpheusClient
from tests.suites.unit.builders import (
    PROMPT,
    API_KEY,
    SERVER_URL,
    AUDIO_FRAME,
    BAD_GATEWAY,
    TONE_SECONDS,
    UNAUTHORIZED,
    SILENCE_SECONDS,
    SILENCE_TOLERANCE_MS,
)

if TYPE_CHECKING:
    from pathlib import Path

    from schemas.record import Record
    from tests.harness.tts import Outcome

SUCCESS = (AUDIO_FRAME, AUDIO_END)
REJECTIONS = 2


def _synthesize(connector: FakeConnector, sleep: FakeSleep, audio_path: Path) -> Record:
    client = OrpheusClient(SERVER_URL, API_KEY, connect_server=connector, sleep=sleep)
    return asyncio.run(client.synthesize_clip(PROMPT, FIRST_VOICE, audio_path))


def _fail(outcomes: list[Outcome], audio_path: Path) -> tuple[TtsError, FakeConnector, FakeSleep]:
    connector = FakeConnector(outcomes)
    sleep = FakeSleep()
    with pytest.raises(TtsError) as caught:
        _synthesize(connector, sleep, audio_path)
    return caught.value, connector, sleep


def test_retryable_status_retried(tmp_path: Path) -> None:
    """Handshakes rejected with a retryable status take one attempt each, and the next attempt writes the clip.

    Args:
        tmp_path: The test folder.

    """
    audio_path = tmp_path / "clip.wav"
    connector = FakeConnector([*[build_rejection(BAD_GATEWAY)] * REJECTIONS, SUCCESS])

    _synthesize(connector, FakeSleep(), audio_path)

    assert len(connector.connections) == REJECTIONS + 1
    assert audio_path.is_file()


def test_unauthorized_not_retried(tmp_path: Path) -> None:
    """A rejected handshake with a status outside the retryable set fails after one attempt.

    Args:
        tmp_path: The test folder.

    """
    error, connector, sleep = _fail([build_rejection(UNAUTHORIZED)], tmp_path / "clip.wav")

    assert str(UNAUTHORIZED) in str(error)
    assert len(connector.connections) == 1
    assert sleep.delays == []


def test_protocol_error_not_retried(tmp_path: Path) -> None:
    """A protocol error in the handshake is final, even when its text mentions a retryable status.

    Args:
        tmp_path: The test folder.

    """
    failure = InvalidMessage(f"proxy answered {BAD_GATEWAY} Bad Gateway")

    error, connector, _ = _fail([failure, SUCCESS], tmp_path / "clip.wav")

    assert not error.is_retryable
    assert len(connector.connections) == 1


def test_server_error_not_retried(tmp_path: Path) -> None:
    """A server error message fails the request without a second attempt.

    Args:
        tmp_path: The test folder.

    """
    error, connector, _ = _fail([[build_error_message("voice not loaded")], SUCCESS], tmp_path / "clip.wav")

    assert "voice not loaded" in str(error)
    assert len(connector.connections) == 1


def test_abnormal_close_retried(tmp_path: Path) -> None:
    """The client reopens a connection that closes abnormally before audio.

    Args:
        tmp_path: The test folder.

    """
    connector = FakeConnector([[build_close(None)], SUCCESS])
    sleep = FakeSleep()

    record = _synthesize(connector, sleep, tmp_path / "clip.wav")

    assert len(connector.connections) == len(sleep.delays) + 1
    assert record.duration > 0


def test_attempts_stop_at_budget(tmp_path: Path) -> None:
    """The client retries network errors until the attempt budget runs out, and the error names the attempt count.

    Args:
        tmp_path: The test folder.

    """
    outcomes: list[Outcome] = [ConnectionRefusedError("refused") for _ in range(CONNECT_ATTEMPTS)]

    error, connector, sleep = _fail(outcomes, tmp_path / "clip.wav")

    assert f"after {CONNECT_ATTEMPTS} attempts" in str(error)
    assert len(connector.connections) == CONNECT_ATTEMPTS
    assert sleep.delays == [BACKOFF_BASE_SECONDS**attempt for attempt in range(CONNECT_ATTEMPTS - 1)]


def test_empty_audio_rejected(tmp_path: Path) -> None:
    """A request that ends without audio fails and writes no file.

    Args:
        tmp_path: The test folder.

    """
    audio_path = tmp_path / "clip.wav"

    error, _, _ = _fail([[AUDIO_END]], audio_path)

    assert "no audio" in str(error)
    assert not audio_path.exists()


def test_success_writes_clip(tmp_path: Path) -> None:
    """A successful request writes its audio as the WAV and measures the record from it under the stored names.

    Args:
        tmp_path: The test folder.

    """
    audio_path = tmp_path / "clip.wav"
    audio = build_audio(TONE_SECONDS, silence_seconds=SILENCE_SECONDS)

    record = _synthesize(FakeConnector([[audio.frames, AUDIO_END]]), FakeSleep(), audio_path)

    assert read_wav(audio_path) == audio
    assert (record.text, record.speaker, record.voice) == (PROMPT, FIRST_VOICE.speaker, FIRST_VOICE.name)
    assert record.duration == TONE_SECONDS + SILENCE_SECONDS
    assert abs(record.leading_silence_ms - SILENCE_SECONDS * 1000) <= SILENCE_TOLERANCE_MS

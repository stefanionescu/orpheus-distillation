"""Fakes of the Orpheus side: scripted WebSocket connections, their connector, and the clock."""

from __future__ import annotations

import json
import signal
from typing import TYPE_CHECKING, cast, override
import asyncio
from pathlib import Path
from contextlib import asynccontextmanager
from dataclasses import field, dataclass

from websockets.frames import Close
from websockets.http11 import Response
from websockets.exceptions import InvalidStatus, ConnectionClosedOK, ConnectionClosedError
from websockets.datastructures import Headers

from src.dataset.errors import TtsError
from tests.state.server import ConnectCall
from tests.harness.audio import write_wav_file
from config.dataset.server import NORMAL_CLOSE_CODE
from tests.harness.records import build_record
from config.dataset.websocket import MESSAGE_TYPE_KEY, MESSAGE_ERROR_TYPE, MESSAGE_AUDIO_END_TYPE

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence, AsyncGenerator

    from websockets.exceptions import ConnectionClosed
    from websockets.asyncio.client import ClientConnection

    from schemas.voice import Voice
    from schemas.record import Record

type Frame = str | bytes | ConnectionClosed
"""A frame that a fake connection returns, or a close that it raises."""

type Outcome = Sequence[Frame] | Exception
"""The frames of one attempt, or the error it raises before the connection opens."""

AUDIO_END = json.dumps({MESSAGE_TYPE_KEY: MESSAGE_AUDIO_END_TYPE})


def build_error_message(detail: str) -> str:
    """Build the JSON error message that the server sends on failure.

    Args:
        detail: The error text.

    Returns:
        The text frame.

    """
    return json.dumps({MESSAGE_TYPE_KEY: MESSAGE_ERROR_TYPE, "message": detail})


def build_rejection(status_code: int) -> InvalidStatus:
    """Build the error that `websockets` raises when the server rejects the handshake.

    Args:
        status_code: The HTTP status.

    Returns:
        The handshake error.

    """
    return InvalidStatus(Response(status_code, "", Headers()))


def build_close(code: int | None) -> ConnectionClosed:
    """Build the error that `websockets` raises when the connection closes.

    Args:
        code: The close code, or None when no close frame arrived.

    Returns:
        The close error; the normal code gives a clean close.

    """
    if code == NORMAL_CLOSE_CODE:
        return ConnectionClosedOK(Close(code, ""), None)
    return ConnectionClosedError(None if code is None else Close(code, ""), None)


@dataclass
class FakeConnection:
    """A WebSocket connection that plays scripted frames and keeps the client messages.

    Attributes:
        frames: Frames to return or closes to raise; the connection closes after the last.
        sent: The client text messages, in order.

    """

    frames: list[Frame]
    sent: list[str] = field(default_factory=list[str])

    async def send(self, message: str) -> None:
        """Keep a client message.

        Args:
            message: The text message.

        """
        self.sent.append(message)

    async def recv(self) -> str | bytes:
        """Return the next scripted frame.

        Returns:
            The frame text or bytes.

        Raises:
            frame: The scripted close, or a normal close after the last frame.

        """
        frame = self.frames.pop(0) if self.frames else build_close(NORMAL_CLOSE_CODE)
        if isinstance(frame, str | bytes):
            return frame
        raise frame


def cast_connection(connection: object) -> ClientConnection:
    """Type a fake as a `websockets` connection; the fake has only the methods the code calls.

    Args:
        connection: The fake connection.

    Returns:
        The same object.

    """
    return cast("ClientConnection", connection)


@dataclass
class FakeConnector:
    """A connector that plays one outcome per attempt and records each attempt.

    Attributes:
        outcomes: The outcomes still to come: frames or a handshake error.
        connections: One record per attempt, in order.

    """

    outcomes: list[Outcome]
    connections: list[ConnectCall] = field(default_factory=list[ConnectCall])

    @asynccontextmanager
    async def __call__(
        self,
        uri: str,
        *,
        max_size: int | None,
        additional_headers: Mapping[str, str],
    ) -> AsyncGenerator[ClientConnection]:
        """Open the next scripted connection and record it when it closes.

        Args:
            uri: The URL.
            max_size: The largest message the client accepts.
            additional_headers: The handshake headers.

        Yields:
            The scripted connection.

        Raises:
            outcome: This attempt's handshake error.

        """
        outcome = self.outcomes.pop(0)
        connection = FakeConnection([] if isinstance(outcome, Exception) else list(outcome))
        try:
            if isinstance(outcome, Exception):
                raise outcome
            yield cast_connection(connection)
        finally:
            record = ConnectCall(uri, dict(additional_headers), max_size, tuple(connection.sent))
            self.connections.append(record)


@dataclass
class FakeSleep:
    """A sleep that returns at once and records each delay, so retry tests do not wait.

    Attributes:
        delays: The requested delays in seconds, in order.

    """

    delays: list[float] = field(default_factory=list[float])

    async def __call__(self, seconds: float) -> None:
        """Record one delay.

        Args:
            seconds: The requested delay.

        """
        self.delays.append(seconds)


@dataclass
class FakeTtsClient:
    """An Orpheus client that writes a real WAV per request and fails the chosen clips.

    Attributes:
        failing_paths: The WAV files whose request raises `TtsError`.
        calls: The WAV file of each request, in order.
        servers: The server URL and API key of each command that built this client.

    """

    failing_paths: frozenset[Path] = frozenset()
    calls: list[Path] = field(default_factory=list[Path])
    servers: list[tuple[str, str]] = field(default_factory=list[tuple[str, str]])

    async def synthesize_clip(self, text: str, voice: Voice, audio_path: Path) -> Record:
        """Yield to the event loop like a real request, then write the clip or fail.

        Args:
            text: The prompt to read aloud.
            voice: The voice that reads it.
            audio_path: The WAV file to write.

        Returns:
            The clip record.

        Raises:
            TtsError: The clip is in `failing_paths`.

        """
        self.calls.append(audio_path)
        await asyncio.sleep(0)
        if audio_path in self.failing_paths:
            message = f"The server failed: {text}"
            raise TtsError(message)
        record = build_record(voice, text=text)
        write_wav_file(audio_path, record.duration)
        return record


@dataclass
class CountingTtsClient(FakeTtsClient):
    """A fake client that counts the requests in flight, to show how many a caller runs at once.

    Attributes:
        in_flight: The requests started and not yet finished.
        peak_in_flight: The most requests in flight at one time.

    """

    in_flight: int = 0
    peak_in_flight: int = 0

    @override
    async def synthesize_clip(self, text: str, voice: Voice, audio_path: Path) -> Record:
        """Count the request as in flight until its clip is written.

        Args:
            text: Prompt of the request.
            voice: Voice of the request.
            audio_path: Clip file of the request.

        Returns:
            The record of the written clip.

        """
        self.in_flight += 1
        self.peak_in_flight = max(self.peak_in_flight, self.in_flight)
        try:
            return await super().synthesize_clip(text, voice, audio_path)
        finally:
            self.in_flight -= 1


@dataclass
class SignalingTtsClient(FakeTtsClient):
    """A fake client that signals its own process after some requests, as `scripts/stop.sh dataset` does.

    Attributes:
        signal_number: The signal.
        signal_after: Requests before the signal.

    """

    signal_number: int = signal.SIGTERM
    signal_after: int = 2

    @override
    async def synthesize_clip(self, text: str, voice: Voice, audio_path: Path) -> Record:
        """Write the clip, then send the signal after the chosen request.

        Args:
            text: The prompt.
            voice: The voice.
            audio_path: The WAV file.

        Returns:
            The clip record.

        """
        record = await super().synthesize_clip(text, voice, audio_path)
        if len(self.calls) == self.signal_after:
            signal.raise_signal(self.signal_number)
        return record

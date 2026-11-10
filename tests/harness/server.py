"""A fake Orpheus WebSocket server on loopback that plays scripted replies and records requests."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING
import threading
from contextlib import contextmanager
from dataclasses import field, dataclass

from websockets.exceptions import ConnectionClosed
from websockets.sync.server import serve

from tests.harness.tts import AUDIO_END, build_error_message
from tests.state.server import ScriptedReply, ServedConnection
from tests.harness.audio import build_audio
from config.dataset.websocket import END_MESSAGE, REQUEST_TEXT_KEY, REQUEST_VOICE_KEY

if TYPE_CHECKING:
    from collections.abc import Sequence, Generator

    from websockets.http11 import Request, Response
    from websockets.sync.server import ServerConnection

LOOPBACK_HOST = "127.0.0.1"
FRAME_BYTES = 4096
"""The binary frame size, so one clip arrives in several frames."""

UNSCRIPTED_STATUS = 500
"""The status for a connection with no scripted reply, so an unplanned request fails its test."""


def build_audio_reply(seconds: float) -> ScriptedReply:
    """Build a success reply: tone PCM in several binary frames, then the end message.

    Args:
        seconds: The tone length.

    Returns:
        The reply.

    """
    pcm = build_audio(seconds).frames
    chunks = tuple(pcm[start : start + FRAME_BYTES] for start in range(0, len(pcm), FRAME_BYTES))
    return ScriptedReply(status=None, frames=(*chunks, AUDIO_END))


def build_error_reply(detail: str) -> ScriptedReply:
    """Build a failure reply: one JSON error message on an accepted connection.

    Args:
        detail: The error text.

    Returns:
        The reply.

    """
    return ScriptedReply(status=None, frames=(build_error_message(detail),))


def build_rejection_reply(status: int) -> ScriptedReply:
    """Build a reply that rejects the handshake with an HTTP status, as a proxy or the auth check does.

    Args:
        status: The HTTP status.

    Returns:
        The reply.

    """
    return ScriptedReply(status=status, frames=())


def list_requested_clips(connections: Sequence[ServedConnection]) -> list[tuple[str, str]]:
    """List the prompt and voice of each request.

    Args:
        connections: The connections the server answered.

    Returns:
        The prompt and voice of each request that sent its text message, in order.

    """
    payloads = [json.loads(message) for connection in connections for message in connection.messages]
    return [
        (payload[REQUEST_TEXT_KEY], payload[REQUEST_VOICE_KEY]) for payload in payloads if REQUEST_TEXT_KEY in payload
    ]


@dataclass
class FakeTtsServer:
    """Fake server that answers each connection with the next scripted reply, then the default reply.

    The websockets server runs each connection on its own thread, so a lock guards the script.

    Attributes:
        replies: The replies still to play, in connection order.
        default_reply: The reply after the script runs out, or None to reject.
        connections: Every connection in arrival order, recorded before the client sees its reply.

    """

    replies: list[ScriptedReply] = field(default_factory=list[ScriptedReply])
    default_reply: ScriptedReply | None = None
    connections: list[ServedConnection] = field(default_factory=list[ServedConnection])
    _accepted: dict[int, ScriptedReply] = field(default_factory=dict[int, ScriptedReply])
    _lock: threading.Lock = field(default_factory=threading.Lock)

    def answer_handshake(self, connection: ServerConnection, request: Request) -> Response | None:
        """Take the next reply, and reject the handshake when the reply carries a status.

        Args:
            connection: The connection.
            request: The opening request.

        Returns:
            The rejection, or None to accept the connection.

        """
        with self._lock:
            reply = self.replies.pop(0) if self.replies else self.default_reply
        if reply is None:
            reply = build_rejection_reply(UNSCRIPTED_STATUS)
        if reply.status is not None:
            self.connections.append(ServedConnection(request.path, request.headers.get("Authorization"), ()))
            return connection.respond(reply.status, "Rejected by the fake server\n")
        with self._lock:
            self._accepted[id(connection)] = reply
        return None

    def answer_request(self, connection: ServerConnection) -> None:
        """Record the messages of one request up to its end message, then send the reply frames.

        Args:
            connection: The accepted connection.

        """
        with self._lock:
            reply = self._accepted.pop(id(connection))
        messages: list[str] = []
        try:
            while (message := connection.recv()) != END_MESSAGE:
                messages.append(str(message))
        except ConnectionClosed:
            # A cancelled run leaves before its end message, so the reply has no reader.
            reply = ScriptedReply(status=None, frames=())
        request = connection.request
        authorization = None if request is None else request.headers.get("Authorization")
        self.connections.append(
            ServedConnection("" if request is None else request.path, authorization, tuple(messages))
        )
        for frame in reply.frames:
            connection.send(frame)


@contextmanager
def serve_fake_tts(fake: FakeTtsServer) -> Generator[str]:
    """Run the fake server on a free loopback port for the block, then wait for its connections to end.

    Args:
        fake: Answers the connections.

    Yields:
        The address, as `ws://127.0.0.1:<port>`.

    """
    server = serve(fake.answer_request, LOOPBACK_HOST, 0, process_request=fake.answer_handshake)
    thread = threading.Thread(target=server.serve_forever)
    thread.start()
    try:
        host, port = server.socket.getsockname()[:2]
        yield f"ws://{host}:{port}"
    finally:
        server.shutdown()
        thread.join()

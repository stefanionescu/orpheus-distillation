"""One Orpheus request over a WebSocket connection."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, TypedDict
from urllib.parse import urlsplit, urlunsplit

from websockets.exceptions import ConnectionClosed

from src.dataset.errors import TtsError
from config.dataset.server import TTS_ROUTE, HTTP_TO_WS_SCHEME, NORMAL_CLOSE_CODE, ABNORMAL_CLOSE_CODE
from config.dataset.websocket import END_MESSAGE
from src.dataset.tts.protocol import build_text_request, parse_server_message, build_request_settings

if TYPE_CHECKING:
    from collections.abc import Mapping

    from websockets.asyncio.client import ClientConnection

    from schemas.voice import Voice


class ConnectOptions(TypedDict):
    """Keyword arguments of `websockets.connect` that every request passes.

    Attributes:
        max_size: Message size limit in bytes, or None for no limit.
        additional_headers: Handshake headers.

    """

    max_size: int | None
    additional_headers: Mapping[str, str]


async def _receive_frame(connection: ClientConnection, *, has_audio: bool) -> str | bytes | None:
    """Wait for the next frame. A normal close ends the audio like an end message.

    Args:
        connection: Open connection.
        has_audio: Whether audio arrived already, which makes an abnormal close final.

    Returns:
        The frame, or None after a normal close.

    Raises:
        TtsError: The connection closed with another code. Retryable for an abnormal close before any audio.

    """
    try:
        return await connection.recv()
    except ConnectionClosed as closed:
        code = ABNORMAL_CLOSE_CODE if closed.rcvd is None else closed.rcvd.code
        if code == NORMAL_CLOSE_CODE:
            return None
        if code == ABNORMAL_CLOSE_CODE and not has_audio:
            message = "The connection closed abnormally before any audio arrived"
            raise TtsError(message, is_retryable=True) from closed
        message = f"The connection closed with code {code}"
        raise TtsError(message) from closed


def build_tts_url(server: str) -> str:
    """Build the WebSocket URL of the speech route from a server address.

    The function maps `http` to `ws` and `https` to `wss`, treats a bare `host:port` as `ws`, and appends the route
    once.

    Args:
        server: Address such as `https://host`, `wss://host/base`, or `host:8000`.

    Returns:
        URL to connect to.

    Raises:
        ValueError: The address is empty.

    """
    address = server.strip()
    if not address:
        message = "The server address is empty"
        raise ValueError(message)
    parts = urlsplit(address if "://" in address else f"ws://{address}")
    path = parts.path.rstrip("/").removesuffix(TTS_ROUTE) + TTS_ROUTE
    return urlunsplit((HTTP_TO_WS_SCHEME.get(parts.scheme, parts.scheme), parts.netloc, path, parts.query, ""))


async def receive_pcm(connection: ClientConnection) -> bytes:
    """Collect binary frames until the server ends the audio or closes the connection.

    Args:
        connection: Connection that carried the request.

    Returns:
        PCM bytes of every binary frame, in order.

    Raises:
        TtsError: The server sent an error, or the connection closed abnormally.

    """
    frames = bytearray()
    while (frame := await _receive_frame(connection, has_audio=bool(frames))) is not None:
        if isinstance(frame, bytes):
            frames.extend(frame)
            continue
        message = parse_server_message(frame)
        if message.kind == "error":
            raise TtsError(message.detail)
        if message.kind == "end":
            break
    return bytes(frames)


async def request_pcm(connection: ClientConnection, text: str, voice: Voice) -> bytes:
    """Send one prompt and collect its audio.

    Args:
        connection: Open connection to the speech route.
        text: Prompt to read aloud.
        voice: Voice that reads the prompt.

    Returns:
        PCM bytes of the clip.

    """
    await connection.send(json.dumps(build_request_settings(voice)))
    await connection.send(json.dumps(build_text_request(text, voice)))
    await connection.send(END_MESSAGE)
    return await receive_pcm(connection)

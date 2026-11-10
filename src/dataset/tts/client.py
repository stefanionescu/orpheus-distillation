"""Orpheus client with a retry policy around each request."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol
import asyncio
import logging

from websockets import connect
from websockets.exceptions import InvalidStatus, WebSocketException

from config.audio import SAMPLE_RATE
from schemas.record import Record
from src.dataset.errors import TtsError
from config.dataset.server import CONNECT_ATTEMPTS, BACKOFF_BASE_SECONDS, RETRYABLE_STATUS_CODES
from schemas.dataset.audio import PcmAudio
from src.dataset.audio.wav import write_wav, get_duration_seconds
from src.dataset.audio.silence import detect_leading_silence_ms
from src.dataset.tts.transport import ConnectOptions, request_pcm, build_tts_url

if TYPE_CHECKING:
    from pathlib import Path
    from contextlib import AbstractAsyncContextManager
    from collections.abc import Callable, Awaitable

    from websockets.asyncio.client import ClientConnection

    from schemas.voice import Voice

logger = logging.getLogger(__name__)


class TtsClient(Protocol):
    """Interface of the Orpheus client that the pipeline needs."""

    async def synthesize_clip(self, text: str, voice: Voice, audio_path: Path) -> Record:
        """Read one prompt aloud, write the clip, and return its record.

        Args:
            text: Prompt to read aloud.
            voice: Voice that reads the prompt.
            audio_path: WAV file to write.

        Returns:
            Clip record.

        """
        ...


class OrpheusClient:
    """Client of one Orpheus server that opens one WebSocket connection per request."""

    def __init__(
        self,
        url: str,
        api_key: str,
        *,
        connect_server: Callable[..., AbstractAsyncContextManager[ClientConnection]] = connect,
        sleep: Callable[[float], Awaitable[None]] = asyncio.sleep,
    ) -> None:
        """Store the route and token, and the connect and sleep functions that tests replace.

        Args:
            url: Server address in any form that `build_tts_url` accepts.
            api_key: Bearer token.
            connect_server: Opens a WebSocket connection.
            sleep: Waits between attempts.

        """
        self._url = build_tts_url(url)
        self._options: ConnectOptions = {"max_size": None, "additional_headers": {"Authorization": f"Bearer {api_key}"}}
        self._connect_server = connect_server
        self._sleep = sleep

    async def _send_request(self, text: str, voice: Voice) -> bytes:
        """Send the request on a new connection, turning connection failures into `TtsError`.

        Args:
            text: Prompt to read aloud.
            voice: Voice that reads the prompt.

        Returns:
            PCM bytes of the clip.

        Raises:
            TtsError: The handshake, connection, or server failed. Retryable for `RETRYABLE_STATUS_CODES` and network
                errors.

        """
        try:
            async with self._connect_server(self._url, **self._options) as connection:
                return await request_pcm(connection, text, voice)
        except InvalidStatus as rejection:
            status_code = rejection.response.status_code
            message = f"The server rejected the connection with HTTP {status_code}"
            raise TtsError(message, is_retryable=status_code in RETRYABLE_STATUS_CODES) from rejection
        except (OSError, WebSocketException) as error:
            message = f"The connection failed: {error}"
            raise TtsError(message, is_retryable=isinstance(error, OSError)) from error

    async def _request_audio(self, text: str, voice: Voice) -> bytes:
        attempt = 1
        while True:
            try:
                return await self._send_request(text, voice)
            except TtsError as error:
                if not error.is_retryable:
                    raise
                if attempt == CONNECT_ATTEMPTS:
                    message = f"{error} (after {attempt} attempts)"
                    raise TtsError(message) from error
                logger.warning("Attempt %d of %d failed, retrying: %s", attempt, CONNECT_ATTEMPTS, error)
            await self._sleep(BACKOFF_BASE_SECONDS ** (attempt - 1))
            attempt += 1

    async def synthesize_clip(self, text: str, voice: Voice, audio_path: Path) -> Record:
        """Read one prompt aloud, write the clip, and return its record.

        The client retries a retryable status, a network error, or an abnormal close before any audio, up to
        `CONNECT_ATTEMPTS` attempts with exponential backoff. It never retries an error message from the server.

        Args:
            text: Prompt to read aloud.
            voice: Voice that reads the prompt.
            audio_path: WAV file to write.

        Returns:
            Clip record, measured from the received audio.

        Raises:
            TtsError: The server failed the request, every attempt failed, or no audio arrived.

        """
        frames = await self._request_audio(text, voice)
        if not frames:
            message = "The server sent no audio"
            raise TtsError(message)
        audio = PcmAudio(frames=frames, sample_rate=SAMPLE_RATE)
        write_wav(audio, audio_path)
        return Record(
            text=text,
            speaker=voice.speaker,
            voice=voice.name,
            duration=get_duration_seconds(audio),
            leading_silence_ms=detect_leading_silence_ms(frames),
        )

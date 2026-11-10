"""Frozen records of the fake Orpheus side: what it saw and what it plays."""

from __future__ import annotations

from typing import TYPE_CHECKING
from dataclasses import dataclass

if TYPE_CHECKING:
    from collections.abc import Mapping


@dataclass(frozen=True)
class ConnectCall:
    """One connection attempt and the text messages the client sent.

    Attributes:
        url: The URL the client opened.
        headers: The handshake headers.
        max_size: The largest message the client accepts, or None for no limit.
        messages: The text messages in order; empty when the handshake failed.

    """

    url: str
    headers: Mapping[str, str]
    max_size: int | None
    messages: tuple[str, ...]


@dataclass(frozen=True)
class ScriptedReply:
    """The fake server's answer to one connection.

    Attributes:
        status: The HTTP status that rejects the handshake, or None to accept it.
        frames: The frames sent after the request's end message; then the server closes normally.

    """

    status: int | None
    frames: tuple[str | bytes, ...]


@dataclass(frozen=True)
class ServedConnection:
    """One connection as the fake server saw it.

    Attributes:
        path: The request path.
        authorization: The Authorization header, or None.
        messages: The text messages before the end message; empty for a rejected handshake.

    """

    path: str
    authorization: str | None
    messages: tuple[str, ...]

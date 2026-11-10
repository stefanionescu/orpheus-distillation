"""The server address a user gives becomes one WebSocket URL of the speech route."""

from __future__ import annotations

import pytest

from src.dataset.tts.transport import build_tts_url


@pytest.mark.parametrize(
    ("server", "expected"),
    [
        ("https://host", "wss://host/ws/tts"),
        ("ws://host:8000/", "ws://host:8000/ws/tts"),
        ("host:8000", "ws://host:8000/ws/tts"),
        ("wss://host/base", "wss://host/base/ws/tts"),
        ("wss://host/ws/tts", "wss://host/ws/tts"),
        ("http://host?region=eu", "ws://host/ws/tts?region=eu"),
    ],
    ids=["secure-http", "trailing-slash", "bare-host", "base-path", "route-once", "query"],
)
def test_url_targets_speech_route(server: str, expected: str) -> None:
    """Each address form maps to the WebSocket scheme and ends at the speech route once.

    Args:
        server: The address the user gave.
        expected: The URL the client opens.

    """
    assert build_tts_url(server) == expected


def test_empty_address_rejected() -> None:
    """A blank address has no URL."""
    with pytest.raises(ValueError, match="empty"):
        build_tts_url("  ")

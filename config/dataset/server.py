"""Orpheus server route and client retry policy."""

from __future__ import annotations

TTS_ROUTE = "/ws/tts"
HTTP_TO_WS_SCHEME = {"http": "ws", "https": "wss"}
CONNECT_ATTEMPTS = 5
RETRYABLE_STATUS_CODES = (404, 502)
BACKOFF_BASE_SECONDS = 2.0
NORMAL_CLOSE_CODE = 1000
ABNORMAL_CLOSE_CODE = 1006

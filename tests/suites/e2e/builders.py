"""Builders for the e2e suite: the live Orpheus server."""

from __future__ import annotations

import pytest

from schemas.dataset.settings import ServerSettings
from tests.harness.environment import API_KEY_VARIABLE, SERVER_URL_VARIABLE, read_hidden_variable

LIVE_PROMPT_COUNT = 2
LEADING_SILENCE_MARGIN_MS = 100.0
"""How far the measured leading silence can exceed the server's pad. A soft onset, such as a breath, stays under the
detector threshold for a while."""


def read_live_server() -> ServerSettings:
    """Read the live Orpheus server from the shell, and fail the test when a variable is missing.

    Returns:
        The server address and API key.

    """
    url = read_hidden_variable(SERVER_URL_VARIABLE)
    if url is None:
        pytest.fail(
            f"{SERVER_URL_VARIABLE} is not set: the synthesis e2e test needs the address of a live Orpheus server"
        )
    api_key = read_hidden_variable(API_KEY_VARIABLE)
    if api_key is None:
        pytest.fail(f"{API_KEY_VARIABLE} is not set: the synthesis e2e test needs the API key of the Orpheus server")
    return ServerSettings(url=url, api_key=api_key)

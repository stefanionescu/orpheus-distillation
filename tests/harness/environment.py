"""Environment variables for one test. Tests name a variable only here."""

from __future__ import annotations

import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable

    import pytest

# reason: The value is a made-up token that only the tests set, so it grants no access.
HF_TOKEN = "hf-test-token"  # noqa: S105
SERVER_URL_VARIABLE = "ORPHEUS_SERVER_URL"
API_KEY_VARIABLE = "ORPHEUS_API_KEY"
CACHE_FOLDER_VARIABLE = "VOXCPM_CACHE_FOLDER"
"""The Hub cache folder where the e2e training tests download the base model."""

CLEARED_VARIABLES = ("HF_TOKEN", "HF_HOME", "WORLD_SIZE", "LOCAL_RANK")
"""Variables no suite takes from the developer, so no test uses a Hub token or runs distributed."""

SERVER_VARIABLES = (SERVER_URL_VARIABLE, API_KEY_VARIABLE)
"""The live Orpheus server variables, which only the e2e suite reads."""

HIDDEN_PREFIX = "TESTS_HIDDEN_"
"""The prefix that `hide_variables` adds; no repository code reads such a name."""


def clear_variables(names: Iterable[str]) -> None:
    """Remove variables from the test process environment.

    Args:
        names: The variable names.

    """
    for name in names:
        os.environ.pop(name, None)


def hide_variables(names: Iterable[str]) -> None:
    """Move variables under names no code reads, so only a test that asks sees them.

    Args:
        names: The variable names; an unset variable stays unset.

    """
    for name in names:
        value = os.environ.pop(name, None)
        if value is not None:
            os.environ[f"{HIDDEN_PREFIX}{name}"] = value


def read_hidden_variable(name: str) -> str | None:
    """Read a variable that `hide_variables` moved.

    Args:
        name: The name the developer sets.

    Returns:
        The stripped value, or None when unset or blank.

    """
    return read_variable(f"{HIDDEN_PREFIX}{name}")


def read_variable(name: str) -> str | None:
    """Read a variable of the e2e environment.

    Args:
        name: The variable name.

    Returns:
        The stripped value, or None when unset or blank.

    """
    return os.environ.get(name, "").strip() or None


def set_hf_token(monkeypatch: pytest.MonkeyPatch) -> str:
    """Set the Hugging Face token so the upload commands accept the run.

    Args:
        monkeypatch: Removes the variable after the test.

    Returns:
        The token.

    """
    monkeypatch.setenv("HF_TOKEN", HF_TOKEN)
    return HF_TOKEN


def set_world_size(monkeypatch: pytest.MonkeyPatch, value: str) -> None:
    """Set the process count that torchrun reports.

    Args:
        monkeypatch: Removes the variable after the test.
        value: The variable text.

    """
    monkeypatch.setenv("WORLD_SIZE", value)


def set_environment(
    monkeypatch: pytest.MonkeyPatch,
    *,
    server_url: str | None = None,
    api_key: str | None = None,
    hf_token: str | None = None,
) -> None:
    """Set the variables that the settings reader reads.

    Args:
        monkeypatch: Restores each variable after the test.
        server_url: ORPHEUS_SERVER_URL, or None to leave it unset.
        api_key: ORPHEUS_API_KEY, or None to leave it unset.
        hf_token: HF_TOKEN, or None to leave it unset.

    """
    variables = {SERVER_URL_VARIABLE: server_url, API_KEY_VARIABLE: api_key, "HF_TOKEN": hf_token}
    for name, value in variables.items():
        if value is not None:
            monkeypatch.setenv(name, value)

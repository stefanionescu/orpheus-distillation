"""Flags and the environment resolve into the server and Hub settings of a run."""

from __future__ import annotations

from typing import TYPE_CHECKING
from dataclasses import replace

import pytest

from src.dataset.errors import UsageError
from src.dataset.cli.main import main
from src.dataset.settings import read_environment, build_hub_settings, build_server_settings
from schemas.dataset.settings import HubSettings, ServerSettings
from src.dataset.cli.arguments import EXIT_USAGE
from tests.harness.environment import HF_TOKEN, set_environment
from tests.suites.unit.builders import (
    API_KEY,
    SERVER_URL,
    DATASET_REPO,
    OTHER_API_KEY,
    OTHER_SERVER_URL,
    DEFAULT_ARGUMENTS,
    build_run_flags,
    build_environment,
    install_fake_client,
)

if TYPE_CHECKING:
    from pathlib import Path


def test_flag_beats_variable() -> None:
    """A flag wins over its environment variable."""
    arguments = replace(DEFAULT_ARGUMENTS, server=SERVER_URL, api_key=API_KEY)
    environment = build_environment(server_url=OTHER_SERVER_URL, api_key=OTHER_API_KEY)

    assert build_server_settings(arguments, environment) == ServerSettings(url=SERVER_URL, api_key=API_KEY)


def test_variable_fills_absent_flag() -> None:
    """The environment supplies a value whose flag is absent or blank."""
    arguments = replace(DEFAULT_ARGUMENTS, api_key="  ")
    environment = build_environment(server_url=OTHER_SERVER_URL, api_key=OTHER_API_KEY)

    settings = build_server_settings(arguments, environment)

    assert settings == ServerSettings(url=OTHER_SERVER_URL, api_key=OTHER_API_KEY)


def test_missing_server_url_rejected() -> None:
    """Without a flag or variable, the missing server URL stops the run with a usage error naming both."""
    with pytest.raises(UsageError, match="--server or set ORPHEUS_SERVER_URL"):
        build_server_settings(DEFAULT_ARGUMENTS, build_environment(api_key=API_KEY))


def test_missing_api_key_rejected() -> None:
    """Without a flag or variable, the missing API key stops the run with a usage error naming both."""
    with pytest.raises(UsageError, match="--api-key or set ORPHEUS_API_KEY"):
        build_server_settings(DEFAULT_ARGUMENTS, build_environment(server_url=SERVER_URL))


def test_hub_needs_token() -> None:
    """Without HF_TOKEN the Hub settings fail with a usage error that names the variable."""
    with pytest.raises(UsageError, match="set HF_TOKEN"):
        build_hub_settings(DEFAULT_ARGUMENTS, build_environment())


def test_hub_visibility_follows_flag() -> None:
    """The repository stays private unless the run passes --public."""
    environment = build_environment(hf_token=HF_TOKEN)

    private = build_hub_settings(DEFAULT_ARGUMENTS, environment)
    public = build_hub_settings(replace(DEFAULT_ARGUMENTS, public=True), environment)

    assert private == HubSettings(token=HF_TOKEN, repo=DATASET_REPO, public=False)
    assert public == HubSettings(token=HF_TOKEN, repo=DATASET_REPO, public=True)


def test_environment_skips_blank_values(monkeypatch: pytest.MonkeyPatch) -> None:
    """The reader treats a blank variable as unset and strips the others.

    Args:
        monkeypatch: Restores the environment.

    """
    set_environment(monkeypatch, server_url="   ", api_key=f" {API_KEY} ", hf_token=HF_TOKEN)

    assert read_environment() == build_environment(api_key=API_KEY, hf_token=HF_TOKEN)


def test_missing_server_exits_usage(caplog: pytest.LogCaptureFixture) -> None:
    """A run with no server URL in the flags or environment exits with the usage code and says what to set.

    Args:
        caplog: Captures log records.

    """
    exit_code = main([])

    assert exit_code == EXIT_USAGE
    assert "ORPHEUS_SERVER_URL" in caplog.text


def test_publish_needs_token_first(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """With --publish and no HF_TOKEN, the command exits with the usage code before it synthesizes or writes anything.

    Args:
        tmp_path: The test folder.
        monkeypatch: Replaces the Orpheus client.

    """
    client = install_fake_client(monkeypatch)
    output_folder = tmp_path / "output"

    exit_code = main([*build_run_flags(tmp_path, output_folder), "--publish"])

    assert exit_code == EXIT_USAGE
    assert client.calls == []
    assert not output_folder.exists()

"""Settings reader, the only dataset module that reads the environment.

A flag wins over its environment variable, and the variable wins over the default.
"""

from __future__ import annotations

import os
from typing import TYPE_CHECKING

from src.dataset.errors import UsageError
from schemas.dataset.settings import HubSettings, ServerSettings, DatasetEnvironment

if TYPE_CHECKING:
    from schemas.dataset.arguments import DatasetArguments


def _read_variable(name: str) -> str | None:
    value = os.environ.get(name, "").strip()
    return value or None


def _select_value(flag_value: str | None, variable_value: str | None) -> str | None:
    if flag_value is not None and flag_value.strip():
        return flag_value.strip()
    return variable_value


def read_environment() -> DatasetEnvironment:
    """Read the environment variables, treating an empty value as unset.

    Returns:
        The server URL, API key, and Hugging Face token, each None when unset.

    """
    return DatasetEnvironment(
        server_url=_read_variable("ORPHEUS_SERVER_URL"),
        api_key=_read_variable("ORPHEUS_API_KEY"),
        hf_token=_read_variable("HF_TOKEN"),
    )


def build_server_settings(arguments: DatasetArguments, environment: DatasetEnvironment) -> ServerSettings:
    """Resolve the Orpheus server of a run.

    Args:
        arguments: Parsed flags.
        environment: Variables from `read_environment`.

    Returns:
        The server URL and API key.

    Raises:
        UsageError: The server URL or the API key is missing.

    """
    url = _select_value(arguments.server, environment.server_url)
    if url is None:
        message = "Missing server URL: pass --server or set ORPHEUS_SERVER_URL"
        raise UsageError(message)
    api_key = _select_value(arguments.api_key, environment.api_key)
    if api_key is None:
        message = "Missing API key: pass --api-key or set ORPHEUS_API_KEY"
        raise UsageError(message)
    return ServerSettings(url=url, api_key=api_key)


def build_hub_settings(arguments: DatasetArguments, environment: DatasetEnvironment) -> HubSettings:
    """Resolve the Hub repository that `--publish` and `--publish-only` publish to.

    Args:
        arguments: Parsed flags.
        environment: Variables from `read_environment`.

    Returns:
        The token, repository, and visibility.

    Raises:
        UsageError: HF_TOKEN is not set.

    """
    if environment.hf_token is None:
        message = "Missing Hugging Face token: set HF_TOKEN to publish with --publish or --publish-only"
        raise UsageError(message)
    return HubSettings(token=environment.hf_token, repo=arguments.dataset_repo, public=arguments.public)

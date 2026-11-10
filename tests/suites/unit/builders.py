"""Builders and named values private to the unit suite."""

from __future__ import annotations

import io
from typing import TYPE_CHECKING, NoReturn, override
from pathlib import Path

from src.dataset.cli import generate
from tests.harness.tts import FakeTtsClient
from tests.harness.tasks import build_prompt_list
from config.dataset.paths import OUTPUT_FOLDER
from schemas.dataset.settings import DatasetEnvironment
from config.dataset.generation import CONCURRENCY, CLIPS_PER_SHARD
from schemas.dataset.arguments import DatasetArguments

if TYPE_CHECKING:
    from types import ModuleType

    import pytest

    from tests.harness.hub import FakeHubApi

SILENCE_TOLERANCE_MS = 15.0
"""How far the measured leading silence can sit from the written silence: one and a half RMS windows."""

SILENCE_SECONDS = 0.2
TONE_SECONDS = 0.5
CLICK_SECONDS = 0.002
CLIP_SECONDS = 3

SERVER_URL = "ws://orpheus.test:8000"
OTHER_SERVER_URL = "wss://other.test"
API_KEY = "orpheus-test-key"
OTHER_API_KEY = "other-test-key"
DATASET_REPO = "owner/dataset"

DEFAULT_ARGUMENTS = DatasetArguments(
    publish_only=False,
    server=None,
    api_key=None,
    prompts_path=None,
    voice=None,
    max_prompts=None,
    clips_per_shard=CLIPS_PER_SHARD,
    concurrency=CONCURRENCY,
    resume=False,
    output_folder=Path(OUTPUT_FOLDER),
    publish=False,
    dataset_repo=DATASET_REPO,
    public=False,
    yes=False,
)
"""The flags of a run that passes none, with a repository no test publishes to."""


def build_environment(
    *,
    server_url: str | None = None,
    api_key: str | None = None,
    hf_token: str | None = None,
) -> DatasetEnvironment:
    """Build the settings reader's record without touching the process environment.

    Args:
        server_url: The server URL.
        api_key: The API key.
        hf_token: The Hugging Face token.

    Returns:
        The environment record.

    """
    return DatasetEnvironment(server_url=server_url, api_key=api_key, hf_token=hf_token)


PROMPT = "The quick brown fox jumps over the lazy dog."
AUDIO_FRAME = bytes(range(256)) * 4
"""One binary frame of 16-bit PCM audio."""

GOING_AWAY_CODE = 1001
"""A close code that is neither normal nor abnormal: the server shuts down."""

BAD_GATEWAY = 502
UNAUTHORIZED = 401


class TerminalStream(io.StringIO):
    """A text stream that answers `isatty` as told, to stand in for a terminal or a log file."""

    def __init__(self, text: str = "", *, is_terminal: bool) -> None:
        """Keep the text to read and the `isatty` answer.

        Args:
            text: The text to read back, such as a typed answer.
            is_terminal: Whether the stream claims to be a terminal.

        """
        super().__init__(text)
        self._is_terminal = is_terminal

    @override
    def isatty(self) -> bool:
        """Answer whether the stream is a terminal.

        Returns:
            The answer the test chose.

        """
        return self._is_terminal


class InterruptedTerminal(TerminalStream):
    """A terminal whose user presses Ctrl-C at the prompt."""

    @override
    def readline(self, size: int | None = -1) -> NoReturn:
        """Stop the read as Ctrl-C does.

        Args:
            size: The read limit, which the interrupt ignores.

        Raises:
            KeyboardInterrupt: Always.

        """
        del size
        raise KeyboardInterrupt


RUN_PROMPT_COUNT = 2
"""The prompt count of a small generate run."""


def install_fake_client(monkeypatch: pytest.MonkeyPatch, client: FakeTtsClient | None = None) -> FakeTtsClient:
    """Make the generate command build a fake Orpheus client in place of a server connection.

    Args:
        monkeypatch: Restores the client class after the test.
        client: The fake to hand out, or None for a new one that never fails.

    Returns:
        The fake client that every run of the test uses.

    """
    client = FakeTtsClient() if client is None else client

    def build_client(url: str, api_key: str) -> FakeTtsClient:
        """Record the run's server and hand out the fake client.

        Args:
            url: The server URL.
            api_key: The API key.

        Returns:
            The fake client.

        """
        client.servers.append((url, api_key))
        return client

    monkeypatch.setattr(generate, "OrpheusClient", build_client)
    return client


def build_run_flags(tmp_path: Path, output_folder: Path, prompt_count: int = RUN_PROMPT_COUNT) -> list[str]:
    """Build the flags of a small generate run, and write its prompt file.

    Args:
        tmp_path: Where the prompt file goes.
        output_folder: The run's output folder.
        prompt_count: How many prompts the file holds.

    Returns:
        The flags.

    """
    prompts_path = tmp_path / "prompts.txt"
    prompts_path.write_text("\n".join(build_prompt_list(prompt_count)), encoding="utf-8")
    return [
        "--server",
        SERVER_URL,
        "--api-key",
        API_KEY,
        "--prompts-file",
        str(prompts_path),
        "--output-folder",
        str(output_folder),
        "--concurrency",
        "1",
    ]


def install_fake_hub_api(monkeypatch: pytest.MonkeyPatch, module: ModuleType, api: FakeHubApi) -> list[str]:
    """Make a command module build the fake Hub client in place of `HfApi`.

    Args:
        monkeypatch: Restores the client class after the test.
        module: The command module that builds the client.
        api: The fake client to hand out.

    Returns:
        The token of each client the module builds, filled as the command runs.

    """
    tokens: list[str] = []

    def connect_hub(*, token: str) -> FakeHubApi:
        """Keep the token and hand out the fake client.

        Args:
            token: The Hugging Face token.

        Returns:
            The fake client.

        """
        tokens.append(token)
        return api

    monkeypatch.setattr(module, "HfApi", connect_hub)
    return tokens


def read_results(capsys: pytest.CaptureFixture[str]) -> dict[str, list[str]]:
    """Read the `key=value` result lines that a training command printed to stdout.

    Args:
        capsys: Captures stdout.

    Returns:
        Each value of each key, in print order.

    """
    results: dict[str, list[str]] = {}
    for line in capsys.readouterr().out.splitlines():
        key, value = line.split("=", 1)
        results.setdefault(key, []).append(value)
    return results

"""Argparse checks every flag value before any work; a bad count exits with the usage code and names its flag."""

from __future__ import annotations

import sys
import signal
from typing import TYPE_CHECKING

import pytest

from src.dataset.cli.main import main
from tests.harness.voices import SECOND_VOICE, TABLE_VOICES
from schemas.dataset.arguments import DatasetArguments
from src.dataset.cli.arguments import EXIT_USAGE, EXIT_SUCCESS, EXIT_SIGNAL_BASE, parse_arguments
from tests.suites.unit.builders import (
    API_KEY,
    SERVER_URL,
    DATASET_REPO,
    RUN_PROMPT_COUNT,
    TerminalStream,
    InterruptedTerminal,
    build_run_flags,
    install_fake_client,
)

if TYPE_CHECKING:
    from pathlib import Path

    from tests.harness.tts import FakeTtsClient


def _prepare_existing_run(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    standard_input: TerminalStream,
) -> tuple[FakeTtsClient, Path, Path]:
    monkeypatch.setattr(sys, "stdin", standard_input)
    client = install_fake_client(monkeypatch)
    output_folder = tmp_path / "output"
    clip_path = output_folder / "audio" / "clip_00000_earlier.wav"
    clip_path.parent.mkdir(parents=True)
    clip_path.write_bytes(b"earlier run")
    return client, output_folder, clip_path


def test_flags_fill_arguments(tmp_path: Path) -> None:
    """Each flag lands in its field of the arguments record.

    Args:
        tmp_path: The test folder.

    """
    prompts_path = tmp_path / "prompts.txt"
    flags = [
        "--publish-only",
        "--server",
        SERVER_URL,
        "--api-key",
        API_KEY,
        "--prompts-file",
        str(prompts_path),
        "--voice",
        SECOND_VOICE.name,
        "--max-prompts",
        "3",
        "--clips-per-shard",
        "4",
        "--concurrency",
        "2",
        "--resume",
        "--output-folder",
        str(tmp_path),
        "--publish",
        "--dataset-repo",
        DATASET_REPO,
        "--public",
        "--yes",
    ]

    assert parse_arguments(flags) == DatasetArguments(
        publish_only=True,
        server=SERVER_URL,
        api_key=API_KEY,
        prompts_path=prompts_path,
        voice=SECOND_VOICE.name,
        max_prompts=3,
        clips_per_shard=4,
        concurrency=2,
        resume=True,
        output_folder=tmp_path,
        publish=True,
        dataset_repo=DATASET_REPO,
        public=True,
        yes=True,
    )


@pytest.mark.parametrize("flag", ["--concurrency", "--clips-per-shard", "--max-prompts"])
def test_zero_count_rejected(flag: str) -> None:
    """A count below 1 exits with the usage code before any work.

    Args:
        flag: The count flag.

    """
    with pytest.raises(SystemExit) as caught:
        parse_arguments([flag, "0"])

    assert caught.value.code == EXIT_USAGE


@pytest.mark.parametrize(
    ("flags", "exit_code"),
    [(["--help"], EXIT_SUCCESS), (["--concurrency", "0"], EXIT_USAGE)],
    ids=["help", "bad-flag"],
)
def test_parser_exit_returned(flags: list[str], exit_code: int) -> None:
    """The entry point returns the parser's exit code instead of raising: success for help, usage for a bad flag.

    Args:
        flags: The command flags.
        exit_code: The code the parser exits with.

    """
    assert main(flags) == exit_code


def test_clean_needs_consent(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Without a terminal, a run over earlier output exits with the usage code and deletes nothing.

    Args:
        tmp_path: The test folder.
        monkeypatch: Replaces standard input and the Orpheus client.

    """
    client, output_folder, clip_path = _prepare_existing_run(tmp_path, monkeypatch, TerminalStream(is_terminal=False))

    exit_code = main(build_run_flags(tmp_path, output_folder))

    assert exit_code == EXIT_USAGE
    assert clip_path.exists()
    assert client.calls == []


def test_yes_allows_clean(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """With --yes, the run cleans the earlier output and synthesizes every clip.

    Args:
        tmp_path: The test folder.
        monkeypatch: Replaces standard input and the Orpheus client.

    """
    client, output_folder, clip_path = _prepare_existing_run(tmp_path, monkeypatch, TerminalStream(is_terminal=False))

    exit_code = main([*build_run_flags(tmp_path, output_folder), "--yes"])

    assert exit_code == EXIT_SUCCESS
    assert not clip_path.exists()
    assert len(client.calls) == len(TABLE_VOICES) * RUN_PROMPT_COUNT


@pytest.mark.parametrize(("answer", "is_deleted"), [("Y\n", True), ("n\n", False)], ids=["yes", "no"])
def test_terminal_answer_decides(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    *,
    answer: str,
    is_deleted: bool,
) -> None:
    """On a terminal the command asks on stderr, deletes on yes in any case, and keeps the output on any other answer.

    Args:
        tmp_path: The test folder.
        monkeypatch: Replaces standard input and the Orpheus client.
        capsys: Captures standard error.
        answer: The line the user types.
        is_deleted: Whether the earlier output is gone afterwards.

    """
    _, output_folder, clip_path = _prepare_existing_run(tmp_path, monkeypatch, TerminalStream(answer, is_terminal=True))

    exit_code = main(build_run_flags(tmp_path, output_folder))

    assert exit_code == (EXIT_SUCCESS if is_deleted else EXIT_USAGE)
    assert clip_path.exists() is not is_deleted
    assert str(output_folder) in capsys.readouterr().err


def test_interrupted_prompt_keeps_output(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Ctrl-C at the prompt exits with 128 plus SIGINT, before any request, and deletes nothing.

    Args:
        tmp_path: The test folder.
        monkeypatch: Replaces standard input and the Orpheus client.

    """
    client, output_folder, clip_path = _prepare_existing_run(
        tmp_path, monkeypatch, InterruptedTerminal(is_terminal=True)
    )

    exit_code = main(build_run_flags(tmp_path, output_folder))

    assert exit_code == EXIT_SIGNAL_BASE + signal.SIGINT
    assert clip_path.exists()
    assert client.calls == []

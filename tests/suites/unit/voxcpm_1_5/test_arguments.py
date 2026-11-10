"""The VoxCPM 1.5 commands stop with a usage error on bad flags or variables, before they touch a file."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from src.train.cli import EXIT_USAGE
from tests.harness.hub import install_fake_hub
from tests.harness.voices import FIRST_VOICE
from tests.harness.environment import set_world_size
from src.train.voxcpm_1_5.commands import train, publish, pipeline

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Callable, Sequence

TRAIN_FOLDERS = (
    "--base-model-folder",
    "model",
    "--train-manifest",
    "train.jsonl",
    "--tokenizer-folder",
    "tokenizer",
    "--checkpoints-folder",
    "checkpoints",
    "--events-folder",
    "events",
)


def _read_usage_error(
    capsys: pytest.CaptureFixture[str], command: Callable[[Sequence[str] | None], int], arguments: Sequence[str]
) -> str:
    with pytest.raises(SystemExit) as exit_info:
        command(arguments)
    assert exit_info.value.code == EXIT_USAGE
    return capsys.readouterr().err


def test_speaker_not_a_voice(capsys: pytest.CaptureFixture[str]) -> None:
    """The voice flag takes a voice, so an Orpheus speaker is a usage error.

    Args:
        capsys: Reads stderr.

    """
    assert "--voice" in _read_usage_error(capsys, train.main, ["--voice", FIRST_VOICE.speaker, *TRAIN_FOLDERS])


def test_clean_stays_in_runs(
    tmp_path: Path, capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    """A run name of `..` stops the pipeline before --clean deletes the folder above the runs folder.

    Args:
        tmp_path: Holds the runs folder and a file beside it.
        capsys: Reads stderr.
        monkeypatch: Replaces the Hub client, so a run that starts downloads nothing.

    """
    install_fake_hub(monkeypatch, {})
    neighbour_path = tmp_path / "neighbour.txt"
    neighbour_path.write_text("keep", encoding="utf-8")
    (tmp_path / "runs").mkdir()
    folders = ["--runs-folder", str(tmp_path / "runs"), "--cache-folder", str(tmp_path / "cache")]

    assert "--run-name" in _read_usage_error(capsys, pipeline.main, ["--run-name", "..", *folders, "--clean", "--yes"])
    assert neighbour_path.exists()


def test_publish_needs_token(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """Publishing without a dry run needs HF_TOKEN, and the command stops before it stages a file.

    Args:
        tmp_path: The test folder, which the command must leave empty.
        capsys: Reads stderr.

    """
    arguments = [
        "--run-name",
        "run",
        "--checkpoints-folder",
        str(tmp_path / "checkpoints"),
        "--base-model-folder",
        "model",
    ]

    assert "HF_TOKEN" in _read_usage_error(capsys, publish.main, [*arguments, "--tokenizer-folder", "tokenizer"])
    assert list(tmp_path.iterdir()) == []


def test_pipeline_publish_needs_token(
    tmp_path: Path, capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    """A pipeline run that publishes needs HF_TOKEN, and the command stops before the downloads start.

    Args:
        tmp_path: Holds the runs and cache folders.
        capsys: Reads stderr.
        monkeypatch: Replaces the Hub client.

    """
    hub = install_fake_hub(monkeypatch, {})
    folders = ["--runs-folder", str(tmp_path / "runs"), "--cache-folder", str(tmp_path / "cache")]

    assert "HF_TOKEN" in _read_usage_error(capsys, pipeline.main, ["--run-name", "run", *folders, "--publish"])
    assert hub.downloads == []


def test_invalid_world_size_rejected(capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch) -> None:
    """An invalid torchrun layout stops training with a usage error that names the variable.

    Args:
        capsys: Reads stderr.
        monkeypatch: Sets the variable.

    """
    set_world_size(monkeypatch, "0")

    assert "WORLD_SIZE" in _read_usage_error(capsys, train.main, ["--voice", FIRST_VOICE.name, *TRAIN_FOLDERS])

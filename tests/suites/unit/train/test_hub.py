"""A Hub failure of the shared snapshot download fails the command with exit code 1 instead of a traceback."""

from __future__ import annotations

from typing import TYPE_CHECKING, NoReturn

import httpx2
import huggingface_hub

from config.hub import DATASET_REPO
from src.train.cli import EXIT_FAILURE
from tests.harness.hub import install_fake_hub
from src.train.__main__ import main as run_training_command
from config.voxcpm_1_5.hub import BASE_MODEL_REPO

if TYPE_CHECKING:
    from pathlib import Path

    import pytest

MODEL_NAME = "voxcpm_1_5"


def _refuse_connection(*_arguments: object, **_options: object) -> NoReturn:
    message = "Connection refused"
    raise httpx2.ConnectError(message)


def test_missing_repo_fails(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A repository missing from the Hub fails the download with exit code 1 instead of a traceback.

    Args:
        tmp_path: The test folder.
        monkeypatch: Replaces the Hub client.

    """
    install_fake_hub(monkeypatch, {DATASET_REPO: tmp_path / "dataset", BASE_MODEL_REPO: tmp_path / "model"})
    arguments = [MODEL_NAME, "download", "--cache-folder", str(tmp_path), "--base-model-repo", "owner/missing"]

    assert run_training_command(arguments) == EXIT_FAILURE


def test_unreachable_hub_fails_download(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A Hub that refuses the connection fails the download with exit code 1 instead of a traceback.

    Args:
        tmp_path: The test folder.
        monkeypatch: Makes the download refuse the connection.

    """
    monkeypatch.setattr(huggingface_hub, "snapshot_download", _refuse_connection)

    assert run_training_command([MODEL_NAME, "download", "--cache-folder", str(tmp_path)]) == EXIT_FAILURE

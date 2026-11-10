"""The training entry point hands a model command its flags."""

from __future__ import annotations

from typing import TYPE_CHECKING

from config.hub import DATASET_REPO, REPO_TYPE_MODEL, REPO_TYPE_DATASET
from src.train.cli import EXIT_SUCCESS
from tests.state.hub import DownloadCall
from tests.harness.hub import install_fake_hub
from src.train.__main__ import main as run_training_command
from tests.suites.unit.builders import read_results
from config.models.voxcpm_1_5.hub import BASE_MODEL_REPO

if TYPE_CHECKING:
    from pathlib import Path

    import pytest

MODEL_NAME = "voxcpm_1_5"


def test_dispatch_runs_download(
    tmp_path: Path, capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    """The entry point hands the flags after the model and command to the download, which prints both folders.

    Args:
        tmp_path: The test folder.
        capsys: Reads stdout.
        monkeypatch: Replaces the Hub client.

    """
    hub = install_fake_hub(monkeypatch, {DATASET_REPO: tmp_path / "dataset", BASE_MODEL_REPO: tmp_path / "model"})

    exit_code = run_training_command([MODEL_NAME, "download", "--cache-folder", str(tmp_path / "cache")])

    assert exit_code == EXIT_SUCCESS
    assert read_results(capsys) == {
        "dataset_folder": [str(tmp_path / "dataset")],
        "base_model_folder": [str(tmp_path / "model")],
    }
    assert hub.downloads == [
        DownloadCall(repo_id=DATASET_REPO, repo_type=REPO_TYPE_DATASET, folder=tmp_path / "dataset"),
        DownloadCall(repo_id=BASE_MODEL_REPO, repo_type=REPO_TYPE_MODEL, folder=tmp_path / "model"),
    ]

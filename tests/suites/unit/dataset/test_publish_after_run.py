"""With --publish, generate publishes the dataset it wrote; a failed publish leaves it for --publish-only."""

from __future__ import annotations

import signal
from typing import TYPE_CHECKING

from src.dataset.cli import generate
from tests.harness.hub import FakeHubApi
from src.dataset.shards import write_shards
from src.dataset.cli.main import main
from src.dataset.generation import pipeline
from src.dataset.cli.arguments import EXIT_FAILURE, EXIT_SUCCESS, EXIT_SIGNAL_BASE
from tests.harness.environment import HF_TOKEN, set_environment
from tests.suites.unit.builders import (
    DATASET_REPO,
    build_run_flags,
    install_fake_client,
    install_fake_hub_api,
)
from src.dataset.generation.tasks import build_output_folders

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Sequence

    import pytest

    from schemas.dataset.generation import Clip


def _run_generate_publish(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, api: FakeHubApi) -> tuple[int, list[str]]:
    set_environment(monkeypatch, hf_token=HF_TOKEN)
    install_fake_client(monkeypatch)
    tokens = install_fake_hub_api(monkeypatch, generate, api)
    flags = [*build_run_flags(tmp_path, tmp_path / "output"), "--publish", "--dataset-repo", DATASET_REPO]
    return main(flags), tokens


def test_publish_follows_run(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """After the run, the shards and stats file that it wrote go to the repository with the environment token.

    Args:
        tmp_path: The test folder.
        monkeypatch: Sets the token and replaces the speech and Hub clients.

    """
    api = FakeHubApi()
    folders = build_output_folders(tmp_path / "output")

    exit_code, tokens = _run_generate_publish(tmp_path, monkeypatch, api)

    assert (exit_code, tokens) == (EXIT_SUCCESS, [HF_TOKEN])
    assert [repository.repo_id for repository in api.created_repos] == [DATASET_REPO]
    assert [upload.content for upload in api.uploads[1:]] == [str(folders.shards_folder), str(folders.stats_path)]


def test_failed_publish_keeps_dataset(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A failed publish exits with the failure code and keeps the dataset for --publish-only.

    Args:
        tmp_path: The test folder.
        monkeypatch: Sets the token and replaces the speech and Hub clients.

    """
    exit_code, _ = _run_generate_publish(tmp_path, monkeypatch, FakeHubApi(failing_method="upload_folder"))

    assert exit_code == EXIT_FAILURE
    assert build_output_folders(tmp_path / "output").stats_path.is_file()


def test_late_stop_skips_publish(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """SIGTERM during the shard write exits with 128 plus the signal once the write ends, and publishes nothing.

    Args:
        tmp_path: The test folder.
        monkeypatch: Sets the token, replaces the clients, and signals during the shard write.

    """
    api = FakeHubApi()

    def write_shards_on_signal(clips: Sequence[Clip], shards_folder: Path, clips_per_shard: int) -> int:
        signal.raise_signal(signal.SIGTERM)
        return write_shards(clips, shards_folder, clips_per_shard)

    monkeypatch.setattr(pipeline, "write_shards", write_shards_on_signal)
    # When the command ignores SIGTERM, the default action kills pytest; a KeyboardInterrupt fails the test instead.
    pytest_sigterm = signal.signal(signal.SIGTERM, signal.default_int_handler)
    try:
        exit_code, _ = _run_generate_publish(tmp_path, monkeypatch, api)
    finally:
        signal.signal(signal.SIGTERM, pytest_sigterm)

    assert exit_code == EXIT_SIGNAL_BASE + signal.SIGTERM
    assert (api.created_repos, api.uploads) == ([], [])

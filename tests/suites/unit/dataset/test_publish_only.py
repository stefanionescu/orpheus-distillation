"""The publish-only mode publishes the dataset on disk, and fails without shards or on a Hub error."""

from __future__ import annotations

from typing import TYPE_CHECKING

from src.dataset.cli import publish
from src.dataset.stats import write_stats
from tests.harness.hub import FakeHubApi
from src.dataset.cli.main import main
from src.dataset.hub.card import format_card
from tests.harness.records import build_stats
from src.dataset.cli.arguments import EXIT_FAILURE, EXIT_SUCCESS
from tests.harness.environment import HF_TOKEN, set_environment
from tests.suites.unit.builders import (
    DATASET_REPO,
    install_fake_hub_api,
)
from src.dataset.generation.tasks import build_output_folders, prepare_output_folders

if TYPE_CHECKING:
    from pathlib import Path

    import pytest


def _write_dataset(output_folder: Path, *, has_shards: bool = True) -> None:
    folders = build_output_folders(output_folder)
    prepare_output_folders(folders, resume=False)
    write_stats(folders.stats_path, build_stats())
    if has_shards:
        (folders.shards_folder / "shard-000000.tar").write_bytes(b"")


def _publish_only(output_folder: Path, monkeypatch: pytest.MonkeyPatch, api: FakeHubApi) -> tuple[int, list[str]]:
    set_environment(monkeypatch, hf_token=HF_TOKEN)
    tokens = install_fake_hub_api(monkeypatch, publish, api)
    return main(["--publish-only", "--output-folder", str(output_folder), "--dataset-repo", DATASET_REPO]), tokens


def test_publish_only_uploads_dataset(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A complete dataset goes to the Hub with the environment token and a card of the stats on disk.

    Args:
        tmp_path: The test folder.
        monkeypatch: Sets the token and replaces the Hub client.

    """
    api = FakeHubApi()
    folders = build_output_folders(tmp_path)
    _write_dataset(tmp_path)

    exit_code, tokens = _publish_only(tmp_path, monkeypatch, api)

    assert (exit_code, tokens) == (EXIT_SUCCESS, [HF_TOKEN])
    assert [upload.content for upload in api.uploads] == [
        format_card(build_stats(), DATASET_REPO).encode(),
        str(folders.shards_folder),
        str(folders.stats_path),
    ]


def test_missing_shards_fail(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A dataset without a shard exits with the failure code before any Hub call.

    Args:
        tmp_path: The test folder.
        monkeypatch: Sets the token and replaces the Hub client.

    """
    api = FakeHubApi()
    _write_dataset(tmp_path, has_shards=False)

    exit_code, _ = _publish_only(tmp_path, monkeypatch, api)

    assert exit_code == EXIT_FAILURE
    assert api.calls == []


def test_hub_error_fails_publish(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A Hub error during the publish exits with the failure code instead of raising.

    Args:
        tmp_path: The test folder.
        monkeypatch: Sets the token and replaces the Hub client.

    """
    _write_dataset(tmp_path)

    exit_code, _ = _publish_only(tmp_path, monkeypatch, FakeHubApi(failing_method="upload_folder"))

    assert exit_code == EXIT_FAILURE

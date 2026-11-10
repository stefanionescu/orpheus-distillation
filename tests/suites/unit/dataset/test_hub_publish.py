"""A publish creates the repository and uploads the card, the shards, and the stats file, in that order."""

from __future__ import annotations

from typing import TYPE_CHECKING, NoReturn

import httpx2
import pytest

from tests.state.hub import CreateRepoCall
from tests.harness.hub import FakeHubApi, cast_hub_api
from src.dataset.hub.card import format_card
from tests.harness.records import build_stats
from src.dataset.hub.publish import PublishError, publish_dataset
from schemas.dataset.settings import HubSettings
from tests.harness.environment import HF_TOKEN
from tests.suites.unit.builders import DATASET_REPO
from src.dataset.generation.tasks import build_output_folders

if TYPE_CHECKING:
    from pathlib import Path

PRIVATE_SETTINGS = HubSettings(token=HF_TOKEN, repo=DATASET_REPO, public=False)


def _publish(api: FakeHubApi, output_folder: Path) -> None:
    publish_dataset(cast_hub_api(api), PRIVATE_SETTINGS, build_stats(), build_output_folders(output_folder))


def test_publish_runs_in_order(tmp_path: Path) -> None:
    """A publish creates a private dataset repository or keeps it, then uploads the card, shards, and stats file.

    Args:
        tmp_path: The test folder.

    """
    api = FakeHubApi()
    folders = build_output_folders(tmp_path)

    _publish(api, tmp_path)

    assert api.calls == ["create_repo", "upload_file", "list_repo_files", "upload_folder", "upload_file"]
    assert api.created_repos == [CreateRepoCall(DATASET_REPO, "dataset", is_private=True, exist_ok=True)]
    assert [(upload.repo_id, upload.repo_type, upload.path_in_repo, upload.content) for upload in api.uploads] == [
        (DATASET_REPO, "dataset", "README.md", format_card(build_stats(), DATASET_REPO).encode()),
        (DATASET_REPO, "dataset", "shards", str(folders.shards_folder)),
        (DATASET_REPO, "dataset", "stats.json", str(folders.stats_path)),
    ]


def test_previous_shards_deleted(tmp_path: Path) -> None:
    """A publish deletes earlier shards before the upload, so no stale shard stays.

    Args:
        tmp_path: The test folder.

    """
    api = FakeHubApi(repo_files=["README.md", "shards/shard-000000.tar"])

    _publish(api, tmp_path)

    assert [deletion.path_in_repo for deletion in api.deletions] == ["shards"]
    assert api.calls.index("delete_folder") < api.calls.index("upload_folder")


def test_hub_failure_stops_publish(tmp_path: Path) -> None:
    """A Hub error stops the publish with an error that names the repository, and no later step runs.

    Args:
        tmp_path: The test folder.

    """
    api = FakeHubApi(failing_method="upload_folder")

    with pytest.raises(PublishError, match=DATASET_REPO):
        _publish(api, tmp_path)

    assert api.calls[-1] == "upload_folder"


def test_network_failure_stops_publish(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A refused connection stops the publish with the publish error, which tells the user to rerun with --publish-only.

    Args:
        tmp_path: The test folder.
        monkeypatch: Makes the upload refuse the connection.

    """
    api = FakeHubApi()

    def refuse_connection(**_options: object) -> NoReturn:
        message = "Connection refused"
        raise httpx2.ConnectError(message)

    monkeypatch.setattr(api, "upload_folder", refuse_connection)

    with pytest.raises(PublishError, match=DATASET_REPO):
        _publish(api, tmp_path)

"""Publishing of a finished dataset to the Hugging Face Hub."""

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx2
from huggingface_hub.errors import HfHubHTTPError

from config.hub import CARD_FILE, REPO_TYPE_DATASET
from config.shards import SHARDS_FOLDER
from config.dataset.paths import STATS_FILE
from src.dataset.hub.card import format_card

if TYPE_CHECKING:
    from pathlib import Path

    from huggingface_hub import HfApi

    from schemas.dataset.stats import DatasetStats
    from schemas.dataset.settings import HubSettings
    from schemas.dataset.generation import OutputFolders


class PublishError(Exception):
    """Publishing to the Hub failed. The dataset on disk is complete, so `--publish-only` can retry."""


def _replace_shards(api: HfApi, repo: str, shards_folder: Path) -> None:
    """Delete the shards of an earlier publish, then upload these, so no stale shard stays.

    Args:
        api: Hub client.
        repo: Dataset repository.
        shards_folder: Shards of this run.

    """
    if any(name.startswith(f"{SHARDS_FOLDER}/") for name in api.list_repo_files(repo, repo_type=REPO_TYPE_DATASET)):
        api.delete_folder(
            SHARDS_FOLDER,
            repo_id=repo,
            repo_type=REPO_TYPE_DATASET,
            commit_message="Delete the previous WebDataset shards",
        )
    api.upload_folder(
        folder_path=shards_folder,
        path_in_repo=SHARDS_FOLDER,
        repo_id=repo,
        repo_type=REPO_TYPE_DATASET,
        commit_message="Update WebDataset shards",
    )


def publish_dataset(api: HfApi, settings: HubSettings, stats: DatasetStats, folders: OutputFolders) -> None:
    """Create the repository when missing, then upload the card, shards, and stats file.

    Args:
        api: Hub client with the token.
        settings: Repository and its visibility when new.
        stats: Run totals for the card.
        folders: Run paths.

    Raises:
        PublishError: The Hub or network failed a step. Earlier steps stay published.

    """
    try:
        api.create_repo(settings.repo, repo_type=REPO_TYPE_DATASET, private=not settings.public, exist_ok=True)
        api.upload_file(
            path_or_fileobj=format_card(stats, settings.repo).encode("utf-8"),
            path_in_repo=CARD_FILE,
            repo_id=settings.repo,
            repo_type=REPO_TYPE_DATASET,
            commit_message="Update dataset card",
        )
        _replace_shards(api, settings.repo, folders.shards_folder)
        api.upload_file(
            path_or_fileobj=folders.stats_path,
            path_in_repo=STATS_FILE,
            repo_id=settings.repo,
            repo_type=REPO_TYPE_DATASET,
            commit_message="Update dataset stats",
        )
    except (HfHubHTTPError, httpx2.TransportError, OSError) as error:
        message = f"Publishing to {settings.repo} failed: {error}"
        raise PublishError(message) from error

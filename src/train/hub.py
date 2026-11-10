"""Hub downloads and uploads that every model shares."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast
import logging
from pathlib import Path

import httpx2
import huggingface_hub
from huggingface_hub.errors import RepositoryNotFoundError

from config.hub import REPO_TYPE_MODEL

if TYPE_CHECKING:
    from collections.abc import Callable

logger = logging.getLogger(__name__)


class HubError(Exception):
    """A repository does not exist, or the token cannot read it."""


def download_snapshot(repo: str, repo_type: str, cache_folder: Path, token: str | None) -> Path:
    """Download the newest revision of a repository, or reuse the cached files.

    Args:
        repo: Repository, owner/name.
        repo_type: Dataset or model.
        cache_folder: Download cache.
        token: Hugging Face token, or None to download anonymously.

    Returns:
        Folder of the downloaded revision.

    Raises:
        HubError: The repository does not exist, the token cannot read it, or the Hub is unreachable.

    """
    logger.info("Downloading the %s repository %s into %s", repo_type, repo, cache_folder)
    download_repository = cast("Callable[..., str]", huggingface_hub.snapshot_download)
    try:
        snapshot_folder = download_repository(repo_id=repo, repo_type=repo_type, cache_dir=cache_folder, token=token)
    except RepositoryNotFoundError as error:
        message = f"The {repo_type} repository {repo} does not exist, or HF_TOKEN cannot read it"
        raise HubError(message) from error
    except httpx2.TransportError as error:
        message = f"Could not reach the Hub to download the {repo_type} repository {repo}: {error}"
        raise HubError(message) from error
    return Path(snapshot_folder)


def upload_folder(folder: Path, repo: str, token: str, commit_message: str, *, public: bool) -> str:
    """Create the model repository when missing, then upload a folder as one commit.

    Args:
        folder: Files to upload.
        repo: Model repository, owner/name.
        token: Hugging Face token with write access to the owner.
        commit_message: Commit message.
        public: Make a new repository public; otherwise it is private. An existing repository keeps its visibility.

    Returns:
        Commit URL.

    """
    api = huggingface_hub.HfApi(token=token)
    api.create_repo(repo, repo_type=REPO_TYPE_MODEL, private=not public, exist_ok=True)
    commit = api.upload_folder(
        repo_id=repo, folder_path=folder, repo_type=REPO_TYPE_MODEL, commit_message=commit_message
    )
    return commit.commit_url

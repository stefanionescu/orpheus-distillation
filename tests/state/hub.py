"""Frozen records of the calls that the Hub fakes receive."""

from __future__ import annotations

from typing import TYPE_CHECKING
from dataclasses import dataclass

if TYPE_CHECKING:
    from pathlib import Path


@dataclass(frozen=True)
class CreateRepoCall:
    """One repository creation.

    Attributes:
        repo_id: The repository.
        repo_type: The kind of repository, such as `dataset`.
        is_private: Whether a new repository is private.
        exist_ok: Whether the call accepts an existing repository.

    """

    repo_id: str
    repo_type: str | None
    is_private: bool | None
    exist_ok: bool


@dataclass(frozen=True)
class UploadCall:
    """One file or folder upload.

    Attributes:
        repo_id: The repository.
        repo_type: The kind of repository.
        path_in_repo: Where the upload lands.
        content: The uploaded bytes, or the local path as text.
        commit_message: The commit message.

    """

    repo_id: str
    repo_type: str | None
    path_in_repo: str
    content: bytes | str
    commit_message: str | None


@dataclass(frozen=True)
class DeleteCall:
    """One folder deletion.

    Attributes:
        repo_id: The repository.
        repo_type: The kind of repository.
        path_in_repo: The deleted folder.
        commit_message: The commit message.

    """

    repo_id: str
    repo_type: str | None
    path_in_repo: str
    commit_message: str | None


@dataclass(frozen=True)
class ListCall:
    """One listing of the repository files.

    Attributes:
        repo_id: The repository.
        repo_type: The kind of repository.

    """

    repo_id: str
    repo_type: str | None


@dataclass(frozen=True)
class DownloadCall:
    """One snapshot download.

    Attributes:
        repo_id: The repository, as owner/name.
        repo_type: The kind of repository the call named.
        folder: The folder the fake returned, or None for a missing repository.

    """

    repo_id: str
    repo_type: str
    folder: Path | None


@dataclass(frozen=True)
class FolderUploadCall:
    """One folder upload.

    Attributes:
        repo_id: The repository, as owner/name.
        repo_type: The kind of repository the call named.
        files: Sorted paths of the uploaded files, as the folder held them at the call.
        commit_message: The commit message.

    """

    repo_id: str
    repo_type: str
    files: tuple[str, ...]
    commit_message: str

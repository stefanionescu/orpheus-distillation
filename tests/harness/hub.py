"""Hub fakes: an HfApi stand-in for the dataset publish, and a module fake for training downloads and uploads."""

from __future__ import annotations

from typing import TYPE_CHECKING, BinaryIO, cast
from dataclasses import field, dataclass

import httpx2
import huggingface_hub
from huggingface_hub.errors import HfHubHTTPError, RepositoryNotFoundError

from config.hub import REPO_TYPE_MODEL
from tests.state.hub import (
    ListCall,
    DeleteCall,
    UploadCall,
    DownloadCall,
    CreateRepoCall,
    FolderUploadCall,
)

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Mapping

    import pytest
    from huggingface_hub import HfApi


@dataclass
class FakeHubApi:
    """The `HfApi` methods that the dataset publish calls; each records its call and can fail.

    Attributes:
        repo_files: The files in the repository before the publish.
        failing_method: The method that raises `HfHubHTTPError`, or None.
        calls: Each called method name, in order.
        created_repos: Each repository creation.
        uploads: Each file and folder upload.
        deletions: Each folder deletion.
        listings: Each file listing.

    """

    repo_files: list[str] = field(default_factory=list[str])
    failing_method: str | None = None
    calls: list[str] = field(default_factory=list[str])
    created_repos: list[CreateRepoCall] = field(default_factory=list[CreateRepoCall])
    uploads: list[UploadCall] = field(default_factory=list[UploadCall])
    deletions: list[DeleteCall] = field(default_factory=list[DeleteCall])
    listings: list[ListCall] = field(default_factory=list[ListCall])

    def _record_call(self, method: str) -> None:
        """Record a call, and fail it when the test asks.

        Args:
            method: The method name.

        Raises:
            HfHubHTTPError: The method is `failing_method`.

        """
        self.calls.append(method)
        if method == self.failing_method:
            message = f"{method} failed with HTTP 500"
            response = httpx2.Response(500, request=httpx2.Request("POST", "https://huggingface.co/api"))
            raise HfHubHTTPError(message, response=response)

    def create_repo(
        self,
        repo_id: str,
        *,
        repo_type: str | None = None,
        private: bool | None = None,
        exist_ok: bool = False,
    ) -> None:
        """Record a repository creation.

        Args:
            repo_id: The repository.
            repo_type: The kind of repository.
            private: Whether a new repository is private.
            exist_ok: Whether the call accepts an existing repository.

        """
        self._record_call("create_repo")
        self.created_repos.append(CreateRepoCall(repo_id, repo_type, private, exist_ok))

    def upload_file(
        self,
        *,
        path_in_repo: str,
        repo_id: str,
        repo_type: str | None = None,
        commit_message: str | None = None,
        **source: str | Path | bytes | BinaryIO,
    ) -> None:
        """Record a file upload; the content arrives under the keyword that `HfApi.upload_file` gives it.

        Args:
            path_in_repo: Where the file lands.
            repo_id: The repository.
            repo_type: The kind of repository.
            commit_message: The commit message.
            **source: The bytes or local file, as the only keyword left.

        """
        self._record_call("upload_file")
        content = next(iter(source.values()))
        recorded_content = content if isinstance(content, bytes) else str(content)
        self.uploads.append(UploadCall(repo_id, repo_type, path_in_repo, recorded_content, commit_message))

    def upload_folder(
        self,
        *,
        repo_id: str,
        folder_path: str | Path,
        path_in_repo: str | None = None,
        repo_type: str | None = None,
        commit_message: str | None = None,
    ) -> None:
        """Record a folder upload.

        Args:
            repo_id: The repository.
            folder_path: The local folder.
            path_in_repo: Where the folder lands.
            repo_type: The kind of repository.
            commit_message: The commit message.

        """
        self._record_call("upload_folder")
        self.uploads.append(UploadCall(repo_id, repo_type, path_in_repo or "", str(folder_path), commit_message))

    def delete_folder(
        self,
        path_in_repo: str,
        *,
        repo_id: str,
        repo_type: str | None = None,
        commit_message: str | None = None,
    ) -> None:
        """Record a folder deletion.

        Args:
            path_in_repo: The folder to delete.
            repo_id: The repository.
            repo_type: The kind of repository.
            commit_message: The commit message.

        """
        self._record_call("delete_folder")
        self.deletions.append(DeleteCall(repo_id, repo_type, path_in_repo, commit_message))

    def list_repo_files(self, repo_id: str, *, repo_type: str | None = None) -> list[str]:
        """List the files in the repository before the publish.

        Args:
            repo_id: The repository.
            repo_type: The kind of repository.

        Returns:
            The file paths.

        """
        self._record_call("list_repo_files")
        self.listings.append(ListCall(repo_id, repo_type))
        return list(self.repo_files)


def cast_hub_api(api: object) -> HfApi:
    """Type the fake client as `HfApi`; it has only the methods the code calls.

    Args:
        api: The fake client.

    Returns:
        The same object.

    """
    return cast("HfApi", api)


COMMIT_URL_TEMPLATE = "https://huggingface.co/{repo_id}/commit/fake"


@dataclass(frozen=True)
class FakeCommit:
    """The part of an upload's commit that the training command reads.

    Attributes:
        commit_url: The commit URL.

    """

    commit_url: str


@dataclass
class FakeHub:
    """Hub module fake that serves downloads from local folders and records each call.

    Attributes:
        snapshot_folders: The folder each repository download returns; other repositories do not exist.
        downloads: The downloads, in order.
        created_repos: Whether each repository that an upload created is private.
        uploads: The uploads, in order.

    """

    snapshot_folders: Mapping[str, Path]
    downloads: list[DownloadCall] = field(default_factory=list[DownloadCall])
    created_repos: dict[str, bool] = field(default_factory=dict[str, bool])
    uploads: list[FolderUploadCall] = field(default_factory=list[FolderUploadCall])

    def snapshot_download(self, repo_id: str, *, repo_type: str = REPO_TYPE_MODEL, **_options: object) -> str:
        """Return a repository's local folder in place of a download.

        Args:
            repo_id: The repository.
            repo_type: The kind of repository; a model by default, as in the Hub client.
            **_options: Other options of the real call, which the fake ignores.

        Returns:
            The repository folder.

        Raises:
            RepositoryNotFoundError: The fake has no folder for the repository.

        """
        folder = self.snapshot_folders.get(repo_id)
        self.downloads.append(DownloadCall(repo_id=repo_id, repo_type=repo_type, folder=folder))
        if folder is None:
            message = f"Repository Not Found for {repo_id}"
            response = httpx2.Response(
                404, request=httpx2.Request("GET", f"https://huggingface.co/api/models/{repo_id}")
            )
            raise RepositoryNotFoundError(message, response=response)
        return str(folder)

    def create_api(self, *, token: str) -> FakeHub:
        """Stand in for the `HfApi` constructor, so API calls reach this fake.

        Args:
            token: The client token, which the fake ignores.

        Returns:
            This fake.

        """
        del token
        return self

    def create_repo(self, repo_id: str, *, private: bool, **_options: object) -> None:
        """Record the repository and its visibility.

        Args:
            repo_id: The repository.
            private: Whether a new repository is private.
            **_options: Other options of the real call, which the fake ignores.

        """
        self.created_repos[repo_id] = private

    def upload_folder(self, *, repo_id: str, folder_path: Path, repo_type: str, commit_message: str) -> FakeCommit:
        """Record the files of a folder upload as the folder holds them now.

        Args:
            repo_id: The repository.
            folder_path: The uploaded folder.
            repo_type: The kind of repository.
            commit_message: The commit message.

        Returns:
            The commit; its URL names the repository.

        """
        files = tuple(sorted(str(path.relative_to(folder_path)) for path in folder_path.rglob("*") if path.is_file()))
        self.uploads.append(
            FolderUploadCall(repo_id=repo_id, repo_type=repo_type, files=files, commit_message=commit_message)
        )
        return FakeCommit(commit_url=COMMIT_URL_TEMPLATE.format(repo_id=repo_id))


def install_fake_hub(monkeypatch: pytest.MonkeyPatch, snapshot_folders: Mapping[str, Path]) -> FakeHub:
    """Replace the Hub client functions with a fake, so no call leaves the process.

    Args:
        monkeypatch: Restores the client after the test.
        snapshot_folders: The folder each repository download returns.

    Returns:
        The fake, for the test to read.

    """
    hub = FakeHub(snapshot_folders=snapshot_folders)
    monkeypatch.setattr(huggingface_hub, "snapshot_download", hub.snapshot_download)
    monkeypatch.setattr(huggingface_hub, "HfApi", hub.create_api)
    return hub

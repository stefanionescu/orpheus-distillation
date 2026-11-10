"""Resolved settings of the dataset command."""

from __future__ import annotations

from typing import TYPE_CHECKING
from dataclasses import dataclass

if TYPE_CHECKING:
    from pathlib import Path


@dataclass(frozen=True)
class DatasetEnvironment:
    """Environment variables of the dataset command, each None when unset or empty.

    Attributes:
        server_url: Value of ORPHEUS_SERVER_URL.
        api_key: Value of ORPHEUS_API_KEY.
        hf_token: Value of HF_TOKEN.

    """

    server_url: str | None
    api_key: str | None
    hf_token: str | None


@dataclass(frozen=True)
class ServerSettings:
    """Orpheus server of a run.

    Attributes:
        url: Server address.
        api_key: Bearer token of each request.

    """

    url: str
    api_key: str


@dataclass(frozen=True)
class GenerationSettings:
    """Resolved settings of one dataset run.

    Attributes:
        server: Orpheus server.
        output_folder: Where the run writes.
        clips_per_shard: Clips per shard.
        concurrency: Requests that run at once.
        resume: Whether to keep the clips of an earlier run.
        max_prompts: Prompt limit, or None for all.

    """

    server: ServerSettings
    output_folder: Path
    clips_per_shard: int
    concurrency: int
    resume: bool
    max_prompts: int | None


@dataclass(frozen=True)
class HubSettings:
    """Hugging Face repository that the dataset command publishes to.

    Attributes:
        token: Hub access token.
        repo: Dataset repository.
        public: Whether a new repository is public.

    """

    token: str
    repo: str
    public: bool

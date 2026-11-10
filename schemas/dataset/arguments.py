"""Parsed flags of the dataset command."""

from __future__ import annotations

from typing import TYPE_CHECKING
from dataclasses import dataclass

if TYPE_CHECKING:
    from pathlib import Path


@dataclass(frozen=True)
class DatasetArguments:
    """Parsed flags of one dataset command, with bounds that argparse already checked.

    Attributes:
        publish_only: Whether to publish the dataset on disk and synthesize nothing.
        server: Orpheus server URL, or None.
        api_key: Orpheus API key, or None.
        prompts_path: Prompt file, or None for the built-in corpus.
        voice: Only voice to synthesize, or None for all.
        max_prompts: Prompt limit, or None for all.
        clips_per_shard: Clips per shard.
        concurrency: Requests that run at once.
        resume: Whether to keep the clips of an earlier run.
        output_folder: Where the run writes.
        publish: Whether to publish after the run.
        dataset_repo: Hugging Face dataset repository.
        public: Whether a new repository is public.
        yes: Whether to delete an earlier output without asking.

    """

    publish_only: bool
    server: str | None
    api_key: str | None
    prompts_path: Path | None
    voice: str | None
    max_prompts: int | None
    clips_per_shard: int
    concurrency: int
    resume: bool
    output_folder: Path
    publish: bool
    dataset_repo: str
    public: bool
    yes: bool

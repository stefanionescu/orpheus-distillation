"""Publish-only mode: publish a dataset that an earlier run wrote."""

from __future__ import annotations

from typing import TYPE_CHECKING
import logging

from huggingface_hub import HfApi

from config.shards import SHARD_GLOB
from src.dataset.stats import read_stats, format_duration
from src.dataset.errors import GenerationError
from src.dataset.settings import build_hub_settings
from src.dataset.hub.publish import publish_dataset
from src.dataset.cli.arguments import EXIT_SUCCESS
from src.dataset.generation.tasks import build_output_folders

if TYPE_CHECKING:
    from schemas.dataset.settings import DatasetEnvironment
    from schemas.dataset.arguments import DatasetArguments

logger = logging.getLogger(__name__)


def run_publish_command(arguments: DatasetArguments, environment: DatasetEnvironment) -> int:
    """Publish the card, shards, and stats file of the dataset in `--output-folder`.

    Args:
        arguments: Parsed flags.
        environment: Variables from `read_environment`.

    Returns:
        Exit code 0.

    Raises:
        GenerationError: The output folder holds no shard.

    """
    hub = build_hub_settings(arguments, environment)
    folders = build_output_folders(arguments.output_folder)
    stats = read_stats(folders.stats_path)
    if not any(folders.shards_folder.glob(SHARD_GLOB)):
        message = f"No shards found in {folders.shards_folder}; generate the dataset first"
        raise GenerationError(message)
    logger.info(
        "Publishing %d clips (%s) of the voices %s to %s",
        stats.clip_count,
        format_duration(stats.total_duration_seconds),
        ", ".join(stats.voices),
        hub.repo,
    )
    publish_dataset(HfApi(token=hub.token), hub, stats, folders)
    logger.info("Published the dataset to %s", hub.repo)
    return EXIT_SUCCESS

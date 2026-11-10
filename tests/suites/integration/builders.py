"""Builders private to the integration suite."""

from __future__ import annotations

from typing import TYPE_CHECKING
from pathlib import PurePosixPath
import tarfile

from config.shards import SHARD_GLOB
from src.dataset.shards import write_shards
from tests.harness.records import write_clip
from src.dataset.generation.tasks import build_output_folders

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Mapping, Sequence

    from schemas.record import Record
    from schemas.dataset.generation import Clip

API_KEY = "orpheus-test-key"
CLIPS_PER_SHARD = 4
"""Clips per shard, below the suite's clip count, so a run writes two shards."""


def write_dataset(output_folder: Path, records: Mapping[str, Record], clips_per_shard: int) -> list[Clip]:
    """Write a WAV file per clip and the shards, laid out like a dataset run's output folder.

    Args:
        output_folder: The run's output folder, which training reads as the dataset.
        records: The records by clip key, in shard order; each duration sets its tone length.
        clips_per_shard: The most clips per shard.

    Returns:
        The clips, in shard order.

    """
    folders = build_output_folders(output_folder)
    clips = [write_clip(folders.audio_folder, key, record) for key, record in records.items()]
    write_shards(clips, folders.shards_folder, clips_per_shard)
    return clips


def write_prompt_file(prompts_path: Path, prompts: Sequence[str]) -> Path:
    """Write a prompt file with one prompt per line.

    Args:
        prompts_path: The prompt file.
        prompts: The prompts, in order.

    Returns:
        The prompt file.

    """
    prompts_path.write_text("\n".join(prompts), encoding="utf-8")
    return prompts_path


def build_run_flags(server_url: str, prompts_path: Path, output_folder: Path) -> list[str]:
    """Build the flags of a dataset run that sends one request at a time.

    Args:
        server_url: The server address.
        prompts_path: The prompt file.
        output_folder: The run's output folder.

    Returns:
        The flags.

    """
    return [
        "--server",
        server_url,
        "--api-key",
        API_KEY,
        "--prompts-file",
        str(prompts_path),
        "--output-folder",
        str(output_folder),
        "--concurrency",
        "1",
        "--clips-per-shard",
        str(CLIPS_PER_SHARD),
    ]


def list_shard_keys(shards_folder: Path) -> list[list[str]]:
    """List each shard's clip keys, in shard name order.

    Args:
        shards_folder: The shards folder.

    Returns:
        Each shard's sorted clip keys.

    """
    keys: list[list[str]] = []
    for shard_path in sorted(shards_folder.glob(SHARD_GLOB)):
        with tarfile.open(shard_path) as archive:
            keys.append(sorted({PurePosixPath(name).stem for name in archive.getnames()}))
    return keys

"""WebDataset writer. Each shard is a TAR file with a WAV member and a JSON record per clip."""

from __future__ import annotations

import io
import json
import math
from typing import TYPE_CHECKING
import tarfile
import dataclasses

from config.shards import (
    SHARD_GLOB,
    AUDIO_EXTENSION,
    SHARD_EXTENSION,
    RECORD_EXTENSION,
    SHARD_INDEX_WIDTH,
    SHARD_NAME_PREFIX,
)

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Sequence

    from schemas.dataset.generation import Clip


def _add_member(archive: tarfile.TarFile, name: str, data: bytes) -> None:
    member = tarfile.TarInfo(name=name)
    member.size = len(data)
    archive.addfile(member, io.BytesIO(data))


def _write_shard(shard_path: Path, clips: Sequence[Clip]) -> None:
    """Write one shard through a temporary file, so a failure leaves no partial shard.

    Args:
        shard_path: Shard file to write.
        clips: Clips in order.

    """
    temporary_path = shard_path.with_name(f"{shard_path.name}.tmp")
    try:
        with tarfile.open(temporary_path, "w") as archive:
            for clip in clips:
                _add_member(archive, f"{clip.key}{AUDIO_EXTENSION}", clip.audio_path.read_bytes())
                _add_member(
                    archive,
                    f"{clip.key}{RECORD_EXTENSION}",
                    json.dumps(dataclasses.asdict(clip.record), ensure_ascii=False).encode("utf-8"),
                )
        temporary_path.replace(shard_path)
    finally:
        temporary_path.unlink(missing_ok=True)


def write_shards(clips: Sequence[Clip], shards_folder: Path, clips_per_shard: int) -> int:
    """Write the clips in order into shards numbered from 0.

    Args:
        clips: Clips in shard order.
        shards_folder: Where the shards go. It must hold no shard yet.
        clips_per_shard: Clip limit per shard.

    Returns:
        The shard count, 0 for no clips.

    Raises:
        ValueError: `clips_per_shard` is below 1.
        FileExistsError: The folder already holds shards.

    """
    if clips_per_shard < 1:
        message = f"clips_per_shard must be at least 1, got {clips_per_shard}"
        raise ValueError(message)
    shards_folder.mkdir(parents=True, exist_ok=True)
    if any(shards_folder.glob(SHARD_GLOB)):
        message = f"The shard folder already holds shards: {shards_folder}"
        raise FileExistsError(message)
    shard_count = math.ceil(len(clips) / clips_per_shard)
    for index in range(shard_count):
        shard_name = f"{SHARD_NAME_PREFIX}{index:0{SHARD_INDEX_WIDTH}d}{SHARD_EXTENSION}"
        start = index * clips_per_shard
        _write_shard(shards_folder / shard_name, clips[start : start + clips_per_shard])
    return shard_count

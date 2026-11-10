"""Reader of the WebDataset shards: one WAV member and one JSON record per clip."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, cast
import logging
from pathlib import PurePosixPath
import tarfile

from config.shards import SHARD_GLOB, SHARDS_FOLDER, AUDIO_EXTENSION, RECORD_EXTENSION
from schemas.record import Record

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Mapping, Iterator

logger = logging.getLogger(__name__)


def _read_text_field(payload: Mapping[str, object], key: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str):
        message = f"The record field {key!r} is missing or is not text"
        raise TypeError(message)
    return value


def _read_number_field(payload: Mapping[str, object], key: str) -> float:
    value = payload.get(key)
    if isinstance(value, bool) or not isinstance(value, int | float):
        message = f"The record field {key!r} is missing or is not a number"
        raise TypeError(message)
    return float(value)


def _group_members(archive: tarfile.TarFile) -> dict[str, dict[str, tarfile.TarInfo]]:
    groups: dict[str, dict[str, tarfile.TarInfo]] = {}
    for member in archive.getmembers():
        name = PurePosixPath(member.name)
        if member.isfile() and not name.name.startswith("."):
            groups.setdefault(name.stem, {})[name.suffix] = member
    return groups


def _read_member(archive: tarfile.TarFile, member: tarfile.TarInfo) -> bytes:
    file = archive.extractfile(member)
    if file is None:
        message = f"The shard member {member.name} is not a file"
        raise ValueError(message)
    with file:
        return file.read()


def _read_clip(archive: tarfile.TarFile, members: Mapping[str, tarfile.TarInfo]) -> tuple[bytes, Record]:
    record_member = members.get(RECORD_EXTENSION)
    audio = members.get(AUDIO_EXTENSION)
    if record_member is None or audio is None:
        message = "The clip has no WAV member or no JSON record"
        raise ValueError(message)
    payload: object = json.loads(_read_member(archive, record_member))
    if not isinstance(payload, dict):
        message = "The record is not a JSON object"
        raise TypeError(message)
    fields = cast("dict[str, object]", payload)
    record = Record(
        text=_read_text_field(fields, "text"),
        speaker=_read_text_field(fields, "speaker"),
        voice=_read_text_field(fields, "voice"),
        duration=_read_number_field(fields, "duration"),
        leading_silence_ms=_read_number_field(fields, "leading_silence_ms"),
    )
    return _read_member(archive, audio), record


def list_shards(dataset_folder: Path) -> list[Path]:
    """List the shards of a downloaded dataset, sorted by name.

    Args:
        dataset_folder: Dataset snapshot, with its shards in the shards folder or at its root.

    Returns:
        The shard files, or an empty list.

    """
    shards_folder = dataset_folder / SHARDS_FOLDER
    search_folder = shards_folder if shards_folder.is_dir() else dataset_folder
    return sorted(search_folder.glob(SHARD_GLOB))


def read_shard_clips(shard_path: Path) -> Iterator[tuple[str, bytes, Record]]:
    """Read the clips of one shard, and log and skip a clip that lacks a member or has a bad record.

    The generator keeps the shard open until it finishes or closes, so a caller that stops early must close it.

    Args:
        shard_path: Shard file.

    Yields:
        Key, WAV bytes, and record of each clip, in shard order.

    """
    with tarfile.open(shard_path) as archive:
        for key, members in _group_members(archive).items():
            try:
                audio, record = _read_clip(archive, members)
            except (ValueError, TypeError) as error:
                logger.warning("Skipping clip %s of shard %s: %s", key, shard_path.name, error)
                continue
            yield key, audio, record

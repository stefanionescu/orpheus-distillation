"""Shards written member by member, including shapes the dataset writer never writes."""

from __future__ import annotations

import io
import json
from typing import TYPE_CHECKING, cast
import tarfile
import dataclasses

import numpy as np
import soundfile

from config.shards import AUDIO_EXTENSION, RECORD_EXTENSION

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Mapping, Callable

    from schemas.record import Record

CLIP_SAMPLE_RATE = 16_000
TONE_FREQUENCY_HZ = 220.0
TONE_AMPLITUDE = 0.25


def encode_record(record: Record) -> bytes:
    """Encode a record as a shard's JSON record member.

    Args:
        record: The clip record.

    Returns:
        UTF-8 JSON keyed by the record field names.

    """
    return json.dumps(dataclasses.asdict(record)).encode("utf-8")


def encode_tone_wav(seconds: float, sample_rate: int) -> bytes:
    """Encode a steady tone as 16-bit mono WAV bytes.

    Args:
        seconds: The tone length.
        sample_rate: The sample rate in hertz.

    Returns:
        The WAV bytes.

    """
    times = np.arange(round(seconds * sample_rate)) / sample_rate
    buffer = io.BytesIO()
    write_audio = cast("Callable[..., None]", soundfile.write)
    write_audio(buffer, TONE_AMPLITUDE * np.sin(2 * np.pi * TONE_FREQUENCY_HZ * times), sample_rate, format="WAV")
    return buffer.getvalue()


def build_clip_members(records: Mapping[str, Record]) -> dict[str, bytes]:
    """Build each clip's WAV and record members, in the dataset writer's order.

    Args:
        records: The records, by clip key.

    Returns:
        The member bytes, by member name.

    """
    members: dict[str, bytes] = {}
    for key, record in records.items():
        members[f"{key}{AUDIO_EXTENSION}"] = encode_tone_wav(record.duration, CLIP_SAMPLE_RATE)
        members[f"{key}{RECORD_EXTENSION}"] = encode_record(record)
    return members


def write_shard(shard_path: Path, members: Mapping[str, bytes]) -> Path:
    """Write a shard with the members in order, and create its folder when missing.

    Args:
        shard_path: The shard file.
        members: The member bytes, by member name.

    Returns:
        The shard file.

    """
    shard_path.parent.mkdir(parents=True, exist_ok=True)
    with tarfile.open(shard_path, "w") as archive:
        for name, data in members.items():
            member = tarfile.TarInfo(name=name)
            member.size = len(data)
            archive.addfile(member, io.BytesIO(data))
    return shard_path

"""Stats file and fingerprint file of a run."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, cast
import dataclasses

from src.dataset.errors import GenerationError
from schemas.dataset.stats import DatasetStats
from schemas.dataset.generation import Fingerprint

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Mapping, Callable, Sequence

    from _typeshed import DataclassInstance

    from schemas.voice import Voice
    from schemas.dataset.generation import Clip


def _decode_count(value: object, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        message = f"Stats field {name} is not a whole number"
        raise TypeError(message)
    return value


def _decode_seconds(value: object, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, int | float):
        message = f"Stats field {name} is not a number"
        raise TypeError(message)
    return float(value)


def _decode_text(value: object, name: str) -> str:
    if not isinstance(value, str):
        message = f"Stats field {name} is not text"
        raise TypeError(message)
    return value


def _decode_voices(value: object, name: str) -> tuple[str, ...]:
    if not isinstance(value, list | tuple):
        message = f"Stats field {name} is not a list"
        raise TypeError(message)
    return tuple(_decode_text(item, name) for item in cast("Sequence[object]", value))


def _decode_per_voice[Value](value: object, name: str, decode: Callable[[object, str], Value]) -> dict[str, Value]:
    if not isinstance(value, dict):
        message = f"Stats field {name} is not an object"
        raise TypeError(message)
    entries = cast("dict[object, object]", value)
    return {_decode_text(key, name): decode(item, name) for key, item in entries.items()}


def _read_text(path: Path) -> str | None:
    """Read a file, or return None when it is absent or unreadable.

    Args:
        path: File to read.

    Returns:
        UTF-8 text, or None.

    """
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None


def _write_text_file(path: Path, text: str) -> None:
    """Write a file through a temporary file, so an interrupted write leaves the old file whole.

    Args:
        path: File to write.
        text: Text to write.

    """
    temporary_path = path.with_name(f"{path.name}.tmp")
    try:
        temporary_path.write_text(text, encoding="utf-8")
        temporary_path.replace(path)
    finally:
        temporary_path.unlink(missing_ok=True)


def _assert_fields_present(payload: Mapping[str, object], record_type: type[DataclassInstance], label: str) -> None:
    """Check that a JSON object holds every field of its record.

    Args:
        payload: JSON object of the file.
        record_type: Record whose field names are the keys.
        label: File kind for the message.

    Raises:
        ValueError: A field is missing. The message names each one.

    """
    missing = [field.name for field in dataclasses.fields(record_type) if field.name not in payload]
    if missing:
        message = f"{label} lacks {', '.join(missing)}"
        raise ValueError(message)


def _read_record_file[Record](path: Path, label: str, decode: Callable[[Mapping[str, object]], Record]) -> Record:
    """Read and decode a JSON file, turning every failure into one error that names the file.

    Args:
        path: File to read.
        label: File kind for the messages.
        decode: Decoder of the JSON object.

    Returns:
        The decoded record.

    Raises:
        GenerationError: The file is missing, is not JSON, is not an object, or lacks a field.

    """
    try:
        payload: object = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        message = f"{label} not found: {path}"
        raise GenerationError(message) from error
    except (OSError, ValueError) as error:
        message = f"{label} is not readable JSON: {path}"
        raise GenerationError(message) from error
    if not isinstance(payload, dict):
        message = f"{label} does not hold a JSON object: {path}"
        raise GenerationError(message)
    try:
        return decode(cast("dict[str, object]", payload))
    except (ValueError, TypeError) as error:
        message = f"{error}: {path}"
        raise GenerationError(message) from error


def build_dataset_stats(
    clips: Sequence[Clip],
    voices: Sequence[Voice],
    shard_count: int,
    prompt_hash: str,
    prompt_count: int,
) -> DatasetStats:
    """Sum the clips of a run per voice.

    Args:
        clips: All clips of the dataset.
        voices: Voices, in synthesis order.
        shard_count: Shard count.
        prompt_hash: Hash of the prompt list.
        prompt_count: Prompt count.

    Returns:
        Run totals.

    """
    names = tuple(voice.name for voice in voices)
    clips_per_voice = dict.fromkeys(names, 0)
    duration_per_voice = dict.fromkeys(names, 0.0)
    for clip in clips:
        clips_per_voice[clip.record.voice] += 1
        duration_per_voice[clip.record.voice] += clip.record.duration
    return DatasetStats(
        clip_count=len(clips),
        total_duration_seconds=sum(clip.record.duration for clip in clips),
        voices=names,
        clips_per_voice=clips_per_voice,
        duration_per_voice=duration_per_voice,
        shard_count=shard_count,
        prompt_hash=prompt_hash,
        prompt_count=prompt_count,
    )


def encode_stats(stats: DatasetStats) -> dict[str, object]:
    """Encode the stats as the JSON object of the stats file.

    Args:
        stats: Run totals.

    Returns:
        The stats fields plus a readable `total_duration_formatted`.

    """
    payload: dict[str, object] = dataclasses.asdict(stats)
    payload["total_duration_formatted"] = format_duration(stats.total_duration_seconds)
    return payload


def decode_stats(payload: Mapping[str, object]) -> DatasetStats:
    """Decode the JSON object of a stats file. Every field is required.

    A missing field raises `ValueError` and a wrong type raises `TypeError`, each naming the field.

    Args:
        payload: Object from the stats file.

    Returns:
        Run totals.

    """
    _assert_fields_present(payload, DatasetStats, "Stats file")
    return DatasetStats(
        clip_count=_decode_count(payload["clip_count"], "clip_count"),
        total_duration_seconds=_decode_seconds(payload["total_duration_seconds"], "total_duration_seconds"),
        voices=_decode_voices(payload["voices"], "voices"),
        clips_per_voice=_decode_per_voice(payload["clips_per_voice"], "clips_per_voice", _decode_count),
        duration_per_voice=_decode_per_voice(payload["duration_per_voice"], "duration_per_voice", _decode_seconds),
        shard_count=_decode_count(payload["shard_count"], "shard_count"),
        prompt_hash=_decode_text(payload["prompt_hash"], "prompt_hash"),
        prompt_count=_decode_count(payload["prompt_count"], "prompt_count"),
    )


def read_stats(path: Path) -> DatasetStats:
    """Read the stats file of a finished run. A missing or bad file raises `GenerationError`.

    Args:
        path: File to read.

    Returns:
        Run totals.

    """
    return _read_record_file(path, "Stats file", decode_stats)


def write_stats(path: Path, stats: DatasetStats) -> bool:
    """Write the stats file unless it already holds the same text.

    Args:
        path: File to write.
        stats: Run totals.

    Returns:
        True when it wrote the file, False when the text matched.

    """
    text = json.dumps(encode_stats(stats), indent=2)
    if _read_text(path) == text:
        return False
    _write_text_file(path, text)
    return True


def decode_fingerprint(payload: Mapping[str, object]) -> Fingerprint:
    """Decode the JSON object of a fingerprint file. Every field is required.

    A missing field raises `ValueError` and a wrong type raises `TypeError`, each naming the field.

    Args:
        payload: Object from the fingerprint file.

    Returns:
        Fingerprint of the run that wrote the file.

    """
    _assert_fields_present(payload, Fingerprint, "Fingerprint file")
    return Fingerprint(
        prompt_hash=_decode_text(payload["prompt_hash"], "prompt_hash"),
        prompt_count=_decode_count(payload["prompt_count"], "prompt_count"),
        voices=_decode_voices(payload["voices"], "voices"),
    )


def read_fingerprint(path: Path) -> Fingerprint:
    """Read the fingerprint file. A missing or bad file raises `GenerationError`.

    Args:
        path: File to read.

    Returns:
        Fingerprint of the run that wrote the file.

    """
    return _read_record_file(path, "Fingerprint file", decode_fingerprint)


def write_fingerprint(path: Path, fingerprint: Fingerprint) -> None:
    """Write the fingerprint through a temporary file, so a stop at any point leaves it whole.

    Args:
        path: File to write.
        fingerprint: Fingerprint of the run.

    """
    _write_text_file(path, json.dumps(dataclasses.asdict(fingerprint), indent=2))


def format_duration(seconds: float) -> str:
    """Format seconds as HH:MM:SS.

    Args:
        seconds: Duration. The function drops the fraction.

    Returns:
        Hours, minutes, and seconds, each with at least two digits.

    """
    minutes, whole_seconds = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02d}:{minutes:02d}:{whole_seconds:02d}"

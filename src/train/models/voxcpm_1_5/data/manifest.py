"""The manifests and the tokenizer copy that the prepare command writes."""

from __future__ import annotations

import json
import shutil
from typing import TYPE_CHECKING
import logging

import numpy as np

from config.shards import AUDIO_EXTENSION
from src.train.shards import list_shards, read_shard_clips
from src.train.voices import get_voice_for_speaker
from config.models.voxcpm_1_5.data import (
    TEXT_KEY,
    AUDIO_KEY,
    VOICE_KEY,
    SPLIT_SEED,
    DURATION_KEY,
    TOKENIZER_FILES,
    VAL_MANIFEST_FILE,
    TRAIN_MANIFEST_FILE,
    MAX_DURATION_SECONDS,
    MIN_DURATION_SECONDS,
    MANIFEST_AUDIO_FOLDER,
)
from schemas.models.voxcpm_1_5.manifest import ManifestEntry, ManifestFiles, ManifestStats

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Sequence

    from schemas.record import Record

SECONDS_PER_HOUR = 3600

logger = logging.getLogger(__name__)


class ManifestError(Exception):
    """The shards hold no usable clip, or a manifest line is malformed."""


def _select_voice(record: Record) -> str | None:
    voice = get_voice_for_speaker(record.speaker)
    if voice is None or not record.text.strip():
        return None
    if not MIN_DURATION_SECONDS <= record.duration <= MAX_DURATION_SECONDS:
        return None
    return voice.name


def _extract_clips(shard_paths: Sequence[Path], audio_folder: Path) -> list[ManifestEntry]:
    entries: list[ManifestEntry] = []
    for shard_path in shard_paths:
        logger.info("Reading shard %s", shard_path.name)
        shard_audio_folder = audio_folder / shard_path.stem
        shard_audio_folder.mkdir(parents=True, exist_ok=True)
        for key, audio, record in read_shard_clips(shard_path):
            voice = _select_voice(record)
            if voice is not None:
                audio_path = shard_audio_folder / f"{key}{AUDIO_EXTENSION}"
                audio_path.write_bytes(audio)
                entry = ManifestEntry(
                    audio=str(audio_path.absolute()), text=record.text.strip(), duration=record.duration, voice=voice
                )
                entries.append(entry)
    return entries


def _write_val_manifest(entries: Sequence[ManifestEntry], manifest_path: Path) -> Path | None:
    if not entries:
        manifest_path.unlink(missing_ok=True)
        return None
    write_manifest(entries, manifest_path)
    return manifest_path


def _decode_entry(line: str) -> ManifestEntry:
    try:
        payload = json.loads(line)
        return ManifestEntry(
            audio=str(payload[AUDIO_KEY]),
            text=str(payload[TEXT_KEY]),
            duration=float(payload[DURATION_KEY]),
            voice=str(payload[VOICE_KEY]),
        )
    except (ValueError, KeyError, TypeError) as error:
        message = (
            f"The line is not a JSON object with the keys {AUDIO_KEY}, {TEXT_KEY}, {DURATION_KEY}, and {VOICE_KEY}"
        )
        raise ManifestError(message) from error


def split_entries(
    entries: Sequence[ManifestEntry], val_split: float, seed: int
) -> tuple[list[ManifestEntry], list[ManifestEntry]]:
    """Split the entries into training and validation shares in a seeded shuffle.

    Args:
        entries: Kept entries.
        val_split: Share for validation; 0 keeps every entry for training, in order.
        seed: Shuffle seed, so two runs over the same shards split the same way.

    Returns:
        The training entries and the validation entries.

    """
    if val_split <= 0:
        return list(entries), []
    order = [int(index) for index in np.random.default_rng(seed).permutation(len(entries))]
    shuffled = [entries[index] for index in order]
    split_index = int(len(shuffled) * (1 - val_split))
    return shuffled[:split_index], shuffled[split_index:]


def build_manifest_stats(entries: Sequence[ManifestEntry]) -> ManifestStats:
    """Count the entries and their hours, overall and per voice.

    Args:
        entries: Kept entries.

    Returns:
        The totals.

    """
    clips_per_voice: dict[str, int] = {}
    seconds_per_voice: dict[str, float] = {}
    for entry in entries:
        clips_per_voice[entry.voice] = clips_per_voice.get(entry.voice, 0) + 1
        seconds_per_voice[entry.voice] = seconds_per_voice.get(entry.voice, 0.0) + entry.duration
    return ManifestStats(
        clip_count=len(entries),
        hours=sum(seconds_per_voice.values()) / SECONDS_PER_HOUR,
        clips_per_voice=clips_per_voice,
        hours_per_voice={voice: seconds / SECONDS_PER_HOUR for voice, seconds in seconds_per_voice.items()},
    )


def print_manifest_stats(stats: ManifestStats) -> None:
    """Log the totals: one line overall and one per voice.

    Args:
        stats: The totals.

    """
    logger.info("Manifests hold %d clips, %.2f hours", stats.clip_count, stats.hours)
    for voice, clips in sorted(stats.clips_per_voice.items()):
        logger.info("Voice %s: %d clips, %.2f hours", voice, clips, stats.hours_per_voice[voice])


def write_manifest(entries: Sequence[ManifestEntry], manifest_path: Path) -> None:
    """Write entries as JSON lines through a temporary file, so a failure leaves no partial file.

    Args:
        entries: Entries to write.
        manifest_path: Manifest file; the call creates its folder when missing.

    """
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = manifest_path.with_name(f"{manifest_path.name}.tmp")
    lines = [
        json.dumps(
            {
                AUDIO_KEY: entry.audio,
                TEXT_KEY: entry.text,
                DURATION_KEY: entry.duration,
                VOICE_KEY: entry.voice,
            },
            ensure_ascii=False,
        )
        for entry in entries
    ]
    try:
        temporary_path.write_text("".join(f"{line}\n" for line in lines), encoding="utf-8")
        temporary_path.replace(manifest_path)
    finally:
        temporary_path.unlink(missing_ok=True)
    logger.info("Wrote %d entries to %s", len(entries), manifest_path)


def write_manifests(dataset_folder: Path, manifests_folder: Path, val_split: float) -> ManifestFiles:
    """Write the training and validation manifests of the clips that training keeps.

    Training keeps a clip whose speaker has a voice in the table, whose text is not empty, and whose length is within
    the duration bounds. The WAV files of the kept clips go to the audio folder of the manifests folder.

    Args:
        dataset_folder: Downloaded dataset snapshot.
        manifests_folder: Where the manifests go.
        val_split: Share of kept clips for validation.

    Returns:
        The manifest files and the totals of the kept clips.

    Raises:
        ManifestError: The dataset holds no shard, no clip passes the filters, or the split leaves no training clip.

    """
    shard_paths = list_shards(dataset_folder)
    if not shard_paths:
        message = f"The dataset folder {dataset_folder} holds no shard"
        raise ManifestError(message)
    entries = _extract_clips(shard_paths, manifests_folder / MANIFEST_AUDIO_FOLDER)
    train_entries, val_entries = split_entries(entries, val_split, SPLIT_SEED)
    if not train_entries:
        message = f"No clip of the {len(shard_paths)} shards in {dataset_folder} is left for training"
        raise ManifestError(message)
    train_manifest_path = manifests_folder / TRAIN_MANIFEST_FILE
    write_manifest(train_entries, train_manifest_path)
    val_manifest_path = _write_val_manifest(val_entries, manifests_folder / VAL_MANIFEST_FILE)
    return ManifestFiles(train_manifest_path, val_manifest_path, build_manifest_stats(entries))


def read_voice_entries(manifest_path: Path, voice: str) -> list[ManifestEntry]:
    """Read the entries of one voice from a manifest.

    Args:
        manifest_path: Manifest file.
        voice: Voice to keep.

    Returns:
        Entries of the voice in file order, or an empty list.

    Raises:
        ManifestError: A line is not a JSON object with the four manifest keys.

    """
    entries: list[ManifestEntry] = []
    for line_number, line in enumerate(manifest_path.read_text(encoding="utf-8").splitlines(), start=1):
        try:
            entry = _decode_entry(line)
        except ManifestError as error:
            message = f"{manifest_path}:{line_number}: {error}"
            raise ManifestError(message) from error
        if entry.voice == voice:
            entries.append(entry)
    return entries


def copy_tokenizer_files(source_folder: Path, target_folder: Path) -> None:
    """Copy the tokenizer files into a folder, creating it when missing.

    Args:
        source_folder: Folder with every tokenizer file, such as the base model.
        target_folder: Where the files go.

    """
    target_folder.mkdir(parents=True, exist_ok=True)
    for filename in TOKENIZER_FILES:
        shutil.copy2(source_folder / filename, target_folder / filename)

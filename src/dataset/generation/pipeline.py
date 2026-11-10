"""One dataset run, from the prompt list to the shards and stats file."""

from __future__ import annotations

from typing import TYPE_CHECKING
import logging

from src.dataset.stats import write_stats, format_duration, write_fingerprint, build_dataset_stats
from src.dataset.shards import write_shards
from src.dataset.generation.pool import run_worker_pool
from src.dataset.generation.clips import build_clip, read_existing_clips
from src.dataset.generation.tasks import build_tasks, build_output_folders, prepare_output_folders
from src.dataset.generation.resume import (
    build_fingerprint,
    list_existing_clips,
    read_existing_fingerprint,
    assert_fingerprint_matches,
)
from src.dataset.generation.progress import build_progress_bar
from src.dataset.generation.preflight import run_preflight_check

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Sequence

    from schemas.voice import Voice
    from schemas.record import Record
    from schemas.dataset.stats import DatasetStats
    from src.dataset.tts.client import TtsClient
    from schemas.dataset.settings import GenerationSettings
    from schemas.dataset.generation import Clip, Fingerprint, OutputFolders, GenerationTask

logger = logging.getLogger(__name__)


def _resume_existing_run(
    folders: OutputFolders, fingerprint: Fingerprint, voices: Sequence[Voice]
) -> set[tuple[int, str]]:
    """Check that the earlier run matches, then list its clips.

    Args:
        folders: Run paths.
        fingerprint: Fingerprint of this run.
        voices: Voices, in order.

    Returns:
        Prompt index and speaker of each existing clip, empty without an earlier run.

    """
    existing = read_existing_fingerprint(folders)
    if existing is None:
        logger.warning("No earlier run to resume in %s; the run starts from the first clip", folders.root)
        return set()
    assert_fingerprint_matches(existing, fingerprint)
    return list_existing_clips(folders.audio_folder, voices)


async def _synthesize_clips(
    client: TtsClient,
    pending: Sequence[GenerationTask],
    concurrency: int,
) -> list[tuple[GenerationTask, Record]]:
    if not pending:
        logger.info("Every clip exists already; nothing to synthesize")
        return []
    first = await run_preflight_check(client, pending[0])
    progress = build_progress_bar(len(pending), first.duration)
    try:
        results = await run_worker_pool(
            client,
            pending[1:],
            concurrency,
            progress,
            audio_seconds=first.duration,
        )
    finally:
        progress.close()
    return [(pending[0], first), *results]


def print_generation_summary(stats: DatasetStats, output_folder: Path) -> None:
    """Log the totals of a finished run, one line per voice.

    Args:
        stats: Run totals.
        output_folder: Where the run wrote.

    """
    logger.info(
        "Generation complete: %d clips, %s of audio, %d shards",
        stats.clip_count,
        format_duration(stats.total_duration_seconds),
        stats.shard_count,
    )
    for voice in stats.voices:
        logger.info(
            "%s: %d clips, %s",
            voice,
            stats.clips_per_voice[voice],
            format_duration(stats.duration_per_voice[voice]),
        )
    logger.info("Output folder: %s", output_folder)


async def generate_dataset(
    client: TtsClient,
    prompts: Sequence[str],
    voices: Sequence[Voice],
    settings: GenerationSettings,
) -> DatasetStats:
    """Synthesize every prompt with every voice, then write the shards and the stats file.

    The run writes its fingerprint before the first clip, so `--resume` works after a stop. The fingerprint covers
    the prompts after the `--max-prompts` cut, so a resume with another limit fails.

    Args:
        client: Orpheus client.
        prompts: Prompts, in order.
        voices: Voices, in order.
        settings: Run settings.

    Returns:
        Run totals, as the stats file holds them.

    """
    selected = prompts[: settings.max_prompts]
    fingerprint = build_fingerprint(selected, voices)
    folders = build_output_folders(settings.output_folder)
    existing = _resume_existing_run(folders, fingerprint, voices) if settings.resume else set[tuple[int, str]]()
    prepare_output_folders(folders, resume=settings.resume)
    write_fingerprint(folders.fingerprint_path, fingerprint)
    tasks, pending = build_tasks(selected, voices, folders.audio_folder, existing)
    logger.info(
        "Planned %d clips from %d prompts and %d voices: %d existing, %d to synthesize",
        len(tasks),
        len(selected),
        len(voices),
        len(tasks) - len(pending),
        len(pending),
    )
    results = await _synthesize_clips(client, pending, settings.concurrency)
    clips: list[Clip] = [build_clip(task, record) for task, record in results]
    clips.extend(read_existing_clips(tasks, existing))
    clips.sort(key=lambda clip: clip.key)
    shard_count = write_shards(clips, folders.shards_folder, settings.clips_per_shard)
    stats = build_dataset_stats(clips, voices, shard_count, fingerprint.prompt_hash, fingerprint.prompt_count)
    write_stats(folders.stats_path, stats)
    print_generation_summary(stats, folders.root)
    return stats

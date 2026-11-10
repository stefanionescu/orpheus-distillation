"""Output folders of a run and its prompt and voice pairs."""

from __future__ import annotations

import shutil
from typing import TYPE_CHECKING
import logging

from config.shards import SHARDS_FOLDER, AUDIO_EXTENSION
from config.dataset.paths import (
    KEY_WIDTH,
    KEY_PREFIX,
    STATS_FILE,
    AUDIO_FOLDER,
    FINGERPRINT_FILE,
    AUDIO_FILE_TEMPLATE,
)
from schemas.dataset.generation import OutputFolders, GenerationTask

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Set as AbstractSet
    from collections.abc import Sequence

    from schemas.voice import Voice

logger = logging.getLogger(__name__)


def build_output_folders(output_folder: Path) -> OutputFolders:
    """Build the paths that a run writes under its output folder.

    Args:
        output_folder: Where the run writes.

    Returns:
        The paths. The function neither creates nor checks them.

    """
    return OutputFolders(
        root=output_folder,
        audio_folder=output_folder / AUDIO_FOLDER,
        shards_folder=output_folder / SHARDS_FOLDER,
        stats_path=output_folder / STATS_FILE,
        fingerprint_path=output_folder / FINGERPRINT_FILE,
    )


def prepare_output_folders(folders: OutputFolders, *, resume: bool) -> None:
    """Clean the output of an earlier run and create the audio and shard folders.

    A fresh run deletes the whole output folder. A resumed run deletes only the shards, which it rewrites from every
    clip.

    Args:
        folders: Run paths.
        resume: Whether to keep the clips of an earlier run.

    """
    if not resume and folders.root.exists():
        logger.info("Deleting the output of the earlier run in %s", folders.root)
        shutil.rmtree(folders.root)
    if resume and folders.shards_folder.exists():
        shutil.rmtree(folders.shards_folder)
    folders.audio_folder.mkdir(parents=True, exist_ok=True)
    folders.shards_folder.mkdir(parents=True, exist_ok=True)


def build_tasks(
    prompts: Sequence[str],
    voices: Sequence[Voice],
    audio_folder: Path,
    existing_clips: AbstractSet[tuple[int, str]],
) -> tuple[list[GenerationTask], list[GenerationTask]]:
    """Pair every prompt with every voice and find the pairs that still need a clip.

    The clip number is `prompt_index * len(voices) + voice_index`, so the same prompts and voices give the same file
    names in every run. `list_existing_clips` inverts this formula.

    Args:
        prompts: Prompts, in order.
        voices: Voices, in order.
        audio_folder: Folder of the WAV files.
        existing_clips: Prompt index and speaker of each existing clip.

    Returns:
        Every task in clip order, and the tasks that still need a clip.

    """
    tasks: list[GenerationTask] = []
    for prompt_index, prompt in enumerate(prompts):
        for voice_index, voice in enumerate(voices):
            key = f"{KEY_PREFIX}{prompt_index * len(voices) + voice_index:0{KEY_WIDTH}d}"
            file_name = AUDIO_FILE_TEMPLATE.format(key=key, speaker=voice.speaker, extension=AUDIO_EXTENSION)
            task = GenerationTask(
                key=key,
                prompt_index=prompt_index,
                prompt=prompt,
                voice=voice,
                audio_path=audio_folder / file_name,
            )
            tasks.append(task)
    pending = [task for task in tasks if (task.prompt_index, task.voice.speaker) not in existing_clips]
    return tasks, pending

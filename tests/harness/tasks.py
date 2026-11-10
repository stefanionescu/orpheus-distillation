"""Generation tasks built the way a run builds them."""

from __future__ import annotations

from typing import TYPE_CHECKING

from tests.harness.voices import TABLE_VOICES
from src.dataset.generation.tasks import build_tasks

if TYPE_CHECKING:
    from pathlib import Path

    from schemas.dataset.generation import GenerationTask


def build_prompt_list(prompt_count: int) -> list[str]:
    """Build distinct prompts that the parser keeps unchanged.

    Args:
        prompt_count: How many prompts.

    Returns:
        The prompts.

    """
    return [f"Prompt number {index}." for index in range(prompt_count)]


def build_generation_tasks(audio_folder: Path, prompt_count: int) -> list[GenerationTask]:
    """Build every task of a run over the table voices.

    Args:
        audio_folder: Where the WAV files go.
        prompt_count: How many prompts.

    Returns:
        One task per prompt and voice, in clip order.

    """
    tasks, _ = build_tasks(build_prompt_list(prompt_count), TABLE_VOICES, audio_folder, set())
    return tasks

"""Preflight clip. The first task runs alone, so a wrong server or key stops the run before the pool starts."""

from __future__ import annotations

from typing import TYPE_CHECKING
import logging

from src.dataset.errors import TtsError, GenerationError

if TYPE_CHECKING:
    from schemas.record import Record
    from src.dataset.tts.client import TtsClient
    from schemas.dataset.generation import GenerationTask

logger = logging.getLogger(__name__)


async def run_preflight_check(client: TtsClient, task: GenerationTask) -> Record:
    """Synthesize the first clip of the run on its own.

    Args:
        client: Orpheus client.
        task: First pending task.

    Returns:
        Clip record. It counts as the first finished task.

    Raises:
        GenerationError: The server failed the clip.

    """
    logger.info("Preflight: synthesizing %s to check the server", task.key)
    try:
        record = await client.synthesize_clip(task.prompt, task.voice, task.audio_path)
    except TtsError as error:
        message = f"Preflight check failed: {error}"
        raise GenerationError(message) from error
    logger.info("Preflight succeeded: generated %.1f s of audio", record.duration)
    return record

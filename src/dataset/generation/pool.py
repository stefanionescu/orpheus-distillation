"""Worker pool that synthesizes tasks concurrently and stops at the first failure."""

from __future__ import annotations

from typing import TYPE_CHECKING
import asyncio
from dataclasses import dataclass

from src.dataset.errors import TtsError, GenerationError
from src.dataset.prompts import format_prompt_preview
from src.dataset.generation.progress import set_progress_duration

if TYPE_CHECKING:
    from typing import NoReturn
    from collections.abc import Sequence

    from tqdm import tqdm

    from schemas.record import Record
    from src.dataset.tts.client import TtsClient
    from schemas.dataset.generation import GenerationTask


@dataclass
class PoolState:
    """State the workers share. They all run on the event loop thread, so they need no lock.

    Attributes:
        results: Finished tasks and their records, in finishing order.
        failure: The first failed task and its error, or None.
        audio_seconds: Audio synthesized so far, preflight clip included.

    """

    results: list[tuple[GenerationTask, Record]]
    failure: tuple[GenerationTask, TtsError] | None
    audio_seconds: float


async def run_worker(
    client: TtsClient,
    queue: asyncio.Queue[GenerationTask],
    state: PoolState,
    progress: tqdm[NoReturn],
) -> None:
    """Synthesize queued tasks until the pool cancels the worker or a task fails.

    The client already retries connections, so the worker does not retry. On a failure it returns without
    `task_done`, so the queue never joins and the pool sees the worker finish first.

    Args:
        client: Orpheus client.
        queue: Tasks that wait for a worker.
        state: Shared results and failure.
        progress: Progress bar.

    """
    while True:
        task = await queue.get()
        try:
            record = await client.synthesize_clip(task.prompt, task.voice, task.audio_path)
        except TtsError as error:
            state.failure = (task, error)
            return
        state.results.append((task, record))
        state.audio_seconds += record.duration
        progress.update(1)
        set_progress_duration(progress, state.audio_seconds)
        queue.task_done()


async def run_worker_pool(
    client: TtsClient,
    tasks: Sequence[GenerationTask],
    concurrency: int,
    progress: tqdm[NoReturn],
    *,
    audio_seconds: float,
) -> list[tuple[GenerationTask, Record]]:
    """Synthesize every task with at most `concurrency` requests at once.

    The pool waits until the queue joins or a worker fails, then cancels and awaits the rest, so no task outlives
    the call. An error other than `TtsError` propagates.

    Args:
        client: Orpheus client.
        tasks: Tasks to synthesize.
        concurrency: Request limit.
        progress: Progress bar.
        audio_seconds: Audio synthesized before the pool started.

    Returns:
        Tasks and their records, in finishing order.

    Raises:
        GenerationError: A task failed. The message names its clip, voice, and prompt.

    """
    state = PoolState(results=[], failure=None, audio_seconds=audio_seconds)
    queue: asyncio.Queue[GenerationTask] = asyncio.Queue()
    for task in tasks:
        queue.put_nowait(task)
    workers = [
        asyncio.create_task(run_worker(client, queue, state, progress)) for _ in range(min(concurrency, len(tasks)))
    ]
    pending = [asyncio.create_task(queue.join()), *workers]
    try:
        finished, _ = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
        for done in finished:
            done.result()
    finally:
        for waiting in pending:
            waiting.cancel()
        await asyncio.gather(*pending, return_exceptions=True)
    if state.failure is not None:
        task, error = state.failure
        preview = format_prompt_preview(task.prompt)
        message = f"Synthesis of {task.key} ({task.voice.name}) failed: {error}; prompt: {preview}"
        raise GenerationError(message)
    return state.results

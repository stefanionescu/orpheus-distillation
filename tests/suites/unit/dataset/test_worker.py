"""The worker pool runs each task once within its limit, stops at a failure or signal, and leaves no task running."""

from __future__ import annotations

import signal
from typing import TYPE_CHECKING
import asyncio

import pytest

from tests.harness.tts import FakeTtsClient, CountingTtsClient, SignalingTtsClient
from src.dataset.errors import GenerationError
from tests.harness.tasks import build_generation_tasks
from src.dataset.cli.main import main
from tests.harness.voices import TABLE_VOICES
from src.dataset.cli.arguments import EXIT_SUCCESS, EXIT_SIGNAL_BASE
from tests.suites.unit.builders import (
    build_run_flags,
    install_fake_client,
)
from src.dataset.generation.pool import run_worker_pool
from src.dataset.generation.tasks import build_output_folders
from src.dataset.generation.progress import build_progress_bar

if TYPE_CHECKING:
    from pathlib import Path

    from schemas.record import Record
    from schemas.dataset.generation import GenerationTask

PROMPT_COUNT = 4
CONCURRENCY = 2


async def _run_pool(client: FakeTtsClient, tasks: list[GenerationTask]) -> list[tuple[GenerationTask, Record]]:
    progress = build_progress_bar(len(tasks) + 1, 0.0)
    try:
        return await run_worker_pool(client, tasks, CONCURRENCY, progress, audio_seconds=0.0)
    finally:
        progress.close()


def test_pool_finishes_every_task(tmp_path: Path) -> None:
    """Without failures, each task gives one result and one request.

    Args:
        tmp_path: The test folder.

    """
    tasks = build_generation_tasks(tmp_path, PROMPT_COUNT)
    client = FakeTtsClient()

    results = asyncio.run(_run_pool(client, tasks))

    assert sorted(task.key for task, _ in results) == [task.key for task in tasks]
    assert sorted(client.calls) == [task.audio_path for task in tasks]


def test_pool_limits_requests(tmp_path: Path) -> None:
    """The pool never runs more requests at once than its limit, and with more tasks than the limit it reaches it.

    Args:
        tmp_path: The test folder.

    """
    tasks = build_generation_tasks(tmp_path, PROMPT_COUNT)
    client = CountingTtsClient()

    asyncio.run(_run_pool(client, tasks))

    assert client.peak_in_flight == CONCURRENCY


def test_failure_stops_pool(tmp_path: Path) -> None:
    """A failed task stops the pool early, runs only once, and the error names it.

    Args:
        tmp_path: The test folder.

    """
    tasks = build_generation_tasks(tmp_path, PROMPT_COUNT)
    failing = tasks[1]
    client = FakeTtsClient(failing_paths=frozenset({failing.audio_path}))

    with pytest.raises(GenerationError, match=failing.key) as caught:
        asyncio.run(_run_pool(client, tasks))

    assert failing.voice.name in str(caught.value)
    assert client.calls.count(failing.audio_path) == 1
    assert len(client.calls) < len(tasks)


def test_pool_leaves_no_tasks(tmp_path: Path) -> None:
    """After a failure, no worker task is left on the event loop.

    Args:
        tmp_path: The test folder.

    """
    tasks = build_generation_tasks(tmp_path, PROMPT_COUNT)
    client = FakeTtsClient(failing_paths=frozenset({tasks[0].audio_path}))

    async def list_leftover_tasks() -> set[asyncio.Task[object]]:
        with pytest.raises(GenerationError):
            await _run_pool(client, tasks)
        return asyncio.all_tasks() - {asyncio.current_task()}

    assert asyncio.run(list_leftover_tasks()) == set()


def test_sigterm_stops_run(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """SIGTERM exits with 128 plus the signal, restores the earlier handler, and leaves a run that --resume finishes.

    Args:
        tmp_path: The test folder.
        monkeypatch: Replaces the Orpheus client.

    """
    install_fake_client(monkeypatch, SignalingTtsClient())
    output_folder = tmp_path / "output"
    flags = build_run_flags(tmp_path, output_folder, prompt_count=PROMPT_COUNT)
    # When the command ignores SIGTERM, the default action kills pytest; a KeyboardInterrupt fails the test instead.
    pytest_sigterm = signal.signal(signal.SIGTERM, signal.default_int_handler)
    try:
        exit_code = main(flags)
        restored_action = signal.getsignal(signal.SIGTERM)
    finally:
        signal.signal(signal.SIGTERM, pytest_sigterm)
    folders = build_output_folders(output_folder)
    written = len(list(folders.audio_folder.glob("*.wav")))
    resumed = install_fake_client(monkeypatch)

    assert exit_code == EXIT_SIGNAL_BASE + signal.SIGTERM
    assert restored_action is signal.default_int_handler
    assert not folders.stats_path.exists()
    assert main([*flags, "--resume"]) == EXIT_SUCCESS
    assert len(resumed.calls) == PROMPT_COUNT * len(TABLE_VOICES) - written

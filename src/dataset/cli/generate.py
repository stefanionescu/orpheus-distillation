"""Generate mode: synthesize the dataset, then publish it with `--publish`."""

from __future__ import annotations

import sys
import signal
from typing import TYPE_CHECKING
import asyncio
import logging

from huggingface_hub import HfApi

from config.voices import VOICES
from src.dataset.errors import UsageError
from src.dataset.prompts import read_prompts, list_corpus_prompts
from src.dataset.settings import build_hub_settings, build_server_settings
from src.dataset.tts.client import OrpheusClient
from src.dataset.hub.publish import PublishError, publish_dataset
from schemas.dataset.settings import GenerationSettings
from src.dataset.cli.arguments import EXIT_FAILURE, EXIT_SUCCESS
from src.dataset.generation.tasks import build_output_folders
from src.dataset.generation.pipeline import generate_dataset

if TYPE_CHECKING:
    from types import FrameType
    from pathlib import Path
    from collections.abc import Coroutine

    from schemas.dataset.stats import DatasetStats
    from schemas.dataset.settings import HubSettings, DatasetEnvironment
    from schemas.dataset.arguments import DatasetArguments

logger = logging.getLogger(__name__)

STOP_SIGNALS = (signal.SIGINT, signal.SIGTERM)


class StoppedError(Exception):
    """A stop signal cancelled the run. A run with `--resume` finishes it from the clips on disk.

    Attributes:
        stop_signal: Signal that stopped the run.

    """

    stop_signal: int

    def __init__(self, stop_signal: int) -> None:
        """Store the signal that stopped the run.

        Args:
            stop_signal: Signal number.

        """
        super().__init__(f"Stopped by {signal.Signals(stop_signal).name}; rerun with --resume")
        self.stop_signal = stop_signal


async def _run_until_stopped(work: Coroutine[object, object, DatasetStats]) -> DatasetStats:
    """Await the dataset run and cancel it on SIGINT or SIGTERM.

    The handlers replace the SIGINT handler of `asyncio.run`, so both signals stop the run the same way. A signal
    during the synchronous end of the run cannot cancel it, so the run writes its shards and stats, then counts as
    stopped and skips the publish.

    Args:
        work: The dataset run.

    Returns:
        Run totals.

    Raises:
        StoppedError: A stop signal cancelled the run, or arrived after its last await.
        asyncio.CancelledError: Something other than a stop signal cancelled the run.

    """
    loop = asyncio.get_running_loop()
    task = asyncio.create_task(work)
    received: list[int] = []

    def stop(signal_number: int, _frame: FrameType | None) -> None:
        """Record the signal and cancel the run.

        A loop signal handler runs only when the loop regains control, too late for a signal during synchronous code.
        This handler runs at once, so it records the signal and leaves the cancellation to the loop.

        Args:
            signal_number: Signal that arrived.
            _frame: Interrupted frame, unused.

        """
        received.append(signal_number)
        loop.call_soon_threadsafe(task.cancel)

    earlier_actions = {number: signal.signal(number, stop) for number in STOP_SIGNALS}
    try:
        stats = await task
    except asyncio.CancelledError as cancellation:
        if not received:
            raise
        raise StoppedError(received[0]) from cancellation
    finally:
        for number, action in earlier_actions.items():
            signal.signal(number, action)
    if received:
        raise StoppedError(received[0])
    return stats


def _assert_clean_allowed(arguments: DatasetArguments) -> None:
    """Refuse to delete a non-empty output folder unless the user agrees.

    Without `--resume`, the run deletes the output folder. On a terminal the command asks first; otherwise it needs
    `--yes`.

    Args:
        arguments: Parsed flags.

    Raises:
        UsageError: The folder holds an earlier output and the user did not agree.

    """
    output_folder = arguments.output_folder
    if arguments.resume or arguments.yes or not output_folder.is_dir() or not any(output_folder.iterdir()):
        return
    if sys.stdin.isatty():
        sys.stderr.write(f"Delete everything in {output_folder} and start a new run? [y/N] ")
        sys.stderr.flush()
        if sys.stdin.readline().strip().lower() in {"y", "yes"}:
            return
    message = f"{output_folder} holds an earlier run: pass --resume to keep it or --yes to delete it"
    raise UsageError(message)


def publish_after_run(hub: HubSettings, stats: DatasetStats, output_folder: Path) -> int:
    """Publish the dataset that the run just wrote. A failed publish leaves it on disk for `--publish-only`.

    Args:
        hub: Repository and token.
        stats: Run totals.
        output_folder: Where the run wrote.

    Returns:
        Exit code: 0 on success, 1 when the publish failed.

    """
    try:
        publish_dataset(HfApi(token=hub.token), hub, stats, build_output_folders(output_folder))
    except PublishError:
        logger.exception("Publishing failed; the dataset on disk is complete, rerun with --publish-only")
        return EXIT_FAILURE
    logger.info("Published the dataset to %s", hub.repo)
    return EXIT_SUCCESS


def run_generate_command(arguments: DatasetArguments, environment: DatasetEnvironment) -> int:
    """Synthesize every prompt with every voice, write the shards, and publish them with `--publish`.

    The command checks every flag and variable before the run, so a missing HF_TOKEN or a refused clean stops it at
    once.

    Args:
        arguments: Parsed flags.
        environment: Variables from `read_environment`.

    Returns:
        Exit code: 0 on success, 1 when the publish failed.

    """
    server = build_server_settings(arguments, environment)
    hub = build_hub_settings(arguments, environment) if arguments.publish else None
    _assert_clean_allowed(arguments)
    prompts = list_corpus_prompts() if arguments.prompts_path is None else read_prompts(arguments.prompts_path)
    voices = list(VOICES.values()) if arguments.voice is None else [VOICES[arguments.voice]]
    logger.info("Loaded %d prompts for the voices %s", len(prompts), ", ".join(voice.name for voice in voices))
    settings = GenerationSettings(
        server=server,
        output_folder=arguments.output_folder,
        clips_per_shard=arguments.clips_per_shard,
        concurrency=arguments.concurrency,
        resume=arguments.resume,
        max_prompts=arguments.max_prompts,
    )
    client = OrpheusClient(server.url, server.api_key)
    stats = asyncio.run(_run_until_stopped(generate_dataset(client, prompts, voices, settings)))
    return EXIT_SUCCESS if hub is None else publish_after_run(hub, stats, arguments.output_folder)

"""A dataset run against the fake server writes its output folder, and --resume finishes a stopped run from it."""

from __future__ import annotations

from typing import TYPE_CHECKING

from src.dataset.stats import read_stats, read_fingerprint
from tests.harness.tasks import build_prompt_list, build_generation_tasks
from src.dataset.cli.main import main
from tests.harness.server import (
    FakeTtsServer,
    serve_fake_tts,
    build_audio_reply,
    build_error_reply,
    list_requested_clips,
)
from tests.harness.voices import TABLE_VOICES
from src.dataset.cli.arguments import EXIT_FAILURE, EXIT_SUCCESS
from src.dataset.generation.tasks import build_output_folders
from src.dataset.generation.resume import build_fingerprint
from tests.suites.integration.builders import (
    CLIPS_PER_SHARD,
    build_run_flags,
    list_shard_keys,
    write_prompt_file,
)

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Sequence

    from schemas.dataset.generation import GenerationTask

PROMPTS = build_prompt_list(3)
CLIP_SECONDS = 0.5
STOPPED_AFTER = 2
"""The clips a stopped run writes before the server fails its next request."""

OTHER_CLIPS_PER_SHARD = 3
"""Clips per shard that split a run's clips unlike the suite's value."""


def _run(tmp_path: Path, fake: FakeTtsServer, prompts: Sequence[str], *flags: str) -> int:
    prompts_path = write_prompt_file(tmp_path / "prompts.txt", prompts)
    with serve_fake_tts(fake) as server_url:
        return main([*build_run_flags(server_url, prompts_path, tmp_path / "output"), *flags])


def _list_tasks(tmp_path: Path) -> list[GenerationTask]:
    return build_generation_tasks(build_output_folders(tmp_path / "output").audio_folder, len(PROMPTS))


def _split_into_shards(tasks: Sequence[GenerationTask], clips_per_shard: int) -> list[list[str]]:
    keys = [task.key for task in tasks]
    return [keys[start : start + clips_per_shard] for start in range(0, len(keys), clips_per_shard)]


def _build_answering_server() -> FakeTtsServer:
    return FakeTtsServer(default_reply=build_audio_reply(CLIP_SECONDS))


def test_run_writes_output_folder(tmp_path: Path) -> None:
    """A run requests each prompt in each voice once and leaves the clips, shards, stats file, and fingerprint.

    Args:
        tmp_path: The test folder.

    """
    fake = _build_answering_server()

    exit_code = _run(tmp_path, fake, PROMPTS)

    folders = build_output_folders(tmp_path / "output")
    tasks = _list_tasks(tmp_path)
    shards = _split_into_shards(tasks, CLIPS_PER_SHARD)
    stats = read_stats(folders.stats_path)
    assert exit_code == EXIT_SUCCESS
    assert list_requested_clips(fake.connections) == [(task.prompt, task.voice.name) for task in tasks]
    assert sorted(folders.audio_folder.iterdir()) == [task.audio_path for task in tasks]
    assert list_shard_keys(folders.shards_folder) == shards
    assert read_fingerprint(folders.fingerprint_path) == build_fingerprint(PROMPTS, TABLE_VOICES)
    assert (stats.clip_count, stats.shard_count, stats.prompt_count) == (len(tasks), len(shards), len(PROMPTS))


def test_resume_finishes_stopped_run(tmp_path: Path) -> None:
    """After a server failure stops a run, --resume requests only the missing clips and shards every clip.

    Args:
        tmp_path: The test folder.

    """
    stopping = FakeTtsServer([build_audio_reply(CLIP_SECONDS)] * STOPPED_AFTER + [build_error_reply("model crashed")])
    resuming = _build_answering_server()
    stopped_code = _run(tmp_path, stopping, PROMPTS)

    resumed_code = _run(tmp_path, resuming, PROMPTS, "--resume")

    folders = build_output_folders(tmp_path / "output")
    tasks = _list_tasks(tmp_path)
    assert (stopped_code, resumed_code) == (EXIT_FAILURE, EXIT_SUCCESS)
    assert list_requested_clips(resuming.connections) == [
        (task.prompt, task.voice.name) for task in tasks[STOPPED_AFTER:]
    ]
    assert list_shard_keys(folders.shards_folder) == _split_into_shards(tasks, CLIPS_PER_SHARD)
    assert read_stats(folders.stats_path).clip_count == len(tasks)


def test_finished_run_reshards_offline(tmp_path: Path) -> None:
    """Resuming a finished run requests nothing and writes the shards again, here at another size.

    Args:
        tmp_path: The test folder.

    """
    idle = FakeTtsServer()
    _run(tmp_path, _build_answering_server(), PROMPTS)

    exit_code = _run(tmp_path, idle, PROMPTS, "--resume", "--clips-per-shard", str(OTHER_CLIPS_PER_SHARD))

    shards_folder = build_output_folders(tmp_path / "output").shards_folder
    assert exit_code == EXIT_SUCCESS
    assert idle.connections == []
    assert list_shard_keys(shards_folder) == _split_into_shards(_list_tasks(tmp_path), OTHER_CLIPS_PER_SHARD)


def test_changed_prompts_stop_resume(tmp_path: Path) -> None:
    """A changed prompt list stops --resume with the failure code, before any request, and keeps the clips.

    Args:
        tmp_path: The test folder.

    """
    changed = _build_answering_server()
    _run(tmp_path, _build_answering_server(), PROMPTS)
    audio_folder = build_output_folders(tmp_path / "output").audio_folder
    clips = sorted(audio_folder.iterdir())

    exit_code = _run(tmp_path, changed, [*PROMPTS[:-1], "A prompt that the first run never read."], "--resume")

    assert exit_code == EXIT_FAILURE
    assert changed.connections == []
    assert sorted(audio_folder.iterdir()) == clips


def test_resume_without_existing_run(tmp_path: Path) -> None:
    """--resume on a folder no run wrote starts from the first clip and requests every clip.

    Args:
        tmp_path: The test folder.

    """
    fake = _build_answering_server()

    exit_code = _run(tmp_path, fake, PROMPTS, "--resume")

    assert exit_code == EXIT_SUCCESS
    assert list_requested_clips(fake.connections) == [(task.prompt, task.voice.name) for task in _list_tasks(tmp_path)]

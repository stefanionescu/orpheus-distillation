"""The training loop steps, writes checkpoints on its interval, and stops between steps when a signal asks."""

from __future__ import annotations

import os
import signal
from typing import TYPE_CHECKING
from dataclasses import replace

import torch
import pytest
from torch.optim import AdamW
from transformers import get_cosine_schedule_with_warmup
from torch.utils.data import DataLoader
from torch.utils.data.distributed import DistributedSampler

from tests.harness.voices import FIRST_VOICE
from tests.harness.manifests import write_clip_manifest
from tests.harness.checkpoints import build_training_folders, build_training_settings
from config.models.voxcpm_1_5.checkpoints import STEP_PREFIX, STEP_TEMPLATE
from src.train.models.voxcpm_1_5.training.loop import (
    STOP_SIGNALS,
    TrainingContext,
    TrainingProgress,
    is_step_due,
    run_validation,
    run_training_steps,
    install_stop_signal,
    build_batch_iterator,
)
from src.train.models.voxcpm_1_5.training.batch import build_batch_packer
from src.train.models.voxcpm_1_5.training.dataset import build_loader, collate_batch, read_training_dataset
from tests.suites.unit.models.voxcpm_1_5.builders import MODEL_SAMPLE_RATE, build_tiny_model, build_lora_config
from src.train.models.voxcpm_1_5.training.accelerator import Accelerator
from src.train.models.voxcpm_1_5.training.checkpoints import write_checkpoint, read_checkpoint_step
from tests.suites.unit.models.voxcpm_1_5.training_runs import FakeWriter, NumberedClips

if TYPE_CHECKING:
    from types import FrameType
    from pathlib import Path

    from schemas.models.voxcpm_1_5.training import TrainingClip

CPU = torch.device("cpu")
CLIP_SECONDS = 0.01
CHECKPOINT_INTERVAL = 2
STEPS = 3
EARLIER_TIME_NS = 10**18
"""An old file time, so a rewrite shows even within one tick of the file system clock."""
OTHER_RANK = 1
SHARE_SIZE = 8
VALIDATION_STEP = 2


def _build_context(tmp_path: Path) -> TrainingContext:
    model = build_tiny_model(lora_config=build_lora_config())
    folders = build_training_folders(tmp_path, tmp_path, has_validation=False)
    write_clip_manifest(folders.train_manifest_path, [(FIRST_VOICE, CLIP_SECONDS)] * 2, MODEL_SAMPLE_RATE)
    settings = build_training_settings(folders, FIRST_VOICE.name, steps=STEPS, checkpoint_interval=CHECKPOINT_INTERVAL)
    dataset = read_training_dataset(folders.train_manifest_path, FIRST_VOICE.name, model, None)
    optimizer = AdamW(model.parameters(), lr=settings.learning_rate)
    return TrainingContext(
        model=model,
        unwrapped_model=model,
        train_loader=build_loader(dataset, settings, None, is_training=True),
        train_sampler=None,
        train_size=len(dataset),
        val_loader=None,
        batch_packer=build_batch_packer(model, CPU),
        optimizer=optimizer,
        scheduler=get_cosine_schedule_with_warmup(optimizer, 0, STEPS),
        accelerator=Accelerator(CPU, 1, 0, None),
        writer=None,
        settings=settings,
    )


def _list_file_identities(folder: Path) -> dict[str, tuple[int, int]]:
    return {path.name: (path.stat().st_ino, path.stat().st_mtime_ns) for path in folder.iterdir()}


@pytest.mark.parametrize(
    ("step", "is_due"), [(5, False), (10, True), (STEPS, True)], ids=["between", "interval", "last-step"]
)
def test_action_due_on_interval(step: int, *, is_due: bool) -> None:
    """A periodic action runs every interval of steps and after the last step of the run.

    Args:
        step: Steps completed.
        is_due: Whether the action runs after that step.

    """
    assert is_step_due(step, 10, STEPS) is is_due


def test_checkpoints_follow_interval(tmp_path: Path) -> None:
    """The loop writes a checkpoint at each checkpoint interval and after the last step.

    Args:
        tmp_path: The test folder.

    """
    context = _build_context(tmp_path)

    checkpoint_folder = run_training_steps(context, TrainingProgress(step=0))

    voice_checkpoints_folder = context.settings.folders.voice_checkpoints_folder
    assert sorted(folder.name for folder in voice_checkpoints_folder.glob(f"{STEP_PREFIX}*")) == [
        STEP_TEMPLATE.format(step=CHECKPOINT_INTERVAL),
        STEP_TEMPLATE.format(step=STEPS),
    ]
    assert read_checkpoint_step(checkpoint_folder) == STEPS
    assert context.scheduler.last_epoch == STEPS


def test_stop_request_ends_run(tmp_path: Path) -> None:
    """A stop request takes no further step and writes the last completed step's checkpoint.

    Args:
        tmp_path: The test folder.

    """
    context = _build_context(tmp_path)
    progress = TrainingProgress(step=1)
    progress.request_stop(signal.SIGTERM, None)

    checkpoint_folder = run_training_steps(context, progress)

    assert checkpoint_folder.name == STEP_TEMPLATE.format(step=1)
    assert read_checkpoint_step(checkpoint_folder) == 1
    assert context.scheduler.last_epoch == 0


def test_saved_step_not_rewritten(tmp_path: Path) -> None:
    """A stop at a step already saved on disk leaves its files untouched.

    A rewrite replaces the files the newest link points at, so a KILL during it leaves no whole checkpoint.

    Args:
        tmp_path: The test folder.

    """
    context = _build_context(tmp_path)
    saved_folder = write_checkpoint(
        context.unwrapped_model, context.optimizer, context.scheduler, CHECKPOINT_INTERVAL, context.settings.folders
    )
    for path in saved_folder.iterdir():
        os.utime(path, ns=(EARLIER_TIME_NS, EARLIER_TIME_NS))
    saved_files = _list_file_identities(saved_folder)
    progress = TrainingProgress(step=CHECKPOINT_INTERVAL)
    progress.request_stop(signal.SIGTERM, None)

    checkpoint_folder = run_training_steps(context, progress)

    assert checkpoint_folder == saved_folder
    assert _list_file_identities(saved_folder) == saved_files


def test_signal_only_requests_stop() -> None:
    """SIGTERM during training records a stop request instead of ending the process, until the handler leaves."""
    progress = TrainingProgress(step=0)
    earlier_action = signal.getsignal(signal.SIGTERM)

    with install_stop_signal(progress):
        signal.raise_signal(signal.SIGTERM)

    assert (progress.stop_requested, progress.stop_signal) == (True, signal.SIGTERM)
    assert signal.getsignal(signal.SIGTERM) == earlier_action


def test_workers_ignore_stop_signals(tmp_path: Path) -> None:
    """A training loader worker survives SIGINT and SIGTERM, which a process group signal also sends it.

    Args:
        tmp_path: The test folder.

    """
    worker_init = _build_context(tmp_path).train_loader.worker_init_fn
    received: list[int] = []

    def record_signal(signal_number: int, _frame: FrameType | None) -> None:
        received.append(signal_number)

    earlier_actions = {number: signal.signal(number, record_signal) for number in STOP_SIGNALS}
    try:
        assert worker_init is not None
        worker_init(0)
        for number in STOP_SIGNALS:
            signal.raise_signal(number)
    finally:
        for number, action in earlier_actions.items():
            signal.signal(number, action)

    assert received == []


def test_other_rank_writes_nothing(tmp_path: Path) -> None:
    """A process other than rank 0 writes no checkpoint, so the processes of a run never write one folder at once.

    Args:
        tmp_path: The test folder.

    """
    context = _build_context(tmp_path)
    context.accelerator.rank = OTHER_RANK

    checkpoint_folder = run_training_steps(context, TrainingProgress(step=0))

    assert checkpoint_folder.name == STEP_TEMPLATE.format(step=STEPS)
    assert not context.settings.folders.voice_checkpoints_folder.exists()


def test_metrics_count_epochs(tmp_path: Path) -> None:
    """Each logged step records the epochs of clips seen so far, counting the step it just took.

    Args:
        tmp_path: The test folder.

    """
    writer = FakeWriter()
    context = replace(_build_context(tmp_path), writer=writer)

    run_training_steps(context, TrainingProgress(step=0))

    # Each step takes one batch of both clips, so each step is one more epoch.
    assert [(step, value) for tag, value, step in writer.scalars if tag == "train/epoch"] == [
        (1, 1.0),
        (2, 2.0),
        (3, 3.0),
    ]


def test_validation_restores_training(tmp_path: Path) -> None:
    """Validation records one mean loss at its step and puts the model back in training mode.

    Args:
        tmp_path: The test folder.

    """
    writer = FakeWriter()
    context = _build_context(tmp_path)
    dataset = read_training_dataset(
        context.settings.folders.train_manifest_path, FIRST_VOICE.name, context.unwrapped_model, None
    )
    val_loader = build_loader(dataset, context.settings, None, is_training=False)
    context = replace(context, writer=writer, val_loader=val_loader)

    run_validation(context, VALIDATION_STEP)

    [(tag, value, step)] = writer.scalars
    assert (tag, step) == ("val/loss/total", VALIDATION_STEP)
    assert value > 0
    assert context.model.training


def test_epochs_reshuffle_share() -> None:
    """Each epoch of a distributed run draws a new order of the process share, and each clip once."""
    clips = NumberedClips(SHARE_SIZE)
    sampler: DistributedSampler[TrainingClip] = DistributedSampler(clips, num_replicas=1, rank=0)
    loader = DataLoader(clips, batch_size=SHARE_SIZE, sampler=sampler, collate_fn=collate_batch)
    batches = build_batch_iterator(loader, sampler)

    first, second = [[int(token) for token in next(batches).text_tokens[:, 0]] for _ in range(2)]

    assert sorted(first) == sorted(second) == list(range(SHARE_SIZE))
    assert first != second

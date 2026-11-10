"""A few training steps of one voice on the GPU write checkpoints, lower the loss, and resume after a restart."""

from __future__ import annotations

from typing import TYPE_CHECKING
import logging
from statistics import fmean
from dataclasses import replace

from tests.harness.voices import FIRST_VOICE
from config.voxcpm_1_5.checkpoints import NEWEST_LINK, STEP_TEMPLATE
from src.train.voxcpm_1_5.training import loop
from tests.suites.e2e.voxcpm_1_5.builders import (
    SMOKE_STEPS,
    RESUMED_STEPS,
    LOSS_WINDOW_STEPS,
    CHECKPOINT_INTERVAL,
    read_logged_losses,
    download_base_model,
    train_smoke_adapter,
    build_smoke_settings,
    write_smoke_manifest,
    assert_cuda_available,
)
from src.train.voxcpm_1_5.training.checkpoints import read_checkpoint_step

if TYPE_CHECKING:
    from pathlib import Path

    import pytest

    from schemas.voxcpm_1_5.training import TrainingSettings


def _prepare_run(tmp_path: Path, caplog: pytest.LogCaptureFixture, steps: int) -> TrainingSettings:
    assert_cuda_available()
    caplog.set_level(logging.INFO, logger=loop.logger.name)
    base_model_folder = download_base_model()
    write_smoke_manifest(tmp_path, [FIRST_VOICE])
    return build_smoke_settings(tmp_path, base_model_folder, FIRST_VOICE, steps)


def _read_losses(caplog: pytest.LogCaptureFixture) -> dict[int, float]:
    return read_logged_losses(record.getMessage() for record in caplog.records if record.name == loop.logger.name)


def test_smoke_run_lowers_loss(tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
    """A short run logs every step with a falling loss and links the last step's checkpoint as the newest.

    Args:
        tmp_path: The run folder.
        caplog: Captures the loop's metric lines.

    """
    settings = _prepare_run(tmp_path, caplog, SMOKE_STEPS)

    result = train_smoke_adapter(settings)

    voice_checkpoints_folder = settings.folders.voice_checkpoints_folder
    losses = _read_losses(caplog)
    assert result.checkpoint_folder == voice_checkpoints_folder / STEP_TEMPLATE.format(step=SMOKE_STEPS)
    assert (voice_checkpoints_folder / NEWEST_LINK).resolve() == result.checkpoint_folder.resolve()
    assert read_checkpoint_step(result.checkpoint_folder) == SMOKE_STEPS
    assert (
        read_checkpoint_step(voice_checkpoints_folder / STEP_TEMPLATE.format(step=CHECKPOINT_INTERVAL))
        == CHECKPOINT_INTERVAL
    )
    assert sorted(losses) == list(range(1, SMOKE_STEPS + 1))
    first_steps, last_steps = list(losses.values())[:LOSS_WINDOW_STEPS], list(losses.values())[-LOSS_WINDOW_STEPS:]
    assert fmean(last_steps) < fmean(first_steps)


def test_restart_resumes_from_checkpoint(tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
    """A second run with more steps starts after the newest checkpoint's step and trains only the rest.

    Args:
        tmp_path: The run folder.
        caplog: Captures the loop's metric lines.

    """
    settings = _prepare_run(tmp_path, caplog, CHECKPOINT_INTERVAL)
    train_smoke_adapter(settings)
    caplog.clear()

    result = train_smoke_adapter(replace(settings, steps=CHECKPOINT_INTERVAL + RESUMED_STEPS))

    assert sorted(_read_losses(caplog)) == list(range(CHECKPOINT_INTERVAL + 1, CHECKPOINT_INTERVAL + RESUMED_STEPS + 1))
    assert read_checkpoint_step(result.checkpoint_folder) == CHECKPOINT_INTERVAL + RESUMED_STEPS

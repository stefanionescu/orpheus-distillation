"""A checkpoint holds a step's LoRA weights and optimizer state, and a resumed run reads them back."""

from __future__ import annotations

import json
import errno
import shutil
from typing import TYPE_CHECKING, cast

import torch
import pytest
from torch.optim import AdamW
from transformers import get_cosine_schedule_with_warmup
import safetensors.torch

from tests.harness.voices import FIRST_VOICE
from tests.harness.checkpoints import build_training_folders, create_checkpoint_tree
from config.models.voxcpm_1_5.checkpoints import NEWEST_LINK, STEP_TEMPLATE, TRAINING_STATE_FILE
from src.train.models.voxcpm_1_5.training import checkpoints
from src.train.models.voxcpm_1_5.model.lora import LORA_WEIGHTS_FILE
from tests.suites.unit.models.voxcpm_1_5.builders import build_tiny_model, build_lora_config, write_lora_weights
from src.train.models.voxcpm_1_5.training.checkpoints import (
    CheckpointError,
    read_checkpoint,
    write_checkpoint,
    read_checkpoint_step,
)

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Callable

    from torch.optim.lr_scheduler import LambdaLR

    from src.train.models.voxcpm_1_5.model.voxcpm import VoxCPMModel

SAVED_STEP = 3
STALE_FILE = "stale.bin"


def _build_optimizer(model: VoxCPMModel) -> tuple[AdamW, LambdaLR]:
    optimizer = AdamW([parameter for name, parameter in model.named_parameters() if "lora_" in name], lr=1e-3)
    return optimizer, get_cosine_schedule_with_warmup(optimizer, 0, SAVED_STEP * 2)


def _fill_disk(_state: object, path: Path) -> None:
    path.write_bytes(b"\x80")
    raise OSError(errno.ENOSPC, "No space left on device", str(path))


def _write_trained_checkpoint(run_folder: Path, step: int) -> tuple[VoxCPMModel, Path]:
    model = build_tiny_model(lora_config=build_lora_config())
    optimizer, scheduler = _build_optimizer(model)
    with torch.no_grad():
        for name, parameter in model.named_parameters():
            if "lora_" in name:
                parameter.grad = torch.ones_like(parameter)
    cast("Callable[[], object]", optimizer.step)()
    scheduler.step()
    folders = build_training_folders(run_folder, run_folder, has_validation=False)
    write_checkpoint(model, optimizer, scheduler, step, folders)
    return model, folders.voice_checkpoints_folder


def _rewrite_checkpoint(model: VoxCPMModel, run_folder: Path, step: int) -> Path:
    optimizer, scheduler = _build_optimizer(model)
    return write_checkpoint(
        model, optimizer, scheduler, step, build_training_folders(run_folder, run_folder, has_validation=False)
    )


def test_checkpoint_holds_lora_only(tmp_path: Path) -> None:
    """The weights file holds every LoRA weight of the model and no base weight.

    Args:
        tmp_path: The test folder.

    """
    model, voice_checkpoints_folder = _write_trained_checkpoint(tmp_path, SAVED_STEP)

    weights_path = voice_checkpoints_folder / STEP_TEMPLATE.format(step=SAVED_STEP) / LORA_WEIGHTS_FILE
    names = sorted(safetensors.torch.load(weights_path.read_bytes()))
    assert names == sorted(name for name, _ in model.named_parameters() if "lora_" in name)


def test_resume_restores_weights(tmp_path: Path) -> None:
    """A fresh model resumes at the saved step with the saved LoRA weights and optimizer state.

    Args:
        tmp_path: The test folder.

    """
    trained, voice_checkpoints_folder = _write_trained_checkpoint(tmp_path, SAVED_STEP)
    fresh = build_tiny_model(lora_config=build_lora_config())
    with torch.no_grad():
        for name, parameter in fresh.named_parameters():
            if "lora_" in name:
                parameter.zero_()
    optimizer, scheduler = _build_optimizer(fresh)

    step = read_checkpoint(fresh, optimizer, scheduler, voice_checkpoints_folder)

    trained_weights = {name: parameter for name, parameter in trained.named_parameters() if "lora_" in name}
    assert step == SAVED_STEP
    assert all(
        torch.equal(parameter, trained_weights[name])
        for name, parameter in fresh.named_parameters()
        if name in trained_weights
    )
    assert len(optimizer.state) == len(trained_weights)
    assert scheduler.last_epoch == 1


def test_newest_link_survives_move(tmp_path: Path) -> None:
    """The newest link names its checkpoint relative to the voice folder, so a moved run keeps a valid link.

    Args:
        tmp_path: The test folder.

    """
    run_folder = tmp_path / "run"
    _, voice_checkpoints_folder = _write_trained_checkpoint(run_folder, SAVED_STEP)

    moved_folder = run_folder.rename(tmp_path / "moved")

    moved_link = moved_folder / voice_checkpoints_folder.relative_to(run_folder) / NEWEST_LINK
    assert (moved_link / LORA_WEIGHTS_FILE).is_file()


def test_newest_link_moves_forward(tmp_path: Path) -> None:
    """A second checkpoint moves the newest link off the first one, which stays on disk.

    Args:
        tmp_path: The test folder.

    """
    model, voice_checkpoints_folder = _write_trained_checkpoint(tmp_path, SAVED_STEP)

    _rewrite_checkpoint(model, tmp_path, SAVED_STEP + 1)

    assert (voice_checkpoints_folder / NEWEST_LINK).resolve().name == STEP_TEMPLATE.format(step=SAVED_STEP + 1)
    assert (voice_checkpoints_folder / STEP_TEMPLATE.format(step=SAVED_STEP) / LORA_WEIGHTS_FILE).is_file()


def test_resume_without_link(tmp_path: Path) -> None:
    """A voice whose newest link is gone resumes from its highest complete step, not step 0.

    Args:
        tmp_path: The test folder.

    """
    _, voice_checkpoints_folder = _write_trained_checkpoint(tmp_path, SAVED_STEP)
    (voice_checkpoints_folder / NEWEST_LINK).unlink()
    model = build_tiny_model(lora_config=build_lora_config())
    optimizer, scheduler = _build_optimizer(model)

    assert read_checkpoint(model, optimizer, scheduler, voice_checkpoints_folder) == SAVED_STEP


def test_fresh_voice_starts_zero(tmp_path: Path) -> None:
    """A voice without a checkpoint starts at step 0 and leaves the model unchanged.

    Args:
        tmp_path: The test folder.

    """
    model = build_tiny_model(lora_config=build_lora_config())
    optimizer, scheduler = _build_optimizer(model)

    assert read_checkpoint(model, optimizer, scheduler, tmp_path / FIRST_VOICE.name) == 0


def test_link_without_weights_raises(tmp_path: Path) -> None:
    """A newest link to a folder without weights stops the run instead of training over it from scratch.

    Args:
        tmp_path: The test folder.

    """
    create_checkpoint_tree(tmp_path, [SAVED_STEP], SAVED_STEP)
    model = build_tiny_model(lora_config=build_lora_config())
    optimizer, scheduler = _build_optimizer(model)

    with pytest.raises(CheckpointError, match=LORA_WEIGHTS_FILE):
        read_checkpoint(model, optimizer, scheduler, tmp_path)


def test_failed_rewrite_keeps_checkpoint(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A rewrite of the newest checkpoint that fails halfway, as on a full disk, leaves that checkpoint readable.

    Args:
        tmp_path: The test folder.
        monkeypatch: Fills the disk during the optimizer state write.

    """
    trained, voice_checkpoints_folder = _write_trained_checkpoint(tmp_path, SAVED_STEP)
    monkeypatch.setattr(checkpoints, "write_torch_file", _fill_disk)
    with pytest.raises(OSError, match="No space left"):
        _rewrite_checkpoint(trained, tmp_path, SAVED_STEP)
    fresh = build_tiny_model(lora_config=build_lora_config())
    fresh_optimizer, fresh_scheduler = _build_optimizer(fresh)

    assert read_checkpoint(fresh, fresh_optimizer, fresh_scheduler, voice_checkpoints_folder) == SAVED_STEP


def test_rewrite_replaces_leftovers(tmp_path: Path) -> None:
    """A run that reaches a written step again replaces that step and the half-written folder of a killed write.

    A kill between the rename and the link update leaves the link on an older step, so the resumed run writes the
    newer step a second time.

    Args:
        tmp_path: The test folder.

    """
    trained, voice_checkpoints_folder = _write_trained_checkpoint(tmp_path, SAVED_STEP)
    step_name = STEP_TEMPLATE.format(step=SAVED_STEP)
    for folder in (voice_checkpoints_folder / step_name, voice_checkpoints_folder / f".{step_name}.partial"):
        folder.mkdir(exist_ok=True)
        (folder / STALE_FILE).write_bytes(b"stale")

    checkpoint_folder = _rewrite_checkpoint(trained, tmp_path, SAVED_STEP)

    assert sorted(path.name for path in voice_checkpoints_folder.iterdir()) == [NEWEST_LINK, step_name]
    assert not (checkpoint_folder / STALE_FILE).exists()
    assert read_checkpoint_step(checkpoint_folder) == SAVED_STEP


def test_copied_newest_folder_replaced(tmp_path: Path) -> None:
    """A newest folder that a copy turned from a link into a real folder becomes a link to the next checkpoint.

    Args:
        tmp_path: The test folder.

    """
    model, voice_checkpoints_folder = _write_trained_checkpoint(tmp_path, SAVED_STEP)
    newest_link = voice_checkpoints_folder / NEWEST_LINK
    newest_link.unlink()
    shutil.copytree(voice_checkpoints_folder / STEP_TEMPLATE.format(step=SAVED_STEP), newest_link)

    _rewrite_checkpoint(model, tmp_path, SAVED_STEP + 1)

    assert newest_link.resolve() == (voice_checkpoints_folder / STEP_TEMPLATE.format(step=SAVED_STEP + 1)).resolve()


def test_unknown_weights_stop_resume(tmp_path: Path) -> None:
    """A newest checkpoint with weights the model lacks, as from other LoRA settings, stops the resume.

    Args:
        tmp_path: The test folder.

    """
    trained, voice_checkpoints_folder = _write_trained_checkpoint(tmp_path, SAVED_STEP)
    write_lora_weights(trained, voice_checkpoints_folder / NEWEST_LINK, {"extra.lora_A": torch.zeros(1)})
    model = build_tiny_model(lora_config=build_lora_config())
    optimizer, scheduler = _build_optimizer(model)

    with pytest.raises(CheckpointError):
        read_checkpoint(model, optimizer, scheduler, voice_checkpoints_folder)


@pytest.mark.parametrize(
    "content",
    [None, "{not json", json.dumps([SAVED_STEP]), json.dumps({"step": str(SAVED_STEP)})],
    ids=["missing", "not-json", "not-an-object", "step-not-a-number"],
)
def test_bad_training_state_raises(tmp_path: Path, content: str | None) -> None:
    """A training state that holds no whole step number stops the reader instead of resuming from a wrong step.

    Args:
        tmp_path: The checkpoint folder.
        content: The state file text, or None for no file.

    """
    if content is not None:
        (tmp_path / TRAINING_STATE_FILE).write_text(content, encoding="utf-8")

    with pytest.raises(CheckpointError):
        read_checkpoint_step(tmp_path)

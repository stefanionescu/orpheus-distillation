"""Inference and publishing find the newest checkpoint of each voice that training wrote."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.harness.voices import FIRST_VOICE, SECOND_VOICE, TABLE_VOICES
from tests.harness.checkpoints import create_checkpoint_tree
from config.voxcpm_1_5.checkpoints import STEP_TEMPLATE, TRAINING_STATE_FILE
from src.train.voxcpm_1_5.training.checkpoints import (
    CheckpointError,
    find_newest_checkpoint,
    list_voice_checkpoints,
)

if TYPE_CHECKING:
    from pathlib import Path

VOICE_NAMES = tuple(voice.name for voice in TABLE_VOICES)


def test_newest_link_wins(tmp_path: Path) -> None:
    """The newest link picks the checkpoint, even when a higher step folder exists.

    Args:
        tmp_path: The test folder.

    """
    linked, _ = create_checkpoint_tree(tmp_path, [5, 10], 5)

    assert find_newest_checkpoint(tmp_path) == linked.resolve()


def test_highest_step_without_link(tmp_path: Path) -> None:
    """Without a newest link, the highest step wins, and a complete folder without a step number is no checkpoint.

    Args:
        tmp_path: The test folder.

    """
    _, highest = create_checkpoint_tree(tmp_path, [9, 10], None)
    backup_folder = tmp_path / "backup"
    backup_folder.mkdir()
    (backup_folder / TRAINING_STATE_FILE).write_text("{}", encoding="utf-8")

    assert find_newest_checkpoint(tmp_path) == highest


def test_incomplete_folders_skipped(tmp_path: Path) -> None:
    """Without a newest link, the search skips a step folder without its training state and a write in progress.

    Args:
        tmp_path: The test folder.

    """
    [complete, incomplete] = create_checkpoint_tree(tmp_path, [1, 2], None)
    (incomplete / TRAINING_STATE_FILE).unlink()
    partial_folder = tmp_path / f".{STEP_TEMPLATE.format(step=3)}.partial"
    partial_folder.mkdir()
    (partial_folder / TRAINING_STATE_FILE).write_text("{}", encoding="utf-8")

    assert find_newest_checkpoint(tmp_path) == complete


@pytest.mark.parametrize("is_created", [False, True], ids=["missing-folder", "empty-folder"])
def test_no_checkpoint_found(tmp_path: Path, *, is_created: bool) -> None:
    """A voice with a missing or empty folder of checkpoints has no newest checkpoint.

    Args:
        tmp_path: The test folder.
        is_created: Whether the folder of the voice exists.

    """
    voice_checkpoints_folder = tmp_path / FIRST_VOICE.name
    if is_created:
        voice_checkpoints_folder.mkdir()

    assert find_newest_checkpoint(voice_checkpoints_folder) is None


def test_voices_without_checkpoint_skipped(tmp_path: Path) -> None:
    """Each voice with a checkpoint maps to its newest one, and a voice without one drops out.

    Args:
        tmp_path: The test folder.

    """
    [checkpoint_folder] = create_checkpoint_tree(tmp_path / SECOND_VOICE.name, [1], 1)

    assert list_voice_checkpoints(tmp_path, VOICE_NAMES) == {SECOND_VOICE.name: checkpoint_folder.resolve()}


def test_no_voice_checkpoint_raises(tmp_path: Path) -> None:
    """A checkpoints folder with no voice checkpoint stops inference and publishing.

    Args:
        tmp_path: The test folder.

    """
    with pytest.raises(CheckpointError):
        list_voice_checkpoints(tmp_path, VOICE_NAMES)

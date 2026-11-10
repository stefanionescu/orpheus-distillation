"""The LoRA config reader returns the config that training wrote and refuses any other file."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest
from torch.optim import AdamW
from transformers import get_cosine_schedule_with_warmup

from tests.harness.checkpoints import build_training_folders
from config.models.voxcpm_1_5.checkpoints import LORA_CONFIG_FILE
from tests.suites.unit.models.voxcpm_1_5.builders import build_tiny_model, build_lora_config
from src.train.models.voxcpm_1_5.training.checkpoints import CheckpointError, read_lora_config, write_checkpoint

if TYPE_CHECKING:
    from pathlib import Path


def _write_checkpoint(tmp_path: Path) -> Path:
    model = build_tiny_model(lora_config=build_lora_config())
    optimizer = AdamW(model.parameters())
    folders = build_training_folders(tmp_path, tmp_path, has_validation=False)
    return write_checkpoint(model, optimizer, get_cosine_schedule_with_warmup(optimizer, 0, 1), 1, folders)


def test_reader_returns_written_config(tmp_path: Path) -> None:
    """The reader that samples and publish use returns the config training wrote.

    Args:
        tmp_path: The test folder.

    """
    assert read_lora_config(_write_checkpoint(tmp_path)) == build_lora_config()


CONFIG_FIELDS = build_lora_config().model_dump()


@pytest.mark.parametrize(
    "content",
    [
        None,
        "{not json",
        json.dumps(CONFIG_FIELDS | {"rank_pattern": {}}),
        json.dumps({key: value for key, value in CONFIG_FIELDS.items() if key != "dropout"}),
        json.dumps(CONFIG_FIELDS | {"r": "many"}),
    ],
    ids=["missing", "not-json", "extra-field", "missing-field", "invalid-value"],
)
def test_bad_config_raises(tmp_path: Path, content: str | None) -> None:
    """A missing, malformed, or invalid config, or one with other fields, stops the reader instead of filling defaults.

    Args:
        tmp_path: The test folder.
        content: The config file text, or None for no file.

    """
    if content is not None:
        tmp_path.joinpath(LORA_CONFIG_FILE).write_text(content, encoding="utf-8")

    with pytest.raises(CheckpointError):
        read_lora_config(tmp_path)

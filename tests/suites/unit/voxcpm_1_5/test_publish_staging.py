"""Publishing stages every file the model loader reads, each voice's adapter, and the samples."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from config.hub import CARD_FILE
from tests.harness.voices import FIRST_VOICE, SECOND_VOICE
from config.voxcpm_1_5.hub import SAMPLES_FOLDER, ADAPTERS_FOLDER
from config.voxcpm_1_5.data import TOKENIZER_FILES
from schemas.voxcpm_1_5.publish import PublishRequest
from config.voxcpm_1_5.checkpoints import NEWEST_LINK, LORA_CONFIG_FILE, TRAINING_STATE_FILE
from src.train.voxcpm_1_5.model.lora import LORA_WEIGHTS_FILE
from src.train.voxcpm_1_5.hub.publish import PublishError, create_staging_folder
from src.train.voxcpm_1_5.model.loader import MODEL_WEIGHTS_FILES
from tests.suites.unit.voxcpm_1_5.builders import (
    HUB_CONFIG_FILE,
    HUB_WEIGHTS_FILE,
    HUB_AUDIO_VAE_FILE,
    build_lora_config,
)
from tests.suites.unit.voxcpm_1_5.run_files import write_voice_checkpoint, write_base_model_folder

if TYPE_CHECKING:
    from pathlib import Path

ADAPTER_FILES = (LORA_WEIGHTS_FILE, LORA_CONFIG_FILE, TRAINING_STATE_FILE)
SAMPLE_FILE = "sample.wav"


def _build_request(tmp_path: Path, *, has_samples: bool) -> PublishRequest:
    base_model_folder = write_base_model_folder(tmp_path / "base_model")
    checkpoints_folder = tmp_path / "run" / "checkpoints"
    for voice in (FIRST_VOICE, SECOND_VOICE):
        write_voice_checkpoint(checkpoints_folder, voice.name, build_lora_config(), 1)
    samples_folder = tmp_path / "run" / SAMPLES_FOLDER
    if has_samples:
        samples_folder.mkdir()
        (samples_folder / SAMPLE_FILE).write_bytes(b"RIFF")
    return PublishRequest(
        run_name="orpheus-run",
        checkpoints_folder=checkpoints_folder,
        base_model_folder=base_model_folder,
        tokenizer_folder=base_model_folder,
        samples_folder=samples_folder if has_samples else None,
        output_repo="owner/voice-adapters",
        base_model_repo="owner/base-model",
        public=False,
    )


def _list_files(folder: Path) -> set[str]:
    return {str(path.relative_to(folder)) for path in folder.rglob("*") if path.is_file()}


def test_staging_holds_loader_files(tmp_path: Path) -> None:
    """The staged repository holds each voice's adapter, the base model files under their Hub names, and a card.

    Args:
        tmp_path: The test folder.

    """
    staging_folder = create_staging_folder(_build_request(tmp_path, has_samples=True))

    adapter_files = {
        f"{ADAPTERS_FOLDER}/{voice.name}/{filename}"
        for voice in (FIRST_VOICE, SECOND_VOICE)
        for filename in ADAPTER_FILES
    }
    model_files = {HUB_WEIGHTS_FILE, HUB_CONFIG_FILE, HUB_AUDIO_VAE_FILE, *TOKENIZER_FILES}
    assert _list_files(staging_folder) == {
        *adapter_files,
        *model_files,
        f"{SAMPLES_FOLDER}/{SAMPLE_FILE}",
        CARD_FILE,
    }


def test_second_weights_name_staged(tmp_path: Path) -> None:
    """Staging keeps the loader's second weights file name when the base model uses it.

    Args:
        tmp_path: The test folder.

    """
    request = _build_request(tmp_path, has_samples=False)
    first_name, second_name = MODEL_WEIGHTS_FILES
    (request.base_model_folder / first_name).rename(request.base_model_folder / second_name)

    staging_folder = create_staging_folder(request)

    assert (staging_folder / second_name).is_file()
    assert f"`{second_name}`" in (staging_folder / CARD_FILE).read_text(encoding="utf-8")


def test_weightless_base_model_raises(tmp_path: Path) -> None:
    """A base model with neither weights file name cannot load, so staging stops.

    Args:
        tmp_path: The test folder.

    """
    request = _build_request(tmp_path, has_samples=False)
    (request.base_model_folder / HUB_WEIGHTS_FILE).unlink()

    with pytest.raises(PublishError, match=str(request.base_model_folder)):
        create_staging_folder(request)


def test_missing_adapter_raises(tmp_path: Path) -> None:
    """A newest checkpoint without its adapter weights stops staging and names the missing file.

    Args:
        tmp_path: The test folder.

    """
    request = _build_request(tmp_path, has_samples=False)
    weights_path = request.checkpoints_folder / FIRST_VOICE.name / NEWEST_LINK / LORA_WEIGHTS_FILE
    weights_path.unlink()

    with pytest.raises(PublishError, match=LORA_WEIGHTS_FILE):
        create_staging_folder(request)


def test_restaging_drops_stale_files(tmp_path: Path) -> None:
    """A second staging run starts from an empty folder, so the publish leaves out an earlier run's files.

    Args:
        tmp_path: The test folder.

    """
    request = _build_request(tmp_path, has_samples=False)
    stale_path = create_staging_folder(request) / "stale.bin"
    stale_path.write_bytes(b"stale")

    create_staging_folder(request)

    assert not stale_path.exists()

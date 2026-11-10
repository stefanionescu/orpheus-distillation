"""The model card describes the published voices and adapters, and its usage snippet runs on the published files."""

from __future__ import annotations

import wave
import runpy
from typing import TYPE_CHECKING, cast

import torch
import pytest
import safetensors.torch

from config.hub import CARD_FILE
from tests.harness.hub import install_fake_hub
from tests.harness.voices import FIRST_VOICE, SECOND_VOICE
from config.models.voxcpm_1_5.hub import SAMPLES_FOLDER, ADAPTERS_FOLDER
from schemas.models.voxcpm_1_5.publish import PublishRequest
from src.train.models.voxcpm_1_5.hub.card import format_card, format_files_table
from src.train.models.voxcpm_1_5.model.lora import LORA_WEIGHTS_FILE
from src.train.models.voxcpm_1_5.hub.publish import create_staging_folder
from src.train.models.voxcpm_1_5.model.loader import MODEL_WEIGHTS_FILES
from tests.suites.unit.models.voxcpm_1_5.builders import (
    LORA_RANK,
    run_on_cpu,
    build_lora_config,
)
from tests.suites.unit.models.voxcpm_1_5.run_files import write_voice_checkpoint, write_base_model_folder

if TYPE_CHECKING:
    from pathlib import Path

    from src.train.models.voxcpm_1_5.model.voxcpm import VoxCPMModel

RUN_NAME = "orpheus-run"
OUTPUT_REPO = "owner/voice-adapters"
BASE_MODEL_REPO = "owner/base-model"
FIRST_STEPS = 4
SECOND_STEPS = 7
CODE_FENCE = "```"
PYTHON_FENCE = f"{CODE_FENCE}python\n"


def _build_request(run_folder: Path, base_model_folder: Path) -> PublishRequest:
    return PublishRequest(
        run_name=RUN_NAME,
        checkpoints_folder=run_folder / "checkpoints",
        base_model_folder=base_model_folder,
        tokenizer_folder=base_model_folder,
        samples_folder=None,
        output_repo=OUTPUT_REPO,
        base_model_repo=BASE_MODEL_REPO,
        public=False,
    )


def _read_usage_snippet(card_text: str) -> str:
    start = card_text.index(PYTHON_FENCE) + len(PYTHON_FENCE)
    return card_text[start : card_text.index(CODE_FENCE, start)]


def test_card_lists_each_voice(tmp_path: Path) -> None:
    """Each published voice gets a row with its speaker, adapter folder, and steps, and the card shows the rank.

    Args:
        tmp_path: The test folder.

    """
    voice_steps = {FIRST_VOICE.name: FIRST_STEPS, SECOND_VOICE.name: SECOND_STEPS}
    files_table = format_files_table(MODEL_WEIGHTS_FILES[0], has_samples=False)

    card_text = format_card(_build_request(tmp_path, tmp_path), build_lora_config(), voice_steps, files_table)

    for voice, steps in ((FIRST_VOICE, FIRST_STEPS), (SECOND_VOICE, SECOND_STEPS)):
        assert f"| {voice.name} | {voice.display_name} | `{ADAPTERS_FOLDER}/{voice.name}` | {steps} |" in card_text
    assert f"| Rank | {LORA_RANK} |" in card_text
    assert f"`{RUN_NAME}`" in card_text


def test_card_marks_disabled_layers(tmp_path: Path) -> None:
    """A layer kind that the adapters leave out shows as none, and the others list their layers.

    Args:
        tmp_path: The test folder.

    """
    lora_config = build_lora_config().model_copy(update={"enable_dit": False})
    files_table = format_files_table(MODEL_WEIGHTS_FILES[0], has_samples=False)

    card_text = format_card(_build_request(tmp_path, tmp_path), lora_config, {FIRST_VOICE.name: 1}, files_table)

    language_layers = ", ".join(f"`{layer}`" for layer in lora_config.target_modules_lm)
    assert "| Diffusion transformer layers | none |" in card_text
    assert f"| Language model layers | {language_layers} |" in card_text


@pytest.mark.parametrize("has_samples", [False, True], ids=["without-samples", "with-samples"])
def test_files_table_lists_samples(*, has_samples: bool) -> None:
    """The files table lists the samples folder only when the repository holds samples.

    Args:
        has_samples: Whether the staged repository holds samples.

    """
    files_table = format_files_table(MODEL_WEIGHTS_FILES[0], has_samples=has_samples)

    assert (f"`{SAMPLES_FOLDER}/`" in files_table) is has_samples


def test_card_snippet_runs(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A published card's usage snippet loads the first voice's adapter weights and config and writes a clip.

    The staged folder holds every file the loader reads, so it stands in for the Hub download.

    Args:
        tmp_path: The test folder; the snippet writes its clip here.
        monkeypatch: Replaces the Hub download and the working folder.

    """
    request = _build_request(tmp_path / "run", write_base_model_folder(tmp_path / "base_model"))
    write_voice_checkpoint(request.checkpoints_folder, FIRST_VOICE.name, build_lora_config(), FIRST_STEPS)
    staging_folder = create_staging_folder(request)
    snippet_path = tmp_path / "usage.py"
    snippet_path.write_text(_read_usage_snippet((staging_folder / CARD_FILE).read_text(encoding="utf-8")))
    install_fake_hub(monkeypatch, {OUTPUT_REPO: staging_folder})
    monkeypatch.chdir(tmp_path)

    with run_on_cpu():
        snippet_globals = runpy.run_path(str(snippet_path))

    model = cast("VoxCPMModel", snippet_globals["model"])
    adapter = safetensors.torch.load(
        (staging_folder / ADAPTERS_FOLDER / FIRST_VOICE.name / LORA_WEIGHTS_FILE).read_bytes()
    )
    parameters = dict(model.named_parameters())
    assert model.lora_config == build_lora_config()
    assert all(torch.equal(parameters[name], weight) for name, weight in adapter.items())
    with wave.open(str(tmp_path / f"{FIRST_VOICE.name}.wav")) as clip:
        assert clip.getnframes() > 0

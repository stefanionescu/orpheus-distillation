"""The commands run their stage in process, print each result as a key=value line, and exit 1 on an expected failure."""

from __future__ import annotations

import wave
import signal
from typing import TYPE_CHECKING, NoReturn

import torch
import httpx2
import pytest

from config.hub import CARD_FILE, DATASET_REPO
from src.train.cli import EXIT_FAILURE, EXIT_SUCCESS, EXIT_SIGNAL_BASE
from tests.harness.hub import install_fake_hub
from tests.harness.voices import FIRST_VOICE
from tests.harness.environment import set_hf_token
from tests.suites.unit.builders import read_results
from config.models.voxcpm_1_5.hub import STAGING_FOLDER, BASE_MODEL_REPO, PUBLISH_COMMIT_MESSAGE
from config.models.voxcpm_1_5.training import LOG_INTERVAL
from config.models.voxcpm_1_5.checkpoints import STEP_TEMPLATE
from src.train.models.voxcpm_1_5.commands import infer, train, prepare, publish
from tests.suites.unit.models.voxcpm_1_5.builders import (
    PATCH_SIZE,
    SHORT_MAX_PATCHES,
    run_on_cpu,
    build_tiny_model,
    build_lora_config,
)
from tests.suites.unit.models.voxcpm_1_5.run_files import (
    write_train_flags,
    write_voice_checkpoint,
    write_base_model_folder,
)
from src.train.models.voxcpm_1_5.training.checkpoints import read_checkpoint_step
from tests.suites.unit.models.voxcpm_1_5.training_runs import install_stopping_cpu_run

if TYPE_CHECKING:
    from pathlib import Path

    from tests.harness.hub import FakeHub

OUTPUT_REPO = "owner/voice-adapters"


def _write_publish_inputs(tmp_path: Path) -> list[str]:
    base_model_folder = write_base_model_folder(tmp_path / "base_model")
    write_voice_checkpoint(tmp_path / "run" / "checkpoints", FIRST_VOICE.name, build_lora_config(), 1)
    return [
        "--run-name",
        "first-run",
        "--checkpoints-folder",
        str(tmp_path / "run" / "checkpoints"),
        "--base-model-folder",
        str(base_model_folder),
        "--tokenizer-folder",
        str(base_model_folder),
        "--output-repo",
        OUTPUT_REPO,
    ]


def _refuse_connection(*_arguments: object, **_options: object) -> NoReturn:
    message = "Connection refused"
    raise httpx2.ConnectError(message)


def _install_hub(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> FakeHub:
    folders = {DATASET_REPO: tmp_path / "dataset", BASE_MODEL_REPO: tmp_path / "model"}
    return install_fake_hub(monkeypatch, folders)


def test_max_patches_caps_clips(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """The --max-patches flag reaches the sampler, so every clip ends after that many audio patches.

    Args:
        tmp_path: The test folder.
        capsys: Reads stdout.

    """
    write_voice_checkpoint(tmp_path / "checkpoints", FIRST_VOICE.name, build_lora_config(), 1)
    arguments = [
        "--checkpoints-folder",
        str(tmp_path / "checkpoints"),
        "--base-model-folder",
        str(write_base_model_folder(tmp_path / "base_model")),
        "--samples-folder",
        str(tmp_path / "samples"),
        "--max-patches",
        str(SHORT_MAX_PATCHES),
    ]

    with run_on_cpu():
        exit_code = infer.main(arguments)

    hop_length = int(build_tiny_model().audio_vae.hop_length)
    sample_paths = read_results(capsys)["sample"]
    assert exit_code == EXIT_SUCCESS
    assert sample_paths
    for sample_path in sample_paths:
        with wave.open(sample_path) as clip:
            assert clip.getnframes() == SHORT_MAX_PATCHES * PATCH_SIZE * hop_length


def test_dry_run_uploads_nothing(
    tmp_path: Path, capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    """A dry run stages the repository with its card and prints its folder, and uploads nothing despite a token.

    Args:
        tmp_path: Holds the run and the base model.
        capsys: Captures the result lines.
        monkeypatch: Replaces the Hub client and sets the token.

    """
    hub = _install_hub(monkeypatch, tmp_path)
    set_hf_token(monkeypatch)

    exit_code = publish.main([*_write_publish_inputs(tmp_path), "--dry-run"])

    results = read_results(capsys)
    assert exit_code == EXIT_SUCCESS
    assert list(results) == ["staging_folder"]
    assert (tmp_path / "run" / "staging" / CARD_FILE).is_file()
    assert hub.uploads == []


@pytest.mark.parametrize(
    ("flags", "created_repos"),
    [([], {OUTPUT_REPO: True}), (["--public"], {OUTPUT_REPO: False})],
    ids=["private", "public"],
)
def test_publish_uploads_staging(
    flags: list[str],
    created_repos: dict[str, bool],
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """With a token, the command creates a private repository unless --public, uploads one commit, and prints its URL.

    Args:
        flags: The visibility flags.
        created_repos: Whether the created repository is private.
        tmp_path: The test folder.
        capsys: Reads stdout.
        monkeypatch: Replaces the Hub client and sets the token.

    """
    hub = _install_hub(monkeypatch, tmp_path)
    set_hf_token(monkeypatch)

    exit_code = publish.main([*_write_publish_inputs(tmp_path), *flags])

    [upload] = hub.uploads
    assert exit_code == EXIT_SUCCESS
    assert hub.created_repos == created_repos
    assert (upload.repo_id, upload.commit_message) == (OUTPUT_REPO, PUBLISH_COMMIT_MESSAGE)
    assert CARD_FILE in upload.files
    assert read_results(capsys)["commit_url"] == [f"https://huggingface.co/{OUTPUT_REPO}/commit/fake"]


def test_train_needs_cuda(tmp_path: Path, capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch) -> None:
    """Training on a host without CUDA exits with code 1 and writes no checkpoint, though its inputs fit a CPU run.

    Args:
        tmp_path: Holds the inputs of a tiny run.
        capsys: Reads stdout.
        monkeypatch: Hides any CUDA GPU.

    """
    monkeypatch.setattr(torch.cuda, "is_available", lambda: False)
    arguments, voice_checkpoints_folder = write_train_flags(tmp_path, 1)

    with run_on_cpu():
        exit_code = train.main(arguments)

    assert exit_code == EXIT_FAILURE
    assert capsys.readouterr().out == ""
    assert not voice_checkpoints_folder.exists()


def test_stopped_training_exit_code(
    tmp_path: Path, capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    """SIGTERM mid-run ends training with 128 plus the signal number and prints the checkpoint of the last step.

    Args:
        tmp_path: Holds the inputs of a tiny run.
        capsys: Reads stdout.
        monkeypatch: Runs the command on the CPU and sends SIGTERM at the first logged step.

    """
    install_stopping_cpu_run(monkeypatch)
    arguments, voice_checkpoints_folder = write_train_flags(tmp_path, 2 * LOG_INTERVAL)

    with run_on_cpu():
        exit_code = train.main(arguments)

    stopped_folder = voice_checkpoints_folder / STEP_TEMPLATE.format(step=LOG_INTERVAL)
    assert exit_code == EXIT_SIGNAL_BASE + signal.SIGTERM
    assert read_results(capsys)["checkpoint_folder"] == [str(stopped_folder)]
    assert read_checkpoint_step(stopped_folder) == LOG_INTERVAL


def test_infer_without_checkpoints_fails(tmp_path: Path) -> None:
    """Sampling a run whose voices have no checkpoint exits with code 1 before it reads the base model.

    Args:
        tmp_path: The test folder, with an empty checkpoints folder.

    """
    (tmp_path / "checkpoints").mkdir()
    folders = [
        "--checkpoints-folder",
        str(tmp_path / "checkpoints"),
        "--base-model-folder",
        str(tmp_path / "base_model"),
    ]

    exit_code = infer.main([*folders, "--samples-folder", str(tmp_path / "samples")])

    assert exit_code == EXIT_FAILURE
    assert not (tmp_path / "samples").exists()


def test_publish_missing_samples_fails(tmp_path: Path) -> None:
    """A missing samples folder stops staging with exit code 1, and the command writes no model card.

    Args:
        tmp_path: Holds the run and the base model.

    """
    arguments = [*_write_publish_inputs(tmp_path), "--samples-folder", str(tmp_path / "missing"), "--dry-run"]

    exit_code = publish.main(arguments)

    assert exit_code == EXIT_FAILURE
    assert not (tmp_path / "run" / STAGING_FOLDER / CARD_FILE).exists()


def test_prepare_without_shards_fails(tmp_path: Path) -> None:
    """A dataset folder without shards stops preparation with exit code 1 before it writes any manifest.

    Args:
        tmp_path: The test folder.

    """
    (tmp_path / "dataset").mkdir()
    folders = ["--dataset-folder", str(tmp_path / "dataset"), "--base-model-folder", str(tmp_path / "base_model")]

    exit_code = prepare.main([*folders, "--run-folder", str(tmp_path / "run")])

    assert exit_code == EXIT_FAILURE
    assert not (tmp_path / "run").exists()


def test_unreachable_hub_fails_publish(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A Hub that refuses the upload fails the publish with exit code 1 instead of a traceback.

    Args:
        tmp_path: The test folder.
        monkeypatch: Makes the upload refuse the connection and sets the token.

    """
    hub = _install_hub(monkeypatch, tmp_path)
    monkeypatch.setattr(hub, "upload_folder", _refuse_connection)
    set_hf_token(monkeypatch)

    assert publish.main(_write_publish_inputs(tmp_path)) == 1

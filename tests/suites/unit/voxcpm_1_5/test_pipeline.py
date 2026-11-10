"""The pipeline runs the stages of a run in process, resumes a run, and deletes a run folder only with consent."""

from __future__ import annotations

import io
import sys
import signal
from typing import TYPE_CHECKING, NoReturn

import torch
import pytest
import huggingface_hub

from config.hub import CARD_FILE, DATASET_REPO
from config.shards import SHARD_GLOB
from src.train.cli import EXIT_USAGE, EXIT_FAILURE, EXIT_SUCCESS, EXIT_SIGNAL_BASE
from tests.harness.hub import install_fake_hub
from tests.harness.shards import write_shard, build_clip_members
from tests.harness.voices import FIRST_VOICE, TABLE_VOICES
from config.voxcpm_1_5.hub import SAMPLES_FOLDER, ADAPTERS_FOLDER, BASE_MODEL_REPO
from tests.harness.records import build_record
from config.voxcpm_1_5.data import MANIFESTS_FOLDER, TRAIN_MANIFEST_FILE
from config.voxcpm_1_5.samples import SAMPLE_PROMPTS
from tests.harness.checkpoints import TINY_LORA_RANK, TINY_BATCH_SIZE, TINY_LORA_ALPHA
from tests.harness.environment import set_hf_token
from config.voxcpm_1_5.training import LOG_INTERVAL
from tests.suites.unit.builders import TerminalStream
from config.voxcpm_1_5.checkpoints import STEP_PREFIX, STEP_TEMPLATE, CHECKPOINTS_FOLDER
from tests.suites.unit.voxcpm_1_5.builders import run_on_cpu, build_lora_config
from src.train.voxcpm_1_5.commands.pipeline import main
from tests.suites.unit.voxcpm_1_5.run_files import write_voice_checkpoint, write_base_model_folder
from tests.suites.unit.voxcpm_1_5.training_runs import install_stopping_cpu_run

if TYPE_CHECKING:
    from pathlib import Path

    from tests.harness.hub import FakeHub

RUN_NAME = "first-run"
OUTPUT_REPO = "owner/voice-adapters"
STALE_FILE = "stale.txt"


def _write_stale_run(tmp_path: Path) -> Path:
    stale_path = tmp_path / "runs" / RUN_NAME / STALE_FILE
    stale_path.parent.mkdir(parents=True)
    stale_path.write_text("from an earlier run", encoding="utf-8")
    return stale_path


def _build_arguments(tmp_path: Path, *flags: str) -> list[str]:
    return [
        "--run-name",
        RUN_NAME,
        "--runs-folder",
        str(tmp_path / "runs"),
        "--cache-folder",
        str(tmp_path / "cache"),
        "--output-repo",
        OUTPUT_REPO,
        *flags,
    ]


def _install_hub(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> FakeHub:
    dataset_folder = tmp_path / "dataset"
    records = {f"clip_{index}": build_record(voice) for index, voice in enumerate(TABLE_VOICES * 2)}
    write_shard(dataset_folder / SHARD_GLOB.replace("*", "000000"), build_clip_members(records))
    base_model_folder = write_base_model_folder(tmp_path / "model")
    return install_fake_hub(monkeypatch, {DATASET_REPO: dataset_folder, BASE_MODEL_REPO: base_model_folder})


def test_clean_needs_yes(tmp_path: Path, capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch) -> None:
    """Without a terminal to ask, --clean needs --yes, and the run folder stays.

    Args:
        tmp_path: The test folder.
        capsys: Reads stderr.
        monkeypatch: Replaces standard input.

    """
    stale_path = _write_stale_run(tmp_path)
    monkeypatch.setattr(sys, "stdin", io.StringIO())

    with pytest.raises(SystemExit) as exit_info:
        main(_build_arguments(tmp_path, "--clean"))

    assert exit_info.value.code == EXIT_USAGE
    assert "--yes" in capsys.readouterr().err
    assert stale_path.exists()


def test_declined_clean_keeps_run(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A person who answers no at the prompt keeps the run folder, and the run does not start.

    Args:
        tmp_path: The test folder.
        monkeypatch: Replaces standard input.

    """
    stale_path = _write_stale_run(tmp_path)
    hub = _install_hub(monkeypatch, tmp_path)
    monkeypatch.setattr(sys, "stdin", TerminalStream("n\n", is_terminal=True))

    assert main(_build_arguments(tmp_path, "--clean")) == 1
    assert stale_path.exists()
    assert hub.downloads == []


@pytest.mark.parametrize(
    ("answer", "flags"), [("y\n", ["--clean"]), ("", ["--clean", "--yes"])], ids=["answered-yes", "yes-flag"]
)
def test_confirmed_clean_deletes_run(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, answer: str, flags: list[str]
) -> None:
    """A yes at the prompt, or --yes without a terminal, deletes the run folder before the stages start.

    With no checkpoint left, sampling then fails.

    Args:
        tmp_path: The test folder.
        monkeypatch: Replaces standard input and the Hub client.
        answer: What the person types; a run with --yes has no terminal.
        flags: The clean flags.

    """
    stale_path = _write_stale_run(tmp_path)
    _install_hub(monkeypatch, tmp_path)
    monkeypatch.setattr(sys, "stdin", TerminalStream(answer, is_terminal=bool(answer)))

    with run_on_cpu():
        exit_code = main(_build_arguments(tmp_path, *flags, "--samples-only"))

    assert exit_code == EXIT_FAILURE
    assert not stale_path.exists()


def test_finished_voices_skipped(
    tmp_path: Path, capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    """A second run downloads and prepares again, skips each finished voice, and writes samples.

    Training needs CUDA, which the test hides, so the run succeeds only when no voice trains again.

    Args:
        tmp_path: The test folder.
        capsys: Reads stdout.
        monkeypatch: Replaces the Hub client and hides any CUDA GPU.

    """
    _install_hub(monkeypatch, tmp_path)
    monkeypatch.setattr(torch.cuda, "is_available", lambda: False)
    checkpoints_folder = tmp_path / "runs" / RUN_NAME / CHECKPOINTS_FOLDER
    for voice in TABLE_VOICES:
        write_voice_checkpoint(checkpoints_folder, voice.name, build_lora_config(), 1)

    with run_on_cpu():
        exit_code = main(_build_arguments(tmp_path, "--steps", "1"))

    sample_lines = [line for line in capsys.readouterr().out.splitlines() if line.startswith("sample=")]
    assert exit_code == EXIT_SUCCESS
    assert (checkpoints_folder.parent / MANIFESTS_FOLDER / TRAIN_MANIFEST_FILE).is_file()
    assert len(sample_lines) == len(TABLE_VOICES) * len(SAMPLE_PROMPTS)
    assert len(list(checkpoints_folder.glob(f"*/{STEP_PREFIX}*"))) == len(TABLE_VOICES)


def test_samples_only_publishes(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A samples-only run with --publish downloads only the base model, writes samples, and uploads the repository.

    Args:
        tmp_path: The test folder.
        monkeypatch: Replaces the Hub client and sets the token.

    """
    hub = _install_hub(monkeypatch, tmp_path)
    set_hf_token(monkeypatch)
    checkpoints_folder = tmp_path / "runs" / RUN_NAME / CHECKPOINTS_FOLDER
    write_voice_checkpoint(checkpoints_folder, FIRST_VOICE.name, build_lora_config(), 1)

    with run_on_cpu():
        exit_code = main(_build_arguments(tmp_path, "--samples-only", "--publish"))

    [upload] = hub.uploads
    assert exit_code == EXIT_SUCCESS
    assert [download.repo_id for download in hub.downloads] == [BASE_MODEL_REPO]
    assert upload.repo_id == OUTPUT_REPO
    assert {CARD_FILE, f"{ADAPTERS_FOLDER}/{FIRST_VOICE.name}/lora_weights.safetensors"} <= set(upload.files)
    assert sum(path.startswith(f"{SAMPLES_FOLDER}/") for path in upload.files) == len(SAMPLE_PROMPTS)


def test_stop_signal_ends_pipeline(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """SIGTERM while a voice trains ends the run with 128 plus the signal number after that voice's checkpoint.

    The next voice does not train, and the run writes no samples.

    Args:
        tmp_path: The test folder.
        monkeypatch: Replaces the Hub client, runs training on the CPU, and sends SIGTERM at the first logged step.

    """
    _install_hub(monkeypatch, tmp_path)
    install_stopping_cpu_run(monkeypatch)
    training_flags = ["--steps", str(2 * LOG_INTERVAL), "--batch-size", str(TINY_BATCH_SIZE)]
    lora_flags = ["--lora-rank", str(TINY_LORA_RANK), "--lora-alpha", str(TINY_LORA_ALPHA)]

    with run_on_cpu():
        exit_code = main(_build_arguments(tmp_path, *training_flags, *lora_flags))

    run_folder = tmp_path / "runs" / RUN_NAME
    first_folder, second_folder = (run_folder / CHECKPOINTS_FOLDER / voice.name for voice in TABLE_VOICES[:2])
    assert exit_code == EXIT_SIGNAL_BASE + signal.SIGTERM
    assert [path.name for path in first_folder.glob(f"{STEP_PREFIX}*")] == [STEP_TEMPLATE.format(step=LOG_INTERVAL)]
    assert not second_folder.exists()
    assert not (run_folder / SAMPLES_FOLDER).exists()


def test_interrupt_outside_training(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Control+C during the download ends the run with 128 plus SIGINT instead of a traceback.

    Args:
        tmp_path: The test folder.
        monkeypatch: Makes the Hub download stop as Control+C stops it.

    """

    def interrupt_download(repo_id: str, **_options: object) -> NoReturn:
        """Stop the download as Control+C does.

        Args:
            repo_id: The repository, which the fake ignores.
            **_options: Other options of the real call, which the fake ignores.

        Raises:
            KeyboardInterrupt: Always.

        """
        del repo_id
        raise KeyboardInterrupt

    monkeypatch.setattr(huggingface_hub, "snapshot_download", interrupt_download)

    assert main(_build_arguments(tmp_path)) == EXIT_SIGNAL_BASE + signal.SIGINT

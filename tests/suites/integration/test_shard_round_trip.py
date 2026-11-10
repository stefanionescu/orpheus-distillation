"""The training command reads the shards that the dataset command writes; the record is their contract."""

from __future__ import annotations

import math
from typing import TYPE_CHECKING
from pathlib import Path

from config.audio import SAMPLE_RATE
from src.train.cli import EXIT_SUCCESS
from tests.harness.voices import FIRST_VOICE, SECOND_VOICE, TABLE_VOICES
from tests.harness.records import build_record
from config.voxcpm_1_5.data import TOKENIZER_FILES
from config.voxcpm_1_5.model import MODEL_SAMPLE_RATE
from tests.harness.checkpoints import write_tokenizer_files
from src.train.voxcpm_1_5.commands import prepare
from tests.suites.integration.builders import write_dataset
from src.train.voxcpm_1_5.data.manifest import write_manifests, read_voice_entries
from src.train.voxcpm_1_5.training.dataset import ManifestDataset

if TYPE_CHECKING:
    import pytest

    from schemas.record import Record
    from schemas.voxcpm_1_5.manifest import ManifestEntry

SMALL_CLIPS_PER_SHARD = 3
"""Below the clip count, so the dataset spans two shards and the reader reads both."""

RECORDS = {
    "clip_00000": build_record(FIRST_VOICE, text="The first clip.", duration=1.0),
    "clip_00001": build_record(SECOND_VOICE, text="The second clip.", duration=1.5),
    "clip_00002": build_record(FIRST_VOICE, text="The third clip.", duration=0.75),
    "clip_00003": build_record(SECOND_VOICE, text="The fourth clip.", duration=2.0),
}
KEPT_KEY = "clip_00000"
UNICODE_TEXT = "Café déjà vu, naïve — ¿qué tal? Ça va!"


def _read_entries(manifest_path: Path) -> list[ManifestEntry]:
    return [entry for voice in TABLE_VOICES for entry in read_voice_entries(manifest_path, voice.name)]


def _write_manifests(tmp_path: Path, records: dict[str, Record]) -> list[ManifestEntry]:
    write_dataset(tmp_path / "dataset", records, SMALL_CLIPS_PER_SHARD)
    return _read_entries(write_manifests(tmp_path / "dataset", tmp_path / "manifests", 0.0).train_manifest_path)


def test_kept_clips_keep_record(tmp_path: Path) -> None:
    """Each clip of every shard becomes an entry of its voice with its record's text, length, and WAV.

    Args:
        tmp_path: The test folder.

    """
    clips = write_dataset(tmp_path / "dataset", RECORDS, SMALL_CLIPS_PER_SHARD)

    files = write_manifests(tmp_path / "dataset", tmp_path / "manifests", 0.0)

    expected = [
        (voice.name, clip.record.text, clip.record.duration, clip.audio_path.read_bytes())
        for voice in TABLE_VOICES
        for clip in clips
        if clip.record.voice == voice.name
    ]
    entries = _read_entries(files.train_manifest_path)
    assert [(entry.voice, entry.text, entry.duration, Path(entry.audio).read_bytes()) for entry in entries] == expected


def test_training_reads_clip_audio(tmp_path: Path) -> None:
    """The training dataset decodes each extracted WAV at the model sample rate, with its record's length.

    Args:
        tmp_path: The test folder.

    """
    entries = _write_manifests(tmp_path, RECORDS)

    dataset = ManifestDataset(entries, [[0]] * len(entries), MODEL_SAMPLE_RATE)

    lengths = [dataset[index].waveform.numel() for index in range(len(dataset))]
    assert lengths == [
        math.ceil(round(entry.duration * SAMPLE_RATE) * MODEL_SAMPLE_RATE / SAMPLE_RATE) for entry in entries
    ]


def test_unicode_text_kept(tmp_path: Path) -> None:
    """Non-ASCII text reaches the manifest unchanged, so a voice reads the prompt the server read.

    Args:
        tmp_path: The test folder.

    """
    [entry] = _write_manifests(tmp_path, {KEPT_KEY: build_record(FIRST_VOICE, text=UNICODE_TEXT)})

    assert entry.text == UNICODE_TEXT


def test_prepare_prints_training_inputs(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """The prepare command prints the manifests and the tokenizer folder that training reads, each clip in one manifest.

    Args:
        tmp_path: The test folder.
        capsys: Reads the result lines.

    """
    write_dataset(tmp_path / "dataset", RECORDS, SMALL_CLIPS_PER_SHARD)
    base_model_folder = write_tokenizer_files(tmp_path / "model")
    flags = [
        "--dataset-folder",
        str(tmp_path / "dataset"),
        "--base-model-folder",
        str(base_model_folder),
        "--val-split",
        "0.5",
    ]

    exit_code = prepare.main([*flags, "--run-folder", str(tmp_path / "run")])

    results = dict(line.split("=", 1) for line in capsys.readouterr().out.splitlines())
    texts = [entry.text for key in ("train_manifest", "val_manifest") for entry in _read_entries(Path(results[key]))]
    assert exit_code == EXIT_SUCCESS
    assert sorted(texts) == sorted(record.text for record in RECORDS.values())
    assert sorted(path.name for path in Path(results["tokenizer_folder"]).iterdir()) == sorted(TOKENIZER_FILES)

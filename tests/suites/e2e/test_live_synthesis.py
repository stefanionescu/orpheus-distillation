"""The dataset command against the live Orpheus server writes clips that the training command keeps."""

from __future__ import annotations

from typing import TYPE_CHECKING

from src.dataset.prompts import list_corpus_prompts
from src.dataset.cli.main import main
from tests.harness.voices import TABLE_VOICES
from src.dataset.audio.wav import read_wav
from src.dataset.audio.silence import detect_leading_silence_ms
from src.dataset.cli.arguments import EXIT_SUCCESS
from tests.suites.e2e.builders import LIVE_PROMPT_COUNT, LEADING_SILENCE_MARGIN_MS, read_live_server
from src.dataset.generation.tasks import build_tasks, build_output_folders
from src.train.voxcpm_1_5.data.manifest import write_manifests, read_voice_entries

if TYPE_CHECKING:
    from pathlib import Path


def test_live_clips_fit_training(tmp_path: Path) -> None:
    """Each live prompt and voice gives a clip that starts near the voice's pad, and training keeps every clip.

    The training command reads the run's shards and keeps a clip only when its speaker, text, and length pass its
    filters, so a manifest entry per clip proves that the live clips fit training.

    Args:
        tmp_path: The test folder.

    """
    server = read_live_server()
    folders = build_output_folders(tmp_path / "output")
    flags = ["--server", server.url, "--api-key", server.api_key, "--max-prompts", str(LIVE_PROMPT_COUNT)]

    exit_code = main([*flags, "--output-folder", str(folders.root)])

    assert exit_code == EXIT_SUCCESS
    tasks, _ = build_tasks(list_corpus_prompts()[:LIVE_PROMPT_COUNT], TABLE_VOICES, folders.audio_folder, set())
    manifest_path = write_manifests(folders.root, tmp_path / "manifests", 0.0).train_manifest_path
    entries = [entry for voice in TABLE_VOICES for entry in read_voice_entries(manifest_path, voice.name)]
    expected = [(task.voice.name, task.prompt) for task in tasks]
    assert sorted((entry.voice, entry.text) for entry in entries) == sorted(expected)
    for task in tasks:
        audio = read_wav(task.audio_path)
        silence_limit_ms = task.voice.prespeech_pad_ms + LEADING_SILENCE_MARGIN_MS
        assert detect_leading_silence_ms(audio.frames, audio.sample_rate) <= silence_limit_ms

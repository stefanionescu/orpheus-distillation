"""Training estimates each clip's packed length from its manifest entry and drops clips over budget."""

from __future__ import annotations

from typing import TYPE_CHECKING

from tests.harness.voices import FIRST_VOICE, SECOND_VOICE
from tests.harness.manifests import write_clip_manifest
from config.models.voxcpm_1_5.data import TRAIN_MANIFEST_FILE
from src.train.models.voxcpm_1_5.training.dataset import read_training_dataset, build_sequence_lengths
from tests.suites.unit.models.voxcpm_1_5.builders import MODEL_SAMPLE_RATE, build_tiny_model

if TYPE_CHECKING:
    from pathlib import Path

SHORT_SECONDS = 0.01
LONG_SECONDS = 0.1
# The budget fits the text and a short clip, but not a long clip.
TOKEN_BUDGET = 64


def test_lengths_count_patches() -> None:
    """A clip takes its text tokens, one position per started patch, and the start and end tokens."""
    assert build_sequence_lengths([3, 10], [1.0, 0.01], 25.0, 2) == [3 + 13 + 2, 10 + 1 + 2]


def test_budget_drops_long_clip(tmp_path: Path) -> None:
    """A clip over the token budget leaves the dataset, and so does every clip of the other voice.

    Args:
        tmp_path: The test folder.

    """
    manifest_path = tmp_path / TRAIN_MANIFEST_FILE
    clips = [(FIRST_VOICE, LONG_SECONDS), (FIRST_VOICE, SHORT_SECONDS), (SECOND_VOICE, SHORT_SECONDS)]
    write_clip_manifest(manifest_path, clips, MODEL_SAMPLE_RATE)

    dataset = read_training_dataset(manifest_path, FIRST_VOICE.name, build_tiny_model(), TOKEN_BUDGET)

    assert len(dataset) == 1
    assert dataset[0].waveform.shape == (round(SHORT_SECONDS * MODEL_SAMPLE_RATE),)

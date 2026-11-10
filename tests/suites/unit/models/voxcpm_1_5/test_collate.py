"""The loader collates clips of different lengths into one padded batch."""

from __future__ import annotations

import torch

from config.models.voxcpm_1_5.model import PAD_TOKEN_ID
from schemas.models.voxcpm_1_5.training import TrainingClip
from src.train.models.voxcpm_1_5.training.dataset import collate_batch
from tests.suites.unit.models.voxcpm_1_5.builders import to_list


def test_collate_pads_to_longest() -> None:
    """Text and audio pad with the pad token id to the longest clip, so the packer can cut them back."""
    short = TrainingClip(text_tokens=torch.tensor([3], dtype=torch.int32), waveform=torch.tensor([0.5]))
    long = TrainingClip(text_tokens=torch.tensor([4, 5], dtype=torch.int32), waveform=torch.tensor([0.1, 0.2, 0.3]))

    batch = collate_batch([short, long])

    assert to_list(batch.text_tokens) == [[3, PAD_TOKEN_ID], [4, 5]]
    assert to_list(batch.waveforms[0]) == [0.5, PAD_TOKEN_ID, PAD_TOKEN_ID]

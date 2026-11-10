"""The batch packer lays out each clip as text, the audio start token, audio patches, and the audio end token."""

from __future__ import annotations

import torch
import pytest

from config.models.voxcpm_1_5.model import PAD_TOKEN_ID
from schemas.models.voxcpm_1_5.training import CollatedBatch
from src.train.models.voxcpm_1_5.model.forward import LOSS_DIFF_KEY, LOSS_STOP_KEY
from src.train.models.voxcpm_1_5.training.batch import build_total_loss, build_batch_packer
from tests.suites.unit.models.voxcpm_1_5.builders import (
    MAX_LENGTH,
    AUDIO_END_TOKEN,
    AUDIO_START_TOKEN,
    to_list,
    build_tiny_model,
)

CPU = torch.device("cpu")
# The patch counts follow from the waveform lengths, the audio VAE hop, and PATCH_SIZE.
FIRST_PATCHES = 5
SECOND_PATCHES = 3
DIFF_LOSS = 2.0
STOP_LOSS = 3.0
DIFF_WEIGHT = 0.5
STOP_WEIGHT = 2.0
LONG_TEXT_TOKENS = MAX_LENGTH - 4
# Ten audio patches, which push the packed clip past the model's maximum length.
LONG_WAVEFORM_SAMPLES = 80


def _build_batch() -> CollatedBatch:
    generator = torch.Generator().manual_seed(7)
    first_waveform = torch.rand(37, generator=generator) - 0.5
    second_waveform = torch.cat([torch.rand(20, generator=generator) - 0.5, torch.full((17,), float(PAD_TOKEN_ID))])
    return CollatedBatch(
        text_tokens=torch.tensor([[11, 8, PAD_TOKEN_ID], [26, 18, 5]], dtype=torch.int32),
        waveforms=torch.stack([first_waveform, second_waveform]),
    )


def test_clip_layout_order() -> None:
    """Text and the start token come first, then the audio patches, then the end token."""
    packed = build_batch_packer(build_tiny_model(), CPU)(_build_batch())

    audio_positions = [0, 0, 0] + [1] * FIRST_PATCHES + [0]
    tokens = [11, 8, AUDIO_START_TOKEN] + [0] * FIRST_PATCHES + [AUDIO_END_TOKEN]
    assert to_list(packed.text_tokens[0]) == tokens
    assert to_list(packed.audio_mask[0]) == audio_positions
    assert to_list(packed.text_mask[0]) == [1 - position for position in audio_positions]
    assert to_list(packed.loss_mask[0]) == audio_positions
    assert packed.audio_feats[0, 3:-1].abs().sum() > 0
    assert packed.audio_feats[0, :3].abs().sum() == 0


def test_stop_label_before_end() -> None:
    """Each clip's stop label sits on its last audio patch, one position before its end token."""
    packed = build_batch_packer(build_tiny_model(), CPU)(_build_batch())

    first_stop = 3 + FIRST_PATCHES - 1
    second_stop = 4 + SECOND_PATCHES - 1
    assert to_list(packed.labels.nonzero()) == [[0, first_stop], [1, second_stop]]


def test_batch_pads_to_longest() -> None:
    """The shorter clip pads to the longer one, and its positions stop at its own length."""
    packed = build_batch_packer(build_tiny_model(), CPU)(_build_batch())

    first_length = 3 + FIRST_PATCHES + 1
    second_length = 4 + SECOND_PATCHES + 1
    assert packed.text_tokens.shape == (2, first_length)
    padding = [0] * (first_length - second_length)
    assert to_list(packed.position_ids[1]) == list(range(second_length)) + padding


def test_long_clip_truncated() -> None:
    """A clip longer than the model reads is cut to the maximum length, and the batch is that long."""
    long_text = torch.arange(1, LONG_TEXT_TOKENS + 1, dtype=torch.int32)
    short_text = torch.full((LONG_TEXT_TOKENS,), PAD_TOKEN_ID, dtype=torch.int32)
    short_text[0] = 5
    batch = CollatedBatch(
        text_tokens=torch.stack([long_text, short_text]), waveforms=torch.full((2, LONG_WAVEFORM_SAMPLES), 0.1)
    )

    packed = build_batch_packer(build_tiny_model(), CPU)(batch)

    assert packed.text_tokens.shape == (2, MAX_LENGTH)
    assert to_list(packed.text_tokens[0, :LONG_TEXT_TOKENS]) == to_list(long_text)
    assert to_list(packed.position_ids[0]) == list(range(MAX_LENGTH))


def test_total_loss_weights() -> None:
    """The total loss weights the diffusion and stop losses, and the metrics keep both unweighted."""
    outputs = {LOSS_DIFF_KEY: torch.tensor(DIFF_LOSS), LOSS_STOP_KEY: torch.tensor(STOP_LOSS)}

    total, losses = build_total_loss(outputs, DIFF_WEIGHT, STOP_WEIGHT)

    assert total.item() == DIFF_WEIGHT * DIFF_LOSS + STOP_WEIGHT * STOP_LOSS
    assert losses == {LOSS_DIFF_KEY: DIFF_LOSS, LOSS_STOP_KEY: STOP_LOSS}


def test_missing_loss_raises() -> None:
    """A forward pass without the stop loss cannot train, so the step stops with an error."""
    with pytest.raises(ValueError, match=LOSS_STOP_KEY):
        build_total_loss({LOSS_DIFF_KEY: torch.tensor(2.0), LOSS_STOP_KEY: None}, 1.0, 1.0)

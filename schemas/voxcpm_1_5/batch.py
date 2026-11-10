"""The batch that one training step passes to the model."""

from __future__ import annotations

from typing import TYPE_CHECKING
from dataclasses import dataclass

if TYPE_CHECKING:
    import torch


@dataclass(frozen=True)
class PackedBatch:
    """Padded tensors of one training step, in the layout that the forward pass reads.

    Attributes:
        text_tokens: Text token ids of each clip.
        audio_feats: Audio features of each clip, grouped into patches.
        text_mask: Positions that hold text tokens.
        audio_mask: Positions that hold audio features.
        loss_mask: Positions that count toward the loss.
        position_ids: Position of each token in its clip.
        labels: Stop labels, set where the model learns to stop.

    """

    text_tokens: torch.Tensor
    audio_feats: torch.Tensor
    text_mask: torch.Tensor
    audio_mask: torch.Tensor
    loss_mask: torch.Tensor
    position_ids: torch.Tensor
    labels: torch.Tensor

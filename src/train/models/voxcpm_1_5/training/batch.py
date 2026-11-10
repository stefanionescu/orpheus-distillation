"""Packing of collated clips into training sequences: text, then audio patches, then an end token."""

from __future__ import annotations

from typing import TYPE_CHECKING
from dataclasses import dataclass

import torch
from torch.nn import functional

from config.models.voxcpm_1_5.model import PAD_TOKEN_ID, STOP_LABEL_VALUE, STOP_LABEL_POSITION
from schemas.models.voxcpm_1_5.batch import PackedBatch
from schemas.models.voxcpm_1_5.training import PackingLayout
from src.train.models.voxcpm_1_5.model.base import AUDIO_END_TOKEN, AUDIO_START_TOKEN
from src.train.models.voxcpm_1_5.model.forward import LOSS_DIFF_KEY, LOSS_STOP_KEY

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence

    from schemas.models.voxcpm_1_5.training import CollatedBatch
    from src.train.models.voxcpm_1_5.model.voxcpm import VoxCPMModel
    from src.train.models.voxcpm_1_5.model.modules.audiovae.audiovae import AudioVae


@dataclass(frozen=True)
class _PackedClip:
    text_tokens: torch.Tensor
    audio_feats: torch.Tensor
    text_mask: torch.Tensor
    audio_mask: torch.Tensor
    labels: torch.Tensor


def remove_padding(tensor: torch.Tensor, pad_value: int = PAD_TOKEN_ID) -> torch.Tensor:
    """Cut a collated row at its first pad value.

    Args:
        tensor: One row of a collated batch.
        pad_value: Value that `collate_batch` pads with.

    Returns:
        The row up to its first pad value, or the whole row.

    """
    pad_positions = (tensor == pad_value).nonzero()
    if pad_positions.numel() == 0:
        return tensor
    return tensor[: int(pad_positions[0, 0])]


def pad_to_length(tensor: torch.Tensor, length: int) -> torch.Tensor:
    """Pad a sequence with zeros, or cut it, to a length along its first dimension.

    Args:
        tensor: Sequence with positions along the first dimension.
        length: Positions of the result.

    Returns:
        The sequence with exactly `length` positions.

    """
    if tensor.shape[0] >= length:
        return tensor[:length]
    padding = torch.zeros((length - tensor.shape[0], *tensor.shape[1:]), dtype=tensor.dtype, device=tensor.device)
    return torch.cat([tensor, padding])


def build_position_ids(lengths: Sequence[int], length: int, device: torch.device) -> torch.Tensor:
    """Build the position of each token in its clip, with zeros past the end of each clip.

    Args:
        lengths: Positions of each clip before padding.
        length: Positions of the batch, which cuts longer clips.
        device: Device of the result.

    Returns:
        Positions, shaped (clips, length).

    """
    positions = torch.arange(length, device=device).expand(len(lengths), length)
    limits = torch.tensor(lengths, device=device).clamp(max=length).unsqueeze(1)
    return torch.where(positions < limits, positions, torch.zeros_like(positions))


def encode_audio(audio_vae: AudioVae, waveform: torch.Tensor, patch_size: int) -> torch.Tensor:
    """Encode a waveform into audio feature patches with the frozen audio VAE.

    Args:
        audio_vae: Audio VAE of the model.
        waveform: Mono audio at the VAE sample rate, shaped (samples,).
        patch_size: VAE frames per patch.

    Returns:
        Patches, shaped (1, patches, patch_size, latent_dim). The call pads the waveform with silence to whole patches.

    """
    patch_samples = int(audio_vae.hop_length) * patch_size
    audio = waveform.reshape(1, 1, -1)
    padding = -audio.shape[-1] % patch_samples
    audio = functional.pad(audio, (0, padding))
    with torch.no_grad():
        latents = audio_vae.encode(audio, audio_vae.sample_rate)
    return latents.transpose(1, 2).reshape(1, -1, patch_size, latents.shape[1])


def build_total_loss(
    outputs: Mapping[str, torch.Tensor | None], diff_weight: float, stop_weight: float
) -> tuple[torch.Tensor, dict[str, float]]:
    """Sum the weighted diffusion and stop losses of one forward pass.

    Args:
        outputs: Forward pass outputs.
        diff_weight: Diffusion loss weight.
        stop_weight: Stop loss weight.

    Returns:
        The total loss to back-propagate, and the value of each loss.

    Raises:
        ValueError: The outputs lack one of the two losses.

    """
    diff_loss = outputs.get(LOSS_DIFF_KEY)
    stop_loss = outputs.get(LOSS_STOP_KEY)
    if diff_loss is None or stop_loss is None:
        message = f"The forward pass returned no {LOSS_DIFF_KEY} or no {LOSS_STOP_KEY}"
        raise ValueError(message)
    total = diff_weight * diff_loss + stop_weight * stop_loss
    return total, {LOSS_DIFF_KEY: diff_loss.item(), LOSS_STOP_KEY: stop_loss.item()}


class BatchPacker:
    """Turns collated batches into the packed batches that the model trains on."""

    def __init__(self, audio_vae: AudioVae, layout: PackingLayout, device: torch.device) -> None:
        """Move the audio VAE to the device of the batches.

        Args:
            audio_vae: Frozen audio VAE that encodes the waveforms.
            layout: Model facts that decide the packing.
            device: Device of the packed batches.

        """
        self._audio_vae = audio_vae.to(device)
        self._layout = layout
        self._device = device

    def __call__(self, batch: CollatedBatch) -> PackedBatch:
        """Pack each clip, then pad all to the longest, capped at the model maximum length.

        Args:
            batch: Collated clips.

        Returns:
            The packed batch on the device.

        """
        clips = [
            self._pack_clip(remove_padding(text).to(self._device), remove_padding(waveform).to(self._device))
            for text, waveform in zip(batch.text_tokens, batch.waveforms, strict=True)
        ]
        lengths = [clip.text_tokens.shape[0] for clip in clips]
        length = min(self._layout.max_length, max(lengths))
        audio_mask = torch.stack([pad_to_length(clip.audio_mask, length) for clip in clips])
        return PackedBatch(
            text_tokens=torch.stack([pad_to_length(clip.text_tokens, length) for clip in clips]),
            audio_feats=torch.stack([pad_to_length(clip.audio_feats, length) for clip in clips]),
            text_mask=torch.stack([pad_to_length(clip.text_mask, length) for clip in clips]),
            audio_mask=audio_mask,
            # No clip carries prompt audio, so the loss covers every audio position.
            loss_mask=audio_mask,
            position_ids=build_position_ids(lengths, length, self._device),
            labels=torch.stack([pad_to_length(clip.labels, length) for clip in clips]),
        )

    def _pack_clip(self, text: torch.Tensor, waveform: torch.Tensor) -> _PackedClip:
        layout = self._layout
        features = encode_audio(self._audio_vae, waveform.float(), layout.patch_size).squeeze(0)
        prefix_length = text.shape[0] + 1
        audio_length = features.shape[0]
        is_audio = torch.cat(
            [
                torch.zeros(prefix_length, dtype=torch.int32),
                torch.ones(audio_length, dtype=torch.int32),
                torch.zeros(1, dtype=torch.int32),
            ]
        ).to(self._device)
        tokens = torch.zeros(prefix_length + audio_length + 1, dtype=torch.int32, device=self._device)
        tokens[: text.shape[0]] = text
        tokens[text.shape[0]] = layout.audio_start_token
        tokens[-1] = layout.audio_end_token
        labels = torch.zeros_like(tokens)
        # The stop head learns to fire one position before the end token.
        labels[STOP_LABEL_POSITION] = STOP_LABEL_VALUE
        silence = torch.zeros((1, *features.shape[1:]), dtype=features.dtype, device=self._device)
        return _PackedClip(
            text_tokens=tokens,
            audio_feats=torch.cat([silence.expand(prefix_length, -1, -1), features, silence]),
            text_mask=1 - is_audio,
            audio_mask=is_audio,
            labels=labels,
        )


def build_batch_packer(model: VoxCPMModel, device: torch.device) -> BatchPacker:
    """Build the batch packer of a loaded model.

    Args:
        model: Model whose config, audio VAE, and audio tokens decide the packing.
        device: Device of the packed batches.

    Returns:
        The packer.

    """
    layout = PackingLayout(
        max_length=model.config.max_length,
        patch_size=model.config.patch_size,
        audio_start_token=AUDIO_START_TOKEN,
        audio_end_token=AUDIO_END_TOKEN,
    )
    return BatchPacker(model.audio_vae, layout, device)

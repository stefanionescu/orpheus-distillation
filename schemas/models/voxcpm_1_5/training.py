"""Records of one training run."""

from __future__ import annotations

from typing import TYPE_CHECKING
from dataclasses import dataclass

if TYPE_CHECKING:
    from pathlib import Path

    import torch


@dataclass(frozen=True)
class TrainingFolders:
    """The files that one training run reads and the folders that it writes.

    Attributes:
        base_model_folder: Downloaded base model.
        train_manifest_path: Training manifest.
        val_manifest_path: Validation manifest, or None to skip validation.
        tokenizer_folder: Tokenizer files that each checkpoint copies.
        voice_checkpoints_folder: Where the checkpoints of the voice go, inside the checkpoints folder of the run.
        voice_events_folder: Where the TensorBoard events of the voice go, inside the events folder of the run.

    """

    base_model_folder: Path
    train_manifest_path: Path
    val_manifest_path: Path | None
    tokenizer_folder: Path
    voice_checkpoints_folder: Path
    voice_events_folder: Path


@dataclass(frozen=True)
class TrainingSettings:
    """Resolved settings of one training run of one voice.

    Attributes:
        voice: Voice whose adapter trains.
        folders: Files and folders of the run.
        batch_size: Clips per micro-batch.
        accumulation_steps: Micro-batches per optimizer step.
        loader_workers: Loader worker processes.
        steps: Optimizer steps of the voice.
        learning_rate: Peak learning rate.
        weight_decay: Optimizer weight decay.
        warmup_steps: Steps over which the learning rate rises.
        max_batch_tokens: Token budget of one batch. The run drops a clip longer than this budget over the batch size.
        log_interval: Steps between metric lines.
        val_interval: Steps between validation passes.
        checkpoint_interval: Steps between checkpoints.
        loss_diff_weight: Weight of the diffusion loss.
        loss_stop_weight: Weight of the stop loss.

    """

    voice: str
    folders: TrainingFolders
    batch_size: int
    accumulation_steps: int
    loader_workers: int
    steps: int
    learning_rate: float
    weight_decay: float
    warmup_steps: int
    max_batch_tokens: int
    log_interval: int
    val_interval: int
    checkpoint_interval: int
    loss_diff_weight: float
    loss_stop_weight: float


@dataclass(frozen=True)
class LoraSettings:
    """LoRA settings of one training run.

    Attributes:
        enable_lm: Whether the adapter covers the language model layers.
        enable_dit: Whether the adapter covers the diffusion transformer layers.
        enable_proj: Whether the adapter covers the projection layers.
        rank: Rank of the low-rank matrices.
        alpha: Scaling factor of the adapter output.
        dropout: Dropout rate of the adapter input.
        target_modules: Linear layers that the adapter wraps.

    """

    enable_lm: bool
    enable_dit: bool
    enable_proj: bool
    rank: int
    alpha: int
    dropout: float
    target_modules: tuple[str, ...]


@dataclass(frozen=True)
class TrainingResult:
    """What one training run leaves behind.

    Attributes:
        checkpoint_folder: Last checkpoint written, which the newest link points to.
        stop_signal: Signal that stopped the run early, or None when the run took every step.

    """

    checkpoint_folder: Path
    stop_signal: int | None


@dataclass(frozen=True)
class TrainingClip:
    """One manifest clip as the loader yields it.

    Attributes:
        text_tokens: Text token ids, shaped (tokens,).
        waveform: Mono audio at the model sample rate, shaped (samples,).

    """

    text_tokens: torch.Tensor
    waveform: torch.Tensor


@dataclass(frozen=True)
class CollatedBatch:
    """One micro-batch, each clip padded with the pad token id to the longest.

    Attributes:
        text_tokens: Token ids, shaped (batch, tokens).
        waveforms: Audio, shaped (batch, samples).

    """

    text_tokens: torch.Tensor
    waveforms: torch.Tensor


@dataclass(frozen=True)
class PackingLayout:
    """Facts of the loaded model that decide the batch packing.

    Attributes:
        max_length: Longest sequence that the model reads, in positions.
        patch_size: Audio frames per position.
        audio_start_token: Token id that ends the text and starts the audio.
        audio_end_token: Token id that ends the audio.

    """

    max_length: int
    patch_size: int
    audio_start_token: int
    audio_end_token: int

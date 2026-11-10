"""The dataset of one voice and its loaders."""

from __future__ import annotations

import math
import signal
from typing import TYPE_CHECKING, cast, override
import logging
from pathlib import Path
import functools
from collections.abc import Sized

import torch
import soundfile
from torch.utils.data import Dataset, DataLoader
from torch.nn.utils.rnn import pad_sequence
import torchaudio.functional
from torch.utils.data.distributed import DistributedSampler

from config.models.voxcpm_1_5.model import PAD_TOKEN_ID
from schemas.models.voxcpm_1_5.training import TrainingClip, CollatedBatch
from src.train.models.voxcpm_1_5.data.manifest import read_voice_entries
from src.train.models.voxcpm_1_5.training.loop import set_stop_action

if TYPE_CHECKING:
    from collections.abc import Callable, Sequence

    import numpy as np
    from numpy.typing import NDArray

    from schemas.models.voxcpm_1_5.manifest import ManifestEntry
    from schemas.models.voxcpm_1_5.training import TrainingSettings
    from src.train.models.voxcpm_1_5.model.voxcpm import VoxCPMModel
    from src.train.models.voxcpm_1_5.training.accelerator import Accelerator

# The audio start and end tokens take one position each.
AUDIO_MARKER_POSITIONS = 2

logger = logging.getLogger(__name__)


def _read_waveform(audio_path: Path, sample_rate: int) -> torch.Tensor:
    read_audio = cast("Callable[..., tuple[NDArray[np.float32], int]]", soundfile.read)
    frames, file_sample_rate = read_audio(audio_path, dtype="float32", always_2d=True)
    waveform = torch.tensor(frames.mean(axis=1), dtype=torch.float32)
    if file_sample_rate == sample_rate:
        return waveform
    return torchaudio.functional.resample(waveform, file_sample_rate, sample_rate)


class ManifestDataset(Dataset[TrainingClip], Sized):
    """Clips of one voice. Indexing reads the WAV file as mono at the model sample rate."""

    def __init__(
        self, entries: Sequence[ManifestEntry], text_tokens: Sequence[Sequence[int]], sample_rate: int
    ) -> None:
        """Hold the entries and the token ids of their texts.

        Args:
            entries: Manifest entries.
            text_tokens: Token ids of each entry text, in the same order.
            sample_rate: Model sample rate in hertz.

        Raises:
            ValueError: The two sequences differ in length.

        """
        if len(entries) != len(text_tokens):
            message = "Each manifest entry needs the token ids of its text"
            raise ValueError(message)
        self._audio_paths = [Path(entry.audio) for entry in entries]
        self._text_tokens = [list(tokens) for tokens in text_tokens]
        self._sample_rate = sample_rate

    @override
    def __len__(self) -> int:
        return len(self._audio_paths)

    @override
    def __getitem__(self, index: int) -> TrainingClip:
        waveform = _read_waveform(self._audio_paths[index], self._sample_rate)
        return TrainingClip(text_tokens=torch.tensor(self._text_tokens[index], dtype=torch.int32), waveform=waveform)


def build_sequence_lengths(
    text_lengths: Sequence[int], durations: Sequence[float], frame_rate: float, patch_size: int
) -> list[int]:
    """Compute the packed length of each clip from its token count and duration, without reading its audio.

    Args:
        text_lengths: Text token count of each clip.
        durations: Length of each clip in seconds.
        frame_rate: Audio VAE frames per second.
        patch_size: VAE frames per patch.

    Returns:
        Positions that each clip takes in a packed batch.

    """
    lengths: list[int] = []
    for text_length, duration in zip(text_lengths, durations, strict=True):
        patches = math.ceil(math.ceil(duration * frame_rate) / patch_size)
        lengths.append(text_length + patches + AUDIO_MARKER_POSITIONS)
    return lengths


def read_training_dataset(
    manifest_path: Path, voice: str, model: VoxCPMModel, token_budget: int | None
) -> ManifestDataset:
    """Read and tokenize the clips of one voice from a manifest.

    Args:
        manifest_path: Manifest file.
        voice: Voice to keep.
        model: Model whose tokenizer, sample rate, audio VAE, and patch size the clips follow.
        token_budget: Longest packed clip to keep, or None to keep all.

    Returns:
        The dataset, empty when no clip of the voice fits the budget.

    """
    entries = read_voice_entries(manifest_path, voice)
    text_tokens = [model.text_tokenizer(entry.text) for entry in entries]
    if token_budget is not None:
        frame_rate = model.audio_vae.sample_rate / int(model.audio_vae.hop_length)
        lengths = build_sequence_lengths(
            [len(tokens) for tokens in text_tokens], [entry.duration for entry in entries], frame_rate, model.patch_size
        )
        kept = [index for index, length in enumerate(lengths) if length <= token_budget]
        logger.info("Kept %d of %d clips within %d tokens", len(kept), len(entries), token_budget)
        entries = [entries[index] for index in kept]
        text_tokens = [text_tokens[index] for index in kept]
    logger.info("Read %d clips of voice %s from %s", len(entries), voice, manifest_path)
    return ManifestDataset(entries, text_tokens, model.sample_rate)


def collate_batch(clips: Sequence[TrainingClip]) -> CollatedBatch:
    """Collate clips into one batch, padding each to the longest with the pad token id.

    Args:
        clips: Clips of the batch.

    Returns:
        The batch.

    """
    text_tokens = pad_sequence([clip.text_tokens for clip in clips], batch_first=True, padding_value=PAD_TOKEN_ID)
    waveforms = pad_sequence([clip.waveform for clip in clips], batch_first=True, padding_value=PAD_TOKEN_ID)
    return CollatedBatch(text_tokens=text_tokens, waveforms=waveforms)


def build_sampler(dataset: ManifestDataset, accelerator: Accelerator) -> DistributedSampler[TrainingClip] | None:
    """Build a sampler that gives each process its own shuffled share of the dataset.

    Args:
        dataset: The dataset.
        accelerator: The process, whose rank picks its share.

    Returns:
        The sampler, or None in a single process, where the loader shuffles.

    """
    if accelerator.world_size == 1:
        return None
    return DistributedSampler(dataset, num_replicas=accelerator.world_size, rank=accelerator.rank)


def build_loader(
    dataset: ManifestDataset,
    settings: TrainingSettings,
    sampler: DistributedSampler[TrainingClip] | None,
    *,
    is_training: bool,
) -> DataLoader[TrainingClip]:
    """Build a shuffled loader whose workers ignore the stop signals.

    Args:
        dataset: The dataset.
        settings: Run settings, for the batch size and worker count.
        sampler: Sampler of the process share, or None to shuffle the whole dataset.
        is_training: Whether to drop the last incomplete batch.

    Returns:
        The loader, which yields collated batches.

    """
    return DataLoader(
        dataset,
        batch_size=settings.batch_size,
        shuffle=sampler is None,
        sampler=sampler,
        num_workers=settings.loader_workers,
        collate_fn=collate_batch,
        drop_last=is_training,
        pin_memory=torch.cuda.is_available(),
        worker_init_fn=functools.partial(set_stop_action, signal.SIG_IGN),
    )

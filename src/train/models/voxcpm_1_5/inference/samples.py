"""Sample clips: one WAV file per prompt for each voice that has a checkpoint."""

from __future__ import annotations

from typing import TYPE_CHECKING
import logging

from config.models.voxcpm_1_5.samples import SAMPLE_INDEX_START, SAMPLE_FILE_TEMPLATE
from src.train.models.voxcpm_1_5.training.checkpoints import read_lora_config, list_voice_checkpoints
from src.train.models.voxcpm_1_5.inference.synthesizer import Synthesizer

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Sequence

    from schemas.models.voxcpm_1_5.inference import SampleSettings

logger = logging.getLogger(__name__)


def write_voice_samples(
    synthesizer: Synthesizer, voice: str, checkpoint_folder: Path, prompts: Sequence[str], samples_folder: Path
) -> list[Path]:
    """Read the adapter of one voice, then write one sample clip per prompt in that voice.

    Args:
        synthesizer: Synthesizer with the base model.
        voice: Voice, which names the files.
        checkpoint_folder: Checkpoint of the voice.
        prompts: Texts that the voice reads.
        samples_folder: Where the files go.

    Returns:
        The sample files, in prompt order.

    """
    logger.info("Writing %d samples of voice %s", len(prompts), voice)
    synthesizer.read_adapter(checkpoint_folder)
    return [
        synthesizer.write_sample(prompt, samples_folder / SAMPLE_FILE_TEMPLATE.format(voice=voice, index=index))
        for index, prompt in enumerate(prompts, start=SAMPLE_INDEX_START)
    ]


def write_samples(
    checkpoints_folder: Path, base_model_folder: Path, samples_folder: Path, settings: SampleSettings
) -> list[Path]:
    """Write the sample clips of each voice that has a checkpoint, reading the base model once.

    A voice without a checkpoint gets a warning and no samples. The base model takes the LoRA config of the first
    voice. No checkpoint of any voice raises CheckpointError, and an adapter that does not fit raises AdapterError.

    Args:
        checkpoints_folder: The checkpoints folder of the run, one folder per voice.
        base_model_folder: Downloaded base model.
        samples_folder: Where the files go; the call creates it when missing.
        settings: Voices, prompts, and sampler settings.

    Returns:
        The sample files, voice by voice.

    """
    voice_checkpoints = list_voice_checkpoints(checkpoints_folder, settings.voices)
    lora_config = read_lora_config(next(iter(voice_checkpoints.values())))
    synthesizer = Synthesizer.read_base_model(base_model_folder, lora_config, settings.sampler)
    samples_folder.mkdir(parents=True, exist_ok=True)
    sample_paths: list[Path] = []
    for voice in settings.voices:
        checkpoint_folder = voice_checkpoints.get(voice)
        if checkpoint_folder is None:
            logger.warning("Voice %s has no checkpoint in %s, so it gets no samples", voice, checkpoints_folder)
            continue
        sample_paths.extend(
            write_voice_samples(synthesizer, voice, checkpoint_folder, settings.prompts, samples_folder)
        )
    return sample_paths

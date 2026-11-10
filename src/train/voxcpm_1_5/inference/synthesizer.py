"""Speech synthesis with the base model and one voice adapter at a time."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast
import logging

import numpy as np
import torch
import soundfile

from config.voxcpm_1_5.inference import TARGET_PEAK
from src.train.voxcpm_1_5.model.voxcpm import VoxCPMModel
from src.train.voxcpm_1_5.training.checkpoints import read_lora_config

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Callable

    from numpy.typing import NDArray

    from schemas.voxcpm_1_5.inference import SamplerSettings
    from src.train.voxcpm_1_5.model.config import LoraConfig

logger = logging.getLogger(__name__)

write_audio_file = cast("Callable[[Path, NDArray[np.float32], int], None]", soundfile.write)
convert_to_array = cast("Callable[[torch.Tensor], NDArray[np.float32]]", torch.Tensor.numpy)


class AdapterError(Exception):
    """An adapter does not fit the model: it lacks its weights file, or training used other LoRA settings."""


def scale_to_peak(audio: NDArray[np.float32], target_peak: float) -> NDArray[np.float32]:
    """Scale audio so its loudest sample reaches the target peak, and leave silence unchanged.

    Args:
        audio: The waveform.
        target_peak: Absolute value of the loudest sample after scaling.

    Returns:
        The scaled waveform.

    """
    peak = float(np.abs(audio).max(initial=0.0))
    if peak == 0:
        return audio
    return (audio * (target_peak / peak)).astype(np.float32)


class Synthesizer:
    """The base model with LoRA layers and the sampler settings."""

    def __init__(self, model: VoxCPMModel, settings: SamplerSettings) -> None:
        """Hold the model and the sampler settings.

        Args:
            model: Base model with LoRA layers, in inference mode.
            settings: Sampler settings of every call.

        """
        self._model = model
        self._settings = settings

    @classmethod
    def read_base_model(
        cls, base_model_folder: Path, lora_config: LoraConfig, settings: SamplerSettings
    ) -> Synthesizer:
        """Read the base model in inference mode with LoRA layers shaped like the adapters, and turn them on.

        Args:
            base_model_folder: Downloaded base model.
            lora_config: LoRA config of the adapters.
            settings: Sampler settings of every call.

        Returns:
            The synthesizer, with no adapter weights yet.

        """
        logger.info("Reading the base model from %s with LoRA rank %d", base_model_folder, lora_config.r)
        model = VoxCPMModel.read_pretrained(base_model_folder, optimize=True, training=False, lora_config=lora_config)
        model.set_lora_enabled(enabled=True)
        return cls(model, settings)

    def read_adapter(self, checkpoint_folder: Path) -> None:
        """Read the adapter weights of a checkpoint into the LoRA layers, replacing the previous adapter.

        Args:
            checkpoint_folder: A training checkpoint.

        Raises:
            AdapterError: The checkpoint lacks its weights, stores other LoRA settings, or holds weights that the
                model lacks.

        """
        if read_lora_config(checkpoint_folder) != self._model.lora_config:
            message = f"The adapter {checkpoint_folder} was trained with other LoRA settings than the first voice"
            raise AdapterError(message)
        try:
            loaded_keys, skipped_keys = self._model.read_lora_weights(checkpoint_folder)
        except FileNotFoundError as error:
            message = f"The adapter {checkpoint_folder} has no weights file"
            raise AdapterError(message) from error
        if skipped_keys:
            message = f"The adapter {checkpoint_folder} holds {len(skipped_keys)} weights that the model lacks"
            raise AdapterError(message)
        logger.info("Read %d adapter weights from %s", len(loaded_keys), checkpoint_folder)

    def synthesize(self, text: str) -> NDArray[np.float32]:
        """Speak a text in the adapter voice, scaled to the target peak.

        Args:
            text: Text to speak.

        Returns:
            Mono waveform at the model sample rate.

        """
        waveform = self._model.generate(text, self._settings)
        audio = convert_to_array(waveform.squeeze(0).float().cpu())
        return scale_to_peak(audio, TARGET_PEAK)

    def write_sample(self, text: str, sample_path: Path) -> Path:
        """Synthesize speech for a text and write it as a WAV file.

        Args:
            text: Text to speak.
            sample_path: WAV file; its folder must exist.

        Returns:
            The WAV file.

        """
        audio = self.synthesize(text)
        write_audio_file(sample_path, audio, self._model.sample_rate)
        logger.info("Wrote %s, %.1f seconds", sample_path.name, len(audio) / self._model.sample_rate)
        return sample_path

"""Checkpoint loading and the checkpoint file names."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Self, cast
import logging

import torch
from transformers import PreTrainedTokenizerFast
import safetensors.torch

from src.train.models.voxcpm_1_5.model.base import VoxCPMBase
from src.train.models.voxcpm_1_5.model.config import VoxCPMConfig
from src.train.models.voxcpm_1_5.model.dtypes import select_dtype
from src.train.models.voxcpm_1_5.model.modules.audiovae.audiovae import AudioVae

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Callable

    from src.train.models.voxcpm_1_5.model.config import LoraConfig

MODEL_CONFIG_FILE = "config.json"
AUDIO_VAE_FILE = "audiovae.pth"
# Order matters: the loader reads the first file that exists.
MODEL_WEIGHTS_FILES = ("model.safetensors", "pytorch_model.bin")
AUDIO_VAE_PREFIX = "audio_vae."

logger = logging.getLogger(__name__)
_read_torch_file = cast("Callable[..., Any]", torch.load)


class VoxCPMLoaderMixin(VoxCPMBase):
    """Checkpoint loading of the model, its tokenizer, and its audio VAE."""

    @classmethod
    def read_pretrained(
        cls,
        path: Path,
        *,
        optimize: bool,
        training: bool,
        lora_config: LoraConfig | None,
    ) -> Self:
        """Load the model from a local checkpoint folder.

        It loads the weights with `strict=False` because the checkpoint holds no LoRA matrices.

        Args:
            path: Checkpoint folder with the config, tokenizer, audio VAE, and model weights.
            optimize: Whether to compile with `torch.compile`; only applies when `training` is false.
            training: Whether to keep the model on the CPU for training instead of on its device in eval
                mode. With `lora_config`, it also freezes every non-LoRA weight.
            lora_config: LoRA layers to inject, or None for the base model.

        Returns:
            The model.

        """
        config = VoxCPMConfig.model_validate_json((path / MODEL_CONFIG_FILE).read_text(encoding="utf-8"))
        # In transformers 5, LlamaTokenizerFast replaces the tokenizer.json normalizer with its own pre-tokenizer,
        # which changes token ids, so read the tokenizer with the generic class.
        read_tokenizer = cast("Callable[[Path], PreTrainedTokenizerFast]", PreTrainedTokenizerFast.from_pretrained)
        tokenizer = read_tokenizer(path)
        audio_vae = AudioVae(config=config.audio_vae_config)
        vae_checkpoint = _read_torch_file(path / AUDIO_VAE_FILE, map_location="cpu", weights_only=True)
        vae_state_dict = cast("dict[str, torch.Tensor]", vae_checkpoint["state_dict"])
        model = cls(config, tokenizer, audio_vae, lora_config)
        if not training:
            model = model.to(select_dtype(model.config.dtype))
        else:
            _freeze_for_training(model, lora_config)
        model.audio_vae = model.audio_vae.to(torch.float32)

        model_state_dict = _read_model_state(path)
        for key, value in vae_state_dict.items():
            model_state_dict[f"{AUDIO_VAE_PREFIX}{key}"] = value

        model.load_state_dict(model_state_dict, strict=False)
        if training:
            return model
        return model.to(model.device).eval().optimize(disable=not optimize)


def _freeze_for_training(model: VoxCPMBase, lora_config: LoraConfig | None) -> None:
    for name, param in model.named_parameters():
        if "audio_vae" in name:
            param.requires_grad = False
            continue
        if lora_config is not None and "lora" not in name:
            param.requires_grad = False


def _read_model_state(path: Path) -> dict[str, torch.Tensor]:
    safetensors_filename, pytorch_model_filename = MODEL_WEIGHTS_FILES
    safetensors_path = path / safetensors_filename
    pytorch_model_path = path / pytorch_model_filename

    if safetensors_path.exists():
        logger.info("Loading model from safetensors: %s", safetensors_path)
        read_safetensors = cast("Callable[[Path], dict[str, torch.Tensor]]", safetensors.torch.load_file)
        return read_safetensors(safetensors_path)
    if pytorch_model_path.exists():
        logger.info("Loading model from pytorch_model.bin: %s", pytorch_model_path)
        checkpoint = _read_torch_file(pytorch_model_path, map_location="cpu", weights_only=True)
        if isinstance(checkpoint, dict):
            return cast("dict[str, torch.Tensor]", cast("dict[str, Any]", checkpoint).get("state_dict", checkpoint))
        return cast("dict[str, torch.Tensor]", checkpoint)
    message = f"Model file not found. Expected either {safetensors_path} or {pytorch_model_path}"
    raise FileNotFoundError(message)

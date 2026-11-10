"""LoRA weight loading and switching, and the LoRA file names."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

import torch
import safetensors.torch

from src.train.models.voxcpm_1_5.model.base import VoxCPMBase
from src.train.models.voxcpm_1_5.model.modules.layers.lora import LoraLinear

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Callable

LORA_WEIGHTS_FILE = "lora_weights.safetensors"
LORA_CHECKPOINT_FILE = "lora_weights.ckpt"
LORA_CHECKPOINT_SUFFIXES = (".ckpt", ".pth")
# torch.compile wraps a module as `_orig_mod`, which adds this segment to its parameter names.
COMPILED_SEGMENT = "._orig_mod."


class VoxCPMLoraMixin(VoxCPMBase):
    """LoRA weight loading and the switch that turns the LoRA layers on and off."""

    def read_lora_weights(self, path: Path) -> tuple[list[str], list[str]]:
        """Copy saved LoRA weights into the LoRA layers of the model.

        Args:
            path: A folder with `LORA_WEIGHTS_FILE` or `LORA_CHECKPOINT_FILE`, or one `.safetensors`,
                `.ckpt`, or `.pth` file.

        Returns:
            Saved keys that matched a parameter, and saved keys that matched none.

        Raises:
            FileNotFoundError: When no weights file exists at the path.

        """
        safetensors_file, checkpoint_file = _find_lora_files(path)
        if safetensors_file is not None and safetensors_file.exists():
            read_safetensors = cast("Callable[..., dict[str, torch.Tensor]]", safetensors.torch.load_file)
            state_dict = read_safetensors(str(safetensors_file), device=self.device)
        elif checkpoint_file is not None and checkpoint_file.exists():
            read_torch_file = cast("Callable[..., Any]", torch.load)
            checkpoint = read_torch_file(checkpoint_file, map_location=self.device, weights_only=True)
            state_dict = cast("dict[str, torch.Tensor]", checkpoint.get("state_dict", checkpoint))
        else:
            message = f"LoRA checkpoint not found. Expected either {safetensors_file} or {checkpoint_file}"
            raise FileNotFoundError(message)

        model_params = dict(self.named_parameters())
        compiled_names = {
            name.replace(COMPILED_SEGMENT, "."): name for name in model_params if COMPILED_SEGMENT in name
        }
        loaded_keys: list[str] = []
        skipped_keys: list[str] = []
        for key, value in state_dict.items():
            target_key = key if key in model_params else compiled_names.get(key)
            if target_key:
                model_params[target_key].data.copy_(value.to(self.device))
                loaded_keys.append(key)
            else:
                skipped_keys.append(key)
        return loaded_keys, skipped_keys

    def set_lora_enabled(self, *, enabled: bool) -> None:
        """Switch every LoRA layer on or off. With LoRA off, the model matches the base model.

        Args:
            enabled: Whether the LoRA updates apply.

        """
        for module in self.modules():
            if isinstance(module, LoraLinear):
                cast("torch.Tensor", module.scaling).fill_(module.base_scaling if enabled else 0.0)


def _find_lora_files(path: Path) -> tuple[Path | None, Path | None]:
    if path.is_dir():
        return path / LORA_WEIGHTS_FILE, path / LORA_CHECKPOINT_FILE
    safetensors_file = path if path.suffix == ".safetensors" else None
    checkpoint_file = path if path.suffix in LORA_CHECKPOINT_SUFFIXES else None
    return safetensors_file, checkpoint_file

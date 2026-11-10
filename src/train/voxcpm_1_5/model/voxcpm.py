"""The VoxCPM model class, assembled from its mixins."""

from __future__ import annotations

from src.train.voxcpm_1_5.model.lora import VoxCPMLoraMixin
from src.train.voxcpm_1_5.model.loader import VoxCPMLoaderMixin
from src.train.voxcpm_1_5.model.forward import VoxCPMForwardMixin
from src.train.voxcpm_1_5.model.generation import VoxCPMGenerationMixin


class VoxCPMModel(VoxCPMForwardMixin, VoxCPMGenerationMixin, VoxCPMLoraMixin, VoxCPMLoaderMixin):
    """VoxCPM 1.5: training forward pass, generation, LoRA weights, and checkpoint loading."""

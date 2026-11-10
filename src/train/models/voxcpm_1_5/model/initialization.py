"""Builders of the VoxCPMBase submodules."""

from __future__ import annotations

from typing import TYPE_CHECKING

import torch
from torch import nn

from src.train.models.voxcpm_1_5.model.dtypes import select_dtype
from src.train.models.voxcpm_1_5.model.modules.minicpm4.cache import StaticKvCache
from src.train.models.voxcpm_1_5.model.modules.minicpm4.model import MiniCpmModel
from src.train.models.voxcpm_1_5.model.modules.layers.scalar_quantization import ScalarQuantizationLayer

if TYPE_CHECKING:
    from src.train.models.voxcpm_1_5.model.config import VoxCPMConfig, VoxCPMTransformerConfig
    from src.train.models.voxcpm_1_5.model.modules.minicpm4.config import MiniCpmConfig

STOP_CLASS_COUNT = 2


def select_device(config: VoxCPMConfig) -> str:
    """Return the configured device if CUDA exists, else the Apple GPU if present, else the CPU.

    Args:
        config: Model config.

    Returns:
        Device name.

    """
    device = config.device
    if not torch.cuda.is_available():
        device = "mps" if torch.backends.mps.is_available() else "cpu"
    return device


def build_language_model(lm_config: MiniCpmConfig, config: VoxCPMConfig, device: str) -> MiniCpmModel:
    """Build a MiniCPM language model with a one-sample KV cache.

    Args:
        lm_config: Base config or the residual copy.
        config: Model config, for the cache length and dtype.
        device: KV cache device.

    Returns:
        The language model.

    """
    model = MiniCpmModel(lm_config)
    head_dim = (
        lm_config.hidden_size // lm_config.num_attention_heads
        if lm_config.kv_channels is None
        else lm_config.kv_channels
    )
    model.kv_cache = StaticKvCache(
        num_layers=lm_config.num_hidden_layers,
        max_length=config.max_length,
        head_shape=(1, lm_config.num_key_value_heads, head_dim),
        device=torch.device(device),
        dtype=select_dtype(config.dtype),
    )
    return model


def copy_residual_config(config: VoxCPMConfig) -> MiniCpmConfig:
    """Copy the base config with fewer layers and no token embedding, for the residual model.

    Args:
        config: Model config.

    Returns:
        Residual language model config.

    """
    residual_lm_config = config.lm_config.model_copy(deep=True)
    residual_lm_config.num_hidden_layers = config.residual_lm_num_layers
    residual_lm_config.vocab_size = 0
    return residual_lm_config


def copy_lm_config(config: VoxCPMConfig, transformer: VoxCPMTransformerConfig) -> MiniCpmConfig:
    """Copy the language model config, resized to a small transformer and without a token embedding.

    Args:
        config: Model config.
        transformer: Size of the local encoder or the diffusion estimator.

    Returns:
        Config of that transformer.

    """
    copied = config.lm_config.model_copy(deep=True)
    copied.hidden_size = transformer.hidden_dim
    copied.intermediate_size = transformer.ffn_dim
    copied.num_attention_heads = transformer.num_heads
    copied.num_hidden_layers = transformer.num_layers
    copied.kv_channels = transformer.kv_channels
    copied.vocab_size = 0
    return copied


def build_projection_layers(config: VoxCPMConfig) -> tuple[ScalarQuantizationLayer, nn.Linear, nn.Linear, nn.Linear]:
    """Build the scalar quantization layer and the encoder-to-LM, LM-to-DiT, and residual-to-DiT projections.

    Args:
        config: Model config.

    Returns:
        The layers, in the order the model registers them.

    """
    fsq_layer = ScalarQuantizationLayer(
        config.lm_config.hidden_size,
        config.lm_config.hidden_size,
        config.scalar_quantization_latent_dim,
        config.scalar_quantization_scale,
    )
    enc_to_lm_proj = nn.Linear(config.encoder_config.hidden_dim, config.lm_config.hidden_size)
    lm_to_dit_proj = nn.Linear(config.lm_config.hidden_size, config.dit_config.hidden_dim)
    res_to_dit_proj = nn.Linear(config.lm_config.hidden_size, config.dit_config.hidden_dim)
    return fsq_layer, enc_to_lm_proj, lm_to_dit_proj, res_to_dit_proj


def build_stop_predictor(config: VoxCPMConfig) -> tuple[nn.Linear, nn.SiLU, nn.Linear]:
    """Build the projection, activation, and head that predict the end of the audio.

    Args:
        config: Model config.

    Returns:
        The layers, in the order the model registers them.

    """
    stop_proj = nn.Linear(config.lm_config.hidden_size, config.lm_config.hidden_size)
    stop_actn = nn.SiLU()
    stop_head = nn.Linear(config.lm_config.hidden_size, STOP_CLASS_COUNT, bias=False)
    return stop_proj, stop_actn, stop_head

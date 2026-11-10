"""VoxCPM backbone: submodules, LoRA injection, and compilation."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Self, cast
import logging
import importlib.util

import torch
from torch import nn

from src.train.voxcpm_1_5.model.text import TextTokenizer, ChineseCharacterTokenizer
from src.train.voxcpm_1_5.model.dtypes import select_dtype
from src.train.voxcpm_1_5.model.initialization import (
    select_device,
    copy_lm_config,
    build_language_model,
    build_stop_predictor,
    copy_residual_config,
    build_projection_layers,
)
from src.train.voxcpm_1_5.model.modules.locenc import VoxCPMLocEnc
from src.train.voxcpm_1_5.model.modules.layers.lora import LoraLinear, inject_lora_layers
from src.train.voxcpm_1_5.model.modules.locdit.local_dit import VoxCPMLocDit
from src.train.voxcpm_1_5.model.modules.locdit.unified_cfm import UnifiedCfm

if TYPE_CHECKING:
    from collections.abc import Callable

    from transformers import PreTrainedTokenizerFast

    from src.train.voxcpm_1_5.model.config import LoraConfig, VoxCPMConfig
    from src.train.voxcpm_1_5.model.modules.audiovae.audiovae import AudioVae

logger = logging.getLogger(__name__)

AUDIO_START_TOKEN = 101
# The model never reads this id; the batch packer appends it after the last patch.
AUDIO_END_TOKEN = 102
COMPILE_MODE = "reduce-overhead"


class VoxCPMBase(nn.Module):
    """Two language models, the local encoder, the diffusion decoder, and their projections."""

    def __init__(
        self,
        config: VoxCPMConfig,
        tokenizer: PreTrainedTokenizerFast,
        audio_vae: AudioVae,
        lora_config: LoraConfig | None = None,
    ) -> None:
        """Build the submodules in the order the seeded tests and the checkpoint expect.

        Args:
            config: Model config.
            tokenizer: Checkpoint tokenizer.
            audio_vae: Audio VAE whose latents the model predicts.
            lora_config: LoRA layers to inject, or None for the base model.

        """
        cast("Callable[[], None]", super().__init__)()
        self.config = config
        self.lora_config = lora_config
        self.feat_dim = config.feat_dim
        self.patch_size = config.patch_size
        self.device = select_device(config)
        logger.info("Running on device: %s, dtype: %s", self.device, config.dtype)

        self.base_lm = build_language_model(config.lm_config, config, self.device)
        self.text_tokenizer: TextTokenizer = ChineseCharacterTokenizer(tokenizer)
        self.audio_start_token = AUDIO_START_TOKEN

        self.residual_lm = build_language_model(copy_residual_config(config), config, self.device)
        self.feat_encoder = VoxCPMLocEnc(copy_lm_config(config, config.encoder_config), input_dim=config.feat_dim)
        self.feat_decoder = UnifiedCfm(
            in_channels=config.feat_dim,
            cfm_params=config.dit_config.cfm_config,
            estimator=VoxCPMLocDit(copy_lm_config(config, config.dit_config), in_channels=config.feat_dim),
            mean_mode=config.dit_mean_mode,
        )
        self.fsq_layer, self.enc_to_lm_proj, self.lm_to_dit_proj, self.res_to_dit_proj = build_projection_layers(config)
        self.stop_proj, self.stop_actn, self.stop_head = build_stop_predictor(config)
        self.stop_loss = nn.CrossEntropyLoss(reduction="none")

        self.audio_vae = audio_vae
        self.chunk_size = audio_vae.chunk_size
        self.sample_rate = audio_vae.sample_rate
        if lora_config is not None:
            self._apply_lora(lora_config)

    def optimize(self, *, disable: bool = False) -> Self:
        """Compile the decoding steps, local encoder, and diffusion estimator on CUDA.

        Without CUDA or triton, it logs a warning and skips compilation.

        Args:
            disable: Whether to skip compilation.

        Returns:
            The model itself.

        """
        if disable:
            return self
        if self.device != "cuda":
            logger.warning("torch.compile disabled: %s", "VoxCPMModel can only be optimized on CUDA device")
            return self
        if importlib.util.find_spec("triton") is None:
            logger.warning("torch.compile disabled: %s", "triton is not installed")
            return self
        compile_function = cast("Callable[..., Any]", torch.compile)
        try:
            cast("Any", self.base_lm).forward_step = compile_function(
                self.base_lm.forward_step, mode=COMPILE_MODE, fullgraph=True
            )
            cast("Any", self.residual_lm).forward_step = compile_function(
                self.residual_lm.forward_step, mode=COMPILE_MODE, fullgraph=True
            )
            self.feat_encoder = cast(
                "VoxCPMLocEnc", compile_function(self.feat_encoder, mode=COMPILE_MODE, fullgraph=True)
            )
            cast("Any", self.feat_decoder).estimator = compile_function(
                self.feat_decoder.estimator, mode=COMPILE_MODE, fullgraph=True
            )
        except RuntimeError as exc:
            logger.warning("torch.compile disabled: %s", exc)
        return self

    def _apply_lora(self, lora_config: LoraConfig) -> None:
        lora_r = int(lora_config.r)
        lora_alpha = float(lora_config.alpha)
        lora_dropout = float(lora_config.dropout)

        if lora_config.enable_lm:
            for lm in [self.base_lm, self.residual_lm]:
                inject_lora_layers(
                    lm,
                    target_submodule_names=lora_config.target_modules_lm,
                    r=lora_r,
                    alpha=lora_alpha,
                    dropout=lora_dropout,
                )

        if lora_config.enable_dit:
            inject_lora_layers(
                self.feat_decoder.estimator,
                target_submodule_names=lora_config.target_modules_dit,
                r=lora_r,
                alpha=lora_alpha,
                dropout=lora_dropout,
            )

        if lora_config.enable_proj:
            for attr_name in lora_config.target_proj_modules:
                module = getattr(self, attr_name, None)
                if isinstance(module, nn.Linear):
                    setattr(
                        self,
                        attr_name,
                        LoraLinear(base=module, r=lora_r, alpha=lora_alpha, dropout=lora_dropout),
                    )

    def _get_dtype(self) -> torch.dtype:
        return select_dtype(self.config.dtype)

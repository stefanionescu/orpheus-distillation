"""Builders for the train unit suite: a tiny CPU VoxCPM model, fixed inputs, and checkpoint files."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, cast
from unittest import mock
from contextlib import contextmanager
from dataclasses import dataclass

import torch
from tokenizers import Tokenizer
from transformers import LlamaTokenizerFast
import safetensors.torch

from schemas.voxcpm_1_5.batch import PackedBatch
from schemas.voxcpm_1_5.inference import SamplerSettings
from src.train.voxcpm_1_5.model.lora import LORA_WEIGHTS_FILE
from src.train.voxcpm_1_5.model.config import LoraConfig, VoxCPMConfig, VoxCPMDitConfig, VoxCPMEncoderConfig
from src.train.voxcpm_1_5.model.voxcpm import VoxCPMModel
from src.train.voxcpm_1_5.model.modules.minicpm4.config import MiniCpmConfig, RopeScalingConfig
from src.train.voxcpm_1_5.model.modules.audiovae.audiovae import AudioVae, AudioVaeConfig
from src.train.voxcpm_1_5.model.modules.locdit.unified_cfm import CfmConfig

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Callable, Generator

SEED = 1234
HIDDEN_SIZE = 32
FFN_SIZE = 64
HEAD_COUNT = 2
FEAT_DIM = 8
PATCH_SIZE = 2
MAX_LENGTH = 64
MODEL_SAMPLE_RATE = 16000
ROPE_FACTORS = (1.0, 1.05, 1.1, 1.2, 1.3, 1.5, 1.8, 2.0)
SPECIAL_TOKENS = ("<unk>", "<s>", "</s>", "▁")
TOKENIZER_CHARACTERS = "abcdefghijklmnopqrstuvwxyz"
# Hub file names spelled out, not the loader constants, so a loader that reads another name fails the tests.
HUB_CONFIG_FILE = "config.json"
HUB_AUDIO_VAE_FILE = "audiovae.pth"
HUB_WEIGHTS_FILE = "model.safetensors"
TOKENIZER_FILE = "tokenizer.json"
TOKENIZER_CONFIG_FILE = "tokenizer_config.json"
AUDIO_START_TOKEN = 101
AUDIO_END_TOKEN = 102

FORWARD_PROGRESS = 0.5
LORA_RANK = 2
LORA_ALPHA = 4
LORA_B_SCALE = 0.1
LINEAR_IN_FEATURES = 8
LINEAR_OUT_FEATURES = 6
QUANTIZER_DIM = 16
QUANTIZER_LATENT_DIM = 8
QUANTIZER_SCALE = 9
WAVEFORM_SAMPLES = 37
WAVEFORM_SCALE = 0.3
WAVEFORM_OFFSET = 4
LINEAR_INPUT_OFFSET = 5
LORA_B_OFFSET = 6
QUANTIZER_INPUT_OFFSET = 7
SOLVER_TIMESTEPS = 10
GUIDANCE_SCALE = 2.0
SPEECH_TEXT = "hello world"
SAMPLER_GUIDANCE_SCALE = 1.5
SAMPLER_TIMESTEPS = 3
# The seeded model stops before it reaches this cap.
LONG_MAX_PATCHES = 20
SHORT_MAX_PATCHES = 2

# Torch types `tolist` loosely, and the tests compare its nested lists with plain lists.
to_list = cast("Callable[[torch.Tensor], object]", torch.Tensor.tolist)


@dataclass(frozen=True)
class SamplerInputs:
    """Fixed conditions of one sampler call of the flow matching decoder.

    Attributes:
        mu: The hidden state that conditions the estimator, shaped (batch, hidden_size).
        cond: The previous patch that prefixes the estimator input, shaped (batch, feat_dim, patch_size).

    """

    mu: torch.Tensor
    cond: torch.Tensor


def _build_lm_config() -> MiniCpmConfig:
    return MiniCpmConfig(
        bos_token_id=1,
        eos_token_id=2,
        hidden_size=HIDDEN_SIZE,
        intermediate_size=FFN_SIZE,
        max_position_embeddings=MAX_LENGTH,
        num_attention_heads=HEAD_COUNT,
        num_hidden_layers=2,
        num_key_value_heads=1,
        rms_norm_eps=1e-5,
        rope_scaling=RopeScalingConfig(
            type="longrope",
            long_factor=list(ROPE_FACTORS),
            short_factor=list(reversed(ROPE_FACTORS)),
            original_max_position_embeddings=MAX_LENGTH // 2,
        ),
        vocab_size=128,
        use_mup=True,
        scale_emb=12.0,
        dim_model_base=16,
        scale_depth=1.4,
        rope_theta=10000.0,
    )


def _build_cfm_config() -> CfmConfig:
    return CfmConfig(
        sigma_min=1e-6,
        solver="euler",
        t_scheduler="log-norm",
        training_cfg_rate=0.1,
        inference_cfg_rate=1.0,
        reg_loss_type="l1",
        ratio_r_neq_t_range=(0.25, 0.75),
        noise_cond_prob_range=(0.2, 0.8),
        noise_cond_scale=0.1,
    )


def _build_tokenizer_spec() -> dict[str, object]:
    vocab = {token: index for index, token in enumerate((*SPECIAL_TOKENS, *TOKENIZER_CHARACTERS))}
    metaspace = {"type": "Metaspace", "replacement": "▁", "prepend_scheme": "always", "split": True}
    return {
        "version": "1.0",
        "truncation": None,
        "padding": None,
        "added_tokens": [],
        "normalizer": None,
        "pre_tokenizer": metaspace,
        "post_processor": None,
        "decoder": metaspace,
        "model": {"type": "BPE", "unk_token": "<unk>", "vocab": vocab, "merges": []},
    }


def build_audio_vae_config() -> AudioVaeConfig:
    """Return the tiny model's depthwise audio VAE config.

    Returns:
        The config.

    """
    return AudioVaeConfig(
        encoder_dim=4,
        encoder_rates=[2, 2],
        latent_dim=FEAT_DIM,
        decoder_dim=16,
        decoder_rates=[2, 2],
        depthwise=True,
        sample_rate=MODEL_SAMPLE_RATE,
        use_noise_block=False,
    )


def build_lora_config() -> LoraConfig:
    """Return a small LoRA config on the language models, diffusion estimator, and projections.

    Returns:
        The config.

    """
    return LoraConfig(enable_lm=True, enable_dit=True, enable_proj=True, r=LORA_RANK, alpha=LORA_ALPHA, dropout=0.0)


def build_tokenizer() -> LlamaTokenizerFast:
    """Return a character-level Llama tokenizer over the lowercase letters.

    Returns:
        The tokenizer.

    """
    read_tokenizer = cast("Callable[[str], Tokenizer]", Tokenizer.from_str)
    return LlamaTokenizerFast(tokenizer_object=read_tokenizer(json.dumps(_build_tokenizer_spec())), legacy=False)


def reset_random_state() -> None:
    """Seed the CPU generator that model init, dropout, and the samplers draw from."""
    torch.default_generator.manual_seed(SEED)


@contextmanager
def run_on_cpu() -> Generator[None]:
    """Hide the Apple GPU while the model picks its device, so a Mac runs on the CPU like Linux.

    Yields:
        Nothing; exit restores the device probe.

    """
    # The first compiler import reads the probe, so load the compiler before the patch replaces the probe.
    torch.compiler.reset()
    with mock.patch.object(torch.backends.mps, "is_available", return_value=False):
        yield


def build_tiny_model(*, lora_config: LoraConfig | None = None, is_mean_mode: bool = False) -> VoxCPMModel:
    """Return a seeded tiny float32 VoxCPM model with seeded nonzero LoRA B matrices.

    Args:
        lora_config: The LoRA layers to inject, or None for the base model.
        is_mean_mode: Whether the diffusion decoder trains on the mean velocity.

    Returns:
        The model in training mode.

    """
    reset_random_state()
    config = VoxCPMConfig(
        lm_config=_build_lm_config(),
        patch_size=PATCH_SIZE,
        feat_dim=FEAT_DIM,
        residual_lm_num_layers=1,
        scalar_quantization_latent_dim=16,
        scalar_quantization_scale=9,
        encoder_config=VoxCPMEncoderConfig(
            hidden_dim=HIDDEN_SIZE, ffn_dim=FFN_SIZE, num_heads=HEAD_COUNT, num_layers=1
        ),
        dit_config=VoxCPMDitConfig(
            hidden_dim=HIDDEN_SIZE, ffn_dim=FFN_SIZE, num_heads=HEAD_COUNT, num_layers=1, cfm_config=_build_cfm_config()
        ),
        audio_vae_config=build_audio_vae_config(),
        max_length=MAX_LENGTH,
        device="cpu",
        dtype="float32",
        dit_mean_mode=is_mean_mode,
    )
    audio_vae = AudioVae(config=config.audio_vae_config)
    with run_on_cpu():
        model = VoxCPMModel(config, build_tokenizer(), audio_vae, lora_config)
    generator = torch.Generator().manual_seed(SEED + 1)
    with torch.no_grad():
        for name, parameter in model.named_parameters():
            if "lora_B" in name:
                parameter.copy_(torch.randn(parameter.shape, generator=generator) * LORA_B_SCALE)
    return model


def build_packed_batch() -> PackedBatch:
    """Return a two-clip batch: text, the audio start token, audio patches, and the audio end token.

    Returns:
        The batch.

    """
    generator = torch.Generator().manual_seed(SEED + 2)
    text_tokens = torch.tensor(
        [
            [11, 8, 15, AUDIO_START_TOKEN, 0, 0, 0, AUDIO_END_TOKEN],
            [26, 18, AUDIO_START_TOKEN, 0, 0, 0, 0, AUDIO_END_TOKEN],
        ],
        dtype=torch.int32,
    )
    text_mask = torch.tensor([[1, 1, 1, 1, 0, 0, 0, 1], [1, 1, 1, 0, 0, 0, 0, 1]], dtype=torch.int32)
    audio_mask = 1 - text_mask
    audio_feats = torch.randn((2, 8, PATCH_SIZE, FEAT_DIM), generator=generator) * audio_mask[..., None, None]
    labels = torch.zeros((2, 8), dtype=torch.int32)
    labels[:, 6] = 1
    return PackedBatch(
        text_tokens=text_tokens,
        audio_feats=audio_feats,
        text_mask=text_mask,
        audio_mask=audio_mask,
        loss_mask=audio_mask.clone(),
        position_ids=torch.arange(8, dtype=torch.int32).repeat(2, 1),
        labels=labels,
    )


def build_sampler_inputs() -> SamplerInputs:
    """Return the seeded conditions of one sampler call.

    Returns:
        The conditions.

    """
    generator = torch.Generator().manual_seed(SEED + 3)
    # The recording drew a noise patch from this generator before the conditions, so draw it to keep their values.
    torch.randn((2, FEAT_DIM, PATCH_SIZE), generator=generator)
    return SamplerInputs(
        mu=torch.randn((2, HIDDEN_SIZE), generator=generator),
        cond=torch.randn((2, FEAT_DIM, PATCH_SIZE), generator=generator),
    )


def build_sampler_settings(max_patches: int) -> SamplerSettings:
    """Return sampler settings that differ from the upstream defaults, so a dropped setting changes the output.

    Args:
        max_patches: The most audio patches.

    Returns:
        The settings.

    """
    return SamplerSettings(guidance_scale=SAMPLER_GUIDANCE_SCALE, timesteps=SAMPLER_TIMESTEPS, max_patches=max_patches)


def build_seeded_tensor(shape: tuple[int, ...], offset: int) -> torch.Tensor:
    """Return standard normal values seeded with the suite seed plus an offset.

    Args:
        shape: The tensor shape.
        offset: Keeps each suite input distinct.

    Returns:
        The tensor.

    """
    return torch.randn(shape, generator=torch.Generator().manual_seed(SEED + offset))


def write_checkpoint_folder(model: VoxCPMModel, folder: Path) -> None:
    """Write a model as a base model folder with the VoxCPM 1.5 Hub file names.

    Args:
        model: A model without LoRA layers.
        folder: Where the config, tokenizer, audio VAE, and weights go.

    """
    (folder / HUB_CONFIG_FILE).write_text(model.config.model_dump_json(by_alias=True), encoding="utf-8")
    (folder / TOKENIZER_FILE).write_text(json.dumps(_build_tokenizer_spec()), encoding="utf-8")
    (folder / TOKENIZER_CONFIG_FILE).write_text(json.dumps({"legacy": False}), encoding="utf-8")
    write_torch_file = cast("Callable[[object, Path], None]", torch.save)
    write_torch_file({"state_dict": model.audio_vae.state_dict()}, folder / HUB_AUDIO_VAE_FILE)
    weights = {name: tensor for name, tensor in model.state_dict().items() if not name.startswith("audio_vae.")}
    (folder / HUB_WEIGHTS_FILE).write_bytes(safetensors.torch.save(weights))


def write_space_normalizer_tokenizer(folder: Path) -> None:
    """Replace a checkpoint's tokenizer with one whose normalizer marks spaces, as VoxCPM 1.5 does.

    Args:
        folder: The checkpoint folder.

    """
    prepend = {"type": "Prepend", "prepend": "▁"}
    replace = {"type": "Replace", "pattern": {"String": " "}, "content": "▁"}
    normalizer = {"type": "Sequence", "normalizers": [prepend, replace]}
    spec = _build_tokenizer_spec() | {"normalizer": normalizer, "pre_tokenizer": None}
    (folder / TOKENIZER_FILE).write_text(json.dumps(spec), encoding="utf-8")


def write_lora_weights(model: VoxCPMModel, folder: Path, extra_weights: dict[str, torch.Tensor]) -> list[str]:
    """Write a model's LoRA parameters, plus extra entries, as a checkpoint's adapter file.

    Args:
        model: A model with LoRA layers.
        folder: The checkpoint folder.
        extra_weights: Entries to add beside the LoRA parameters.

    Returns:
        The sorted LoRA parameter names.

    """
    weights = {name: tensor.detach().clone() for name, tensor in model.named_parameters() if "lora_" in name}
    (folder / LORA_WEIGHTS_FILE).write_bytes(safetensors.torch.save(weights | extra_weights))
    return sorted(weights)

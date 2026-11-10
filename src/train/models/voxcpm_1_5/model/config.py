"""Records of `config.json` and `lora_config.json`. Field names are the file keys."""

from __future__ import annotations

from pydantic import BaseModel

from src.train.models.voxcpm_1_5.model.modules.minicpm4.config import MiniCpmConfig
from src.train.models.voxcpm_1_5.model.modules.audiovae.audiovae import AudioVaeConfig
from src.train.models.voxcpm_1_5.model.modules.locdit.unified_cfm import CfmConfig


class VoxCPMTransformerConfig(BaseModel):
    """Size of a small transformer: the local encoder or the diffusion estimator.

    Attributes:
        hidden_dim: Hidden size.
        ffn_dim: Feed-forward size.
        num_heads: Attention heads.
        num_layers: Decoder layers.
        kv_channels: Head size, or None for `hidden_dim // num_heads`.

    """

    hidden_dim: int = 1024
    ffn_dim: int = 4096
    num_heads: int = 16
    num_layers: int = 4
    kv_channels: int | None = None


class VoxCPMEncoderConfig(VoxCPMTransformerConfig):
    """Size of the local encoder."""


class VoxCPMDitConfig(VoxCPMTransformerConfig):
    """Size of the diffusion estimator and its flow matching settings.

    Attributes:
        cfm_config: Flow matching settings.

    """

    cfm_config: CfmConfig


class VoxCPMConfig(BaseModel):
    """Model config, as `config.json` holds it.

    Attributes:
        lm_config: Base language model; the residual model and both small transformers copy it.
        patch_size: Latent frames per audio patch.
        feat_dim: Size of one latent frame, the audio VAE latent size.
        residual_lm_num_layers: Layers of the residual language model.
        scalar_quantization_latent_dim: Size of the scalar quantization bottleneck.
        scalar_quantization_scale: Quantization levels on each side of zero.
        encoder_config: Local encoder.
        dit_config: Diffusion estimator.
        audio_vae_config: Audio VAE, or None for its defaults.
        max_length: KV cache length.
        device: Device to use when CUDA is available.
        dtype: Dtype of the language models.
        dit_mean_mode: Whether the diffusion estimator trains on the mean velocity.

    """

    lm_config: MiniCpmConfig
    patch_size: int = 2
    feat_dim: int = 64
    residual_lm_num_layers: int = 6
    scalar_quantization_latent_dim: int = 256
    scalar_quantization_scale: int = 9

    encoder_config: VoxCPMEncoderConfig
    dit_config: VoxCPMDitConfig
    audio_vae_config: AudioVaeConfig | None = None

    max_length: int = 4096
    device: str = "cuda"
    dtype: str = "bfloat16"
    dit_mean_mode: bool = False


class LoraConfig(BaseModel):
    """LoRA layers that fine-tuning injects, as `lora_config.json` holds them.

    Attributes:
        enable_lm: Whether to inject LoRA into both language models.
        enable_dit: Whether to inject LoRA into the diffusion estimator.
        enable_proj: Whether to inject LoRA into the projections between the parts.
        r: Rank of each LoRA layer.
        alpha: Scale numerator; each update scales by `alpha / r`.
        dropout: Dropout probability before the update.
        target_modules_lm: Linear layer names to adapt in the language models.
        target_modules_dit: Linear layer names to adapt in the diffusion estimator.
        target_proj_modules: Projection attribute names to adapt.

    """

    enable_lm: bool = False
    enable_dit: bool = False
    enable_proj: bool = False

    r: int = 8
    alpha: int = 16
    dropout: float = 0.0

    target_modules_lm: list[str] = ["q_proj", "v_proj", "k_proj", "o_proj"]
    target_modules_dit: list[str] = ["q_proj", "v_proj", "k_proj", "o_proj"]
    target_proj_modules: list[str] = ["enc_to_lm_proj", "lm_to_dit_proj", "res_to_dit_proj"]

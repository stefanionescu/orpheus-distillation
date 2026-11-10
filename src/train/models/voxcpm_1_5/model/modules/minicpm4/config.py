"""Records of the MiniCPM4 config in `config.json`."""

from __future__ import annotations

from pydantic import BaseModel


class RopeScalingConfig(BaseModel):
    """LongRoPE settings of the rotary embedding.

    Attributes:
        type: Scaling type name.
        long_factor: Frequency factors past the original context length.
        short_factor: Frequency factors within the original context length.
        original_max_position_embeddings: Pretraining context length.

    """

    type: str
    long_factor: list[float]
    short_factor: list[float]
    original_max_position_embeddings: int


class MiniCpmConfig(BaseModel):
    """MiniCPM4 config, under `lm_config` in `config.json`.

    Attributes:
        bos_token_id: Begin-of-sequence token id.
        eos_token_id: End-of-sequence token id.
        hidden_size: Hidden size.
        intermediate_size: Feed-forward size.
        max_position_embeddings: Longest context.
        num_attention_heads: Query heads.
        num_hidden_layers: Decoder layers.
        num_key_value_heads: Key and value heads.
        rms_norm_eps: Epsilon of the RMS norm.
        rope_scaling: LongRoPE settings.
        vocab_size: Vocabulary size; zero for a model that takes embeddings.
        use_mup: Whether to scale embeddings and residual branches for maximal update parametrization.
        scale_emb: Token embedding scale under that parametrization.
        dim_model_base: Base width of that parametrization.
        scale_depth: Residual branch scale under that parametrization.
        rope_theta: Base of the rotary frequencies.
        kv_channels: Head size, or None for `hidden_size // num_attention_heads`.

    """

    bos_token_id: int
    eos_token_id: int
    hidden_size: int
    intermediate_size: int
    max_position_embeddings: int
    num_attention_heads: int
    num_hidden_layers: int
    num_key_value_heads: int
    rms_norm_eps: float
    rope_scaling: RopeScalingConfig
    vocab_size: int
    use_mup: bool = True
    scale_emb: float
    dim_model_base: int
    scale_depth: float
    rope_theta: float
    kv_channels: int | None = None

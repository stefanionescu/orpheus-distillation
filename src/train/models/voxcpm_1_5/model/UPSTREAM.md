# Upstream

Source: [OpenBMB VoxCPM](https://github.com/OpenBMB/VoxCPM), commit
[`ee5f2567ac684739bf254c5f09a1e9bcd5cd9555`](https://github.com/OpenBMB/VoxCPM/tree/ee5f2567ac684739bf254c5f09a1e9bcd5cd9555/src/voxcpm)
of 2025-12-15, packages `voxcpm.model` and `voxcpm.modules`. The code here is a
hand port, so a refresh ports the upstream diff by hand.

## File mapping

| Upstream module                                   | Here                                                                                                                              |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `voxcpm.model.voxcpm`, the four config classes    | `config.py`                                                                                                                       |
| `voxcpm.model.voxcpm`, `VoxCPMModel`              | `voxcpm.py`, built from `base.py`, `initialization.py`, `forward.py`, `inference.py`, `generation.py`, `lora.py`, and `loader.py` |
| `voxcpm.model.utils`                              | `text.py` for the tokenizer, `dtypes.py` for the dtype names                                                                      |
| `voxcpm.modules.audiovae.audio_vae`               | `modules/audiovae/`: `audiovae.py`, `encoder.py`, `decoder.py`, and `layers.py`                                                   |
| `voxcpm.modules.layers.lora`                      | `modules/layers/lora.py`                                                                                                          |
| `voxcpm.modules.layers.scalar_quantization_layer` | `modules/layers/scalar_quantization.py`                                                                                           |
| `voxcpm.modules.locdit.local_dit`, `unified_cfm`  | `modules/locdit/local_dit.py`, `unified_cfm.py`                                                                                   |
| `voxcpm.modules.locenc.local_encoder`             | `modules/locenc.py`                                                                                                               |
| `voxcpm.modules.minicpm4.model`                   | `modules/minicpm4/`: `model.py`, `attention.py`, `decoder.py`, and `layers.py`                                                    |
| `voxcpm.modules.minicpm4.cache`, `config`         | `modules/minicpm4/cache.py`, `config.py`                                                                                          |

## Renamed names

| Upstream                                                                               | Here                                                                                       |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `VoxCPMModel.from_local`, `load_lora_weights`                                          | `read_pretrained`, `read_lora_weights`                                                     |
| `LoRAConfig`, `LoRALinear`, `AudioVAE`, `AudioVAEConfig`, `UnifiedCFM`, `VoxCPMLocDiT` | `LoraConfig`, `LoraLinear`, `AudioVae`, `AudioVaeConfig`, `UnifiedCfm`, `VoxCPMLocDit`     |
| `MiniCPM4Config`, `MiniCPMModel`, `MiniCPMDecoderLayer`, `MiniCPMAttention`            | `MiniCpmConfig`, `MiniCpmModel`, `MiniCpmDecoderLayer`, `MiniCpmAttention`                 |
| `MiniCPMLongRoPE`, `MiniCPMRMSNorm`, `MiniCPMMLP`, `StaticKVCache`                     | `MiniCpmLongRope`, `MiniCpmRmsNorm`, `MiniCpmMlp`, `StaticKvCache`                         |
| `CausalConv1d`, `CausalTransposeConv1d`, `Snake1d`, `WNCausalConv1d`, `snake`          | `CausalConv`, `CausalTransposeConv`, `SnakeActivation`, `build_causal_conv`, `apply_snake` |
| `CharTokenizerWrapper`, `mask_multichar_chinese_tokens`                                | `ChineseCharacterTokenizer`, which builds its own set of multi-character tokens            |
| `apply_lora_to_named_linear_modules`, `get_dtype`, `setup_cache`                       | `inject_lora_layers`, `select_dtype`, the cache that `build_language_model` allocates      |

Module attributes, parameters, and config keys keep their upstream names,
because they are the keys of `model.safetensors`, `audiovae.pth`, `config.json`,
and the saved LoRA adapters. `tests/suites/unit/models/voxcpm_1_5` pins them.

Three `CfmConfig` fields read their upstream key through a pydantic alias:
`condition_drop_rate` reads `training_cfg_rate`, `default_guidance_scale` reads
`inference_cfg_rate`, and `unequal_time_ratio_range` reads
`ratio_r_neq_t_range`. Code that writes a `config.json` dumps with
`by_alias=True`.

## Dropped

- The prompt cache: `build_prompt_cache`, `merge_prompt_cache`, and
  `generate_with_prompt_cache` with its streaming form.
- Voice cloning from a prompt waveform, the retry on overlong output, and
  streaming: `generate_streaming`, `inference`, `inference_streaming`, and the
  matching branches of `_generate` and `_inference`.
- The `sample_generate` option of `forward`. It raised a `TypeError`, because
  it passed the float `inference_cfg_rate` as the step count.
- The sampler options that every caller left at their defaults: the
  temperature, the sway coefficient, and the switch that turned off the
  zero-star guidance correction.
- The LoRA helpers `reset_lora_weights`, `get_lora_state_dict`,
  `reset_lora_parameters`, and the `enabled` property.
- Unused code: `WNConv1d`, `WNConvTranspose1d`, `init_weights`,
  `TransposeLastTwoDim`, and the attributes `enc_dim` and
  `num_key_value_groups`.

## Changed

- `base.py` holds the audio token ids as `AUDIO_START_TOKEN` and
  `AUDIO_END_TOKEN`, and the training batch packer reads both.
- `forward` takes a `PackedBatch` from `schemas.models.voxcpm_1_5.batch`.
- `generate` takes a `SamplerSettings` from `schemas.models.voxcpm_1_5.inference`, and
  passes its `max_patches`, `timesteps`, and `guidance_scale` to the sampler.
- Smaller methods hold the steps of `solve_euler`, `_inference`, and
  `_generate`.
- Type annotations cover the folder, and `typing.cast` wraps the torch calls
  that lack types.
- `logging` replaces `print`, `raise` replaces `assert`, and every import sits
  at the top of its module.
- Boolean parameters are keyword-only, and named constants hold the formula
  values.
- `torch.nn.attention.sdpa_kernel` replaces the deprecated
  `torch.backends.cuda.sdp_kernel` and keeps its math and cuDNN backends.
- `read_pretrained` reads the tokenizer with `PreTrainedTokenizerFast`, which
  keeps the normalizer of `tokenizer.json`. In transformers 5,
  `LlamaTokenizerFast` replaces that normalizer with its own pre-tokenizer and
  changes the ids of text with a leading space.
- The decoding step gives `scaled_dot_product_attention` a mask with one row
  for its one query, because torch 2.15 rejects a one-dimensional mask.

No other behavior changed. The CPU tests in `tests/suites/unit/models/voxcpm_1_5`
pin the outputs that this code gave before the changes.

## Refresh

1. Read the upstream diff between the source commit and the new commit.
2. Port each change by hand into the module that now holds that code.
3. Run `uv run --all-extras pytest tests/suites/unit/models/voxcpm_1_5`. Update
   `recording.json` there only for an output that upstream changed on
   purpose.
4. Update the source commit.

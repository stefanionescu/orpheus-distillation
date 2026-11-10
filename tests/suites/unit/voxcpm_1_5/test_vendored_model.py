"""The vendored VoxCPM model's public surface matches the recorded outputs on a tiny CPU model."""

from __future__ import annotations

import math
from typing import TYPE_CHECKING, Any, cast

import torch
import pytest

from src.train.voxcpm_1_5.model.text import ChineseCharacterTokenizer
from src.train.voxcpm_1_5.model.voxcpm import VoxCPMModel
from src.train.voxcpm_1_5.model.forward import LOSS_DIFF_KEY, LOSS_STOP_KEY
from src.train.voxcpm_1_5.model.generation import EXTRA_PATCHES, PATCHES_PER_TOKEN
from tests.suites.unit.voxcpm_1_5.builders import (
    MAX_LENGTH,
    PATCH_SIZE,
    HIDDEN_SIZE,
    SPEECH_TEXT,
    FORWARD_PROGRESS,
    LONG_MAX_PATCHES,
    SHORT_MAX_PATCHES,
    run_on_cpu,
    build_tiny_model,
    build_lora_config,
    build_packed_batch,
    reset_random_state,
    write_lora_weights,
    build_seeded_tensor,
    build_audio_vae_config,
    build_sampler_settings,
    write_checkpoint_folder,
    write_space_normalizer_tokenizer,
)
from tests.suites.unit.voxcpm_1_5.recording import validate_recording

if TYPE_CHECKING:
    from pathlib import Path

FORWARD_TENSOR_KEYS = (LOSS_DIFF_KEY, LOSS_STOP_KEY, "feat_gt")
PROMPT_POSITIONS = 3
PROMPT_OFFSET = 8
STEP_INPUT_OFFSET = 9
UNKNOWN_LORA_KEY = "unknown.lora_A"
CAPPED_TEXT = "ab"
"""A text short enough that its length cap leaves room in the tiny model's KV cache."""


def _list_forward_problems(model: VoxCPMModel, recording_key: str) -> list[str]:
    reset_random_state()
    outputs = model(build_packed_batch(), progress=FORWARD_PROGRESS)
    problems = [] if set(outputs) == set(FORWARD_TENSOR_KEYS) else [f"keys {sorted(outputs)}"]
    for key in FORWARD_TENSOR_KEYS:
        problems.extend(validate_recording(outputs[key], recording_key, key))
    return problems


def _generate(max_patches: int) -> torch.Tensor:
    model = build_tiny_model().eval()
    reset_random_state()
    return model.generate(SPEECH_TEXT, build_sampler_settings(max_patches))


def _build_untrained_lora_model() -> VoxCPMModel:
    model = build_tiny_model(lora_config=build_lora_config())
    with torch.no_grad():
        for name, parameter in model.named_parameters():
            if "lora_" in name:
                parameter.zero_()
    return model


def _turn_off_stop_head(model: VoxCPMModel) -> None:
    # A constant positive input to the head and a head that reads only the continue class: no step votes stop.
    with torch.no_grad():
        model.stop_proj.weight.zero_()
        model.stop_proj.bias.fill_(1.0)
        model.stop_head.weight.zero_()
        model.stop_head.weight[0].fill_(1.0)


def _list_changed_tensors(actual: dict[str, torch.Tensor], expected: dict[str, torch.Tensor]) -> list[str]:
    return sorted(
        name
        for name in actual.keys() | expected.keys()
        if name not in actual or name not in expected or not torch.equal(actual[name], expected[name])
    )


def test_forward_matches_recording() -> None:
    """The training forward pass of the base model returns the recorded losses and target features."""
    assert _list_forward_problems(build_tiny_model(), "forward") == []


def test_lora_forward_matches_recording() -> None:
    """LoRA layers on the language models, estimator, and projections change both losses as recorded."""
    assert _list_forward_problems(build_tiny_model(lora_config=build_lora_config()), "forward_lora") == []


def test_mean_mode_forward_matches() -> None:
    """The mean-velocity objective, which differentiates the estimator with `jvp`, gives the recorded losses."""
    assert _list_forward_problems(build_tiny_model(is_mean_mode=True), "forward_mean_mode") == []


def test_lora_switch_toggles_adapters() -> None:
    """Turning the LoRA layers off gives the base model's losses, and turning them on again gives the LoRA losses."""
    model = build_tiny_model(lora_config=build_lora_config())

    model.set_lora_enabled(enabled=False)
    disabled_problems = _list_forward_problems(model, "forward")
    model.set_lora_enabled(enabled=True)

    assert disabled_problems == []
    assert _list_forward_problems(model, "forward_lora") == []


def test_generate_honors_stop_head() -> None:
    """With a cap above the stop step, generation stops on the stop head and decodes the recorded waveform."""
    assert validate_recording(_generate(LONG_MAX_PATCHES), "generate") == []


def test_generate_honors_max_patches() -> None:
    """The `max_patches` setting reaches the decoding loop: a cap below the stop step shortens the waveform."""
    assert validate_recording(_generate(SHORT_MAX_PATCHES), "generate_short") == []


def test_text_length_caps_audio() -> None:
    """Without a stop vote, generation ends at six patches per text token plus ten, below a larger `max_patches`."""
    model = build_tiny_model().eval()
    _turn_off_stop_head(model)
    samples_per_patch = PATCH_SIZE * math.prod(build_audio_vae_config().decoder_rates)
    token_count = len(model.text_tokenizer(CAPPED_TEXT))

    waveform = model.generate(CAPPED_TEXT, build_sampler_settings(MAX_LENGTH))

    assert waveform.shape[-1] == int(token_count * PATCHES_PER_TOKEN + EXTRA_PATCHES) * samples_per_patch


def test_compiled_decode_step_matches() -> None:
    """One decoding step compiles into one graph, as inference does on CUDA, and matches eager mode."""
    language_model = build_tiny_model().eval().base_lm
    cache = language_model.kv_cache
    assert cache is not None
    prompt = build_seeded_tensor((1, PROMPT_POSITIONS, HIDDEN_SIZE), PROMPT_OFFSET)
    step_input = build_seeded_tensor((1, HIDDEN_SIZE), STEP_INPUT_OFFSET)
    compiled_step = torch.compile(language_model.forward_step, fullgraph=True, backend="eager")
    try:
        with torch.no_grad():
            _, prompt_cache = language_model(prompt, is_causal=True)
            cache.fill_caches(prompt_cache)
            eager_output = language_model.forward_step(step_input, torch.tensor([cache.step()]))
            eager_cache = cache.kv_cache.clone()
            cache.fill_caches(prompt_cache)
            compiled_output = compiled_step(step_input, torch.tensor([cache.step()]))
    finally:
        torch.compiler.reset()

    assert torch.equal(compiled_output, eager_output)
    assert torch.equal(cache.kv_cache, eager_cache)


def test_checkpoint_round_trip(tmp_path: Path) -> None:
    """Reading a folder with the Hub file names restores the config and every weight, the audio VAE's included.

    Args:
        tmp_path: The checkpoint folder.

    """
    written = build_tiny_model()
    write_checkpoint_folder(written, tmp_path)

    with run_on_cpu():
        model = VoxCPMModel.read_pretrained(tmp_path, optimize=False, training=False, lora_config=None)

    assert model.config == written.config
    assert _list_changed_tensors(model.state_dict(), written.state_dict()) == []


def test_tokenizer_keeps_leading_space(tmp_path: Path) -> None:
    """A tokenizer that marks spaces in its normalizer keeps a leading space as its own token.

    Args:
        tmp_path: The checkpoint folder.

    """
    write_checkpoint_folder(build_tiny_model(), tmp_path)
    write_space_normalizer_tokenizer(tmp_path)

    with run_on_cpu():
        model = VoxCPMModel.read_pretrained(tmp_path, optimize=False, training=False, lora_config=None)

    tokenizer = model.text_tokenizer
    assert isinstance(tokenizer, ChineseCharacterTokenizer)
    assert tokenizer.tokenize(" ab") == ["▁", "▁", "a", "b"]


def test_training_freezes_base_weights(tmp_path: Path) -> None:
    """Reading a checkpoint for LoRA training leaves exactly the LoRA matrices trainable.

    Args:
        tmp_path: The checkpoint folder.

    """
    write_checkpoint_folder(build_tiny_model(), tmp_path)

    with run_on_cpu():
        model = VoxCPMModel.read_pretrained(tmp_path, optimize=False, training=True, lora_config=build_lora_config())

    trainable = {name for name, parameter in model.named_parameters() if parameter.requires_grad}
    lora_matrices = {name for name, _ in model.named_parameters() if name.endswith(("lora_A", "lora_B"))}
    assert lora_matrices
    assert trainable == lora_matrices


def test_lora_weights_round_trip(tmp_path: Path) -> None:
    """Reading an adapter file fills every LoRA matrix, and an entry that names no parameter comes back as skipped.

    Args:
        tmp_path: The checkpoint folder.

    """
    adapted_model = build_tiny_model(lora_config=build_lora_config())
    written = write_lora_weights(adapted_model, tmp_path, {UNKNOWN_LORA_KEY: torch.zeros(1)})
    model = _build_untrained_lora_model()

    loaded, skipped = model.read_lora_weights(tmp_path)

    assert sorted(loaded) == written
    assert skipped == [UNKNOWN_LORA_KEY]
    assert _list_forward_problems(model, "forward_lora") == []


def test_compiled_estimator_reads_adapter(tmp_path: Path) -> None:
    """An adapter saved in training fills the diffusion estimator after inference compiles it, as it does on CUDA.

    Args:
        tmp_path: The checkpoint folder.

    """
    written = write_lora_weights(build_tiny_model(lora_config=build_lora_config()), tmp_path, {})
    model = _build_untrained_lora_model()
    estimator = model.feat_decoder.estimator
    cast("Any", model.feat_decoder).estimator = torch.compile(estimator, backend="eager")

    loaded, skipped = model.read_lora_weights(tmp_path)

    model.feat_decoder.estimator = estimator
    assert sorted(loaded) == written
    assert skipped == []
    assert _list_forward_problems(model, "forward_lora") == []


def test_missing_lora_file_raises(tmp_path: Path) -> None:
    """A folder without an adapter file raises `FileNotFoundError`.

    Args:
        tmp_path: The empty checkpoint folder.

    """
    with pytest.raises(FileNotFoundError):
        _build_untrained_lora_model().read_lora_weights(tmp_path)

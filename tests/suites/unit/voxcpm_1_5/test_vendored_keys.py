"""The vendored model keeps the state-dict keys and config fields of the published checkpoint files.

The base model loads `model.safetensors` and `audiovae.pth` with `strict=False`, so a renamed module or parameter
stays unloaded without an error. These tests catch that rename.
"""

from __future__ import annotations

from src.train.voxcpm_1_5.model.config import LoraConfig
from tests.suites.unit.voxcpm_1_5.builders import build_tiny_model, build_lora_config
from tests.suites.unit.voxcpm_1_5.recording import list_field_paths, read_recorded_keys


def test_state_dict_keys_unchanged() -> None:
    """The base model has the parameter and buffer names the checkpoint holds."""
    assert sorted(build_tiny_model().state_dict()) == read_recorded_keys("state_dict")


def test_lora_state_keys_unchanged() -> None:
    """The LoRA layers add the `lora_A` and `lora_B` names that the saved adapters hold."""
    model = build_tiny_model(lora_config=build_lora_config())

    assert sorted(model.state_dict()) == read_recorded_keys("lora_state_dict")


def test_config_fields_unchanged() -> None:
    """The model config reads and writes the keys of `config.json`."""
    fields = list_field_paths(build_tiny_model().config.model_dump(by_alias=True))

    assert sorted(fields) == read_recorded_keys("config_fields")


def test_lora_config_fields_unchanged() -> None:
    """The LoRA config reads and writes the keys of `lora_config.json`."""
    assert sorted(LoraConfig().model_dump()) == read_recorded_keys("lora_config_fields")

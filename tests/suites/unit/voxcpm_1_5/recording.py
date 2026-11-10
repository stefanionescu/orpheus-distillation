"""Recorded outputs and checkpoint keys of the vendored model, and the checks against them."""

from __future__ import annotations

import json
import math
from typing import cast
from pathlib import Path

import torch

RECORDING_PATH = Path(__file__).with_name("recording.json")
KEYS_PATH = Path(__file__).with_name("checkpoint_keys.json")
# The recording ran on the CPU in float32; the tolerance absorbs a different BLAS or thread count.
RELATIVE_TOLERANCE = 1e-5
ABSOLUTE_TOLERANCE = 1e-6
SAMPLED_ELEMENT_COUNT = 6


def validate_recording(tensor: torch.Tensor, *keys: str) -> list[str]:
    """Compare a tensor with its summary in the recording file.

    Args:
        tensor: The output to compare.
        *keys: The summary's path in the file, such as `"forward", "loss/diff"`.

    Returns:
        One line per statistic or sampled element outside the tolerance, and one for a shape mismatch.

    """
    recording = json.loads(RECORDING_PATH.read_text(encoding="utf-8"))
    for key in keys:
        recording = recording[key]
    values = tensor.detach().to(torch.float64).flatten()
    last = values.numel() - 1
    indices = {round(step * last / (SAMPLED_ELEMENT_COUNT - 1)) for step in range(SAMPLED_ELEMENT_COUNT)}
    actual = {"sum": values.sum(), "abs_sum": values.abs().sum(), "mean": values.mean()}
    actual.update({f"values.{index}": values[index] for index in sorted(indices)})
    expected = {"sum": recording["sum"], "abs_sum": recording["abs_sum"], "mean": recording["mean"]}
    expected.update({f"values.{index}": value for index, value in recording["values"].items()})
    problems = (
        [] if list(tensor.shape) == recording["shape"] else [f"shape {list(tensor.shape)} != {recording['shape']}"]
    )
    problems.extend(
        f"{name} {float(actual[name])} != {expected.get(name)}"
        for name in actual
        if name not in expected
        or not math.isclose(float(actual[name]), expected[name], rel_tol=RELATIVE_TOLERANCE, abs_tol=ABSOLUTE_TOLERANCE)
    )
    return problems


def read_recorded_keys(name: str) -> list[str]:
    """Read one recorded, sorted key list from the checkpoint keys file.

    Args:
        name: `state_dict`, `lora_state_dict`, `config_fields`, or `lora_config_fields`.

    Returns:
        The keys.

    """
    return json.loads(KEYS_PATH.read_text(encoding="utf-8"))[name]


def list_field_paths(values: dict[str, object], prefix: str = "") -> list[str]:
    """List the dotted path of every key in a nested config dump, as `config.json` spells it.

    Args:
        values: A pydantic config dump.
        prefix: The dump's path inside its parent.

    Returns:
        The paths, parents first.

    """
    paths: list[str] = []
    for key, value in values.items():
        paths.append(f"{prefix}{key}")
        if isinstance(value, dict):
            paths.extend(list_field_paths(cast("dict[str, object]", value), f"{prefix}{key}."))
    return paths

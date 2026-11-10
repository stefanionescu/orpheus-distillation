"""Low-rank adaptation (LoRA) linear layers and their injection into a module tree."""

from __future__ import annotations

import math
from typing import TYPE_CHECKING, cast, override

import torch
from torch import nn
from torch.nn import functional

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable, Iterator

# Match the init that `nn.Linear` gives its own weight.
KAIMING_NEGATIVE_SLOPE = math.sqrt(5)


class LoraLinear(nn.Module):
    """Linear layer plus a scaled low-rank update.

    It keeps the `weight` and `bias` keys of the layer it replaces, so pretrained weights load unchanged.
    """

    def __init__(self, base: nn.Linear, r: int, alpha: float = 1.0, dropout: float = 0.0) -> None:
        """Take over the weights of a linear layer and add LoRA matrices whose update starts at zero.

        Args:
            base: Linear layer to replace.
            r: Rank of the update; zero adds no update.
            alpha: Scale numerator; the update scales by `alpha / r`.
            dropout: Dropout probability before the update.

        """
        cast("Callable[[], None]", super().__init__)()
        self.in_features = base.in_features
        self.out_features = base.out_features
        self.r = r
        self.alpha = alpha
        self.base_scaling = alpha / r if r > 0 else 0.0

        # A buffer lets a switch skip the recompile, and a non-persistent one stays out of checkpoints.
        self.register_buffer("scaling", torch.tensor(self.base_scaling), persistent=False)

        self.weight = base.weight
        self.bias = base.bias

        if r > 0:
            self.lora_A = nn.Parameter(torch.zeros(r, self.in_features))
            self.lora_B = nn.Parameter(torch.zeros(self.out_features, r))
            nn.init.kaiming_uniform_(self.lora_A, a=KAIMING_NEGATIVE_SLOPE)
            nn.init.zeros_(self.lora_B)
        else:
            self.register_parameter("lora_A", None)
            self.register_parameter("lora_B", None)

        self.dropout = nn.Dropout(dropout) if dropout > 0 else nn.Identity()

    @override
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Apply the linear layer and add the scaled low-rank update.

        Args:
            x: Input, with `in_features` as its last dimension.

        Returns:
            Output, with `out_features` as its last dimension.

        """
        result = functional.linear(x, self.weight, self.bias)
        if self.r <= 0:
            return result
        lora_out = functional.linear(functional.linear(x, self.lora_A), self.lora_B)
        return result + self.dropout(lora_out) * cast("torch.Tensor", self.scaling)


def inject_lora_layers(
    root: nn.Module,
    *,
    target_submodule_names: Iterable[str],
    r: int,
    alpha: float,
    dropout: float,
) -> None:
    """Replace each target linear layer with a LoRA layer.

    A target matches the last part of a module name, so `q_proj` replaces every `*.q_proj` linear layer.

    Args:
        root: Module tree to change in place.
        target_submodule_names: Attribute names of the linear layers to replace.
        r: Rank of each LoRA layer.
        alpha: Scale numerator of each LoRA layer.
        dropout: Dropout probability of each LoRA layer.

    """
    targets = set(target_submodule_names)
    list_named_modules = cast("Callable[[], Iterator[tuple[str, nn.Module]]]", root.named_modules)
    for full_name, module in list(list_named_modules()):
        short_name = full_name.split(".")[-1]
        if not isinstance(module, nn.Linear) or short_name not in targets:
            continue
        parent = _find_parent_module(root, full_name)
        if parent is not None:
            setattr(parent, short_name, LoraLinear(base=module, r=r, alpha=alpha, dropout=dropout))


def _find_parent_module(root: nn.Module, name: str) -> nn.Module | None:
    parts = name.split(".")
    parent = root
    for part in parts[:-1]:
        if not hasattr(parent, part):
            return None
        parent = cast("nn.Module", getattr(parent, part))
    return parent

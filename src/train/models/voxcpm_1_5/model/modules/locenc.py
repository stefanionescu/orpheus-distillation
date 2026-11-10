"""Local encoder that embeds each audio patch as one language model position."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast, override

import torch
from torch import nn
import einops

from src.train.models.voxcpm_1_5.model.modules.minicpm4.model import MiniCpmModel

if TYPE_CHECKING:
    from collections.abc import Callable

    from src.train.models.voxcpm_1_5.model.modules.minicpm4.config import MiniCpmConfig

_rearrange = cast("Callable[..., torch.Tensor]", einops.rearrange)


class VoxCPMLocEnc(nn.Module):
    """Bidirectional MiniCPM over a learned token and one patch; the token output is the embedding."""

    def __init__(self, config: MiniCpmConfig, input_dim: int = 64) -> None:
        """Build the special token, the input projection, and the transformer.

        Args:
            config: Transformer config, with no token embedding.
            input_dim: Size of one latent frame.

        Raises:
            ValueError: When the config has a vocabulary.

        """
        cast("Callable[[], None]", super().__init__)()
        self.config = config
        self.special_token = nn.Parameter(torch.randn(1, 1, 1, config.hidden_size))
        self.in_proj = nn.Linear(input_dim, config.hidden_size, bias=True)

        if config.vocab_size != 0:
            message = "vocab_size must be 0 for local encoder"
            raise ValueError(message)
        self.encoder = MiniCpmModel(config)

    @override
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Embed every patch.

        Args:
            x: Patches, shaped (batch, positions, patch_size, input_dim).

        Returns:
            Embeddings, shaped (batch, positions, hidden_size).

        """
        batch_size, time_steps, _, _ = x.shape

        x = self.in_proj(x)
        special_tokens = self.special_token.expand(batch_size, time_steps, 1, -1)
        x = torch.cat([special_tokens, x], dim=2)
        x = _rearrange(x, "b t p c -> (b t) p c")
        outputs, _ = self.encoder(x, is_causal=False)
        cls_output = outputs[:, 0, :]
        return _rearrange(cls_output, "(b t) c -> b t c", b=batch_size)

"""Prompts about fashion, clothing, and style, in reading order."""

from __future__ import annotations

from config.prompts.fashion.outfits import OUTFITS
from config.prompts.fashion.wardrobe import WARDROBE
from config.prompts.fashion.occasions import OCCASIONS
from config.prompts.fashion.reactions import REACTIONS

FASHION: list[str] = [
    *WARDROBE,
    *OUTFITS,
    *OCCASIONS,
    *REACTIONS,
]

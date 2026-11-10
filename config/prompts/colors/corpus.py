"""Prompts mentioning colors, shades, and visual descriptions, in reading order."""

from __future__ import annotations

from config.prompts.colors.hues import HUES
from config.prompts.colors.shades import SHADES
from config.prompts.colors.palettes import PALETTES

COLORS: list[str] = [
    *SHADES,
    *PALETTES,
    *HUES,
]

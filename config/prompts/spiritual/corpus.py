"""Prompts about spirituality, mindfulness, and inner peace, in reading order."""

from __future__ import annotations

from config.prompts.spiritual.signs import SIGNS
from config.prompts.spiritual.ceremony import CEREMONY
from config.prompts.spiritual.shifting import SHIFTING
from config.prompts.spiritual.astrology import ASTROLOGY
from config.prompts.spiritual.awakening import AWAKENING

SPIRITUAL: list[str] = [
    *ASTROLOGY,
    *AWAKENING,
    *SIGNS,
    *SHIFTING,
    *CEREMONY,
]

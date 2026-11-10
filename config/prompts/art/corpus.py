"""Prompts about art, creativity, and artistic expression, in reading order."""

from __future__ import annotations

from config.prompts.art.craft import CRAFT
from config.prompts.art.studio import STUDIO
from config.prompts.art.sketches import SKETCHES
from config.prompts.art.techniques import TECHNIQUES
from config.prompts.art.appreciation import APPRECIATION
from config.prompts.art.masterpieces import MASTERPIECES

ART: list[str] = [
    *SKETCHES,
    *APPRECIATION,
    *TECHNIQUES,
    *MASTERPIECES,
    *CRAFT,
    *STUDIO,
]

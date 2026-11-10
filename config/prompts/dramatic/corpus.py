"""Prompts with dramatic, theatrical, or exaggerated expressions, in reading order."""

from __future__ import annotations

from config.prompts.dramatic.gasps import GASPS
from config.prompts.dramatic.encores import ENCORES
from config.prompts.dramatic.monologues import MONOLOGUES
from config.prompts.dramatic.confrontations import CONFRONTATIONS

DRAMATIC: list[str] = [
    *GASPS,
    *CONFRONTATIONS,
    *MONOLOGUES,
    *ENCORES,
]

"""Prompts expressing confusion and puzzlement, in reading order."""

from __future__ import annotations

from config.prompts.confused.moods import MOODS
from config.prompts.confused.analogies import ANALOGIES
from config.prompts.confused.bafflement import BAFFLEMENT
from config.prompts.confused.puzzlement import PUZZLEMENT
from config.prompts.confused.temperaments import TEMPERAMENTS

CONFUSED: list[str] = [
    *PUZZLEMENT,
    *BAFFLEMENT,
    *ANALOGIES,
    *MOODS,
    *TEMPERAMENTS,
]

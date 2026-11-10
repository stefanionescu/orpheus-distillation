"""Prompts about animals, wildlife, and nature, in reading order."""

from __future__ import annotations

from config.prompts.animals.marvels import MARVELS
from config.prompts.animals.stories import STORIES
from config.prompts.animals.glimpses import GLIMPSES
from config.prompts.animals.oddities import ODDITIES
from config.prompts.animals.curiosities import CURIOSITIES

ANIMALS: list[str] = [
    *GLIMPSES,
    *STORIES,
    *CURIOSITIES,
    *ODDITIES,
    *MARVELS,
]

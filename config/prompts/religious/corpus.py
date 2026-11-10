"""Prompts about religion, faith, and spiritual practices, in reading order."""

from __future__ import annotations

from config.prompts.religious.liturgy import LITURGY
from config.prompts.religious.worship import WORSHIP
from config.prompts.religious.devotion import DEVOTION
from config.prompts.religious.denominations import DENOMINATIONS

RELIGIOUS: list[str] = [
    *WORSHIP,
    *DEVOTION,
    *LITURGY,
    *DENOMINATIONS,
]

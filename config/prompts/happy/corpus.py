"""Prompts expressing happiness and joy, in reading order."""

from __future__ import annotations

from config.prompts.happy.cheer import CHEER
from config.prompts.happy.delight import DELIGHT
from config.prompts.happy.elation import ELATION

HAPPY: list[str] = [
    *CHEER,
    *DELIGHT,
    *ELATION,
]

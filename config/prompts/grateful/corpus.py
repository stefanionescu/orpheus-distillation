"""Prompts expressing gratitude and appreciation, in reading order."""

from __future__ import annotations

from config.prompts.grateful.thanks import THANKS
from config.prompts.grateful.blessings import BLESSINGS
from config.prompts.grateful.overwhelmed import OVERWHELMED

GRATEFUL: list[str] = [
    *THANKS,
    *OVERWHELMED,
    *BLESSINGS,
]

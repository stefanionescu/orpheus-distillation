"""Prompts expressing frustration and annoyance, in reading order."""

from __future__ import annotations

from config.prompts.frustrated.kinds import KINDS
from config.prompts.frustrated.phrases import PHRASES

FRUSTRATED: list[str] = [
    *PHRASES,
    *KINDS,
]

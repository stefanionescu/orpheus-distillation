"""Prompts expressing anger and fury emotions, in reading order."""

from __future__ import annotations

from config.prompts.angry.kinds import KINDS
from config.prompts.angry.phrases import PHRASES

ANGRY: list[str] = [
    *PHRASES,
    *KINDS,
]

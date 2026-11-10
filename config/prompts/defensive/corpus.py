"""Prompts expressing defensiveness and self-justification, in reading order."""

from __future__ import annotations

from config.prompts.defensive.appeals import APPEALS
from config.prompts.defensive.denials import DENIALS
from config.prompts.defensive.rebuttals import REBUTTALS

DEFENSIVE: list[str] = [
    *DENIALS,
    *REBUTTALS,
    *APPEALS,
]

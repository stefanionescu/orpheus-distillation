"""Prompts with vocal reactions, interjections, and filler sounds, in reading order."""

from __future__ import annotations

from config.prompts.reactions.responses import RESPONSES
from config.prompts.reactions.epiphanies import EPIPHANIES
from config.prompts.reactions.interjections import INTERJECTIONS

REACTIONS: list[str] = [
    *INTERJECTIONS,
    *RESPONSES,
    *EPIPHANIES,
]

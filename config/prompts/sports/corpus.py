"""Prompts about sports, athletics, and competitive games, in reading order."""

from __future__ import annotations

from config.prompts.sports.calls import CALLS
from config.prompts.sports.banter import BANTER
from config.prompts.sports.jargon import JARGON
from config.prompts.sports.vocabulary import VOCABULARY
from config.prompts.sports.disciplines import DISCIPLINES

SPORTS: list[str] = [
    *CALLS,
    *JARGON,
    *DISCIPLINES,
    *VOCABULARY,
    *BANTER,
]

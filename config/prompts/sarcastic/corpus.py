"""Prompts with sarcastic and ironic tones, in reading order."""

from __future__ import annotations

from config.prompts.sarcastic.barbs import BARBS
from config.prompts.sarcastic.quips import QUIPS
from config.prompts.sarcastic.everyday import EVERYDAY
from config.prompts.sarcastic.workplace import WORKPLACE

SARCASTIC: list[str] = [
    *QUIPS,
    *WORKPLACE,
    *EVERYDAY,
    *BARBS,
]

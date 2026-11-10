"""Prompts containing profanity and explicit language, in reading order."""

from __future__ import annotations

from config.prompts.cursing.rants import RANTS
from config.prompts.cursing.roasts import ROASTS
from config.prompts.cursing.swears import SWEARS
from config.prompts.cursing.insults import INSULTS
from config.prompts.cursing.tirades import TIRADES
from config.prompts.cursing.outbursts import OUTBURSTS

CURSING: list[str] = [
    *SWEARS,
    *RANTS,
    *INSULTS,
    *TIRADES,
    *OUTBURSTS,
    *ROASTS,
]

"""Prompts with sassy, sharp, or cutting tones, in reading order."""

from __future__ import annotations

from config.prompts.bitchy.jabs import JABS
from config.prompts.bitchy.retorts import RETORTS

BITCHY: list[str] = [
    *JABS,
    *RETORTS,
]

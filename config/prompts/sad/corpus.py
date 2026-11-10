"""Prompts expressing sadness and heartbreak, in reading order."""

from __future__ import annotations

from config.prompts.sad.loss import LOSS
from config.prompts.sad.waves import WAVES
from config.prompts.sad.sorrow import SORROW
from config.prompts.sad.despair import DESPAIR
from config.prompts.sad.struggles import STRUGGLES

SAD: list[str] = [
    *SORROW,
    *STRUGGLES,
    *LOSS,
    *DESPAIR,
    *WAVES,
]

"""Prompts containing slang, informal language, and colloquialisms, in reading order."""

from __future__ import annotations

from config.prompts.slang.raw import RAW
from config.prompts.slang.banter import BANTER
from config.prompts.slang.regional import REGIONAL
from config.prompts.slang.unfiltered import UNFILTERED
from config.prompts.slang.generations import GENERATIONS

SLANG: list[str] = [
    *GENERATIONS,
    *REGIONAL,
    *BANTER,
    *RAW,
    *UNFILTERED,
]

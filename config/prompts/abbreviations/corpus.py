"""Prompts containing common abbreviations, acronyms, and initialisms, in reading order."""

from __future__ import annotations

from config.prompts.abbreviations.brief import BRIEF
from config.prompts.abbreviations.extended import EXTENDED
from config.prompts.abbreviations.sentences import SENTENCES

ABBREVIATIONS: list[str] = [
    *BRIEF,
    *SENTENCES,
    *EXTENDED,
]

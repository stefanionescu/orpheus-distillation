"""Prompts with unique pronunciations, onomatopoeia, and special sounds, in reading order."""

from __future__ import annotations

from config.prompts.unique.silent import SILENT
from config.prompts.unique.jumbles import JUMBLES
from config.prompts.unique.medleys import MEDLEYS
from config.prompts.unique.twisters import TWISTERS
from config.prompts.unique.loanwords import LOANWORDS
from config.prompts.unique.curiosities import CURIOSITIES
from config.prompts.unique.combinations import COMBINATIONS

UNIQUE_PRONUNCIATIONS: list[str] = [
    *SILENT,
    *TWISTERS,
    *JUMBLES,
    *LOANWORDS,
    *COMBINATIONS,
    *MEDLEYS,
    *CURIOSITIES,
]

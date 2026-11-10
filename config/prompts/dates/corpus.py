"""Prompts containing dates, years, and calendar references, in reading order."""

from __future__ import annotations

from config.prompts.dates.formats import FORMATS
from config.prompts.dates.expressions import EXPRESSIONS

DATES: list[str] = [
    *FORMATS,
    *EXPRESSIONS,
]

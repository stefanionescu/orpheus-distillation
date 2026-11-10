"""Prompts containing measurement units and quantities, in reading order."""

from __future__ import annotations

from config.prompts.units.industry import INDUSTRY
from config.prompts.units.measures import MEASURES
from config.prompts.units.astronomy import ASTRONOMY
from config.prompts.units.engineering import ENGINEERING

UNITS: list[str] = [
    *MEASURES,
    *ENGINEERING,
    *ASTRONOMY,
    *INDUSTRY,
]

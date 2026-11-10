"""Prompts about chemistry, elements, and chemical processes, in reading order."""

from __future__ import annotations

from config.prompts.chemistry.analysis import ANALYSIS
from config.prompts.chemistry.formulas import FORMULAS
from config.prompts.chemistry.compounds import COMPOUNDS
from config.prompts.chemistry.molecules import MOLECULES
from config.prompts.chemistry.principles import PRINCIPLES

CHEMISTRY: list[str] = [
    *FORMULAS,
    *PRINCIPLES,
    *ANALYSIS,
    *COMPOUNDS,
    *MOLECULES,
]

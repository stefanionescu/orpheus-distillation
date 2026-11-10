"""Prompts about jobs, careers, and occupations, in reading order."""

from __future__ import annotations

from config.prompts.occupations.roles import ROLES
from config.prompts.occupations.careers import CAREERS
from config.prompts.occupations.workdays import WORKDAYS

OCCUPATIONS: list[str] = [
    *ROLES,
    *CAREERS,
    *WORKDAYS,
]

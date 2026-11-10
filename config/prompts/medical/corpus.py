"""Prompts about medical topics, healthcare, and health conditions, in reading order."""

from __future__ import annotations

from config.prompts.medical.cases import CASES
from config.prompts.medical.terms import TERMS
from config.prompts.medical.rounds import ROUNDS
from config.prompts.medical.diagnoses import DIAGNOSES
from config.prompts.medical.treatments import TREATMENTS
from config.prompts.medical.specialties import SPECIALTIES

MEDICAL: list[str] = [
    *TERMS,
    *SPECIALTIES,
    *CASES,
    *DIAGNOSES,
    *ROUNDS,
    *TREATMENTS,
]

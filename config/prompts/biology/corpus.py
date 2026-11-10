"""Prompts about biology, life sciences, and organisms, in reading order."""

from __future__ import annotations

from config.prompts.biology.ecology import ECOLOGY
from config.prompts.biology.diversity import DIVERSITY
from config.prompts.biology.molecules import MOLECULES
from config.prompts.biology.essentials import ESSENTIALS
from config.prompts.biology.immunology import IMMUNOLOGY
from config.prompts.biology.physiology import PHYSIOLOGY
from config.prompts.biology.microbiology import MICROBIOLOGY
from config.prompts.biology.neuroscience import NEUROSCIENCE

BIOLOGY: list[str] = [
    *ESSENTIALS,
    *PHYSIOLOGY,
    *IMMUNOLOGY,
    *ECOLOGY,
    *DIVERSITY,
    *MICROBIOLOGY,
    *NEUROSCIENCE,
    *MOLECULES,
]

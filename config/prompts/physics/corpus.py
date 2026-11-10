"""Prompts about physics, mechanics, and physical phenomena, in reading order."""

from __future__ import annotations

from config.prompts.physics.cosmos import COSMOS
from config.prompts.physics.mechanics import MECHANICS
from config.prompts.physics.particles import PARTICLES
from config.prompts.physics.phenomena import PHENOMENA
from config.prompts.physics.relativity import RELATIVITY

PHYSICS: list[str] = [
    *MECHANICS,
    *RELATIVITY,
    *PHENOMENA,
    *PARTICLES,
    *COSMOS,
]

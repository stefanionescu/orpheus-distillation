"""Prompts about fitness, exercise, and physical health, in reading order."""

from __future__ import annotations

from config.prompts.fitness.gym import GYM
from config.prompts.fitness.mobility import MOBILITY
from config.prompts.fitness.supplements import SUPPLEMENTS

FITNESS: list[str] = [
    *GYM,
    *SUPPLEMENTS,
    *MOBILITY,
]

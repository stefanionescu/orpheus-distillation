"""Prompts containing time references, durations, and schedules, in reading order."""

from __future__ import annotations

from config.prompts.time.clock import CLOCK
from config.prompts.time.routines import ROUTINES
from config.prompts.time.deadlines import DEADLINES
from config.prompts.time.precision import PRECISION
from config.prompts.time.scenarios import SCENARIOS

TIME: list[str] = [
    *CLOCK,
    *ROUTINES,
    *DEADLINES,
    *SCENARIOS,
    *PRECISION,
]

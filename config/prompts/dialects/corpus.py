"""Prompts featuring regional dialects and accented speech patterns, in reading order."""

from __future__ import annotations

from config.prompts.dialects.local import LOCAL
from config.prompts.dialects.reprises import REPRISES
from config.prompts.dialects.southern import SOUTHERN
from config.prompts.dialects.worldwide import WORLDWIDE
from config.prompts.dialects.northeastern import NORTHEASTERN

DIALECTS: list[str] = [
    *SOUTHERN,
    *NORTHEASTERN,
    *WORLDWIDE,
    *LOCAL,
    *REPRISES,
]

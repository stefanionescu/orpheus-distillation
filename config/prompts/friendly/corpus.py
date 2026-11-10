"""Prompts expressing friendliness and warmth, in reading order."""

from __future__ import annotations

from config.prompts.friendly.plans import PLANS
from config.prompts.friendly.cheers import CHEERS
from config.prompts.friendly.greetings import GREETINGS
from config.prompts.friendly.appreciation import APPRECIATION

FRIENDLY: list[str] = [
    *GREETINGS,
    *APPRECIATION,
    *PLANS,
    *CHEERS,
]

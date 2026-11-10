"""Prompts expressing tiredness and exhaustion, in reading order."""

from __future__ import annotations

from config.prompts.tired.pleas import PLEAS
from config.prompts.tired.drowsy import DROWSY
from config.prompts.tired.burnout import BURNOUT
from config.prompts.tired.ravings import RAVINGS
from config.prompts.tired.collapse import COLLAPSE
from config.prompts.tired.overwork import OVERWORK
from config.prompts.tired.scenarios import SCENARIOS
from config.prompts.tired.weariness import WEARINESS
from config.prompts.tired.caretakers import CARETAKERS
from config.prompts.tired.frustration import FRUSTRATION

TIRED: list[str] = [
    *DROWSY,
    *WEARINESS,
    *BURNOUT,
    *OVERWORK,
    *SCENARIOS,
    *PLEAS,
    *FRUSTRATION,
    *CARETAKERS,
    *COLLAPSE,
    *RAVINGS,
]

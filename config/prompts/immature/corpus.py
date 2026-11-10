"""Prompts with immature and childish expressions, in reading order."""

from __future__ import annotations

from config.prompts.immature.sagas import SAGAS
from config.prompts.immature.pranks import PRANKS
from config.prompts.immature.giggles import GIGGLES
from config.prompts.immature.whining import WHINING

IMMATURE: list[str] = [
    *GIGGLES,
    *SAGAS,
    *PRANKS,
    *WHINING,
]

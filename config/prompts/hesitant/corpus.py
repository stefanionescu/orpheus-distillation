"""Prompts expressing hesitation and uncertainty, in reading order."""

from __future__ import annotations

from config.prompts.hesitant.doubts import DOUBTS
from config.prompts.hesitant.pauses import PAUSES
from config.prompts.hesitant.qualms import QUALMS
from config.prompts.hesitant.misgivings import MISGIVINGS

HESITANT: list[str] = [
    *DOUBTS,
    *QUALMS,
    *MISGIVINGS,
    *PAUSES,
]

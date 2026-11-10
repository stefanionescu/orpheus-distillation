"""Prompts with flirtatious and romantic tones, in reading order."""

from __future__ import annotations

from config.prompts.flirty.rough import ROUGH
from config.prompts.flirty.openers import OPENERS
from config.prompts.flirty.worship import WORSHIP
from config.prompts.flirty.afterglow import AFTERGLOW
from config.prompts.flirty.intensity import INTENSITY

FLIRTY: list[str] = [
    *OPENERS,
    *AFTERGLOW,
    *WORSHIP,
    *ROUGH,
    *INTENSITY,
]

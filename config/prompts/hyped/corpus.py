"""Prompts expressing excitement and enthusiasm, in reading order."""

from __future__ import annotations

from config.prompts.hyped.buzz import BUZZ
from config.prompts.hyped.triumphs import TRIUMPHS
from config.prompts.hyped.victories import VICTORIES
from config.prompts.hyped.jubilation import JUBILATION
from config.prompts.hyped.milestones import MILESTONES
from config.prompts.hyped.celebrations import CELEBRATIONS

HYPED: list[str] = [
    *BUZZ,
    *CELEBRATIONS,
    *VICTORIES,
    *MILESTONES,
    *TRIUMPHS,
    *JUBILATION,
]

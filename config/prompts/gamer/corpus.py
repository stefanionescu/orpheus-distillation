"""Prompts about gaming, video games, and gamer culture, in reading order."""

from __future__ import annotations

from config.prompts.gamer.banter import BANTER
from config.prompts.gamer.bosses import BOSSES
from config.prompts.gamer.ranked import RANKED
from config.prompts.gamer.releases import RELEASES
from config.prompts.gamer.community import COMMUNITY
from config.prompts.gamer.franchises import FRANCHISES

GAMER: list[str] = [
    *BANTER,
    *RANKED,
    *COMMUNITY,
    *BOSSES,
    *FRANCHISES,
    *RELEASES,
]

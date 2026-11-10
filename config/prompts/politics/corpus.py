"""Prompts about politics, government, and civic topics, in reading order."""

from __future__ import annotations

from config.prompts.politics.campaigns import CAMPAIGNS
from config.prompts.politics.democracy import DEMOCRACY
from config.prompts.politics.ideologies import IDEOLOGIES
from config.prompts.politics.propaganda import PROPAGANDA
from config.prompts.politics.statecraft import STATECRAFT
from config.prompts.politics.bureaucracy import BUREAUCRACY

POLITICS: list[str] = [
    *DEMOCRACY,
    *IDEOLOGIES,
    *CAMPAIGNS,
    *PROPAGANDA,
    *STATECRAFT,
    *BUREAUCRACY,
]

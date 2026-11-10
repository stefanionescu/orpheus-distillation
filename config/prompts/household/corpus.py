"""Prompts about household items, chores, and domestic life, in reading order."""

from __future__ import annotations

from config.prompts.household.chores import CHORES
from config.prompts.household.storage import STORAGE
from config.prompts.household.fixtures import FIXTURES
from config.prompts.household.surfaces import SURFACES
from config.prompts.household.appliances import APPLIANCES
from config.prompts.household.renovations import RENOVATIONS

HOUSEHOLD: list[str] = [
    *CHORES,
    *RENOVATIONS,
    *FIXTURES,
    *APPLIANCES,
    *SURFACES,
    *STORAGE,
]

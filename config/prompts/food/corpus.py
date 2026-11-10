"""Prompts about food, cooking, and cuisine, in reading order."""

from __future__ import annotations

from config.prompts.food.dishes import DISHES
from config.prompts.food.grains import GRAINS
from config.prompts.food.spices import SPICES
from config.prompts.food.staples import STAPLES
from config.prompts.food.cuisines import CUISINES
from config.prompts.food.proteins import PROTEINS
from config.prompts.food.regional import REGIONAL
from config.prompts.food.fermented import FERMENTED
from config.prompts.food.botanicals import BOTANICALS
from config.prompts.food.seasonings import SEASONINGS
from config.prompts.food.sweeteners import SWEETENERS

FOOD: list[str] = [
    *STAPLES,
    *DISHES,
    *SEASONINGS,
    *GRAINS,
    *FERMENTED,
    *PROTEINS,
    *SWEETENERS,
    *SPICES,
    *CUISINES,
    *BOTANICALS,
    *REGIONAL,
]

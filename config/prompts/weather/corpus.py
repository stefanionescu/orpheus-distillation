"""Prompts about weather, climate, and atmospheric conditions, in reading order."""

from __future__ import annotations

from config.prompts.weather.storms import STORMS
from config.prompts.weather.climate import CLIMATE
from config.prompts.weather.seasons import SEASONS
from config.prompts.weather.forecast import FORECAST

WEATHER: list[str] = [
    *FORECAST,
    *STORMS,
    *SEASONS,
    *CLIMATE,
]

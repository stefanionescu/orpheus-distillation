"""Prompts about mobile apps, software, and digital services, in reading order."""

from __future__ import annotations

from config.prompts.apps.services import SERVICES
from config.prompts.apps.platforms import PLATFORMS
from config.prompts.apps.technology import TECHNOLOGY

APPS: list[str] = [
    *PLATFORMS,
    *SERVICES,
    *TECHNOLOGY,
]

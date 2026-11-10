"""Prompts containing personal names and proper nouns, in reading order."""

from __future__ import annotations

from config.prompts.names.brands import BRANDS
from config.prompts.names.cities import CITIES
from config.prompts.names.titles import TITLES
from config.prompts.names.cultures import CULTURES
from config.prompts.names.diaspora import DIASPORA
from config.prompts.names.everyday import EVERYDAY
from config.prompts.names.heritage import HERITAGE
from config.prompts.names.surnames import SURNAMES
from config.prompts.names.countries import COUNTRIES
from config.prompts.names.fictional import FICTIONAL
from config.prompts.names.nicknames import NICKNAMES
from config.prompts.names.conversations import CONVERSATIONS
from config.prompts.names.international import INTERNATIONAL

NAMES: list[str] = [
    *EVERYDAY,
    *HERITAGE,
    *CULTURES,
    *SURNAMES,
    *TITLES,
    *NICKNAMES,
    *CITIES,
    *COUNTRIES,
    *FICTIONAL,
    *CONVERSATIONS,
    *BRANDS,
    *INTERNATIONAL,
    *DIASPORA,
]

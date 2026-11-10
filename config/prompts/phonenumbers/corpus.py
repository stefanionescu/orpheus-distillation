"""Prompts containing phone numbers and telephone formats, in reading order."""

from __future__ import annotations

from config.prompts.phonenumbers.domestic import DOMESTIC
from config.prompts.phonenumbers.overseas import OVERSEAS
from config.prompts.phonenumbers.international import INTERNATIONAL

PHONE_NUMBERS: list[str] = [
    *DOMESTIC,
    *INTERNATIONAL,
    *OVERSEAS,
]

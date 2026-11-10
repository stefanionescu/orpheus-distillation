"""Prompts containing email addresses and email-related content, in reading order."""

from __future__ import annotations

from config.prompts.emails.addresses import ADDRESSES
from config.prompts.emails.exclamations import EXCLAMATIONS
from config.prompts.emails.instructions import INSTRUCTIONS

EMAILS: list[str] = [
    *ADDRESSES,
    *INSTRUCTIONS,
    *EXCLAMATIONS,
]

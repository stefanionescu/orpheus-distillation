"""Prompts about legal matters, courts, and law, in reading order."""

from __future__ import annotations

from config.prompts.legal.rights import RIGHTS
from config.prompts.legal.courtroom import COURTROOM
from config.prompts.legal.testimony import TESTIMONY
from config.prompts.legal.sentencing import SENTENCING

LEGAL: list[str] = [
    *COURTROOM,
    *TESTIMONY,
    *SENTENCING,
    *RIGHTS,
]

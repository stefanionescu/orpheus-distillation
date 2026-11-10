"""Prompts with condescending or patronizing tones, in reading order."""

from __future__ import annotations

from config.prompts.condescending.remarks import REMARKS
from config.prompts.condescending.lectures import LECTURES
from config.prompts.condescending.questions import QUESTIONS

CONDESCENDING: list[str] = [
    *REMARKS,
    *QUESTIONS,
    *LECTURES,
]

"""Prompts about therapy, mental health, and counseling, in reading order."""

from __future__ import annotations

from config.prompts.therapy.trauma import TRAUMA
from config.prompts.therapy.sessions import SESSIONS
from config.prompts.therapy.cognitive import COGNITIVE
from config.prompts.therapy.humanistic import HUMANISTIC
from config.prompts.therapy.techniques import TECHNIQUES
from config.prompts.therapy.mindfulness import MINDFULNESS

THERAPY: list[str] = [
    *COGNITIVE,
    *TRAUMA,
    *HUMANISTIC,
    *MINDFULNESS,
    *TECHNIQUES,
    *SESSIONS,
]

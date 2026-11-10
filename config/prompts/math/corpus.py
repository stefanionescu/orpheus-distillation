"""Prompts containing mathematical expressions and calculations, in reading order."""

from __future__ import annotations

from config.prompts.math.logic import LOGIC
from config.prompts.math.drills import DRILLS
from config.prompts.math.analysis import ANALYSIS
from config.prompts.math.topology import TOPOLOGY
from config.prompts.math.equations import EQUATIONS
from config.prompts.math.arithmetic import ARITHMETIC
from config.prompts.math.structures import STRUCTURES
from config.prompts.math.expressions import EXPRESSIONS
from config.prompts.math.cryptography import CRYPTOGRAPHY

MATH: list[str] = [
    *ARITHMETIC,
    *EXPRESSIONS,
    *DRILLS,
    *ANALYSIS,
    *EQUATIONS,
    *STRUCTURES,
    *TOPOLOGY,
    *LOGIC,
    *CRYPTOGRAPHY,
]

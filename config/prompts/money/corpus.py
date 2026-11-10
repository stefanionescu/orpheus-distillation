"""Prompts containing monetary values, prices, and financial terms, in reading order."""

from __future__ import annotations

from config.prompts.money.taxes import TAXES
from config.prompts.money.amounts import AMOUNTS
from config.prompts.money.budgets import BUDGETS
from config.prompts.money.markets import MARKETS

MONEY: list[str] = [
    *AMOUNTS,
    *MARKETS,
    *BUDGETS,
    *TAXES,
]

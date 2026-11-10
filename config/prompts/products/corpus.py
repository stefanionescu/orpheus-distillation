"""Prompts about products, brands, and consumer goods, in reading order."""

from __future__ import annotations

from config.prompts.products.goods import GOODS
from config.prompts.products.devices import DEVICES

PRODUCTS: list[str] = [
    *DEVICES,
    *GOODS,
]

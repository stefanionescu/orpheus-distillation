"""LoRA adapter defaults."""

from __future__ import annotations

LORA_RANK = 48
LORA_ALPHA = 48
LORA_DROPOUT = 0.05
LORA_TARGET_MODULES = ("q_proj", "v_proj", "k_proj", "o_proj")
LORA_ENABLE_LM = True
LORA_ENABLE_DIT = True
LORA_ENABLE_PROJ = True

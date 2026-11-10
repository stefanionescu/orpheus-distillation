"""Checkpoint folder and file names."""

from __future__ import annotations

CHECKPOINTS_FOLDER = "checkpoints"
EVENTS_FOLDER = "events"
NEWEST_LINK = "newest"
STEP_PREFIX = "step_"
STEP_TEMPLATE = STEP_PREFIX + "{step:07d}"
LORA_CONFIG_FILE = "lora_config.json"
OPTIMIZER_STATE_FILE = "optimizer.pth"
SCHEDULER_STATE_FILE = "scheduler.pth"
TRAINING_STATE_FILE = "training_state.json"
LORA_PARAMETER_MARKER = "lora_"
TRAINING_STATE_STEP_KEY = "step"

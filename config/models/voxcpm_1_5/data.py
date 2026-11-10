"""Manifest names, keys, and clip length bounds."""

from __future__ import annotations

MANIFESTS_FOLDER = "manifests"
MANIFEST_AUDIO_FOLDER = "audio"
TRAIN_MANIFEST_FILE = "train.jsonl"
VAL_MANIFEST_FILE = "val.jsonl"
AUDIO_KEY = "audio"
TEXT_KEY = "text"
DURATION_KEY = "duration"
VOICE_KEY = "voice"
MIN_DURATION_SECONDS = 0.5
MAX_DURATION_SECONDS = 30.0
VAL_SPLIT = 0.0
SPLIT_SEED = 42
TOKENIZER_FOLDER = "tokenizer"
TOKENIZER_FILES = ("tokenizer.json", "tokenizer_config.json", "special_tokens_map.json")

"""Names of the WebDataset shards that both commands use."""

from __future__ import annotations

SHARDS_FOLDER = "shards"
SHARD_NAME_PREFIX = "shard-"
SHARD_INDEX_WIDTH = 6
SHARD_EXTENSION = ".tar"
SHARD_GLOB = f"{SHARD_NAME_PREFIX}*{SHARD_EXTENSION}"
RECORD_EXTENSION = ".json"
AUDIO_EXTENSION = ".wav"

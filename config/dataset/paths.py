"""Names of the files and folders in the output folder."""

from __future__ import annotations

OUTPUT_FOLDER = "dataset_output"
AUDIO_FOLDER = "audio"
STATS_FILE = "stats.json"
FINGERPRINT_FILE = "fingerprint.json"
KEY_PREFIX = "clip_"
KEY_WIDTH = 5
AUDIO_FILE_TEMPLATE = "{key}_{speaker}{extension}"
AUDIO_FILE_GLOB = "*.wav"

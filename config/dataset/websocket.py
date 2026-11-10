"""Keys and markers of the Orpheus WebSocket protocol, spelled as the server spells them."""

from __future__ import annotations

END_MESSAGE = "__END__"
MESSAGE_TYPE_KEY = "type"
MESSAGE_ERROR_TYPE = "error"
MESSAGE_AUDIO_END_TYPE = "audio_end"
MESSAGE_ERROR_KEYS = ("message", "error", "detail")
MESSAGE_ERROR_KEY = "error"
REQUEST_TEXT_KEY = "text"
REQUEST_VOICE_KEY = "voice"
SETTINGS_VOICE_KEY = "voice"
SETTINGS_TRIM_SILENCE_KEY = "trim_silence"
SETTINGS_TEMPERATURE_KEY = "temperature"
SETTINGS_TOP_P_KEY = "top_p"
SETTINGS_REPETITION_PENALTY_KEY = "repetition_penalty"
SETTINGS_PRESPEECH_PAD_KEY = "prespeech_pad_ms"
TEXT_ERROR_MARKERS = ("error", "fail")

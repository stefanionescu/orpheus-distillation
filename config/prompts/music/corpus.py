"""Prompts about music, songs, and musical instruments, in reading order."""

from __future__ import annotations

from config.prompts.music.albums import ALBUMS
from config.prompts.music.genres import GENRES
from config.prompts.music.scenes import SCENES
from config.prompts.music.artists import ARTISTS
from config.prompts.music.history import HISTORY
from config.prompts.music.legends import LEGENDS
from config.prompts.music.performers import PERFORMERS
from config.prompts.music.discoveries import DISCOVERIES

MUSIC: list[str] = [
    *ARTISTS,
    *GENRES,
    *HISTORY,
    *ALBUMS,
    *PERFORMERS,
    *DISCOVERIES,
    *SCENES,
    *LEGENDS,
]

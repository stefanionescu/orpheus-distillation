"""Records of the files that the prepare command writes."""

from __future__ import annotations

from typing import TYPE_CHECKING
from dataclasses import dataclass

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Mapping


@dataclass(frozen=True)
class ManifestEntry:
    """One manifest line. Each field name is a stored JSON key.

    Attributes:
        audio: Path of the WAV file.
        text: Text that the clip reads.
        duration: Length in seconds.
        voice: Voice.

    """

    audio: str
    text: str
    duration: float
    voice: str


@dataclass(frozen=True)
class ManifestStats:
    """Totals of the kept clips.

    Attributes:
        clip_count: Clip count.
        hours: Total length in hours.
        clips_per_voice: Clip count per voice.
        hours_per_voice: Length in hours per voice.

    """

    clip_count: int
    hours: float
    clips_per_voice: Mapping[str, int]
    hours_per_voice: Mapping[str, float]


@dataclass(frozen=True)
class ManifestFiles:
    """The manifests that one prepare run writes.

    Attributes:
        train_manifest_path: Training manifest.
        val_manifest_path: Validation manifest, or None when the split keeps no clip.
        stats: Totals of every kept clip.

    """

    train_manifest_path: Path
    val_manifest_path: Path | None
    stats: ManifestStats


@dataclass(frozen=True)
class PreparedInputs:
    """The files that the prepare command writes for the train command.

    Attributes:
        train_manifest_path: Training manifest.
        val_manifest_path: Validation manifest, or None when the split keeps no clip.
        tokenizer_folder: Copied tokenizer files.

    """

    train_manifest_path: Path
    val_manifest_path: Path | None
    tokenizer_folder: Path

"""Training reads one voice's entries back from a manifest the prepare stage wrote."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.harness.voices import FIRST_VOICE, SECOND_VOICE
from tests.harness.manifests import build_manifest_entry
from config.models.voxcpm_1_5.data import TRAIN_MANIFEST_FILE
from src.train.models.voxcpm_1_5.data.manifest import ManifestError, write_manifest, read_voice_entries

if TYPE_CHECKING:
    from pathlib import Path


def test_voice_entries_round_trip(tmp_path: Path) -> None:
    """One voice's entries come back as written, in order, without the other voice.

    Args:
        tmp_path: The test folder.

    """
    first_entries = [build_manifest_entry(FIRST_VOICE, text="one"), build_manifest_entry(FIRST_VOICE, text="two")]
    manifest_path = tmp_path / TRAIN_MANIFEST_FILE
    write_manifest([first_entries[0], build_manifest_entry(SECOND_VOICE), first_entries[1]], manifest_path)

    assert read_voice_entries(manifest_path, FIRST_VOICE.name) == first_entries


def test_malformed_line_raises(tmp_path: Path) -> None:
    """A line without the manifest keys stops training with an error naming the file and line.

    Args:
        tmp_path: The test folder.

    """
    manifest_path = tmp_path / TRAIN_MANIFEST_FILE
    write_manifest([build_manifest_entry(FIRST_VOICE)], manifest_path)
    with manifest_path.open("a", encoding="utf-8") as file:
        file.write('{"text": "no audio"}\n')

    with pytest.raises(ManifestError, match=f"{TRAIN_MANIFEST_FILE}:2"):
        read_voice_entries(manifest_path, FIRST_VOICE.name)

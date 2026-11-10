"""A resumed run reads the earlier run's fingerprint and stops unless the prompts and voices match."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from src.dataset.stats import (
    read_stats,
    write_stats,
    encode_stats,
    read_fingerprint,
    write_fingerprint,
    decode_fingerprint,
)
from src.dataset.errors import GenerationError
from tests.harness.tasks import build_prompt_list
from tests.harness.voices import TABLE_VOICES
from tests.harness.records import build_stats
from schemas.dataset.generation import Fingerprint
from src.dataset.generation.tasks import build_output_folders
from src.dataset.generation.resume import build_fingerprint, read_existing_fingerprint, assert_fingerprint_matches

if TYPE_CHECKING:
    from pathlib import Path

PROMPTS = build_prompt_list(2)


def _encode_stats_without(field: str) -> str:
    payload = encode_stats(build_stats())
    del payload[field]
    return json.dumps(payload)


def test_stats_file_reads_back(tmp_path: Path) -> None:
    """The reader returns the stats that the writer wrote.

    Args:
        tmp_path: The test folder.

    """
    path = tmp_path / "stats.json"
    stats = build_stats()
    write_stats(path, stats)

    assert read_stats(path) == stats


def test_missing_stats_file_fails(tmp_path: Path) -> None:
    """A missing stats file stops the run with a generation error that names the path.

    Args:
        tmp_path: The test folder.

    """
    path = tmp_path / "stats.json"

    with pytest.raises(GenerationError) as caught:
        read_stats(path)

    assert str(path) in str(caught.value)


@pytest.mark.parametrize(
    ("text", "fault"),
    [("{", "not readable JSON"), (_encode_stats_without("prompt_count"), "lacks prompt_count")],
    ids=["not-json", "missing-field"],
)
def test_broken_stats_file_fails(tmp_path: Path, text: str, fault: str) -> None:
    """A stats file that is not JSON or lacks a field stops the run with a generation error naming the file and fault.

    Args:
        tmp_path: The test folder.
        text: The file content.
        fault: The part of the message that names what is wrong.

    """
    path = tmp_path / "stats.json"
    path.write_text(text, encoding="utf-8")

    with pytest.raises(GenerationError, match=fault) as caught:
        read_stats(path)

    assert str(path) in str(caught.value)


@pytest.mark.parametrize(
    "current_prompts", [[PROMPTS[0], "Something else."], PROMPTS[::-1]], ids=["other", "reordered"]
)
def test_prompt_change_rejected(current_prompts: list[str]) -> None:
    """Other or reordered prompts of the same count stop the resumed run.

    Args:
        current_prompts: The prompts of the resumed run.

    """
    existing = build_fingerprint(PROMPTS, TABLE_VOICES)

    with pytest.raises(GenerationError):
        assert_fingerprint_matches(existing, build_fingerprint(current_prompts, TABLE_VOICES))


def test_changed_voice_order_rejected() -> None:
    """The same voices in another order stop the resumed run."""
    existing = build_fingerprint(PROMPTS, TABLE_VOICES)

    with pytest.raises(GenerationError):
        assert_fingerprint_matches(existing, build_fingerprint(PROMPTS, TABLE_VOICES[::-1]))


def test_fingerprint_reads_back(tmp_path: Path) -> None:
    """The fingerprint that the writer wrote is the earlier run's fingerprint.

    Args:
        tmp_path: The test folder.

    """
    folders = build_output_folders(tmp_path)
    fingerprint = build_fingerprint(PROMPTS, TABLE_VOICES)

    write_fingerprint(folders.fingerprint_path, fingerprint)

    assert read_existing_fingerprint(folders) == fingerprint


def test_incomplete_fingerprint_fails(tmp_path: Path) -> None:
    """A fingerprint file without a field stops the resumed run and names the field.

    Args:
        tmp_path: The test folder.

    """
    path = build_output_folders(tmp_path).fingerprint_path
    path.write_text(json.dumps({"prompt_hash": "0" * 64, "voices": []}), encoding="utf-8")

    with pytest.raises(GenerationError, match="prompt_count"):
        read_fingerprint(path)


def test_fingerprint_type_named() -> None:
    """A fingerprint field of the wrong type fails to decode, and the message names the field."""
    with pytest.raises(TypeError, match="prompt_count"):
        decode_fingerprint({"prompt_hash": "0" * 64, "prompt_count": "two", "voices": []})


def test_stats_file_seeds_resume(tmp_path: Path) -> None:
    """An output folder that predates the fingerprint file resumes from the fingerprint in its stats file.

    Args:
        tmp_path: The test folder.

    """
    folders = build_output_folders(tmp_path)
    stats = build_stats()
    write_stats(folders.stats_path, stats)

    existing = read_existing_fingerprint(folders)

    assert existing == Fingerprint(prompt_hash=stats.prompt_hash, prompt_count=stats.prompt_count, voices=stats.voices)

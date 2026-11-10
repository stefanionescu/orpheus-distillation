"""The --voice and --max-prompts flags choose the clips a run synthesizes and the fingerprint it writes."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from src.dataset.stats import read_fingerprint
from tests.harness.tasks import build_prompt_list
from src.dataset.cli.main import main
from tests.harness.voices import SECOND_VOICE, TABLE_VOICES
from src.dataset.cli.arguments import EXIT_SUCCESS
from tests.suites.unit.builders import RUN_PROMPT_COUNT, build_run_flags, install_fake_client
from src.dataset.generation.tasks import build_tasks, build_output_folders
from src.dataset.generation.resume import build_fingerprint

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Sequence

    from schemas.voice import Voice

PROMPTS = build_prompt_list(RUN_PROMPT_COUNT)


@pytest.mark.parametrize(
    ("flags", "prompts", "voices"),
    [
        (["--voice", SECOND_VOICE.name], PROMPTS, [SECOND_VOICE]),
        (["--max-prompts", "1"], PROMPTS[:1], TABLE_VOICES),
    ],
    ids=["voice", "max-prompts"],
)
def test_flags_choose_clips(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    flags: list[str],
    prompts: list[str],
    voices: Sequence[Voice],
) -> None:
    """The flag keeps one voice or the first prompts, both in the requests and in the fingerprint of the run.

    Args:
        tmp_path: The test folder.
        monkeypatch: Replaces the Orpheus client.
        flags: The selection flags.
        prompts: The prompts the run keeps.
        voices: The voices the run keeps.

    """
    client = install_fake_client(monkeypatch)
    folders = build_output_folders(tmp_path / "output")

    exit_code = main([*build_run_flags(tmp_path, folders.root), *flags])

    tasks, _ = build_tasks(prompts, voices, folders.audio_folder, set())
    assert exit_code == EXIT_SUCCESS
    assert client.calls == [task.audio_path for task in tasks]
    assert read_fingerprint(folders.fingerprint_path) == build_fingerprint(prompts, voices)

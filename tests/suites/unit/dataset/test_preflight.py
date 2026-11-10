"""The first clip of a run goes alone, so a server that fails it stops the run before the pool sends more."""

from __future__ import annotations

from typing import TYPE_CHECKING
import asyncio

import pytest

from tests.harness.tts import FakeTtsClient
from src.dataset.errors import GenerationError
from tests.harness.tasks import build_prompt_list, build_generation_tasks
from tests.harness.voices import TABLE_VOICES
from schemas.dataset.settings import ServerSettings, GenerationSettings
from tests.suites.unit.builders import API_KEY, SERVER_URL
from src.dataset.generation.tasks import build_output_folders
from src.dataset.generation.pipeline import generate_dataset

if TYPE_CHECKING:
    from pathlib import Path

PROMPT_COUNT = 2
CONCURRENCY = 2


def test_failed_preflight_stops_run(tmp_path: Path) -> None:
    """A server failure on the first clip stops the run with a generation error after that one request.

    Args:
        tmp_path: The test folder.

    """
    settings = GenerationSettings(
        server=ServerSettings(url=SERVER_URL, api_key=API_KEY),
        output_folder=tmp_path / "output",
        clips_per_shard=PROMPT_COUNT,
        concurrency=CONCURRENCY,
        resume=False,
        max_prompts=None,
    )
    first = build_generation_tasks(build_output_folders(settings.output_folder).audio_folder, PROMPT_COUNT)[0]
    client = FakeTtsClient(failing_paths=frozenset({first.audio_path}))

    with pytest.raises(GenerationError):
        asyncio.run(generate_dataset(client, build_prompt_list(PROMPT_COUNT), TABLE_VOICES, settings))

    assert client.calls == [first.audio_path]

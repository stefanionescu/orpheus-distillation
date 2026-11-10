"""The loader checks prompts from the corpus or a file and keeps each one whole, once, in order."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from src.dataset.prompts import PromptError, read_prompts, build_prompts, list_corpus_prompts
from src.dataset.cli.main import main
from config.prompts.corpus import PROMPTS
from src.dataset.cli.arguments import EXIT_FAILURE
from tests.suites.unit.builders import API_KEY, SERVER_URL, install_fake_client

if TYPE_CHECKING:
    from pathlib import Path


def test_prompts_stay_whole() -> None:
    """Each prompt stays whole without its outer spaces, and a blank or repeated prompt yields nothing."""
    prompts = build_prompts(["Dr. Lee called. One foot. Then the other.", "", " Thank you! ", "Thank you!"])

    assert prompts == ["Dr. Lee called. One foot. Then the other.", "Thank you!"]


def test_double_dots_rejected() -> None:
    """Two dots outside an ellipsis stop the run, and the message names every such line."""
    long_prompt = "Long.. " + "word " * 40

    with pytest.raises(PromptError) as caught:
        build_prompts(["Fine... really.", "Bad.. one", long_prompt])

    lines = str(caught.value).splitlines()[1:]
    assert [line.split(":")[0].strip() for line in lines] == ["Line 2", "Line 3"]
    assert lines[1].endswith("...")


def test_file_skips_comments(tmp_path: Path) -> None:
    """A prompt file drops comments, indented ones too, and blank lines, and keeps each other line whole.

    Args:
        tmp_path: The test folder.

    """
    path = tmp_path / "prompts.txt"
    path.write_text("# greeting\n  # indented note\n\nHello there. How are you?\n", encoding="utf-8")

    assert read_prompts(path) == ["Hello there. How are you?"]


def test_file_errors_name_lines(tmp_path: Path) -> None:
    """A rejected prompt's line number counts the file's comments and blank lines.

    Args:
        tmp_path: The test folder.

    """
    path = tmp_path / "prompts.txt"
    path.write_text("# greeting\n\nBad.. one\n", encoding="utf-8")

    with pytest.raises(PromptError, match="Line 3"):
        read_prompts(path)


def test_empty_file_rejected(tmp_path: Path) -> None:
    """A file with only comments holds no prompt.

    Args:
        tmp_path: The test folder.

    """
    path = tmp_path / "prompts.txt"
    path.write_text("# nothing yet\n\n", encoding="utf-8")

    with pytest.raises(PromptError, match="No prompts"):
        read_prompts(path)


@pytest.mark.parametrize("file_name", ["missing.txt", "typo.txt"], ids=["missing-file", "double-dot"])
def test_bad_prompt_file_fails(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, file_name: str) -> None:
    """A prompt file that is missing or holds a stray double dot exits with the failure code before any work.

    Args:
        tmp_path: The test folder.
        monkeypatch: Replaces the Orpheus client.
        file_name: The prompt file the run names.

    """
    client = install_fake_client(monkeypatch)
    (tmp_path / "typo.txt").write_text("Typo.. here\n", encoding="utf-8")
    output_folder = tmp_path / "output"
    flags = ["--server", SERVER_URL, "--api-key", API_KEY, "--prompts-file", str(tmp_path / file_name)]

    exit_code = main([*flags, "--output-folder", str(output_folder)])

    assert exit_code == EXIT_FAILURE
    assert client.calls == []
    assert not output_folder.exists()


def test_corpus_lines_become_prompts() -> None:
    """The built-in corpus builds without a rejected prompt, and each corpus line becomes one prompt as written."""
    assert list_corpus_prompts() == [prompt.strip() for prompt in PROMPTS]

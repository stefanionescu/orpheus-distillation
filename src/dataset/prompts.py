"""Prompt list of a run: the built-in corpus or a file, checked, with each prompt once and whole."""

from __future__ import annotations

from typing import TYPE_CHECKING

from config.prompts.corpus import PROMPTS
from config.dataset.prompts import ELLIPSIS, DOUBLE_DOT, COMMENT_PREFIX, PROMPT_PREVIEW_CHARS

if TYPE_CHECKING:
    from pathlib import Path
    from collections.abc import Sequence


class PromptError(Exception):
    """A prompt holds a stray double dot, or the prompt file holds no prompt."""


def format_prompt_preview(prompt: str) -> str:
    """Shorten a prompt for an error message or a log line.

    Args:
        prompt: Prompt to show.

    Returns:
        The prompt, cut to `PROMPT_PREVIEW_CHARS` with an ellipsis when longer.

    """
    return prompt if len(prompt) <= PROMPT_PREVIEW_CHARS else f"{prompt[:PROMPT_PREVIEW_CHARS]}{ELLIPSIS}"


def build_prompts(raw_prompts: Sequence[str]) -> list[str]:
    """Check the raw prompts, then strip them and drop the blank and repeated ones.

    Each prompt becomes one clip as written, so no clip holds part of a sentence.

    Args:
        raw_prompts: Prompts as the corpus or file holds them.

    Returns:
        Prompts to synthesize, each once, in the order they first appear.

    Raises:
        PromptError: A prompt holds a stray double dot. The message lists each one with its line.

    """
    # The server reads two dots outside an ellipsis as a typo.
    invalid = [
        (position, prompt)
        for position, prompt in enumerate(raw_prompts, start=1)
        if DOUBLE_DOT in prompt.replace(ELLIPSIS, "")
    ]
    if invalid:
        lines = "\n".join(f"  Line {position}: {format_prompt_preview(prompt)}" for position, prompt in invalid)
        message = f"Prompts with two dots outside an ellipsis:\n{lines}"
        raise PromptError(message)
    stripped = (raw.strip() for raw in raw_prompts)
    return list(dict.fromkeys(prompt for prompt in stripped if prompt))


def read_prompts(path: Path) -> list[str]:
    """Read a prompt file with one prompt per line, skipping blank lines and `#` comments.

    Args:
        path: UTF-8 prompt file.

    Returns:
        The prompts to synthesize.

    Raises:
        PromptError: The file holds no prompt.

    """
    with path.open(encoding="utf-8") as prompt_file:
        lines = [line.strip() for line in prompt_file]
    raw_prompts = ["" if line.startswith(COMMENT_PREFIX) else line for line in lines]
    if not any(raw_prompts):
        message = f"No prompts found in {path}"
        raise PromptError(message)
    return build_prompts(raw_prompts)


def list_corpus_prompts() -> list[str]:
    """List the built-in corpus prompts, checked like a prompt file.

    Returns:
        The prompts to synthesize.

    """
    return build_prompts(PROMPTS)

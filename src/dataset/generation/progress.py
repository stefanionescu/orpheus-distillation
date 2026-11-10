"""Progress bar of a run: finished clips and audio synthesized so far."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from tqdm import tqdm

from src.dataset.stats import format_duration
from config.dataset.generation import (
    PROGRESS_COLUMNS_WITHOUT_TTY,
    PROGRESS_INTERVAL_LOG_SECONDS,
    PROGRESS_INTERVAL_TTY_SECONDS,
)

if TYPE_CHECKING:
    from typing import NoReturn


def set_progress_duration(progress: tqdm[NoReturn], seconds: float) -> None:
    """Show the audio length synthesized so far beside the bar.

    Args:
        progress: Progress bar.
        seconds: Audio length.

    """
    progress.set_postfix_str(f"audio: {format_duration(seconds)}")


def build_progress_bar(total: int, initial_duration: float) -> tqdm[NoReturn]:
    """Build the bar on standard error, starting at one for the preflight clip.

    On a terminal the bar refreshes often. In a log it refreshes seldom at a fixed width.

    Args:
        total: Clips to synthesize, preflight clip included.
        initial_duration: Preflight clip length in seconds.

    Returns:
        The bar; the caller closes it.

    """
    is_terminal = sys.stderr.isatty()
    progress = tqdm(
        total=total,
        initial=1,
        desc="Synthesizing clips",
        file=sys.stderr,
        dynamic_ncols=is_terminal,
        ncols=None if is_terminal else PROGRESS_COLUMNS_WITHOUT_TTY,
        mininterval=PROGRESS_INTERVAL_TTY_SECONDS if is_terminal else PROGRESS_INTERVAL_LOG_SECONDS,
    )
    set_progress_duration(progress, initial_duration)
    return progress

"""Logging setup and the stdout result lines that the shell reads."""

from __future__ import annotations

import sys
import logging

LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s %(message)s"

logger = logging.getLogger(__name__)


def configure_logging() -> None:
    """Send INFO and higher log records to stderr, so stdout carries only results."""
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, stream=sys.stderr)


def print_result(key: str, value: object) -> None:
    """Print one command result to stdout as a `key=value` line.

    Args:
        key: Result name, such as `checkpoint_folder`.
        value: Result, written with `str`.

    """
    sys.stdout.write(f"{key}={value}\n")
    sys.stdout.flush()


def print_failure(stage: str, error: Exception) -> None:
    """Log an expected failure of a stage as one line, without a traceback.

    Args:
        stage: What failed, such as `The download`.
        error: The error, whose message names what to fix.

    """
    logger.error("%s failed: %s", stage, error)

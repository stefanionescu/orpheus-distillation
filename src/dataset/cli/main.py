"""Entry point of the dataset command."""

from __future__ import annotations

import sys
import signal
from typing import TYPE_CHECKING
import logging

from src.dataset.errors import UsageError, GenerationError
from src.dataset.prompts import PromptError
from src.dataset.settings import read_environment
from src.dataset.cli.publish import run_publish_command
from src.dataset.hub.publish import PublishError
from src.dataset.cli.generate import StoppedError, run_generate_command
from src.dataset.cli.arguments import EXIT_USAGE, EXIT_FAILURE, EXIT_SIGNAL_BASE, parse_arguments

if TYPE_CHECKING:
    from collections.abc import Sequence

logger = logging.getLogger(__name__)


def main(argument_values: Sequence[str] | None = None) -> int:
    """Run the dataset command and return its exit code.

    This function logs each failure that a command raises, once.

    Args:
        argument_values: Flags, or None for `sys.argv`.

    Returns:
        0 on success, 1 on failure, 2 on a usage error, and 128 plus the signal number on SIGINT or SIGTERM.

    """
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s", stream=sys.stderr)
    try:
        arguments = parse_arguments(argument_values)
    except SystemExit as stop:
        return stop.code if isinstance(stop.code, int) else EXIT_USAGE
    command = run_publish_command if arguments.publish_only else run_generate_command
    try:
        return command(arguments, read_environment())
    except UsageError as error:
        exit_code, level, failure = EXIT_USAGE, logging.ERROR, str(error)
    except (GenerationError, PromptError, PublishError, FileNotFoundError) as error:
        exit_code, level, failure = EXIT_FAILURE, logging.ERROR, str(error)
    except StoppedError as error:
        exit_code, level, failure = EXIT_SIGNAL_BASE + error.stop_signal, logging.WARNING, str(error)
    except KeyboardInterrupt:
        exit_code, level, failure = EXIT_SIGNAL_BASE + signal.SIGINT, logging.WARNING, "Interrupted"
    logger.log(level, "%s", failure)
    return exit_code

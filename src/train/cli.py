"""Argument parsers and exit codes that every model command shares."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING
from pathlib import Path
import argparse

from src.train.settings import read_environment

if TYPE_CHECKING:
    from schemas.settings import TrainEnvironment

EXIT_SUCCESS = 0
EXIT_FAILURE = 1
EXIT_USAGE = 2
EXIT_SIGNAL_BASE = 128
RUN_NAME_PATTERN = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*")
REPO_PATTERN = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*/[A-Za-z0-9][A-Za-z0-9._-]*")
EXIT_CODES = f"""exit codes:
  {EXIT_SUCCESS}      success
  {EXIT_FAILURE}      failure: a missing file, a bad shard or checkpoint, a Hub error, or no CUDA GPU
  {EXIT_USAGE}      usage error"""
SIGNAL_EXIT_CODE = f"""
  {EXIT_SIGNAL_BASE}+N  stopped by signal N after writing a checkpoint; the next run resumes from it"""


def _parse_number(value: str, number_type: type[float | int]) -> float:
    try:
        return number_type(value)
    except ValueError as error:
        message = f"{value!r} is not a number"
        raise argparse.ArgumentTypeError(message) from error


def parse_positive_int(value: str) -> int:
    """Parse a whole number of 1 or more.

    Args:
        value: Flag text.

    Returns:
        The number.

    Raises:
        argparse.ArgumentTypeError: The text is not a whole number of 1 or more.

    """
    number = int(_parse_number(value, int))
    if number < 1:
        message = f"{value} is below 1"
        raise argparse.ArgumentTypeError(message)
    return number


def parse_positive_float(value: str) -> float:
    """Parse a number above 0.

    Args:
        value: Flag text.

    Returns:
        The number.

    Raises:
        argparse.ArgumentTypeError: The text is not a number above 0.

    """
    number = _parse_number(value, float)
    if number <= 0:
        message = f"{value} is not above 0"
        raise argparse.ArgumentTypeError(message)
    return number


def parse_non_negative_float(value: str) -> float:
    """Parse a number of 0 or more.

    Args:
        value: Flag text.

    Returns:
        The number.

    Raises:
        argparse.ArgumentTypeError: The text is not a number of 0 or more.

    """
    number = _parse_number(value, float)
    if number < 0:
        message = f"{value} is below 0"
        raise argparse.ArgumentTypeError(message)
    return number


def parse_fraction(value: str) -> float:
    """Parse a fraction of at least 0 and below 1.

    Args:
        value: Flag text.

    Returns:
        The fraction.

    Raises:
        argparse.ArgumentTypeError: The text is not a number of at least 0 and below 1.

    """
    fraction = _parse_number(value, float)
    if not 0 <= fraction < 1:
        message = f"{value} is not at least 0 and below 1"
        raise argparse.ArgumentTypeError(message)
    return fraction


def parse_run_name(value: str) -> str:
    """Parse a run name, which must name one folder inside the runs folder.

    Args:
        value: Flag text.

    Returns:
        The run name.

    Raises:
        argparse.ArgumentTypeError: The name does not start with a letter or digit, or holds a character other than
            letters, digits, dots, underscores, and hyphens.

    """
    if RUN_NAME_PATTERN.fullmatch(value) is None:
        message = f"{value!r} is not one folder name of letters, digits, dots, underscores, and hyphens"
        raise argparse.ArgumentTypeError(message)
    return value


def parse_repo(value: str) -> str:
    """Parse a Hugging Face repository of the form owner/name.

    Args:
        value: Flag text.

    Returns:
        The repository.

    Raises:
        argparse.ArgumentTypeError: The text is not of the form owner/name.

    """
    if REPO_PATTERN.fullmatch(value) is None:
        message = f"{value!r} is not a repository of the form owner/name"
        raise argparse.ArgumentTypeError(message)
    return value


def build_parser(
    prog: str, description: str | None, example: str, *, is_interruptible: bool = False
) -> argparse.ArgumentParser:
    """Build a command parser whose help ends with the exit codes and an example.

    Args:
        prog: Command line that the usage line shows.
        description: Help text before the flags.
        example: One command line that runs the command.
        is_interruptible: Whether to list the 128+N exit code of a stop after a checkpoint.

    Returns:
        The parser, without flags.

    """
    signal_exit_code = SIGNAL_EXIT_CODE if is_interruptible else ""
    return argparse.ArgumentParser(
        prog=prog,
        description=description,
        epilog=f"{EXIT_CODES}{signal_exit_code}\n\nexample:\n  {example}",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )


def add_path_flag(parser: argparse.ArgumentParser, flag: str, destination: str, help_text: str) -> None:
    """Add a required path flag: a folder when the destination ends in _folder, else a file.

    Args:
        parser: Command parser.
        flag: The flag, such as `--tokenizer-folder`.
        destination: Attribute name, ending in `_folder` or `_path`.
        help_text: What the path holds.

    """
    metavar = "FOLDER" if destination.endswith("_folder") else "FILE"
    parser.add_argument(flag, dest=destination, type=Path, metavar=metavar, required=True, help=help_text)


def read_command_environment(parser: argparse.ArgumentParser) -> TrainEnvironment:
    """Read the process environment, or exit with a usage error when a variable is invalid.

    Args:
        parser: Parser that reports the error and exits with code 2.

    Returns:
        The environment.

    """
    try:
        return read_environment()
    except ValueError as error:
        parser.error(str(error))

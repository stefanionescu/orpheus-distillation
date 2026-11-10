"""Synthesize Orpheus clips into WebDataset shards, or publish a dataset on disk to the Hugging Face Hub."""

from __future__ import annotations

from typing import TYPE_CHECKING
from pathlib import Path
import argparse

from config.hub import DATASET_REPO
from config.voices import VOICES
from config.dataset.paths import OUTPUT_FOLDER
from config.dataset.generation import CONCURRENCY, CLIPS_PER_SHARD
from schemas.dataset.arguments import DatasetArguments

if TYPE_CHECKING:
    from collections.abc import Sequence

EXIT_SUCCESS = 0
EXIT_FAILURE = 1
EXIT_USAGE = 2
EXIT_SIGNAL_BASE = 128
EPILOG = """example:
  python -m src.dataset --server ws://localhost:8000 --api-key KEY --max-prompts 10

exit codes:
  0 success, 1 failure, 2 usage error, 130 interrupted, 143 terminated
"""


class _HelpFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter):
    """Help formatter that shows flag defaults and keeps the epilog line breaks."""


def _add_output_arguments(parser: argparse.ArgumentParser) -> None:
    """Add the output and publish flags.

    Args:
        parser: Command parser.

    """
    parser.add_argument(
        "--resume", action="store_true", help="keep the clips of an earlier run with the same prompts and voices"
    )
    parser.add_argument(
        "--output-folder",
        dest="output_folder",
        metavar="FOLDER",
        type=Path,
        default=Path(OUTPUT_FOLDER),
        help="folder that the run writes, relative to the current folder; a run without --resume cleans it first",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="without --resume, delete the output of an earlier run without asking first",
    )
    parser.add_argument("--publish", action="store_true", help="publish the dataset after the run; needs HF_TOKEN")
    parser.add_argument("--dataset-repo", metavar="REPO", default=DATASET_REPO, help="Hugging Face dataset repository")
    parser.add_argument("--public", action="store_true", help="make a new Hugging Face repository public")


def parse_positive_int(text: str) -> int:
    """Parse a flag value as a whole number of at least 1.

    Args:
        text: Raw flag value.

    Returns:
        The number.

    Raises:
        argparse.ArgumentTypeError: The value is not a whole number or is below 1.

    """
    try:
        value = int(text)
    except ValueError as error:
        message = f"must be a whole number, got {text!r}"
        raise argparse.ArgumentTypeError(message) from error
    if value < 1:
        message = "must be at least 1"
        raise argparse.ArgumentTypeError(message)
    return value


def build_parser() -> argparse.ArgumentParser:
    """Build the parser of the generate and publish-only modes.

    Returns:
        The parser.

    """
    parser = argparse.ArgumentParser(
        prog="python -m src.dataset",
        description=__doc__,
        epilog=EPILOG,
        formatter_class=_HelpFormatter,
    )
    parser.add_argument(
        "--publish-only", action="store_true", help="publish the dataset in --output-folder and synthesize nothing"
    )
    parser.add_argument(
        "--server",
        metavar="URL",
        help="Orpheus server URL: http, https, ws, wss, or host:port; overrides ORPHEUS_SERVER_URL",
    )
    parser.add_argument("--api-key", metavar="KEY", help="Orpheus API key; overrides ORPHEUS_API_KEY")
    parser.add_argument(
        "--prompts-file",
        dest="prompts_path",
        metavar="PATH",
        type=Path,
        help="text file with one prompt per line and # comments; the built-in corpus when absent",
    )
    parser.add_argument("--voice", choices=tuple(VOICES), help="synthesize only this voice")
    parser.add_argument(
        "--max-prompts", metavar="COUNT", type=parse_positive_int, help="largest number of prompts to synthesize"
    )
    parser.add_argument(
        "--clips-per-shard",
        metavar="COUNT",
        type=parse_positive_int,
        default=CLIPS_PER_SHARD,
        help="clips in each shard",
    )
    parser.add_argument(
        "--concurrency",
        metavar="COUNT",
        type=parse_positive_int,
        default=CONCURRENCY,
        help="requests that run at once",
    )
    _add_output_arguments(parser)
    return parser


def parse_arguments(argument_values: Sequence[str] | None) -> DatasetArguments:
    """Parse the command flags. On a bad value, argparse raises `SystemExit` with code 2.

    Args:
        argument_values: Flags, or None for `sys.argv`.

    Returns:
        The parsed flags.

    """
    namespace = build_parser().parse_args(argument_values)
    return DatasetArguments(
        publish_only=namespace.publish_only,
        server=namespace.server,
        api_key=namespace.api_key,
        prompts_path=namespace.prompts_path,
        voice=namespace.voice,
        max_prompts=namespace.max_prompts,
        clips_per_shard=namespace.clips_per_shard,
        concurrency=namespace.concurrency,
        resume=namespace.resume,
        output_folder=namespace.output_folder,
        publish=namespace.publish,
        dataset_repo=namespace.dataset_repo,
        public=namespace.public,
        yes=namespace.yes,
    )

"""Run one VoxCPM 1.5 command. Each command takes its own flags and --help."""

from __future__ import annotations

from typing import TYPE_CHECKING
import argparse

from src.train.cli import build_parser
from src.train.voxcpm_1_5.commands import infer, train, prepare, publish, download, pipeline

if TYPE_CHECKING:
    from collections.abc import Callable, Sequence

PROGRAM = "python -m src.train voxcpm_1_5"
EXAMPLE = f"{PROGRAM} pipeline --run-name first-run"


def main(argument_values: Sequence[str] | None = None) -> int:
    """Run the named command with the arguments after it.

    Args:
        argument_values: Command and flags; None reads `sys.argv`.

    Returns:
        Exit code of the command.

    """
    commands: dict[str, Callable[[Sequence[str] | None], int]] = {
        "download": download.main,
        "prepare": prepare.main,
        "train": train.main,
        "infer": infer.main,
        "publish": publish.main,
        "pipeline": pipeline.main,
    }
    parser = build_parser(PROGRAM, __doc__, EXAMPLE, is_interruptible=True)
    parser.add_argument("command", choices=tuple(commands), help="the command to run")
    parser.add_argument("arguments", nargs=argparse.REMAINDER, help="the flags of the command")
    arguments = parser.parse_args(argument_values)
    return commands[arguments.command](arguments.arguments)


if __name__ == "__main__":
    raise SystemExit(main())

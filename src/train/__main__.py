"""Train a target model on the Orpheus dataset."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING
import argparse

from src.train.cli import build_parser
from src.train.voxcpm_1_5.__main__ import main as run_voxcpm_1_5

if TYPE_CHECKING:
    from collections.abc import Callable, Sequence

# The target models, in the order the docs list them. Add a new model as a package under src/train/ and one entry here.
MODELS: MappingProxyType[str, Callable[[Sequence[str] | None], int]] = MappingProxyType(
    {
        "voxcpm_1_5": run_voxcpm_1_5,
    }
)

PROGRAM = "python -m src.train"
EXAMPLE = f"{PROGRAM} voxcpm_1_5 pipeline --run-name first-run"


def main(argument_values: Sequence[str] | None = None) -> int:
    """Run a command of the named model.

    Args:
        argument_values: Model, command, and flags; None reads `sys.argv`.

    Returns:
        Exit code of the command.

    """
    parser = build_parser(PROGRAM, __doc__, EXAMPLE, is_interruptible=True)
    parser.add_argument("model", choices=tuple(MODELS), help="the target model")
    parser.add_argument("arguments", nargs=argparse.REMAINDER, help="the command of the model and its flags")
    arguments = parser.parse_args(argument_values)
    return MODELS[arguments.model](arguments.arguments)


if __name__ == "__main__":
    raise SystemExit(main())

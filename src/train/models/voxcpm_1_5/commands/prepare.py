"""Write the training and validation manifests from the dataset shards, and copy the base model tokenizer.

The files go to the manifests and tokenizer folders of the run folder. Each result goes to stdout as a key=value
line: train_manifest, val_manifest when the split keeps validation clips, and tokenizer_folder.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from src.train.cli import EXIT_FAILURE, EXIT_SUCCESS, build_parser, add_path_flag, parse_fraction
from src.train.logs import print_result, print_failure, configure_logging
from config.models.voxcpm_1_5.data import VAL_SPLIT, MANIFESTS_FOLDER, TOKENIZER_FOLDER
from schemas.models.voxcpm_1_5.manifest import PreparedInputs
from src.train.models.voxcpm_1_5.data.manifest import (
    ManifestError,
    write_manifests,
    copy_tokenizer_files,
    print_manifest_stats,
)

if TYPE_CHECKING:
    from pathlib import Path
    import argparse
    from collections.abc import Sequence

PROGRAM = "python -m src.train voxcpm_1_5 prepare"
EXAMPLE = (
    f"{PROGRAM} --dataset-folder DATASET --base-model-folder BASE_MODEL --run-folder training_output/first-run "
    "--val-split 0.05"
)


def _parse_arguments(argument_values: Sequence[str] | None) -> argparse.Namespace:
    parser = build_parser(PROGRAM, __doc__, EXAMPLE)
    add_path_flag(parser, "--dataset-folder", "dataset_folder", "the downloaded dataset folder")
    add_path_flag(parser, "--base-model-folder", "base_model_folder", "the downloaded base model folder")
    add_path_flag(parser, "--run-folder", "run_folder", "the run folder that receives the files")
    parser.add_argument(
        "--val-split",
        type=parse_fraction,
        default=VAL_SPLIT,
        help="the share of clips, at least 0 and below 1, that validation keeps (default: %(default)s)",
    )
    return parser.parse_args(argument_values)


def prepare_inputs(dataset_folder: Path, base_model_folder: Path, run_folder: Path, val_split: float) -> PreparedInputs:
    """Write the manifests and the tokenizer files into a run folder, and print each path.

    No shard or no usable clip raises ManifestError, and a missing tokenizer file raises FileNotFoundError.

    Args:
        dataset_folder: Downloaded dataset.
        base_model_folder: Downloaded base model, which holds the tokenizer files.
        run_folder: The run folder.
        val_split: Share of clips for validation.

    Returns:
        The manifests and the tokenizer folder.

    """
    manifests = write_manifests(dataset_folder, run_folder / MANIFESTS_FOLDER, val_split)
    print_manifest_stats(manifests.stats)
    tokenizer_folder = run_folder / TOKENIZER_FOLDER
    copy_tokenizer_files(base_model_folder, tokenizer_folder)
    print_result("train_manifest", manifests.train_manifest_path)
    if manifests.val_manifest_path is not None:
        print_result("val_manifest", manifests.val_manifest_path)
    print_result("tokenizer_folder", tokenizer_folder)
    return PreparedInputs(manifests.train_manifest_path, manifests.val_manifest_path, tokenizer_folder)


def main(argument_values: Sequence[str] | None = None) -> int:
    """Run the prepare command.

    Args:
        argument_values: Command flags; None reads `sys.argv`.

    Returns:
        0 on success, 1 when the shards hold no usable clip or a file is missing.

    """
    configure_logging()
    arguments = _parse_arguments(argument_values)
    try:
        prepare_inputs(arguments.dataset_folder, arguments.base_model_folder, arguments.run_folder, arguments.val_split)
    except (ManifestError, OSError) as error:
        print_failure("The preparation", error)
        return EXIT_FAILURE
    return EXIT_SUCCESS


if __name__ == "__main__":
    raise SystemExit(main())

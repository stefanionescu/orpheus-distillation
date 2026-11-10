"""Download the dataset shards and the VoxCPM 1.5 base model from the Hugging Face Hub into a cache folder.

Each result goes to stdout as a key=value line: dataset_folder, then base_model_folder.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from huggingface_hub.errors import HfHubHTTPError

from config.hub import DATASET_REPO, REPO_TYPE_MODEL, REPO_TYPE_DATASET
from src.train.cli import (
    EXIT_FAILURE,
    EXIT_SUCCESS,
    parse_repo,
    build_parser,
    add_path_flag,
    read_command_environment,
)
from src.train.hub import HubError, download_snapshot
from src.train.logs import print_result, print_failure, configure_logging
from config.voxcpm_1_5.hub import BASE_MODEL_REPO

if TYPE_CHECKING:
    from pathlib import Path
    import argparse
    from collections.abc import Sequence

    from schemas.settings import TrainEnvironment

PROGRAM = "python -m src.train voxcpm_1_5 download"
EXAMPLE = f"{PROGRAM} --cache-folder .cache/voxcpm"


def _parse_arguments(argument_values: Sequence[str] | None) -> tuple[argparse.Namespace, TrainEnvironment]:
    parser = build_parser(PROGRAM, __doc__, EXAMPLE)
    parser.add_argument(
        "--dataset-repo",
        type=parse_repo,
        default=DATASET_REPO,
        help="the dataset repository that holds the shards (default: %(default)s)",
    )
    parser.add_argument(
        "--base-model-repo",
        type=parse_repo,
        default=BASE_MODEL_REPO,
        help="the repository of the base model (default: %(default)s)",
    )
    add_path_flag(parser, "--cache-folder", "cache_folder", "the folder of the download cache")
    arguments = parser.parse_args(argument_values)
    return arguments, read_command_environment(parser)


def download_inputs(
    dataset_repo: str, base_model_repo: str, cache_folder: Path, token: str | None
) -> tuple[Path, Path]:
    """Download the dataset and the base model, and print the folder of each.

    Args:
        dataset_repo: Dataset repository with the shards.
        base_model_repo: Base model repository.
        cache_folder: Download cache.
        token: Hugging Face token, or None to download anonymously.

    Returns:
        The dataset folder and the base model folder.

    """
    dataset_folder = download_snapshot(dataset_repo, REPO_TYPE_DATASET, cache_folder, token)
    print_result("dataset_folder", dataset_folder)
    base_model_folder = download_snapshot(base_model_repo, REPO_TYPE_MODEL, cache_folder, token)
    print_result("base_model_folder", base_model_folder)
    return dataset_folder, base_model_folder


def main(argument_values: Sequence[str] | None = None) -> int:
    """Run the download command.

    Args:
        argument_values: Command flags; None reads `sys.argv`.

    Returns:
        0 on success, 1 when a repository is missing or the Hub fails.

    """
    configure_logging()
    arguments, environment = _parse_arguments(argument_values)
    try:
        download_inputs(arguments.dataset_repo, arguments.base_model_repo, arguments.cache_folder, environment.hf_token)
    except (HubError, HfHubHTTPError) as error:
        print_failure("The download", error)
        return EXIT_FAILURE
    return EXIT_SUCCESS


if __name__ == "__main__":
    raise SystemExit(main())

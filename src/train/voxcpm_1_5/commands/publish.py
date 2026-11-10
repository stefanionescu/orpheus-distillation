"""Stage the adapter of each voice with the base model, the tokenizer, the samples, and a model card, then upload them.

The staging folder sits beside the checkpoints folder. Each result goes to stdout as a key=value line: staging_folder,
then commit_url without --dry-run. An upload needs HF_TOKEN with write access to the output repository.
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from pathlib import Path

import httpx2
from huggingface_hub.errors import HfHubHTTPError

from src.train.cli import (
    EXIT_FAILURE,
    EXIT_SUCCESS,
    parse_repo,
    build_parser,
    add_path_flag,
    parse_run_name,
    read_command_environment,
)
from src.train.hub import upload_folder
from src.train.logs import print_result, print_failure, configure_logging
from config.voxcpm_1_5.hub import OUTPUT_REPO, BASE_MODEL_REPO, PUBLISH_COMMIT_MESSAGE
from schemas.voxcpm_1_5.publish import PublishRequest
from src.train.voxcpm_1_5.hub.publish import PublishError, create_staging_folder
from src.train.voxcpm_1_5.training.checkpoints import CheckpointError

if TYPE_CHECKING:
    import argparse
    from collections.abc import Sequence

    from schemas.settings import TrainEnvironment

PROGRAM = "python -m src.train voxcpm_1_5 publish"
EXAMPLE = (
    f"{PROGRAM} --run-name first-run --checkpoints-folder RUN/checkpoints --base-model-folder BASE_MODEL "
    "--tokenizer-folder RUN/tokenizer --samples-folder RUN/samples --dry-run"
)
PUBLISH_ERRORS = (PublishError, CheckpointError, HfHubHTTPError, httpx2.TransportError, OSError)


def _parse_arguments(argument_values: Sequence[str] | None) -> tuple[argparse.Namespace, TrainEnvironment]:
    parser = build_parser(PROGRAM, __doc__, EXAMPLE)
    parser.add_argument("--run-name", type=parse_run_name, required=True, help="the training run that the card names")
    add_path_flag(
        parser,
        "--checkpoints-folder",
        "checkpoints_folder",
        "the checkpoints folder of the run, one folder per voice",
    )
    add_path_flag(parser, "--base-model-folder", "base_model_folder", "the downloaded base model folder")
    add_path_flag(parser, "--tokenizer-folder", "tokenizer_folder", "the tokenizer folder of the run")
    parser.add_argument(
        "--samples-folder", dest="samples_folder", type=Path, metavar="FOLDER", help="the folder of the sample clips"
    )
    add_repository_flags(parser)
    parser.add_argument("--dry-run", action="store_true", help="stage the files and the card without uploading them")
    arguments = parser.parse_args(argument_values)
    environment = read_command_environment(parser)
    if not arguments.dry_run and environment.hf_token is None:
        parser.error("an upload needs HF_TOKEN; set it, or pass --dry-run to stage without uploading")
    return arguments, environment


def add_repository_flags(parser: argparse.ArgumentParser) -> None:
    """Add the output repository, its visibility, and the base model repository flags.

    Args:
        parser: Parser of a command that publishes.

    """
    parser.add_argument(
        "--output-repo",
        type=parse_repo,
        default=OUTPUT_REPO,
        help="the model repository that receives the adapters (default: %(default)s)",
    )
    parser.add_argument(
        "--base-model-repo",
        type=parse_repo,
        default=BASE_MODEL_REPO,
        help="the repository of the base model (default: %(default)s)",
    )
    parser.add_argument("--public", action="store_true", help="make a new Hugging Face repository public")


def publish_adapters(request: PublishRequest, token: str | None) -> Path:
    """Stage the repository and print its folder, then with a token upload it and print the commit URL.

    A missing file raises PublishError or CheckpointError, and a Hub failure raises HfHubHTTPError.

    Args:
        request: Folders and repositories of the run.
        token: Token with write access to the output repository, or None to stop after staging.

    Returns:
        The staging folder.

    """
    staging_folder = create_staging_folder(request)
    print_result("staging_folder", staging_folder)
    if token is not None:
        commit_url = upload_folder(
            staging_folder, request.output_repo, token, PUBLISH_COMMIT_MESSAGE, public=request.public
        )
        print_result("commit_url", commit_url)
    return staging_folder


def main(argument_values: Sequence[str] | None = None) -> int:
    """Run the publish command.

    Args:
        argument_values: Command flags; None reads `sys.argv`.

    Returns:
        0 on success, 1 when a file is missing or the upload fails.

    """
    configure_logging()
    arguments, environment = _parse_arguments(argument_values)
    request = PublishRequest(
        run_name=arguments.run_name,
        checkpoints_folder=arguments.checkpoints_folder,
        base_model_folder=arguments.base_model_folder,
        tokenizer_folder=arguments.tokenizer_folder,
        samples_folder=arguments.samples_folder,
        output_repo=arguments.output_repo,
        base_model_repo=arguments.base_model_repo,
        public=arguments.public,
    )
    try:
        publish_adapters(request, None if arguments.dry_run else environment.hf_token)
    except PUBLISH_ERRORS as error:
        print_failure("Publishing", error)
        return EXIT_FAILURE
    return EXIT_SUCCESS


if __name__ == "__main__":
    raise SystemExit(main())

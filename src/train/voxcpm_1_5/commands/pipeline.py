"""Run the whole pipeline of one run: download, prepare, train each voice, write samples, and publish.

The run folder inside the runs folder holds every output of the run. A second run of the same name skips each
voice that finished its steps and resumes a stopped voice from its newest checkpoint. SIGINT or SIGTERM stop training
after the current step and write a checkpoint. Each result goes to stdout as a key=value line.
"""

from __future__ import annotations

import sys
import shutil
import signal
from typing import TYPE_CHECKING
import logging
from pathlib import Path

import httpx2
from huggingface_hub.errors import HfHubHTTPError

from config.hub import DATASET_REPO, REPO_TYPE_MODEL
from config.voices import VOICES
from src.train.cli import (
    EXIT_FAILURE,
    EXIT_SUCCESS,
    EXIT_SIGNAL_BASE,
    parse_repo,
    build_parser,
    parse_fraction,
    parse_run_name,
    read_command_environment,
)
from src.train.hub import HubError, download_snapshot
from src.train.logs import print_result, print_failure, configure_logging
from config.voxcpm_1_5.hub import SAMPLES_FOLDER
from config.voxcpm_1_5.data import VAL_SPLIT, TOKENIZER_FOLDER
from config.voxcpm_1_5.pipeline import RUNS_FOLDER, CACHE_FOLDER
from schemas.voxcpm_1_5.publish import PublishRequest
from config.voxcpm_1_5.inference import TIMESTEPS, MAX_PATCHES, GUIDANCE_SCALE
from schemas.voxcpm_1_5.training import TrainingFolders
from schemas.voxcpm_1_5.inference import SamplerSettings
from config.voxcpm_1_5.checkpoints import EVENTS_FOLDER, CHECKPOINTS_FOLDER
from src.train.voxcpm_1_5.hub.publish import PublishError
from src.train.voxcpm_1_5.training.job import TrainingDataError
from src.train.voxcpm_1_5.data.manifest import ManifestError
from src.train.voxcpm_1_5.commands.infer import write_run_samples
from src.train.voxcpm_1_5.commands.train import (
    train_voice,
    add_training_flags,
    build_lora_settings,
    build_training_settings,
)
from src.train.voxcpm_1_5.commands.prepare import prepare_inputs
from src.train.voxcpm_1_5.commands.publish import publish_adapters, add_repository_flags
from src.train.voxcpm_1_5.training.devices import GpuError
from src.train.voxcpm_1_5.commands.download import download_inputs
from src.train.voxcpm_1_5.training.checkpoints import CheckpointError, read_checkpoint_step, find_newest_checkpoint
from src.train.voxcpm_1_5.inference.synthesizer import AdapterError

if TYPE_CHECKING:
    import argparse
    from collections.abc import Sequence

    from schemas.settings import TrainEnvironment
    from schemas.voxcpm_1_5.manifest import PreparedInputs

PROGRAM = "python -m src.train voxcpm_1_5 pipeline"
EXAMPLE = f"{PROGRAM} --run-name first-run --voices female --steps 2000 --publish"
CONSENT_ANSWERS = frozenset({"y", "yes"})
PIPELINE_ERRORS = (
    HubError,
    HfHubHTTPError,
    httpx2.TransportError,
    ManifestError,
    GpuError,
    TrainingDataError,
    CheckpointError,
    AdapterError,
    PublishError,
    OSError,
)

logger = logging.getLogger(__name__)


def _parse_arguments(argument_values: Sequence[str] | None) -> tuple[argparse.Namespace, TrainEnvironment]:
    parser = build_parser(PROGRAM, __doc__, EXAMPLE, is_interruptible=True)
    parser.add_argument(
        "--run-name", type=parse_run_name, required=True, help="the run, which names its folder in the runs folder"
    )
    parser.add_argument(
        "--voices",
        nargs="+",
        choices=tuple(VOICES),
        default=list(VOICES),
        help=f"the voices to train, in order (default: {' '.join(VOICES)})",
    )
    parser.add_argument(
        "--dataset-repo",
        type=parse_repo,
        default=DATASET_REPO,
        help="the dataset repository that holds the shards (default: %(default)s)",
    )
    add_repository_flags(parser)
    add_training_flags(parser)
    parser.add_argument(
        "--val-split",
        type=parse_fraction,
        default=VAL_SPLIT,
        help="the share of clips, at least 0 and below 1, that validation keeps (default: %(default)s)",
    )
    parser.add_argument(
        "--cache-folder",
        dest="cache_folder",
        type=Path,
        metavar="FOLDER",
        default=Path(CACHE_FOLDER),
        help="the folder of the download cache (default: %(default)s)",
    )
    parser.add_argument(
        "--runs-folder",
        dest="runs_folder",
        type=Path,
        metavar="FOLDER",
        default=Path(RUNS_FOLDER),
        help="the folder that holds one folder per run (default: %(default)s)",
    )
    parser.add_argument("--publish", action="store_true", help="publish the adapters and samples; needs HF_TOKEN")
    parser.add_argument(
        "--samples-only", action="store_true", help="skip download, preparation, and training; write samples only"
    )
    parser.add_argument("--clean", action="store_true", help="delete the run folder first, after a confirmation")
    parser.add_argument("--yes", action="store_true", help="confirm --clean without a prompt")
    arguments = parser.parse_args(argument_values)
    environment = read_command_environment(parser)
    if arguments.publish and environment.hf_token is None:
        parser.error("--publish needs HF_TOKEN with write access to the output repository")
    run_folder = arguments.runs_folder / arguments.run_name
    if arguments.clean and not arguments.yes and run_folder.exists() and not sys.stdin.isatty():
        parser.error(f"--clean deletes {run_folder}; pass --yes to confirm it without a terminal")
    return arguments, environment


def _ask_clean_consent(run_folder: Path) -> bool:
    sys.stderr.write(f"Delete {run_folder} and every file in it? [y/N] ")
    sys.stderr.flush()
    return sys.stdin.readline().strip().lower() in CONSENT_ANSWERS


def _train_voices(
    arguments: argparse.Namespace, environment: TrainEnvironment, base_model_folder: Path, prepared: PreparedInputs
) -> int | None:
    run_folder = arguments.runs_folder / arguments.run_name
    for voice in arguments.voices:
        folders = TrainingFolders(
            base_model_folder=base_model_folder,
            train_manifest_path=prepared.train_manifest_path,
            val_manifest_path=prepared.val_manifest_path,
            tokenizer_folder=prepared.tokenizer_folder,
            voice_checkpoints_folder=run_folder / CHECKPOINTS_FOLDER / voice,
            voice_events_folder=run_folder / EVENTS_FOLDER / voice,
        )
        newest_folder = find_newest_checkpoint(folders.voice_checkpoints_folder)
        if newest_folder is not None and read_checkpoint_step(newest_folder) >= arguments.steps:
            logger.info("Voice %s has trained %d steps already; skipping it", voice, arguments.steps)
            continue
        settings = build_training_settings(voice, folders, arguments)
        result = train_voice(settings, build_lora_settings(arguments), environment)
        if result.stop_signal is not None:
            return result.stop_signal
    return None


def run_pipeline(arguments: argparse.Namespace, environment: TrainEnvironment) -> int:
    """Run the pipeline stages in order, from the download to the optional publish.

    Args:
        arguments: Parsed pipeline flags.
        environment: Hub token and distributed layout.

    Returns:
        0 when every stage ran, or 128 plus the number of the signal that stopped a voice.

    """
    run_folder = arguments.runs_folder / arguments.run_name
    if arguments.samples_only:
        base_model_folder = download_snapshot(
            arguments.base_model_repo, REPO_TYPE_MODEL, arguments.cache_folder, environment.hf_token
        )
        print_result("base_model_folder", base_model_folder)
    else:
        dataset_folder, base_model_folder = download_inputs(
            arguments.dataset_repo, arguments.base_model_repo, arguments.cache_folder, environment.hf_token
        )
        prepared = prepare_inputs(dataset_folder, base_model_folder, run_folder, arguments.val_split)
        stop_signal = _train_voices(arguments, environment, base_model_folder, prepared)
        if stop_signal is not None:
            logger.warning("Signal %d stopped the run; run it again to resume from the newest checkpoint", stop_signal)
            return EXIT_SIGNAL_BASE + stop_signal
    checkpoints_folder = run_folder / CHECKPOINTS_FOLDER
    samples_folder = run_folder / SAMPLES_FOLDER
    sampler = SamplerSettings(guidance_scale=GUIDANCE_SCALE, timesteps=TIMESTEPS, max_patches=MAX_PATCHES)
    write_run_samples(checkpoints_folder, base_model_folder, samples_folder, sampler)
    if arguments.publish:
        request = PublishRequest(
            run_name=arguments.run_name,
            checkpoints_folder=checkpoints_folder,
            base_model_folder=base_model_folder,
            tokenizer_folder=run_folder / TOKENIZER_FOLDER,
            samples_folder=samples_folder,
            output_repo=arguments.output_repo,
            base_model_repo=arguments.base_model_repo,
            public=arguments.public,
        )
        publish_adapters(request, environment.hf_token)
    return EXIT_SUCCESS


def main(argument_values: Sequence[str] | None = None) -> int:
    """Run the pipeline command.

    Args:
        argument_values: Command flags; None reads `sys.argv`.

    Returns:
        0 on success, 1 on a failure or a refused --clean, 128 plus the signal number on a stop.

    """
    configure_logging()
    arguments, environment = _parse_arguments(argument_values)
    run_folder = arguments.runs_folder / arguments.run_name
    if arguments.clean and run_folder.exists():
        if not (arguments.yes or _ask_clean_consent(run_folder)):
            logger.error("Kept %s; the run did not start", run_folder)
            return EXIT_FAILURE
        shutil.rmtree(run_folder)
        logger.info("Deleted %s", run_folder)
    try:
        return run_pipeline(arguments, environment)
    except PIPELINE_ERRORS as error:
        print_failure("The pipeline", error)
        return EXIT_FAILURE
    except KeyboardInterrupt:
        logger.warning("Interrupted outside a training step, which keeps every checkpoint written so far")
        return EXIT_SIGNAL_BASE + signal.SIGINT


if __name__ == "__main__":
    raise SystemExit(main())

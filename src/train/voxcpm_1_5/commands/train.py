"""Train the LoRA adapter of one voice on a CUDA GPU, resuming from its newest checkpoint.

The last checkpoint goes to stdout as a key=value line: checkpoint_folder. SIGINT or SIGTERM stop the run after the
current step and write a checkpoint, and the next run of the voice resumes from it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from pathlib import Path

from config.voices import VOICES
from src.train.cli import (
    EXIT_FAILURE,
    EXIT_SUCCESS,
    EXIT_SIGNAL_BASE,
    build_parser,
    add_path_flag,
    parse_positive_int,
    parse_positive_float,
    read_command_environment,
)
from src.train.logs import print_result, print_failure, configure_logging
from config.voxcpm_1_5.lora import (
    LORA_RANK,
    LORA_ALPHA,
    LORA_DROPOUT,
    LORA_ENABLE_LM,
    LORA_ENABLE_DIT,
    LORA_ENABLE_PROJ,
    LORA_TARGET_MODULES,
)
from config.voxcpm_1_5.training import (
    STEPS,
    BATCH_SIZE,
    LOG_INTERVAL,
    VAL_INTERVAL,
    WARMUP_STEPS,
    WEIGHT_DECAY,
    LEARNING_RATE,
    LOADER_WORKERS,
    LOSS_DIFF_WEIGHT,
    LOSS_STOP_WEIGHT,
    MAX_BATCH_TOKENS,
    ACCUMULATION_STEPS,
    CHECKPOINT_INTERVAL,
)
from schemas.voxcpm_1_5.training import LoraSettings, TrainingFolders, TrainingSettings
from src.train.voxcpm_1_5.training.job import TrainingDataError, run_training_job
from src.train.voxcpm_1_5.data.manifest import ManifestError
from src.train.voxcpm_1_5.training.devices import GpuError, assert_cuda_available
from src.train.voxcpm_1_5.training.checkpoints import CheckpointError

if TYPE_CHECKING:
    import argparse
    from collections.abc import Sequence

    from schemas.settings import TrainEnvironment
    from schemas.voxcpm_1_5.training import TrainingResult

PROGRAM = "python -m src.train voxcpm_1_5 train"
EXAMPLE = (
    f"{PROGRAM} --voice female --base-model-folder BASE_MODEL --train-manifest RUN/manifests/train.jsonl "
    "--tokenizer-folder RUN/tokenizer --checkpoints-folder RUN/checkpoints --events-folder RUN/events"
)
TRAINING_ERRORS = (GpuError, TrainingDataError, CheckpointError, ManifestError, OSError)


def _parse_arguments(argument_values: Sequence[str] | None) -> tuple[argparse.Namespace, TrainEnvironment]:
    parser = build_parser(PROGRAM, __doc__, EXAMPLE, is_interruptible=True)
    parser.add_argument("--voice", required=True, choices=tuple(VOICES), help="the voice whose adapter trains")
    for flag, destination, help_text in (
        ("--base-model-folder", "base_model_folder", "the downloaded base model folder"),
        ("--train-manifest", "train_manifest_path", "the manifest of the training clips"),
        ("--tokenizer-folder", "tokenizer_folder", "the tokenizer folder that each checkpoint copies"),
        ("--checkpoints-folder", "checkpoints_folder", "the checkpoints folder of the run, one folder per voice"),
        ("--events-folder", "events_folder", "the TensorBoard events folder of the run, one folder per voice"),
    ):
        add_path_flag(parser, flag, destination, help_text)
    parser.add_argument(
        "--val-manifest",
        dest="val_manifest_path",
        type=Path,
        metavar="FILE",
        help="the manifest of the validation clips",
    )
    add_training_flags(parser)
    arguments = parser.parse_args(argument_values)
    return arguments, read_command_environment(parser)


def add_training_flags(parser: argparse.ArgumentParser) -> None:
    """Add the training flags: batch size, learning rate, steps, and LoRA rank and alpha.

    Args:
        parser: Parser of a command that trains.

    """
    parser.add_argument(
        "--batch-size", type=parse_positive_int, default=BATCH_SIZE, help="clips per batch (default: %(default)s)"
    )
    parser.add_argument(
        "--learning-rate",
        type=parse_positive_float,
        default=LEARNING_RATE,
        help="the peak learning rate (default: %(default)s)",
    )
    parser.add_argument(
        "--steps",
        type=parse_positive_int,
        default=STEPS,
        help="the optimizer steps of each voice (default: %(default)s)",
    )
    parser.add_argument(
        "--lora-rank", type=parse_positive_int, default=LORA_RANK, help="the rank of the adapter (default: %(default)s)"
    )
    parser.add_argument(
        "--lora-alpha",
        type=parse_positive_int,
        default=LORA_ALPHA,
        help="the scaling factor of the adapter (default: %(default)s)",
    )


def build_training_settings(voice: str, folders: TrainingFolders, arguments: argparse.Namespace) -> TrainingSettings:
    """Build the run settings from the training flags and the defaults.

    Args:
        voice: Voice whose adapter trains.
        folders: Files and folders of the run.
        arguments: Flags from `add_training_flags`.

    Returns:
        The settings.

    """
    return TrainingSettings(
        voice=voice,
        folders=folders,
        batch_size=arguments.batch_size,
        accumulation_steps=ACCUMULATION_STEPS,
        loader_workers=LOADER_WORKERS,
        steps=arguments.steps,
        learning_rate=arguments.learning_rate,
        weight_decay=WEIGHT_DECAY,
        warmup_steps=WARMUP_STEPS,
        max_batch_tokens=MAX_BATCH_TOKENS,
        log_interval=LOG_INTERVAL,
        val_interval=VAL_INTERVAL,
        checkpoint_interval=CHECKPOINT_INTERVAL,
        loss_diff_weight=LOSS_DIFF_WEIGHT,
        loss_stop_weight=LOSS_STOP_WEIGHT,
    )


def build_lora_settings(arguments: argparse.Namespace) -> LoraSettings:
    """Build the LoRA settings from the training flags and the defaults.

    Args:
        arguments: Flags from `add_training_flags`.

    Returns:
        The LoRA settings.

    """
    return LoraSettings(
        enable_lm=LORA_ENABLE_LM,
        enable_dit=LORA_ENABLE_DIT,
        enable_proj=LORA_ENABLE_PROJ,
        rank=arguments.lora_rank,
        alpha=arguments.lora_alpha,
        dropout=LORA_DROPOUT,
        target_modules=LORA_TARGET_MODULES,
    )


def train_voice(settings: TrainingSettings, lora: LoraSettings, environment: TrainEnvironment) -> TrainingResult:
    """Train the adapter of one voice on the CUDA GPU of the process, and print the last checkpoint.

    Without a CUDA GPU, raise GpuError before reading the base model.

    Args:
        settings: Run settings.
        lora: LoRA settings of a fresh run.
        environment: Distributed layout of the process.

    Returns:
        The last checkpoint, and the signal that stopped the run, if any.

    """
    assert_cuda_available()
    result = run_training_job(settings, lora, environment)
    print_result("checkpoint_folder", result.checkpoint_folder)
    return result


def main(argument_values: Sequence[str] | None = None) -> int:
    """Run the train command.

    Args:
        argument_values: Command flags; None reads `sys.argv`.

    Returns:
        0 on success, 1 on a failure such as no CUDA GPU, 128 plus the signal number on a stop.

    """
    configure_logging()
    arguments, environment = _parse_arguments(argument_values)
    folders = TrainingFolders(
        base_model_folder=arguments.base_model_folder,
        train_manifest_path=arguments.train_manifest_path,
        val_manifest_path=arguments.val_manifest_path,
        tokenizer_folder=arguments.tokenizer_folder,
        voice_checkpoints_folder=arguments.checkpoints_folder / arguments.voice,
        voice_events_folder=arguments.events_folder / arguments.voice,
    )
    settings = build_training_settings(arguments.voice, folders, arguments)
    try:
        result = train_voice(settings, build_lora_settings(arguments), environment)
    except TRAINING_ERRORS as error:
        print_failure("Training", error)
        return EXIT_FAILURE
    return EXIT_SUCCESS if result.stop_signal is None else EXIT_SIGNAL_BASE + result.stop_signal


if __name__ == "__main__":
    raise SystemExit(main())

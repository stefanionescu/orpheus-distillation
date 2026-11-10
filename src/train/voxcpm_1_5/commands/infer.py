"""Write sample clips for every voice that has a checkpoint.

Each clip goes to stdout as a key=value line: sample.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from config.voices import VOICES
from src.train.cli import (
    EXIT_FAILURE,
    EXIT_SUCCESS,
    build_parser,
    add_path_flag,
    parse_positive_int,
    parse_non_negative_float,
)
from src.train.logs import print_result, print_failure, configure_logging
from config.voxcpm_1_5.samples import SAMPLE_PROMPTS
from config.voxcpm_1_5.inference import TIMESTEPS, MAX_PATCHES, GUIDANCE_SCALE
from schemas.voxcpm_1_5.inference import SampleSettings, SamplerSettings
from src.train.voxcpm_1_5.inference.samples import write_samples
from src.train.voxcpm_1_5.training.checkpoints import CheckpointError
from src.train.voxcpm_1_5.inference.synthesizer import AdapterError

if TYPE_CHECKING:
    from pathlib import Path
    import argparse
    from collections.abc import Sequence

PROGRAM = "python -m src.train voxcpm_1_5 infer"
EXAMPLE = f"{PROGRAM} --checkpoints-folder RUN/checkpoints --base-model-folder BASE_MODEL --samples-folder RUN/samples"


def _parse_arguments(argument_values: Sequence[str] | None) -> argparse.Namespace:
    parser = build_parser(PROGRAM, __doc__, EXAMPLE)
    add_path_flag(
        parser,
        "--checkpoints-folder",
        "checkpoints_folder",
        "the checkpoints folder of the run, one folder per voice",
    )
    add_path_flag(parser, "--base-model-folder", "base_model_folder", "the downloaded base model folder")
    add_path_flag(parser, "--samples-folder", "samples_folder", "the folder that receives the sample clips")
    parser.add_argument(
        "--guidance-scale",
        type=parse_non_negative_float,
        default=GUIDANCE_SCALE,
        help="the classifier-free guidance scale (default: %(default)s)",
    )
    parser.add_argument(
        "--timesteps",
        type=parse_positive_int,
        default=TIMESTEPS,
        help="the diffusion steps of each audio patch (default: %(default)s)",
    )
    parser.add_argument(
        "--max-patches",
        type=parse_positive_int,
        default=MAX_PATCHES,
        help="the most audio patches of one clip (default: %(default)s)",
    )
    return parser.parse_args(argument_values)


def write_run_samples(
    checkpoints_folder: Path, base_model_folder: Path, samples_folder: Path, sampler: SamplerSettings
) -> list[Path]:
    """Write one clip per prompt for each voice that has a checkpoint, and print each path.

    No checkpoint of any voice raises CheckpointError, and an adapter that does not fit raises AdapterError.

    Args:
        checkpoints_folder: The checkpoints folder of the run, one folder per voice.
        base_model_folder: Downloaded base model.
        samples_folder: Where the clips go; the call creates it when missing.
        sampler: Sampler settings of each clip.

    Returns:
        The clips, voice by voice.

    """
    settings = SampleSettings(voices=tuple(VOICES), prompts=SAMPLE_PROMPTS, sampler=sampler)
    sample_paths = write_samples(checkpoints_folder, base_model_folder, samples_folder, settings)
    for sample_path in sample_paths:
        print_result("sample", sample_path)
    return sample_paths


def main(argument_values: Sequence[str] | None = None) -> int:
    """Run the infer command.

    Args:
        argument_values: Command flags; None reads `sys.argv`.

    Returns:
        0 on success, 1 when no voice has a checkpoint, an adapter does not fit, or a file is missing.

    """
    configure_logging()
    arguments = _parse_arguments(argument_values)
    sampler = SamplerSettings(
        guidance_scale=arguments.guidance_scale, timesteps=arguments.timesteps, max_patches=arguments.max_patches
    )
    try:
        write_run_samples(arguments.checkpoints_folder, arguments.base_model_folder, arguments.samples_folder, sampler)
    except (CheckpointError, AdapterError, OSError) as error:
        print_failure("Writing the samples", error)
        return EXIT_FAILURE
    return EXIT_SUCCESS


if __name__ == "__main__":
    raise SystemExit(main())

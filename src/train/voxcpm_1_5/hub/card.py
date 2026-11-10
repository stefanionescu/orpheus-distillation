"""The model card of the published adapters."""

from __future__ import annotations

from string import Template
from typing import TYPE_CHECKING
from pathlib import Path

from config.voices import VOICES
from config.voxcpm_1_5.hub import SAMPLES_FOLDER, ADAPTERS_FOLDER, MODEL_CARD_TEMPLATE, MODEL_CARD_TEMPLATE_FOLDER
from config.voxcpm_1_5.data import TOKENIZER_FILES
from config.voxcpm_1_5.model import MODEL_SAMPLE_RATE
from config.voxcpm_1_5.checkpoints import LORA_CONFIG_FILE, TRAINING_STATE_FILE
from src.train.voxcpm_1_5.model.lora import LORA_WEIGHTS_FILE
from src.train.voxcpm_1_5.model.loader import AUDIO_VAE_FILE, MODEL_CONFIG_FILE

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence

    from schemas.voxcpm_1_5.publish import PublishRequest
    from src.train.voxcpm_1_5.model.config import LoraConfig

ADAPTER_PATH_TEMPLATE = f"{ADAPTERS_FOLDER}/<voice>/{{filename}}"


def _format_table(header: Sequence[str], rows: Sequence[Sequence[str]]) -> str:
    lines = [header, ["---"] * len(header), *rows]
    return "\n".join(f"| {' | '.join(cells)} |" for cells in lines)


def _format_layers(layers: Sequence[str], *, enabled: bool) -> str:
    return ", ".join(f"`{layer}`" for layer in layers) if enabled else "none"


def format_files_table(model_weights_filename: str, *, has_samples: bool) -> str:
    """Format the Markdown table of the published files.

    Args:
        model_weights_filename: Base model weights file name.
        has_samples: Whether the repository holds sample clips.

    Returns:
        The table.

    """
    tokenizer_files = ", ".join(f"`{filename}`" for filename in TOKENIZER_FILES)
    rows = [
        [f"`{ADAPTER_PATH_TEMPLATE.format(filename=LORA_WEIGHTS_FILE)}`", "The adapter weights of one voice"],
        [f"`{ADAPTER_PATH_TEMPLATE.format(filename=LORA_CONFIG_FILE)}`", "The LoRA config of the adapter"],
        [f"`{ADAPTER_PATH_TEMPLATE.format(filename=TRAINING_STATE_FILE)}`", "The steps that the adapter trained"],
        [f"`{model_weights_filename}`", "The base model weights"],
        [f"`{MODEL_CONFIG_FILE}`", "The base model config"],
        [f"`{AUDIO_VAE_FILE}`", "The audio VAE weights"],
        [tokenizer_files, "The tokenizer"],
    ]
    if has_samples:
        rows.append([f"`{SAMPLES_FOLDER}/`", "Sample clips of each voice"])
    return _format_table(["File", "Content"], rows)


def format_card(
    request: PublishRequest, lora_config: LoraConfig, voice_steps: Mapping[str, int], files_table: str
) -> str:
    """Fill the model card template.

    Args:
        request: Run and repositories that the card names.
        lora_config: LoRA config that the adapters store.
        voice_steps: Optimizer steps per published voice, in table order.
        files_table: Output of `format_files_table`.

    Returns:
        Markdown text of the card.

    Raises:
        ValueError: `voice_steps` is empty.

    """
    if not voice_steps:
        message = "A model card needs at least one published voice"
        raise ValueError(message)
    voice_rows = [
        [voice, VOICES[voice].display_name, f"`{ADAPTERS_FOLDER}/{voice}`", str(steps)]
        for voice, steps in voice_steps.items()
    ]
    parameter_rows = [
        ["Rank", str(lora_config.r)],
        ["Alpha", str(lora_config.alpha)],
        ["Dropout", str(lora_config.dropout)],
        ["Language model layers", _format_layers(lora_config.target_modules_lm, enabled=lora_config.enable_lm)],
        [
            "Diffusion transformer layers",
            _format_layers(lora_config.target_modules_dit, enabled=lora_config.enable_dit),
        ],
        ["Projection layers", _format_layers(lora_config.target_proj_modules, enabled=lora_config.enable_proj)],
    ]
    card_fields = {
        "run_name": request.run_name,
        "base_model_repo": request.base_model_repo,
        "output_repo": request.output_repo,
        "sample_rate": str(MODEL_SAMPLE_RATE),
        "voice_table": _format_table(["Voice", "Orpheus speaker", "Adapter folder", "Training steps"], voice_rows),
        "parameters_table": _format_table(["Setting", "Value"], parameter_rows),
        "files_table": files_table,
        "first_voice": next(iter(voice_steps)),
        "adapters_folder": ADAPTERS_FOLDER,
        "lora_config_file": LORA_CONFIG_FILE,
    }
    template_path = Path(__file__).with_name(MODEL_CARD_TEMPLATE_FOLDER) / MODEL_CARD_TEMPLATE
    return Template(template_path.read_text(encoding="utf-8")).substitute(card_fields)

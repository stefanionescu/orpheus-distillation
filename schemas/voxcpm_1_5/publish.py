"""What the publish command stages and uploads."""

from __future__ import annotations

from typing import TYPE_CHECKING
from dataclasses import dataclass

if TYPE_CHECKING:
    from pathlib import Path


@dataclass(frozen=True)
class PublishRequest:
    """The folders and repositories of one publish run.

    Attributes:
        run_name: Training run name, which the model card shows.
        checkpoints_folder: The checkpoints folder of the run, one folder per voice.
        base_model_folder: Downloaded base model.
        tokenizer_folder: Tokenizer files.
        samples_folder: Sample WAV files, or None to publish no samples.
        output_repo: Hub repository that receives the adapters.
        base_model_repo: Hub repository of the base model.
        public: Make a new output repository public; otherwise it is private.

    """

    run_name: str
    checkpoints_folder: Path
    base_model_folder: Path
    tokenizer_folder: Path
    samples_folder: Path | None
    output_repo: str
    base_model_repo: str
    public: bool

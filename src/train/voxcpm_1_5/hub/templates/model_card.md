---
language: en
license: apache-2.0
base_model: $base_model_repo
pipeline_tag: text-to-speech
tags:
  - voxcpm
  - text-to-speech
  - lora
  - orpheus-distillation
---

# VoxCPM 1.5 Orpheus distillation adapters

LoRA adapters for the VoxCPM 1.5 model `$base_model_repo`, one for each voice,
from the training run `$run_name`. Training fit each adapter to clips that Orpheus TTS
synthesized in one voice, so the base model with that adapter speaks in that
voice. The audio is mono at $sample_rate Hz.

## Voices

$voice_table

## Usage

The adapters load into the VoxCPM 1.5 model code of the training repository,
[orpheus-distillation](https://github.com/stefanionescu/orpheus-distillation).
Run this from the root of a clone of that repository:

```python
import json
from pathlib import Path

import soundfile
from huggingface_hub import snapshot_download

from config.voxcpm_1_5.inference import TIMESTEPS, MAX_PATCHES, GUIDANCE_SCALE
from schemas.voxcpm_1_5.inference import SamplerSettings
from src.train.voxcpm_1_5.model.config import LoraConfig
from src.train.voxcpm_1_5.model.voxcpm import VoxCPMModel

repo_folder = Path(snapshot_download("$output_repo"))
adapter_folder = repo_folder / "$adapters_folder" / "$first_voice"
config_text = (adapter_folder / "$lora_config_file").read_text(encoding="utf-8")
lora_config = LoraConfig(**json.loads(config_text))
model = VoxCPMModel.read_pretrained(repo_folder, optimize=False, training=False, lora_config=lora_config)
model.read_lora_weights(adapter_folder)
model.set_lora_enabled(enabled=True)
# The adapter selects the voice.
settings = SamplerSettings(guidance_scale=GUIDANCE_SCALE, timesteps=TIMESTEPS, max_patches=MAX_PATCHES)
waveform = model.generate("Hello, how are you today?", settings)
soundfile.write("$first_voice.wav", waveform.squeeze(0).float().numpy(), model.sample_rate)
```

To switch voices, call `model.read_lora_weights` with the adapter folder of
another voice. The base model stays in memory.

## Training parameters

$parameters_table

## Files

$files_table

## License

The adapters keep the
[Apache 2.0 license](https://www.apache.org/licenses/LICENSE-2.0) of the base
model.

## Citation

```bibtex
@article{voxcpm2025,
  title   = {VoxCPM: Tokenizer-Free TTS for Context-Aware Speech Generation and True-to-Life Voice Cloning},
  author  = {Zhou, Yixuan and Zeng, Guoyang and Liu, Xin and Li, Xiang and Yu, Renjie and Wang, Ziyang and Ye, Runchuan and Sun, Weiyue and Gui, Jiancheng and Li, Kehan and Wu, Zhiyong and Liu, Zhiyuan},
  journal = {arXiv preprint arXiv:2509.24650},
  year    = {2025},
}
```

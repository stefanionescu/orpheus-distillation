---
license: apache-2.0
pretty_name: Orpheus Distillation Dataset
task_categories:
  - text-to-speech
  - audio-classification
language:
  - en
tags:
  - orpheus
  - tts
  - voice-distillation
  - synthetic-speech
size_categories:
  - ${size_category}
---

# Orpheus Distillation dataset

Speech clips that the [Orpheus TTS](https://github.com/canopyai/Orpheus-TTS) model synthesized from English prompts,
for training smaller text-to-speech models on its voices.

## How the clips came about

The dataset command sends each prompt to an Orpheus server once per voice and stores the audio that the server streams
back. Each prompt becomes one clip as written, and the command synthesizes a repeated prompt once. For each clip, it
measures the silence before the speech starts.

## Voices

<table>
  <thead>
    <tr><th>Voice</th><th>Speaker</th><th>Clips</th><th>Duration</th></tr>
  </thead>
  <tbody>
${voice_rows}
  </tbody>
</table>

## Shard format

The dataset is a set of WebDataset shards. Each shard is a tar file that holds two members per clip with the same stem.

| Property      | Value                                                                                                     |
| ------------- | --------------------------------------------------------------------------------------------------------- |
| Shard folder  | `${shards_folder}`                                                                                        |
| Shards        | ${shard_count}                                                                                            |
| Audio member  | `<key>${audio_extension}`: WAV, ${sample_rate_khz} kHz, ${channels} channel, ${sample_width_bits}-bit PCM |
| Record member | `<key>${record_extension}`: one JSON object                                                               |

The JSON record of each clip holds these fields.

| Field                         | Meaning                                         |
| ----------------------------- | ----------------------------------------------- |
| `${text_field}`               | The prompt that the voice read aloud.           |
| `${speaker_field}`            | The Orpheus speaker of the clip.                |
| `${voice_field}`              | The voice of the clip.                          |
| `${duration_field}`           | The length of the clip in seconds.              |
| `${leading_silence_ms_field}` | The silence before the speech, in milliseconds. |

## Usage

Load the dataset with the `datasets` library:

```python
from datasets import load_dataset

dataset = load_dataset("${repo}")
```

Stream the shards with the `webdataset` library, which keys each member by its extension without the dot:

```python
import json

import webdataset

dataset = webdataset.WebDataset(
    "https://huggingface.co/datasets/${repo}/resolve/main/${shards_folder}/${shard_range}"
)
for sample in dataset:
    record = json.loads(sample["${record_key}"])
    print(record["${text_field}"], len(sample["${audio_key}"]))
```

## License

The Apache 2.0 license covers the dataset.

## Citation

```bibtex
@misc{orpheus-distillation-dataset,
  title = {Orpheus Distillation Dataset},
  year = {${year}},
  url = {https://huggingface.co/datasets/${repo}}
}
```

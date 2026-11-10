# Orpheus Distillation

This repository distills the voices of the Orpheus TTS model into other speech
models. The dataset command synthesizes speech with an Orpheus server and
publishes it to the Hugging Face Hub as WebDataset shards. The training command
fine-tunes a target model on those shards, with one LoRA adapter per voice, and
publishes the adapters.

The training code does not depend on one model. Each target model is a package
under `src/train/`, and `python -m src.train MODEL COMMAND` runs it.

## Contents

- [Models and voices](#models-and-voices)
- [Requirements](#requirements)
- [Set up](#set-up)
- [Generate the dataset](#generate-the-dataset)
- [Train a model](#train-a-model)
- [Publish](#publish)
- [Resume a stopped run](#resume-a-stopped-run)
- [Output files](#output-files)
- [Add a target model](#add-a-target-model)
- [Run the tests](#run-the-tests)
- [Troubleshoot](#troubleshoot)
- [License](#license)

## Models and voices

| Model      | Package      | Base model                                                    | Default output repository                |
| ---------- | ------------ | ------------------------------------------------------------- | ---------------------------------------- |
| VoxCPM 1.5 | `voxcpm_1_5` | [OpenBMB VoxCPM1.5](https://huggingface.co/openbmb/VoxCPM1.5) | `yapwithai/voxcpm-1.5-orpheus-distilled` |

List the models that the training command accepts:

```shell
uv run --extra train python -m src.train --help
```

Two Orpheus speakers read the dataset. Commands and flags take the voice. Clip
file names hold the speaker, and shard records hold both.

| Voice    | Orpheus speaker |
| -------- | --------------- |
| `female` | `tara`          |
| `male`   | `zac`           |

## Requirements

- `mise`, which installs the pinned Python and `uv`.
- For the dataset: an Orpheus TTS server that the host reaches over WebSocket,
  and its API key.
- For training: Linux with a CUDA GPU and `nvidia-smi`.
- For background runs: Linux with `setsid`. On macOS, run commands in the
  foreground.
- For publishing and private downloads: a Hugging Face token.

## Set up

```shell
mise run setup
cp .env.example .env
```

Fill in `.env`. mise loads it into every task.

| Variable             | Used by                                                   |
| -------------------- | --------------------------------------------------------- |
| `ORPHEUS_SERVER_URL` | Dataset generation. `--server` overrides it.              |
| `ORPHEUS_API_KEY`    | Dataset generation. `--api-key` overrides it.             |
| `HF_TOKEN`           | Every publish, and downloads of a private dataset.        |
| `WORLD_SIZE`         | Distributed training. `torchrun` sets it; leave it empty. |
| `LOCAL_RANK`         | Distributed training. `torchrun` sets it; leave it empty. |

## Generate the dataset

Run a smoke test of 10 prompts, then generate and publish the full dataset:

```shell
mise run dataset:start -- --max-prompts 10 --yes
mise run dataset:start -- --yes --publish
```

The task starts the run in the background and follows its log. Control+C stops
the log, not the run. `mise run dataset:stop` stops the run, and
`mise run dataset:logs` follows its log again.

A run without `--resume` cleans its output folder first. With no terminal to
confirm, it needs `--yes`.

On macOS, run the command in the foreground:

```shell
uv run --extra dataset python -m src.dataset --max-prompts 10
```

| Flag                | Effect                                                                      |
| ------------------- | --------------------------------------------------------------------------- |
| `--server`          | The Orpheus server: an `http`, `https`, `ws`, or `wss` URL, or `host:port`. |
| `--api-key`         | The Orpheus API key.                                                        |
| `--prompts-file`    | A file with one prompt per line, in place of the built-in corpus.           |
| `--voice`           | Synthesize only `female` or only `male`.                                    |
| `--max-prompts`     | Synthesize at most this many prompts.                                       |
| `--clips-per-shard` | Clips in each shard.                                                        |
| `--concurrency`     | Requests at once.                                                           |
| `--resume`          | Keep the existing clips and synthesize the rest.                            |
| `--output-folder`   | The output folder.                                                          |
| `--yes`             | Clean the output folder without asking.                                     |
| `--publish`         | Publish the dataset after the run.                                          |
| `--publish-only`    | Publish the dataset in `--output-folder` and synthesize nothing.            |
| `--dataset-repo`    | The Hugging Face dataset repository.                                        |
| `--public`          | Make a new repository public. New repositories start private.               |

`--help` prints the defaults. The command exits with `0` on success, `1` on a
failure, `2` on a usage error, `130` after Control+C, and `143` after `SIGTERM`.

## Train a model

Training downloads the dataset from the Hub, so publish it first. Start a run of
VoxCPM 1.5:

```shell
mise run train:start -- voxcpm_1_5 --run-name first-run
```

The task checks for a GPU, starts the pipeline in the background, and follows
its log. The pipeline runs these stages:

1. Download the dataset shards and the base model into the download cache.
1. Prepare the training manifests and copy the tokenizer into the run folder.
1. Train one adapter per voice, with checkpoints. The pipeline skips a voice
   that finished its steps.
1. Write sample clips for every voice that has a checkpoint.
1. Publish the adapters and samples, with `--publish` only.

Each stage prints its results as `key=value` lines. `mise run train:stop` stops
training after the current step, with a checkpoint. `mise run train:logs`
follows the log again.

| Flag                | Effect                                                         |
| ------------------- | -------------------------------------------------------------- |
| `--run-name`        | Names the run and its folder. Required.                        |
| `--voices`          | The voices to train, in order.                                 |
| `--dataset-repo`    | The dataset repository.                                        |
| `--base-model-repo` | The base model repository.                                     |
| `--output-repo`     | The model repository that `--publish` uploads to.              |
| `--batch-size`      | Clips per batch.                                               |
| `--learning-rate`   | The peak learning rate.                                        |
| `--steps`           | Optimizer steps per voice.                                     |
| `--lora-rank`       | The adapter rank.                                              |
| `--lora-alpha`      | The adapter scaling factor.                                    |
| `--val-split`       | The share of clips that validation keeps, from 0 up to 1.      |
| `--cache-folder`    | The download cache.                                            |
| `--runs-folder`     | The folder that holds one folder per run.                      |
| `--publish`         | Publish the adapters and samples after inference.              |
| `--public`          | Make a new repository public. New repositories start private.  |
| `--samples-only`    | Skip download, preparation, and training; write samples only.  |
| `--clean`           | Delete the run folder first. Needs `--yes` without a terminal. |
| `--yes`             | Confirm `--clean` without a prompt.                            |

Print the defaults:

```shell
uv run --extra train python -m src.train voxcpm_1_5 pipeline --help
```

The pipeline exits with `0` on success, `1` on a failure, `2` on a usage error,
and 128 plus the signal number after a stop signal.

### Run one stage

Each stage has its own command, which prints the paths that the next stage
takes. The tasks take the model as their first argument:

```shell
mise run train:download -- voxcpm_1_5 --cache-folder .cache/voxcpm
mise run train:prepare -- voxcpm_1_5 --dataset-folder <dataset-folder> \
  --base-model-folder <base-model-folder> --run-folder <run-folder>
mise run train:infer -- voxcpm_1_5 --checkpoints-folder <run-folder>/checkpoints \
  --base-model-folder <base-model-folder> --samples-folder <run-folder>/samples
```

Train one voice in the foreground. The tokenizers library deadlocks in loader
workers, so turn off its threads:

```shell
TOKENIZERS_PARALLELISM=false uv run --extra train python -m src.train voxcpm_1_5 train \
  --voice female --base-model-folder <base-model-folder> \
  --train-manifest <run-folder>/manifests/train.jsonl --tokenizer-folder <run-folder>/tokenizer \
  --checkpoints-folder <run-folder>/checkpoints --events-folder <run-folder>/events
```

## Publish

Every publish needs `HF_TOKEN` with write access to the repository.

```shell
mise run dataset:publish -- --dataset-repo <owner>/<dataset>
mise run train:start -- voxcpm_1_5 --run-name first-run --publish
```

`dataset:publish` publishes the dataset in the output folder without synthesizing.
It creates a private repository unless it gets `--public`, uploads the card,
replaces the shards, and uploads the stats file.

Publish a finished run without the pipeline. `--dry-run` stages the files and
the card without uploading them:

```shell
mise run train:publish -- voxcpm_1_5 \
  --run-name first-run --checkpoints-folder <run-folder>/checkpoints \
  --base-model-folder <base-model-folder> --tokenizer-folder <run-folder>/tokenizer \
  --samples-folder <run-folder>/samples --output-repo <owner>/<model>
```

A model publish creates a private repository unless it gets `--public`, then
uploads the adapters, the base model files, the tokenizer, the samples, and a
model card in one commit. A repository that already exists keeps its visibility.

## Resume a stopped run

A dataset run writes a fingerprint of its prompts and voices before the first
clip. `--resume` keeps every readable clip and synthesizes the rest. It refuses
to start when the prompts or voices differ from the fingerprint. Pass the same
`--prompts-file`, `--max-prompts`, and `--voice` as the first run:

```shell
mise run dataset:start -- --resume
```

A training run resumes each voice from its newest checkpoint. Start it again
with the same `--run-name`.

## Output files

The dataset output folder, `dataset_output` by default:

| Path                               | Holds                                              |
| ---------------------------------- | -------------------------------------------------- |
| `audio/clip_<index>_<speaker>.wav` | One clip: 24 kHz, mono, 16-bit PCM.                |
| `shards/shard-<index>.tar`         | The shards. Each clip is a WAV and a JSON record.  |
| `stats.json`                       | Counts, durations, and the fingerprint fields.     |
| `fingerprint.json`                 | The prompt hash and voices that `--resume` checks. |

Each JSON record holds `text`, `speaker`, `voice`, `duration` in seconds, and
`leading_silence_ms`.

A training run folder, `training_output/<run-name>` by default:

| Path                               | Holds                                                        |
| ---------------------------------- | ------------------------------------------------------------ |
| `manifests/`                       | The training and validation manifests.                       |
| `tokenizer/`                       | The tokenizer of the base model.                             |
| `checkpoints/<voice>/step_<step>/` | Adapter weights, LoRA config, optimizer, and training state. |
| `checkpoints/<voice>/newest`       | A link to the newest checkpoint of the voice.                |
| `events/<voice>/`                  | TensorBoard events.                                          |
| `samples/`                         | Sample clips of each voice.                                  |
| `staging/`                         | The files that a publish uploads.                            |

## Add a target model

1. Add `config/<model>/`, `schemas/<model>/`, and `src/train/<model>/`. The
   package's `__main__.py` exposes `main()`, which runs its commands.
1. Add the model to `MODELS` in `src/train/__main__.py`.
1. Add its tests to `tests/suites/unit/<model>/` and `tests/suites/e2e/<model>/`.
1. Add the model to the table in [Models and voices](#models-and-voices).

## Run the tests

```shell
mise run test
```

`mise run test` runs the unit and integration suites; `test:unit` and
`test:integration` run one each. `mise run test:e2e` needs a live Orpheus server
and a CUDA GPU; `test:e2e:synthesis` needs only the server, and
`test:e2e:training` only the GPU.

## Troubleshoot

- Exit code `2`: the message names the flag or variable to fix.
- "Background runs need Linux": run the printed `uv run` command in the
  foreground.
- A Hub error on download: `HF_TOKEN` needs read access to a private dataset.
- `--resume` refuses to start: the prompts or voices changed. Pass the values of
  the first run, or start without `--resume`.
- Training exits with 128 plus a signal number: a stop signal ended it after a
  checkpoint. Start the run again to resume it.

## License

[Apache 2.0](LICENSE.md)

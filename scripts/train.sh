#!/usr/bin/env bash
# Start the training pipeline of one model in the background and follow its log.
# Runtime: Bash 3.2+, Linux.

set -euo pipefail

# shellcheck source=scripts/lib/environment.sh
source "$(dirname -- "${BASH_SOURCE[0]}")/lib/environment.sh"
LIBRARY_FOLDER="$(get_scripts_folder)/lib"
readonly LIBRARY_FOLDER
# shellcheck source=scripts/lib/gpu.sh
source "${LIBRARY_FOLDER}/gpu.sh"
# shellcheck source=scripts/lib/uv.sh
source "${LIBRARY_FOLDER}/uv.sh"
# shellcheck source=scripts/lib/follow.sh
source "${LIBRARY_FOLDER}/follow.sh"

readonly TRAIN_PROCESS_NAME="train"
readonly TRAIN_EXTRA="train"
readonly TRAIN_COMMAND="pipeline"
readonly TRAIN_USAGE_LINES=(
  "Usage: mise run train:start -- MODEL --run-name NAME [PIPELINE_FLAGS]"
  ""
  "Start the training pipeline of MODEL in the background and follow its log."
  "Control+C stops the follow. mise run train:stop stops training after a"
  "checkpoint. Background runs need Linux; on macOS run in the foreground:"
  "  uv run --extra train python -m src.train MODEL pipeline [FLAGS]"
  ""
  "List the models, then the flags of the pipeline:"
  "  uv run --extra train python -m src.train --help"
  "  uv run --extra train python -m src.train MODEL pipeline --help"
  ""
  "Example:"
  "  mise run train:start -- voxcpm_1_5 --run-name first-run"
  ""
  "Exit codes: the code of the pipeline once it ends. Before that: 1 when"
  "training runs already, no GPU is found, or the start fails; 2 when this"
  "host cannot run in the background; 127 when uv, nvidia-smi, or setsid is"
  "missing; 130 or 143 when a signal stops the follow."
)

main() {
  local root_folder
  local python_path
  local module
  local model

  case "${1:-}" in
    -h | --help)
      printf '%s\n' "${TRAIN_USAGE_LINES[@]}"
      return 0
      ;;
    *) ;;
  esac
  module="$(select_process_module "${TRAIN_PROCESS_NAME}")"
  model="${1-}"
  assert_background_supported "${TRAIN_PROCESS_NAME}" \
    uv run --extra "${TRAIN_EXTRA}" python -m "${module}" "${model:-MODEL}" "${TRAIN_COMMAND}"
  root_folder="$(get_root_folder)"
  assert_process_stopped "${root_folder}" "${TRAIN_PROCESS_NAME}"
  assert_cuda_available
  sync_uv_extra "${root_folder}" "${TRAIN_EXTRA}"
  python_path="$(build_python_path "${root_folder}")"
  # Forked loader workers deadlock on tokenizers threads, so turn them off.
  export TOKENIZERS_PARALLELISM=false
  spawn_background_process "${root_folder}" "${TRAIN_PROCESS_NAME}" \
    "${python_path}" -m "${module}" "${model}" "${TRAIN_COMMAND}" "${@:2}"
  # Pass $! so the follow can return the exit status of the pipeline.
  follow_process_log "${root_folder}" "${TRAIN_PROCESS_NAME}" "$!"
}

main "$@"

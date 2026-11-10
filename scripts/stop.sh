#!/usr/bin/env bash
# Stop the background dataset or training process of this repository.
# Runtime: Bash 3.2+, macOS and Linux.

set -euo pipefail

# shellcheck source=scripts/lib/environment.sh
source "$(dirname -- "${BASH_SOURCE[0]}")/lib/environment.sh"
LIBRARY_FOLDER="$(get_scripts_folder)/lib"
readonly LIBRARY_FOLDER
# shellcheck source=scripts/lib/process.sh
source "${LIBRARY_FOLDER}/process.sh"

print_stop_usage() {
  local status="$1"
  local stream=1

  ((status == 0)) || stream=2
  printf '%s\n' \
    "Usage: bash scripts/stop.sh dataset|train" \
    "" \
    "Send TERM to the process, then KILL to its process group after" \
    "${TRAIN_STOP_WAIT_SECONDS} seconds for training, which writes a checkpoint first, or" \
    "${DATASET_STOP_WAIT_SECONDS} seconds for the dataset." \
    "" \
    "Example:" \
    "  mise run dataset:stop" \
    "" \
    "Exit codes:" \
    "  0  no process remains" \
    "  1  the process survived KILL" \
    "  2  usage error" >&"${stream}"
  exit "${status}"
}

stop_named_process() {
  local root_folder

  root_folder="$(get_root_folder)"
  print_diagnostic "[stop] Stopping $1"
  stop_owned_process "${root_folder}" "$1"
  print_diagnostic "[stop] $1 stopped"
}

main() {
  local name

  name="$(parse_process_argument "$@")"
  case "${name}" in
    --help) print_stop_usage 0 ;;
    "") print_stop_usage 2 ;;
    *) stop_named_process "${name}" ;;
  esac
}

main "$@"

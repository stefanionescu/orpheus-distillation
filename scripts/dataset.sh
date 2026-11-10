#!/usr/bin/env bash
# Start the dataset command in the background and follow its log.
# Runtime: Bash 3.2+, Linux.

set -euo pipefail

# shellcheck source=scripts/lib/environment.sh
source "$(dirname -- "${BASH_SOURCE[0]}")/lib/environment.sh"
LIBRARY_FOLDER="$(get_scripts_folder)/lib"
readonly LIBRARY_FOLDER
# shellcheck source=scripts/lib/uv.sh
source "${LIBRARY_FOLDER}/uv.sh"
# shellcheck source=scripts/lib/follow.sh
source "${LIBRARY_FOLDER}/follow.sh"

readonly DATASET_PROCESS_NAME="dataset"
readonly DATASET_EXTRA="dataset"
readonly DATASET_USAGE_LINES=(
  "Usage: mise run dataset:start -- [DATASET_FLAGS]"
  ""
  "Start the dataset command in the background and follow its log."
  "Control+C stops the follow. mise run dataset:stop stops generation."
  "The command runs without a terminal, so a run that cleans an earlier"
  "output folder needs --yes. Background runs need Linux; on macOS run in"
  "the foreground:"
  "  uv run --extra dataset python -m src.dataset [DATASET_FLAGS]"
  ""
  "List the flags:"
  "  uv run --extra dataset python -m src.dataset --help"
  ""
  "Environment: ORPHEUS_SERVER_URL, ORPHEUS_API_KEY, and HF_TOKEN for --publish."
  ""
  "Example:"
  "  mise run dataset:start -- --voice female --max-prompts 10 --yes"
  ""
  "Exit codes: the code of the dataset command once it ends, which is 0 on"
  "success, 1 on a failure, and 2 on a usage error. Before that: 1 when"
  "generation runs already, or the sync or the start fails; 2 when this"
  "host cannot run in the background; 127 when uv or setsid is missing;"
  "130 or 143 when a signal stops the follow."
)

main() {
  local root_folder
  local python_path
  local module

  case "${1:-}" in
    -h | --help)
      printf '%s\n' "${DATASET_USAGE_LINES[@]}"
      return 0
      ;;
    *) ;;
  esac
  module="$(select_process_module "${DATASET_PROCESS_NAME}")"
  assert_background_supported "${DATASET_PROCESS_NAME}" \
    uv run --extra "${DATASET_EXTRA}" python -m "${module}"
  root_folder="$(get_root_folder)"
  python_path="$(build_python_path "${root_folder}")"
  assert_process_stopped "${root_folder}" "${DATASET_PROCESS_NAME}"
  sync_uv_extra "${root_folder}" "${DATASET_EXTRA}"
  spawn_background_process "${root_folder}" "${DATASET_PROCESS_NAME}" \
    "${python_path}" -m "${module}" "$@"
  # Pass $! so the follow can return the exit status of the dataset command.
  follow_process_log "${root_folder}" "${DATASET_PROCESS_NAME}" "$!"
}

main "$@"

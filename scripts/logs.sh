#!/usr/bin/env bash
# Print and follow the log of the background dataset or training process.
# Runtime: Bash 3.2+, macOS and Linux.

set -euo pipefail

# shellcheck source=scripts/lib/environment.sh
source "$(dirname -- "${BASH_SOURCE[0]}")/lib/environment.sh"
LIBRARY_FOLDER="$(get_scripts_folder)/lib"
readonly LIBRARY_FOLDER
# shellcheck source=scripts/lib/follow.sh
source "${LIBRARY_FOLDER}/follow.sh"

print_logs_usage() {
  local status="$1"
  local stream=1

  ((status == 0)) || stream=2
  printf '%s\n' \
    "Usage: bash scripts/logs.sh dataset|train" \
    "" \
    "Print logs/NAME.log and follow it while the process runs. Control+C" \
    "stops the follow, not the process." \
    "" \
    "Example:" \
    "  mise run train:logs" \
    "" \
    "Exit codes:" \
    "  0         the process is not running or has ended" \
    "  1         no log exists" \
    "  2         usage error" \
    "  130, 143  Control+C or TERM stopped the follow" >&"${stream}"
  exit "${status}"
}

main() {
  local name
  local root_folder

  name="$(parse_process_argument "$@")"
  root_folder="$(get_root_folder)"
  case "${name}" in
    --help) print_logs_usage 0 ;;
    "") print_logs_usage 2 ;;
    *) follow_process_log "${root_folder}" "${name}" ;;
  esac
}

main "$@"

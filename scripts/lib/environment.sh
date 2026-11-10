#!/usr/bin/env bash
# Give the entry points the repository folders and the host check.
# Runtime: Bash 3.2+, macOS and Linux.

# shellcheck source=scripts/lib/print.sh
source "$(dirname -- "${BASH_SOURCE[0]}")/print.sh"

# Resolve the folders once at source time, so a later cd cannot move them.
_SCRIPTS_FOLDER="$(CDPATH='' cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
readonly _SCRIPTS_FOLDER
_ROOT_FOLDER="$(CDPATH='' cd -- "${_SCRIPTS_FOLDER}/.." && pwd -P)"
readonly _ROOT_FOLDER

get_scripts_folder() {
  printf '%s\n' "${_SCRIPTS_FOLDER}"
}

get_root_folder() {
  printf '%s\n' "${_ROOT_FOLDER}"
}

# assert_background_supported - Return 2 off Linux. The arguments after the name
# form the foreground command that the message suggests.
assert_background_supported() {
  local name="$1"
  local system_name

  shift
  system_name="$(uname -s)" || return 1
  if [[ ${system_name} == Linux ]]; then
    return 0
  fi
  print_diagnostic "[${name}] Background runs need Linux and setsid; this host runs ${system_name}"
  print_diagnostic "[${name}] Run the command in the foreground instead: $* [FLAGS]"
  return 2
}

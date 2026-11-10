#!/usr/bin/env bash
# Write the diagnostics of the scripts to standard error.
# Runtime: Bash 3.2+, macOS and Linux.

print_diagnostic() {
  local message="$*"

  [[ -n ${message} ]] || return 2
  printf '%s\n' "${message}" >&2
  return 0
}

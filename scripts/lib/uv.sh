#!/usr/bin/env bash
# Sync one extra of the locked project into .venv.
# Runtime: Bash 3.2+, macOS and Linux.

# shellcheck source=scripts/lib/print.sh
source "$(dirname -- "${BASH_SOURCE[0]}")/print.sh"

readonly VENV_FOLDER=".venv"

build_python_path() {
  printf '%s/%s/bin/python\n' "$1" "${VENV_FOLDER}"
}

# sync_uv_extra - Sync extra $2 into the .venv of root $1; return 127 without uv.
sync_uv_extra() {
  local extra="$2"
  local python_path
  local status

  if ! command -v uv >/dev/null 2>&1; then
    print_diagnostic "[uv] uv is required; run: mise run setup"
    return 127
  fi
  # --inexact keeps the other extras, so one .venv serves every command.
  (cd -- "$1" && uv sync --frozen --inexact --extra "${extra}") || {
    status=$?
    print_diagnostic "[uv] uv sync --extra ${extra} failed"
    return "${status}"
  }
  python_path="$(build_python_path "$1")" || return 1
  if [[ ! -x ${python_path} ]]; then
    print_diagnostic "[uv] Interpreter missing after sync: ${python_path}"
    return 1
  fi
}

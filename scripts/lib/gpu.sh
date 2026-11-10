#!/usr/bin/env bash
# Fail on a host without a GPU before uv downloads the training stack.
# Runtime: Bash 3.2+, Linux.

# shellcheck source=scripts/lib/print.sh
source "$(dirname -- "${BASH_SOURCE[0]}")/print.sh"

assert_cuda_available() {
  if ! command -v nvidia-smi >/dev/null 2>&1; then
    print_diagnostic "[gpu] nvidia-smi is required"
    return 127
  fi
  if ! nvidia-smi >/dev/null 2>&1; then
    print_diagnostic "[gpu] nvidia-smi found no GPU"
    return 1
  fi
}

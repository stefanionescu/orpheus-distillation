#!/usr/bin/env bash
# Follow the log of a background process while it runs.
# Runtime: Bash 3.2+, macOS and Linux.

# shellcheck source=scripts/lib/process.sh
source "$(dirname -- "${BASH_SOURCE[0]}")/process.sh"

readonly POLL_SECONDS=1

# follow_running_log - Print log $2 until the PID in PID file $1 ends; return 130
# on INT and 143 on TERM.
follow_running_log() {
  local pid_file="$1"
  local tail_pid
  local signal_status=0

  tail -n +1 -F -- "$2" &
  tail_pid=$!
  # The process has its own session, so these signals stop only the follow.
  trap 'signal_status=130' INT
  trap 'signal_status=143' TERM
  while ((signal_status == 0)) && find_running_pid "${pid_file}" >/dev/null; do
    sleep "${POLL_SECONDS}"
  done
  # Wait one more poll so tail prints the last lines of the process.
  ((signal_status != 0)) || sleep "${POLL_SECONDS}"
  trap - INT TERM
  if kill -- "${tail_pid}" 2>/dev/null; then
    # The TERM makes tail exit with 143, so ignore its status.
    wait "${tail_pid}" 2>/dev/null || return "${signal_status}"
  fi
  return "${signal_status}"
}

# follow_process_log - Print the log of process $2 under root $1 and follow it
# while the process runs. Pass the PID that this shell spawned as $3 to return
# its exit status instead of 0. Return 1 without a log, 130 on INT, 143 on TERM.
follow_process_log() {
  local name="$2"
  local child_pid="${3:-}"
  local pid_file
  local log_file
  local status=0

  pid_file="$(build_process_path "$1" "${name}" pid)" || return 1
  log_file="$(build_process_path "$1" "${name}" log)" || return 1
  if [[ ! -f ${log_file} ]]; then
    print_diagnostic "[${name}] No log file at ${log_file}"
    return 1
  fi
  if find_running_pid "${pid_file}" >/dev/null; then
    follow_running_log "${pid_file}" "${log_file}" || status=$?
  else
    tail -n +1 -- "${log_file}" || return 1
  fi
  if ((status != 0)); then
    print_diagnostic "[${name}] Stopped following; the process keeps running"
    return "${status}"
  fi
  if [[ -z ${child_pid} ]]; then
    print_diagnostic "[${name}] Not running; log: ${log_file}"
    return 0
  fi
  # The child has ended, so wait returns the status that bash kept for it.
  wait "${child_pid}" || status=$?
  print_diagnostic "[${name}] Exited with status ${status}; log: ${log_file}"
  return "${status}"
}

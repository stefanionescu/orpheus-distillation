#!/usr/bin/env bash
# Stop a process group: TERM to its leader, then KILL to the whole group.
# Runtime: Bash 3.2+, macOS and Linux.

# shellcheck source=scripts/lib/print.sh
source "$(dirname -- "${BASH_SOURCE[0]}")/print.sh"

# The dataset stops within seconds. Training first finishes its step and then
# writes a checkpoint, which takes minutes on a slow disk.
readonly DATASET_STOP_WAIT_SECONDS=10
readonly TRAIN_STOP_WAIT_SECONDS=120

# select_stop_wait - Print the seconds between TERM and KILL for process $1.
select_stop_wait() {
  case "$1" in
    dataset) printf '%s\n' "${DATASET_STOP_WAIT_SECONDS}" ;;
    train) printf '%s\n' "${TRAIN_STOP_WAIT_SECONDS}" ;;
    *) return 2 ;;
  esac
}

select_process_module() {
  case "$1" in
    dataset) printf '%s\n' src.dataset ;;
    train) printf '%s\n' src.train ;;
    *) return 2 ;;
  esac
}

# is_process_command - Return 1 when PID $2 runs a command other than process
# $1, as when a reboot gives the PID of an ended run to a new process.
is_process_command() {
  local module
  local command_line

  module="$(select_process_module "$1")" || return 2
  command_line="$(ps -o args= -p "$2")" || return 1
  [[ ${command_line} == *"${module}"* ]]
}

# wait_for_exit - Return 1 when PID $1 still runs after $2 seconds.
wait_for_exit() {
  local attempt

  for ((attempt = 0; attempt < $2; attempt++)); do
    kill -0 -- "$1" 2>/dev/null || return 0
    sleep 1
  done
  ! kill -0 -- "$1" 2>/dev/null
}

# stop_process_group - Send TERM to PID $2, then KILL to its group after $3
# seconds; return 1 when the PID survives KILL.
stop_process_group() {
  local name="$1"
  local pid="$2"

  # TERM goes to the leader alone: loader workers that get their own TERM
  # exit early, and training then fails before it writes its checkpoint.
  print_diagnostic "[${name}] Sending TERM to process ${pid}"
  kill -s TERM -- "${pid}" 2>/dev/null || print_diagnostic "[${name}] TERM did not reach ${pid}"
  wait_for_exit "${pid}" "$3" && return 0
  print_diagnostic "[${name}] Sending KILL to process group ${pid}"
  if ! kill -s KILL -- "-${pid}" 2>/dev/null; then
    # Before setsid runs, the PID leads no group, so KILL the PID alone.
    kill -s KILL -- "${pid}" 2>/dev/null || print_diagnostic "[${name}] KILL did not reach ${pid}"
  fi
  wait_for_exit "${pid}" 1
}

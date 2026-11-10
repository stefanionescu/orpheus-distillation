#!/usr/bin/env bash
# Start, find, and stop the background processes and their PID files.
# Runtime: Bash 3.2+, Linux for the start, macOS and Linux for the rest.

# shellcheck source=scripts/lib/print.sh
source "$(dirname -- "${BASH_SOURCE[0]}")/print.sh"
# shellcheck source=scripts/lib/stop.sh
source "$(dirname -- "${BASH_SOURCE[0]}")/stop.sh"

readonly PID_FOLDER=".run"
readonly LOGS_FOLDER="logs"

# parse_process_argument - Print the process name or --help; print nothing for a
# usage error.
parse_process_argument() {
  (($# == 1)) || return 0
  case "$1" in
    dataset | train) printf '%s\n' "$1" ;;
    -h | --help) printf '%s\n' "--help" ;;
    *) ;;
  esac
}

# build_process_path - Print the $3 path, pid or log, of process $2 under root $1.
build_process_path() {
  case "$3" in
    pid) printf '%s/%s/%s.pid\n' "$1" "${PID_FOLDER}" "$2" ;;
    log) printf '%s/%s/%s.log\n' "$1" "${LOGS_FOLDER}" "$2" ;;
    *) return 2 ;;
  esac
}

# find_running_pid - Print the PID in PID file $1 while it runs; return 1 otherwise.
find_running_pid() {
  local pid_file="$1"
  local pid

  [[ -f ${pid_file} ]] || return 1
  IFS= read -r pid <"${pid_file}" || return 1
  [[ ${pid} =~ ^[1-9][0-9]*$ ]] || return 1
  kill -0 -- "${pid}" 2>/dev/null || return 1
  printf '%s\n' "${pid}"
}

# write_pid - Replace the PID file atomically, so a reader never sees half a PID.
write_pid() {
  local pid_file="$1"
  local pid="$2"
  local temporary_file

  temporary_file="$(mktemp "${pid_file}.XXXXXX")" || return 1
  trap 'rm -f -- "${temporary_file}"; trap - RETURN' RETURN
  printf '%s\n' "${pid}" >"${temporary_file}" || return 1
  mv -- "${temporary_file}" "${pid_file}" || return 1
}

# assert_process_stopped - Return 1 while process $2 under root $1 runs; remove
# the PID file of an ended process.
assert_process_stopped() {
  local name="$2"
  local pid_file
  local pid

  pid_file="$(build_process_path "$1" "${name}" pid)" || return 1
  if pid="$(find_running_pid "${pid_file}")"; then
    print_diagnostic "[${name}] Already running with PID ${pid}; stop it with: mise run ${name}:stop"
    return 1
  fi
  [[ -e ${pid_file} ]] || return 0
  rm -f -- "${pid_file}" || return 1
  print_diagnostic "[${name}] Removed stale PID file ${pid_file}"
}

# spawn_background_process - Run the command after root $1 and name $2 in a new
# session and write its PID file; return 2 for an unknown name, 127 without setsid.
spawn_background_process() {
  local root_folder="$1"
  local name="$2"
  local wait_seconds
  local pid_file
  local log_file
  local pid

  shift 2
  wait_seconds="$(select_stop_wait "${name}")" || return 2
  if ! command -v setsid >/dev/null 2>&1; then
    print_diagnostic "[${name}] setsid is required to start a background run"
    return 127
  fi
  pid_file="$(build_process_path "${root_folder}" "${name}" pid)" || return 1
  log_file="$(build_process_path "${root_folder}" "${name}" log)" || return 1
  mkdir -p -- "${pid_file%/*}" "${log_file%/*}" || return 1
  : >"${log_file}" || return 1
  # A new session keeps Control+C on the follow away from the command and lets
  # a stop KILL every process that the command forks.
  (
    cd -- "${root_folder}" || exit 1
    export PYTHONUNBUFFERED=1
    exec setsid nohup "$@" </dev/null >>"${log_file}" 2>&1
  ) &
  pid=$!
  write_pid "${pid_file}" "${pid}" || {
    print_diagnostic "[${name}] Failed to write the PID file of ${pid}; stopping it"
    stop_process_group "${name}" "${pid}" "${wait_seconds}"
    return 1
  }
  print_diagnostic "[${name}] Started with PID ${pid}; log: ${log_file}; stop: mise run ${name}:stop"
}

# stop_owned_process - Stop process $2 under root $1 and remove its PID file;
# return 1 when it survives KILL, 2 for an unknown name.
stop_owned_process() {
  local name="$2"
  local wait_seconds
  local pid_file
  local pid

  wait_seconds="$(select_stop_wait "${name}")" || return 2
  pid_file="$(build_process_path "$1" "${name}" pid)" || return 1
  if ! pid="$(find_running_pid "${pid_file}")"; then
    rm -f -- "${pid_file}" || return 1
    print_diagnostic "[${name}] No running process"
    return 0
  fi
  if ! is_process_command "${name}" "${pid}"; then
    rm -f -- "${pid_file}" || return 1
    print_diagnostic "[${name}] Removed stale PID file ${pid_file}: PID ${pid} runs another command"
    return 0
  fi
  if ! stop_process_group "${name}" "${pid}" "${wait_seconds}"; then
    print_diagnostic "[${name}] Failed to stop process ${pid}"
    return 1
  fi
  rm -f -- "${pid_file}" || return 1
  print_diagnostic "[${name}] Stopped process ${pid}"
}

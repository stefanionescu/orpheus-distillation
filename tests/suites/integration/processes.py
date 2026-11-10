"""Process groups that stand in for a background run, and bash calls of the run management libraries.

Each process starts from a fixed command line and gets the values that vary through its environment or stdin, so no
test builds a command line.
"""

from __future__ import annotations

import os
import sys
import shlex
from typing import TYPE_CHECKING
from pathlib import Path
import contextlib
import subprocess

if TYPE_CHECKING:
    from collections.abc import Sequence, Generator

LIBRARY_FOLDER = Path(__file__).resolve().parents[3] / "scripts" / "lib"
"""The shell libraries that the background tasks source."""

STOP_TIMEOUT_SECONDS = 15
"""How long a test waits for a stop, well past the libraries' poll interval."""

SETSID_STAND_IN = """#!{interpreter}
import os
import sys

os.setsid()
os.execvp(sys.argv[1], sys.argv[1:])
"""
"""A setsid command for macOS, which has none. It starts a session and runs its arguments in place, as util-linux
setsid does for a process that leads no group."""


def _start_sleeper(process_group: int, command_title: str, *, is_term_ignored: bool) -> subprocess.Popen[str]:
    environment = {
        **os.environ,
        "IGNORED_SIGNAL": "TERM" if is_term_ignored else "",
        "COMMAND_TITLE": command_title,
    }
    # The sleeper prints a line once its trap is in place, so a test signals it only after that. An ignored signal
    # stays ignored across the exec.
    sleeper = subprocess.Popen(
        [
            "/usr/bin/env",
            "bash",
            "-c",
            '[[ -z ${IGNORED_SIGNAL} ]] || trap "" TERM; echo ready; exec -a "${COMMAND_TITLE}" sleep 60',
        ],
        stdout=subprocess.PIPE,
        text=True,
        env=environment,
        process_group=process_group,
    )
    if sleeper.stdout is not None:
        sleeper.stdout.readline()
    return sleeper


def _end_sleeper(sleeper: subprocess.Popen[str]) -> None:
    if sleeper.poll() is None:
        sleeper.kill()
    sleeper.wait()
    if sleeper.stdout is not None:
        sleeper.stdout.close()


@contextlib.contextmanager
def start_process_group(
    command_title: str, *, is_term_ignored: bool
) -> Generator[tuple[subprocess.Popen[str], subprocess.Popen[str]]]:
    """Start a group leader and a second process in its group, like a training run and its loader worker.

    The test process is the parent of both, so a test that waits for one reaps it, and a stop sees it end.

    Args:
        command_title: The first word of the leader's command line, such as `python -m src.dataset`.
        is_term_ignored: Whether the leader ignores TERM, like a run that outlasts a stop's wait.

    Yields:
        The leader and the second process; exit sends KILL to each one still running.

    """
    leader = _start_sleeper(0, command_title, is_term_ignored=is_term_ignored)
    try:
        member = _start_sleeper(leader.pid, "sleep", is_term_ignored=False)
        try:
            yield leader, member
        finally:
            _end_sleeper(member)
    finally:
        _end_sleeper(leader)


def write_pid_file(root_folder: Path, name: str, pid: int) -> Path:
    """Write a background run's PID file, as a start does.

    Args:
        root_folder: The run's repository root.
        name: The process name, dataset or train.
        pid: The PID to record.

    Returns:
        The PID file.

    """
    pid_path = root_folder / ".run" / f"{name}.pid"
    pid_path.parent.mkdir(parents=True, exist_ok=True)
    pid_path.write_text(f"{pid}\n", encoding="utf-8")
    return pid_path


def write_run_log(root_folder: Path, name: str) -> Path:
    """Write a background run's log with one line, as a start leaves it.

    Args:
        root_folder: The run's repository root.
        name: The process name, dataset or train.

    Returns:
        The log file.

    """
    log_path = root_folder / "logs" / f"{name}.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text("Started\n", encoding="utf-8")
    return log_path


def run_process_to_end() -> int:
    """Run a process until it ends, like a run that crashed and left its PID file.

    Returns:
        The PID of the ended process.

    """
    ended = subprocess.Popen(["/usr/bin/env", "true"])
    ended.wait()
    return ended.pid


def start_polling_follow(root_folder: Path, name: str) -> subprocess.Popen[str]:
    """Start a follow of a running process's log, and return once it polls the process with its traps in place.

    The follow runs with bash tracing on stderr; its first `sleep` trace comes from the poll loop, after the traps.

    Args:
        root_folder: The run's repository root.
        name: The process name, dataset or train.

    Returns:
        The bash process that follows the log, with piped stdout and stderr.

    """
    follower = start_library_script("follow.sh", ["set -x", shlex.join(["follow_process_log", str(root_folder), name])])
    if follower.stderr is not None:
        for line in follower.stderr:
            if line.startswith("+ sleep"):
                break
    return follower


def write_setsid_stand_in(bin_folder: Path) -> str:
    """Write the setsid stand-in into a folder, so a background start works on any host.

    Args:
        bin_folder: Where the stand-in goes; created when missing.

    Returns:
        The bash command that puts the folder first on the shell's search path.

    """
    bin_folder.mkdir(parents=True, exist_ok=True)
    stand_in_path = bin_folder / "setsid"
    stand_in_path.write_text(SETSID_STAND_IN.format(interpreter=sys.executable), encoding="utf-8")
    stand_in_path.chmod(0o700)
    return f'PATH={shlex.quote(str(bin_folder))}:"${{PATH}}"'


def start_library_script(library_name: str, commands: Sequence[str]) -> subprocess.Popen[str]:
    """Start bash with a scripts library sourced, and run commands in that shell.

    Args:
        library_name: The library file name in the scripts library folder.
        commands: Bash commands, one per line; a test quotes their values with `shlex`.

    Returns:
        The bash process, with the last command's exit status and piped stdout and stderr.

    """
    script = "\n".join([f"source {shlex.quote(str(LIBRARY_FOLDER / library_name))}", *commands, ""])
    # The script fits in the pipe buffer, so the write finishes before bash starts to read.
    script_reader, script_writer = os.pipe()
    with os.fdopen(script_writer, "w", encoding="utf-8") as script_stream:
        script_stream.write(script)
    try:
        return subprocess.Popen(
            ["/usr/bin/env", "bash", "-s"],
            stdin=script_reader,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    finally:
        os.close(script_reader)


def start_library_call(library_name: str, arguments: Sequence[str]) -> subprocess.Popen[str]:
    """Start bash with a scripts library sourced, and call one of its functions.

    Args:
        library_name: The library file name in the scripts library folder.
        arguments: The function and its arguments.

    Returns:
        The bash process, with piped stdout and stderr.

    """
    return start_library_script(library_name, [shlex.join(arguments)])

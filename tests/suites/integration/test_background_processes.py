"""The shell libraries start, follow, and stop a background run through its PID file and its log."""

from __future__ import annotations

import shlex
import signal
from typing import TYPE_CHECKING

import pytest

from src.dataset.cli.arguments import EXIT_SIGNAL_BASE
from tests.suites.integration.processes import (
    STOP_TIMEOUT_SECONDS,
    write_run_log,
    write_pid_file,
    run_process_to_end,
    start_library_call,
    start_process_group,
    start_library_script,
    start_polling_follow,
    write_setsid_stand_in,
)

if TYPE_CHECKING:
    from pathlib import Path

ESCALATION_WAIT_SECONDS = 1
"""The wait after TERM when a test drives a stop straight to KILL."""

FAILED_RUN_STATUS = 3
"""A run exit status that no library function returns itself."""

DATASET_COMMAND_TITLE = "python -m src.dataset"
"""The start of a dataset run's command line, which a stop checks before it signals the recorded PID."""

RUN_SCRIPT = f'pwd -P; echo "$$"; echo "${{PYTHONUNBUFFERED-}}"; exit {FAILED_RUN_STATUS}'
"""A run that prints its folder, its PID, and its output buffering setting, then fails."""


def test_stop_terms_leader_only(tmp_path: Path) -> None:
    """A stop sends TERM to the recorded process alone; the rest of its group gets no signal.

    Args:
        tmp_path: The run's repository root.

    """
    with start_process_group(DATASET_COMMAND_TITLE, is_term_ignored=False) as (leader, member):
        pid_path = write_pid_file(tmp_path, "dataset", leader.pid)
        stopper = start_library_call("process.sh", ["stop_owned_process", str(tmp_path), "dataset"])
        leader.wait(timeout=STOP_TIMEOUT_SECONDS)
        stopper.communicate(timeout=STOP_TIMEOUT_SECONDS)
        member_status = member.poll()

    assert stopper.returncode == 0
    assert leader.returncode == -signal.SIGTERM
    assert member_status is None
    assert not pid_path.exists()


def test_group_killed_after_wait() -> None:
    """A leader that outlives the wait after TERM gets KILL with its group, which never got TERM."""
    with start_process_group("sleep", is_term_ignored=True) as (leader, member):
        stopper = start_library_call(
            "stop.sh", ["stop_process_group", "train", str(leader.pid), str(ESCALATION_WAIT_SECONDS)]
        )
        leader.wait(timeout=STOP_TIMEOUT_SECONDS)
        member.wait(timeout=STOP_TIMEOUT_SECONDS)
        stopper.communicate(timeout=STOP_TIMEOUT_SECONDS)

    assert stopper.returncode == 0
    assert (leader.returncode, member.returncode) == (-signal.SIGKILL, -signal.SIGKILL)


def test_reused_pid_not_signalled(tmp_path: Path) -> None:
    """A stop removes a PID file whose PID now runs another command, as after a reboot, and leaves that command alone.

    Args:
        tmp_path: The run's repository root.

    """
    with start_process_group("sleep", is_term_ignored=False) as (other, member):
        pid_path = write_pid_file(tmp_path, "dataset", other.pid)
        stopper = start_library_call("process.sh", ["stop_owned_process", str(tmp_path), "dataset"])
        stopper.communicate(timeout=STOP_TIMEOUT_SECONDS)
        statuses = (other.poll(), member.poll())

    assert stopper.returncode == 0
    assert statuses == (None, None)
    assert not pid_path.exists()


def test_stop_removes_stale_pid(tmp_path: Path) -> None:
    """A stop whose PID file names an ended process removes the file and exits 0, because nothing runs.

    Args:
        tmp_path: The run's repository root.

    """
    pid_path = write_pid_file(tmp_path, "dataset", run_process_to_end())

    stopper = start_library_call("process.sh", ["stop_owned_process", str(tmp_path), "dataset"])
    stopper.communicate(timeout=STOP_TIMEOUT_SECONDS)

    assert stopper.returncode == 0
    assert not pid_path.exists()


def test_running_process_blocks_start(tmp_path: Path) -> None:
    """A start refuses with status 1 while the recorded process runs, and keeps the PID file and the process.

    Args:
        tmp_path: The run's repository root.

    """
    with start_process_group(DATASET_COMMAND_TITLE, is_term_ignored=False) as (leader, _):
        pid_path = write_pid_file(tmp_path, "dataset", leader.pid)
        checker = start_library_call("process.sh", ["assert_process_stopped", str(tmp_path), "dataset"])
        checker.communicate(timeout=STOP_TIMEOUT_SECONDS)
        leader_status = leader.poll()

    assert checker.returncode == 1
    assert pid_path.read_text(encoding="utf-8") == f"{leader.pid}\n"
    assert leader_status is None


def test_start_removes_stale_pid(tmp_path: Path) -> None:
    """A start after a crashed run removes the ended process's PID file and goes on.

    Args:
        tmp_path: The run's repository root.

    """
    pid_path = write_pid_file(tmp_path, "dataset", run_process_to_end())

    checker = start_library_call("process.sh", ["assert_process_stopped", str(tmp_path), "dataset"])
    checker.communicate(timeout=STOP_TIMEOUT_SECONDS)

    assert checker.returncode == 0
    assert not pid_path.exists()


@pytest.mark.parametrize("signal_number", [signal.SIGINT, signal.SIGTERM], ids=["interrupt", "terminate"])
def test_follow_signal_spares_run(tmp_path: Path, signal_number: signal.Signals) -> None:
    """A signal to the follow of a running process ends the follow with 128 plus its number; the run keeps going.

    Args:
        tmp_path: The run's repository root.
        signal_number: The signal that Control+C or a TERM sends to the follow.

    """
    with start_process_group(DATASET_COMMAND_TITLE, is_term_ignored=False) as (leader, _):
        write_pid_file(tmp_path, "dataset", leader.pid)
        write_run_log(tmp_path, "dataset")
        follower = start_polling_follow(tmp_path, "dataset")
        follower.send_signal(signal_number)
        follower.communicate(timeout=STOP_TIMEOUT_SECONDS)
        leader_status = leader.poll()

    assert follower.returncode == EXIT_SIGNAL_BASE + signal_number
    assert leader_status is None


def test_follow_returns_run_status(tmp_path: Path) -> None:
    """A start runs its command unbuffered in the root folder; the follow prints its log and exits with its status.

    The start also writes the command's own PID to the PID file, which a stop signals.

    Args:
        tmp_path: The run's repository root.

    """
    root_folder = str(tmp_path)
    commands = [
        write_setsid_stand_in(tmp_path / "bin"),
        "unset PYTHONUNBUFFERED",
        shlex.join(["spawn_background_process", root_folder, "dataset", "sh", "-c", RUN_SCRIPT]),
        f'follow_process_log {shlex.quote(root_folder)} dataset "$!"',
    ]

    starter = start_library_script("follow.sh", commands)
    output, _ = starter.communicate(timeout=STOP_TIMEOUT_SECONDS)

    run_folder, run_pid, unbuffered = output.splitlines()
    assert starter.returncode == FAILED_RUN_STATUS
    assert run_folder == str(tmp_path.resolve())
    assert (tmp_path / ".run" / "dataset.pid").read_text(encoding="utf-8") == f"{run_pid}\n"
    assert unbuffered == "1"

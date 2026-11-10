"""The training environment reader reads the Hub token and the torchrun layout once."""

from __future__ import annotations

import pytest

from schemas.settings import TrainEnvironment
from src.train.settings import read_environment
from tests.harness.environment import HF_TOKEN

WORLD_SIZE = 4
LOCAL_RANK = 3


@pytest.mark.parametrize("value", [None, "", "  "], ids=["unset", "empty", "spaces"])
def test_blank_means_one_process(monkeypatch: pytest.MonkeyPatch, value: str | None) -> None:
    """Unset or empty variables, as a copied environment example leaves them, mean one process without a token.

    Args:
        monkeypatch: Sets the variables.
        value: Each variable's text, or None to leave it unset.

    """
    if value is not None:
        for name in ("HF_TOKEN", "WORLD_SIZE", "LOCAL_RANK"):
            monkeypatch.setenv(name, value)

    assert read_environment() == TrainEnvironment(hf_token=None, world_size=1, local_rank=0)


def test_variables_read_as_given(monkeypatch: pytest.MonkeyPatch) -> None:
    """The token and both torchrun counts come from their variables as given.

    Args:
        monkeypatch: Sets the variables.

    """
    monkeypatch.setenv("HF_TOKEN", HF_TOKEN)
    monkeypatch.setenv("WORLD_SIZE", str(WORLD_SIZE))
    monkeypatch.setenv("LOCAL_RANK", str(LOCAL_RANK))

    assert read_environment() == TrainEnvironment(hf_token=HF_TOKEN, world_size=WORLD_SIZE, local_rank=LOCAL_RANK)


@pytest.mark.parametrize(
    ("name", "value"),
    [("WORLD_SIZE", "0"), ("WORLD_SIZE", "two"), ("LOCAL_RANK", "-1")],
    ids=["world-size-below-one", "world-size-not-a-number", "local-rank-negative"],
)
def test_invalid_count_raises(monkeypatch: pytest.MonkeyPatch, name: str, value: str) -> None:
    """An invalid count stops the command with an error that names the variable to fix.

    Args:
        monkeypatch: Sets the variable.
        name: The variable to set.
        value: The invalid value.

    """
    monkeypatch.setenv(name, value)

    with pytest.raises(ValueError, match=name):
        read_environment()

"""The flag parsers that every model command shares accept their bounds and reject the values past them."""

from __future__ import annotations

from typing import TYPE_CHECKING
import argparse

import pytest

from src.train.cli import (
    parse_repo,
    parse_fraction,
    parse_run_name,
    parse_positive_int,
    parse_positive_float,
    parse_non_negative_float,
)

if TYPE_CHECKING:
    from collections.abc import Callable


@pytest.mark.parametrize(
    ("parser", "text", "value"),
    [
        (parse_positive_int, "1", 1),
        (parse_positive_float, "1e-4", 1e-4),
        (parse_non_negative_float, "0", 0.0),
        (parse_fraction, "0", 0.0),
        (parse_run_name, "run-1.v2_b", "run-1.v2_b"),
        (parse_repo, "owner-1/model.v2_b", "owner-1/model.v2_b"),
    ],
    ids=[
        "positive-int-one",
        "positive-float-small",
        "non-negative-zero",
        "fraction-zero",
        "run-name-punctuation",
        "repo-id-punctuation",
    ],
)
def test_bound_value_accepted(parser: Callable[[str], object], text: str, value: object) -> None:
    """Each parser accepts the value at its bound and returns it.

    Args:
        parser: The flag parser.
        text: The flag text at the bound.
        value: The parsed value.

    """
    assert parser(text) == value


@pytest.mark.parametrize(
    ("parser", "text"),
    [
        (parse_positive_int, "0"),
        (parse_positive_int, "1.5"),
        (parse_positive_float, "0"),
        (parse_non_negative_float, "-0.5"),
        (parse_fraction, "1"),
        (parse_fraction, "-0.1"),
        (parse_run_name, ".."),
        (parse_run_name, "runs/../escape"),
        (parse_repo, "model"),
        (parse_repo, "owner/model/extra"),
    ],
    ids=[
        "positive-int-zero",
        "positive-int-fraction",
        "positive-float-zero",
        "non-negative-negative",
        "fraction-one",
        "fraction-negative",
        "run-name-parent",
        "run-name-path",
        "repo-id-without-owner",
        "repo-id-nested",
    ],
)
def test_value_past_bound_rejected(parser: Callable[[str], object], text: str) -> None:
    """Each parser rejects the first value past its bound as a usage error.

    Args:
        parser: The flag parser.
        text: The flag text past the bound.

    """
    with pytest.raises(argparse.ArgumentTypeError):
        parser(text)

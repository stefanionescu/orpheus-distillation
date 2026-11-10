"""The topic packages join into the corpus prompts, each prompt once, in reading order."""

from __future__ import annotations

from typing import TYPE_CHECKING
import hashlib

from config.prompts.corpus import PROMPTS, MULTI_SENTENCE

if TYPE_CHECKING:
    from collections.abc import Sequence

PROMPTS_COUNT = 37_462
PROMPTS_SHA256 = "b2a3ccd539c3c9ebebee0009708ae99f3287b8bbc551c3ea047eacc1c36e1bf9"
MULTI_SENTENCE_COUNT = 2_520
MULTI_SENTENCE_SHA256 = "2abe292a3698392c8848e8fe85b1a6c4750b15e315b27f7c61724d0a1ea8dbc7"


def _hash_prompts(prompts: Sequence[str]) -> str:
    return hashlib.sha256("\n".join(prompts).encode("utf-8")).hexdigest()


def test_prompts_match_snapshot() -> None:
    """The joined prompt list keeps its count and hash, so every corpus edit is deliberate."""
    assert len(PROMPTS) == PROMPTS_COUNT
    assert _hash_prompts(PROMPTS) == PROMPTS_SHA256


def test_multi_sentence_matches_snapshot() -> None:
    """The multi-sentence list keeps its count and hash."""
    assert len(MULTI_SENTENCE) == MULTI_SENTENCE_COUNT
    assert _hash_prompts(MULTI_SENTENCE) == MULTI_SENTENCE_SHA256


def test_prompts_hold_no_repeat() -> None:
    """Each prompt appears once, so no voice reads a corpus line twice."""
    assert len(set(PROMPTS)) == len(PROMPTS)

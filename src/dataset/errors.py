"""Errors that cross module boundaries in the dataset command."""

from __future__ import annotations


class UsageError(Exception):
    """A required flag or environment variable is missing. The command exits with code 2."""


class TtsError(Exception):
    """The Orpheus server rejected or failed a request."""

    def __init__(self, message: str, *, is_retryable: bool = False) -> None:
        """Store the message and the retry flag.

        Args:
            message: What went wrong.
            is_retryable: Whether a new connection can succeed.

        """
        super().__init__(message)
        self.is_retryable = is_retryable


class GenerationError(Exception):
    """A failure that stops the dataset run."""

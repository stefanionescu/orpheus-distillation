"""The text tokenizer of the model."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from collections.abc import Callable

    from transformers import PreTrainedTokenizerFast

MIN_SPLIT_LENGTH = 2
CJK_FIRST = "一"
CJK_LAST = "鿿"
WORD_START = "▁"


# Text in, token ids out, without special tokens.
type TextTokenizer = Callable[[str], list[int]]


class ChineseCharacterTokenizer:
    """Tokenizer that splits each multi-character Chinese entry into one token per character."""

    def __init__(self, base_tokenizer: PreTrainedTokenizerFast) -> None:
        """Store the base tokenizer and collect its multi-character Chinese entries.

        Args:
            base_tokenizer: Hugging Face tokenizer of the checkpoint.

        """
        self.tokenizer = base_tokenizer
        self.multichar_tokens = {
            token
            for token in base_tokenizer.vocab
            if len(token) >= MIN_SPLIT_LENGTH and all(CJK_FIRST <= character <= CJK_LAST for character in token)
        }

    def tokenize(self, text: str, **kwargs: object) -> list[str]:
        """Tokenize a text and split multi-character Chinese tokens into characters.

        Args:
            text: Text to split.
            **kwargs: Options for the base tokenizer.

        Returns:
            The tokens.

        """
        split = cast("Callable[..., list[str]]", self.tokenizer.tokenize)
        processed: list[str] = []
        for token in split(text, **kwargs):
            clean_token = token.replace(WORD_START, "")
            if clean_token in self.multichar_tokens:
                processed.extend(list(clean_token))
            else:
                processed.append(token)
        return processed

    def __call__(self, text: str, **kwargs: object) -> list[int]:
        """Return the token ids of a text, without special tokens.

        Args:
            text: Text to encode.
            **kwargs: Options for the base tokenizer.

        Returns:
            The token ids.

        Raises:
            ValueError: When the base tokenizer fails.

        """
        try:
            result = self.tokenizer.convert_tokens_to_ids(self.tokenize(text, **kwargs))
        except Exception as exc:
            message = f"Tokenization failed: {exc}"
            raise ValueError(message) from exc
        if isinstance(result, int):
            return [result]
        return list(result)

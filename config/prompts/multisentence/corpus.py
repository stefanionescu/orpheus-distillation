"""Prompts of several sentences, in reading order."""

from __future__ import annotations

from config.prompts.multisentence.arts import ARTS
from config.prompts.multisentence.books import BOOKS
from config.prompts.multisentence.careers import CAREERS
from config.prompts.multisentence.chatter import CHATTER
from config.prompts.multisentence.finance import FINANCE
from config.prompts.multisentence.moments import MOMENTS
from config.prompts.multisentence.romance import ROMANCE
from config.prompts.multisentence.worries import WORRIES
from config.prompts.multisentence.feelings import FEELINGS
from config.prompts.multisentence.jealousy import JEALOUSY
from config.prompts.multisentence.mischief import MISCHIEF
from config.prompts.multisentence.opinions import OPINIONS
from config.prompts.multisentence.pleading import PLEADING
from config.prompts.multisentence.athletics import ATHLETICS
from config.prompts.multisentence.outbursts import OUTBURSTS
from config.prompts.multisentence.reflection import REFLECTION
from config.prompts.multisentence.situations import SITUATIONS
from config.prompts.multisentence.frustration import FRUSTRATION
from config.prompts.multisentence.explanations import EXPLANATIONS
from config.prompts.multisentence.conversations import CONVERSATIONS
from config.prompts.multisentence.confrontations import CONFRONTATIONS

MULTI_SENTENCE: list[str] = [
    *ROMANCE,
    *CONFRONTATIONS,
    *JEALOUSY,
    *PLEADING,
    *OUTBURSTS,
    *CAREERS,
    *ARTS,
    *ATHLETICS,
    *BOOKS,
    *FINANCE,
    *OPINIONS,
    *EXPLANATIONS,
    *FEELINGS,
    *WORRIES,
    *SITUATIONS,
    *REFLECTION,
    *MOMENTS,
    *CONVERSATIONS,
    *CHATTER,
    *FRUSTRATION,
    *MISCHIEF,
]

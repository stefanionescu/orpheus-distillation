"""The corpus of the dataset command: its built-in prompts, joined from the topic packages in reading order."""

from __future__ import annotations

from config.prompts.art.corpus import ART
from config.prompts.sad.corpus import SAD
from config.prompts.apps.corpus import APPS
from config.prompts.food.corpus import FOOD
from config.prompts.math.corpus import MATH
from config.prompts.time.corpus import TIME
from config.prompts.angry.corpus import ANGRY
from config.prompts.dates.corpus import DATES
from config.prompts.gamer.corpus import GAMER
from config.prompts.happy.corpus import HAPPY
from config.prompts.hyped.corpus import HYPED
from config.prompts.legal.corpus import LEGAL
from config.prompts.money.corpus import MONEY
from config.prompts.music.corpus import MUSIC
from config.prompts.names.corpus import NAMES
from config.prompts.slang.corpus import SLANG
from config.prompts.tired.corpus import TIRED
from config.prompts.units.corpus import UNITS
from config.prompts.bitchy.corpus import BITCHY
from config.prompts.colors.corpus import COLORS
from config.prompts.emails.corpus import EMAILS
from config.prompts.flirty.corpus import FLIRTY
from config.prompts.sports.corpus import SPORTS
from config.prompts.unique.corpus import UNIQUE_PRONUNCIATIONS
from config.prompts.animals.corpus import ANIMALS
from config.prompts.biology.corpus import BIOLOGY
from config.prompts.cursing.corpus import CURSING
from config.prompts.fashion.corpus import FASHION
from config.prompts.fitness.corpus import FITNESS
from config.prompts.medical.corpus import MEDICAL
from config.prompts.physics.corpus import PHYSICS
from config.prompts.therapy.corpus import THERAPY
from config.prompts.weather.corpus import WEATHER
from config.prompts.confused.corpus import CONFUSED
from config.prompts.dialects.corpus import DIALECTS
from config.prompts.dramatic.corpus import DRAMATIC
from config.prompts.friendly.corpus import FRIENDLY
from config.prompts.grateful.corpus import GRATEFUL
from config.prompts.hesitant.corpus import HESITANT
from config.prompts.immature.corpus import IMMATURE
from config.prompts.politics.corpus import POLITICS
from config.prompts.products.corpus import PRODUCTS
from config.prompts.chemistry.corpus import CHEMISTRY
from config.prompts.defensive.corpus import DEFENSIVE
from config.prompts.household.corpus import HOUSEHOLD
from config.prompts.reactions.corpus import REACTIONS
from config.prompts.religious.corpus import RELIGIOUS
from config.prompts.sarcastic.corpus import SARCASTIC
from config.prompts.spiritual.corpus import SPIRITUAL
from config.prompts.frustrated.corpus import FRUSTRATED
from config.prompts.occupations.corpus import OCCUPATIONS
from config.prompts.phonenumbers.corpus import PHONE_NUMBERS
from config.prompts.abbreviations.corpus import ABBREVIATIONS
from config.prompts.condescending.corpus import CONDESCENDING
from config.prompts.multisentence.corpus import MULTI_SENTENCE

PROMPTS: list[str] = [
    # EMOTIONS & MOODS
    # Positive emotions
    *HAPPY,
    *GRATEFUL,
    *FRIENDLY,
    *FLIRTY,
    # Negative emotions
    *ANGRY,
    *FRUSTRATED,
    *SAD,
    *CONFUSED,
    *HESITANT,
    *TIRED,
    *HYPED,
    # Attitudinal/behavioral emotions
    *CONDESCENDING,
    *DEFENSIVE,
    *BITCHY,
    *IMMATURE,
    *SARCASTIC,
    # Expressive/emotional styles
    *DRAMATIC,
    *RELIGIOUS,
    # TOPICS & DOMAINS
    *OCCUPATIONS,
    *FASHION,
    *LEGAL,
    *WEATHER,
    *ANIMALS,
    *APPS,
    *COLORS,
    *FOOD,
    *HOUSEHOLD,
    *MUSIC,
    *ART,
    *GAMER,
    *PRODUCTS,
    *SPORTS,
    *FITNESS,
    *POLITICS,
    *THERAPY,
    *SPIRITUAL,
    # SCIENCE & TECHNICAL
    *MEDICAL,
    *CHEMISTRY,
    *MATH,
    *BIOLOGY,
    *PHYSICS,
    # NUMBERS & DATA
    *PHONE_NUMBERS,
    *DATES,
    *MONEY,
    *TIME,
    *UNITS,
    # NAMES & PROPER NOUNS
    *NAMES,
    # SPECIAL FORMATS
    *EMAILS,
    *ABBREVIATIONS,
    # SPEECH PATTERNS
    *REACTIONS,
    *SLANG,
    *CURSING,
    *UNIQUE_PRONUNCIATIONS,
    *DIALECTS,
    # MULTI-SENTENCE
    *MULTI_SENTENCE,
]

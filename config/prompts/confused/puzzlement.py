"""Confusion prompts: short expressions by kind, then medium statements and questions."""

from __future__ import annotations

PUZZLEMENT: list[str] = [
    # ULTRA SHORT - VARIED
    "Huh?",
    "What?",
    "Wait.",
    "Hmm?",
    "Sorry?",
    "Pardon?",
    "Come again?",
    "Say what?",
    "Excuse me?",
    "Lost me.",
    "Totally lost.",
    "Brain freeze.",
    "Mind blank.",
    "Drawing blanks.",
    "Zero clue.",
    # SHORT CONFUSION - VARIED STARTERS
    "Okay, you lost me there.",
    "Hold up, that's confusing.",
    "Wait wait wait, back up.",
    "Hang on, start over please.",
    "Whoa, slow down a second.",
    "Right, so what now?",
    "Um, totally not following.",
    "Uh, could you repeat that?",
    "Er, went right over my head.",
    "Hmm, something's not clicking.",
    "See, this is where I get lost.",
    "Yeah, none of that made sense.",
    "Nope, completely baffled here.",
    "Sorry, brain isn't computing.",
    "Help, my brain just crashed.",
    # QUESTIONING UNDERSTANDING
    "Did you just say what I think you said?",
    "Am I missing something obvious here?",
    "Is there context I should know about?",
    "Are we even on the same page?",
    "Was that supposed to make sense?",
    "Should this be clicking for me?",
    "Have I been zoning out or something?",
    "Did I miss a step somewhere?",
    "Is my brain broken or is this actually confusing?",
    "Were you speaking English just now?",
    "Does anyone else understand this?",
    "Can someone translate that into human?",
    "Are you messing with me right now?",
    "Is this some kind of test?",
    "Was there a memo I didn't get?",
    # PROCESSING CONFUSION
    "Brain is buffering, please wait.",
    "Give me a minute to process.",
    "Loading, loading, still loading.",
    "Neurons are not connecting.",
    "Synapses are misfiring here.",
    "Mental gears are grinding.",
    "Thought process just derailed.",
    "Logic circuits are overloaded.",
    "Understanding has left the building.",
    "Comprehension just blue screened.",
    "Mind went completely blank.",
    "Cognitive function is offline.",
    "Processing power at zero.",
    "Error four oh four, understanding not found.",
    "System reboot required.",
    # EXPRESSING BAFFLEMENT
    "Completely and utterly baffled.",
    "Absolutely no idea what's happening.",
    "Totally out of my depth here.",
    "Genuinely have no clue.",
    "Legitimately cannot understand.",
    "Honestly don't get it at all.",
    "Seriously drawing a blank.",
    "Truly mystified by this.",
    "Literally cannot comprehend.",
    "Actually don't understand.",
    "Straight up confused right now.",
    "Flat out don't get it.",
    "Simply cannot follow this.",
    "Just not computing for me.",
    "Really struggling to understand.",
    # SEEKING CLARIFICATION
    "Run that by me again?",
    "Wanna try that in English?",
    "Care to elaborate on that?",
    "Mind explaining from scratch?",
    "Think you could simplify that?",
    "Got a dumbed down version?",
    "Try again, slower this time?",
    "Another way to say that?",
    "Plain English, please?",
    "Pretend I'm five years old.",
    "Break it down for me?",
    "Step by step would help.",
    "From the beginning please.",
    "One more time with feeling?",
    "Layman's terms, if you would.",
    # COMPARING TO CONFUSION
    "Might as well be speaking Martian.",
    "Like reading hieroglyphics honestly.",
    "Feels like I walked into a foreign film.",
    "Hearing words but they mean nothing.",
    "Words going in, nothing sticking.",
    "All I hear is static.",
    "Feels like you're speaking backwards.",
    "Sounds like word salad to me.",
    "May as well be gibberish.",
    "Complete alphabet soup in my head.",
    "Absolute word vomit, sorry.",
    "Sounds like the adults in Peanuts.",
    "Wah wah wah, that's all I got.",
    "You lost me at hello basically.",
    "In one ear, out the other.",
    # SELF-DEPRECATING CONFUSION
    "Clearly missing something here.",
    "Obviously not smart enough for this.",
    "Apparently this is beyond me.",
    "Evidently went over my head.",
    "Guess my brain took the day off.",
    "Seems I'm the only one lost.",
    "Must be having a slow moment.",
    "Probably just me being dense.",
    "Maybe I need more coffee first.",
    "Perhaps my brain needs rebooting.",
    "Think I need a simpler explanation.",
    "Feeling particularly stupid right now.",
    "Intelligence clearly left the chat.",
    "Brain cells on vacation today.",
    "Two plus two not equaling four here.",
    # SITUATIONAL CONFUSION
    "When did this become so complicated?",
    "Where exactly did I lose the plot?",
    "How did we get from A to Z?",
    "Why is this so hard to follow?",
    "What happened to the simple version?",
    "Who decided to make this confusing?",
    "Since when is this how it works?",
    "At what point did this go sideways?",
    "Which part was I supposed to understand?",
    "How many things am I missing here?",
    "Whose idea was this nonsense?",
    "When did everything get so tangled?",
    "Where did the logic go exactly?",
    "Why can't anything be straightforward?",
    "What universe does this make sense in?",
    # MEDIUM - VARIED STARTERS
    "Okay, so you completely lost me about three sentences ago, and I've been nodding pretending to follow ever since.",
    (
        "Honestly, I have absolutely no idea what just happened, but I'm going to pretend I do for now until someone "
        "explains."
    ),
    (
        "Brain officially checked out somewhere around the middle, and now I'm scrambling to catch up with zero "
        "success so far."
    ),
    "Thought I was following along just fine until that last part, and now everything's a jumbled mess in my head.",
    (
        "Pretty sure we skipped about twelve steps between the beginning and here because I'm missing major connecting "
        "pieces somehow."
    ),
    (
        "Feeling like everyone else got the instruction manual, and I'm just winging it with absolutely no guidance "
        "whatsoever."
    ),
    (
        "Started strong with the understanding, but somewhere along the way my brain just completely disconnected from "
        "the conversation entirely."
    ),
    (
        "Words are coming out of your mouth, but they're forming absolutely no coherent pattern in my processing "
        "center right now."
    ),
    (
        "Nodding along doesn't mean understanding is happening, just so we're clear, because I'm totally lost at this "
        "point honestly."
    ),
    (
        "Every new piece of information you add makes this whole thing exponentially more confusing rather than "
        "clearer somehow magically."
    ),
    (
        "Struggling to connect any of these dots because they seem to be in completely different galaxies from each "
        "other right now."
    ),
    (
        "Mind is doing that thing where it refuses to accept new information because the old information isn't making "
        "sense yet."
    ),
    (
        "Getting the distinct feeling I missed something crucial early on that would make everything else actually "
        "make some sense."
    ),
    (
        "Desperately trying to follow, but it's like chasing a train that's already three stations ahead of where I'm "
        "standing now."
    ),
    (
        "Attempting to piece this together, but the puzzle pieces seem to be from entirely different boxes at this "
        "point honestly."
    ),
    # MEDIUM - QUESTIONS
    (
        "Can we rewind to the beginning because somewhere along the way my understanding completely derailed and I "
        "need a fresh start?"
    ),
    (
        "Is there a version of this explanation that exists in simpler terms for people who aren't following at all "
        "like me?"
    ),
    (
        "Would it be possible to go step by step because jumping ahead is causing major gaps in my comprehension right "
        "now?"
    ),
    (
        "How is this supposed to make sense when every explanation just adds more confusion on top of the confusion I "
        "already had?"
    ),
    (
        "Why does it feel like we're having two completely different conversations that occasionally overlap but "
        "mostly just confuse me further?"
    ),
    (
        "What crucial piece of information am I clearly missing that would make this whole thing suddenly click into "
        "place for me?"
    ),
    (
        "Are you intentionally being vague or is this genuinely just going completely over my head for reasons I can't "
        "identify?"
    ),
    (
        "Could someone, anyone at all, please explain this like I'm someone who has absolutely no background knowledge "
        "whatsoever?"
    ),
    (
        "Where exactly did the logic train leave the station without me because I'm still standing on the platform "
        "waiting confused?"
    ),
    (
        "When you say that, what do you actually mean because I can think of at least five interpretations and none "
        "feel right?"
    ),
    "Which part of this am I supposed to understand first before the rest will even have a chance of making sense?",
    "Does this make sense to anyone else here or am I the only one completely lost in this conversation right now?",
    (
        "Should I be taking notes or something because my brain is not retaining any of this information you're "
        "throwing at me?"
    ),
    (
        "Am I supposed to already know something that I clearly don't know because there's a foundation missing in my "
        "understanding here?"
    ),
    (
        "Have we collectively decided that clarity is optional because nothing about this explanation is landing for "
        "me at all currently?"
    ),
]

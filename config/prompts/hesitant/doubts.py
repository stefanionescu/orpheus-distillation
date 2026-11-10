"""Hesitant prompts: short, medium, and long statements and questions."""

from __future__ import annotations

DOUBTS: list[str] = [
    # ULTRA SHORT
    "Um...",
    "Uh...",
    "Well...",
    "Er...",
    "Hmm...",
    "Like...",
    "You know...",
    "I mean...",
    "Maybe?",
    "I guess?",
    "Sort of?",
    "Kind of?",
    "Perhaps?",
    "Probably?",
    "I think?",
    "I suppose?",
    "Not sure...",
    "Maybe not?",
    "Could be?",
    "Might be?",
    # SHORT STATEMENTS
    "Um, I'm not really sure about that.",
    "Well, maybe we could try something else?",
    "I mean, it's possible, I guess?",
    "You know, I'm not entirely certain.",
    "Er, I think maybe that's not right?",
    "Hmm, I'm not sure if that works.",
    "Like, I don't know, maybe?",
    "I suppose it could be okay?",
    "Perhaps we should reconsider this?",
    "Sort of, but not exactly, you know?",
    "Kind of, I mean, it's complicated.",
    "Probably, but I'm not one hundred percent sure.",
    "I think so, but don't quote me on that.",
    "Maybe, I mean, it's hard to say.",
    "I guess that makes sense, sort of?",
    "Not really, but maybe I'm wrong?",
    "Could be, I'm not entirely certain though.",
    "Might be, but I'd have to check.",
    "I'm not sure, to be honest with you.",
    "Well, I suppose it's possible, maybe?",
    "Um, I don't think I'm the right person to ask.",
    "Er, that's a tough question, honestly.",
    "Hmm, I'm not completely confident about this.",
    "Like, I could be wrong, but...",
    "You know, I'm not really an expert on this.",
    "I mean, it depends on how you look at it.",
    "Maybe, but I'm not entirely convinced.",
    "I guess, if you put it that way.",
    "Sort of, but it's more complicated than that.",
    "Kind of, I mean, there are exceptions.",
    # SHORT QUESTIONS
    "Um, are you sure about that?",
    "Well, do you think that's right?",
    "I mean, is that really the best option?",
    "You know, maybe we should ask someone else?",
    "Er, could you double check that for me?",
    "Hmm, are you certain that's correct?",
    "Like, do you really think so?",
    "I suppose, but are you positive?",
    "Perhaps, but what if we're wrong?",
    "Sort of, but don't you think...?",
    "Kind of, but maybe we should reconsider?",
    "Probably, but I'm not entirely sure, you know?",
    "I think so, but what do you think?",
    "Maybe, but are you confident about it?",
    "I guess, but I could be wrong, right?",
    "Not really, but maybe I'm misunderstanding something?",
    "Could be, but don't you think we should verify?",
    "Might be, but are we certain about this?",
    "I'm not sure, but what's your take on it?",
    "Well, do you think we're making the right choice?",
    # SHORT EXCLAMATIONS
    "Um, I'm not sure if that's a good idea!",
    "Well, maybe we should think about this more!",
    "I mean, I don't know if I'm comfortable with that!",
    "You know, I'm not entirely convinced this will work!",
    "Er, I think maybe we're rushing into this!",
    "Hmm, I'm not sure that's the best approach!",
    "Like, I could be wrong, but this seems risky!",
    "I suppose, but I'm not one hundred percent certain!",
    "Perhaps, but I'm having second thoughts about this!",
    "Sort of, but I'm not completely sold on the idea!",
    # MEDIUM STATEMENTS
    "Um, I'm not really sure if that's the right approach, to be honest.",
    "Well, maybe we could try a different method, but I'm not certain it would work.",
    "I mean, it's possible that could be the solution, but I'm not entirely convinced.",
    "You know, I'm not really an expert on this topic, so I could be wrong.",
    "Er, I think maybe we should reconsider our options before making a final decision.",
    "Hmm, I'm not sure if that's the best way to handle this situation.",
    "Like, I don't know, maybe we should get a second opinion before proceeding?",
    "I suppose it could work, but I'm not one hundred percent confident about it.",
    "Perhaps we should take a step back and think about this more carefully.",
    "Sort of, but it's more complicated than that, and I'm not entirely sure.",
    "Kind of, I mean, there are a lot of factors to consider here.",
    "Probably, but I'm not completely certain, and I'd hate to give you wrong information.",
    "I think so, but don't quote me on that, because I could be mistaken.",
    "Maybe, I mean, it's hard to say without more information about the situation.",
    "I guess that makes sense, sort of, but I'm still not entirely sure.",
    "Not really, but maybe I'm wrong, and I don't want to mislead you.",
    "Could be, I'm not entirely certain though, and I'd rather not guess.",
    "Might be, but I'd have to check first before I can say for sure.",
    "I'm not sure, to be honest with you, and I don't want to pretend I know.",
    "Well, I suppose it's possible, maybe, but I'm not completely confident about it.",
    "Um, I don't think I'm the right person to ask about this particular topic.",
    "Er, that's a really tough question, honestly, and I'm not sure I have the answer.",
    "Hmm, I'm not completely confident about this, so maybe we should verify it first.",
    "Like, I could be wrong, but this doesn't seem quite right to me somehow.",
    "You know, I'm not really an expert on this, so take what I say with a grain of salt.",
    "I mean, it depends on how you look at it, and there are multiple perspectives to consider.",
    "Maybe, but I'm not entirely convinced, and I'd like to think about it more.",
    "I guess, if you put it that way, but I'm still not one hundred percent sure.",
    "Sort of, but it's more complicated than that, and I don't want to oversimplify it.",
    "Kind of, I mean, there are exceptions to every rule, so it's hard to say definitively.",
    # MEDIUM QUESTIONS
    "Um, are you sure about that, because I'm not entirely certain myself?",
    "Well, do you think that's really the right approach, or should we consider alternatives?",
    "I mean, is that actually the best option, or are there other possibilities we should explore?",
    "You know, maybe we should ask someone else who might have more experience with this?",
    "Er, could you double check that for me, because I'm not completely confident it's correct?",
    "Hmm, are you certain that's the right answer, or could there be another solution?",
    "Like, do you really think so, because I'm having some doubts about it?",
    "I suppose, but are you positive about this, and have you verified all the details?",
    "Perhaps, but what if we're wrong about this, and we need to reconsider our approach?",
    "Sort of, but don't you think we should get more information before making a decision?",
    "Kind of, but maybe we should reconsider this, because I'm not entirely sure it's right?",
    "Probably, but I'm not entirely sure, you know, and I'd hate to give you wrong information?",
    "I think so, but what do you think, and do you have any concerns about it?",
    "Maybe, but are you confident about it, because I'm still not completely certain myself?",
    "I guess, but I could be wrong, right, and I don't want to mislead you?",
    "Not really, but maybe I'm misunderstanding something, and you could help clarify it for me?",
    "Could be, but don't you think we should verify this before we proceed with anything?",
    "Might be, but are we certain about this, because I'm having some doubts about it?",
    "I'm not sure, but what's your take on it, and do you think we're on the right track?",
    "Well, do you think we're making the right choice, or should we take more time to think?",
    # MEDIUM EXCLAMATIONS
    "Um, I'm not sure if that's a good idea, and I'm a bit worried about it!",
    "Well, maybe we should think about this more before we commit to anything!",
    "I mean, I don't know if I'm comfortable with that, and I'm having second thoughts!",
    "You know, I'm not entirely convinced this will work, and I'm a little skeptical!",
    "Er, I think maybe we're rushing into this, and we should slow down a bit!",
    "Hmm, I'm not sure that's the best approach, and maybe we should reconsider!",
    "Like, I could be wrong, but this seems risky, and I'm not completely comfortable with it!",
    "I suppose, but I'm not one hundred percent certain, and I'd rather be more confident!",
    "Perhaps, but I'm having second thoughts about this, and I'm not sure it's right!",
    "Sort of, but I'm not completely sold on the idea, and I have some concerns!",
    # LONG STATEMENTS
    "Um, I'm not really sure if that's the right approach, to be honest, and I'd hate to give you wrong advice.",
    (
        "Well, maybe we could try a different method, but I'm not certain it would work, and I'm not entirely "
        "confident about it."
    ),
    (
        "I mean, it's possible that could be the solution, but I'm not entirely convinced, and I'd like to think about "
        "it more."
    ),
    "You know, I'm not really an expert on this topic, so I could be wrong, and I don't want to mislead you.",
    (
        "Er, I think maybe we should reconsider our options before making a final decision, because I'm not completely "
        "sure about this."
    ),
    "Hmm, I'm not sure if that's the best way to handle this situation, and I'm having some doubts about it.",
    (
        "Like, I don't know, maybe we should get a second opinion before proceeding, because I'm not entirely certain "
        "myself."
    ),
    "I suppose it could work, but I'm not one hundred percent confident about it, and I'd rather verify it first.",
    (
        "Perhaps we should take a step back and think about this more carefully, because I'm not completely sure we're "
        "on the right track."
    ),
    "Sort of, but it's more complicated than that, and I'm not entirely sure, so maybe we should get more information.",
    "Kind of, I mean, there are a lot of factors to consider here, and I don't want to oversimplify the situation.",
    (
        "Probably, but I'm not completely certain, and I'd hate to give you wrong information, so maybe we should "
        "double check."
    ),
    "I think so, but don't quote me on that, because I could be mistaken, and I'm not entirely confident about it.",
    (
        "Maybe, I mean, it's hard to say without more information about the situation, and I don't want to guess "
        "incorrectly."
    ),
    "I guess that makes sense, sort of, but I'm still not entirely sure, and I'd like to think about it more.",
    "Not really, but maybe I'm wrong, and I don't want to mislead you, so perhaps we should verify this first.",
    (
        "Could be, I'm not entirely certain though, and I'd rather not guess, so maybe we should ask someone who knows "
        "more."
    ),
    (
        "Might be, but I'd have to check first before I can say for sure, and I don't want to give you incorrect "
        "information."
    ),
    "I'm not sure, to be honest with you, and I don't want to pretend I know, so maybe we should look into it more.",
    (
        "Well, I suppose it's possible, maybe, but I'm not completely confident about it, and I'm having some doubts "
        "about whether it's right."
    ),
    # LONG QUESTIONS
    (
        "Um, are you sure about that, because I'm not entirely certain myself, and I'd like to verify it before we "
        "proceed?"
    ),
    (
        "Well, do you think that's really the right approach, or should we consider alternatives, because I'm not "
        "completely convinced about it?"
    ),
    (
        "I mean, is that actually the best option, or are there other possibilities we should explore, because I'm not "
        "entirely sure?"
    ),
    (
        "You know, maybe we should ask someone else who might have more experience with this, because I'm not really "
        "an expert on this topic?"
    ),
    (
        "Er, could you double check that for me, because I'm not completely confident it's correct, and I'd hate to "
        "make a mistake?"
    ),
    (
        "Hmm, are you certain that's the right answer, or could there be another solution, because I'm having some "
        "doubts about it?"
    ),
    (
        "Like, do you really think so, because I'm having some doubts about it, and I'm not entirely convinced it's "
        "the right approach?"
    ),
    (
        "I suppose, but are you positive about this, and have you verified all the details, because I'm not completely "
        "certain myself?"
    ),
    (
        "Perhaps, but what if we're wrong about this, and we need to reconsider our approach, because I'm not entirely "
        "confident about it?"
    ),
    (
        "Sort of, but don't you think we should get more information before making a decision, because I'm not "
        "completely sure about this?"
    ),
    (
        "Kind of, but maybe we should reconsider this, because I'm not entirely sure it's right, and I'd like to think "
        "about it more?"
    ),
    (
        "Probably, but I'm not entirely sure, you know, and I'd hate to give you wrong information, so maybe we should "
        "verify it first?"
    ),
    (
        "I think so, but what do you think, and do you have any concerns about it, because I'm not completely "
        "confident about this?"
    ),
    (
        "Maybe, but are you confident about it, because I'm still not completely certain myself, and I'm having some "
        "doubts about it?"
    ),
    (
        "I guess, but I could be wrong, right, and I don't want to mislead you, so perhaps we should double check this "
        "first?"
    ),
    (
        "Not really, but maybe I'm misunderstanding something, and you could help clarify it for me, because I'm not "
        "entirely sure about this?"
    ),
    (
        "Could be, but don't you think we should verify this before we proceed with anything, because I'm not "
        "completely confident about it?"
    ),
    (
        "Might be, but are we certain about this, because I'm having some doubts about it, and I'm not entirely "
        "convinced it's right?"
    ),
    (
        "I'm not sure, but what's your take on it, and do you think we're on the right track, because I'm not "
        "completely certain myself?"
    ),
    (
        "Well, do you think we're making the right choice, or should we take more time to think, because I'm not "
        "entirely confident about this?"
    ),
]

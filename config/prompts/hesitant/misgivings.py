"""Hesitant prompts: extra long and ultra long statements and questions."""

from __future__ import annotations

MISGIVINGS: list[str] = [
    # EXTRA LONG QUESTIONS
    (
        "Um, are you sure about that, because I'm not entirely certain myself, and I'd like to verify it before we "
        "proceed, so maybe we should double check?"
    ),
    (
        "Well, do you think that's really the right approach, or should we consider alternatives, because I'm not "
        "completely convinced about it, and I'm having some doubts?"
    ),
    (
        "I mean, is that actually the best option, or are there other possibilities we should explore, because I'm not "
        "entirely sure, and I'd like to think about it more?"
    ),
    (
        "You know, maybe we should ask someone else who might have more experience with this, because I'm not really "
        "an expert on this topic, and I could be wrong?"
    ),
    (
        "Er, could you double check that for me, because I'm not completely confident it's correct, and I'd hate to "
        "make a mistake, so perhaps we should verify it first?"
    ),
    (
        "Hmm, are you certain that's the right answer, or could there be another solution, because I'm having some "
        "doubts about it, and I'm not entirely convinced?"
    ),
    (
        "Like, do you really think so, because I'm having some doubts about it, and I'm not entirely convinced it's "
        "the right approach, so maybe we should reconsider?"
    ),
    (
        "I suppose, but are you positive about this, and have you verified all the details, because I'm not completely "
        "certain myself, and I'd like to be more confident?"
    ),
    (
        "Perhaps, but what if we're wrong about this, and we need to reconsider our approach, because I'm not entirely "
        "confident about it, so maybe we should think about it more?"
    ),
    (
        "Sort of, but don't you think we should get more information before making a decision, because I'm not "
        "completely sure about this, and I'd hate to make the wrong choice?"
    ),
    (
        "Kind of, but maybe we should reconsider this, because I'm not entirely sure it's right, and I'd like to think "
        "about it more, so perhaps we should take a step back?"
    ),
    (
        "Probably, but I'm not entirely sure, you know, and I'd hate to give you wrong information, so maybe we should "
        "verify it first, because I'm not completely confident about it?"
    ),
    (
        "I think so, but what do you think, and do you have any concerns about it, because I'm not completely "
        "confident about this, and I'm having some doubts about it?"
    ),
    (
        "Maybe, but are you confident about it, because I'm still not completely certain myself, and I'm having some "
        "doubts about it, so perhaps we should verify it first?"
    ),
    (
        "I guess, but I could be wrong, right, and I don't want to mislead you, so perhaps we should double check this "
        "first, because I'm not entirely confident about it?"
    ),
    (
        "Not really, but maybe I'm misunderstanding something, and you could help clarify it for me, because I'm not "
        "entirely sure about this, and I'd like to understand it better?"
    ),
    (
        "Could be, but don't you think we should verify this before we proceed with anything, because I'm not "
        "completely confident about it, and I'm having some concerns about it?"
    ),
    (
        "Might be, but are we certain about this, because I'm having some doubts about it, and I'm not entirely "
        "convinced it's right, so maybe we should think about it more?"
    ),
    (
        "I'm not sure, but what's your take on it, and do you think we're on the right track, because I'm not "
        "completely certain myself, and I'd like to hear your perspective?"
    ),
    (
        "Well, do you think we're making the right choice, or should we take more time to think, because I'm not "
        "entirely confident about this, and I'm having some doubts about it?"
    ),
    # EXTRA LONG EXCLAMATIONS
    (
        "Um, I'm not sure if that's a good idea, and I'm a bit worried about it, so maybe we should reconsider, "
        "because I'm not entirely confident about it!"
    ),
    (
        "Well, maybe we should think about this more before we commit to anything, because I'm not entirely confident "
        "about it, and I'm having some concerns about it!"
    ),
    (
        "I mean, I don't know if I'm comfortable with that, and I'm having second thoughts, so maybe we should slow "
        "down, because I'm not completely sure it's right!"
    ),
    (
        "You know, I'm not entirely convinced this will work, and I'm a little skeptical, so perhaps we should get "
        "more information, because I'm not entirely confident about it!"
    ),
    (
        "Er, I think maybe we're rushing into this, and we should slow down a bit, because I'm not completely sure "
        "it's right, and I'm having some doubts about it!"
    ),
    (
        "Hmm, I'm not sure that's the best approach, and maybe we should reconsider, because I'm having some doubts "
        "about it, and I'm not entirely convinced it's right!"
    ),
    (
        "Like, I could be wrong, but this seems risky, and I'm not completely comfortable with it, so maybe we should "
        "think about it more, because I'm not entirely confident!"
    ),
    (
        "I suppose, but I'm not one hundred percent certain, and I'd rather be more confident, so perhaps we should "
        "verify it first, because I'm having some concerns about it!"
    ),
    (
        "Perhaps, but I'm having second thoughts about this, and I'm not sure it's right, so maybe we should take a "
        "step back, because I'm not entirely confident about it!"
    ),
    (
        "Sort of, but I'm not completely sold on the idea, and I have some concerns, so perhaps we should reconsider "
        "this approach, because I'm not entirely sure it's right!"
    ),
    # ULTRA LONG STATEMENTS
    (
        "Um, I'm not really sure if that's the right approach, to be honest, and I'd hate to give you wrong advice, so "
        "maybe we should get a second opinion, because I'm not entirely confident about it."
    ),
    (
        "Well, maybe we could try a different method, but I'm not certain it would work, and I'm not entirely "
        "confident about it, so perhaps we should think about it more, because I'm having some doubts."
    ),
    (
        "I mean, it's possible that could be the solution, but I'm not entirely convinced, and I'm having some doubts "
        "about it, and I'm not completely certain, so maybe we should verify it first."
    ),
    (
        "Er, I think maybe we should reconsider our options before making a final decision, because I'm not completely "
        "sure about this, and I'd rather verify it first, so perhaps we should take a step back."
    ),
    (
        "Hmm, I'm not sure if that's the best way to handle this situation, and I'm having some doubts about it, so "
        "maybe we should take a step back, because I'm not entirely convinced it's right."
    ),
    (
        "Like, I don't know, maybe we should get a second opinion before proceeding, because I'm not entirely certain "
        "myself, and I don't want to make a mistake, so perhaps we should verify it first."
    ),
    (
        "I suppose it could work, but I'm not one hundred percent confident about it, and I'd rather verify it first, "
        "so perhaps we should double check everything, because I'm not entirely sure about it."
    ),
    (
        "Perhaps we should take a step back and think about this more carefully, because I'm not completely sure we're "
        "on the right track, and I'm having some concerns, so maybe we should reconsider our approach."
    ),
    (
        "Sort of, but it's more complicated than that, and I'm not entirely sure, so maybe we should get more "
        "information before we make any final decisions, because I'm not completely confident about it."
    ),
    (
        "Kind of, I mean, there are a lot of factors to consider here, and I don't want to oversimplify the situation, "
        "so maybe we should think about it more, because I'm not entirely certain about it."
    ),
    (
        "Probably, but I'm not completely certain, and I'd hate to give you wrong information, so maybe we should "
        "double check, because I'm not entirely confident about it, and I'm having some doubts about it."
    ),
    (
        "I think so, but don't quote me on that, because I could be mistaken, and I'm not entirely confident about it, "
        "so perhaps we should verify it first, because I'm not completely certain about it."
    ),
    (
        "Maybe, I mean, it's hard to say without more information about the situation, and I don't want to guess "
        "incorrectly, so maybe we should gather more data first, because I'm not entirely confident about it."
    ),
    (
        "I guess that makes sense, sort of, but I'm still not entirely sure, and I'm having some doubts about it, and "
        "I'm not completely certain about it, so perhaps we should take a step back."
    ),
    (
        "Not really, but maybe I'm wrong, and I don't want to mislead you, so perhaps we should verify this first, "
        "because I'm not completely certain about it, and I'm having some concerns about it."
    ),
    (
        "Could be, I'm not entirely certain though, and I'd rather not guess, so maybe we should ask someone who knows "
        "more about this particular topic, because I'm not entirely confident about it."
    ),
    (
        "Might be, but I'd have to check first before I can say for sure, and I don't want to give you incorrect "
        "information, so perhaps we should verify it, because I'm not completely certain about it."
    ),
    (
        "I'm not sure, to be honest with you, and I don't want to pretend I know, so maybe we should look into it "
        "more, because I'm not entirely confident, and I'm having some doubts about it."
    ),
    (
        "Well, I suppose it's possible, maybe, but I'm not completely confident about it, and I'm having some doubts "
        "about whether it's right, so perhaps we should reconsider, because I'm not entirely certain about it."
    ),
    # ULTRA LONG QUESTIONS
]

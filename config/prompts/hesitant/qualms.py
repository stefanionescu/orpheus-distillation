"""Hesitant prompts: long exclamations, then longer and extra long statements, questions, and exclamations."""

from __future__ import annotations

QUALMS: list[str] = [
    # LONG EXCLAMATIONS
    "Um, I'm not sure if that's a good idea, and I'm a bit worried about it, so maybe we should reconsider!",
    (
        "Well, maybe we should think about this more before we commit to anything, because I'm not entirely confident "
        "about it!"
    ),
    "I mean, I don't know if I'm comfortable with that, and I'm having second thoughts, so maybe we should slow down!",
    (
        "You know, I'm not entirely convinced this will work, and I'm a little skeptical, so perhaps we should get "
        "more information!"
    ),
    (
        "Er, I think maybe we're rushing into this, and we should slow down a bit, because I'm not completely sure "
        "it's right!"
    ),
    (
        "Hmm, I'm not sure that's the best approach, and maybe we should reconsider, because I'm having some doubts "
        "about it!"
    ),
    (
        "Like, I could be wrong, but this seems risky, and I'm not completely comfortable with it, so maybe we should "
        "think about it more!"
    ),
    (
        "I suppose, but I'm not one hundred percent certain, and I'd rather be more confident, so perhaps we should "
        "verify it first!"
    ),
    (
        "Perhaps, but I'm having second thoughts about this, and I'm not sure it's right, so maybe we should take a "
        "step back!"
    ),
    (
        "Sort of, but I'm not completely sold on the idea, and I have some concerns, so perhaps we should reconsider "
        "this approach!"
    ),
    # LONGER STATEMENTS
    (
        "I mean, it's possible that could be the solution, but I'm not entirely convinced, and I'm having some doubts "
        "about it."
    ),
    (
        "Er, I think maybe we should reconsider our options before making a final decision, because I'm not completely "
        "sure."
    ),
    (
        "Well, I suppose it's possible, maybe, but I'm not completely confident about it, and I'm having some doubts "
        "about it."
    ),
    # LONGER QUESTIONS
    (
        "Well, do you think that's really the right approach, or should we consider alternatives, because I'm not "
        "completely convinced?"
    ),
    (
        "You know, maybe we should ask someone else who might have more experience with this, because I'm not really "
        "an expert?"
    ),
    (
        "Not really, but maybe I'm misunderstanding something, and you could help clarify it for me, because I'm not "
        "entirely sure?"
    ),
    (
        "Could be, but don't you think we should verify this before we proceed, because I'm not completely confident "
        "about it?"
    ),
    # LONGER EXCLAMATIONS
    # EXTRA LONG STATEMENTS
    (
        "Um, I'm not really sure if that's the right approach, to be honest, and I'd hate to give you wrong advice, so "
        "maybe we should get a second opinion."
    ),
    (
        "Well, maybe we could try a different method, but I'm not certain it would work, and I'm not entirely "
        "confident about it, so perhaps we should think about it more."
    ),
    (
        "I mean, it's possible that could be the solution, but I'm not entirely convinced, and I'm having some doubts "
        "about it, and I'm not completely certain."
    ),
    (
        "You know, I'm not really an expert on this topic, so I could be wrong, and I don't want to mislead you, so "
        "maybe we should ask someone who knows more."
    ),
    (
        "Er, I think maybe we should reconsider our options before making a final decision, because I'm not completely "
        "sure about this, and I'd rather verify it first."
    ),
    (
        "Hmm, I'm not sure if that's the best way to handle this situation, and I'm having some doubts about it, so "
        "maybe we should take a step back."
    ),
    (
        "Like, I don't know, maybe we should get a second opinion before proceeding, because I'm not entirely certain "
        "myself, and I don't want to make a mistake."
    ),
    (
        "I suppose it could work, but I'm not one hundred percent confident about it, and I'd rather verify it first, "
        "so perhaps we should double check everything."
    ),
    (
        "Perhaps we should take a step back and think about this more carefully, because I'm not completely sure we're "
        "on the right track, and I'm having some concerns."
    ),
    (
        "Sort of, but it's more complicated than that, and I'm not entirely sure, so maybe we should get more "
        "information before we make any final decisions."
    ),
    (
        "Kind of, I mean, there are a lot of factors to consider here, and I don't want to oversimplify the situation, "
        "so maybe we should think about it more."
    ),
    (
        "Probably, but I'm not completely certain, and I'd hate to give you wrong information, so maybe we should "
        "double check, because I'm not entirely confident about it."
    ),
    (
        "I think so, but don't quote me on that, because I could be mistaken, and I'm not entirely confident about it, "
        "so perhaps we should verify it first."
    ),
    (
        "Maybe, I mean, it's hard to say without more information about the situation, and I don't want to guess "
        "incorrectly, so maybe we should gather more data first."
    ),
    (
        "I guess that makes sense, sort of, but I'm still not entirely sure, and I'm having some doubts about it, and "
        "I'm not completely certain about it."
    ),
    (
        "Not really, but maybe I'm wrong, and I don't want to mislead you, so perhaps we should verify this first, "
        "because I'm not completely certain about it."
    ),
    (
        "Could be, I'm not entirely certain though, and I'd rather not guess, so maybe we should ask someone who knows "
        "more about this particular topic."
    ),
    (
        "Might be, but I'd have to check first before I can say for sure, and I don't want to give you incorrect "
        "information, so perhaps we should verify it."
    ),
    (
        "I'm not sure, to be honest with you, and I don't want to pretend I know, so maybe we should look into it "
        "more, because I'm not entirely confident."
    ),
    (
        "Well, I suppose it's possible, maybe, but I'm not completely confident about it, and I'm having some doubts "
        "about whether it's right, so perhaps we should reconsider."
    ),
]

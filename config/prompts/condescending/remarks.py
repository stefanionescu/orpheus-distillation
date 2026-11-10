"""Condescending prompts: short, medium, and longer statements."""

from __future__ import annotations

REMARKS: list[str] = [
    # SHORT / ULTRA SHORT
    "Oh, sweetie.",
    "Bless your heart.",
    "That's adorable.",
    "How cute.",
    "Aww, honey.",
    "Oh, honey.",
    "Well, bless you.",
    "That's precious.",
    "How sweet.",
    "Aww, bless.",
    "Oh, dear.",
    "How quaint.",
    "That's nice, dear.",
    "Oh, you tried.",
    "How charming.",
    "That's so cute.",
    "Aww, how sweet.",
    "Well, aren't you special?",
    "How endearing.",
    "That's darling.",
    # MEDIUM SENTENCES
    "Oh sweetie, that's adorable.",
    "Let me explain this in simpler terms for you.",
    "Bless your heart, you tried your best.",
    "That's so cute that you think that.",
    "Aww, honey, you don't understand, do you?",
    "Well, aren't you just precious?",
    "How charming that you believe that.",
    "Oh, you poor thing, you have no idea.",
    "That's nice, dear, but you're wrong.",
    "How endearing that you think you know what you're talking about.",
    "Aww, bless your heart for trying.",
    "Oh honey, that's not how it works.",
    "Well, that's adorable that you think that.",
    "How sweet that you believe you're right.",
    "That's precious, but you're completely wrong.",
    "Oh dear, you really don't get it, do you?",
    "How quaint that you think you understand.",
    "That's so cute, but you're way off base.",
    "Aww, honey, let me help you understand.",
    "Well, bless you for your effort, but no.",
    "How charming that you think you know better.",
    "Oh sweetie, you're so naive.",
    "That's adorable that you believe that.",
    "How endearing that you think you're helping.",
    "Aww, bless your heart, you're confused.",
    "Oh honey, you really don't know what you're talking about.",
    "Well, that's precious, but you're mistaken.",
    "How sweet that you think you understand.",
    "Oh dear, you're so far off it's almost funny.",
    "How quaint that you believe you're right.",
    "That's so cute, but you're completely wrong.",
    "Aww, honey, let me break this down for you.",
    "Well, bless you for trying, but that's not it.",
    "How charming that you think you know what's best.",
    "Oh sweetie, you're way out of your depth.",
    "That's adorable that you think that matters.",
    "How endearing that you believe you're contributing.",
    "Aww, bless your heart, you're lost.",
    "Oh honey, you really don't understand the situation.",
    "Well, that's precious, but you're way off.",
    "How sweet that you think you have a clue.",
    "That's nice, dear, but you're completely wrong.",
    "Oh dear, you're so naive it's almost cute.",
    "How quaint that you think you know what you're doing.",
    "That's so cute, but you're mistaken.",
    "Aww, honey, let me explain this to you slowly.",
    "Well, bless you for your opinion, but no.",
    "How charming that you think you're right.",
    # LONGER
    (
        "Oh sweetie, that's adorable that you think you understand what's happening here, but you're really way out of "
        "your depth and you should probably just let the adults handle this."
    ),
    (
        "Let me explain this in simpler terms for you, because I can see you're struggling to grasp the basic concepts "
        "here, and I want to make sure you can at least follow along."
    ),
    (
        "Bless your heart, you tried your best, but unfortunately your best just isn't good enough for this situation, "
        "and I think it's time for someone more qualified to step in."
    ),
    (
        "That's so cute that you think that, and I really appreciate the effort you're putting in, but you're "
        "completely wrong and you're making things more difficult for everyone."
    ),
    (
        "Aww, honey, you don't understand, do you? And that's okay, not everyone can grasp these complex ideas, so "
        "maybe you should just step back and let someone who actually knows what they're doing take over."
    ),
    (
        "Well, aren't you just precious? I love how confident you are despite clearly not having any idea what you're "
        "talking about, and it's honestly kind of endearing how wrong you are."
    ),
    (
        "How charming that you believe that, and I can see you've put some thought into it, but unfortunately your "
        "thinking is flawed and you're way off base here."
    ),
    (
        "Oh, you poor thing, you have no idea what's really going on, do you? And that's okay, because some people "
        "just aren't equipped to handle these kinds of situations."
    ),
    (
        "That's nice, dear, but you're wrong, and I think it's time for you to stop talking and start listening to "
        "people who actually know what they're doing."
    ),
    (
        "How endearing that you think you know what you're talking about, but the reality is that you're completely "
        "out of your element and you should probably just stop while you're ahead."
    ),
    (
        "Aww, bless your heart for trying, but your attempt is so far off the mark that it's almost impressive how "
        "wrong you managed to be."
    ),
    (
        "Oh honey, that's not how it works, and I can see you're confused, so let me help you understand why you're so "
        "completely mistaken about everything."
    ),
    (
        "Well, that's adorable that you think that, and I appreciate your enthusiasm, but you're so wrong that it's "
        "almost cute how confident you are in your incorrectness."
    ),
    (
        "How sweet that you believe you're right, but unfortunately you're not, and I think it's time someone set you "
        "straight before you embarrass yourself further."
    ),
    (
        "That's precious, but you're completely wrong, and I'm going to need you to step aside and let someone who "
        "actually understands the situation handle this."
    ),
    (
        "Oh dear, you really don't get it, do you? And that's okay, because not everyone can be expected to understand "
        "these things, but maybe you should just stop trying."
    ),
    (
        "How quaint that you think you understand, but the truth is you're way out of your depth and you should "
        "probably just admit you don't know what you're doing."
    ),
    (
        "That's so cute, but you're way off base, and I think it's time for you to realize that you're not helping and "
        "you should probably just stop talking."
    ),
    (
        "Aww, honey, let me help you understand, because I can see you're struggling, and I want to make sure you at "
        "least have a basic grasp of what's actually happening here."
    ),
    (
        "Well, bless you for your effort, but no, that's not it at all, and I think you need to take a step back and "
        "reconsider everything you think you know about this situation."
    ),
    (
        "How charming that you think you know better, but unfortunately you don't, and your confidence is actually "
        "making things worse because you're so sure you're right when you're completely wrong."
    ),
    (
        "Oh sweetie, you're so naive, and I can see you genuinely believe what you're saying, but the reality is that "
        "you're way out of your element and you should probably just listen instead of talking."
    ),
    (
        "That's adorable that you believe that, and I love how sure you are of yourself, but you're so wrong that it's "
        "almost impressive how confident you are in your complete misunderstanding."
    ),
    (
        "How endearing that you think you're helping, but you're actually making things worse, and I think it's time "
        "for you to step back and let someone more qualified handle this."
    ),
    (
        "Aww, bless your heart, you're confused, and that's okay, because this is clearly beyond your understanding, "
        "so maybe you should just stop trying and let the experts deal with it."
    ),
    (
        "Oh honey, you really don't know what you're talking about, and I can see you're trying, but your attempts are "
        "so far off the mark that you're actually making things more difficult."
    ),
    (
        "Well, that's precious, but you're mistaken, and I think it's time someone explained to you why you're so "
        "completely wrong about everything you think you understand."
    ),
    (
        "How sweet that you think you understand, but you don't, and I'm going to need you to stop talking and start "
        "listening to people who actually know what they're doing."
    ),
    (
        "That's nice, dear, but you're wrong, and I can see you're confused, so let me help you understand why your "
        "thinking is so flawed and why you need to reconsider everything."
    ),
    (
        "Oh dear, you're so far off it's almost funny, and I appreciate your effort, but you're way out of your depth "
        "and you should probably just admit you don't know what you're doing."
    ),
    (
        "How quaint that you believe you're right, but unfortunately you're not, and I think it's time for you to "
        "realize that your confidence is misplaced and you're completely wrong."
    ),
    (
        "That's so cute, but you're completely wrong, and I can see you're trying your best, but your best just isn't "
        "good enough and you need to step aside."
    ),
    (
        "Aww, honey, let me break this down for you, because I can see you're struggling to understand, and I want to "
        "make sure you at least have a basic grasp of what's happening."
    ),
    (
        "Well, bless you for trying, but that's not it, and I think you need to understand that you're way off base "
        "and you should probably just stop while you're ahead."
    ),
    (
        "How charming that you think you know what's best, but you don't, and your attempts to help are actually "
        "making things worse because you're so sure you're right when you're not."
    ),
    (
        "Oh sweetie, you're way out of your depth, and I can see you're trying, but this is clearly beyond your "
        "understanding and you should probably just let someone else handle it."
    ),
    (
        "That's adorable that you think that matters, but it doesn't, and I think it's time for you to realize that "
        "you're not contributing anything useful here."
    ),
    (
        "How endearing that you believe you're contributing, but you're not, and I can see you're confused, so maybe "
        "you should just stop talking and start listening."
    ),
    (
        "Aww, bless your heart, you're lost, and that's okay, because not everyone can be expected to understand these "
        "things, but maybe you should just step back."
    ),
    (
        "Oh honey, you really don't understand the situation, and I can see you're trying, but your understanding is "
        "so flawed that you're actually making things worse."
    ),
    (
        "Well, that's precious, but you're way off, and I think it's time someone explained to you why you're so "
        "completely wrong about everything you think you know."
    ),
    (
        "How sweet that you think you have a clue, but you don't, and I'm going to need you to stop talking and let "
        "someone who actually knows what they're doing take over."
    ),
    (
        "That's nice, dear, but you're completely wrong, and I can see you're confused, so let me help you understand "
        "why your thinking is so flawed."
    ),
    (
        "Oh dear, you're so naive it's almost cute, and I appreciate your effort, but you're way out of your element "
        "and you should probably just stop trying."
    ),
    (
        "How quaint that you think you know what you're doing, but you don't, and I think it's time for you to realize "
        "that your confidence is completely misplaced."
    ),
    (
        "That's so cute, but you're mistaken, and I can see you're trying your best, but your best just isn't good "
        "enough and you need to step aside."
    ),
    (
        "Aww, honey, let me explain this to you slowly, because I can see you're struggling, and I want to make sure "
        "you can at least follow along with what's happening."
    ),
    (
        "Well, bless you for your opinion, but no, that's not how it works, and I think you need to understand that "
        "you're way off base here."
    ),
    (
        "How charming that you think you're right, but you're not, and your attempts to help are actually making "
        "things worse because you're so sure of yourself when you're completely wrong."
    ),
]

"""Condescending prompts: questions of medium and longer length, then medium exclamations."""

from __future__ import annotations

QUESTIONS: list[str] = [
    # QUESTIONS - MEDIUM
    "Oh sweetie, do you really think that's how it works?",
    "Bless your heart, do you actually understand what you're saying?",
    "That's adorable, but do you really think you know what you're talking about?",
    "Aww, honey, do you honestly believe that?",
    "Well, aren't you just precious? Do you really think that matters?",
    "How charming, but do you actually know what you're doing?",
    "Oh, you poor thing, do you really think you understand this?",
    "That's nice, dear, but do you honestly believe you're right?",
    "How endearing, but do you really think you're helping?",
    "Aww, bless your heart, do you actually know what's going on?",
    "Oh honey, do you really think that's correct?",
    "Well, that's precious, but do you honestly understand the situation?",
    "How sweet, but do you really think you know what you're talking about?",
    "That's cute, but do you actually believe you're right?",
    "Oh dear, do you really think you understand what's happening?",
    "How quaint, but do you honestly know what you're doing?",
    "That's so cute, but do you really think that matters?",
    "Aww, honey, do you actually understand what you're saying?",
    "Well, bless you, but do you really think you're helping?",
    "How charming, but do you honestly believe you know what's best?",
    "Oh sweetie, do you really think you understand this?",
    "That's adorable, but do you actually know what you're talking about?",
    "How endearing, but do you really think you're right?",
    "Aww, bless your heart, do you honestly understand the situation?",
    "Oh honey, do you really think that's how it works?",
    "Well, that's precious, but do you actually believe you know what you're doing?",
    "How sweet, but do you really think you understand what's happening?",
    "That's nice, dear, but do you honestly think you're helping?",
    "Oh dear, do you really think you know what you're talking about?",
    "How quaint, but do you actually believe you're right?",
    # QUESTIONS - LONGER FORMATS
    (
        "Oh sweetie, do you really think that's how it works? Because I can see you're confused, and I want to make "
        "sure you understand why you're so completely wrong."
    ),
    (
        "Bless your heart, do you actually understand what you're saying? Because from where I'm standing, it seems "
        "like you have no idea what you're talking about."
    ),
    (
        "That's adorable, but do you really think you know what you're talking about? Because I can see you're trying, "
        "but you're way out of your depth here."
    ),
    (
        "Aww, honey, do you honestly believe that? Because I hate to break it to you, but you're completely wrong and "
        "you're making things worse."
    ),
    (
        "Well, aren't you just precious? Do you really think that matters? Because I can see you're confused, and I "
        "think it's time someone set you straight."
    ),
    (
        "How charming, but do you actually know what you're doing? Because from my perspective, it looks like you're "
        "completely lost and you should probably just stop."
    ),
    (
        "Oh, you poor thing, do you really think you understand this? Because I can see you're trying, but your "
        "understanding is so flawed that it's almost impressive."
    ),
    (
        "That's nice, dear, but do you honestly believe you're right? Because unfortunately you're not, and I think "
        "it's time for you to realize that."
    ),
    (
        "How endearing, but do you really think you're helping? Because you're actually making things worse, and I "
        "think you should probably just step back."
    ),
    (
        "Aww, bless your heart, do you actually know what's going on? Because I can see you're confused, and maybe you "
        "should just let someone else handle this."
    ),
    (
        "Oh honey, do you really think that's correct? Because I hate to tell you, but you're way off base and you're "
        "making things more difficult."
    ),
    (
        "Well, that's precious, but do you honestly understand the situation? Because from where I'm standing, it "
        "seems like you have no clue what's happening."
    ),
    (
        "How sweet, but do you really think you know what you're talking about? Because I can see you're trying, but "
        "you're so wrong it's almost cute."
    ),
    (
        "That's cute, but do you actually believe you're right? Because unfortunately you're not, and I think it's "
        "time someone explained why you're so mistaken."
    ),
    (
        "Oh dear, do you really think you understand what's happening? Because I can see you're confused, and maybe "
        "you should just stop talking and start listening."
    ),
    (
        "How quaint, but do you honestly know what you're doing? Because from my perspective, it looks like you're way "
        "out of your element and you should probably just stop."
    ),
    (
        "That's so cute, but do you really think that matters? Because I can see you're trying, but your attempts are "
        "so far off the mark that they're not helping."
    ),
    (
        "Aww, honey, do you actually understand what you're saying? Because I hate to break it to you, but you're "
        "completely wrong and you're making things worse."
    ),
    (
        "Well, bless you, but do you really think you're helping? Because you're actually making things more "
        "difficult, and I think you should probably just step aside."
    ),
    (
        "How charming, but do you honestly believe you know what's best? Because unfortunately you don't, and I think "
        "it's time for you to realize that."
    ),
    (
        "Oh sweetie, do you really think you understand this? Because I can see you're trying, but you're way out of "
        "your depth and you should probably just stop."
    ),
    (
        "That's adorable, but do you actually know what you're talking about? Because from where I'm standing, it "
        "seems like you have no idea what you're doing."
    ),
    (
        "How endearing, but do you really think you're right? Because I hate to tell you, but you're completely wrong "
        "and you're making things worse."
    ),
    (
        "Aww, bless your heart, do you honestly understand the situation? Because I can see you're confused, and maybe "
        "you should just let someone else handle this."
    ),
    (
        "Oh honey, do you really think that's how it works? Because unfortunately it's not, and I think it's time "
        "someone explained why you're so mistaken."
    ),
    (
        "Well, that's precious, but do you actually believe you know what you're doing? Because from my perspective, "
        "it looks like you're completely lost."
    ),
    (
        "How sweet, but do you really think you understand what's happening? Because I can see you're trying, but your "
        "understanding is so flawed that it's not helping."
    ),
    (
        "That's nice, dear, but do you honestly think you're helping? Because you're actually making things worse, and "
        "I think you should probably just step back."
    ),
    (
        "Oh dear, do you really think you know what you're talking about? Because I hate to break it to you, but "
        "you're way off base and you're making things more difficult."
    ),
    (
        "How quaint, but do you actually believe you're right? Because unfortunately you're not, and I think it's time "
        "for you to realize that your confidence is misplaced."
    ),
    # EXCLAMATIONS - MEDIUM
    "Oh sweetie, that's so adorable!",
    "Bless your heart, you tried!",
    "That's precious, but you're wrong!",
    "Aww, honey, that's so cute!",
    "Well, aren't you just special?",
    "How charming that you think that!",
    "Oh, you poor thing, you have no idea!",
    "That's nice, dear, but no!",
    "How endearing that you believe that!",
    "Aww, bless your heart for trying!",
    "Oh honey, that's not how it works!",
    "Well, that's adorable that you think that!",
    "How sweet that you believe you're right!",
    "That's precious, but you're completely wrong!",
    "Oh dear, you really don't get it!",
    "How quaint that you think you understand!",
    "That's so cute, but you're way off!",
    "Aww, honey, let me help you!",
    "Well, bless you for your effort!",
    "How charming that you think you know better!",
    "Oh sweetie, you're so naive!",
    "That's adorable that you believe that!",
    "How endearing that you think you're helping!",
    "Aww, bless your heart, you're confused!",
    "Oh honey, you don't know what you're talking about!",
    "Well, that's precious, but you're mistaken!",
    "How sweet that you think you understand!",
    "That's nice, dear, but you're wrong!",
    "Oh dear, you're so far off!",
    "How quaint that you believe you're right!",
]

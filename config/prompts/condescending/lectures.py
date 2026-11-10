"""Condescending prompts: longer exclamations, then long statements, questions, and exclamations."""

from __future__ import annotations

LECTURES: list[str] = [
    # EXCLAMATIONS - LONGER FORMATS
    (
        "Oh sweetie, that's so adorable that you think you understand what's happening here, but you're really way out "
        "of your depth!"
    ),
    "Bless your heart, you tried your best, but unfortunately your best just isn't good enough for this situation!",
    (
        "That's precious, but you're wrong, and I think it's time for you to stop talking and start listening to "
        "people who actually know what they're doing!"
    ),
    (
        "Aww, honey, that's so cute that you think that, but you're completely wrong and you're making things more "
        "difficult for everyone!"
    ),
    (
        "Well, aren't you just special? I love how confident you are despite clearly not having any idea what you're "
        "talking about!"
    ),
    "How charming that you think that, but unfortunately your thinking is flawed and you're way off base here!",
    (
        "Oh, you poor thing, you have no idea what's really going on, and that's okay, because some people just aren't "
        "equipped to handle these kinds of situations!"
    ),
    (
        "That's nice, dear, but you're wrong, and I think it's time for you to realize that you're not helping and you "
        "should probably just stop!"
    ),
    (
        "How endearing that you think you know what you're talking about, but the reality is that you're completely "
        "out of your element!"
    ),
    (
        "Aww, bless your heart for trying, but your attempt is so far off the mark that it's almost impressive how "
        "wrong you managed to be!"
    ),
    (
        "Oh honey, that's not how it works, and I can see you're confused, so let me help you understand why you're so "
        "completely mistaken!"
    ),
    (
        "Well, that's adorable that you think that, but you're so wrong that it's almost cute how confident you are in "
        "your incorrectness!"
    ),
    (
        "How sweet that you believe you're right, but unfortunately you're not, and I think it's time someone set you "
        "straight!"
    ),
    (
        "That's precious, but you're completely wrong, and I'm going to need you to step aside and let someone who "
        "actually understands handle this!"
    ),
    (
        "Oh dear, you really don't get it, do you? And that's okay, because not everyone can be expected to understand "
        "these things!"
    ),
    (
        "How quaint that you think you understand, but the truth is you're way out of your depth and you should "
        "probably just admit you don't know what you're doing!"
    ),
    (
        "That's so cute, but you're way off base, and I think it's time for you to realize that you're not helping and "
        "you should probably just stop talking!"
    ),
    (
        "Aww, honey, let me help you understand, because I can see you're struggling, and I want to make sure you at "
        "least have a basic grasp of what's actually happening!"
    ),
    (
        "Well, bless you for your effort, but no, that's not it at all, and I think you need to take a step back and "
        "reconsider everything you think you know!"
    ),
    (
        "How charming that you think you know better, but unfortunately you don't, and your confidence is actually "
        "making things worse!"
    ),
    (
        "Oh sweetie, you're so naive, and I can see you genuinely believe what you're saying, but the reality is that "
        "you're way out of your element!"
    ),
    (
        "That's adorable that you believe that, and I love how sure you are of yourself, but you're so wrong that it's "
        "almost impressive!"
    ),
    (
        "How endearing that you think you're helping, but you're actually making things worse, and I think it's time "
        "for you to step back!"
    ),
    "Aww, bless your heart, you're confused, and that's okay, because this is clearly beyond your understanding!",
    (
        "Oh honey, you really don't know what you're talking about, and I can see you're trying, but your attempts are "
        "so far off the mark!"
    ),
    (
        "Well, that's precious, but you're mistaken, and I think it's time someone explained to you why you're so "
        "completely wrong!"
    ),
    (
        "How sweet that you think you understand, but you don't, and I'm going to need you to stop talking and start "
        "listening!"
    ),
    (
        "That's nice, dear, but you're wrong, and I can see you're confused, so let me help you understand why your "
        "thinking is so flawed!"
    ),
    "Oh dear, you're so far off it's almost funny, and I appreciate your effort, but you're way out of your depth!",
    (
        "How quaint that you believe you're right, but unfortunately you're not, and I think it's time for you to "
        "realize that your confidence is misplaced!"
    ),
    "Oh sweetie, you're way out of your league here.",
    "Bless your heart, you're trying so hard.",
    "That's precious that you think you understand.",
    "Aww, honey, you're so confused.",
    "Well, aren't you just delightful?",
    "Oh, you poor thing, you're lost.",
    "Aww, bless your heart, you tried.",
    "Oh honey, you don't get it, do you?",
    "That's precious, but you're mistaken.",
    "Oh dear, you're so naive.",
    "That's so cute, but you're wrong.",
    "Aww, honey, let me explain this simply.",
    "Well, bless you for your opinion.",
    "How endearing that you think you're contributing.",
    "Oh honey, you don't understand the situation.",
    "Oh sweetie, do you really think that's correct?",
    "Bless your heart, do you actually understand?",
    "That's adorable, but do you really know what you're talking about?",
    # ADDITIONAL LONG EXAMPLES - STATEMENTS
    (
        "I'm sure in your limited experience this seems like a good idea, but those of us who actually know what we're "
        "doing can see the flaws immediately."
    ),
    (
        "It's really sweet that you're trying to contribute, but perhaps you should leave the important decisions to "
        "people with more expertise."
    ),
    (
        "I appreciate the enthusiasm, I really do, but this is clearly beyond your level of understanding and you're "
        "making things more complicated."
    ),
    (
        "Let me explain this in simpler terms since the normal explanation seems to have gone right over your head, "
        "bless your heart."
    ),
    (
        "I'm not trying to be mean, but someone needs to tell you that you're completely out of your depth here and "
        "it's becoming embarrassing."
    ),
    (
        "It must be nice to have such confidence despite having no actual qualifications or experience in this area "
        "whatsoever."
    ),
    (
        "I can see you've put a lot of thought into this, which makes it even more unfortunate that you've arrived at "
        "such a wrong conclusion."
    ),
    # ADDITIONAL LONG EXAMPLES - QUESTIONS
    (
        "Have you considered that maybe, just maybe, the experts who've been doing this for decades might know a bit "
        "more than you do?"
    ),
    (
        "Don't you think it might be wise to actually research this topic before sharing your uninformed opinions with "
        "everyone?"
    ),
    (
        "Do you honestly believe you're qualified to speak on this subject when you clearly don't understand the basic "
        "concepts?"
    ),
    "Isn't it possible that the reason nobody agrees with you is because you're simply wrong about this entire thing?",
    (
        "Have you ever stopped to consider that your lack of experience might be affecting your judgment in ways you "
        "don't even realize?"
    ),
    "Don't you find it a little presumptuous to lecture people who have far more experience and education than you do?",
    "Wouldn't it be better for everyone if you took a step back and let the adults handle this situation properly?",
    # ADDITIONAL LONG EXAMPLES - EXCLAMATIONS
    "It's truly remarkable how confident you are considering you've gotten almost every single fact completely wrong!",
    "I'm genuinely impressed by your ability to be so absolutely certain about things you clearly don't understand!",
    "It's almost admirable how you keep trying despite failing so consistently and spectacularly every single time!",
    "What a delightful reminder that some people have more confidence than actual knowledge or ability!",
    "How refreshing to meet someone who is completely unburdened by the weight of knowing what they're talking about!",
    "I'm honestly in awe of your willingness to share your opinion on topics you obviously know nothing about!",
]

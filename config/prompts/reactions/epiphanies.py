"""Reaction prompts: long reactions of sarcasm, support, nostalgia, realization, gratitude, and complex emotion."""

from __future__ import annotations

EPIPHANIES: list[str] = [
    # LONG REACTIONS - SARCASM AND SASS
    (
        "Oh wow, what a completely unexpected turn of events that literally everyone saw coming from a mile away "
        "except apparently you!"
    ),
    (
        "Well, color me surprised, said absolutely nobody who has ever paid attention to anything that's been "
        "happening around here!"
    ),
    "Congratulations on your discovery, I'm sure the rest of us who figured this out ages ago are thrilled for you!",
    (
        "Thank you for that brilliant observation, I don't know how we would have survived without your keen insight "
        "just now!"
    ),
    (
        "Alert the media, stop the presses, this is groundbreaking information that will revolutionize how we "
        "understand everything forever!"
    ),
    (
        "I'm so shocked I might faint, catch me somebody, because this revelation is just too much for my delicate "
        "sensibilities!"
    ),
    (
        "What an absolutely stunning display of the obvious, you should write a book about this profound wisdom you've "
        "uncovered!"
    ),
    (
        "Please, tell me more, I am absolutely fascinated by this information that I definitely haven't heard a "
        "thousand times before!"
    ),
    (
        "Your ability to state the obvious is truly a gift, have you considered going professional with this "
        "incredible talent?"
    ),
    (
        "I'm writing this down in my journal of things I already knew, right between common sense and basic "
        "observation skills!"
    ),
    # LONG REACTIONS - ENCOURAGEMENT AND SUPPORT
    (
        "You've got this in the bag, I believe in you more than you probably believe in yourself right now, and that's "
        "saying something!"
    ),
    (
        "Whatever happens, just know that there's at least one person rooting for you to succeed, and that person is "
        "definitely me!"
    ),
    (
        "The strength you've shown throughout all of this is genuinely inspiring, and I hope you give yourself credit "
        "for that!"
    ),
    (
        "Don't let anyone dim your shine, because you're absolutely brilliant and the world needs to see what you're "
        "capable of!"
    ),
    "Keep pushing forward because you're so much closer to the finish line than you realize, I can see it from here!",
    (
        "You are capable of so much more than you give yourself credit for, and it's time you started believing that "
        "truth!"
    ),
    (
        "The fact that you even attempted this puts you ahead of most people who are too scared to even try in the "
        "first place!"
    ),
    (
        "Your potential is literally limitless, and anyone who tells you otherwise clearly doesn't see what I'm seeing "
        "right now!"
    ),
    (
        "I've seen you overcome tougher challenges than this before, and I have zero doubt you'll do it again this "
        "time too!"
    ),
    (
        "Remember that every expert was once a beginner, and every master has failed more times than the beginner has "
        "even tried!"
    ),
    # LONG REACTIONS - NOSTALGIA AND REFLECTION
    (
        "This takes me right back to simpler times when things weren't so complicated and life made a lot more sense "
        "overall!"
    ),
    (
        "I can't believe how much has changed since then, it feels like a completely different lifetime ago when I "
        "think about it!"
    ),
    (
        "They really don't make them like they used to, and I'm not just saying that to sound like an old person "
        "complaining!"
    ),
    (
        "If I could go back and relive one moment from the past, I wouldn't even know where to start because there are "
        "so many!"
    ),
    (
        "Looking back now, I realize just how much I took for granted, and I wish I could tell my past self to "
        "appreciate it more!"
    ),
    "The memories are flooding back all at once, and I'm not sure if I should laugh or cry about the passage of time!",
    (
        "It's funny how certain things can trigger such vivid memories that you thought you had forgotten about "
        "completely!"
    ),
    (
        "I get a little nostalgic every time I think about those days, because they really were some of the best times "
        "of my life!"
    ),
    (
        "Sometimes I wonder what life would be like if things had gone differently back then, but there's no point "
        "dwelling on it!"
    ),
    (
        "That era shaped who I am today, and even though it wasn't always easy, I wouldn't trade those experiences for "
        "anything!"
    ),
    # LONG REACTIONS - REALIZATION AND EPIPHANY
    (
        "Oh my god, it all makes sense now, every single piece of the puzzle just clicked into place and I finally see "
        "the big picture!"
    ),
    (
        "I just had an epiphany that's going to fundamentally change the way I approach this entire situation from "
        "this point forward!"
    ),
    (
        "Everything I thought I knew was wrong, and this new understanding is both liberating and terrifying at the "
        "same time honestly!"
    ),
    (
        "The lightbulb just went off in my head and it's shining so bright that I'm surprised everyone else can't see "
        "it too!"
    ),
    (
        "Holy revelation, Batman, I cannot believe it took me this long to connect the dots when it was staring me in "
        "the face!"
    ),
    (
        "This changes everything I thought I understood about the situation, and now I need to completely reevaluate "
        "my approach to it!"
    ),
    (
        "I feel like I just unlocked a new level of understanding that I didn't even know existed until this very "
        "moment right now!"
    ),
    (
        "The clarity hitting me right now is almost overwhelming, like a fog has been lifted and I can finally see "
        "everything clearly!"
    ),
    (
        "Why didn't anyone tell me this sooner, this information would have saved me so much time and confusion along "
        "the way!"
    ),
    (
        "I'm having one of those moments where everything just suddenly makes sense and you wonder why it took you so "
        "long to get there!"
    ),
    # LONG REACTIONS - GRATITUDE AND APPRECIATION
    (
        "I genuinely don't know what I would do without you, and I hope you understand just how much your support "
        "means to me!"
    ),
    (
        "There aren't enough words in the entire English language to express how grateful I am for everything you've "
        "done for me!"
    ),
    "You went above and beyond in every possible way, and I'm going to remember this kindness for the rest of my life!",
    (
        "The fact that you took the time to do this when you didn't have to speaks volumes about the kind of person "
        "you are!"
    ),
    (
        "I'm absolutely overwhelmed by the generosity being shown here, and I promise I won't take any of it for "
        "granted ever!"
    ),
    (
        "This is one of those moments that restores your faith in humanity and reminds you that good people still "
        "exist in the world!"
    ),
    (
        "You've made such a positive impact on my life, and I don't think you fully realize just how significant that "
        "impact has been!"
    ),
    (
        "My heart is so full right now, and it's all because of the incredible kindness and thoughtfulness you've "
        "shown me today!"
    ),
    "I'm going to pay this forward in every way I possibly can, because the world needs more of this kind of energy!",
    (
        "From the bottom of my heart, thank you for being you and for making the world a slightly better place just by "
        "existing!"
    ),
    # EXTRA LONG REACTIONS - COMPLEX EMOTIONS
    (
        "I'm experiencing so many emotions right now that I can't even identify what I'm feeling anymore, it's like a "
        "whole symphony of feelings playing at once and I'm just along for the ride!"
    ),
    (
        "Part of me wants to celebrate while another part wants to cry, and I'm not sure which side is going to win "
        "this internal battle that's raging inside my head right now!"
    ),
    (
        "The emotional whiplash from this situation is giving me vertigo, one second I'm up and the next I'm down, and "
        "I can't keep up with all these sudden changes anymore!"
    ),
    (
        "I've never felt more conflicted in my entire life than I do at this exact moment, because there are "
        "compelling arguments on both sides and I genuinely don't know where I stand!"
    ),
    (
        "This is one of those bittersweet moments where you're happy and sad at the same time, and your brain doesn't "
        "quite know how to process both of those feelings simultaneously!"
    ),
    (
        "I'm laughing on the outside but screaming on the inside, which is probably not the healthiest way to cope "
        "with this but it's all I've got right now honestly!"
    ),
    (
        "The rollercoaster of emotions I've been on today would put any theme park ride to shame, and I'm ready to get "
        "off this wild ride whenever the universe decides to let me!"
    ),
    (
        "I didn't know it was possible to feel this strongly about something until this very moment, and now I "
        "understand what everyone has been talking about all along!"
    ),
    (
        "My emotional bandwidth is completely maxed out and I don't have the capacity to process anything else today, "
        "so if you need me I'll be staring blankly at a wall!"
    ),
    (
        "I need at least a week to emotionally decompress from what just happened here, maybe longer depending on how "
        "the next few hours play out for everyone involved!"
    ),
]

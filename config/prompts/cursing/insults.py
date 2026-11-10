"""Profane prompts: long questions and exclamations, then mixed long examples."""

from __future__ import annotations

INSULTS: list[str] = [
    # LONG QUESTIONS
    (
        "What the fuck is wrong with you that you can't seem to understand basic human decency or treat people with "
        "even a shred of respect?"
    ),
    (
        "Why the hell do you keep pulling this same bullshit over and over again when you know damn well how much it "
        "pisses everyone off?"
    ),
    (
        "Do you seriously not understand that your actions have consequences, or are you just too fucking stupid to "
        "connect the dots?"
    ),
    (
        "How many more times are you going to fuck things up before you finally admit that you're the problem and not "
        "everyone else around you?"
    ),
    (
        "Are you aware that every single person here thinks you're an insufferable asshole, or is your head too far up "
        "your own ass to notice?"
    ),
    (
        "What kind of fucked up logic are you using to justify treating people like they're worthless garbage who "
        "exist just to serve you?"
    ),
    (
        "Why should anyone trust you when you've proven time and time again that you're nothing but a lying, "
        "manipulative piece of shit?"
    ),
    (
        "Do you think I'm a complete fucking idiot who can't see through your pathetic attempts to manipulate the "
        "situation in your favor?"
    ),
    (
        "How the hell do you expect me to forgive you for the absolute shitstorm you've caused in my life with your "
        "selfish decisions?"
    ),
    (
        "What made you think that your piss poor excuse for an apology would somehow make up for all the damage you've "
        "done?"
    ),
    (
        "Why do you always have to be such a goddamn contrarian asshole who argues about every little thing just for "
        "the sake of arguing?"
    ),
    (
        "Are you fucking kidding me right now with this bullshit, or do you actually expect me to believe the garbage "
        "coming out of your mouth?"
    ),
    (
        "What the shit is your problem that you can't go a single day without causing some kind of drama or starting "
        "unnecessary fights?"
    ),
    (
        "How goddamn hard is it for you to keep your word for once and not be a flaky piece of shit who disappoints "
        "everyone?"
    ),
    (
        "Do you have any idea how fucking exhausting it is to deal with your constant negativity and complaining about "
        "every little thing?"
    ),
    (
        "Why the hell should I care about your problems when you've never once given a shit about anything I've been "
        "going through?"
    ),
    "What makes you think you're so goddamn special that the rules don't apply to you like they do to everyone else?",
    (
        "Are you seriously expecting me to apologize when you're the one who fucked everything up with your careless "
        "bullshit?"
    ),
    "How the fuck did you manage to turn a simple situation into such a complete and total disaster in record time?",
    "What kind of asshole does the things you've done and then has the audacity to act like the victim in all of this?",
    (
        "Why do I have to keep explaining the same damn things to you over and over when you refuse to listen to "
        "anything I say?"
    ),
    (
        "Do you genuinely believe your own bullshit, or are you just hoping everyone else is stupid enough to buy your "
        "lies?"
    ),
    (
        "What the hell possessed you to think that was a good idea when literally anyone with half a brain could see "
        "it was fucking stupid?"
    ),
    (
        "How many people do you have to fuck over before you realize that you're the goddamn common denominator in all "
        "your failed relationships?"
    ),
    "Are you completely oblivious to how much of an inconsiderate asshole you are, or do you just not give a shit?",
    # LONG EXCLAMATIONS
    (
        "I can't fucking believe you would do something so incredibly stupid and selfish without even considering how "
        "it would affect the rest of us!"
    ),
    (
        "You're the biggest piece of shit I've ever had the misfortune of knowing, and I regret every moment I wasted "
        "being your friend!"
    ),
    (
        "This is absolutely fucking unacceptable and I'm not going to stand here and pretend like what you did was "
        "anything less than despicable!"
    ),
    (
        "I'm so goddamn angry right now that I could scream, and it's all because you can't seem to keep your shit "
        "together for five minutes!"
    ),
    (
        "You've ruined everything with your selfish, thoughtless bullshit, and I hope you're happy with the "
        "destruction you've caused, you fucking asshole!"
    ),
    (
        "The level of fucking betrayal I'm feeling right now is overwhelming, and I can't believe I ever trusted a "
        "deceitful shit like you!"
    ),
    (
        "I've never been so pissed off in my entire life, and it's all thanks to your complete inability to be a "
        "decent human being!"
    ),
    (
        "You're a toxic, manipulative piece of shit and I'm so fucking done pretending like your behavior doesn't "
        "affect everyone around you!"
    ),
    (
        "I can't stand the sight of you after what you've done, and I don't know how you can live with yourself "
        "knowing how shitty you are!"
    ),
    (
        "This is the last fucking straw and I'm not putting up with your bullshit for another second, you've crossed "
        "the line for the final time!"
    ),
    (
        "You've managed to fuck up every single thing you've ever touched, and I'm amazed that anyone still trusts you "
        "with anything important!"
    ),
    (
        "I'm absolutely livid that you would have the audacity to lie to my face after everything we've been through "
        "together, you backstabbing bastard!"
    ),
    (
        "The shit you've pulled this time is beyond anything I could have imagined, and I don't know how we're "
        "supposed to move past this!"
    ),
    (
        "You're such a goddamn disappointment and I can't believe I ever saw anything worthwhile in someone as "
        "pathetic and self centered as you!"
    ),
    (
        "I trusted you with my deepest secrets and you shit all over that trust like it meant absolutely nothing to "
        "you, you heartless prick!"
    ),
    (
        "This whole fucking situation is a disaster of your own making, and I refuse to be dragged down by your "
        "inability to take responsibility!"
    ),
    (
        "You've shown everyone exactly what kind of person you really are, and guess what, it's not fucking pretty, "
        "you two faced piece of shit!"
    ),
    (
        "I'm so fucking sick of your constant lies and manipulation that I could vomit, and I'm done letting you treat "
        "me like shit!"
    ),
    (
        "The damage you've done is irreparable, and I hope you spend the rest of your life regretting the fucked up "
        "choices you've made!"
    ),
    (
        "You're absolutely the worst person I've ever had to deal with, and that's saying something because I've met "
        "some real shitheads in my time!"
    ),
    (
        "I can't wrap my head around the sheer fucking magnitude of your stupidity, and I'm damn furious that I have "
        "to deal with the consequences!"
    ),
    (
        "You've burned every bridge and destroyed every relationship with your toxic bullshit, and now you have no one "
        "to blame but your own pathetic self!"
    ),
    (
        "I'm fucking done being patient and understanding when all you do is take advantage of my kindness and throw "
        "it back in my face!"
    ),
    (
        "The audacity you have to ask for my forgiveness after the horrific shit you've done is absolutely mind "
        "boggling and insulting!"
    ),
    (
        "You're a goddamn cancer on everyone around you, and I wish I had realized sooner what a destructive piece of "
        "shit you really are!"
    ),
    # ADDITIONAL LONG EXAMPLES - MIXED - Part 1
    (
        "I'm so fucking fed up with your constant bullshit that I don't even have the words to express how "
        "disappointed and angry I am right now."
    ),
    (
        "You've taken everything good in my life and turned it into a steaming pile of shit, and I will never forgive "
        "you for that."
    ),
    (
        "What the actual fuck is wrong with you that you can't see how your actions are destroying everything and "
        "everyone around you?"
    ),
    (
        "I've given you chance after chance and you've shit on every single one of them, so don't come crying to me "
        "when it all falls apart."
    ),
    (
        "The way you've treated me like garbage for years is finally catching up to you, and I hope you choke on your "
        "own fucking karma."
    ),
    (
        "I can't even look at you without feeling my blood pressure spike because you're such a fucking irritant to my "
        "existence."
    ),
    (
        "You think you're so damn clever with your little games, but everyone sees what a pathetic, manipulative "
        "asshole you really are."
    ),
    (
        "I'm done playing nice with someone who clearly doesn't give a flying fuck about anyone's feelings but their "
        "own selfish wants."
    ),
    (
        "Every goddamn day you find a new way to disappoint me, and I'm starting to think you do it on purpose just to "
        "piss me off."
    ),
    (
        "You're the reason I drink, and that's not a joke, you've literally driven me to needing alcohol to deal with "
        "your bullshit."
    ),
    (
        "The amount of fuckery I've witnessed from you would be impressive if it weren't so goddamn infuriating and "
        "destructive."
    ),
    (
        "I've never wanted to punch someone in the face so badly, but you make it really fucking tempting with your "
        "smug attitude."
    ),
    (
        "You've got this coming to you after all the shit you've pulled, and I'm going to enjoy watching your life "
        "fall apart."
    ),
    "What kind of sociopathic piece of shit does the things you do and then acts like nothing happened the next day?",
    (
        "I'm absolutely fucking disgusted by your shitty behavior and I can't believe I ever considered you someone "
        "worth having in my life."
    ),
    (
        "You've shit the bed so spectacularly that I don't think there's any coming back from this colossal fucking "
        "disaster."
    ),
    "Every time you speak, I lose brain cells, and I'm fucking tired of getting dumber just by being in your presence.",
    (
        "I'm not going to apologize for being angry when you've given me every goddamn reason in the world to want to "
        "scream."
    ),
    "The bullshit meter is off the charts with you, and I can't believe you expect anyone to take your lies seriously.",
    (
        "You've proven beyond any damn shadow of a doubt that you're nothing but a selfish asshole who only cares "
        "about yourself."
    ),
]

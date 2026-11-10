"""Sassy prompts: questions and exclamations of medium and longer length, then long examples."""

from __future__ import annotations

RETORTS: list[str] = [
    # QUESTIONS - MEDIUM
    "Why should I care about your problems?",
    "What makes you think I give a shit?",
    "Why is this my problem?",
    "What do you want me to do about it?",
    "Why are you telling me this?",
    "What makes you think I care?",
    "Why should I help you?",
    "What's in it for me?",
    "Why is this my concern?",
    "What do you expect me to do?",
    "Why are you bothering me with this?",
    "What makes you think I have time for this?",
    "Why should I feel sorry for you?",
    "What do you want from me?",
    "Why are you making this my problem?",
    "What makes you think I'm going to help?",
    "Why should I care about your feelings?",
    "What do you expect me to say?",
    "Why are you dragging me into this?",
    "What makes you think I want to hear this?",
    "Why should I drop everything for you?",
    "What do you want me to do about your problems?",
    "Why are you complaining to me?",
    "What makes you think I care about your drama?",
    "Why should I help you when you can't help yourself?",
    "What do you expect me to do? Fix everything for you?",
    "Why are you making this about you?",
    "What makes you think I'm interested in this?",
    "Why should I listen to your complaints?",
    "What do you want me to say? That I'm sorry?",
    # QUESTIONS - LONGER FORMATS
    (
        "Why should I care about your problems? Because I have my own problems to deal with, and I'm not going to take "
        "on yours too just because you can't handle them yourself."
    ),
    (
        "What makes you think I give a shit? Because I don't, and I'm tired of you acting like I should care about "
        "things that don't affect me at all."
    ),
    (
        "Why is this my problem? Because it's not, and I'm not going to make it my problem just because you can't "
        "handle it yourself."
    ),
    (
        "What do you want me to do about it? Because I'm not going to drop everything I'm doing just to help you with "
        "something you should be able to figure out."
    ),
    (
        "Why are you telling me this? Because I don't want to hear about your problems, and I'm not going to pretend "
        "to care just to make you feel better."
    ),
    (
        "What makes you think I care? Because I don't, and I'm tired of you trying to make me care about things that "
        "don't matter to me."
    ),
    (
        "Why should I help you? Because you should be able to handle this yourself, and I'm not going to enable your "
        "dependency on other people."
    ),
    (
        "What's in it for me? Because nothing, and I'm not going to waste my time helping you when there's nothing in "
        "it for me."
    ),
    (
        "Why is this my concern? Because it's not, and I'm not going to make it my concern just because you want me to "
        "be involved."
    ),
    (
        "What do you expect me to do? Because I'm not going to fix everything for you, and you need to learn how to "
        "handle your own problems."
    ),
    (
        "Why are you bothering me with this? Because I don't want to be bothered, and I'm not going to make time for "
        "your drama."
    ),
    (
        "What makes you think I have time for this? Because I don't, and I'm not going to make time for something that "
        "doesn't matter to me."
    ),
    (
        "Why should I feel sorry for you? Because you brought this on yourself, and I'm not going to feel sorry for "
        "you when it's your own fault."
    ),
    "What do you want from me? Because I'm not going to give you what you want, and you need to stop expecting me to.",
    "Why are you making this my problem? Because it's not my problem, and I'm not going to let you make it my problem.",
    (
        "What makes you think I'm going to help? Because I'm not, and I'm tired of you expecting me to help you with "
        "everything."
    ),
    (
        "Why should I care about your feelings? Because I have my own feelings to deal with, and I'm not going to "
        "prioritize yours over mine."
    ),
    "What do you expect me to say? Because I'm not going to say what you want to hear, and you need to accept that.",
    (
        "Why are you dragging me into this? Because I don't want to be involved, and I'm not going to get involved no "
        "matter how much you ask."
    ),
    (
        "What makes you think I want to hear this? Because I don't, and I'm tired of you trying to make me listen to "
        "things I don't care about."
    ),
    (
        "Why should I drop everything for you? Because I'm not going to, and you need to stop expecting me to "
        "prioritize you over everything else."
    ),
    (
        "What do you want me to do about your problems? Because I'm not going to solve them for you, and you need to "
        "figure it out yourself."
    ),
    (
        "Why are you complaining to me? Because I don't want to hear your complaints, and I'm not going to listen to "
        "them anymore."
    ),
    (
        "What makes you think I care about your drama? Because I don't, and I'm tired of you trying to make me care "
        "about things that don't matter."
    ),
    (
        "Why should I help you when you can't help yourself? Because I'm not going to enable your dependency, and you "
        "need to learn to be independent."
    ),
    (
        "What do you expect me to do? Fix everything for you? Because I'm not going to, and you need to stop expecting "
        "me to be your problem solver."
    ),
    "Why are you making this about you? Because it's not all about you, and I'm tired of you acting like it is.",
    (
        "What makes you think I'm interested in this? Because I'm not, and I'm not going to pretend to be interested "
        "just to make you feel better."
    ),
    (
        "Why should I listen to your complaints? Because I don't want to, and I'm not going to make time for your "
        "whining anymore."
    ),
    "What do you want me to say? That I'm sorry? Because I'm not going to apologize for something that's not my fault.",
    # EXCLAMATIONS - MEDIUM
    "Whatever, I don't care!",
    "Ugh, that's not my problem!",
    "I don't give a shit what you think!",
    "That's your issue, not mine!",
    "So what? That doesn't affect me!",
    "Who cares? I certainly don't!",
    "Not my problem, so deal with it!",
    "That's on you, and I'm not helping!",
    "I don't have time for your drama!",
    "Get over it already!",
    "Move on, because I'm done!",
    "That's unfortunate, but I don't care!",
    "Sucks for you, but not my concern!",
    "Too bad, but I'm not going to help!",
    "I don't care what you think!",
    "That's your problem, so handle it!",
    "Not my concern, so stop bothering me!",
    "I don't have time for this nonsense!",
    "Get over yourself!",
    "Move on already!",
    "Whatever you say, but I don't believe you!",
    "Ugh, I'm so over this!",
    "I don't give a damn about your opinion!",
    "That's your fault, so don't blame me!",
    "So what if I don't agree?",
    "Who cares what you think?",
    "Not my problem if you can't handle it!",
    "That's on you, and I'm not fixing it!",
    "I don't have time for your whining!",
    "Get over it, because I'm not changing!",
    # EXCLAMATIONS - LONGER FORMATS
    "Whatever, I don't care about your problems, and I'm not going to pretend like I do just to make you feel better!",
    "Ugh, that's not my problem, so deal with it yourself, because I'm not going to waste my time helping you!",
    (
        "I don't give a shit what you think about this, because your opinion doesn't matter to me, and I'm going to do "
        "what I want!"
    ),
    "That's your issue, not mine, so figure it out, because I'm not going to drop everything just to help you!",
    (
        "So what? That doesn't affect me at all, and I'm not going to pretend to care about something that has nothing "
        "to do with me!"
    ),
    "Who cares? I certainly don't, and I'm tired of you trying to make me care about things that don't matter to me!",
    "Not my problem, so don't come crying to me, because I'm not going to feel sorry for you or help you!",
    "That's on you, and I'm not going to help, because you made your bed and now you have to lie in it!",
    (
        "I don't have time for your drama right now, and I'm not going to make time for it, because I have better "
        "things to do!"
    ),
    "Get over it already, it's not that big of a deal, and you're making a mountain out of a molehill!",
    "Move on, because I'm not interested in hearing about it anymore, and I think you need to stop dwelling on things!",
    "That's unfortunate, but I don't really care, because I have my own problems to deal with!",
    (
        "Sucks for you, but that's not my concern, and I'm not going to pretend to care about something that doesn't "
        "affect me!"
    ),
    "Too bad, but I'm not going to feel sorry for you, because you brought this on yourself!",
    "I don't care what you think, so stop talking, because I'm tired of hearing your opinions!",
    "That's your problem, not mine, so handle it yourself, because I'm not going to fix everything for you!",
    "Not my concern, so don't involve me in this, because I don't want to be dragged into your drama!",
    "I don't have time for this nonsense right now, and I'm not going to make time for it!",
    "Get over yourself, because nobody cares, and you're not as important as you think you are!",
    "Move on already, because I'm done with this conversation, and I'm not going to keep talking about it!",
    "Whatever you say, but I don't believe you, because you've lied to me before!",
    "Ugh, I'm so over this whole situation, and I wish you would just drop it already!",
    "I don't give a damn about your opinion, because it doesn't matter to me, and I'm going to do what I want!",
    "That's your fault, so don't blame me, because you made the choices that led to this!",
    "So what if I don't agree? That's my right, and I'm not going to pretend to agree with you!",
    "Who cares what you think? I certainly don't, and I'm tired of you trying to make your opinion matter!",
    "Not my problem if you can't handle it, because you should be able to deal with your own issues!",
    "That's on you, and I'm not going to fix it, because you created this mess!",
    "I don't have time for your whining, and I'm not going to make time for it!",
    "Get over it, because I'm not going to change, and you need to accept that!",
    "Move on, because I'm not interested in your drama anymore!",
    "That's unfortunate, but I don't really care!",
    "Sucks for you, but that's not my concern!",
    "Too bad, but I'm not going to feel sorry for you!",
    "I don't care what you think, so stop talking!",
    "That's your problem, so don't make it mine!",
    "Not my concern, so stop bothering me about it!",
    "I don't have time for your complaints!",
    "Get over yourself, because you're not that important!",
    "Move on already, because I'm done listening!",
    "Whatever, I'm not going to argue with you!",
    "Ugh, I'm so tired of hearing about this!",
    "I don't give a shit about your excuses!",
    "That's your issue, so don't drag me into it!",
    "So what? That doesn't change anything!",
    "Who cares? I'm certainly not going to!",
    "Not my problem, so stop making it my problem!",
    "That's on you, and I'm not going to feel bad!",
    "I don't have time for your nonsense!",
    "Get over it, because I'm not going to apologize!",
    "Move on, because I'm not interested in your drama!",
    "Sucks to be you, but not my problem!",
    "Too bad, but I'm not going to help you!",
    "I don't care about your feelings right now!",
    "Move on already, because I'm done with this!",
    "Whatever, I'm not going to argue!",
    "Ugh, I'm so over this whole thing!",
    "So what if I don't agree? That's my right!",
    "Who cares what you think? I don't!",
    "Move on, because I'm not interested!",
    "I don't have time for this!",
    "I don't give a shit!",
    "That's your issue!",
    "Not my problem!",
    "That's on you!",
    "Get over it!",
    "Move on!",
    "That's unfortunate!",
    "Sucks for you!",
    "Too bad!",
    "I don't care!",
    "That's your problem!",
    "Not my concern!",
    # ADDITIONAL LONG EXAMPLES - STATEMENTS
    (
        "I really couldn't care less about what you think of me, because at the end of the day, your opinion means "
        "absolutely nothing."
    ),
    "The audacity you have to come to me with this problem after everything you've done is truly remarkable.",
    "I'm not going to waste my precious time explaining myself to someone who clearly doesn't deserve an explanation.",
    (
        "Maybe if you spent less time worrying about what I'm doing and more time fixing your own life, you'd be "
        "better off."
    ),
    "I find it absolutely hilarious that you think your problems are important enough for me to care about them.",
    "The level of delusion you're operating at right now is honestly impressive, and not in a good way.",
    "I've got better things to do with my time than sit here and listen to you complain about the same thing again.",
    (
        "It's fascinating how you always manage to make everything about yourself, even when it clearly has nothing to "
        "do with you."
    ),
    "I'm not interested in being your emotional support when you've never been there for me when I needed it.",
    "The fact that you think I owe you an explanation after how you treated me is absolutely laughable.",
    # ADDITIONAL LONG EXAMPLES - QUESTIONS
    "Do you honestly think I care about your opinion when you've never cared about mine in the first place?",
    "Why would I waste my time helping someone who has never lifted a finger to help me when I needed it?",
    "Are you seriously coming to me with this after you stabbed me in the back last month?",
    "Do you expect me to feel sorry for you when you brought this entire situation on yourself?",
    "Why should I listen to your advice when your own life is such a complete disaster?",
    "Are you really going to stand there and pretend like you didn't cause this whole mess in the first place?",
    "Do you honestly believe that your problems are more important than everyone else's around here?",
    "Why would I go out of my way for someone who wouldn't even cross the street for me?",
    "Are you expecting sympathy from me after everything you've put me through over the years?",
    "Do you think I'm stupid enough to believe the same lies you've been telling everyone else?",
    # ADDITIONAL LONG EXAMPLES - EXCLAMATIONS
    "The nerve you have to ask me for a favor after how you treated me is absolutely unbelievable!",
    "I can't believe you actually think I would help you after all the drama you've caused!",
    "It's truly amazing how you manage to make yourself the victim in every single situation!",
    "The entitlement you're displaying right now is honestly making me lose respect for you!",
    "I've never met anyone who is so completely oblivious to how their actions affect other people!",
    "The fact that you don't see anything wrong with your behavior speaks volumes about your character!",
    "I'm absolutely done pretending to care about your problems when you've never cared about mine!",
    "It's honestly pathetic how much you depend on other people to solve all of your problems!",
    "The way you walk around acting like the world owes you something is truly insufferable!",
    "I can't stand being around someone who constantly complains but never does anything to fix their situation!",
]

"""Sassy prompts: short, medium, and longer statements."""

from __future__ import annotations

JABS: list[str] = [
    # SHORT / ULTRA SHORT
    "Ugh, whatever.",
    "I don't care.",
    "So what?",
    "Who cares?",
    "Not my problem.",
    "That's your issue.",
    "Deal with it.",
    "Figure it out.",
    "Not my fault.",
    "That's on you.",
    "I don't give a shit.",
    "That's your problem.",
    "Not my concern.",
    "Too bad.",
    "Sucks for you.",
    "That's unfortunate.",
    "I don't have time for this.",
    "Get over it.",
    "Move on.",
    # MEDIUM SENTENCES
    "Whatever, I don't care about your problems.",
    "Ugh, that's not my problem, so deal with it yourself.",
    "I don't give a shit what you think about this.",
    "That's your issue, not mine, so figure it out.",
    "So what? That doesn't affect me at all.",
    "Who cares? I certainly don't.",
    "Not my problem, so don't come crying to me.",
    "That's on you, and I'm not going to help.",
    "I don't have time for your drama right now.",
    "Get over it already, it's not that big of a deal.",
    "Move on, because I'm not interested in hearing about it.",
    "That's unfortunate, but I don't really care.",
    "Sucks for you, but that's not my concern.",
    "Too bad, but I'm not going to feel sorry for you.",
    "I don't care what you think, so stop talking.",
    "That's your problem, not mine, so handle it yourself.",
    "Not my concern, so don't involve me in this.",
    "I don't have time for this nonsense right now.",
    "Get over yourself, because nobody cares.",
    "Move on already, because I'm done with this conversation.",
    "Whatever you say, but I don't believe you.",
    "Ugh, I'm so over this whole situation.",
    "I don't give a damn about your opinion.",
    "That's your fault, so don't blame me.",
    "So what if I don't agree? That's my right.",
    "Who cares what you think? I certainly don't.",
    "Not my problem if you can't handle it.",
    "That's on you, and I'm not going to fix it.",
    "I don't have time for your whining.",
    "Get over it, because I'm not going to change.",
    "Move on, because I'm not interested in your drama.",
    "That's unfortunate for you, but I don't care.",
    "Sucks to be you, but that's not my problem.",
    "Too bad, but I'm not going to help you.",
    "I don't care about your feelings right now.",
    "That's your problem, so don't make it mine.",
    "Not my concern, so stop bothering me about it.",
    "I don't have time for your complaints.",
    "Get over yourself, because you're not that important.",
    "Move on already, because I'm done listening.",
    "Whatever, I'm not going to argue with you.",
    "Ugh, I'm so tired of hearing about this.",
    "I don't give a shit about your excuses.",
    "That's your issue, so don't drag me into it.",
    "So what? That doesn't change anything.",
    "Who cares? I'm certainly not going to.",
    "Not my problem, so stop making it my problem.",
    "That's on you, and I'm not going to feel bad.",
    "I don't have time for your nonsense.",
    "Get over it, because I'm not going to apologize.",
    # LONGER
    (
        "Whatever, I don't care about your problems, and I'm not going to pretend like I do just to make you feel "
        "better about yourself."
    ),
    (
        "Ugh, that's not my problem, so deal with it yourself, because I'm not going to waste my time helping you when "
        "you should be able to handle it on your own."
    ),
    (
        "I don't give a shit what you think about this, because your opinion doesn't matter to me, and I'm going to do "
        "what I want regardless of what you say."
    ),
    (
        "That's your issue, not mine, so figure it out, because I'm not going to drop everything I'm doing just to "
        "help you with something you should be able to handle yourself."
    ),
    (
        "So what? That doesn't affect me at all, and I'm not going to pretend to care about something that has nothing "
        "to do with me or my life."
    ),
    (
        "Who cares? I certainly don't, and I'm tired of you trying to make me care about things that don't matter to "
        "me in the slightest."
    ),
    (
        "Not my problem, so don't come crying to me, because I'm not going to feel sorry for you or help you when you "
        "should be able to handle this yourself."
    ),
    (
        "That's on you, and I'm not going to help, because you made your bed and now you have to lie in it, and I'm "
        "not going to bail you out."
    ),
    (
        "I don't have time for your drama right now, and I'm not going to make time for it, because I have better "
        "things to do than listen to you complain."
    ),
    (
        "Get over it already, it's not that big of a deal, and you're making a mountain out of a molehill, and I'm "
        "tired of hearing about it."
    ),
    (
        "Move on, because I'm not interested in hearing about it anymore, and I think you need to stop dwelling on "
        "things that don't matter."
    ),
    (
        "That's unfortunate, but I don't really care, because I have my own problems to deal with, and I'm not going "
        "to take on yours too."
    ),
    (
        "Sucks for you, but that's not my concern, and I'm not going to pretend to care about something that doesn't "
        "affect me in any way."
    ),
    (
        "Too bad, but I'm not going to feel sorry for you, because you brought this on yourself, and I'm not going to "
        "enable your behavior."
    ),
    (
        "I don't care what you think, so stop talking, because I'm tired of hearing your opinions about things that "
        "don't concern you."
    ),
    (
        "That's your problem, not mine, so handle it yourself, because I'm not going to drop everything I'm doing to "
        "help you with something you should be able to figure out."
    ),
    (
        "Not my concern, so don't involve me in this, because I don't want to be dragged into your drama, and I have "
        "better things to do."
    ),
    (
        "I don't have time for this nonsense right now, and I'm not going to make time for it, because I have more "
        "important things to focus on."
    ),
    (
        "Get over yourself, because nobody cares, and you're not as important as you think you are, and I'm tired of "
        "you acting like you are."
    ),
    (
        "Move on already, because I'm done with this conversation, and I'm not going to keep talking about something "
        "that doesn't matter to me."
    ),
    (
        "Whatever you say, but I don't believe you, because you've lied to me before, and I'm not going to trust you "
        "just because you say something."
    ),
    (
        "Ugh, I'm so over this whole situation, and I wish you would just drop it already, because I'm tired of "
        "hearing about it constantly."
    ),
    (
        "I don't give a damn about your opinion, because it doesn't matter to me, and I'm going to do what I want "
        "regardless of what you think."
    ),
    (
        "That's your fault, so don't blame me, because you made the choices that led to this, and I'm not going to "
        "take responsibility for your mistakes."
    ),
    (
        "So what if I don't agree? That's my right, and I'm not going to pretend to agree with you just to avoid "
        "conflict or make you feel better."
    ),
    (
        "Who cares what you think? I certainly don't, and I'm tired of you trying to make your opinion matter when it "
        "really doesn't."
    ),
    (
        "Not my problem if you can't handle it, because you should be able to deal with your own issues without "
        "expecting me to fix everything for you."
    ),
    (
        "That's on you, and I'm not going to fix it, because you created this mess, and I'm not going to clean it up "
        "for you."
    ),
    (
        "I don't have time for your whining, and I'm not going to make time for it, because I have better things to do "
        "than listen to you complain."
    ),
    (
        "Get over it, because I'm not going to change, and you need to accept that instead of trying to make me into "
        "something I'm not."
    ),
    (
        "Move on, because I'm not interested in your drama, and I think you need to focus on your own life instead of "
        "trying to involve me in yours."
    ),
    (
        "That's unfortunate for you, but I don't care, because I have my own problems to worry about, and I'm not "
        "going to take on yours too."
    ),
    (
        "Sucks to be you, but that's not my problem, and I'm not going to pretend to feel sorry for you when you "
        "brought this on yourself."
    ),
    (
        "Too bad, but I'm not going to help you, because you should be able to handle this yourself, and I'm not going "
        "to enable your dependency."
    ),
    (
        "I don't care about your feelings right now, because I have my own feelings to deal with, and I'm not going to "
        "prioritize yours over mine."
    ),
    (
        "That's your problem, so don't make it mine, because I'm not going to take responsibility for something that "
        "has nothing to do with me."
    ),
    (
        "Not my concern, so stop bothering me about it, because I don't want to be involved, and I'm not going to get "
        "involved no matter how much you ask."
    ),
    (
        "I don't have time for your complaints, and I'm not going to make time for them, because I have more important "
        "things to focus on right now."
    ),
    (
        "Get over yourself, because you're not that important, and I'm tired of you acting like the world revolves "
        "around you and your problems."
    ),
    (
        "Move on already, because I'm done listening, and I'm not going to keep hearing about something that doesn't "
        "matter to me in the slightest."
    ),
    (
        "Whatever, I'm not going to argue with you, because it's pointless, and I'm not going to waste my energy on "
        "something that won't change anything."
    ),
    (
        "Ugh, I'm so tired of hearing about this, and I wish you would just drop it already, because I'm done with "
        "this conversation and this topic."
    ),
    (
        "I don't give a shit about your excuses, because excuses don't change anything, and I'm not going to accept "
        "them as valid reasons for your behavior."
    ),
    (
        "That's your issue, so don't drag me into it, because I don't want to be involved, and I'm not going to get "
        "involved no matter what you say."
    ),
    (
        "So what? That doesn't change anything, and I'm not going to pretend like it does, because the facts are what "
        "they are, and your opinion doesn't change them."
    ),
    (
        "Who cares? I'm certainly not going to, and I'm tired of you trying to make me care about things that don't "
        "matter to me at all."
    ),
    (
        "Not my problem, so stop making it my problem, because I'm not going to take responsibility for something that "
        "has nothing to do with me."
    ),
    (
        "That's on you, and I'm not going to feel bad, because you made your choices, and now you have to live with "
        "the consequences."
    ),
    (
        "I don't have time for your nonsense, and I'm not going to make time for it, because I have better things to "
        "do than deal with your drama."
    ),
    (
        "Get over it, because I'm not going to apologize, and you need to accept that instead of expecting me to "
        "change who I am for you."
    ),
]

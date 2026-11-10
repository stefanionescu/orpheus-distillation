"""Defensive prompts: short and medium denials, clarifications, and deflections, then long denials."""

from __future__ import annotations

DENIALS: list[str] = [
    # DENIAL - ULTRA SHORT
    "Wasn't me!",
    "Nope, wrong person.",
    "Absolutely not!",
    "Never happened.",
    "False accusation!",
    "Lies!",
    "Incorrect!",
    "Not guilty!",
    "Didn't do it!",
    "No way!",
    "Wrong!",
    "Nuh uh!",
    "Try again!",
    "Not true!",
    "As if!",
    # DENIAL - VARIED STARTERS
    "Hold on, that's completely inaccurate.",
    "Wait a second, let me set the record straight.",
    "Whoa whoa whoa, back up a minute here.",
    "Excuse me, but that's not even close to reality.",
    "Hang on, where is this coming from?",
    "Actually, check your facts before accusing me.",
    "Look, I can explain exactly what happened.",
    "Listen, there's been some kind of misunderstanding here.",
    "See, this is what actually went down.",
    "First of all, get your story straight.",
    "Okay, clearly there's been some miscommunication.",
    "Right, so let me clarify something real quick.",
    "Seriously, whoever told you that was wrong.",
    "Honestly, I have no idea where you got that from.",
    "Genuinely confused about where this is coming from.",
    # CLARIFICATION - SHORT
    "Let me be crystal clear here.",
    "Allow me to explain the situation.",
    "There's context you're missing.",
    "Here's what really happened.",
    "The full story is different.",
    "Context matters here.",
    "There's more to this.",
    "Hear me out first.",
    "Give me a chance to explain.",
    "The truth is much simpler.",
    "Facts don't support that claim.",
    "Evidence proves otherwise.",
    "Reality tells a different story.",
    "Circumstances were different.",
    "Situation was more complex.",
    # DEFLECTION - VARIED
    "Why am I suddenly the bad guy here?",
    "Since when is this my fault?",
    "How did this become about me?",
    "Pretty convenient to blame me, huh?",
    "Easy target, I guess.",
    "Everyone needs a scapegoat apparently.",
    "Classic deflection onto me.",
    "Sure, make me the villain.",
    "Always easier to point fingers.",
    "Funny how blame always lands here.",
    "Of course it's my fault, it's always my fault.",
    "Right, because everything is always on me.",
    "Naturally, I'm the problem again.",
    "Shocking, I'm getting blamed once more.",
    "Color me surprised, another accusation.",
    # CHALLENGING THE ACCUSATION
    "Where's your proof of that?",
    "Show me the evidence.",
    "What basis do you have for saying that?",
    "Got any receipts to back that up?",
    "On what grounds are you accusing me?",
    "Says who exactly?",
    "According to whom?",
    "Based on what information?",
    "Prove it then.",
    "Back that claim up.",
    "Source, please?",
    "Who told you that nonsense?",
    "Where'd you hear that garbage?",
    "What's your evidence?",
    "Citation needed on that one.",
    # EXPRESSING FRUSTRATION
    "This is getting ridiculous now.",
    "Unbelievable that we're even having this conversation.",
    "Beyond frustrated with these accusations.",
    "Tired of defending myself constantly.",
    "Exhausted from explaining the obvious.",
    "Fed up with being blamed for everything.",
    "So sick of this narrative.",
    "Done with these baseless claims.",
    "Over it, completely over it.",
    "Can't win no matter what I do.",
    "Damned if I do, damned if I don't.",
    "Nothing I say matters apparently.",
    "My words get twisted no matter what.",
    "Everything I do gets misinterpreted.",
    "Speaking feels pointless at this point.",
    # SETTING BOUNDARIES
    "Back off with the accusations.",
    "Stop putting words in my mouth.",
    "Quit twisting what I said.",
    "Don't assume you know my intentions.",
    "Enough with the character assassination.",
    "Cease the unfounded allegations.",
    "Knock it off with the blame game.",
    "Cut the hostile questioning.",
    "Drop the accusatory tone.",
    "Ease up on the judgment.",
    "Lay off the criticism.",
    "Rein in the assumptions.",
    "Check yourself before accusing others.",
    "Think before you speak on this.",
    "Consider the facts before judging.",
    # EXPLAINING INTENT
    "My intentions were completely different.",
    "That wasn't the goal at all.",
    "The purpose was something else entirely.",
    "Motivation behind it was pure.",
    "Reasons for doing that were valid.",
    "Logic made sense at the time.",
    "Thought process was sound.",
    "Decision was made carefully.",
    "Actions had good reasoning.",
    "Choices reflected my values.",
    "Behavior was justified given circumstances.",
    "Response was appropriate then.",
    "Reaction was warranted.",
    "Approach seemed right.",
    "Method was the best option available.",
    # MEDIUM - DENIAL STATEMENTS
    (
        "Absolutely did not say those words, and anyone claiming otherwise is either lying or severely misremembering "
        "the conversation."
    ),
    "Never in my life have I done what you're accusing me of, and I'm frankly insulted by the suggestion.",
    "Categorically deny every single allegation being thrown at me right now, because none of it is accurate.",
    "Completely reject the premise of your accusation, since it's based on false information from the very start.",
    "Totally innocent of whatever you think I did, and I can prove it if you'll actually listen.",
    "One hundred percent did not do that, and I resent the implication that I would even consider it.",
    "Under no circumstances would I ever do something like that, and the fact you'd suggest it hurts.",
    "Nothing about that accusation is true, not one single detail, and I'm prepared to defend myself.",
    "Zero truth to what you're claiming, absolutely zero, and I need you to understand that clearly.",
    "False from start to finish, every word of that accusation is completely fabricated or distorted.",
    "Couldn't be further from the truth if you tried, like you're describing a completely different person.",
    "Patently absurd to even suggest such a thing, and I expected better from you honestly.",
    "Ridiculous allegation that doesn't deserve a response, but I'll dignify it with one anyway unfortunately.",
    "Outrageous claim with absolutely no basis in reality, and I'm offended you'd even bring it up.",
    "Baseless attack on my character that I won't tolerate, not from you or anyone else making accusations.",
    # MEDIUM - QUESTIONS
    "What exactly are you basing this accusation on, because from where I'm standing, the evidence doesn't exist?",
    "Where did you even get this information from, because whoever told you that was completely wrong?",
    "How can you possibly believe that about me after everything we've been through together over time?",
    "Why would I ever do something like that when it goes against everything I stand for as a person?",
    "Who's been feeding you these lies about me, because I'd really like to have a conversation with them?",
    "When did I ever give you reason to think so poorly of me and my intentions toward you?",
    "Do you honestly believe I'm capable of something like that, or are you just looking for someone to blame?",
    "Have you considered that maybe, just maybe, you've got the wrong person or the wrong interpretation?",
    "Are you absolutely certain you want to go down this road with me, because I will defend myself?",
    "Can we talk about what actually happened instead of what you've imagined or been told by others?",
    "Would you like to hear my side of the story before you continue throwing accusations around carelessly?",
    "Did it occur to you to ask me directly before assuming the worst about my actions and intentions?",
    "Is there any way to convince you that you've got this completely wrong from start to finish?",
    "Shouldn't you verify your facts before making such serious accusations against someone you know personally?",
    "Don't you think I deserve a chance to explain myself before you pass judgment on me so harshly?",
    # MEDIUM - EXCLAMATIONS
    "Unreal that you would even suggest something like that, after everything I've done for you and others!",
    "Incredible that this is the conclusion you've jumped to without even bothering to ask me first!",
    "Amazing how quickly you believed the worst about me without any concrete evidence to support it!",
    "Stunning display of distrust from someone I thought knew me better than to believe such nonsense!",
    "Remarkable that you'd throw these accusations around without considering how much damage they could cause me!",
    "Astonishing lack of faith in my character after all the time we've spent getting to know each other!",
    "Outrageous treatment of someone who has never given you any reason to doubt their integrity before!",
    "Appalling that you'd believe gossip and rumors over directly asking me for the actual truth here!",
    "Disgraceful way to treat someone who has always been honest and upfront with you about everything!",
    "Shameful accusations being thrown around without a shred of evidence to back any of them up!",
    "Insulting to my intelligence that you think I wouldn't notice the holes in your accusation story!",
    "Offensive suggestion that I would ever compromise my values in the way you're implying right now!",
    "Hurtful to hear these things from someone I trusted with so much of my personal life!",
    "Painful accusations that cut deep, especially coming from someone who claims to care about me!",
    "Devastating to realize you think so little of me that you'd believe this garbage being spread!",
    # LONG - DENIAL WITH CONTEXT
    (
        "Let me be absolutely clear about this situation, because I refuse to let false narratives take hold when I "
        "know the truth and can prove what actually happened."
    ),
    (
        "Flatly reject every aspect of what you're accusing me of, and I'm prepared to go through each point "
        "systematically to show you where you've gotten it wrong."
    ),
    (
        "Standing here being accused of something I categorically did not do is incredibly frustrating, especially "
        "when I have evidence that completely contradicts your version of events."
    ),
    (
        "Never in a million years would I do what you're suggesting, and the fact that you'd even consider me capable "
        "of it shows you don't really know me at all."
    ),
    (
        "My track record speaks for itself, and I challenge you to find a single instance where I've behaved in the "
        "way you're currently accusing me of behaving."
    ),
    (
        "Firmly maintain my innocence in this matter, and I'm not going to back down or apologize for something I "
        "simply did not do, no matter the pressure."
    ),
    (
        "The accusation you're making is so far removed from reality that I genuinely don't know where to begin "
        "unpacking all the ways you've gotten this wrong."
    ),
    (
        "Whoever fed you this information either has an agenda against me or is seriously confused about what actually "
        "transpired, because that's not even close to accurate."
    ),
    (
        "Prepared to defend my name against these baseless allegations, and I won't rest until the truth comes out and "
        "my reputation is restored to what it should be."
    ),
    (
        "Absolutely floored by the audacity of these accusations, considering I have multiple witnesses who can "
        "confirm I was nowhere near the situation you're describing."
    ),
    (
        "Taking these allegations extremely seriously, which is exactly why I'm demanding a thorough investigation "
        "that will prove once and for all that I'm telling the truth."
    ),
    (
        "Challenging you to produce a single piece of concrete evidence supporting your claims, because I know for a "
        "fact that no such evidence exists anywhere."
    ),
    (
        "My conscience is completely clear regarding this matter, and I can look you straight in the eye and tell you "
        "without hesitation that I did nothing wrong."
    ),
    (
        "Fighting back against these unfair characterizations of my actions, because staying silent would only make "
        "people think there's truth to these ridiculous claims."
    ),
    (
        "Demanding the opportunity to present my side of the story in full, without interruption, so everyone can see "
        "just how distorted these accusations really are."
    ),
    # LONG - EXPLAINING CIRCUMSTANCES
    (
        "The situation was far more complicated than you're making it out to be, and if you'd let me explain the full "
        "context, you'd understand why I made the decisions I did."
    ),
    (
        "Circumstances at the time left me with very few options, and I chose what I genuinely believed was the best "
        "course of action given the information I had available."
    ),
    (
        "Before you judge me too harshly, consider that you're seeing this situation from the outside without any "
        "knowledge of the pressures and constraints I was dealing with internally."
    ),
    (
        "Context is everything here, and you're missing some crucial pieces of information that would completely "
        "change how you interpret my actions if you only knew the full story."
    ),
    (
        "What you're describing as malicious was actually an attempt to help that unfortunately went sideways, and I "
        "feel terrible about the outcome even though my intentions were good."
    ),
    (
        "The version of events you've heard is clearly missing some key details, because if you knew what was really "
        "happening behind the scenes, your perspective would shift dramatically."
    ),
    (
        "My actions might look questionable in hindsight, but at the moment I was operating with limited information "
        "and trying to make the best possible decision under extreme pressure."
    ),
    (
        "People love to judge decisions from the comfort of knowing how things turned out, but in the moment, I had to "
        "choose without knowing what the consequences would be."
    ),
    (
        "Everything I did was in response to a situation that was rapidly deteriorating, and I was trying to prevent "
        "an even worse outcome that nobody seems to appreciate now."
    ),
    (
        "The full picture is much more nuanced than the simplified version being presented, and I think fairness "
        "demands that we examine all the relevant factors before assigning blame."
    ),
    (
        "My reasoning at the time was sound based on what I knew, and I refuse to be judged by standards that only "
        "make sense with the benefit of hindsight and full information."
    ),
    (
        "Anyone in my position facing the same circumstances would have made similar choices, and I resent being "
        "singled out as if I had better options that I willfully ignored."
    ),
    (
        "The pressure I was under to make a quick decision is something you can't possibly understand unless you were "
        "there experiencing it firsthand like I was at that moment."
    ),
    (
        "What looked like a straightforward situation from the outside was actually incredibly complex with competing "
        "interests and no clear right answer, just varying degrees of imperfect solutions."
    ),
    (
        "Before condemning my choices, walk a mile in my shoes and see if you could have done any better with the same "
        "constraints and incomplete information I was working with."
    ),
]

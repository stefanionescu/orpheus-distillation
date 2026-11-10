"""Multi-sentence prompts about life situations, technology, and relationships."""

from __future__ import annotations

SITUATIONS: list[str] = [
    # LIFE SITUATIONS (~22 WORDS AVG)
    (
        "The moving truck arrives tomorrow and I'm nowhere near ready. Boxes everywhere, nothing labeled properly, and "
        "I still haven't found my passport."
    ),
    (
        "We finally closed on the house after three months of negotiations. The relief is immense but now the real "
        "work of making it a home begins."
    ),
    (
        "The diagnosis came back negative, which was the best news I've received all year. The waiting period was "
        "absolute torture though."
    ),
    (
        "My flight got canceled due to mechanical issues. Now I'm stranded at the airport for at least six hours with "
        "a dead laptop battery."
    ),
    (
        "The wedding planning has taken over our entire lives for months now. I'll be relieved when it's over and we "
        "can just be married."
    ),
    (
        "The job offer came through but it requires relocating across the country. We have two weeks to decide whether "
        "to uproot everything."
    ),
    (
        "The basement flooded during last night's storm. We've been shop vacuuming water since five in the morning "
        "with no end in sight."
    ),
    (
        "My teenage daughter hasn't spoken to me in three days over something I said. The silent treatment is more "
        "painful than any argument."
    ),
    (
        "The contractor just informed us the renovation will take an additional eight weeks. We've already been living "
        "with my parents for two months."
    ),
    (
        "The fertility treatments aren't working and each failed attempt takes an emotional toll. We're running out of "
        "options and hope simultaneously."
    ),
    (
        "My elderly mother called confused about where she was again. These episodes are becoming more frequent and "
        "I'm terrified about what comes next."
    ),
    (
        "The company announced layoffs and my entire department is being restructured. I find out tomorrow whether I "
        "still have a position here."
    ),
    (
        "The college acceptance letter arrived today. Four years of hard work have finally paid off and the future "
        "suddenly looks bright."
    ),
    (
        "My car broke down on the highway during rush hour traffic. I'm waiting for the tow truck in ninety degree "
        "heat with no water."
    ),
    (
        "The custody hearing is next week and I'm preparing for the worst. The lawyer says our case is strong but "
        "nothing feels certain."
    ),
    (
        "We adopted a puppy last weekend and I severely underestimated the commitment involved. Sleep deprivation is "
        "real even with a dog."
    ),
    (
        "The identity theft has been a nightmare to resolve. Six months later and I'm still dealing with fraudulent "
        "accounts in my name."
    ),
    (
        "My best friend's wedding is the same day as my sister's baby shower. No matter what I choose, someone "
        "important will be hurt."
    ),
    (
        "The promotion I was passed over for went to someone with half my experience. I'm trying not to be bitter but "
        "it's difficult."
    ),
    (
        "We're planning our first family vacation in five years. The logistics of coordinating everyone's schedules "
        "has been a full time job."
    ),
    # TECHNOLOGY & MODERN LIFE (~22 WORDS AVG)
    (
        "My smart home system has developed a mind of its own lately. The lights turn on randomly and the thermostat "
        "does whatever it wants."
    ),
    (
        "The software update broke features that were working perfectly fine before. Now I have to relearn how to do "
        "basic tasks I've done for years."
    ),
    (
        "I've been on hold with customer service for forty five minutes now. The elevator music is slowly driving me "
        "toward a complete mental breakdown."
    ),
    (
        "The cloud storage company is raising prices again. At this point I'm paying more monthly than I did for "
        "physical storage solutions."
    ),
    (
        "My video doorbell captured footage of someone stealing our packages. The resolution is just clear enough to "
        "be frustrating but not identifying."
    ),
    (
        "The dating app algorithm keeps suggesting people who are completely wrong for me. Either the technology is "
        "broken or I've misrepresented myself entirely."
    ),
    (
        "The wireless printer refuses to connect no matter what troubleshooting steps I follow. Technology was "
        "supposed to make life easier, not infinitely more frustrating."
    ),
    (
        "My social media feed has become an echo chamber of the same perspectives. The algorithm knows what I like but "
        "not what I need."
    ),
    (
        "The navigation app sent me down a road that clearly doesn't exist anymore. Now I'm lost in an industrial area "
        "with no cell signal."
    ),
    (
        "The subscription model for software I used to own outright is genuinely infuriating. I'm paying monthly for "
        "tools I purchased years ago."
    ),
    (
        "My fitness tracker says I slept terribly but I feel completely rested. I'm starting to trust my body more "
        "than the device strapped to it."
    ),
    (
        "The autocorrect changed my professional email into something embarrassing before I noticed. Apologizing for "
        "technology failures has become a regular occurrence."
    ),
    (
        "The targeted ads know things about me that I haven't told anyone. The level of data collection is both "
        "impressive and deeply unsettling."
    ),
    (
        "My phone screen cracked from a two foot drop onto carpet somehow. The repair cost is almost as much as buying "
        "a new device."
    ),
    (
        "The spam calls have become relentless despite every blocking measure I've tried. My phone is barely usable "
        "for its original purpose anymore."
    ),
    (
        "The website crashed during checkout and now I'm not sure if my order went through. My credit card was charged "
        "but no confirmation arrived."
    ),
    (
        "My teenager's screen time report would concern any parent. We're negotiating new boundaries but the arguments "
        "are exhausting for everyone involved."
    ),
    (
        "The electric vehicle's range anxiety is real despite what the enthusiasts claim. I calculated wrong and "
        "barely made it to the charging station."
    ),
    (
        "The smart speaker misheard my request and ordered something I didn't want. Now I have to deal with returning "
        "a product I never intended to buy."
    ),
    (
        "The deepfake technology has made me paranoid about every video I see online. Verifying reality has become "
        "increasingly difficult and time consuming."
    ),
    # INTERPERSONAL DYNAMICS (~22 WORDS AVG)
    (
        "The tension between my mother and my wife is becoming unbearable. I'm constantly mediating conflicts that "
        "have nothing to do with me directly."
    ),
    (
        "My roommate's passive aggressive notes have escalated to a new level. I found a laminated poster about dish "
        "etiquette taped to the refrigerator."
    ),
    (
        "The coworker who takes credit for my ideas did it again in front of leadership. Documenting everything from "
        "now on seems necessary."
    ),
    (
        "My friend group has split into factions after the breakup. Staying neutral while maintaining all the "
        "relationships is exhausting balancing work."
    ),
    (
        "The neighbor's music plays until three in the morning every weekend. My polite requests have been ignored and "
        "I'm considering more formal complaints."
    ),
    (
        "My sibling borrowed money eighteen months ago and hasn't mentioned repayment once. Bringing it up feels "
        "awkward but the amount isn't trivial."
    ),
    (
        "The person I've been mentoring has started to outperform me in certain areas. My pride and my genuine "
        "happiness for them coexist uneasily."
    ),
    (
        "My ex and I share custody drop offs in awkward silence. We were together for eight years and now we're "
        "strangers with a child."
    ),
    (
        "The family group chat has become a battleground for political arguments. I've muted notifications but the "
        "damage to relationships continues."
    ),
    (
        "My colleague's perfume is triggering my migraines. How do you tell someone their personal choices are causing "
        "you physical pain politely?"
    ),
    (
        "The friend who only calls when they need something reached out again. Part of me wants to help; part of me "
        "feels used."
    ),
    (
        "My partner's family has different boundaries than mine about everything. Learning to navigate their "
        "expectations without losing myself has been challenging."
    ),
    (
        "The person who bullied me in high school sent a friend request. I'm not sure if they want to apologize or "
        "just collect connections."
    ),
    (
        "My elderly neighbor relies on me for errands but the requests have become overwhelming. Setting limits feels "
        "heartless given her isolation."
    ),
    (
        "The competitive parent at my kid's school makes every activity stressful. Soccer practice shouldn't involve "
        "this much interpersonal drama."
    ),
    (
        "My therapist pointed out a pattern in my relationships I hadn't noticed before. Now I see it everywhere and "
        "can't unsee it."
    ),
    (
        "The friend who always cancels last minute did it again today. At what point do patterns become too consistent "
        "to ignore anymore?"
    ),
    (
        "My boss plays favorites and I'm not among the chosen. The workplace dynamics make every interaction feel "
        "loaded with unspoken politics."
    ),
    (
        "The couple we're friends with is getting divorced and both want us to take sides. Maintaining both "
        "friendships may not be possible."
    ),
    (
        "My parent's new partner is closer to my age than theirs. Processing complicated feelings about family "
        "configurations I never anticipated having."
    ),
]

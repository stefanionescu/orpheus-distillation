"""Multi-sentence prompts: longer explanations, advice, questions, and stories."""

from __future__ import annotations

EXPLANATIONS: list[str] = [
    # LONGER CONVERSATIONAL - EXPLANATIONS (~25 WORDS AVG)
    (
        "The reason I've been so distracted lately is that we're dealing with a complicated family situation. It "
        "requires a lot of mental energy and emotional bandwidth to navigate."
    ),
    (
        "I should probably explain why I reacted so strongly earlier. It has everything to do with past experiences "
        "and very little to do with what you actually said."
    ),
    (
        "The project is behind schedule primarily because the initial requirements kept changing every week. Making it "
        "nearly impossible to build momentum or maintain consistent progress toward completion."
    ),
    (
        "My reluctance to commit to plans far in advance stems from too many experiences of circumstances changing "
        "unexpectedly. Having to cancel things I was genuinely looking forward to."
    ),
    (
        "The reason that restaurant is always so crowded despite mediocre food is their location and marketing. It "
        "proves that perception often matters more than actual quality."
    ),
    (
        "I didn't respond to your message immediately because I wanted to give it the thoughtful reply it deserved. "
        "Rather than firing off something hasty I might later regret."
    ),
    (
        "The complexity of the situation is difficult to convey briefly. Essentially there are competing interests "
        "that have made finding a solution acceptable to everyone nearly impossible."
    ),
    (
        "My hesitation about accepting the offer isn't about the opportunity itself but about the timing. Given "
        "everything else currently demanding attention in my personal and professional life."
    ),
    (
        "The tradition started somewhat accidentally years ago and has simply persisted. No one wanted to be the "
        "person who broke the chain by suggesting we stop."
    ),
    (
        "I've been avoiding that topic because I honestly don't have a satisfying answer yet. I'd rather wait until "
        "I've figured out my actual position before discussing it."
    ),
    (
        "The difference between the two approaches is subtle but significant. It affects everything from initial "
        "implementation costs to long term maintenance requirements and scalability potential."
    ),
    (
        "My investment in this outcome probably seems disproportionate from the outside. But there's important context "
        "about what this represents symbolically that I haven't fully explained yet."
    ),
    (
        "The challenge with that solution is that it addresses the symptoms without tackling the underlying cause. "
        "We'll likely find ourselves dealing with similar problems again soon."
    ),
    (
        "I realize my behavior lately has been confusing, and I owe you an explanation. I've been reluctant to give it "
        "because it requires admitting some uncomfortable truths."
    ),
    (
        "The reason healthcare costs keep increasing involves a complicated intersection of insurance structures and "
        "pharmaceutical pricing. Plus administrative overhead and demographic shifts that no single policy addresses."
    ),
    (
        "My preference for working alone isn't antisocial at all. It's based on understanding that my most productive "
        "work happens when I'm not managing interpersonal dynamics."
    ),
    (
        "The mechanism behind that phenomenon is actually fascinating once you understand the basic physics involved. "
        "I'll spare you the technical details unless you're genuinely interested."
    ),
    (
        "I should clarify that my previous statement wasn't meant as criticism but as observation. I understand how "
        "the phrasing could have been interpreted less charitably than intended."
    ),
    (
        "The distinction between those two concepts matters because conflating them leads to fundamentally flawed "
        "conclusions. And policies that address the wrong problems with the wrong interventions entirely."
    ),
    (
        "My unusual approach to that problem developed after conventional methods failed repeatedly. I was forced to "
        "experiment with alternatives until I stumbled onto something that actually worked."
    ),
    # LONGER CONVERSATIONAL - ADVICE & WISDOM (~25 WORDS AVG)
    (
        "If there's one thing I've learned from experience, it's that most problems seem much more insurmountable at "
        "night. They look different after good sleep and fresh perspective."
    ),
    (
        "The best advice I ever received was to focus on what I can control. And release attachment to outcomes that "
        "depend on factors entirely beyond my influence."
    ),
    (
        "Something I wish someone had told me earlier is that it's perfectly acceptable to outgrow friendships and "
        "interests. Even versions of yourself, without any guilt owed."
    ),
    (
        "The key to maintaining long term relationships isn't avoiding conflict. It's learning how to navigate "
        "disagreements in ways that ultimately strengthen rather than erode trust."
    ),
    (
        "One insight that genuinely changed my approach to work is that being effective matters far more than being "
        "busy. The two are frequently inversely correlated actually."
    ),
    (
        "If you're struggling with a decision, try imagining what advice you would give a close friend facing the same "
        "situation. Then follow that guidance yourself."
    ),
    (
        "The most valuable skill I've developed is the ability to sit with discomfort without immediately trying to "
        "fix or escape it. It sounds simple but requires practice."
    ),
    (
        "Something worth remembering is that people's reactions often say more about their internal state. It's rarely "
        "about what you said or did to trigger them."
    ),
    (
        "The secret to getting things done consistently is making the desired behavior the path of least resistance. "
        "Through environmental design rather than relying solely on willpower."
    ),
    (
        "One perspective shift that helped me enormously was realizing that asking for help is a sign of self "
        "awareness and strength. Not weakness as I previously believed."
    ),
    (
        "The most underrated life skill is learning to tolerate boredom. The inability to do so drives so many "
        "destructive behaviors and poor decisions people later regret."
    ),
    (
        "The people who complain most about lack of time are often the same ones who struggle to say no to new "
        "commitments. I've observed this repeatedly."
    ),
    (
        "If you want to understand someone's true priorities, don't listen to what they say matters to them. Observe "
        "where they actually invest their time and resources."
    ),
    (
        "The difference between people who achieve their goals and those who don't often comes down to consistency "
        "over intensity. Showing up regularly rather than sporadically."
    ),
    (
        "You're never too old to change direction, learn something new, or become a different version of yourself. One "
        "thing worth internalizing is that growth never stops."
    ),
    (
        "The fastest way to feel better about your own life is to stop comparing yourself to others. Their social "
        "media shows curated highlights, not their complete picture."
    ),
    (
        "Boundaries aren't walls but rather the fences that make good relationships possible. They define where you "
        "end and others begin. Something that took me too long to learn."
    ),
    (
        "If you're constantly exhausted despite adequate sleep, something deeper might be wrong. Consider whether "
        "you're expending energy maintaining roles that no longer serve your wellbeing."
    ),
    (
        "The most important conversation you'll ever have is the ongoing one with yourself. Which is why cultivating a "
        "kinder and more compassionate internal voice matters profoundly."
    ),
    (
        "The things we resist most often contain exactly the growth and transformation we need. That's precisely why "
        "they feel so threatening to us to begin with."
    ),
    # LONGER CONVERSATIONAL - QUESTIONS & PONDERINGS (~25 WORDS AVG)
    (
        "Have you ever wondered what your life would look like now if you'd made different choices? Those few crucial "
        "turning points seemed so momentous at the time."
    ),
    (
        "I keep thinking about whether our current approach is actually effective. Or whether we've simply continued "
        "doing things this way because it's familiar and comfortable."
    ),
    (
        "Do you think people fundamentally change throughout their lives? Or do you believe our core personalities are "
        "essentially fixed by the time we reach adulthood?"
    ),
    (
        "I'm curious whether the constant connectivity we now consider normal is genuinely enriching our lives. Or "
        "whether we're collectively participating in an experiment with unknown consequences."
    ),
    (
        "Have you noticed how differently people respond to uncertainty? Some find it paralyzing while others seem to "
        "thrive in ambiguity and embrace not knowing what comes next."
    ),
    (
        "I sometimes wonder whether the things I worry about most are actually the things most likely to happen. Or "
        "whether I'm expending energy on entirely unlikely scenarios."
    ),
    (
        "Do you ever question whether the goals you're pursuing are genuinely your own? Or whether you've "
        "unconsciously absorbed expectations from family and society about success?"
    ),
    (
        "I've been pondering whether the discomfort I feel about that situation is trying to tell me something "
        "important. Or whether I'm simply resistant to change naturally."
    ),
    (
        "Have you ever considered how much of your personality is innate versus shaped by specific circumstances? The "
        "relationships and environments you happened to encounter growing up?"
    ),
    (
        "I keep wondering whether we place too much emphasis on romantic relationships as the primary source of "
        "fulfillment. While undervaluing friendships and community bonds significantly."
    ),
    (
        "Do you think there's an objective way to measure whether you're living a meaningful life? Or is meaning "
        "entirely subjective and defined differently by each person?"
    ),
    (
        "I'm genuinely uncertain whether the feelings I have about this situation are valid intuitions worth heeding. "
        "Or irrational fears that will dissipate once I push through."
    ),
    (
        "Have you ever thought about what skills or knowledge will actually matter in twenty years? Versus what we're "
        "currently prioritizing in education and professional development now?"
    ),
    (
        "I sometimes question whether my desire for stability is a healthy preference or an avoidance of growth. The "
        "kind that only comes through embracing uncertainty."
    ),
    (
        "Do you find that the questions you ask yourself have evolved significantly over time? Reflecting different "
        "priorities and concerns at various stages of your life journey?"
    ),
    # LONGER CONVERSATIONAL - STORYTELLING (~25 WORDS AVG)
    (
        "So there I was, standing in the middle of the airport with no luggage and a dead phone. The airline had "
        "completely lost track of my connecting flight somehow."
    ),
    (
        "The strangest thing happened at the grocery store today. A woman approached me convinced we'd met at a "
        "wedding three years ago, but I've never seen her before."
    ),
    (
        "Let me tell you about the time my car broke down in the middle of nowhere at two in the morning. No cell "
        "service, no passing cars for hours."
    ),
    (
        "You won't believe what my neighbor did last weekend. She built an entire greenhouse in her backyard using "
        "only reclaimed materials from construction sites around town."
    ),
    (
        "I met the most fascinating person on the train yesterday. A retired archaeologist who spent thirty years "
        "excavating sites across the Middle East and had incredible stories."
    ),
    (
        "The dinner party started out perfectly normal until someone brought up politics around dessert. Within "
        "minutes, two guests who'd been friends for decades weren't speaking to each other."
    ),
    (
        "Picture this: I'm giving the most important presentation of my career, and suddenly the power goes out in the "
        "entire building. Complete darkness and awkward silence everywhere."
    ),
    (
        "My grandmother used to tell this story about immigrating here with nothing but a small suitcase. The "
        "resilience of that generation never ceases to amaze me honestly."
    ),
    (
        "There's this coffee shop I discovered completely by accident last month. Hidden down an alley that I'd walked "
        "past hundreds of times without ever noticing the entrance."
    ),
    (
        "The camping trip took an unexpected turn when we realized bears had gotten into our food supplies overnight. "
        "We spent the next three days surviving on granola bars."
    ),
    (
        "I still laugh about the time I showed up to a costume party that wasn't actually a costume party. Everyone "
        "else was in formal attire while I wore a dinosaur suit."
    ),
    (
        "The best meal I ever had was in this tiny village restaurant in Italy. The owner didn't speak English and I "
        "didn't speak Italian, but somehow we communicated perfectly."
    ),
    (
        "My first day at that job was a complete disaster from start to finish. I got lost in the building, called my "
        "boss by the wrong name twice."
    ),
    (
        "Let me paint the scene for you. It's pouring rain, I've just missed the last bus home, and my umbrella "
        "chooses that exact moment to turn inside out."
    ),
    (
        "The road trip we took after graduation remains one of my fondest memories. Three weeks driving through places "
        "we'd only read about, sleeping in the car most nights."
    ),
]

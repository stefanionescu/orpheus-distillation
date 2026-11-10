"""Multi-sentence prompts: longer talk about worries, gratitude, curiosities, and comparisons."""

from __future__ import annotations

WORRIES: list[str] = [
    # LONGER CONVERSATIONAL - WORRIES & CONCERNS (~25 WORDS AVG)
    (
        "I've been losing sleep over this decision because both options have significant downsides. There's no clear "
        "right answer and the stakes feel uncomfortably high right now."
    ),
    (
        "The uncertainty about the future feels particularly acute right now. So many variables are outside my control "
        "and the possible outcomes range from great to terrible."
    ),
    (
        "I'm worried about the direction things are heading, both personally and in the wider world. That anxiety "
        "colors everything even when I try to stay optimistic."
    ),
    (
        "The conversation we need to have keeps getting postponed because neither of us wants to face the potential "
        "fallout. Avoidance is making everything worse though."
    ),
    (
        "My health has been on my mind more than usual lately. Small symptoms that probably mean nothing but keep "
        "nagging at the back of my thoughts constantly."
    ),
    (
        "The financial situation isn't dire but it's tighter than I'd like it to be. Every unexpected expense sends a "
        "ripple of stress through the rest of the month."
    ),
    (
        "I'm concerned that I'm not doing enough to prepare for what's coming. Whatever that is, because honestly I'm "
        "not even sure what I should be preparing for."
    ),
    (
        "The relationship strain has been building for a while and I'm not sure how to address it constructively. "
        "Every approach I consider seems likely to backfire somehow."
    ),
    (
        "I worry that I've made promises I can't actually keep. The gap between what I committed to and what I can "
        "deliver is becoming increasingly apparent."
    ),
    (
        "The deadline is approaching faster than my progress would suggest is sustainable. Something is going to have "
        "to give, and I'm dreading the conversation about what."
    ),
    (
        "I'm anxious about how this situation will affect the people depending on me. My decisions have consequences "
        "for others that I can't fully predict or control."
    ),
    (
        "The feedback I received was harder to hear than I expected. I'm still processing whether there's validity to "
        "the criticism or if it reflects bias."
    ),
    (
        "I've been avoiding checking my email because I'm afraid of what might be waiting there. That avoidance is "
        "creating its own problems on top of the original ones."
    ),
    (
        "The amount of change happening simultaneously feels overwhelming. Each shift would be manageable alone, but "
        "together they're testing my capacity to adapt effectively."
    ),
    (
        "I'm worried I'm becoming someone I wouldn't have respected a decade ago. The compromises accumulate so "
        "gradually that you don't notice until you look back."
    ),
    # LONGER CONVERSATIONAL - GRATITUDE & APPRECIATION (~25 WORDS AVG)
    (
        "I don't say it enough, but I'm genuinely grateful for the stability we've built together. It's easy to take "
        "for granted when you're living in it daily."
    ),
    (
        "The small kindness you showed me during that difficult time meant more than you probably realized. I still "
        "think about it years later with deep appreciation."
    ),
    (
        "I'm thankful for the teachers who invested in me before I had anything to offer in return. Their belief in "
        "potential that wasn't yet visible shaped everything."
    ),
    (
        "The fact that I have access to clean water, shelter, and food is a privilege I try not to forget. So many "
        "people lack these basic necessities."
    ),
    (
        "I appreciate the friends who accepted me during my least lovable phases. The ones who saw through the mess to "
        "the person underneath struggling to emerge."
    ),
    (
        "The opportunities I've been given weren't earned solely through merit. Luck and circumstance played enormous "
        "roles that I try to acknowledge and pay forward."
    ),
    (
        "I'm grateful for my body even on days when I'm frustrated with it. It carries me through life despite "
        "everything I've put it through over the years."
    ),
    (
        "The technology we take for granted would have seemed miraculous to previous generations. The ability to "
        "connect instantly across vast distances still amazes me sometimes."
    ),
    (
        "I appreciate the quiet moments more now than I used to. The absence of crisis feels like a gift after "
        "experiencing what real difficulty looks like."
    ),
    (
        "The person who gave me my first professional break changed the entire trajectory of my career. That single "
        "act of trust opened doors I couldn't have accessed alone."
    ),
    (
        "I'm thankful for the lessons that came wrapped in disappointment. They hurt at the time, but the growth they "
        "forced has made me more resilient."
    ),
    (
        "The beauty in ordinary things reveals itself when you slow down enough to notice it. A sunset, a well made "
        "meal, a child's laughter, simple things."
    ),
    (
        "I appreciate the privilege of being able to pursue meaning rather than just survival. That luxury isn't "
        "available to everyone and I try not to squander it."
    ),
    (
        "The community I'm part of provides support I couldn't replicate on my own. We're stronger together than any "
        "of us would be in isolation."
    ),
    (
        "I'm grateful for second chances, both the ones I've received and the ones I've given. Life is too short to "
        "hold every mistake against people forever."
    ),
    # LONGER CONVERSATIONAL - CURIOSITIES & WONDERINGS (~25 WORDS AVG)
    (
        "I've been thinking about how different my life would look if I'd been born in a different time or place. The "
        "arbitrariness of it all fascinates me."
    ),
    (
        "What goes through someone's mind in the moment they decide to change everything? That tipping point between "
        "inertia and action remains mysterious to me."
    ),
    (
        "I wonder if the way I experience consciousness is fundamentally similar to how others experience it. Or if "
        "we're all having completely different subjective realities."
    ),
    (
        "The question of what makes something meaningful versus meaningless seems unanswerable yet incredibly "
        "important. How do we decide what matters and what doesn't?"
    ),
    (
        "I'm curious about the path not taken. The life that exists in some parallel universe where I made different "
        "choices at critical junctures."
    ),
    (
        "How much of who we become is inevitable given our starting conditions? And how much is genuinely the result "
        "of choices we made freely?"
    ),
    (
        "I often wonder what future generations will think of how we're living now. What will seem obviously wrong "
        "that we currently accept as normal?"
    ),
    (
        "The nature of time continues to puzzle me. The past feels so substantial, yet it exists only in memory and "
        "evidence left behind."
    ),
    (
        "What is it about certain people that makes them compelling while others with similar qualities fade into the "
        "background? Charisma seems almost magical."
    ),
    (
        "I'm fascinated by how completely two people can experience the same event differently. It makes me question "
        "whether objective reality is even accessible to us."
    ),
    (
        "The origins of consciousness remain one of the great mysteries. How did subjective experience emerge from "
        "physical matter? What does it feel like to be a bat?"
    ),
    (
        "I wonder about the thoughts of historical figures we've mythologized. Were they aware of their significance, "
        "or did they feel as uncertain as we do?"
    ),
    (
        "What happens to all the data we're generating about our lives? Future historians will have unprecedented "
        "access to the mundane details of our existence."
    ),
    (
        "The randomness of which creative works become classics versus which ones are forgotten seems arbitrary. "
        "Timing and circumstance play such enormous roles."
    ),
    (
        "I'm curious whether the constant stimulation we've normalized is changing our brains in ways we won't "
        "understand until much later. We're running an experiment on ourselves."
    ),
    # LONGER CONVERSATIONAL - COMPARISONS & CONTRASTS (~25 WORDS AVG)
    (
        "The difference between how I imagined adulthood would feel and how it actually feels is striking. Less "
        "arrival, more continuous navigation without a clear destination."
    ),
    (
        "My morning self and my evening self might as well be different people. The optimistic plans made at dawn "
        "rarely survive contact with afternoon reality."
    ),
    (
        "The gap between what I say I value and where I actually spend my time reveals uncomfortable truths. Actions "
        "really do speak louder than stated priorities."
    ),
    (
        "Work relationships and genuine friendships operate by completely different rules. Confusing the two has led "
        "me into awkward situations more than once."
    ),
    (
        "The version of me that exists in others' minds probably differs significantly from my self perception. We're "
        "all walking around with inaccurate models of each other."
    ),
    (
        "Online communication and face to face conversation activate different parts of my personality. I'm "
        "simultaneously more bold and more cautious when typing than when speaking."
    ),
    (
        "The effort required to maintain a relationship is inversely proportional to how compatible you actually are. "
        "Hard work shouldn't be the primary characteristic of connection."
    ),
    (
        "My public confidence and private doubt coexist in a tension that never fully resolves. Most people probably "
        "only see the polished exterior version."
    ),
    (
        "The speed at which good habits dissolve versus bad habits shows how much easier destruction is than "
        "construction. Building takes effort; decay happens automatically."
    ),
    (
        "My ideal day and my actual typical day share surprisingly few characteristics. The alignment between "
        "aspiration and reality remains a work in progress."
    ),
]

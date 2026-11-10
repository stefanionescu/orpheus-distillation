"""Multi-sentence prompts: natural talk about money, then longer talk about daily life and reflections."""

from __future__ import annotations

FINANCE: list[str] = [
    # FINANCE & MONEY - NATURAL
    (
        "The compound interest on that investment has grown substantially. Starting early makes an enormous difference "
        "over decades."
    ),
    (
        "Our emergency fund now covers six months of essential expenses. That financial cushion provides significant "
        "peace of mind."
    ),
    (
        "The refinancing reduced our monthly mortgage payment considerably. Interest rates dropped significantly since "
        "our original loan."
    ),
    (
        "His financial advisor recommended diversifying across multiple asset classes. Concentration risk was higher "
        "than we realized."
    ),
    (
        "The budgeting app tracks every transaction automatically now. Visibility into spending patterns has changed "
        "my behavior."
    ),
    (
        "Tax season required organizing receipts from the entire year. Better record keeping would simplify this "
        "annual headache."
    ),
    (
        "The cryptocurrency volatility exceeds my personal risk tolerance. I prefer more stable investments for my "
        "retirement accounts."
    ),
    (
        "Our credit score improved after paying down the balances. The utilization ratio affects the calculation "
        "significantly."
    ),
    (
        "The estate planning attorney drafted our wills and trusts. Nobody enjoys contemplating mortality but "
        "preparation matters."
    ),
    (
        "Inflation has eroded purchasing power more than expected recently. Salary adjustments haven't kept pace with "
        "rising costs."
    ),
    (
        "The subscription audit revealed we were paying for unused services. Canceling forgotten memberships freed up "
        "monthly cash flow."
    ),
    (
        "Her side business generates meaningful supplemental income now. Multiple revenue streams provide financial "
        "resilience."
    ),
    (
        "The pension plan offers guaranteed income throughout retirement. Defined benefit plans are increasingly rare "
        "these days."
    ),
    (
        "Our down payment took several years of disciplined saving. Homeownership seemed impossible until we committed "
        "to the goal."
    ),
    (
        "The identity theft required freezing credit and disputing charges. The resolution process was exhausting and "
        "time consuming."
    ),
    (
        "His charitable giving strategy optimizes both impact and tax benefits. Donor advised funds provide "
        "flexibility in timing."
    ),
    (
        "The healthcare expenses exceeded our annual deductible already. Medical costs seem to increase faster than "
        "everything else."
    ),
    (
        "Our college savings account should cover tuition when needed. Starting contributions early leverages time "
        "effectively."
    ),
    (
        "The market correction tested our long term investment strategy. Panic selling would have locked in "
        "unnecessary losses."
    ),
    (
        "Automating transfers to savings removes the temptation to spend. Paying yourself first is deceptively simple "
        "but effective."
    ),
    # LONGER CONVERSATIONAL - DAILY EXPERIENCES (~25 WORDS AVG)
    (
        "I woke up this morning feeling completely refreshed for once, which almost never happens on weekdays. Maybe "
        "that new mattress is finally making a difference."
    ),
    (
        "The traffic on the highway was absolutely horrendous this morning, so I took the scenic route instead. It "
        "added twenty minutes but reduced my stress considerably."
    ),
    (
        "My coworker brought homemade banana bread to the office today. Honestly, it was the highlight of an otherwise "
        "tedious Wednesday afternoon meeting."
    ),
    (
        "The plumber finally arrived after I'd been waiting for nearly four hours, but he fixed the issue in about "
        "fifteen minutes flat. At least it's solved now."
    ),
    (
        "I've been meaning to reorganize my closet for about three months now. Every weekend something more pressing "
        "seems to come up and demand my attention instead."
    ),
    (
        "The new coffee shop around the corner makes the best oat milk lattes I've ever tasted. I've already become a "
        "regular there, unfortunately for my wallet."
    ),
    (
        "My phone battery has been dying by lunchtime lately. It's incredibly frustrating when I rely on it for "
        "navigation and communication throughout the workday."
    ),
    (
        "We finally finished painting the spare bedroom after procrastinating for nearly six months. The sage green "
        "color looks even better than we expected it would."
    ),
    (
        "The grocery store was completely out of my usual pasta sauce brand. I reluctantly tried a different one that "
        "turned out to be surprisingly delicious."
    ),
    (
        "I accidentally left my umbrella on the train this morning. Of course this happened on the one day when "
        "afternoon thunderstorms were actually predicted."
    ),
    (
        "My neighbor's dog has been barking incessantly since they left for vacation three days ago. I'm starting to "
        "wonder if anyone is checking on the poor creature."
    ),
    (
        "The dentist said I need to floss more consistently. That's the same feedback I've received at every single "
        "appointment for the past decade of my adult life."
    ),
    (
        "I finally unsubscribed from about thirty email newsletters that I never actually read. My inbox already feels "
        "significantly more manageable and less overwhelming than before."
    ),
    (
        "The restaurant we tried for our anniversary had incredible ambiance and attentive service. But the food "
        "itself was disappointingly mediocre for the premium prices they charged."
    ),
    (
        "My gym membership expires next month and I'm debating whether to renew it. I've only actually gone about six "
        "times in the past three months honestly."
    ),
    (
        "The package I ordered was supposed to arrive yesterday but got delayed due to weather conditions. This seems "
        "to happen with increasing frequency regardless of the carrier."
    ),
    (
        "I spent the entire weekend binge watching that documentary series everyone recommended. Now I understand why "
        "people kept insisting I needed to see it immediately."
    ),
    (
        "The air conditioning unit started making a strange rattling noise last night. It kept waking me up every "
        "couple of hours until I finally unplugged it completely."
    ),
    (
        "My grandmother called to share her famous apple pie recipe with me yesterday. She spent forty five minutes "
        "explaining the exact technique for achieving a perfect flaky crust."
    ),
    (
        "The concert tickets sold out in literally less than two minutes after going on sale. I was refreshing "
        "constantly with my payment saved, but it wasn't enough."
    ),
    # LONGER CONVERSATIONAL - REFLECTIONS (~25 WORDS AVG)
    (
        "There's something deeply satisfying about watching a thunderstorm roll in from a safe dry spot on the porch. "
        "A warm cup of tea makes it even better."
    ),
    (
        "The way late afternoon sunlight filters through the kitchen window creates beautiful patterns on the floor. I "
        "never noticed them before we rearranged the furniture."
    ),
    (
        "I've noticed that my productivity tends to peak in the mid morning hours between nine and eleven. It drops "
        "off significantly after lunch no matter what I eat."
    ),
    (
        "The older I get, the more I appreciate simple pleasures like a quiet morning and a good book. No obligations "
        "or responsibilities demanding my immediate attention."
    ),
    (
        "It's fascinating how certain songs can instantly transport you back to specific moments in your life. "
        "Complete with emotions and sensory details you thought you'd forgotten."
    ),
    (
        "The neighborhood has changed so much over the past five years that I sometimes barely recognize it. I walked "
        "these streets daily as a child growing up here."
    ),
    (
        "I find it remarkable how quickly children adapt to new technologies that their parents struggle with. It's as "
        "if their brains are wired completely differently from ours."
    ),
    (
        "There's a particular quality to autumn light that makes everything look warmer and more nostalgic. Like the "
        "entire world is being photographed through a vintage filter."
    ),
    (
        "The sound of rain on a metal roof is one of the most soothing things I've ever experienced. Especially when "
        "you're tucked into bed with nowhere to be."
    ),
    (
        "I've started noticing how different people have completely different walking rhythms and paces. It can be "
        "difficult to synchronize steps with someone whose gait differs from yours."
    ),
    (
        "The way my cat positions herself in the exact center of whatever I'm working on is curious. She's either "
        "attention seeking or deliberately antagonizing me for her amusement."
    ),
    (
        "The anticipation of something often brings more joy than the actual event itself. That probably explains why "
        "I enjoy planning vacations so much more than taking them."
    ),
    (
        "The smell of freshly baked bread has an almost magical effect on my mood instantly. It makes any space feel "
        "more comfortable, welcoming, and reminiscent of childhood."
    ),
    (
        "People tend to underestimate how long tasks will take them while overestimating how much they can accomplish. "
        "This happens to me constantly despite years of experience."
    ),
    (
        "The first truly warm day after a long winter always feels like a collective release. Everyone outside looks "
        "slightly dazed and grateful for the sunshine on their faces."
    ),
    (
        "Certain accents or dialects can immediately make a person seem more trustworthy or intelligent to others. "
        "Despite having no actual correlation to those qualities whatsoever."
    ),
    (
        "Memories from decades ago can suddenly resurface with perfect clarity while yesterday's events remain foggy. "
        "That's one of the strangest aspects of how human consciousness works."
    ),
    (
        "My appetite for risk has decreased substantially as I've accumulated more responsibilities. More things could "
        "potentially go wrong now if I made poor decisions."
    ),
    (
        "Standing at the edge of the ocean and contemplating how those same waves have crashed for millions of years "
        "is profound. Long before humans ever existed here."
    ),
    (
        "Walking into a room and immediately forgetting why you went there happens to me with increasing frequency. "
        "I'm choosing to attribute it to having too much on my mind."
    ),
]

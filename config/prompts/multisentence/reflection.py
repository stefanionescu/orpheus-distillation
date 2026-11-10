"""Multi-sentence prompts about self-reflection, observations, and practical matters."""

from __future__ import annotations

REFLECTION: list[str] = [
    # SELF-REFLECTION (~22 WORDS AVG)
    (
        "I caught myself repeating something my parent used to say that I swore I'd never say. The cycle continues "
        "despite our best intentions."
    ),
    (
        "The person I was ten years ago would be confused by some of my current choices. Growth looks different than I "
        "expected it would."
    ),
    (
        "I've started journaling again after a long hiatus. The practice of externalizing thoughts has become "
        "essential for making sense of everything."
    ),
    (
        "My comfort zone has shrunk considerably since the pandemic. Pushing those boundaries again requires "
        "intentional effort that I don't always have."
    ),
    (
        "The mirror shows someone I don't always recognize immediately. The disconnect between internal self image and "
        "external reality surprises me sometimes."
    ),
    (
        "I realized I've been the toxic person in some situations. That self awareness arrived late but at least it "
        "finally showed up."
    ),
    (
        "My energy levels fluctuate wildly for no apparent reason. Some days I'm productive beyond belief; others I "
        "can barely function at all."
    ),
    (
        "The hobbies I used to love don't spark the same joy anymore. Finding new sources of fulfillment has become a "
        "project in itself."
    ),
    (
        "I've become my own worst critic in ways that aren't constructive. The internal voice needs retraining but old "
        "patterns resist change."
    ),
    (
        "The boundaries I've set feel selfish sometimes even though intellectually I know they're necessary. Guilt "
        "accompanies self protection more than it should."
    ),
    (
        "I'm more risk averse than I used to be and I'm not sure that's entirely bad. Wisdom and fear can look similar "
        "from the outside."
    ),
    (
        "My attention span has definitely shortened over the past few years. Deep focus requires more effort than it "
        "used to before."
    ),
    (
        "The version of success I'm chasing has evolved significantly over time. What seemed important at twenty feels "
        "less so approaching forty."
    ),
    (
        "I notice myself becoming more like my parents in ways both endearing and concerning. Some traits I actively "
        "cultivate; others I resist."
    ),
    (
        "My tolerance for certain behaviors has decreased with age. Things I once excused as harmless now feel like "
        "legitimate dealbreakers."
    ),
    (
        "The imposter syndrome never fully goes away no matter how much evidence contradicts it. Some days the doubt "
        "is quieter than others."
    ),
    (
        "I've stopped apologizing for things that don't require apologies. Unlearning reflexive sorry has been "
        "surprisingly difficult but worthwhile."
    ),
    (
        "My capacity for patience varies dramatically depending on factors I can't always control. Some days I'm a "
        "saint; others I'm insufferable."
    ),
    (
        "The relationship with my body has improved but remains complicated. Acceptance and frustration coexist in "
        "ways I'm still learning to navigate."
    ),
    (
        "I catch myself catastrophizing about unlikely scenarios more than I'd like to admit. The anxiety creates "
        "problems that don't actually exist."
    ),
    # OBSERVATIONS & MUSINGS (~22 WORDS AVG)
    (
        "The barista remembered my order after just two visits. Such a small thing but it made my entire morning feel "
        "more personal."
    ),
    (
        "The street performer's music followed me for three blocks. Some melodies attach themselves to moments and "
        "become inseparable from the memory."
    ),
    (
        "The child's unfiltered laughter on the train reminded everyone how rarely adults laugh like that anymore. We "
        "smiled at each other knowingly."
    ),
    (
        "The sunset turned the entire city pink for exactly seven minutes. Everyone stopped what they were doing just "
        "to witness it together."
    ),
    (
        "The old bookstore smell triggered memories I didn't know I still had. Scent connects to the past in ways "
        "nothing else can."
    ),
    (
        "The handwritten note inside the used book made me wonder about its previous owner. Small traces of strangers' "
        "lives appearing unexpectedly."
    ),
    (
        "The perfectly timed traffic light sequence made my commute feel like the universe was cooperating for once. "
        "Small victories matter."
    ),
    "The stranger who held the door smiled like they meant it. Such a minor kindness but it shifted my entire mood.",
    (
        "The coffee tastes different when you drink it slowly without distractions. The ritual matters as much as the "
        "caffeine itself."
    ),
    (
        "The dog at the park befriended every person regardless of their demeanor. Animals don't discriminate based on "
        "human social signals."
    ),
    (
        "The thunderstorm knocked out power for six hours unexpectedly. Without screens, we actually talked and played "
        "cards like families used to."
    ),
    (
        "The autumn leaves crunch differently depending on how recently they fell. There's a science to the sound that "
        "I've never investigated."
    ),
    (
        "The full moon made the familiar neighborhood look completely different. Lighting changes everything about how "
        "we perceive spaces we think we know."
    ),
    (
        "The elderly couple holding hands on the bench gave me hope about long term relationships. Tenderness survives "
        "decades if you let it."
    ),
    (
        "The rain stopped exactly when I needed to walk outside. Sometimes the timing of things feels suspiciously "
        "fortunate and intentional."
    ),
    (
        "The stranger's t shirt referenced something incredibly specific that I also loved. We exchanged knowing nods "
        "without any words being necessary."
    ),
    (
        "The toddler waving at everyone from the shopping cart improved multiple strangers' days. Joy really is "
        "contagious when offered freely."
    ),
    (
        "The unexpected compliment from someone I barely know stayed with me all week. Kindness from strangers hits "
        "differently than from friends."
    ),
    (
        "The musician busking in the subway tunnel played something I hadn't heard since childhood. The memory flooded "
        "back completely unexpectedly."
    ),
    (
        "The rainbow appeared right after the heaviest part of the storm passed. The timing felt meaningful even if it "
        "was just physics."
    ),
    # PRACTICAL MATTERS (~22 WORDS AVG)
    (
        "The mechanic quoted three times what I expected for the repair. Now I'm debating whether to fix the car or "
        "replace it entirely."
    ),
    (
        "The insurance company denied the claim citing a technicality I don't understand. The appeals process seems "
        "designed to exhaust people into giving up."
    ),
    (
        "The contractor's timeline keeps slipping without explanation or accountability. We're three weeks past the "
        "promised completion date with no end visible."
    ),
    (
        "The appliance broke one month after the warranty expired. The timing is suspicious enough that I'm convinced "
        "they're engineered to fail."
    ),
    (
        "The property taxes increased significantly more than the notice suggested they would. Budgeting has become a "
        "moving target I can't hit accurately."
    ),
    (
        "The leak in the ceiling is coming from somewhere we can't identify. Multiple professionals have different "
        "theories about the water source."
    ),
    (
        "The pest control company needs to come back for the fourth time. Whatever is living in our walls is "
        "remarkably resilient."
    ),
    (
        "The medication costs more without insurance than my groceries for the month. Healthcare affordability remains "
        "an ongoing impossible equation to solve."
    ),
    (
        "The HOA sent another violation notice about something trivial. The neighborhood politics are pettier than "
        "anything I experienced in high school."
    ),
    (
        "The closing costs were significantly higher than the good faith estimate indicated. First time home buying is "
        "full of expensive surprises."
    ),
    (
        "The delivery window is sometime between eight in the morning and eight at night. Apparently my entire day is "
        "hostage to their schedule."
    ),
    (
        "The bank's fraud department flagged a legitimate purchase and froze my card. Now I'm stranded without access "
        "to my own money temporarily."
    ),
    (
        "The restaurant charged for items we didn't order and disputing it became complicated. The manager seemed "
        "annoyed that we noticed the error."
    ),
    (
        "The gym contract has more fine print than my mortgage documents did. Cancellation requires certified mail, "
        "notarized forms, and possibly a blood sacrifice."
    ),
    (
        "The flight was oversold and they're looking for volunteers to give up seats. The compensation offered isn't "
        "enough to justify the inconvenience."
    ),
    (
        "The utility bill tripled despite our usage staying consistent with previous months. Their explanation "
        "involves rate adjustments I don't fully comprehend."
    ),
    (
        "The apartment application requires income verification, references, credit checks, and my firstborn child. "
        "Finding housing has become a competitive sport."
    ),
    (
        "The tax situation is more complicated than last year due to multiple income sources. The accountant's fee "
        "keeps increasing alongside the complexity."
    ),
    (
        "The service department lost my device for two weeks before admitting the mistake. The apology came with no "
        "compensation for my trouble."
    ),
    (
        "The store's return policy changed since I made the purchase. Now I'm stuck with something that doesn't work "
        "for my needs."
    ),
]

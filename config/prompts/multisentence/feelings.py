"""Multi-sentence prompts: longer talk about emotions, people, hopes, and regrets."""

from __future__ import annotations

FEELINGS: list[str] = [
    # LONGER CONVERSATIONAL - EMOTIONS & FEELINGS (~25 WORDS AVG)
    (
        "Some days the weight of everything just feels heavier than usual for no apparent reason. Like carrying "
        "invisible bags that nobody else can see but you feel constantly."
    ),
    (
        "The pride I felt watching them succeed after all those struggles was overwhelming. All those late nights and "
        "setbacks finally culminating in this moment of triumph."
    ),
    (
        "There's a specific kind of loneliness that comes from being surrounded by people who don't really understand "
        "you. It's different from being physically alone somehow."
    ),
    (
        "The relief that washed over me when I finally heard the good news was indescribable. Weeks of anxiety "
        "evaporated in a single moment of pure release."
    ),
    (
        "I've been carrying this low level anxiety for so long that I've almost forgotten what calm feels like. It's "
        "become my baseline, which probably isn't healthy."
    ),
    (
        "The joy that simple moments bring me now wouldn't have registered a decade ago. Somehow I learned to "
        "appreciate small pleasures that previously went unnoticed completely."
    ),
    (
        "There's something bittersweet about watching your children become independent. Pride mixed with grief for the "
        "phase of life that's ending and will never return again."
    ),
    (
        "The frustration of not being able to articulate exactly what I'm feeling is its own special torment. The "
        "emotions are there but the words aren't cooperating."
    ),
    (
        "I experienced a moment of complete contentment yesterday, which is rare enough that I actually noticed it. "
        "Just sitting on the porch, watching the sunset unfold."
    ),
    (
        "The anticipation is almost unbearable at this point. I've been waiting so long that the waiting itself has "
        "become the dominant feature of my daily existence."
    ),
    (
        "There's a heaviness that settles in after you lose someone, and it never fully lifts. You just learn to carry "
        "it more gracefully over time somehow."
    ),
    (
        "The gratitude I feel for the people who showed up during my darkest moments is profound. They didn't have to, "
        "but they chose to anyway."
    ),
    (
        "Sometimes happiness sneaks up on you in unexpected moments. Not the dramatic kind, but a quiet contentment "
        "that settles in when you're not paying attention."
    ),
    (
        "The vulnerability required to admit you were wrong about something important is genuinely uncomfortable. But "
        "the relief that follows the admission makes it worthwhile every time."
    ),
    (
        "I've noticed that my emotional resilience fluctuates more than I'd like to admit. Some weeks I can handle "
        "anything; others, the smallest setback feels catastrophic."
    ),
    # LONGER CONVERSATIONAL - OBSERVATIONS ABOUT PEOPLE (~25 WORDS AVG)
    (
        "She has this incredible ability to make everyone in the room feel seen and valued. A rare gift that seems "
        "effortless but probably requires tremendous emotional intelligence."
    ),
    (
        "The way he talks about his work reveals a passion that most people lose somewhere along the way. It's "
        "refreshing to witness genuine enthusiasm that hasn't faded."
    ),
    (
        "There are people who light up when they enter a room, and people who light up when they leave. It's "
        "fascinating to observe the difference in dynamics."
    ),
    (
        "Her generosity extends far beyond money to include time, attention, and emotional support. The kind of giving "
        "that actually costs something meaningful and personal to provide."
    ),
    (
        "He's one of those rare individuals who actually listens when you speak. Not just waiting for his turn to "
        "talk, but genuinely absorbing what you're saying."
    ),
    (
        "The way they navigate conflict reveals everything about their character. Some people escalate, some avoid, "
        "some address issues directly with remarkable composure and maturity."
    ),
    (
        "She carries herself with a quiet confidence that doesn't need external validation. There's something deeply "
        "appealing about people who are comfortable in their own skin."
    ),
    (
        "His sense of humor reveals an intelligence that his modesty often conceals. The wit is quick and sharp but "
        "never at anyone else's expense, which is admirable."
    ),
    (
        "There are people who make you feel energized after spending time with them, and people who leave you "
        "completely drained. The difference is immediately noticeable."
    ),
    (
        "The patience she shows with difficult people is remarkable. I've watched her defuse tensions that would have "
        "escalated dramatically if anyone else had been handling them."
    ),
    (
        "He has this habit of remembering small details about people's lives that makes everyone feel important. A "
        "powerful social skill that creates genuine connection."
    ),
    (
        "Her resilience after everything she's been through is genuinely inspiring. Not in a performative way, but in "
        "a quiet determination to keep moving forward regardless."
    ),
    (
        "The authenticity with which they live their life is refreshing in an age of carefully curated personas. What "
        "you see is genuinely what you get with them."
    ),
    (
        "Some people have an uncanny ability to ask exactly the right question at the right moment. The kind that "
        "unlocks insight you didn't know you had."
    ),
    (
        "His leadership style is effective precisely because it doesn't feel like leadership at all. More like "
        "collaboration with someone who happens to have the final say."
    ),
    # LONGER CONVERSATIONAL - HOPES & DREAMS (~25 WORDS AVG)
    (
        "I've always dreamed of owning a small cottage by the sea where I could write and watch the waves crash "
        "against the shore. Maybe someday that will happen."
    ),
    (
        "My biggest hope for my children is that they find work that feels meaningful to them. Not necessarily "
        "lucrative, but something that gives them a sense of purpose."
    ),
    (
        "There's a place I visited once as a child that I've been trying to return to ever since. The memory is so "
        "vivid but I can't locate it anywhere."
    ),
    (
        "I imagine sometimes what it would be like to take a year off and travel without any fixed itinerary. Just "
        "following curiosity wherever it leads me next."
    ),
    (
        "The life I envision for myself in twenty years looks nothing like what I thought I wanted at twenty. "
        "Priorities shift in ways you can't anticipate."
    ),
    (
        "I secretly hope that something I create outlives me. A piece of writing, a project, anything that continues "
        "to matter after I'm no longer around to see it."
    ),
    (
        "The dream isn't really about the money itself but about the freedom that financial security would provide. "
        "The ability to say no to things that drain me."
    ),
    (
        "I keep imagining a future where I have more time for the people and activities that actually bring me joy. "
        "Right now those things feel perpetually squeezed out."
    ),
    (
        "My aspiration is to reach a point where I'm no longer motivated by fear of failure. Where I can take creative "
        "risks without the constant anxiety."
    ),
    (
        "There's a conversation I've been rehearsing in my head for years that I hope to have someday. When the timing "
        "finally feels right and I'm brave enough."
    ),
    (
        "I fantasize about a slower pace of life where there's time to cook real meals and read entire books. Where "
        "productivity isn't the only measure of a day."
    ),
    (
        "The future I'm working toward involves less accumulation and more experience. Fewer possessions but richer "
        "memories and deeper connections with the people I love."
    ),
    (
        "I hope to reach a point where I've forgiven myself for the mistakes that still keep me up at night. That self "
        "compassion continues to elude me somehow."
    ),
    (
        "My long term goal is to build something that creates value for others beyond just myself. Something that "
        "contributes positively to a community I care about deeply."
    ),
    (
        "I dream of mastering a skill that currently feels completely beyond my abilities. The satisfaction of "
        "becoming competent at something that once seemed impossible to learn."
    ),
    # LONGER CONVERSATIONAL - REGRETS & LESSONS (~25 WORDS AVG)
    (
        "Looking back, I wish I had spent less time worrying about what other people thought of me. So much energy "
        "wasted on perceptions that probably didn't matter."
    ),
    (
        "The biggest lesson I learned the hard way is that some relationships have an expiration date. Holding on past "
        "that point causes more damage than letting go."
    ),
    (
        "I regret not being more present during certain phases of my life. I was so focused on what came next that I "
        "missed what was happening then."
    ),
    (
        "One thing I would tell my younger self is that the things you're embarrassed about now won't matter in ten "
        "years. Almost nobody remembers except you."
    ),
    (
        "The mistake that taught me the most was the one I initially thought had ruined everything. In hindsight, it "
        "redirected me toward something much better."
    ),
    (
        "I spent years trying to fix something that wasn't mine to fix. Learning to accept what I couldn't change was "
        "one of the hardest lessons of my life."
    ),
    (
        "The opportunity I didn't take still haunts me occasionally. Not because my life is bad, but because I'll "
        "never know what might have happened if I'd been braver."
    ),
    (
        "I wish someone had told me earlier that perfection isn't the goal. Done and imperfect is almost always better "
        "than perfect but never finished."
    ),
    (
        "The relationship I stayed in too long taught me what I actually need from a partner. Sometimes we have to "
        "experience the wrong thing to recognize the right one."
    ),
    (
        "I regret prioritizing career advancement over personal relationships during my thirties. The professional "
        "gains weren't worth the connections I let atrophy during that decade."
    ),
    (
        "The advice I ignored because I thought I knew better turned out to be exactly right. Sometimes wisdom really "
        "does come with age and experience."
    ),
    (
        "Looking back, I realize I was often the problem in situations where I blamed everyone else. That self "
        "awareness came much later than it should have."
    ),
    (
        "The failure that devastated me at the time led directly to the best thing that ever happened to me. I "
        "couldn't see the connection until years later."
    ),
    (
        "I wish I had learned to set boundaries earlier instead of burning out repeatedly. The pattern had to become "
        "unbearable before I finally changed it."
    ),
    (
        "The person I was most angry at for years turned out to be dealing with struggles I knew nothing about. "
        "Empathy would have served me better than resentment."
    ),
]

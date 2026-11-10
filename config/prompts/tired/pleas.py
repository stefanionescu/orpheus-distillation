"""Tired prompts: long questions, exclamations, and mixed types, then raw emotional exhaustion."""

from __future__ import annotations

PLEAS: list[str] = [
    # MORE LONG PROMPTS - QUESTIONS (30-37 WORDS)
    (
        "Why is it that the more exhausted I become, the harder it is to actually fall asleep when I finally get the "
        "chance, like my body is sabotaging its own recovery?"
    ),
    (
        "How do people with demanding schedules manage to function on minimal sleep without completely falling apart, "
        "because I'm barely holding it together and I need to know their secret immediately?"
    ),
    (
        "When did being constantly tired become my default state, and is there any way to reset my baseline back to a "
        "time when I actually had energy to spare?"
    ),
    (
        "Why does exhaustion make everything feel so much more difficult than it actually is, turning simple tasks "
        "into mountains I have to climb with weights strapped to my back?"
    ),
    (
        "How am I expected to make good decisions when my brain is operating at maybe twenty percent capacity on a "
        "good day, running on fumes and pure stubbornness alone?"
    ),
    (
        "Is there a scientific explanation for why being overtired makes you feel slightly drunk, with the same "
        "impaired judgment and coordination but none of the fun that comes with it?"
    ),
    (
        "Why does my body decide to be wide awake at three in the morning when I desperately need sleep, but "
        "completely exhausted at two in the afternoon when I need to work?"
    ),
    (
        "How long can a person actually function on minimal sleep before their body just gives up entirely, because I "
        "feel like I'm approaching that limit faster than I'd like?"
    ),
    (
        "When will I learn to prioritize sleep over staying up late doing things that aren't even important, knowing "
        "full well that tomorrow me will suffer for tonight me's poor choices?"
    ),
    (
        "Why is it that exhaustion makes me crave junk food and sugar, like my body thinks empty calories will somehow "
        "substitute for the rest it actually needs to function?"
    ),
    (
        "How do parents of newborns survive the sleep deprivation, because I'm struggling with self inflicted "
        "tiredness and I can't imagine adding a crying baby to this equation at all?"
    ),
    (
        "Is it normal to feel like you're watching your life happen from outside your body when you're this tired, or "
        "should I be more concerned about this dissociation thing?"
    ),
    (
        "Why does being exhausted make me so emotional about random things, crying at commercials and getting "
        "irrationally angry at minor inconveniences that wouldn't normally bother me at all?"
    ),
    (
        "How am I supposed to be creative or productive when my brain feels like it's been stuffed with cotton and "
        "every thought has to fight through layers of fog?"
    ),
    (
        "When did I become someone who needs coffee just to feel normal, rather than someone who drinks coffee because "
        "they enjoy it and not out of desperate necessity?"
    ),
    # MORE LONG PROMPTS - EXCLAMATIONS (30-37 WORDS)
    (
        "I can't believe I have to function like a normal human being when I've had maybe four hours of sleep and my "
        "brain is running on emergency backup power only!"
    ),
    (
        "I'm so tired that I accidentally sent a text to my boss that was meant for my friend, and now I have to "
        "pretend I meant to say that!"
    ),
    (
        "My exhaustion has reached the point where I'm genuinely impressed with myself for remembering to eat today, "
        "because basic survival tasks have become major accomplishments in my current state!"
    ),
    (
        "I've never been so tired in my entire life, and I've been tired a lot, so the fact that this beats all "
        "previous records is really saying something important!"
    ),
    (
        "I can't keep living like this, running on empty day after day and expecting my body to just keep going "
        "without the rest it desperately needs to function properly!"
    ),
    (
        "I'm so drained that I've started making mistakes I would never normally make, and I'm terrified of what I "
        "might mess up next in my sleep deprived state!"
    ),
    (
        "My body is literally shutting down on me and I can feel it happening, systems going offline one by one as my "
        "energy reserves hit absolute zero today!"
    ),
    (
        "I've consumed enough caffeine to power a small city and I'm still exhausted, which means either the coffee is "
        "broken or I'm more tired than coffee can fix!"
    ),
    (
        "I can't remember the last time I woke up feeling actually rested, and I'm starting to think that feeling "
        "might just be a myth people made up to torture me!"
    ),
    (
        "My tiredness has made me so clumsy that I've broken three things today just by existing near them, my "
        "coordination completely shot by lack of proper sleep this week!"
    ),
    (
        "I'm so exhausted that I've lost the ability to filter my thoughts before they come out of my mouth, and I've "
        "said some things I definitely shouldn't have!"
    ),
    (
        "I can't focus on anything for more than about thirty seconds before my brain wanders off, and I've been "
        "trying to finish the same task for hours now!"
    ),
    (
        "My sleep deprivation has reached dangerous levels and I'm genuinely worried about my ability to function "
        "safely, especially when it comes to things like driving or making decisions!"
    ),
    (
        "I've hit a wall so hard that I've bounced off it and hit another wall, and now I'm just lying here between "
        "the walls wondering how I got here!"
    ),
    (
        "I'm so tired that I've started to hallucinate that my bed is calling my name, and honestly it's the most "
        "compelling argument I've heard all day for anything!"
    ),
    # MORE LONG PROMPTS - MIXED TYPES (30-37 WORDS)
    (
        "My exhaustion has become so normalized that people have stopped asking if I'm okay and just accept that this "
        "is how I look now, which is both sad and convenient."
    ),
    (
        "I've been pushing through this fatigue for so long that I've developed coping mechanisms I didn't know I had, "
        "like the ability to sleep with my eyes open apparently."
    ),
    (
        "My tiredness has given me a new appreciation for people who work night shifts, because fighting your body's "
        "natural sleep schedule is a special kind of torture I now understand."
    ),
    (
        "I'm so drained that I've started to see sleep as a reward I have to earn rather than a basic human need I "
        "deserve, which is probably not healthy thinking."
    ),
    (
        "My fatigue has made me realize how much of my personality is actually just being well rested, because tired "
        "me is basically a completely different and much worse person."
    ),
    (
        "I've gotten to the point where I'm jealous of my past self who used to complain about being tired when they "
        "had no idea what real exhaustion actually feels like."
    ),
    (
        "My sleep deprivation has affected my sense of taste, and food that I normally love just tastes like nothing "
        "because my tired taste buds have given up on their job."
    ),
    (
        "I'm so exhausted that I've started to feel grateful for small mercies, like traffic lights that turn green "
        "and elevators that arrive quickly, because waiting requires energy I don't have."
    ),
    (
        "My tiredness has made me incredibly literal, unable to process sarcasm or subtext because my brain doesn't "
        "have the spare capacity for anything beyond the surface meaning of words."
    ),
    (
        "I've been running on empty for so long that I've started to identify with my car when the fuel light comes "
        "on, both of us desperately needing to refuel."
    ),
    (
        "My exhaustion has turned me into a creature of pure routine, following the same patterns every day because "
        "deviating would require decision making energy that I simply don't possess anymore."
    ),
    (
        "I'm so tired that I've developed a deep emotional attachment to my pillow, thinking about it fondly "
        "throughout the day like a long distance relationship I'm desperate to maintain."
    ),
    (
        "My fatigue has made me philosophical about the nature of rest, wondering if true relaxation is even possible "
        "or if we're all just varying degrees of tired all the time."
    ),
    (
        "I've reached the point where I'm too exhausted to even enjoy the things I do for fun, hobbies becoming chores "
        "because everything requires energy I don't have to spare."
    ),
    (
        "My sleep debt has compounded to the point where I'm not sure I'll ever feel fully rested again, like I've "
        "permanently damaged my relationship with sleep somehow irreparably now."
    ),
    (
        "I'm so drained that I've started to appreciate silence in a way I never did before, because even processing "
        "sounds requires energy that I'm not willing to spend anymore."
    ),
    (
        "My tiredness has made me hyper aware of how much energy everything takes, calculating the cost of each action "
        "and deciding if it's worth the expenditure of my limited reserves."
    ),
    (
        "I've been exhausted for so long that I've started to forget what I was like when I was well rested, that "
        "version of me feeling like a distant stranger."
    ),
    (
        "My fatigue has affected my ability to plan ahead, because thinking about the future requires energy and I'm "
        "barely managing to get through the present moment right now today."
    ),
    (
        "I'm so tired that I've developed a new respect for caffeine, viewing it not as a luxury but as essential "
        "medicine that keeps me functional enough to exist in society."
    ),
    # EMOTIONAL EXHAUSTION - RAW AND VULNERABLE (15-37 WORDS)
    (
        "I'm so tired that I started crying in the shower this morning for no reason, and I couldn't even tell you "
        "what I was crying about."
    ),
    (
        "Sometimes I wonder if anyone notices how exhausted I really am, or if I've gotten too good at hiding it from "
        "everyone around me."
    ),
    (
        "I'm tired in a way that sleep doesn't fix, like my soul needs rest but there's no bed for that kind of "
        "exhaustion."
    ),
    "I want to scream but I'm too tired to make a sound, so I just sit here silently falling apart on the inside.",
    (
        "The worst part about being this tired is pretending I'm fine when someone asks how I'm doing, smiling through "
        "the fog."
    ),
    (
        "I used to have dreams and ambitions, but now my only goal is making it through today without completely "
        "breaking down in front of everyone."
    ),
    (
        "I'm tired of being tired, and I'm tired of saying I'm tired, and I'm tired of no one understanding what that "
        "actually means."
    ),
    (
        "My body is here but my mind checked out hours ago, and I'm just going through motions that don't feel like "
        "they belong to me."
    ),
    (
        "I miss the version of me that had energy to laugh, to care, to feel anything other than this constant heavy "
        "emptiness dragging me down."
    ),
    "Some days the exhaustion feels like grief, like I'm mourning the person I used to be before I got this worn down.",
    (
        "I'm holding myself together with coffee and spite, but both are running dangerously low and I don't know what "
        "comes next."
    ),
    (
        "There's a special kind of loneliness that comes with exhaustion, where you're surrounded by people but too "
        "tired to actually connect with any of them."
    ),
    (
        "I keep waiting for the day I wake up feeling refreshed, but that day never comes and I'm starting to lose "
        "hope it ever will."
    ),
    "I'm so tired that I've started to resent the things I love because they take energy I don't have anymore.",
    (
        "The weight of exhaustion makes everything feel impossible, like I'm trying to swim through concrete just to "
        "do basic human tasks."
    ),
]

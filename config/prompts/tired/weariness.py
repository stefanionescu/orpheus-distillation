"""Tired prompts: long statements and questions."""

from __future__ import annotations

WEARINESS: list[str] = [
    # LONG SENTENCES - STATEMENTS (CLOSE TO 37 WORDS)
    (
        "I've been awake for so long that I've started seeing things in my peripheral vision, and I honestly can't "
        "tell if I'm hallucinating or just too tired to process reality correctly anymore."
    ),
    (
        "My body is running on pure adrenaline and caffeine at this point, and I know the crash is coming soon, but I "
        "just need to push through a few more hours somehow."
    ),
    (
        "I'm so exhausted that I put my shoes in the refrigerator and spent twenty minutes looking for them before "
        "realizing what I'd done, and honestly I'm not even surprised anymore."
    ),
    (
        "The level of fatigue I'm experiencing right now is making me question every life choice that led me to this "
        "moment of complete and utter physical and mental depletion."
    ),
    (
        "I've been yawning so much today that my jaw actually hurts, and every time I think I'm done yawning, another "
        "one hits me like a wave I can't control."
    ),
    (
        "My brain feels like it's operating at about ten percent capacity, and even simple tasks like remembering what "
        "day it is have become genuinely challenging for me right now."
    ),
    (
        "I'm at the point where I've had so much coffee that it's stopped working entirely, and now I'm just jittery "
        "and exhausted at the same time somehow."
    ),
    (
        "I tried to write an email earlier but I kept falling asleep between sentences, and when I finally finished it "
        "made absolutely no sense whatsoever to anyone including me."
    ),
    (
        "My eyes are so dry and heavy from lack of sleep that blinking has become an Olympic sport, and I'm losing "
        "badly with each passing minute of this day."
    ),
    (
        "I've been running on empty for so long that I forgot what it feels like to have actual energy, and the "
        "concept of being well rested seems like a myth now."
    ),
    (
        "I'm so tired that I laughed at something that wasn't funny for about five minutes straight, and then I almost "
        "cried because I couldn't stop laughing about nothing."
    ),
    (
        "My limbs feel like they're filled with sand, and every movement requires a conscious decision and significant "
        "effort that I'm not sure I have left in me today."
    ),
    (
        "I've reached the stage of exhaustion where I'm simultaneously too tired to sleep and too awake to rest, stuck "
        "in this horrible limbo of perpetual fatigue and frustration."
    ),
    (
        "I tried to take a power nap but my brain decided it was the perfect time to replay every embarrassing moment "
        "from my entire life instead of actually letting me rest."
    ),
    (
        "My concentration is so shot that I've been staring at the same page for thirty minutes without absorbing a "
        "single word, and I'm starting to wonder if I forgot how to read."
    ),
    (
        "I'm so exhausted that even my exhaustion is exhausted, and I've entered some kind of meta state of tiredness "
        "that I didn't know was possible until right now."
    ),
    (
        "I've been awake so long that I've started having conversations with myself just to stay alert, and honestly "
        "I'm not sure which version of me is winning anymore."
    ),
    (
        "My body is giving me every possible signal that it needs rest, from the headache to the heavy limbs to the "
        "inability to form coherent sentences without significant effort."
    ),
    (
        "I'm functioning on what I can only describe as survival mode, where my brain has shut down all non essential "
        "functions just to keep me upright and breathing somehow."
    ),
    (
        "The bags under my eyes have their own bags at this point, and I've given up trying to look presentable "
        "because exhaustion has become my permanent aesthetic now."
    ),
    (
        "I'm so tired that I put my coffee in the microwave and then forgot about it three separate times, each time "
        "rediscovering it cold and having to start over again."
    ),
    (
        "My sleep debt has accumulated to the point where I'm pretty sure I'd need to hibernate for an entire season "
        "just to break even on rest at this point."
    ),
    (
        "I've been pushing through this exhaustion for so long that I've forgotten what normal energy levels feel "
        "like, and I'm starting to think I imagined them entirely."
    ),
    (
        "I'm at the stage where even my autopilot is failing, and I keep making mistakes that I wouldn't normally make "
        "if I had slept at all in the past week."
    ),
    (
        "My brain has started playing tricks on me, making me think I've done things I haven't done and forget things "
        "I definitely did, all because I'm too tired to function."
    ),
    (
        "I've consumed enough caffeine to power a small city, but my body has built up such a tolerance that it barely "
        "registers anymore and I'm still completely exhausted."
    ),
    (
        "I'm so drained that I've started prioritizing which muscles to use because I don't have enough energy to "
        "engage all of them at once anymore throughout the day."
    ),
    (
        "My thoughts are moving through my brain like they're wading through thick honey, slow and sluggish and "
        "occasionally getting completely stuck before they reach any conclusion at all."
    ),
    (
        "I've been tired for so long that I've started to wonder if this is just my baseline now, if I'll ever feel "
        "truly awake and energized again in my life."
    ),
    (
        "I'm operating on borrowed energy that I'll definitely have to pay back later with interest, but future me can "
        "deal with that because present me just needs to survive today."
    ),
    (
        "My body has been sending me strongly worded letters about my sleep schedule, and I've been ignoring them, but "
        "now it's escalated to full protests and I'm suffering."
    ),
    (
        "I'm so exhausted that I've lost the ability to judge how tired I actually am, which probably means I'm more "
        "tired than I think and should definitely be sleeping now."
    ),
    (
        "I've reached the point where I can't remember if I already said something or just thought about saying it, "
        "and conversations have become a confusing guessing game for me."
    ),
    (
        "My energy levels are in the negative numbers, and I'm pretty sure I'm running on pure spite and the knowledge "
        "that I can't stop until this is finished."
    ),
    (
        "I'm so tired that my brain has started autocorrecting my thoughts wrong, and I keep thinking things that make "
        "absolutely no sense but seem perfectly logical in the moment."
    ),
    (
        "I've been awake for what feels like several days, and time has lost all meaning because minutes feel like "
        "hours and hours feel like minutes depending on the task."
    ),
    (
        "My body is staging a full rebellion against my brain's insistence that we keep going, and honestly I think my "
        "body might be winning this particular battle today."
    ),
    (
        "I'm functioning at such a low level that I'm impressed I managed to get dressed this morning, even if I did "
        "put my shirt on inside out without noticing."
    ),
    (
        "I've yawned so many times today that I've lost count somewhere after fifty, and each yawn feels like my "
        "body's desperate plea for the sleep I'm not giving it."
    ),
    (
        "My brain fog is so thick today that I could probably cut it with a knife, and finding my way through simple "
        "tasks feels like navigating a maze blindfolded."
    ),
    (
        "I'm so exhausted that I've started making deals with myself about when I can rest, bargaining for just a few "
        "more minutes of productivity before I completely shut down."
    ),
    (
        "I've been running on fumes for so long that I've forgotten what it feels like to have a full tank, and I'm "
        "not sure I'd recognize the feeling anymore."
    ),
    (
        "My concentration has completely abandoned me, leaving me to stare blankly at things while my brain refuses to "
        "engage with anything more complex than basic breathing and blinking."
    ),
    (
        "I'm at the point where I've accepted that nothing I produce today will be my best work, because my best work "
        "requires a version of me that actually slept."
    ),
    (
        "I've tried every trick I know to stay awake, from cold water on my face to jumping jacks, and nothing is "
        "working because my body has decided it's done."
    ),
    (
        "My exhaustion has reached a level where I'm not sure if I'm awake or just dreaming that I'm awake, and the "
        "distinction has become increasingly difficult to determine."
    ),
    (
        "I'm so tired that I've started seeing my bed in my peripheral vision even when I'm nowhere near it, like a "
        "mirage in a desert of endless wakefulness."
    ),
    (
        "I've been pushing through this fatigue with the promise of rest that keeps getting postponed, and my body is "
        "losing faith in my ability to deliver on that promise."
    ),
    (
        "My eyelids are staging a coup against my will to stay awake, slowly closing despite my best efforts to keep "
        "them open and engaged with the world around me."
    ),
    (
        "I'm functioning purely on the fear of what will happen if I stop, because I know the moment I sit down "
        "somewhere comfortable, I'll be unconscious within seconds."
    ),
    # LONG SENTENCES - QUESTIONS (CLOSE TO 37 WORDS)
    (
        "Why is it that my brain decides to become hyperactive and think about every possible thing the moment I "
        "finally lie down to get some desperately needed rest?"
    ),
    (
        "How is it possible that I can be this exhausted and still have insomnia, like my body is too tired to sleep "
        "which makes absolutely no logical sense?"
    ),
    (
        "Why does society expect me to function like a normal human being when I've been running on four hours of "
        "sleep for the past week straight now?"
    ),
    (
        "How do people with kids or demanding jobs ever manage to get enough sleep, because I can barely handle my own "
        "schedule and I'm still completely exhausted?"
    ),
    (
        "Why does my body insist on waking me up at five in the morning on the one day I actually have the chance to "
        "sleep in and rest?"
    ),
    (
        "Is there a scientific explanation for why being overtired makes you feel simultaneously wired and exhausted, "
        "because I'd really like to understand what's happening to me right now?"
    ),
    (
        "How am I supposed to make important decisions when my brain is operating at the cognitive level of a sleep "
        "deprived toddler who missed their afternoon nap?"
    ),
    (
        "Why does exhaustion make everything feel so emotionally overwhelming, like I could cry over a commercial or "
        "laugh hysterically at absolutely nothing at all right now?"
    ),
    (
        "How is it that I can fall asleep accidentally in the most uncomfortable positions but can't seem to drift off "
        "when I'm actually lying in my cozy bed?"
    ),
    (
        "Why do I always seem to get my best ideas right when I'm about to fall asleep, forcing me to choose between "
        "rest and potentially forgetting something brilliant?"
    ),
    (
        "Is it normal to feel like my bones are tired, like the exhaustion has seeped so deep into my body that even "
        "my skeleton needs a break now?"
    ),
    (
        "How many cups of coffee is too many cups of coffee, because I've lost count and I'm still tired so clearly "
        "whatever number I'm at isn't enough?"
    ),
    (
        "Why does being tired make me crave terrible food choices, like my body thinks sugar and carbs will somehow "
        "replace the sleep I'm not getting right now?"
    ),
    (
        "How is it that I can be so tired during the day but the moment night comes and I can actually sleep, suddenly "
        "I'm wide awake again?"
    ),
    (
        "Why does my brain choose three in the morning to remind me of that embarrassing thing I did in middle school "
        "instead of letting me sleep peacefully?"
    ),
    (
        "Is there a support group for people who are perpetually exhausted, because I feel like I need to talk to "
        "others who understand this level of constant fatigue?"
    ),
    (
        "How do I explain to people that I'm not lazy, I'm just so profoundly tired that even basic tasks feel like "
        "climbing mountains with weights on my back?"
    ),
    (
        "Why is it that the more tired I get, the harder it becomes to actually fall asleep, like my body is playing "
        "some cruel joke on itself and me?"
    ),
    (
        "How am I expected to be a functioning adult when I can barely remember what I had for breakfast or if I even "
        "ate breakfast at all today?"
    ),
    (
        "Why does exhaustion make time move so strangely, where five minutes can feel like an hour and an hour can "
        "disappear in what feels like five minutes?"
    ),
]

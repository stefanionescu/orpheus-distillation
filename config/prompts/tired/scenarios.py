"""Tired prompts: tired scenarios and long statements."""

from __future__ import annotations

SCENARIOS: list[str] = [
    # ADDITIONAL LONG - VARIOUS TIRED SCENARIOS (CLOSE TO 37 WORDS)
    (
        "I'm so tired that I've been wearing my shirt inside out all day and nobody told me, or maybe they did and I "
        "just don't remember because my brain isn't recording memories anymore."
    ),
    (
        "My exhaustion has reached the point where I'm having trouble distinguishing between things I actually did and "
        "things I only thought about doing, which is becoming a real problem at work today."
    ),
    (
        "I've been so sleep deprived this week that I've started having vivid daydreams that feel more real than my "
        "actual reality, and the line between them is getting dangerously blurry now."
    ),
    (
        "I'm functioning at such a low level that I've impressed myself by managing to put on matching socks this "
        "morning, even though I later realized they were both from different pairs anyway."
    ),
    (
        "My tiredness has made me hypersensitive to every minor inconvenience, and things that normally wouldn't "
        "bother me at all are now triggering disproportionate emotional responses that I can't seem to control."
    ),
    (
        "I've reached the stage of exhaustion where I'm too tired to even watch television, because following a plot "
        "requires more cognitive engagement than my depleted brain can currently provide right now."
    ),
    (
        "I'm so drained that I've started having philosophical thoughts about the nature of consciousness and whether "
        "I'm actually awake or just dreaming that I'm awake in some kind of exhausted loop."
    ),
    (
        "My sleep deprivation has made me oddly nostalgic for nap time in kindergarten, and I now deeply regret every "
        "single time I resisted taking a nap when I was a child."
    ),
    (
        "I've been awake so long that coffee has stopped being a stimulant and has become more of a comfort ritual, "
        "something warm to hold while I contemplate my exhausted existence quietly."
    ),
    (
        "My tiredness is so profound that I've started to feel a strange kinship with zombies, finally understanding "
        "their slow shuffling movements and their single minded focus on basic needs like rest."
    ),
    (
        "I'm so exhausted that I've been staring at my to do list for twenty minutes without doing anything on it, the "
        "gap between intention and action widened by my complete lack of energy."
    ),
    (
        "My body has started making involuntary sounds of exhaustion, sighs and groans that escape without my "
        "permission every time I have to stand up or move from one place to another today."
    ),
    (
        "I've gotten to the point where I'm genuinely concerned about my ability to drive safely, because my reaction "
        "times are so slow that I might as well be operating the car underwater."
    ),
    (
        "My exhaustion has given me a newfound appreciation for every single person who has ever worked a night shift, "
        "because I now understand the special kind of torture that comes with fighting your body's natural rhythms."
    ),
    (
        "I'm so tired that I've started making promises to my future self about better sleep habits, knowing full well "
        "that future me will probably ignore them just like present me ignored past me's promises."
    ),
    (
        "My brain fog is so dense today that I've walked into the same room four times without remembering why I went "
        "there, each time standing confused before giving up and walking back out again."
    ),
    (
        "I've reached the point of exhaustion where even my dreams are about being tired, like my subconscious can't "
        "escape the reality of how drained I am even when I finally get to sleep."
    ),
    (
        "My tiredness has affected my appetite in weird ways, alternating between not wanting to eat anything at all "
        "and suddenly craving the most random comfort foods at the most inconvenient times possible."
    ),
    (
        "I'm so sleep deprived that I've started to find things funny that aren't funny at all, laughing at random "
        "words and concepts because my tired brain has lost its ability to filter appropriately."
    ),
    (
        "My exhaustion has made me weirdly honest, because I don't have the energy to maintain social niceties or "
        "filter my thoughts before they come out of my mouth anymore today unfortunately."
    ),
    (
        "I've been running on so little sleep that my immune system has started to fail, and I can feel myself getting "
        "sick on top of being exhausted which is just adding insult to injury."
    ),
    (
        "My tiredness is so extreme that I've started to hallucinate the sound of my alarm clock, hearing phantom "
        "beeps that make me think I've overslept when I haven't even gone to bed yet."
    ),
    (
        "I'm so drained that I've lost the ability to estimate time accurately, what feels like five minutes turns out "
        "to be an hour and what feels like an hour was actually just ten minutes."
    ),
    (
        "My sleep deprivation has reached the point where I'm getting emotional about random acts of kindness, nearly "
        "crying when someone held the door open for me because it felt so unexpectedly meaningful today."
    ),
    (
        "I've been awake so long that I've started to feel disconnected from my own body, like I'm piloting a very "
        "tired meat suit from somewhere slightly outside of it which is disconcerting."
    ),
    (
        "My exhaustion has made me incredibly indecisive, unable to commit to even the simplest choices because my "
        "brain doesn't have enough power to weigh options and reach conclusions anymore about anything at all."
    ),
    (
        "I'm so tired that I've started speaking in incomplete sentences, trailing off mid thought because I've "
        "forgotten where I was going with my point before I could finish making it to anyone."
    ),
    (
        "My fatigue has given me a new perspective on the phrase sleeping like a baby, because I now understand that "
        "babies wake up constantly and that sounds absolutely terrible and not restful at all."
    ),
    (
        "I've reached the stage of tired where I'm simultaneously too wired to sleep and too exhausted to do anything "
        "productive, stuck in this useless limbo of unproductive wakefulness that benefits nobody including me."
    ),
    (
        "My sleep debt has accumulated interest to the point where I'm not sure I could ever fully pay it back, like "
        "I'd need to sleep for a month straight just to break even now."
    ),
    (
        "I'm so exhausted that I've started to resent people who look well rested, irrationally jealous of their "
        "bright eyes and alert expressions while I shuffle around like a zombie in human clothing today."
    ),
    (
        "My tiredness has made me paranoid about falling asleep at inappropriate moments, constantly pinching myself "
        "and shifting positions to stay awake during meetings and conversations where dozing off would be extremely "
        "embarrassing for me."
    ),
    (
        "I've been running on empty for so long that I've started to romanticize sleep in ways that are probably "
        "unhealthy, thinking about my bed the way people think about tropical vacation destinations they dream of."
    ),
    (
        "My exhaustion has stripped away my ability to multitask, and now I can barely single task, focusing on one "
        "thing at a time with the kind of intense concentration that comes from having no spare cognitive resources."
    ),
    (
        "I'm so tired that I've started to feel genuinely angry at past me for not going to bed earlier, holding a "
        "grudge against a version of myself that no longer exists."
    ),
    # MORE LONG PROMPTS - STATEMENTS (30-37 WORDS)
    (
        "I've been so exhausted lately that I've started having dreams about sleeping, and even in those dreams I wake "
        "up tired which feels like a cruel cosmic joke my brain is playing on me."
    ),
    (
        "My fatigue has reached a point where I'm making spelling mistakes in words I've known how to spell since "
        "elementary school, my brain too tired to access even basic stored information properly."
    ),
    (
        "I'm so drained that I've started to zone out during conversations and then panic when I realize someone asked "
        "me a question and I have absolutely no idea what we were discussing."
    ),
    (
        "My tiredness has affected my ability to recognize faces, and I've walked past people I know without "
        "acknowledging them because my brain couldn't process their features fast enough to identify them."
    ),
    (
        "I've gotten so used to being exhausted that I've forgotten what normal energy levels feel like, and I'm "
        "starting to wonder if I've ever actually experienced being truly well rested before."
    ),
    (
        "My sleep deprivation has made me hypersensitive to noise, and sounds that normally wouldn't bother me at all "
        "are now grating on my nerves like nails on a chalkboard constantly."
    ),
    (
        "I'm so tired that I've started making backup plans for my backup plans because I don't trust my exhausted "
        "brain to remember or execute the original plan correctly at all."
    ),
    (
        "My exhaustion has turned me into a different person, someone shorter tempered and less patient than I "
        "normally am, and I don't like this tired version of myself very much."
    ),
    (
        "I've been running on so little sleep that my body has started to ache in places I didn't know could ache, "
        "like tiredness has become a physical presence in my bones."
    ),
    (
        "My fatigue is so severe that I've considered calling in sick to work just to sleep, even though technically "
        "exhaustion isn't an illness even if it certainly feels like one right now."
    ),
    (
        "I'm so drained that I've lost the ability to enjoy things I normally love, because appreciation requires "
        "energy and I'm running on completely empty with nothing left to give anything."
    ),
    (
        "My tiredness has made me unreasonably emotional about small things, and I found myself getting teary eyed "
        "over a commercial about paper towels which is definitely not a normal reaction."
    ),
    (
        "I've reached the point of exhaustion where I'm laughing at things that aren't funny and not laughing at "
        "things that are, my sense of humor completely scrambled by lack of sleep."
    ),
    (
        "My sleep deprivation has affected my handwriting to the point where I can barely read my own notes, the "
        "letters shaky and uneven like a toddler learning to write for the first time."
    ),
    (
        "I'm so tired that I've started to feel a strange sense of accomplishment just for making it through each "
        "hour, celebrating tiny victories that wouldn't normally register as achievements at all."
    ),
    (
        "My exhaustion has made me crave comfort in weird ways, wanting to be wrapped in blankets and held like a "
        "child because I'm too tired to take care of myself properly."
    ),
    (
        "I've been awake so long that I've started to feel like I'm moving through water, every action requiring extra "
        "effort as if the air itself has become thick and resistant."
    ),
    (
        "My fatigue has stripped away my social filter, and I've been saying things out loud that I would normally "
        "keep to myself because I'm too tired to maintain proper boundaries."
    ),
    (
        "I'm so drained that I've started having trouble with depth perception, bumping into door frames and "
        "misjudging distances because my tired eyes can't quite figure out where things are in space."
    ),
    (
        "My tiredness has made me nostalgic for times when I had energy, looking back at photos of myself looking "
        "alert and wondering who that well rested person even was anymore."
    ),
    (
        "I've gotten to the point where I'm so exhausted that I've circled back around to a weird kind of calm, too "
        "tired to even feel stressed about being tired anymore."
    ),
    (
        "My sleep debt is so significant that I've started to think of rest as a luxury rather than a necessity, "
        "something other people get to have but not me apparently."
    ),
    (
        "I'm so tired that I've developed a new appreciation for chairs, seeing every seated opportunity as a chance "
        "to rest my weary legs and conserve what little energy I have left."
    ),
    (
        "My exhaustion has made time feel strange, with some moments stretching out forever and others disappearing "
        "entirely, my perception completely warped by the fog of sleep deprivation clouding everything."
    ),
    (
        "I've been running on empty for so long that I've started to feel disconnected from my own emotions, like "
        "they're happening to someone else and I'm just observing from a distance."
    ),
    (
        "My fatigue has turned simple tasks into complex challenges, and things like making breakfast or getting "
        "dressed now require the kind of planning usually reserved for major life events."
    ),
    (
        "I'm so drained that I've started to fantasize about sleep the way other people fantasize about vacations, "
        "imagining myself lying down and resting for hours with nothing to disturb me."
    ),
    (
        "My tiredness has affected my ability to regulate my body temperature, and I keep alternating between being "
        "too hot and too cold without any change in the actual environment around me."
    ),
    (
        "I've reached the stage of exhaustion where I'm too tired to complain about being tired, which is really "
        "saying something because complaining usually doesn't require much energy at all."
    ),
    (
        "My sleep deprivation has made me paranoid about my own competence, constantly second guessing decisions I "
        "would normally make confidently because I don't trust my exhausted judgment anymore at all."
    ),
]

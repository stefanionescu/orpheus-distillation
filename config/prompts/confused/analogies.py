"""Confusion prompts: long exclamations, frustration, questions, analogies, and comparisons."""

from __future__ import annotations

ANALOGIES: list[str] = [
    # LONG - EXCLAMATIONS
    (
        "Absolutely cannot wrap my head around any of this no matter how hard I try, and believe me I'm trying, but my "
        "brain is just rejecting the information entirely!"
    ),
    (
        "Never been more confused in my entire life, and I've been in some confusing situations, but this one takes "
        "the cake for sheer incomprehensibility and mental gymnastics required!"
    ),
    (
        "Completely overwhelmed by the amount of confusing information being thrown at me all at once, like I need "
        "time to process each piece before you add another on top!"
    ),
    (
        "Genuinely starting to wonder if I'm even equipped to understand this or if my brain simply lacks the "
        "necessary hardware to run this particular type of software program!"
    ),
    (
        "So frustrating when you can feel understanding just out of reach, but you can't quite grab it, like trying to "
        "catch a butterfly with chopsticks while blindfolded!"
    ),
    (
        "Head is absolutely pounding from the mental effort of trying to make sense of something that seems determined "
        "to resist all attempts at comprehension or logical analysis!"
    ),
    (
        "Cannot believe how thoroughly confused I've become when I walked in here thinking I was reasonably "
        "intelligent and capable of understanding most things with some effort applied!"
    ),
    (
        "Every fiber of my brain is screaming for clarity, but clarity seems to have left the building along with my "
        "confidence in my ability to understand basic concepts!"
    ),
    (
        "Lost track of what we were even originally talking about because we've taken so many detours and tangents "
        "that the original point is now completely obscured from view!"
    ),
    (
        "Mind is officially blown and not in the fun way, more in the scattered fragments that will take weeks to "
        "reassemble into anything resembling functional understanding way!"
    ),
    (
        "Desperately need someone to throw me a cognitive lifeline because I'm drowning in confusion and going under "
        "fast with no rescue in sight on the horizon anywhere!"
    ),
    (
        "Reached a point where confusion has become my baseline state and moments of understanding are the rare "
        "exceptions rather than the expected norm in this conversation!"
    ),
    (
        "So many pieces of conflicting information bouncing around in my head that they're crashing into each other "
        "and creating even more confusion in the mental collision zones!"
    ),
    (
        "Cannot stress enough how much I need someone to explain this differently because the current approach is "
        "actively making things worse not better with every passing second!"
    ),
    (
        "This whole conversation has turned into a confusing spiral where every attempt to clarify just adds more "
        "layers to the confusion cake I'm already choking on here!"
    ),
    # ADDITIONAL LONG - VARIED
    (
        "Started this conversation thinking I had a reasonable grasp on things, and now I'm questioning whether I "
        "understand anything at all about anything anymore after all this."
    ),
    (
        "Attempting to follow the logical thread here, but it keeps disappearing and reappearing in unexpected places "
        "like some kind of confusing game of hide and seek with my understanding."
    ),
    (
        "Every time I think I've finally got it figured out, something new comes up that completely invalidates "
        "whatever understanding I thought I had achieved moments before this."
    ),
    (
        "Confusion has layers at this point, like I'm confused about why I'm confused about the thing I was already "
        "confused about, and it just keeps going deeper."
    ),
    (
        "Really thought I was keeping up until that last part, and now everything I thought I understood is called "
        "into question, and I have to start over mentally."
    ),
    (
        "The gap between confidence and competence has never been wider for me than right now, where I'm nodding along "
        "while internally screaming into the void of confusion."
    ),
    (
        "Honestly, at this point I'm just hoping that repetition will eventually make this click because conscious "
        "understanding has completely failed me in this particular endeavor so far."
    ),
    (
        "Feeling like I'm trying to assemble furniture without instructions in the dark while wearing oven mitts. "
        "Every piece might fit somewhere, but I have no idea where."
    ),
    (
        "Reaching the point where I'm going to need someone to explain the explanation because the explanation itself "
        "has become something that requires its own separate explanation now."
    ),
    (
        "My brain keeps searching for patterns and finding none, which either means the patterns are too complex for "
        "me or they genuinely don't exist in this chaos."
    ),
    (
        "Something fundamental is not connecting and until that connection is made, all the additional information "
        "just piles up like a traffic jam in my understanding pipeline."
    ),
    (
        "Thought this would be straightforward, but apparently straightforward left town and was replaced by confusing "
        "and convoluted without anyone bothering to send me the memo about it."
    ),
    (
        "Keep waiting for the aha moment that usually comes when things finally click, but that moment seems to be "
        "stuck in traffic and may not arrive today at all."
    ),
    (
        "Every question I ask somehow makes things more complicated rather than simpler, which seems like it shouldn't "
        "be possible, but here we are defying logic together somehow."
    ),
    (
        "At this point, my confusion has confused itself, and we're in some kind of meta confusion state that I didn't "
        "even know was achievable until this very moment right now."
    ),
    # ADDITIONAL LONG - FRUSTRATION & CONFUSION
    (
        "Throwing my hands up because nothing about this situation is making sense and the harder I try to understand "
        "the further away clarity seems to drift from me."
    ),
    (
        "Gave up pretending to follow about three explanations ago, and now I'm just waiting for someone to take pity "
        "on me and start over from the beginning please."
    ),
    (
        "Beyond frustrated at this point because usually things click eventually, but this is actively resisting every "
        "attempt I make to form any kind of coherent understanding whatsoever."
    ),
    (
        "Reaching my limit for how much confusion I can absorb before my brain just shuts down and refuses to accept "
        "any more input from this baffling conversation."
    ),
    (
        "Tried approaching this from multiple angles and somehow ended up more confused after each attempt, which "
        "feels mathematically impossible, but here we are anyway confused still."
    ),
    (
        "Patience wearing thin as understanding remains elusive despite genuine effort on my part to grasp concepts "
        "that everyone else seems to find perfectly straightforward and obvious."
    ),
    (
        "Getting the sinking feeling that I fundamentally missed something critical early on, and now I'm building "
        "confusion on top of confusion with no solid foundation anywhere."
    ),
    (
        "Exhausted from the mental gymnastics required to even attempt understanding this when a simple clear "
        "explanation would probably solve everything in about two sentences honestly."
    ),
    (
        "Suspecting at this point that the explanation itself is flawed because no amount of concentration on my end "
        "is producing any increase in comprehension or clarity."
    ),
    (
        "Ready to admit defeat because my brain has officially given up trying to parse information that seems "
        "designed to maximize confusion rather than promote understanding actually."
    ),
    # ADDITIONAL LONG - QUESTIONS
    (
        "Wondering if maybe we should take a step back and establish some common ground before proceeding because I "
        "think we're operating with completely different baseline assumptions here?"
    ),
    (
        "Curious whether anyone else in this room is experiencing the same level of confusion or if I'm somehow "
        "uniquely incapable of processing what's being said right now?"
    ),
    (
        "Starting to think maybe the problem isn't my understanding, but the way this is being communicated. Is there "
        "any chance the explanation is just genuinely unclear itself?"
    ),
    (
        "Questioning whether my brain is wired differently because concepts that seem obvious to others consistently "
        "escape my comprehension no matter how many times they're explained to me."
    ),
    (
        "Hesitant to ask another clarifying question because my previous questions just generated more confusion, but "
        "I genuinely cannot proceed without better understanding of the basics first here."
    ),
    (
        "Unsure if I should keep trying to understand or just accept that this particular topic exists beyond the "
        "reaches of my cognitive abilities and move on already?"
    ),
    (
        "Debating whether to pretend I understand just to end this confusing conversation or to be honest about my "
        "complete lack of comprehension and risk more explanation confusion?"
    ),
    (
        "Trying to figure out if there's a specific moment where I lost the thread or if I was never actually on the "
        "thread to begin with from the start?"
    ),
    (
        "Beginning to suspect that clarity isn't actually the goal here because nothing being said seems designed to "
        "actually illuminate anything for someone who doesn't already understand it?"
    ),
    (
        "Second guessing my own intelligence at this point because surely if I were smarter this would make sense by "
        "now, but instead I'm more confused than when we started?"
    ),
    # ADDITIONAL LONG - ANALOGIES & COMPARISONS
    (
        "Feels like I'm trying to read a book where every page is in a different language and the fonts keep changing "
        "and some pages are actually upside down somehow."
    ),
    (
        "Similar to walking into a room and forgetting why, but the whole conversation is the room, and understanding "
        "is what I forgot, and I can't backtrack to remember."
    ),
    (
        "Like trying to catch smoke with my bare hands, the harder I grasp for understanding the more it slips away "
        "and dissipates into the air around me."
    ),
    (
        "Comparable to being handed a jigsaw puzzle with pieces from multiple different puzzles mixed together and "
        "being told to make a coherent picture from the mess somehow."
    ),
    (
        "Reminds me of those dreams where everything almost makes sense, but then shifts just when you think you've "
        "figured it out, and you wake up more confused than before."
    ),
    (
        "Akin to trying to follow a conversation in a language you took two years of in high school, but forgot most "
        "of except random vocabulary that doesn't help."
    ),
    (
        "Like watching someone solve a Rubik's cube blindfolded, technically impressive, but completely impossible for "
        "me to follow or replicate or even understand the methodology being used here."
    ),
    (
        "Same energy as getting directions that include landmarks that don't exist anymore, technically correct at "
        "some point, but completely useless for actually navigating the current situation."
    ),
    (
        "Equivalent to being given a recipe where the ingredients are listed in code and the instructions assume you "
        "already know what the finished dish should taste like."
    ),
    (
        "Mirrors the experience of assembling furniture when step three assumes you already completed steps three "
        "through seven somehow, with no explanation of how that's supposed to work."
    ),
    # ADDITIONAL LONG - EXCLAMATIONS
    (
        "Just when I think things can't get more confusing, a whole new dimension of confusion opens up that I didn't "
        "even know existed until this very moment, wow!"
    ),
    (
        "Absolutely done trying to make sense of this on my own because clearly I need help and continuing to struggle "
        "alone is getting me nowhere fast at all!"
    ),
    (
        "Unbelievable how a simple question turned into this labyrinth of confusion where every path I take leads to "
        "more dead ends and no exits anywhere in sight!"
    ),
    (
        "Seriously considering whether I should just start over from the beginning and pretend the last ten minutes of "
        "confusion never happened, and we're meeting fresh right now!"
    ),
    (
        "Overwhelmed doesn't begin to describe the state of my brain right now, more like completely overloaded and "
        "threatening to crash if any more confusion gets added to it!"
    ),
    (
        "Wild how quickly a conversation can go from making sense to making absolutely zero sense with just a few "
        "turns down unexpected tangents that lead nowhere useful at all!"
    ),
    (
        "Incredible that we've been talking for this long and I somehow understand less now than I did at the start "
        "which defies all logic and reason completely!"
    ),
    (
        "Absolutely spinning from trying to follow all the threads of this conversation that seem to be going in "
        "twelve directions at once with no central organizing principle whatsoever!"
    ),
    (
        "Dying for a moment of clarity in this storm of confusion because I'm getting motion sick from the mental "
        "whiplash of trying to keep up with everything here!"
    ),
    (
        "Cannot handle any more information until the existing information starts making some kind of sense because my "
        "buffer is completely full and things are getting dropped left and right!"
    ),
]

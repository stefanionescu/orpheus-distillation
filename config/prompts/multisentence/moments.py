"""Multi-sentence prompts about emotional moments, then mixed conversation."""

from __future__ import annotations

MOMENTS: list[str] = [
    # EMOTIONAL MOMENTS (~22 WORDS AVG)
    (
        "The graduation ceremony brought tears I didn't expect. Watching them cross that stage made every sacrifice "
        "feel worthwhile and necessary."
    ),
    (
        "The anniversary of the loss hit harder this year than last. Grief doesn't follow a predictable timeline no "
        "matter what anyone says."
    ),
    (
        "The reunion with family after years apart was overwhelming in the best way. Distance makes appreciation grow "
        "in ways proximity sometimes doesn't."
    ),
    (
        "The unexpected kindness from a stranger during a difficult moment restored something I didn't realize I'd "
        "lost. Faith in people perhaps."
    ),
    (
        "The song that played during the drive brought up emotions I'd buried. Music unlocks chambers in the heart "
        "that words can't reach."
    ),
    (
        "The achievement I worked toward for years finally happened yesterday. The feeling is different than I "
        "imagined; more relief than celebration."
    ),
    (
        "The argument with my parent touched on wounds that never fully healed. Some conversations excavate pain we've "
        "built entire identities avoiding."
    ),
    (
        "The birth of my niece shifted something fundamental in how I see the world. New life entering changes "
        "everyone it touches."
    ),
    (
        "The farewell at the airport felt more permanent than previous ones somehow. Some goodbyes carry weight we "
        "don't anticipate beforehand."
    ),
    (
        "The moment I realized the relationship was over happened in an ordinary instant. Major life changes often "
        "arrive without dramatic announcement."
    ),
    (
        "The pride in their eyes when they looked at me meant more than the accomplishment itself. Validation from "
        "people we love matters most."
    ),
    (
        "The fear that gripped me when the call came late at night remains visceral. Some moments etch themselves into "
        "cellular memory permanently."
    ),
    (
        "The relief when the test results came back was physical not just mental. My body had been holding tension I "
        "wasn't aware of."
    ),
    (
        "The forgiveness I offered changed me more than it changed them. Releasing resentment creates space for things "
        "more worth carrying."
    ),
    (
        "The joy that surprised me during an ordinary moment was profound. Happiness often arrives uninvited when we "
        "stop demanding its presence."
    ),
    (
        "The loss of the pet affected me more deeply than I'd anticipated. They become family without us consciously "
        "deciding to let them."
    ),
    (
        "The standing ovation after the performance validated years of work and doubt. Some moments make every "
        "sacrifice that preceded them worthwhile."
    ),
    (
        "The connection I felt with a complete stranger was instant and inexplicable. Some people's energy aligns with "
        "ours for reasons beyond understanding."
    ),
    (
        "The realization that my parents are aging hit during a mundane moment. Time's passage becomes undeniable in "
        "accumulated small observations."
    ),
    (
        "The peace I found in solitude surprised me after years of fearing being alone. Sometimes the company we need "
        "most is our own."
    ),
    # MIXED CONVERSATIONAL (~22 WORDS AVG)
    (
        "The recipe turned out nothing like the picture despite following instructions exactly. Either I'm missing "
        "something obvious or food photography is pure deception."
    ),
    (
        "The meeting that could have been an email lasted ninety minutes. My patience for performative productivity "
        "decreases with every passing year."
    ),
    (
        "The plant I was sure I'd killed somehow came back to life. Nature's resilience exceeds our capacity to "
        "destroy it sometimes."
    ),
    (
        "The podcast recommended by multiple people finally clicked on the third attempt. Sometimes we're not ready "
        "for things until we are."
    ),
    (
        "The documentary changed how I think about a topic I thought I understood. Learning how much we don't know is "
        "humbling."
    ),
    (
        "The conversation with my child about a difficult topic went better than expected. They understand more than "
        "we give them credit for."
    ),
    (
        "The silence during the car ride said more than any words could have. Sometimes shared quiet communicates what "
        "language cannot."
    ),
    (
        "The first bite of that dish transported me to a specific memory instantly. Taste connects to the past as "
        "powerfully as scent does."
    ),
    (
        "The sunrise I almost missed because I hit snooze turned out to be spectacular. The universe rewards showing "
        "up even when tired."
    ),
    (
        "The book I resisted reading for years became one of my favorites immediately. Our resistance often points "
        "toward what we need most."
    ),
    (
        "The compromise we reached satisfied neither of us completely. But it preserved the relationship and that's "
        "worth some personal sacrifice."
    ),
    (
        "The routine I thought was boring has become the structure that keeps me sane. Predictability provides more "
        "comfort than I once admitted."
    ),
    (
        "The feedback I received was hard to hear but impossible to dismiss. Truth delivered kindly is still truth "
        "regardless of comfort."
    ),
    (
        "The detour forced by construction led us to discover a neighborhood we loved. Sometimes obstacles redirect us "
        "toward better destinations."
    ),
    (
        "The argument ended differently than our usual pattern. Growth happens in small moments of choosing "
        "differently than we have before."
    ),
    (
        "The dream I had last night felt significant but I can't interpret it. The subconscious speaks in symbols I "
        "don't always understand."
    ),
    (
        "The compliment I gave to a stranger made them visibly emotional. We underestimate the impact of acknowledging "
        "others generously and specifically."
    ),
    (
        "The tradition we started accidentally has become something the family protects fiercely. Rituals gain meaning "
        "through repetition and shared memory."
    ),
    (
        "The mistake I made publicly became a teaching moment I reference often. Failure witnessed becomes wisdom if "
        "we allow the transformation."
    ),
    (
        "The boundary I finally set has improved the relationship despite initial resistance. Protection of self "
        "enables healthier connection with others."
    ),
    (
        "The skill I thought I'd never master started clicking after persistent practice. Competence often arrives "
        "long after we expect its arrival."
    ),
    (
        "The news I dreaded receiving came with unexpected silver linings attached. Rarely is anything as entirely bad "
        "as anticipation suggests."
    ),
    (
        "The memory that resurfaced during therapy explained patterns I hadn't understood before. The past shapes the "
        "present in ways we don't notice."
    ),
    (
        "The gratitude practice I dismissed as trendy actually improved my outlook noticeably. Sometimes the things "
        "that sound simplistic work for good reason."
    ),
    (
        "The apology I received years after the incident still brought closure. Timing matters less than sincerity "
        "when healing old wounds."
    ),
    (
        "The choice between two good options is harder than choosing between good and bad. Abundance creates its own "
        "kind of difficulty."
    ),
    (
        "The moment of clarity came during the most mundane activity possible. Insight arrives on its own schedule "
        "regardless of our seeking."
    ),
    (
        "The person I judged harshly turned out to be dealing with circumstances I knew nothing about. Humility "
        "follows assumption's inevitable failure."
    ),
    (
        "The fear that kept me from trying was entirely disproportionate to the actual risk. Courage means acting "
        "despite the feeling not without it."
    ),
    (
        "The investment of time in something with no guaranteed return felt foolish initially. But the process taught "
        "me more than outcomes ever could."
    ),
    (
        "The thunderstorm knocked out the power for twelve hours straight. We lit candles and actually talked to each "
        "other like people used to."
    ),
    (
        "My commute takes exactly forty seven minutes door to door. I've listened to enough podcasts to have earned "
        "several honorary degrees by now."
    ),
    (
        "The email I've been avoiding requires a diplomatic response I don't have energy for. Tomorrow's problem, I "
        "keep telling myself repeatedly."
    ),
    (
        "The restaurant reservation is for seven but we both know we'll be late. Punctuality has never been our strong "
        "suit as a couple."
    ),
    (
        "The meditation app keeps telling me to clear my mind. Easier said than done when my thoughts refuse to "
        "cooperate politely."
    ),
    (
        "The grocery list somehow never includes the one thing I actually needed. This happens with suspicious "
        "regularity despite my best efforts."
    ),
    (
        "The password I created is so secure that I've now locked myself out. The irony isn't lost on me but it "
        "doesn't help."
    ),
    (
        "The traffic report mentioned an accident but didn't specify which lane. Now I'm committed to this route with "
        "no good alternatives."
    ),
    (
        "The voicemail notification has been sitting there for three days unlistened. Whatever it says probably isn't "
        "good news based on timing."
    ),
    (
        "The hotel room smells vaguely of cleaning products and previous guests. Not unpleasant exactly, but "
        "definitely not home either."
    ),
    (
        "The instructions for this furniture require an engineering degree apparently. Three hours in and I have extra "
        "parts that shouldn't exist."
    ),
    (
        "The autocomplete suggested something embarrassing based on my search history. Now I'm paranoid about who else "
        "might see that pattern."
    ),
    (
        "The elevator stopped between floors for fifteen terrifying seconds today. Long enough for me to contemplate "
        "every bad decision I've ever made."
    ),
    (
        "The checkout line moved steadily until I reached the front of course. Then everything ground to a halt "
        "requiring manager assistance."
    ),
    (
        "The umbrella I finally remembered to bring remained unused all day. The rain held off specifically to spite "
        "my preparedness."
    ),
    (
        "The parking spot I found seemed too good to be true initially. Reading the sign three times confirmed it "
        "actually was legitimate."
    ),
    (
        "The spreadsheet that made sense yesterday now looks like complete gibberish. Past me really should have added "
        "more documentation throughout."
    ),
    (
        "The notification sound made me grab my phone reflexively. Turns out it was someone else's phone not mine this "
        "time."
    ),
    (
        "The meeting invite arrived without an agenda or context whatsoever. Preparing for the unknown is my least "
        "favorite professional activity."
    ),
    (
        "The air freshener is working overtime but barely masking whatever died in here. Some battles against smell "
        "cannot be won easily."
    ),
    (
        "The movie everyone recommended turned out to be deeply unsettling. Not bad exactly, but definitely not what I "
        "expected either."
    ),
    (
        "The keyboard shortcut I accidentally discovered has changed my workflow completely. Efficiency hiding in "
        "plain sight for years apparently."
    ),
]

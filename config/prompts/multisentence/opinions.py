"""Multi-sentence prompts: longer talk about opinions, memories, and plans."""

from __future__ import annotations

OPINIONS: list[str] = [
    # LONGER CONVERSATIONAL - OPINIONS (~25 WORDS AVG)
    (
        "I genuinely believe that learning to cook a handful of basic dishes well is invaluable. It's one of the most "
        "important life skills anyone can develop."
    ),
    (
        "The expectation of constant availability that smartphones have created is genuinely exhausting. More people "
        "are starting to recognize the need for deliberate digital boundaries now."
    ),
    (
        "In my experience, the best conversations happen late at night when everyone's defenses are down. There's no "
        "pressure to maintain any particular facade or social performance."
    ),
    (
        "Most disagreements stem from different underlying values rather than different facts. This makes genuine "
        "persuasion much more difficult than people commonly assume it to be."
    ),
    (
        "The idea that you need to have your entire life figured out by a certain age seems increasingly outdated. "
        "Career paths are rarely linear anymore."
    ),
    (
        "There's tremendous value in maintaining friendships with people who have vastly different perspectives and "
        "life experiences. Even when those conversations can be challenging or uncomfortable."
    ),
    (
        "The pursuit of perfection often prevents people from starting projects at all. That's why I've learned to "
        "embrace good enough as a legitimate goal worth achieving."
    ),
    (
        "Society has collectively forgotten how to be bored. I wonder what we've lost by filling every idle moment "
        "with content consumption and digital stimulation constantly."
    ),
    (
        "The ability to change your mind when presented with new evidence is a sign of intellectual strength. Not "
        "weakness or inconsistency as some people seem to believe."
    ),
    (
        "The pressure to monetize every hobby and turn every passion into a side hustle is problematic. It makes it "
        "harder to simply enjoy activities for their intrinsic value."
    ),
    (
        "Most people are dealing with struggles invisible to others, which has made me more patient. I'm less quick to "
        "judge seemingly inexplicable behavior now."
    ),
    (
        "The cultural obsession with optimization and efficiency bothers me sometimes. I wonder if we've lost sight of "
        "what actually makes life meaningful beyond mere productivity."
    ),
    (
        "The best indicator of someone's character is how they treat people who can do absolutely nothing for them. "
        "Neither professionally nor socially in return."
    ),
    (
        "We undervalue the importance of simply being present with people without trying to fix their problems. "
        "Sometimes just listening without offering advice is what's needed."
    ),
    (
        "Comparing our behind the scenes reality with everyone else's highlight reel has created an epidemic of "
        "unnecessary inadequacy. We're dissatisfied with our own perfectly good lives."
    ),
    (
        "The most confident people I know are often the quickest to admit what they don't know. They're also the most "
        "willing to ask questions without embarrassment."
    ),
    (
        "The assumption that more choices always leads to greater happiness has been thoroughly debunked by research. "
        "Yet we continue overwhelming people with endless options anyway."
    ),
    (
        "Regular exposure to nature is as essential for mental health as exercise is for physical health. Yet it's "
        "rarely prescribed or prioritized by healthcare professionals."
    ),
    (
        "We romanticize being busy as a status symbol while complaining about having no time. That contradiction "
        "reveals something fundamental about modern life."
    ),
    (
        "Apologizing quickly and sincerely when you're wrong costs very little but builds tremendous trust and respect "
        "over time. It's a skill worth developing."
    ),
    # LONGER CONVERSATIONAL - MEMORIES (~25 WORDS AVG)
    (
        "I still remember the exact moment I realized my grandmother was getting older. She forgot my name briefly "
        "before catching herself with an embarrassed laugh."
    ),
    (
        "The summer I turned sixteen was transformative in ways I couldn't articulate at the time. Looking back now, I "
        "can see how it shaped everything that followed."
    ),
    (
        "My father used to say that the measure of a person isn't what they do when everyone watches. It's what they "
        "do when they think no one sees."
    ),
    (
        "There was a teacher in high school who believed in me when I didn't believe in myself. I've never forgotten "
        "how powerful that simple act of faith was."
    ),
    (
        "I once got lost in a foreign city where I didn't speak the language. A complete stranger walked me twenty "
        "minutes out of their way to help me."
    ),
    (
        "The night before my wedding, I barely slept because I kept replaying every significant moment of our "
        "relationship. Marveling at the unlikely chain of events that brought us here."
    ),
    (
        "My childhood best friend and I drifted apart after college. There's a particular kind of grief in losing "
        "someone who isn't gone but simply became a stranger."
    ),
    (
        "I vividly remember the first book that made me cry. I was so surprised that words on a page could evoke such "
        "a visceral physical response."
    ),
    (
        "The job interview that changed my career trajectory almost didn't happen. I nearly talked myself out of "
        "applying, convinced I wasn't qualified enough to bother trying."
    ),
    (
        "My grandfather built the desk I'm sitting at right now with his own hands over forty years ago. Every scratch "
        "on its surface tells a story."
    ),
    (
        "There was a period in my twenties when I felt completely directionless and lost. It terrified me at the time "
        "but taught me resilience I still draw on."
    ),
    (
        "The moment I held my child for the first time, every cliché about unconditional love suddenly made perfect "
        "sense. Words genuinely cannot capture that feeling adequately."
    ),
    (
        "I once witnessed a stranger perform an act of extraordinary kindness for another stranger. It restored my "
        "faith in humanity during a particularly cynical phase of my life."
    ),
    (
        "The house I grew up in was demolished years ago. Sometimes I dream about walking through rooms that no longer "
        "exist except in my increasingly unreliable memory."
    ),
    (
        "My mother used to hum while she cooked, always the same melody. Now whenever I hear that tune, I'm instantly "
        "transported back to our cramped kitchen."
    ),
    (
        "The first time I traveled alone internationally was terrifying and exhilarating in equal measure. It "
        "fundamentally changed how I understood my own capabilities and limitations."
    ),
    (
        "I still have the letter my grandmother wrote me before she passed. I've read it so many times that the paper "
        "has grown soft along the folds."
    ),
    (
        "There was a moment on an ordinary Tuesday when I realized I was genuinely happy with my life. It felt "
        "revolutionary after years of chasing some imaginary future."
    ),
    (
        "The mentor who shaped my early career recently retired. At her farewell party, I tried to articulate what her "
        "guidance meant but couldn't find adequate words."
    ),
    (
        "I remember exactly where I was standing when I learned news that divided my life into before and after. "
        "Certain events become permanent reference points in memory."
    ),
    # LONGER CONVERSATIONAL - PLANS & INTENTIONS (~25 WORDS AVG)
    (
        "I'm planning to finally learn how to play piano next year. I've talked about doing it for at least a decade "
        "without ever actually committing to lessons."
    ),
    (
        "We've been discussing the possibility of relocating to a different city. But the logistics of uprooting our "
        "entire established life feel increasingly overwhelming the more we research."
    ),
    (
        "My goal for this quarter is to establish a more consistent morning routine. One that actually sets me up for "
        "productive days instead of scrambling from the start."
    ),
    (
        "I want to start hosting dinner parties more regularly. My social life has become too reliant on digital "
        "interactions and occasional restaurant outings lately."
    ),
    (
        "We're seriously considering adopting a rescue dog, though we keep going back and forth. Our current lifestyle "
        "and apartment size might not accommodate a pet responsibly."
    ),
    (
        "I've been meaning to write more, whether journaling or something more creative. I keep finding excuses to "
        "avoid the vulnerability that putting words down requires."
    ),
    (
        "The plan is to pay off the remaining credit card balance by summer. Then we can finally start saving for a "
        "proper vacation instead of just weekend trips."
    ),
    (
        "I need to schedule that medical checkup I've been postponing for embarrassingly long. Especially given my "
        "family history and the importance of early detection for certain conditions."
    ),
    (
        "We're hoping to renovate the bathroom before my parents visit in October. The contractor estimates and "
        "timelines we've received so far have been discouraging and inconsistent though."
    ),
    (
        "My intention is to spend less time mindlessly scrolling through social media. I want more time on activities "
        "that actually leave me feeling energized rather than depleted."
    ),
    (
        "I've decided to pursue that certification I've been considering for months. Even though it means sacrificing "
        "several evenings a week for the next six months to complete coursework."
    ),
    (
        "We want to establish better boundaries around work hours. Remote arrangements have blurred the lines between "
        "professional obligations and personal time in unhealthy ways."
    ),
    (
        "The goal is to read at least two books per month this year. That seems modest but would represent a "
        "significant improvement over my recent annual totals honestly."
    ),
    (
        "I'm planning to finally address that difficult conversation I've been avoiding. The temporary discomfort of "
        "honesty is preferable to the ongoing tension of unspoken issues."
    ),
    (
        "We've agreed to review our budget together every month. Instead of avoiding the topic until financial stress "
        "forces an uncomfortable reckoning with our spending habits."
    ),
    (
        "My aim is to reconnect with old friends I've let drift away. Starting with a few specific people I've been "
        "meaning to reach out to for far too long."
    ),
    (
        "I want to develop a more sustainable approach to exercise. One that doesn't depend on motivation or gym "
        "access, incorporating movement naturally into my daily routine."
    ),
    (
        "The plan involves gradually transitioning to more plant based meals. Not necessarily becoming fully "
        "vegetarian but reducing our overall meat consumption for health and environmental reasons."
    ),
    (
        "I've committed to saying no more often to commitments that don't align with my priorities. Disappointing "
        "people in the short term remains genuinely difficult for me though."
    ),
    (
        "We're intending to create a more intentional approach to weekends. Balancing necessary errands with genuine "
        "rest and activities that bring actual joy and restoration."
    ),
]

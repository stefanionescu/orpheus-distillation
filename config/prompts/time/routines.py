"""Time prompts: long statements about waking, deadlines, and travel times."""

from __future__ import annotations

ROUTINES: list[str] = [
    # LONG STATEMENTS
    (
        "I woke up at exactly four twenty seven AM this morning because my neighbor's dog started barking, and now I'm "
        "exhausted but can't fall back asleep no matter how hard I try!"
    ),
    (
        "The wedding ceremony is scheduled to begin at precisely three o'clock PM, but knowing my family, nobody will "
        "actually be seated and ready until at least three thirty!"
    ),
    (
        "My flight departs at six fifteen AM tomorrow morning, which means I need to be at the airport by four AM, "
        "which means I need to wake up at three AM at the latest!"
    ),
    (
        "I've been staring at this clock since two thirty AM wondering why my brain won't shut off, and now it's "
        "almost five AM and I have to be at work by eight!"
    ),
    (
        "The concert doors open at seven PM but the main act doesn't come on until ten thirty PM, so we'll be standing "
        "around for three and a half hours waiting!"
    ),
    (
        "I can't believe I've been on this video call since nine AM and it's now quarter past one PM and we still "
        "haven't made a single decision about anything important!"
    ),
    (
        "My grandmother used to wake up at exactly five o'clock AM every single morning without an alarm, and now I "
        "understand why she always went to bed at eight PM!"
    ),
    (
        "The movie starts at seven forty five PM and it's a three hour epic, so we won't be getting out of the theater "
        "until almost eleven PM on a work night!"
    ),
    (
        "I set my alarm for six thirty AM but my body decided to wake me up at four AM instead, and now I've been "
        "lying here for two and a half hours!"
    ),
    (
        "The restaurant doesn't start serving dinner until five thirty PM, which seems ridiculously late when you've "
        "been hungry since three o'clock in the afternoon!"
    ),
    (
        "I remember exactly what I was doing at eight forty six AM on September eleventh, and that moment is forever "
        "frozen in my memory like a photograph!"
    ),
    (
        "The deadline is at eleven fifty nine PM tonight and I've been working on this project since six AM this "
        "morning with only two short breaks for food!"
    ),
    (
        "My body is convinced it's three AM because of the jet lag, but the clock says it's actually eleven in the "
        "morning and I need to function somehow!"
    ),
    (
        "The fireworks show is scheduled to start at exactly nine PM, but last year they didn't begin until nine "
        "twenty three PM and everyone was getting impatient!"
    ),
    (
        "I've been waiting in this line since seven thirty AM and the store doesn't even open until ten AM, but I "
        "really want to get the limited edition item!"
    ),
    (
        "The sunrise this morning at five thirty seven AM was absolutely breathtaking, with colors I've never seen "
        "before painting the entire sky in orange and pink!"
    ),
    (
        "My internal clock wakes me up at six fifteen AM every single day, including weekends, and I haven't used an "
        "alarm in over three years now!"
    ),
    (
        "The baby finally fell asleep at eleven forty five PM after we tried everything from rocking to singing to "
        "driving around the neighborhood for an hour!"
    ),
    (
        "I looked at the clock at one AM thinking I'd been asleep for hours, but I had only been in bed for twenty "
        "minutes and sleep felt impossible!"
    ),
    (
        "The meeting was supposed to end at two PM but the discussion went on until four thirty PM, and now I'm behind "
        "on everything else I needed to do!"
    ),
    (
        "My favorite bakery opens at five AM and sells out of their famous cinnamon rolls by seven thirty AM, so you "
        "really have to get there early!"
    ),
    (
        "The eclipse will reach totality at exactly two thirty seven PM in our time zone, and I've been planning this "
        "viewing party for months now!"
    ),
    (
        "I've been awake since three AM replaying every embarrassing thing I've ever said, and now it's six AM and I "
        "might as well just start my day!"
    ),
    (
        "The train leaves at seven twelve AM and if I miss it, the next one isn't until eight forty five AM, which "
        "would make me late for work!"
    ),
    (
        "My watch stopped at exactly twelve seventeen PM yesterday and I didn't notice until three PM when I wondered "
        "why time seemed to be standing still!"
    ),
    (
        "The pharmacy said my prescription would be ready by one PM, but when I arrived at two thirty PM, they said it "
        "would be another hour at least!"
    ),
    (
        "I scheduled my gym session for five thirty AM because that's the only time the equipment isn't being hogged "
        "by the after work crowd!"
    ),
    (
        "The power went out at three seventeen AM during the storm, and my phone alarm didn't go off at six AM because "
        "the battery had died overnight!"
    ),
    (
        "My grandmother's antique clock has been stuck at ten twenty three for as long as I can remember, and nobody "
        "has ever bothered to fix it!"
    ),
    (
        "The restaurant's happy hour runs from four to six PM with amazing deals, but I can never make it because I "
        "don't get off work until five thirty PM!"
    ),
    (
        "I finally submitted my assignment at eleven fifty eight PM, just two minutes before the midnight deadline, "
        "and my heart was pounding the entire time!"
    ),
    (
        "The sunset last night at eight forty two PM was so stunning that I sat on my porch for an extra hour just "
        "watching the colors fade!"
    ),
    (
        "My alarm is set for six twenty three AM because I've calculated that I need exactly thirty seven minutes to "
        "get ready and seven minutes to drive!"
    ),
    (
        "The ceremony will commence at precisely sixteen hundred hours according to the military style invitation, "
        "which confused half the guests who don't use that format!"
    ),
    (
        "I've been refreshing this website since eleven fifty nine PM waiting for the midnight drop, and now it's "
        "twelve oh three AM and the site crashed!"
    ),
    (
        "The doctor's office called to move my eleven fifteen AM appointment to two forty five PM, which completely "
        "messes up my entire afternoon schedule!"
    ),
    (
        "My body naturally wants to sleep from two AM to ten AM, but society insists I be functional at eight AM, and "
        "this conflict is destroying me!"
    ),
    (
        "The game starts at seven PM Eastern time, which is four PM for me on the West Coast, which is actually "
        "perfect for watching after work!"
    ),
    (
        "I looked at the clock at three AM, then what felt like five minutes later it was suddenly six thirty AM and "
        "my alarm was going off!"
    ),
    (
        "The museum is only open from ten AM to five PM on weekdays, which makes it nearly impossible to visit unless "
        "you take a day off work!"
    ),
    (
        "My morning routine takes exactly one hour and twenty three minutes, from my six AM alarm to walking out the "
        "door at seven twenty three AM!"
    ),
    (
        "The last train home leaves at eleven forty five PM, and if you miss it, you're stuck paying for an expensive "
        "taxi or sleeping at the station!"
    ),
    (
        "I've been counting down the seconds since eight AM this morning, and now it's finally five PM and I can "
        "escape this office for the weekend!"
    ),
    (
        "The thunderstorm rolled in at two seventeen AM and the lightning was so bright it lit up my entire bedroom "
        "like it was noon outside!"
    ),
    (
        "My phone died at exactly eight PM during the live stream of my favorite artist's concert, and I missed the "
        "entire second half of the show!"
    ),
    (
        "The meeting ran from nine AM to twelve thirty PM without a single break, and by the end I couldn't even "
        "remember what we discussed at the start!"
    ),
    (
        "I set exactly seventeen alarms between six AM and seven AM because I am physically incapable of waking up to "
        "just one alarm in the morning!"
    ),
    (
        "The coffee shop closes at seven PM, which is way too early for someone like me who does their best work "
        "between eight PM and midnight!"
    ),
    (
        "My flight was delayed from the original six fifteen AM departure to eight forty seven AM, and then again to "
        "ten thirty AM, and I just sat there!"
    ),
    (
        "The countdown to midnight on New Year's Eve is the most magical ten seconds of the year, when everything "
        "feels possible and the world holds its breath!"
    ),
    (
        "I've been awake since four AM because my brain decided that was the perfect time to remember every mistake "
        "I've ever made in my entire life!"
    ),
    (
        "The bakery's fresh bread comes out of the oven at exactly six AM, and the smell wafting down the street is "
        "worth waking up early for!"
    ),
    (
        "My grandmother always said nothing good happens after midnight, and now that I'm older, I realize she was "
        "absolutely right about that!"
    ),
    (
        "The interview is scheduled for two fifteen PM, and I've been anxiously watching the clock since I woke up at "
        "six AM this morning!"
    ),
    (
        "I finally fell asleep at three thirty AM after tossing and turning for hours, only to be woken by my alarm at "
        "six AM feeling like death!"
    ),
    (
        "The store opens at nine AM sharp, and there were already fifty people in line when I arrived at eight thirty "
        "AM hoping to beat the crowd!"
    ),
    (
        "My watch says it's four twenty seven PM but my computer says four twenty nine PM, and this two minute "
        "discrepancy is driving me absolutely insane!"
    ),
    (
        "The sunset happens at different times throughout the year, and I love tracking how it shifts from around five "
        "PM in winter to almost nine PM in summer!"
    ),
    (
        "I've been on hold with customer service since eleven AM, and it's now two thirty PM, and the hold music is "
        "permanently burned into my brain!"
    ),
    (
        "The baby has been crying since two AM and it's now almost five AM, and I don't remember what sleep feels like "
        "anymore at this point!"
    ),
    (
        "My flight lands at fourteen twenty three according to the app, but with taxi time it'll probably be closer to "
        "fourteen forty before I'm actually off the plane!"
    ),
    (
        "The concert venue says doors open at six thirty PM, but the opening act doesn't start until eight PM, and the "
        "headliner isn't on until ten PM!"
    ),
    (
        "I checked my phone at four AM to see what time it was, and then I made the mistake of checking my emails and "
        "couldn't fall back asleep!"
    ),
    (
        "The eclipse will be visible in our area starting at one seventeen PM and reaching maximum coverage at two "
        "forty three PM according to the astronomy website!"
    ),
    (
        "My morning alarm goes off at six AM, but I've trained myself to wake up at five fifty five AM so I can "
        "mentally prepare for the alarm!"
    ),
    (
        "The restaurant takes last orders at ten PM, but the kitchen actually closes at ten thirty PM, so there's a "
        "small window for late night cravings!"
    ),
    (
        "I've been tracking my sleep patterns and apparently I enter REM sleep around two AM and wake up naturally "
        "around six thirty AM every single night!"
    ),
    (
        "The fireworks display is scheduled to begin at twenty one hundred hours and will last approximately forty "
        "five minutes according to the official program!"
    ),
    (
        "My body refuses to fall asleep before midnight no matter how tired I am, and then refuses to wake up before "
        "nine AM no matter how much I try!"
    ),
    (
        "The train schedule changed and now the seven twelve AM train doesn't exist anymore, so I have to take the six "
        "forty five AM instead!"
    ),
    (
        "I remember looking at the clock at eleven PM thinking I'd go to bed soon, and then suddenly it was three AM "
        "and I was still scrolling!"
    ),
    (
        "The pharmacy opens at eight AM but the pharmacist doesn't arrive until nine AM, so you can only pick up "
        "prescriptions after nine even though they're open!"
    ),
    (
        "My favorite podcast releases new episodes at midnight on Thursdays, and I always stay up until twelve oh one "
        "AM to start listening immediately!"
    ),
]

"""Time prompts: long statements about schedules, sunsets, and clocks."""

from __future__ import annotations

DEADLINES: list[str] = [
    (
        "The sun rises at five thirty seven AM this time of year, and I've been waking up with the sun instead of "
        "using an alarm lately!"
    ),
    (
        "I scheduled the meeting for three PM thinking that would give everyone time to have lunch, but half the team "
        "has meetings until three thirty PM!"
    ),
    (
        "The movie theater shows the late night screening at eleven fifteen PM, and I always wonder who has the energy "
        "to watch a movie that late!"
    ),
    (
        "My grandmother's funeral was at ten AM on a Tuesday, and I remember the clock in the church striking ten as "
        "we all stood in silence!"
    ),
    (
        "The deadline was eleven fifty nine PM and I submitted at eleven fifty seven PM, giving myself a whole two "
        "minutes to spare for technical difficulties!"
    ),
    (
        "I've been awake since three seventeen AM because I heard a weird noise and convinced myself someone was "
        "breaking in, but it was just the cat!"
    ),
    (
        "The sunrise yoga class starts at five forty five AM, and I have to wake up at five AM to get there on time, "
        "which feels cruel!"
    ),
    (
        "My internal body clock is set to a twenty five hour day apparently, which is why I naturally drift later and "
        "later if I don't force a schedule!"
    ),
    (
        "The concert ended at eleven thirty PM but we didn't get out of the parking lot until almost one AM because of "
        "the traffic!"
    ),
    (
        "I looked at the clock at two AM, then at three AM, then at four AM, and by five AM I just gave up on sleeping "
        "entirely!"
    ),
    (
        "The store's Black Friday sale starts at five AM, and people were already camping outside at eight PM the "
        "night before!"
    ),
    (
        "My flight was supposed to land at three fifteen PM but we circled the airport for an hour and didn't touch "
        "down until four twenty PM!"
    ),
    (
        "The baby finally started sleeping through the night at six months old, going from her seven PM bedtime to six "
        "AM without waking up!"
    ),
    (
        "I set my alarm for five thirty AM to go to the gym before work, but I've hit snooze every day this week until "
        "six thirty AM!"
    ),
    (
        "The restaurant reservation is for eight PM, which feels late for dinner, but apparently that's when all the "
        "good tables become available!"
    ),
    (
        "My watch shows the time in both twelve hour and twenty four hour format, so I can see it's both seven thirty "
        "PM and nineteen thirty simultaneously!"
    ),
    (
        "The thunderstorm knocked out our power at two AM and it didn't come back on until eight AM, so we all slept "
        "through our alarms!"
    ),
    (
        "I've been tracking the exact minute the sun sets every day, and it's shifted from four forty seven PM in "
        "December to eight thirty PM in June!"
    ),
    (
        "The meeting invite said nine AM but the organizer meant nine AM their time, which is noon my time, and I "
        "showed up three hours early!"
    ),
    (
        "My grandmother always had dinner on the table at exactly six PM, and if you were late, your food would be "
        "cold and she wouldn't reheat it!"
    ),
    (
        "The countdown timer shows twelve hours, seventeen minutes, and forty three seconds until the big "
        "announcement, and I'm refreshing constantly!"
    ),
    (
        "I woke up at four AM convinced I had overslept and missed my flight, only to realize my flight isn't until "
        "tomorrow morning!"
    ),
    (
        "The gym is absolutely packed from five PM to seven PM when everyone gets off work, but it's completely empty "
        "at six AM!"
    ),
    (
        "My phone automatically adjusts for daylight saving time, but my microwave doesn't, so for half the year they "
        "show different times!"
    ),
    (
        "The eclipse lasted exactly two minutes and thirty seven seconds of totality, and those were the most magical "
        "seconds of my entire life!"
    ),
    (
        "I've been awake since three AM thinking about that embarrassing thing I said at the party, and now it's seven "
        "AM and I'm exhausted!"
    ),
    (
        "The bakery puts out fresh donuts at exactly seven AM, and if you get there at seven oh five, the best ones "
        "are already gone!"
    ),
    (
        "My alarm is set for six AM but I always wake up at five fifty eight AM, two minutes before it goes off, "
        "without fail!"
    ),
    (
        "The restaurant's kitchen closes at ten PM but they'll still serve dessert until ten thirty PM if you've "
        "already ordered your main course!"
    ),
    (
        "I remember the exact moment the clock struck midnight on my eighteenth birthday, and how everything felt "
        "different even though nothing had changed!"
    ),
    (
        "The train was supposed to arrive at eight seventeen AM but it was delayed until eight forty three AM, making "
        "me late for my interview!"
    ),
    (
        "My body thinks it's six AM because I just flew across six time zones, but the local clock says it's noon and "
        "I need to function!"
    ),
    (
        "The sunset at seven twenty three PM painted the entire sky in shades of orange, pink, and purple that I've "
        "never seen before in my life!"
    ),
    (
        "I've been on this conference call since ten AM and it's now one thirty PM, and I haven't spoken a single word "
        "the entire time!"
    ),
    (
        "The pharmacy drive through closes at nine PM, which is exactly when I remember I need to pick up my "
        "prescription every single time!"
    ),
    (
        "My favorite coffee shop opens at six AM, and I'm always waiting outside at five fifty five AM like a caffeine "
        "addicted stalker!"
    ),
    (
        "The fireworks started at exactly nine PM and ended at nine forty five PM, but the grand finale at nine forty "
        "three PM was incredible!"
    ),
    (
        "I checked the time at eleven PM thinking I should go to bed, and then suddenly it was two AM and I was still "
        "watching videos!"
    ),
    (
        "The meeting was scheduled for fourteen hundred hours, which is two PM for those of us who don't speak "
        "military time fluently!"
    ),
    (
        "My grandmother's clock chimes every hour on the hour, and at midnight it chimes twelve times and wakes up the "
        "entire house!"
    ),
    (
        "The concert started at eight PM sharp, not a minute late, and the band played for three straight hours until "
        "eleven PM!"
    ),
    (
        "I've been awake since four thirty AM because my neighbor decided that was the perfect time to start mowing "
        "their lawn!"
    ),
    (
        "The store opens at ten AM on Sundays instead of nine AM on weekdays, and I always forget and show up an hour "
        "early!"
    ),
    (
        "My flight boards at six fifteen AM, which means I need to be at the gate by five forty five AM, at the "
        "airport by five AM!"
    ),
    (
        "The sunset yesterday was at eight thirty seven PM, but tonight it's at eight thirty six PM because the days "
        "are getting shorter!"
    ),
    "I set my alarm for seven AM but my body woke me up at four AM and refused to let me fall back asleep!",
    (
        "The restaurant reservation is for seven thirty PM, but we always show up at seven twenty PM to get a drink at "
        "the bar first!"
    ),
    (
        "My watch stopped at exactly three seventeen PM and I didn't notice until six PM when I wondered why time "
        "wasn't moving!"
    ),
    "The baby woke up at two AM, then again at four AM, then again at five thirty AM, and I am running on no sleep!",
    (
        "I've been counting down the minutes since eight AM, and now it's finally four fifty nine PM and I can leave "
        "in sixty seconds!"
    ),
    (
        "The eclipse reached totality at exactly two forty one PM and lasted for four minutes and twenty seven seconds "
        "of pure magic!"
    ),
    "My morning routine is timed down to the minute, from my six AM alarm to my seven twenty three AM departure time!",
    (
        "The concert doors opened at seven PM but we didn't get to our seats until seven forty five PM because of the "
        "security line!"
    ),
    "I looked at the clock at midnight thinking I should sleep, then at one AM, then at two AM, and now it's three AM!",
    (
        "The train leaves at oh seven hundred hours, which sounds so much more dramatic than just saying seven AM in "
        "the morning!"
    ),
    (
        "My grandmother always said the hour between three AM and four AM is when the veil between worlds is thinnest, "
        "and I believe her!"
    ),
    "The pharmacy opens at eight AM but the line starts forming at seven thirty AM because everyone wants to be first!",
    (
        "I've been awake since two AM because I drank coffee at eight PM like an absolute fool who never learns from "
        "mistakes!"
    ),
    (
        "The sunset cruise departs at six thirty PM and returns at nine PM, just in time to watch the sun sink below "
        "the horizon!"
    ),
    "My alarm went off at five AM and I hit snooze so many times that it was suddenly seven AM and I was late!",
    "The meeting ran from nine AM to eleven AM, then from one PM to three PM, and I accomplished nothing in between!",
    (
        "I remember looking at the clock at eleven eleven PM and making a wish, and now I do it every time I see that "
        "time!"
    ),
    "The bakery's cinnamon rolls come out of the oven at six thirty AM, and the line to buy them starts at six AM!",
    "My body naturally wakes up at sunrise, which is great in winter at seven AM but terrible in summer at five AM!",
    (
        "The fireworks display was supposed to start at nine PM but got delayed until nine thirty PM due to technical "
        "difficulties!"
    ),
    (
        "I've been tracking my sleep and apparently I fall asleep at eleven forty seven PM on average and wake at six "
        "thirty two AM!"
    ),
    (
        "The restaurant doesn't take reservations for parties under six people before seven PM, which is incredibly "
        "frustrating for couples!"
    ),
    "My flight was originally at eight AM, got moved to ten AM, then to noon, and finally departed at two fifteen PM!",
    (
        "The countdown to midnight felt like it lasted forever, with each second stretching out as we waited for the "
        "new year!"
    ),
    (
        "I set seventeen alarms between five thirty AM and six thirty AM because I am physically incapable of waking "
        "up otherwise!"
    ),
    "The museum's special exhibit is only open from ten AM to two PM on Saturdays, which is a very limited window!",
    (
        "My grandmother's funeral started at exactly eleven AM, and I remember watching the clock tick closer as we "
        "all sat in silence!"
    ),
    (
        "The concert ended at eleven PM but we didn't get home until one thirty AM because of traffic and stopping for "
        "food!"
    ),
    (
        "I've been awake since three AM replaying a conversation from ten years ago that nobody else even remembers "
        "happened!"
    ),
    (
        "The train schedule says arrival at fourteen fifty three, but we're running twelve minutes late so it'll be "
        "fifteen oh five!"
    ),
    (
        "My body clock is permanently set to night owl mode, with my peak productivity happening between ten PM and "
        "two AM!"
    ),
    (
        "The eclipse started at twelve forty seven PM in our time zone and reached maximum coverage at two fifteen PM "
        "exactly!"
    ),
    (
        "I looked at the clock at four AM and decided to just stay awake rather than sleep for only two hours before "
        "my alarm!"
    ),
    (
        "The pharmacy said my prescription would be ready in fifteen minutes at one PM, and it's now two thirty PM and "
        "still waiting!"
    ),
]

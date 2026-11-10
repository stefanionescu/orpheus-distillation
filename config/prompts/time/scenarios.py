"""Time prompts: long questions and exclamations, then conversations and scenarios."""

from __future__ import annotations

SCENARIOS: list[str] = [
    # LONG QUESTIONS & EXCLAMATIONS
    (
        "Why does my brain decide that three AM is the perfect time to remember every embarrassing thing I've ever "
        "done in my entire life?"
    ),
    (
        "How is it possible that I've been at work since eight AM and it's only ten thirty AM but it feels like I've "
        "been here for days?"
    ),
    (
        "Can someone please explain why the hour between four PM and five PM on a Friday feels longer than the entire "
        "rest of the week combined?"
    ),
    (
        "Why do I always manage to look at the clock at exactly eleven eleven, whether it's AM or PM, without even "
        "trying to do it?"
    ),
    (
        "How did we go from it being nine PM and having the whole evening ahead of us to suddenly being two AM with "
        "work in six hours?"
    ),
    (
        "Is it normal that I wake up at exactly three thirty three AM almost every single night like my body has some "
        "kind of internal alarm?"
    ),
    (
        "Why does every important appointment seem to be scheduled for eight AM when I am barely capable of forming "
        "coherent sentences before ten AM?"
    ),
    (
        "How is it that the fifteen minute break at ten thirty AM goes by in what feels like thirty seconds but the "
        "last hour of work is eternal?"
    ),
    (
        "Can you believe I've been awake since four AM because my upstairs neighbor decided that was the perfect time "
        "to rearrange their furniture?"
    ),
    (
        "Why does time move so incredibly slowly when you're waiting for something but fly by when you're actually "
        "having fun and want it to last?"
    ),
    (
        "How did my quick twenty minute power nap at two PM turn into a three hour sleep session that has now ruined "
        "my entire night's sleep?"
    ),
    (
        "Is it just me or does the period between eleven PM and midnight go by incredibly fast while the hour after "
        "midnight drags on forever?"
    ),
    (
        "Why do I always get my most brilliant creative ideas at eleven thirty PM when I should be sleeping and have "
        "to wake up at six AM?"
    ),
    (
        "How is it fair that I have to be functional at eight AM when my brain doesn't actually turn on until at least "
        "ten thirty AM?"
    ),
    (
        "Can someone explain why I can sleep through my six AM alarm but wake up instantly when my cat meows at four "
        "thirty AM?"
    ),
    (
        "Why does every flight I ever book seem to depart at some absolutely ungodly hour like five fifteen AM or "
        "arrive at one AM?"
    ),
    (
        "How did the meeting that was supposed to be thirty minutes starting at two PM somehow expand to take up the "
        "entire afternoon until five PM?"
    ),
    (
        "Is it weird that I'm more productive between the hours of ten PM and two AM than I am during normal business "
        "hours?"
    ),
    "Why does my body refuse to fall asleep before one AM no matter how exhausted I am or how early I have to wake up?",
    (
        "How is it that I can remember exactly what time it was during random moments from years ago but can't "
        "remember what I had for lunch?"
    ),
    (
        "Can you believe the store opens at ten AM on weekends but I was still waiting in line at nine thirty AM like "
        "an absolute fool?"
    ),
    (
        "Why does every minute feel like an hour when you're sitting in a waiting room but hours feel like minutes "
        "when you're enjoying yourself?"
    ),
    "How did my alarm not go off at seven AM when I specifically remember setting it before going to sleep last night?",
    (
        "Is it normal to wake up at five AM on weekends even though you could sleep in, just because your body is used "
        "to the routine?"
    ),
    (
        "Why does the hour between three PM and four PM feel like the absolute longest hour of the entire workday "
        "every single time?"
    ),
    (
        "How is it possible that I've been on hold since eleven AM and it's now two PM and I still haven't spoken to a "
        "human being?"
    ),
    (
        "Can someone explain why time zones exist and why my meeting at nine AM is actually midnight for my colleague "
        "in another country?"
    ),
    (
        "Why do I always seem to check the time at exactly twelve thirty four, like my subconscious is counting or "
        "something weird like that?"
    ),
    (
        "How did we go from it being Friday at five PM to suddenly being Sunday at eight PM with the whole weekend "
        "gone in a blur?"
    ),
    (
        "Is it just me or does the last minute before midnight on New Year's Eve feel like it lasts an entire hour "
        "while you're counting down?"
    ),
    (
        "Why does my body think four AM is an acceptable time to be wide awake when I have to function like a normal "
        "person at eight AM?"
    ),
    (
        "How is it that the ten minutes before a meeting at nine AM feel longer than the entire two hour meeting "
        "itself somehow?"
    ),
    (
        "Can you believe I set five alarms between six AM and six thirty AM and still managed to sleep through every "
        "single one of them?"
    ),
    (
        "Why does every good television show seem to air at ten PM when I have to wake up at six AM for work the next "
        "morning?"
    ),
    (
        "How did my body decide that waking up at four seventeen AM was necessary when my alarm wasn't set to go off "
        "until seven AM?"
    ),
    (
        "Is it normal that I feel most alive and creative between the hours of eleven PM and three AM when everyone "
        "else is asleep?"
    ),
    (
        "Why does the commute home at five thirty PM take twice as long as the commute to work at seven thirty AM even "
        "though it's the same route?"
    ),
    (
        "How is it possible that I've been staring at this clock since two PM waiting for five PM and only thirty "
        "minutes have passed?"
    ),
    (
        "Can someone please explain why daylight saving time exists and why we have to change our clocks at two AM "
        "twice a year?"
    ),
    (
        "Why does every second of the countdown from ten to midnight on New Year's Eve feel like it contains an entire "
        "lifetime of anticipation?"
    ),
    # CONVERSATIONS & SCENARIOS ABOUT TIME
    (
        "Oh my goodness, is it really already quarter past eleven at night? I swear I just sat down at eight PM to "
        "watch one episode!"
    ),
    (
        "Wait, did you say the meeting is at nine AM or nine PM? Because those are two very different levels of "
        "preparation required!"
    ),
    (
        "I can't believe you've been awake since four thirty AM! How are you even functioning right now when it's "
        "already past noon?"
    ),
    "The party starts at eight PM but you know nobody actually shows up until at least nine thirty PM, so don't rush!",
    "My alarm went off at six AM and I genuinely considered quitting my job rather than getting out of bed that early!",
    (
        "Did you know that three AM is statistically the hour when the fewest people are awake? It's called the "
        "witching hour!"
    ),
    "I've been waiting for this moment since eight AM this morning, and now that it's finally five PM, I feel so free!",
    (
        "The sunset at seven forty five PM last night was so beautiful that I just stood there for twenty minutes "
        "watching!"
    ),
    (
        "Can you believe the store closes at six PM on Sundays? Who decided that was an acceptable closing time for "
        "anything?"
    ),
    "I remember exactly where I was at noon on that day, the clock struck twelve and everything changed forever!",
    (
        "My grandmother always said nothing good happens after midnight, and honestly, she was completely right about "
        "that!"
    ),
    (
        "The flight boards at five forty five AM, which means I need to wake up at three AM, which means I won't sleep "
        "at all!"
    ),
    "I looked at the clock at two AM thinking I should sleep, then at three AM, then at four AM, and now it's five AM!",
    (
        "The restaurant reservation is for seven thirty PM, but knowing this group, we won't actually be seated until "
        "eight PM!"
    ),
    (
        "Did you seriously wait in line since six AM just to get those limited edition sneakers when the store opened "
        "at ten AM?"
    ),
    "I've been counting down the seconds since nine AM and now it's finally four fifty nine PM and I can leave!",
    (
        "The concert was supposed to start at eight PM but the band didn't come on until nine thirty PM and I was "
        "exhausted!"
    ),
    "My body thinks it's three AM because of the jet lag, but the sun is shining and the clock says it's eleven AM!",
    "I set my alarm for six thirty AM but I've been awake since four AM because my brain hates me apparently!",
    "The deadline is at midnight tonight and it's already ten PM and I haven't even started on the project yet!",
    (
        "Can you believe the bakery sells out of croissants by seven AM? I got there at seven fifteen AM and they were "
        "gone!"
    ),
    (
        "I remember the clock striking midnight on my twenty first birthday and feeling like my whole life was ahead "
        "of me!"
    ),
    "The meeting was supposed to end at three PM but here we are at five PM still discussing the same three points!",
    "My favorite show comes on at ten PM which is way too late when I have to wake up at five thirty AM for work!",
    "I've been awake since two AM because my neighbor's car alarm went off and wouldn't stop for thirty minutes!",
    "The train leaves at seven twelve AM and if I miss it, I have to wait until eight forty five AM for the next one!",
    "Did you know the sun rises at different times throughout the year? Today it rose at five twenty three AM!",
    "I finally fell asleep at one AM only to be woken up by my alarm at five AM, so I got four hours of sleep!",
    "The pharmacy closes at nine PM and I always remember I need my prescription at eight fifty five PM without fail!",
    "My internal clock wakes me up at six AM every day, even on weekends when I desperately want to sleep in!",
    "The countdown to midnight on New Year's Eve is my favorite ten seconds of the entire year, so magical!",
    "I've been on this phone call since eleven AM and it's now two PM and we still haven't resolved anything!",
    (
        "The sunset cruise leaves at six PM and returns at nine PM, which is the perfect time to watch the sky change "
        "colors!"
    ),
    "Can you believe I've been awake for twenty hours straight? I woke up at six AM yesterday and it's now two AM!",
    "The baby finally slept through the night, from seven PM to six AM, and I feel like a new person today!",
    "I set seventeen alarms between six AM and seven AM because I literally cannot wake up to just one alarm!",
    "The eclipse reached totality at two thirty seven PM and those two minutes felt like they lasted forever!",
    "My watch says it's four twenty three PM but my phone says four twenty five PM and I don't know which to trust!",
    (
        "I've been refreshing this page since eleven fifty nine PM waiting for the midnight drop and now it's twelve "
        "oh three AM!"
    ),
    "The restaurant's happy hour ends at six PM and I always get there at five fifty five PM to maximize my time!",
    "Did you know that most car accidents happen between four PM and six PM during the evening rush hour?",
    "I remember looking at the clock at eleven PM thinking I'd go to bed soon, and suddenly it was three AM!",
    "The meeting invite said nine AM Pacific time but I'm on Eastern time so I showed up at noon their time!",
    "My grandmother's clock has been stuck at ten twenty three for years and nobody has ever thought to fix it!",
    (
        "The fireworks display starts at nine PM and lasts until nine forty five PM, with the grand finale at nine "
        "forty three PM!"
    ),
    "I've been awake since three AM because I had a nightmare and couldn't fall back asleep no matter what I tried!",
    "The store opens at ten AM on weekends instead of nine AM on weekdays, and I always forget and show up early!",
    "Can you believe the concert ended at eleven thirty PM and we didn't get home until two AM because of traffic?",
    (
        "I set my alarm for five AM to go to the gym before work but I've hit snooze every day this week until six "
        "thirty AM!"
    ),
    "The sunset yesterday at eight seventeen PM was the most beautiful thing I've ever seen, the sky was on fire!",
]

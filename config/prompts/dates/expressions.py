"""Date prompts: long date expressions, statements, questions, exclamations, and mixed contexts."""

from __future__ import annotations

EXPRESSIONS: list[str] = [
    # LONG DATE EXPRESSIONS
    (
        "I remember it so clearly, it was March twenty third, two thousand and fifteen, and I had just gotten the call "
        "that changed my entire life."
    ),
    (
        "We first met on September seventh, nineteen ninety eight, at a coffee shop downtown, and I knew from that "
        "moment that everything was about to change."
    ),
    (
        "The company was officially founded on April first, two thousand and ten, which everyone thought was an April "
        "Fools' joke at first."
    ),
    (
        "I'll never forget July fourth, twenty twenty, because that was the day we finally got the news we'd been "
        "waiting for all year."
    ),
    (
        "My grandmother always told me about December seventh, nineteen forty one, and how she heard the news about "
        "Pearl Harbor on the radio."
    ),
    (
        "It was February fourteenth, two thousand and eighteen, Valentine's Day of all days, when he finally got down "
        "on one knee and proposed."
    ),
    (
        "The accident happened on November twenty second, twenty nineteen, and I spent the next six months recovering "
        "in the hospital."
    ),
    (
        "I started my dream job on January third, twenty twenty two, after spending almost two years searching and "
        "interviewing everywhere."
    ),
    (
        "We closed on the house on August fifteenth, two thousand and sixteen, and moved in exactly two weeks later on "
        "the twenty ninth."
    ),
    (
        "The earthquake hit on October seventeenth, nineteen eighty nine, during the World Series, and I remember the "
        "ground shaking for what felt like forever."
    ),
    (
        "She was born at three forty seven in the morning on May twenty first, twenty twenty three, and she weighed "
        "exactly seven pounds, four ounces."
    ),
    "I handed in my resignation on June thirtieth, twenty twenty one, effective two weeks later on July fourteenth.",
    (
        "The trial started on March fifth, two thousand and twelve, and didn't end until November eighteenth of that "
        "same year."
    ),
    "We've been coming to this beach house every summer since August of nineteen ninety five, almost thirty years now.",
    (
        "I got my diagnosis on December third, twenty eighteen, and by February of twenty nineteen, I had already "
        "started treatment."
    ),
    (
        "The concert was originally scheduled for April twenty second, twenty twenty, but got postponed to September "
        "fourth, twenty twenty one because of the pandemic."
    ),
    (
        "My parents got married on June seventh, nineteen seventy five, and they just celebrated their fiftieth "
        "anniversary last year."
    ),
    (
        "I submitted my application on January fifteenth, didn't hear back until March twenty eighth, and finally got "
        "the acceptance letter on April second."
    ),
    (
        "The power went out on February first, twenty twenty one, during the ice storm, and didn't come back on until "
        "February fifth."
    ),
    (
        "We started dating on October thirty first, twenty sixteen, got engaged on December twenty fifth, twenty "
        "eighteen, and married on May eleventh, twenty nineteen."
    ),
    (
        "I remember watching the towers fall on September eleventh, two thousand and one, and thinking the world would "
        "never be the same again."
    ),
    (
        "The renovation project began on March first, twenty twenty three, and we didn't move back in until August "
        "twenty seventh of that year."
    ),
    (
        "She passed away peacefully on November ninth, twenty twenty two, surrounded by her family, exactly one week "
        "after her ninety third birthday."
    ),
    (
        "I took my first steps after the surgery on July eighteenth, twenty twenty, almost three months after the "
        "operation on April twenty third."
    ),
    (
        "The store had its grand opening on September fourteenth, nineteen eighty seven, and my family has been "
        "running it for over thirty five years now."
    ),
    (
        "We adopted our dog on January twenty second, twenty seventeen, and he's been the best part of our lives for "
        "the past seven years."
    ),
    (
        "I finished writing my thesis on April thirtieth, twenty twenty four, after working on it for almost two and a "
        "half years since October of twenty twenty one."
    ),
    (
        "The merger was announced on July first, two thousand and nineteen, but didn't officially go through until "
        "January fifteenth, twenty twenty."
    ),
    (
        "I ran my first marathon on November third, twenty eighteen, in New York City, and finished in four hours and "
        "twenty three minutes."
    ),
    (
        "We found out we were pregnant on February fourteenth, twenty twenty two, and our son was born exactly nine "
        "months later on November fourteenth."
    ),
    # ADDITIONAL LONG EXAMPLES - STATEMENTS
    "The last time I visited my hometown was sometime in March of twenty nineteen, and so much has changed since then.",
    (
        "I've been keeping a journal since January first, twenty fifteen, and I haven't missed a single day in almost "
        "ten years."
    ),
    (
        "The doctor said the results would be ready by December tenth at the latest, so I'm trying not to worry until "
        "then."
    ),
    (
        "We booked the venue for August twentieth, twenty twenty six, because that's the only Saturday they had "
        "available all summer."
    ),
    "I distinctly remember it was a Tuesday in late October because the leaves had already started to change colors.",
    "The warranty expires on March fifteenth of next year, so I need to decide whether to extend it before then.",
    (
        "My flight lands at eleven thirty on the night of June twenty second, so I won't get to the hotel until well "
        "after midnight."
    ),
    (
        "The lease agreement starts on September first and runs for exactly twelve months until August thirty first of "
        "the following year."
    ),
    "I made a New Year's resolution on January first, twenty twenty, to exercise more, and I've mostly kept it up.",
    (
        "The package was supposed to arrive by February fourteenth for Valentine's Day, but it didn't show up until "
        "the eighteenth."
    ),
    (
        "I've been waiting since November of last year for them to process my application, and I still haven't heard "
        "anything."
    ),
    "The deadline was originally set for April thirtieth, but they extended it by two weeks to May fourteenth.",
    "We celebrated our tenth wedding anniversary on July seventh, twenty twenty three, with a trip to Paris.",
    "I started working on this project back in August, and I'm hoping to have it finished before the holidays.",
    (
        "The last major earthquake in this region happened on October seventeenth, nineteen eighty nine, which was "
        "over thirty years ago."
    ),
    (
        "My grandmother was born on December twenty fifth, nineteen thirty two, so she always joked that she shared "
        "her birthday with Christmas."
    ),
    "The school year ends on June fifteenth, which means we only have three more weeks of classes left.",
    "I checked the calendar and realized that Thanksgiving falls on November twenty eighth this year.",
    (
        "The moon landing happened on July twentieth, nineteen sixty nine, and my parents remember watching it live on "
        "television."
    ),
    "I've had this same phone number since March of two thousand and eight, which is over fifteen years now.",
    (
        "The construction project is scheduled to begin on April first and should be completed by November thirtieth "
        "at the latest."
    ),
    (
        "I remember my first day of college was August twenty third, twenty ten, and I was so nervous I could barely "
        "speak."
    ),
    "The company's fiscal year ends on December thirty first, so we're all scrambling to meet our quarterly targets.",
    "My driver's license expires on my birthday, August ninth, twenty twenty five, so I need to renew it soon.",
    "We planted the garden in early May, around the fifth or sixth, and by July we were harvesting tomatoes.",
    "The movie premiere is set for December twentieth, just in time for the holiday box office rush.",
    (
        "I've been a member of this gym since January second, twenty eighteen, right after I made my New Year's "
        "resolution."
    ),
    (
        "The historical records show that the town was founded on September third, eighteen fifty two, by settlers "
        "from the east."
    ),
    (
        "My subscription renews automatically on the fifteenth of every month, and I always forget to check my bank "
        "statement."
    ),
    (
        "The peace treaty was signed on November eleventh, nineteen eighteen, which is why we celebrate Veterans Day "
        "on that date."
    ),
    # ADDITIONAL LONG EXAMPLES - QUESTIONS
    "Do you remember what we were doing on New Year's Eve, nineteen ninety nine, when everyone was worried about Y2K?",
    "Can you believe it's already been five years since we graduated on May twentieth, twenty nineteen?",
    "What time does the store open on Thanksgiving Day, or is it closed for the holiday this year?",
    "Was it February or March when we took that road trip to California, because I can't remember exactly?",
    "Did you know that my parents met on Valentine's Day, nineteen eighty two, at a party in New York City?",
    "When is the deadline for submitting the application, is it still September thirtieth or did they extend it?",
    "Do you think we should book the hotel for July fourth weekend now, or wait until closer to the date?",
    "Can you remind me what date we're supposed to pick up the rental car, was it the fifteenth or the sixteenth?",
    "How long has it been since we last saw each other, wasn't it sometime around Christmas of twenty twenty one?",
    "What year did that movie come out, was it two thousand and five or two thousand and six?",
    "Is the conference still scheduled for March eighteenth through the twentieth, or have the dates changed?",
    "When did you say the building was constructed, was it in the early nineteen hundreds or later?",
    "Do you know if the museum is open on July fourth, or is it closed for Independence Day?",
    "What's the exact date of the eclipse, I know it's sometime in April but I don't remember the specific day?",
    "How old were you when you moved here, wasn't it around August of nineteen ninety five?",
    "Can you check if my appointment is still on the calendar for November third at two o'clock?",
    "Did they ever set a date for the company retreat, I thought they mentioned something about October?",
    "When is the baby's due date again, I know it's sometime in early spring but I forgot the exact date?",
    "Was that the year we went to Hawaii, or was that two thousand and sixteen when we visited Mexico instead?",
    "What day of the week does Christmas fall on this year, and do we get the day before off as well?",
    "Is your birthday on March twenty first or twenty second, because I always get confused about which one it is?",
    "How many days until the deadline, is it more or less than two weeks from today?",
    "When did they announce that the office would be closing early, was it before or after Thanksgiving?",
    "Do you remember the exact date we signed the lease, I need it for my records?",
    "What time zone are they in for the meeting on Tuesday, and what time will that be for us?",
    # ADDITIONAL LONG EXAMPLES - EXCLAMATIONS
    "I can't believe it's already December, this whole year has gone by so incredibly fast!",
    "Happy birthday! I just realized you were born on the same day as my brother, July sixteenth!",
    "The wedding is only three weeks away, on September fourteenth, and we still have so much to do!",
    "I just found out the concert got rescheduled to November tenth, which is the same night as my work event!",
    "Finally, after waiting since February, they announced the release date is October first!",
    "It's our twentieth anniversary on June seventh, I can't believe we've been married for two decades!",
    "The forecast says it's going to snow on Christmas Day this year for the first time since twenty ten!",
    "I just realized that my passport expires on January fifth, and my trip is on January third!",
    "They moved the deadline up to this Friday, March eighth, and I still have so much work to do!",
    "It's amazing that she's already turning eighteen on April twenty second, time flies so fast!",
    "I completely forgot that today is February fourteenth, and I didn't get anything for Valentine's Day!",
    "The tickets go on sale at midnight on November first, and I'm staying up to make sure I get them!",
    "We finally closed on the house on August thirtieth after months of waiting and negotiations!",
    "The doctor said the baby could come any day now, the due date is December twenty fifth!",
    "I've been counting down since January and the vacation finally starts on July fifteenth!",
    # ADDITIONAL LONG EXAMPLES - MIXED CONTEXTS
    "Looking back at old photos from July of twenty fifteen, I barely recognize myself from almost a decade ago.",
    "The tradition started on Thanksgiving of nineteen ninety eight, and we've kept it going every year since.",
    "I marked the calendar with a big red circle around May twenty third because that's when everything changes.",
    "Every year on March seventeenth, we celebrate not just Saint Patrick's Day but also my father's birthday.",
    (
        "The documents show the transaction was completed on February eleventh, twenty twenty two, at approximately "
        "three PM."
    ),
    "According to the schedule, maintenance will take place overnight on the weekend of April sixth and seventh.",
    "I've set a reminder for myself two weeks before the expiration date, which is on August thirty first.",
    "The history books record that the battle took place on October nineteenth, seventeen eighty one.",
    "We try to have a family reunion every year around the fourth of July, usually on the closest weekend.",
    "The original release date was pushed back from June to September because they needed more time for testing.",
    "I woke up on January first, twenty twenty four, with a completely new outlook on life and what I wanted.",
    "The email confirmation says the reservation is for March fifteenth through the nineteenth, four nights total.",
    "My calendar shows that I have three different appointments all scheduled for the same day, November twelfth.",
    "They say the best time to visit is during the last two weeks of April when the cherry blossoms are in bloom.",
    "The report is due on the last business day of the month, which would be Friday, February twenty eighth.",
]

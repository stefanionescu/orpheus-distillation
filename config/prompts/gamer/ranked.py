"""Gaming prompts: long statements about matches, ranked play, and progress."""

from __future__ import annotations

RANKED: list[str] = [
    # LONG STATEMENTS
    (
        "I've been grinding this ranked ladder for the entire season and I'm still stuck at the same rank because the "
        "matchmaking keeps pairing me with players who refuse to communicate."
    ),
    (
        "The new battle pass has over one hundred tiers of content to unlock, and I honestly don't know if I have "
        "enough time to complete it before the season ends next month."
    ),
    (
        "My character build focuses entirely on critical hit damage and attack speed, which makes boss fights trivial "
        "but leaves me incredibly vulnerable to any kind of crowd control effects."
    ),
    (
        "The enemy team's strategy of camping the spawn points and controlling all the power weapon locations has made "
        "this match completely unwinnable for us at this point."
    ),
    (
        "I spent over three hundred hours farming this dungeon for the legendary sword, and when it finally dropped, I "
        "realized my class can't even equip that weapon type."
    ),
    (
        "The developers announced a major balance patch coming next week that will completely change the meta, so I'm "
        "holding off on crafting any new gear until then."
    ),
    (
        "My guild has been attempting this raid boss for two months straight, and we still can't get past the third "
        "phase because people keep dying to the same mechanics."
    ),
    (
        "The crosshair customization options in this game are incredibly detailed, and I spent over an hour fine "
        "tuning my settings to get the perfect aim configuration for my playstyle."
    ),
    (
        "I finally reached the maximum level cap after playing for over five hundred hours, and now I realize the "
        "endgame content is just repeating the same dungeons over and over."
    ),
    (
        "The tutorial section of this game holds your hand for way too long, and by the time you reach the actual "
        "gameplay, you've forgotten half the mechanics they taught you."
    ),
    (
        "My controller's left stick has developed a horrible drift problem, which means my character keeps walking in "
        "random directions even when I'm not touching anything at all."
    ),
    (
        "The seasonal ranking system resets every three months, which means I have to grind through the lower ranks "
        "again even though I was in the top percentage last season."
    ),
    (
        "I've been watching professional players stream this game for months, and I still can't understand how they "
        "make these incredibly complex combos look so effortless and easy."
    ),
    (
        "The loot box system in this game is designed to prey on players with addictive tendencies, and I really wish "
        "more countries would regulate these predatory monetization practices."
    ),
    (
        "My team's composition is completely unbalanced because everyone wanted to play damage dealers, and now we "
        "have no tank or healer to keep us alive during fights."
    ),
    (
        "The map design in this shooter heavily favors one side of the spawn, which means the team that starts on the "
        "bad side has to work twice as hard to win."
    ),
    (
        "I accidentally sold my best legendary weapon to a vendor because I wasn't paying attention, and now I have to "
        "farm for another hundred hours to get it back."
    ),
    (
        "The difficulty spike between the normal mode and the hard mode is absolutely insane, and I don't understand "
        "how anyone beats this without grinding for better gear first."
    ),
    (
        "My internet connection dropped right as I was about to win the tournament match, and now I'm disqualified "
        "because the game counts disconnects as automatic losses."
    ),
    (
        "The crafting system requires materials from five different zones, and each zone has its own reputation grind "
        "that takes weeks to complete before you can even buy recipes."
    ),
    (
        "I've been trying to optimize my character's gear score for the new raid, but the random stat rolls on "
        "equipment make it nearly impossible to get perfect pieces."
    ),
    (
        "The community tier list ranks my favorite character as the worst in the game, but I refuse to switch mains "
        "just because the meta doesn't favor my playstyle."
    ),
    (
        "My squad and I have been playing together since the beta, and watching us improve from complete beginners to "
        "competitive players has been an incredible journey over the years."
    ),
    (
        "The new update added a feature that lets you replay boss fights at higher difficulties, which is perfect for "
        "farming rare materials without having to redo entire dungeons."
    ),
    (
        "I spent my entire weekend attempting to get the platinum trophy, and I'm still missing one achievement that "
        "requires winning fifty matches in a row without dying once."
    ),
    (
        "The enemy sniper has been dominating our team for the entire match because nobody wants to switch to a "
        "flanking character and deal with them properly."
    ),
    (
        "My muscle memory from the previous game keeps making me press the wrong buttons, and it's taking forever to "
        "unlearn those habits and adapt to the new control scheme."
    ),
    (
        "The game's economy is completely broken because veteran players have hoarded so much currency that new "
        "players can't afford anything on the auction house anymore."
    ),
    (
        "I finally found a build guide that explains exactly how to optimize my character for endgame content, and my "
        "damage output has tripled since I followed the recommendations."
    ),
    (
        "The loading screens in this game take so long that I've started bringing my phone to play other games while "
        "waiting for matches to start on my main setup."
    ),
    (
        "My reaction time has gotten noticeably worse since I started playing on a television instead of a gaming "
        "monitor, and the input lag is really affecting my performance."
    ),
    (
        "The story mode in this game is surprisingly emotional, and I wasn't expecting to get so invested in the "
        "characters when I originally bought it just for multiplayer."
    ),
    (
        "I've been saving all my premium currency for months waiting for this specific banner, and I still didn't get "
        "the character I wanted after spending everything I had."
    ),
    (
        "The patch notes mentioned quality of life improvements, but all they actually did was add more "
        "microtransactions and make the grind even longer than it was before."
    ),
    (
        "My team finally figured out the optimal strategy for speedrunning this raid, and we managed to cut our "
        "completion time down from two hours to just under forty minutes."
    ),
    (
        "The competitive scene for this game is dying because the developers refuse to listen to professional players "
        "about the balance changes that would make tournaments more exciting."
    ),
    (
        "I accidentally queued for the wrong game mode and ended up in a hardcore match where friendly fire is "
        "enabled, and my teammates kept killing me by accident."
    ),
    (
        "The new character they added last patch has completely broken the meta, and every single match now revolves "
        "around either picking them or picking their direct counter."
    ),
    (
        "My gaming setup has evolved so much over the years, from playing on a tiny laptop to having a full "
        "battlestation with multiple monitors and a mechanical keyboard."
    ),
    (
        "The achievement for completing the game without taking any damage seemed impossible at first, but after "
        "memorizing every enemy pattern, I finally managed to pull it off."
    ),
    (
        "I've been theory crafting new builds in the character planner for hours, but I won't know if any of them "
        "actually work until I can test them in the game."
    ),
    (
        "The voice acting in this game is surprisingly good for an indie title, and some of the emotional scenes "
        "actually made me tear up during my first playthrough."
    ),
    (
        "My guild drama has gotten so out of control that half the members left to form their own group, and now we "
        "don't have enough people to attempt raids."
    ),
    (
        "The new game plus mode adds so many extra challenges and hidden content that it almost feels like playing a "
        "completely different game the second time through."
    ),
    (
        "I've been streaming my gameplay for months with zero viewers, but I keep going because I genuinely enjoy "
        "sharing my gaming experiences even if nobody is watching."
    ),
    (
        "The seasonal events in this game are always so well designed, with unique mechanics and exclusive rewards "
        "that actually feel worth grinding for during the limited time."
    ),
    (
        "My ping spikes to over two hundred milliseconds every evening because everyone in my neighborhood is "
        "streaming video, and it makes competitive games completely unplayable for me."
    ),
    (
        "The developers just announced a collaboration event with my favorite anime, and I'm so excited to see how "
        "they integrate those characters into the game world."
    ),
    (
        "I've been playing this franchise since the very first game came out, and watching it evolve over the decades "
        "has been like growing up alongside the series itself."
    ),
    (
        "The modding community for this game is incredibly talented, and some of the user created content is honestly "
        "better than what the official developers have released."
    ),
    (
        "My save file is approaching the maximum playtime counter, and I'm curious to see what happens when I finally "
        "hit the limit after all these years of playing."
    ),
    (
        "The esports tournament for this game had a prize pool of over ten million dollars, and watching those "
        "professional players compete at the highest level was truly inspiring."
    ),
    (
        "I've memorized every spawn location, power up timer, and map callout for this game, but I still can't seem to "
        "break into the higher ranks of competitive play."
    ),
    (
        "The accessibility options in this game are incredibly well designed, and it's great to see developers finally "
        "putting effort into making games playable for everyone."
    ),
    (
        "My controller has been with me through three different console generations, and even though the buttons are "
        "worn down, I refuse to replace it for sentimental reasons."
    ),
    (
        "The boss fight at the end of this dungeon requires perfect execution of mechanics that the game never "
        "properly explains, and I had to watch a guide to understand."
    ),
    (
        "I've been playing support characters for so long that I've forgotten how to actually deal damage, and "
        "switching to a carry role feels completely foreign to me now."
    ),
    (
        "The game's photo mode is so detailed that I've spent more time taking screenshots than actually playing "
        "through the story content that I originally bought it for."
    ),
    (
        "My competitive rank finally matches my actual skill level after the new season reset, and climbing feels so "
        "much more rewarding when every match is evenly balanced."
    ),
    (
        "The developers released a roadmap for the next year of content, and I'm genuinely excited about all the new "
        "features and expansions they have planned for us."
    ),
    (
        "I've been trying to get my friends into this game for months, but the learning curve is so steep that they "
        "always give up before reaching the fun parts."
    ),
    (
        "The night and day cycle in this open world affects which enemies spawn and what resources are available, "
        "adding a surprising amount of depth to the exploration."
    ),
    (
        "My character's backstory is surprisingly dark for a game with such colorful graphics, and the contrast "
        "between the visuals and narrative creates an interesting atmosphere."
    ),
    (
        "The weapon upgrade system requires so many different materials that I've created a spreadsheet just to track "
        "what I need and where to farm each component."
    ),
    (
        "I finally beat the secret boss that only appears after completing every side quest in the game, and the "
        "reward was absolutely worth all the extra effort."
    ),
    (
        "The community has created so many helpful resources like wikis and calculators that playing this game "
        "efficiently would be nearly impossible without their contributions."
    ),
    (
        "My gaming chair finally arrived after being backordered for three months, and the difference in comfort "
        "during long sessions is immediately noticeable and worth the wait."
    ),
    (
        "The difficulty settings in this game are perfectly balanced, with each step up adding meaningful challenge "
        "without feeling unfair or artificially inflated with enemy health."
    ),
    (
        "I've been playing the same character since launch day, and even after thousands of hours, I'm still "
        "discovering new tech and optimizations for my main."
    ),
    (
        "The environmental storytelling in this game is masterfully done, with every detail in the world contributing "
        "to the narrative without relying on exposition dumps."
    ),
    (
        "My team's strategy for this map involves an unusual rotation that catches enemies off guard, and we've been "
        "winning consistently ever since we developed this approach."
    ),
]

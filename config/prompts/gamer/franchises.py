"""Gaming prompts: examples of fifteen to thirty-seven words about specific games."""

from __future__ import annotations

FRANCHISES: list[str] = [
    (
        "I finally got the platinum trophy in Bloodborne after beating the Chalice Dungeons, and the Defiled Watchdog "
        "was pure suffering."
    ),
    "The Shrine of Amana in Dark Souls 2 is the worst area in the entire series, and the homing magic is unfair.",
    "My Rust base got raided while I was offline, and I lost everything I spent the entire wipe grinding for.",
    "The Ringed City DLC in Dark Souls 3 has some of the hardest content in the series, but the rewards are worth it.",
    (
        "I've been playing Subnautica and the Reaper Leviathans still make me too scared to explore the crash zone "
        "properly."
    ),
    "The Margit fight in Elden Ring was a wake up call that this game wasn't going to hold my hand at all.",
    "My Smash Ultimate main keeps getting nerfed every patch, and I'm tired of having to relearn all my combos.",
    (
        "The Painted World of Ariandel in Dark Souls 3 has Sister Friede, who might be the hardest boss in the entire "
        "series."
    ),
    "I can't believe how good the Resident Evil 2 remake turned out, and Mr. X still terrifies me every playthrough.",
    (
        "My Genshin Impact account has terrible luck with five star pulls, and I've hit pity on every single banner so "
        "far."
    ),
    (
        "The Sword Saint Isshin fight in Sekiro is the perfect final boss, testing every skill the game taught you "
        "throughout."
    ),
    (
        "I've been playing Celeste and the Farewell chapter is the hardest platforming I've ever attempted in any game "
        "ever."
    ),
    "The Anor Londo archers in Dark Souls are infamous for a reason, and I still die to them on new characters.",
    (
        "My Fortnite building skills are terrible compared to the kids who can construct entire towers in two seconds "
        "flat."
    ),
    (
        "The Mohg fight in Elden Ring requires that specific tear to survive his phase transition, and I learned that "
        "the hard way."
    ),
    "I finally beat Sigrun in God of War on Give Me God of War difficulty, and that took over a hundred attempts.",
    (
        "My Tarkov raids keep ending with me getting head eyes'd by someone I never even saw, and the learning curve "
        "is brutal."
    ),
    (
        "The Ludwig fight in Bloodborne has the best phase transition in any Soulsborne game, and the music change is "
        "incredible."
    ),
    "I've been grinding Mythic Plus keys in World of Warcraft, and the affixes this week make every dungeon miserable.",
    "The Capra Demon in Dark Souls is only hard because of the dogs and the tiny arena, not the actual boss itself.",
    "My Apex ranked grind has stalled because I keep getting teammates who drop Fragment and die in the first minute.",
    "The Slave Knight Gael fight in Dark Souls 3 is the perfect sendoff for the series, epic in scale and lore.",
    (
        "I can't believe the Cyberpunk 2077 launch was so broken, but the game is actually incredible now after all "
        "the patches."
    ),
    "My Rimworld colony just got wiped by a mechanoid cluster that spawned right in the middle of my base somehow.",
    (
        "The Midir fight in Dark Souls 3 requires so much patience, and his health pool is absolutely massive for a "
        "dragon."
    ),
    "I've been playing Returnal and the biome three boss still destroys me even after beating the game multiple times.",
    (
        "The Genichiro fight in Sekiro is where the combat system finally clicked for me, and everything after felt "
        "more manageable."
    ),
    "My Dota 2 MMR has been stuck at the same number for three years because I refuse to play meta heroes.",
    (
        "The Lady Maria fight in Bloodborne is pure elegance, and her aggressive moveset rewards players who match her "
        "aggression."
    ),
    (
        "I finally got all the Korok seeds in Breath of the Wild, and the reward for collecting them all is "
        "hilariously disappointing."
    ),
    "My Sea of Thieves crew keeps getting sunk by Reapers who have way more experience than us at naval combat.",
    "The Friede fight in Dark Souls 3 has three phases and no checkpoints, and the third phase always gets me.",
    (
        "I've been playing Hunt Showdown and the audio design is so good that I can pinpoint enemy locations by sound "
        "alone."
    ),
    (
        "The Artorias fight in Dark Souls is still my favorite boss because of the lore implications and the tragic "
        "backstory."
    ),
    (
        "My Phasmophobia sessions always end with someone getting hunted because they forgot to hide in a closet or "
        "locker."
    ),
    (
        "The Godrick fight in Elden Ring sets the tone for how creative the boss designs are going to be throughout "
        "the game."
    ),
    (
        "I can't stop playing Vampire Survivors even though the gameplay loop is so simple, the dopamine hits are too "
        "satisfying."
    ),
    (
        "My Valorant crosshair placement has improved so much since I started watching professional players and "
        "copying their positioning."
    ),
    (
        "The Manus fight in Dark Souls requires the Silver Pendant to survive, and I didn't know that existed my first "
        "time."
    ),
    (
        "I've been grinding the Riven of a Thousand Voices raid in Destiny 2, and the mechanics are still confusing "
        "after ten clears."
    ),
    "The Owl Father fight in Sekiro is harder than the final boss, and his mikiri counter punishes make me so angry.",
    (
        "My Warzone loadout keeps getting nerfed into the ground every season, and I'm tired of having to find new "
        "meta weapons."
    ),
    (
        "The Bed of Chaos in Dark Souls is universally hated for good reason, and it's the worst boss From Software "
        "ever made."
    ),
    (
        "I finally beat Ornstein and Smough solo in Dark Souls, and killing Ornstein first for the Leo Ring was so "
        "satisfying."
    ),
    "My Escape from Tarkov stash is completely full of gear I'm too scared to use because I might lose it.",
    "The Demon of Hatred in Sekiro feels like a Dark Souls boss in the wrong game, and the fight is frustrating.",
    (
        "I've been playing Risk of Rain 2 and the Mithrix fight on Monsoon difficulty is absolutely chaotic with four "
        "players."
    ),
    (
        "The Four Kings in Dark Souls require you to out DPS them before more spawn, and my build couldn't do enough "
        "damage."
    ),
    (
        "My Overwatch 2 support queue times are instant because nobody wants to play healer, and I'm stuck on Mercy "
        "duty again."
    ),
    "The Pontiff Sulyvahn fight in Dark Souls 3 is a skill check that separates casual players from dedicated ones.",
    "I can't believe how addictive Balatro is, and I've spent more time playing poker roguelike than actual poker now.",
    (
        "My Helldivers 2 squad keeps getting wiped by Chargers because nobody brings enough anti tank weapons to the "
        "mission."
    ),
    (
        "The Gwyn fight in Dark Souls is surprisingly easy if you can parry, but the music makes it emotionally "
        "devastating."
    ),
    (
        "I've been playing Palworld and the base building combined with creature collection is scratching an itch I "
        "didn't know I had."
    ),
    (
        "The Bell Gargoyles in Dark Souls are the first real challenge, and summoning Solaire makes the fight so much "
        "easier."
    ),
    "My Lethal Company runs always end with someone getting grabbed by a Bracken because they wandered off alone.",
    (
        "The Sif fight in Dark Souls is heartbreaking once you know the lore, especially after doing the DLC content "
        "first."
    ),
    "I finally got the Redrix Claymore in Destiny 2 before it was sunset, and the grind for that weapon was insane.",
    (
        "My Deep Rock Galactic team composition is always wrong because everyone wants to play Scout and nobody picks "
        "Driller."
    ),
    (
        "The Quelaag fight in Dark Souls is where many players quit, but learning her patterns makes her surprisingly "
        "manageable."
    ),
    (
        "I've been playing Content Warning and the monster encounters are hilarious when everyone panics and forgets "
        "to record footage."
    ),
    (
        "The Nito fight in Dark Souls requires a divine weapon for the skeletons, and I learned that after dying "
        "repeatedly."
    ),
    "My Sons of the Forest base keeps getting destroyed by cannibals because I built too close to a patrol route.",
    "The Asylum Demon in Dark Souls teaches you that running away is sometimes the correct strategy in these games.",
    (
        "I can't believe how good the audio design in Dead Space remake is, and the necromorphs are more terrifying "
        "than ever."
    ),
    (
        "My Raft playthrough has been going for thirty hours, and we still haven't found all the story locations on "
        "the map."
    ),
    "The Centipede Demon in Dark Souls is annoying because of the arena, and the Orange Charred Ring makes it trivial.",
    (
        "I've been playing Grounded and the spiders in that game trigger genuine arachnophobia even though they're "
        "technically small."
    ),
    (
        "The Ceaseless Discharge in Dark Souls can be cheesed so easily that fighting him legitimately feels like a "
        "waste of time."
    ),
    "My Valheim server has a massive base that took weeks to build, and the building system is surprisingly deep.",
    "The Iron Golem in Dark Souls can be knocked off the edge, and discovering that made the fight anticlimactic.",
    "I finally got all the achievements in Hades after over a hundred escape attempts, and the epilogue was worth it.",
    (
        "My No Man's Sky base spans multiple planets now, and the base building improvements have made the game so "
        "much better."
    ),
    (
        "The Taurus Demon in Dark Souls can be plunged for massive damage, and learning that trick changed how I "
        "approach bosses."
    ),
    (
        "I've been playing Dave the Diver and the restaurant management combined with underwater exploration is "
        "surprisingly addictive."
    ),
    "The Moonlight Butterfly in Dark Souls is easy if you have ranged attacks, but melee only builds struggle so much.",
    (
        "My Satisfactory factory has become so optimized that I spend more time on logistics than actually exploring "
        "the map."
    ),
    "The Gargoyles in Dark Souls 2 are way harder than the original because there are so many of them at once.",
    (
        "I can't stop playing Cult of the Lamb, and the roguelike dungeon crawling combined with cult management is "
        "genius."
    ),
    "My Core Keeper mining operation has gone so deep that I've lost track of where my original base even is.",
    "The Pursuer in Dark Souls 2 can be parried with the ballista, and discovering that secret made me feel so clever.",
    (
        "I've been playing Inscryption and the meta narrative twists caught me completely off guard, what an "
        "incredible experience."
    ),
    (
        "The Looking Glass Knight in Dark Souls 2 can summon real players, and getting invaded during a boss fight is "
        "terrifying."
    ),
    (
        "My V Rising castle has become a sprawling fortress, and the vampire survival mechanics are surprisingly well "
        "designed."
    ),
    (
        "The Freja fight in Dark Souls 2 requires you to attack the heads, and the camera makes that incredibly "
        "frustrating."
    ),
    "I finally beat Sifu without dying once after mastering the combat system, and the aging mechanic is so creative.",
    "My Craftopia base has automated farms for everything, and the progression system keeps me coming back for more.",
    (
        "The Velstadt fight in Dark Souls 2 hits hard emotionally once you understand his dedication to protecting "
        "Vendrick."
    ),
    (
        "I've been playing Tunic and the manual discovery mechanic is such a clever way to teach players without "
        "tutorials."
    ),
    "The Sinh fight in Dark Souls 2 destroys your weapons so fast that you need multiple backups to finish the fight.",
    (
        "My Astroneer base has spread across three planets, and the automation systems make resource gathering almost "
        "passive now."
    ),
    "The Burnt Ivory King fight in Dark Souls 2 requires finding the Loyce Knights first, or the adds overwhelm you.",
    "I can't believe how polished Hi Fi Rush is, and the rhythm action combat is so satisfying when you hit the beat.",
    (
        "My Enshrouded base is built into a cliff face, and the building system allows for some incredibly creative "
        "designs."
    ),
    "The Alonne fight in Dark Souls 2 rewards perfect play with a special death animation, and I finally got it.",
    (
        "I've been playing Dredge and the cosmic horror fishing game concept shouldn't work, but it's absolutely "
        "captivating."
    ),
    (
        "The Darklurker in Dark Souls 2 requires joining the Pilgrims of Dark covenant, and the fight is brutally "
        "difficult."
    ),
    (
        "My Nightingale realm has become a sprawling estate, and the realm card system adds so much variety to "
        "exploration."
    ),
]

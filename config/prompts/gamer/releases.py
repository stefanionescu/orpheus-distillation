"""Gaming prompts: more examples of fifteen to thirty-seven words about specific games."""

from __future__ import annotations

RELEASES: list[str] = [
    "The Ancient Dragon in Dark Souls 2 has a one shot fire breath that covers the entire arena unfairly.",
    (
        "I finally got all the Steam achievements in Hades 2 early access, and the game is already incredible even "
        "unfinished."
    ),
    (
        "My Once Human base has defenses against both monsters and other players, and the survival mechanics are "
        "surprisingly deep."
    ),
    (
        "The Vendrick fight in Dark Souls 2 requires Giant Souls to deal real damage, and I fought him naked the first "
        "time."
    ),
    (
        "I've been playing Pacific Drive and the car maintenance survival mechanics combined with the anomaly zones "
        "are so unique."
    ),
    "The Nashandra fight in Dark Souls 2 is disappointingly easy after everything you go through to reach her throne.",
    "My Soulmask tribe has grown so large that managing everyone's needs has become a full time job in itself.",
    (
        "The Elana fight in Dark Souls 2 keeps summoning Velstadt, and fighting two bosses at once is absolutely "
        "miserable."
    ),
    (
        "I can't stop playing Supermarket Simulator even though it's just stocking shelves, the satisfaction is oddly "
        "compelling."
    ),
    "My Abiotic Factor lab has become a fortress against the monsters, and the crafting depth keeps surprising me.",
    "The Throne Watcher and Defender in Dark Souls 2 can resurrect each other, making the fight a DPS race.",
    "I've been playing Manor Lords and the medieval city builder scratches an itch that Banished left years ago.",
    "The Sinh poison in Dark Souls 2 builds up so fast that you need moss or miracles to survive the fight.",
    (
        "My Myth of Empires territory has expanded across the entire server, and the diplomacy with other clans is "
        "intense."
    ),
    "The Blue Smelter Demon in Dark Souls 2 is just a reskin with magic damage, and the run back is torture.",
    "I finally beat Elden Ring at level one without summons, and Malenia took over two hundred attempts to defeat.",
    (
        "My Bellwright village has grown from a small camp to a thriving settlement, and the management systems are "
        "satisfying."
    ),
    "The Lud and Zallen fight in Dark Souls 2 has the worst run back in the entire series through Frigid Outskirts.",
    (
        "I've been playing Gray Zone Warfare and the extraction shooter mechanics combined with the open world are "
        "promising."
    ),
    "The Smelter Demon run in Dark Souls 2 is almost harder than the actual boss because of all the Alonne Knights.",
    "My Last Epoch build finally came together at endgame, and the Monolith of Fate grinding is actually enjoyable.",
    "The Royal Rat Authority in Dark Souls 2 is only hard because of the small rats that inflict toxic buildup.",
    "I can't believe how good Balatro is for a poker roguelike, and the joker synergies create insane scoring combos.",
    "My Icarus prospect went horribly wrong when a storm destroyed my shelter and I had to survive with nothing.",
    "The Covetous Demon in Dark Souls 2 is a joke boss, but the Undead Purgatory enemies are surprisingly dangerous.",
    "I've been playing The Finals and the destruction physics combined with the game show aesthetic is so refreshing.",
    (
        "The Executioner's Chariot in Dark Souls 2 requires pulling the lever, and I died so many times learning the "
        "gimmick."
    ),
    "My Palworld base has become a factory with Pals doing all the work, and the automation is surprisingly deep.",
    (
        "The Skeleton Lords in Dark Souls 2 are easy individually, but the skeleton spawns can overwhelm unprepared "
        "players."
    ),
    "I finally got Recluse in Destiny 2 before it was sunset, and that weapon dominated the Crucible for so long.",
    (
        "My Enshrouded Flame Altar has been upgraded to maximum, and the shroud exploration is finally manageable with "
        "better gear."
    ),
    "The Mytha fight in Dark Souls 2 requires draining the poison, and I fought her in the poison my first attempt.",
    (
        "I've been playing Helldivers 2 and spreading managed democracy across the galaxy is the most fun I've had in "
        "co op."
    ),
    "The Rotten in Dark Souls 2 is surprisingly easy for a Great Soul boss, and the arena is refreshingly simple.",
    (
        "My Nightingale realm cards have created some incredibly challenging environments, and the procedural "
        "generation keeps things fresh."
    ),
    "The Old Iron King in Dark Souls 2 is easy, but the hole in the arena has killed me more than he has.",
    "I can't stop playing Lethal Company with friends, and the proximity chat creates the funniest horror moments.",
    (
        "My Content Warning footage has gone viral because we captured the most ridiculous monster encounter possible "
        "on camera."
    ),
    (
        "The Scorpioness Najka in Dark Souls 2 burrows underground, and her tail attacks have deceptive range that "
        "catches me."
    ),
    "I've been playing Skull and Bones and the ship combat is satisfying, but the live service elements feel hollow.",
    "The Prowling Magus in Dark Souls 2 is barely a boss, and the congregation dies faster than regular enemies.",
    (
        "My Granblue Fantasy Relink team has finally mastered the Proud difficulty raids, and the action combat is so "
        "fluid."
    ),
    (
        "The Duke's Dear Freja in Dark Souls 2 requires attacking the heads, and the small spiders are more annoying "
        "than her."
    ),
    (
        "I finally got the Whisper of the Worm in Destiny 2 before they changed the mission, and the jumping puzzle "
        "was brutal."
    ),
    (
        "My Tekken 8 rank has been climbing since I learned proper punishment and stopped mashing during pressure "
        "situations."
    ),
    (
        "The Demon of Song in Dark Souls 2 has such a creepy design, but the fight itself is disappointingly "
        "straightforward."
    ),
    (
        "I've been playing Like a Dragon Infinite Wealth and the job system combined with the Hawaii setting is "
        "incredible."
    ),
    "The Giant Lord in Dark Souls 2 is great for soul farming, and I've killed him hundreds of times for levels.",
    (
        "My Street Fighter 6 drive gauge management has improved so much, and understanding when to burnout is crucial "
        "now."
    ),
    (
        "The Guardian Dragon in Dark Souls 2 is a pushover compared to other dragons in the series, almost "
        "disappointingly easy."
    ),
    (
        "I can't believe how good Persona 3 Reload looks, and the quality of life improvements make the game so much "
        "better."
    ),
    "My Dragon's Dogma 2 pawn has become so popular that I'm getting tons of rift crystals from other players.",
    "The Last Giant in Dark Souls 2 is a good introductory boss, teaching players to stay under larger enemies.",
    (
        "I've been playing Final Fantasy 7 Rebirth and the open world exploration combined with the story is "
        "everything I wanted."
    ),
    "The Dragonrider in Dark Souls 2 can fall off the arena, and baiting him to the edge is the easiest strategy.",
    (
        "My Rise of the Ronin playthrough has me torn between factions, and the historical setting is beautifully "
        "realized."
    ),
    "The Flexile Sentry in Dark Souls 2 has two sides to attack, and the rising water adds unnecessary pressure.",
    "I finally got all the Unown forms in Pokemon Legends Arceus, and the Solaceon Ruins were tedious but worth it.",
    (
        "My Unicorn Overlord army composition has been optimized for every battle type, and the tactical depth is "
        "surprising."
    ),
    "The Ruin Sentinels in Dark Souls 2 are a brutal early game trio, and fighting them in the doorway helps.",
    (
        "I've been playing Granblue Fantasy Relink and the endgame grind for Terminus weapons is incredibly time "
        "consuming but rewarding."
    ),
    "The Lost Sinner in Dark Souls 2 is much easier with the torch lit, and her aggression is relentless otherwise.",
    (
        "My Metaphor ReFantazio party has been carefully balanced for every archetype, and the Press Turn combat is "
        "satisfying."
    ),
    "The Belfry Gargoyles in Dark Souls 2 are the worst gank boss, with up to six spawning during the fight.",
    "I can't stop playing Balatro, and discovering new joker synergies that break the game is endlessly satisfying.",
    "My Elden Ring Shadow of the Erdtree playthrough has been brutal, and the new bosses are even harder than before.",
    "The Smelter Demon in Dark Souls 2 deals fire damage just by being near him, and that chip damage adds up.",
    (
        "I've been playing Black Myth Wukong and the boss designs are incredible, some of the best action combat I've "
        "experienced."
    ),
    "The Old Dragonslayer in Dark Souls 2 is just discount Ornstein, and fighting him solo feels wrong without Smough.",
    (
        "My Wuthering Waves team has finally been optimized for the endgame content, and the combat system is "
        "incredibly fluid."
    ),
    (
        "The Pursuer keeps appearing throughout Dark Souls 2, and his relentless stalking makes every encounter tense "
        "and memorable."
    ),
    "I finally got the Outbreak Perfected catalyst in Destiny 2, and the SIVA nanites make add clear so satisfying.",
    "My Zenless Zone Zero team composition has been built around perfect dodge mechanics, and the style is unmatched.",
    "The Throne of Want in Dark Souls 2 requires defeating all the Great Souls, and the journey there is grueling.",
    (
        "I've been playing The First Descendant and the looter shooter mechanics are solid, even if the story is "
        "forgettable."
    ),
    "The Memory of the Old Iron King in Dark Souls 2 has Sir Alonne, one of the best designed bosses in the game.",
    (
        "My Honkai Star Rail account finally has a full team of limited five stars, and the turn based combat is "
        "addictive."
    ),
    "The Sinh the Slumbering Dragon fight in Dark Souls 2 is beautiful, and his aerial attacks are surprisingly fair.",
    (
        "I can't believe how polished Astro Bot is, and the PlayStation nostalgia combined with the platforming is "
        "pure joy."
    ),
    "My Monster Hunter Wilds anticipation is through the roof after the beta, and the seamless world is incredible.",
    (
        "The Eleum Loyce in Dark Souls 2 has the best atmosphere in the DLC, and the frozen kingdom is hauntingly "
        "beautiful."
    ),
    (
        "I've been playing Indiana Jones and the Great Circle, and the adventure game mechanics combined with the "
        "setting are perfect."
    ),
    "The Fume Knight in Dark Souls 2 is considered one of the hardest bosses in the series for good reason.",
    "My Path of Exile 2 early access build has been theory crafted for months, and I'm ready for the grind.",
    (
        "The Brume Tower in Dark Souls 2 has the Ashen Idols that heal enemies, and destroying them is essential for "
        "progress."
    ),
    "I finally got the Anarchy exotic in Destiny 2 before it was nerfed, and that weapon was absolutely broken.",
    (
        "My Stalker 2 playthrough has been tense, and the Zone atmosphere combined with the survival mechanics is "
        "incredible."
    ),
    (
        "The Shulva in Dark Souls 2 has the ghost enemies that require special conditions to kill, and they're so "
        "annoying."
    ),
    (
        "I've been playing Delta Force and the extraction shooter mechanics combined with the larger scale warfare is "
        "promising."
    ),
    "The Iron Passage in Dark Souls 2 is the worst area in the DLC, and the run to the Blue Smelter is torture.",
    (
        "My Marvel Rivals team composition has been optimized for synergy, and the hero shooter mechanics are "
        "surprisingly deep."
    ),
    "The Cave of the Dead in Dark Souls 2 has the Gank Squad boss, three NPCs that fight together unfairly.",
    (
        "I can't stop playing Thank Goodness You're Here, and the British humor combined with the absurdist gameplay "
        "is hilarious."
    ),
]

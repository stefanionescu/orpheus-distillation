"""Gaming prompts: long questions and exclamations, then the first game-specific examples."""

from __future__ import annotations

BOSSES: list[str] = [
    # LONG QUESTIONS
    (
        "Why do the developers keep adding new content instead of fixing the fundamental balance issues that have been "
        "plaguing the competitive scene since the game launched?"
    ),
    (
        "How am I supposed to compete against players who have been grinding this game for years when the matchmaking "
        "keeps putting me in lobbies way above my skill level?"
    ),
    (
        "Does anyone else feel like the grind has become more tedious with each update, or am I just burnt out after "
        "playing this game for so many hours?"
    ),
    (
        "Why would the developers remove the feature that everyone loved without any explanation or community "
        "feedback, when it was clearly one of the best parts of the game?"
    ),
    (
        "Can someone explain how the ranking system actually works, because I've been winning consistently but my rank "
        "refuses to move up no matter how well I perform?"
    ),
    (
        "How do professional players maintain their reaction time and mechanical skill when they're playing the same "
        "game for eight or more hours every single day?"
    ),
    (
        "Why does every game nowadays require a constant internet connection even for single player content that has "
        "no online features or multiplayer components whatsoever?"
    ),
    (
        "Does the endgame content actually get more interesting after the initial grind, or is it just the same "
        "repetitive activities with slightly better rewards?"
    ),
    (
        "How am I supposed to learn all these complex mechanics when the game doesn't explain anything and expects you "
        "to figure everything out through trial and error?"
    ),
    (
        "Why do developers keep releasing games in unfinished states and expecting the community to pay full price for "
        "something that won't be complete for months?"
    ),
    # LONG EXCLAMATIONS
    (
        "I can't believe I finally beat the boss that's been destroying me for the past three weeks, and my hands are "
        "literally shaking from the adrenaline right now!"
    ),
    (
        "The developers just announced they're shutting down the servers next year, and I'm devastated because this "
        "game has been a huge part of my life for so long!"
    ),
    (
        "That was the most incredible comeback I've ever witnessed in competitive gaming, and I'm so glad I was "
        "watching the stream live when it happened!"
    ),
    (
        "I've been waiting for this game to release for over five years, and now that it's finally here, I can't "
        "believe how much it exceeded my expectations!"
    ),
    (
        "The lag spike that killed me right before I clutched the round was the most frustrating thing that's ever "
        "happened to me in my entire gaming career!"
    ),
    (
        "I just realized I've been playing with the wrong settings this entire time, and fixing them has made me "
        "instantly better at the game, I'm so annoyed!"
    ),
    (
        "The community figured out a glitch that lets you skip half the game, and watching speedrunners exploit it in "
        "real time was absolutely mind blowing!"
    ),
    (
        "I can't believe the developers actually listened to community feedback and reverted the terrible changes they "
        "made, this is the best patch in years!"
    ),
    (
        "That player just pulled off a combo that theoretically shouldn't be possible according to the frame data, and "
        "I need to know how they did it!"
    ),
    (
        "The seasonal event rewards are actually worth grinding for this time, and I'm so excited to finally have "
        "content that respects my time investment!"
    ),
    # GAME-SPECIFIC EXAMPLES - 15-37 WORDS
    (
        "I've been grinding Elden Ring for weeks trying to beat Malenia, and her Waterfowl Dance attack still destroys "
        "me every single time without fail."
    ),
    (
        "The Creepers in Minecraft keep blowing up my builds right when I'm about to finish them, and I'm losing my "
        "mind over here."
    ),
    (
        "My Valorant aim has gotten so much better since I started practicing in the range, and I finally hit Immortal "
        "rank last night."
    ),
    (
        "I can't believe I just got a Fatalis kill in Monster Hunter World after carting twice, that was way too close "
        "for comfort."
    ),
    (
        "The new Legend in Apex is completely broken, and everyone's abusing their tactical ability in ranked matches "
        "until Respawn nerfs them."
    ),
    (
        "I've been trying to get the Vex Mythoclast in Destiny to drop for months, and my raid team is getting tired "
        "of running it."
    ),
    (
        "Kratos and Atreus have such an incredible dynamic in God of War Ragnarok, and the story had me emotional the "
        "entire playthrough."
    ),
    (
        "My Minecraft server just got griefed by someone who found our base coordinates, and now I have to rebuild "
        "everything from scratch."
    ),
    (
        "The Lich King fight in World of Warcraft is still one of the most epic raid encounters I've ever experienced "
        "in any MMO."
    ),
    (
        "I finally got Platinum God in The Binding of Isaac after hundreds of hours, and I never want to see Delirium "
        "again."
    ),
    (
        "Playing as Kiryu in Yakuza is always a blast, and the heat actions never get old no matter how many times I "
        "use them."
    ),
    "The Diamond City radio in Fallout 4 has been stuck in my head for days, and I keep humming the songs at work.",
    "I just got invaded by a twink build in Dark Souls 3 at the High Wall, and they destroyed me in two hits.",
    (
        "The Warden in Minecraft is absolutely terrifying, and I refuse to go anywhere near the Deep Dark biome "
        "without full Netherite armor."
    ),
    (
        "My Stardew Valley farm is finally turning a profit after three in game years, and I can finally afford to "
        "upgrade my house."
    ),
    (
        "The Moonlight Greatsword in Elden Ring carried me through most of the game, and the weapon art is incredibly "
        "satisfying to land."
    ),
    (
        "I've been playing Hades for fifty hours and I still haven't beaten the final boss, but each run teaches me "
        "something new."
    ),
    (
        "The Nether in Minecraft is so much better after the update, and the new biomes make exploration actually "
        "worth the danger now."
    ),
    "My Call of Duty lobbies have been nothing but sweats lately, and I can't even enjoy a casual match anymore.",
    (
        "The Clickers in The Last of Us still give me anxiety even after multiple playthroughs, those sound effects "
        "are nightmare fuel."
    ),
    (
        "I finally beat Sans in Undertale after dying over a hundred times, and my hands were shaking during the "
        "entire fight."
    ),
    (
        "The Phantom Thieves in Persona 5 have such great chemistry, and the Palace infiltrations never feel "
        "repetitive thanks to the style."
    ),
    (
        "My Rocket League rank keeps bouncing between Diamond and Platinum because I can't consistently hit aerials "
        "when it matters most."
    ),
    (
        "The Enderdragon fight in Minecraft was anticlimactic after all the preparation, but the credits sequence made "
        "the journey feel worth it."
    ),
    (
        "I've been playing Civilization 6 for twelve hours straight without realizing it, and the one more turn "
        "mentality is dangerously addictive."
    ),
    (
        "The Rathalos in Monster Hunter keeps flying away whenever I mount it, and I'm running out of flash pods to "
        "bring it down."
    ),
    (
        "My Animal Crossing island finally has a five star rating after months of decorating, and Isabelle's "
        "announcement made me so happy."
    ),
    (
        "The Abyss Watchers in Dark Souls 3 are my favorite boss because the music and the lore make the fight feel so "
        "epic."
    ),
    (
        "I can't stop playing Tetris Effect, and the Zone mechanic combined with the music creates such a meditative "
        "gaming experience."
    ),
    "The Blades of Chaos in God of War feel so satisfying to use, and chaining runic attacks together never gets old.",
    (
        "My Overwatch team keeps getting rolled because nobody wants to switch off damage, and we desperately need a "
        "second tank."
    ),
    (
        "I finally got the Master Sword in Breath of the Wild after completing all the shrines, and it was worth every "
        "puzzle."
    ),
    "The Flood reveal in Halo Combat Evolved is still one of the most terrifying moments in gaming history for me.",
    "My Sims keep dying in stupid ways because I forgot to put doors on rooms, and I'm a terrible virtual landlord.",
    "The Ashtray Maze in Control is one of the best video game levels ever made, and the music sync is perfect.",
    (
        "I've been grinding Grandmaster Nightfalls in Destiny 2 for the Adept weapons, and the difficulty spike is "
        "absolutely brutal."
    ),
    (
        "The Leviathan axe recall in God of War is the most satisfying game mechanic I've experienced in years, I "
        "never get tired of it."
    ),
    (
        "My Terraria world has every boss defeated and every item collected, but I still keep coming back to build new "
        "things."
    ),
    "The Orphan of Kos in Bloodborne took me over fifty attempts, and that victory scream at the end was so cathartic.",
    (
        "I can't believe they nerfed Octane's stim in Apex again, he was already balanced and now he feels terrible to "
        "play."
    ),
    (
        "The Outer Wilds time loop mechanic is so clever, and piecing together the mystery felt like genuine discovery "
        "every session."
    ),
    (
        "My Pokemon team in Scarlet has the worst type coverage, but I refuse to bench my favorites for competitive "
        "viability."
    ),
    "The Nameless King in Dark Souls 3 is optional for a reason, and I wish I had skipped him on my first playthrough.",
    (
        "I've been playing Dead Cells for years and I still discover new synergies between weapons and mutations every "
        "run somehow."
    ),
    (
        "The Colossus fights in Shadow of the Colossus are still breathtaking, and the scale of those encounters has "
        "never been matched."
    ),
    (
        "My Warframe arsenal has over fifty weapons but I keep using the same three because the meta builds are too "
        "efficient."
    ),
    (
        "The Dancer of the Boreal Valley in Dark Souls 3 has such unusual attack timing that I can never get the "
        "dodges right."
    ),
    (
        "I finally beat Sekiro without using Kuro's Charm, and the deflect timing is permanently burned into my muscle "
        "memory now."
    ),
    (
        "The Taken King expansion saved Destiny for me, and Oryx is still one of the best raid bosses Bungie has ever "
        "designed."
    ),
    (
        "My Factorio factory has grown so complex that I need a second monitor just to keep track of all the "
        "production chains."
    ),
    (
        "The Fume Knight in Dark Souls 2 has the smallest margin for error, and his second phase still catches me off "
        "guard."
    ),
    (
        "I've been playing Hollow Knight for months trying to complete the Path of Pain, and the precision required is "
        "absolutely insane."
    ),
    (
        "The Nemesis system in Shadow of Mordor was revolutionary, and I still remember the orcs that killed me "
        "multiple times."
    ),
    (
        "My Diablo 4 Barbarian build finally hit the damage threshold for Tier 100 Nightmare Dungeons, and the grind "
        "was worth it."
    ),
    "The Thunderjaw in Horizon Zero Dawn is such a satisfying machine to fight once you learn all its weak points.",
    "I can't believe Cayde died in Destiny 2 Forsaken, and his final stand is still one of my favorite gaming moments.",
    "My Skyrim character has been a stealth archer for every single playthrough, and I can't seem to break the habit.",
    (
        "The Radahn Festival in Elden Ring is such a cool concept, and the fight feels like an actual war with all the "
        "summons."
    ),
    (
        "I've been playing Spelunky 2 for hundreds of hours and I still haven't reached the Sunken City legitimately "
        "without shortcuts."
    ),
    (
        "The Witcher 3 Blood and Wine expansion is basically a full game, and Toussaint is one of the most beautiful "
        "regions ever."
    ),
    (
        "My League of Legends ranked games always have at least one person who refuses to communicate or work with the "
        "team."
    ),
    (
        "The Godskin Duo in Elden Ring is the worst designed boss fight, and using sleep pots feels like the only "
        "viable strategy."
    ),
]

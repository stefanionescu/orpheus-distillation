"""Music prompts about more artists, songs, and genres, the second third."""

from __future__ import annotations

SCENES: list[str] = [
    "Shame's angular post punk evolved from Gang of Four homage to something more personal on 'Drunk Tank Pink.'",
    (
        "Squid's chaotic post punk incorporates jazz and electronic elements, their live shows unpredictable "
        "explosions of coordinated energy."
    ),
    (
        "Black Country, New Road's art rock blends klezmer, post rock, and chamber pop, Isaac Wood's anxious lyrics "
        "before his departure."
    ),
    (
        "Yard Act's spoken word post punk captures Northern English wit, James Smith's observations sharp and "
        "surprisingly moving."
    ),
    (
        "Wet Leg's debut captured slacker rock's return with deadpan humor, their Glastonbury slot proving indie "
        "guitar music's resilience."
    ),
    (
        "Porridge Radio's emotional indie rock builds from whispers to screams, Dana Margolin's vocals raw and "
        "uncompromising throughout."
    ),
    (
        "Goat Girl's feminist post punk addresses gentrification and politics with hooks that make their messages "
        "accessible and memorable."
    ),
    (
        "Sorry's art pop experiments with electronic textures and unconventional song structures, Asha Sheridan's "
        "vocals floating through dense productions."
    ),
    (
        "Nilüfer Yanya's indie rock incorporates R&B and jazz influences, her guitar playing as distinctive as her "
        "vocal delivery."
    ),
    (
        "Rina Sawayama's debut blended Y2K pop nostalgia with nu metal guitars, her British Japanese identity central "
        "to her vision."
    ),
    (
        "Self Esteem's theatrical pop addresses self worth and feminism, Rebecca Lucy Taylor's spoken word passages "
        "building to cathartic choruses."
    ),
    (
        "Dry Cleaning's spoken word post punk features Florence Shaw's deadpan observations over angular "
        "instrumentals, funny and unsettling simultaneously."
    ),
    (
        "Sleaford Mods' minimalist punk captures working class British anger, Jason Williamson's rants over Andrew "
        "Fearn's sparse beats."
    ),
    (
        "Kate Tempest's spoken word spans poetry and hip hop, her London narratives addressing class and community "
        "with literary ambition."
    ),
    (
        "Little Dragon's Swedish electronic pop blends Yukimi Nagano's vocals with organic and synthetic textures "
        "seamlessly."
    ),
    (
        "Robyn's 'Body Talk' reinvented pop for the streaming era, her dancing through tears aesthetic influencing "
        "countless artists afterward."
    ),
    (
        "The Knife's 'Silent Shout' pushed electronic pop into dark territory, Karin Dreijer's processed vocals "
        "creating something genuinely unsettling."
    ),
    (
        "Fever Ray's solo work extends The Knife's experimentation, her visual presentations as important as the music "
        "itself."
    ),
    (
        "Lykke Li's melancholic pop evolved from indie folk to darkwave, her voice conveying heartbreak across "
        "different sonic palettes."
    ),
    (
        "First Aid Kit's Americana harmonies brought Swedish sisters international acclaim, their Laurel Canyon "
        "influences filtered through Nordic sensibilities."
    ),
    (
        "José González's nylon string guitar and hushed vocals created intimate folk that soundtracked countless film "
        "trailers and commercials."
    ),
    (
        "Goat's anonymous psychedelic rock draws from African and Middle Eastern traditions, their masked performances "
        "adding mystique to heavy grooves."
    ),
    (
        "Opeth's progressive metal evolved into pure prog rock, Mikael Åkerfeldt abandoning death growls for clean "
        "vocals and complex arrangements."
    ),
    (
        "Meshuggah's polyrhythmic metal influenced djent and progressive metalcore, their eight string guitars "
        "creating rhythms that confound and hypnotize."
    ),
    (
        "At the Gates' 'Slaughter of the Soul' defined melodic death metal, its influence audible in metalcore decades "
        "later."
    ),
    (
        "Refused's 'The Shape of Punk to Come' predicted post hardcore's evolution, their reunion proving the album's "
        "continued relevance."
    ),
    (
        "Deftones' shoegaze influenced metal created a template that countless bands attempted to replicate without "
        "matching Chino Moreno's emotional range."
    ),
    (
        "Converge's 'Jane Doe' pushed hardcore to its emotional and technical extremes, Jacob Bannon's artwork as "
        "iconic as the music."
    ),
    (
        "Botch's mathcore influenced every technical hardcore band that followed, their reunion shows proving their "
        "legend status."
    ),
    (
        "The Locust's grindcore blasts lasted seconds, their insect costumes and synths making them art punk "
        "provocateurs as much as metal band."
    ),
    (
        "Lightning Bolt's bass and drums duo created noise rock that felt like being inside a jet engine, their "
        "basement shows legendary."
    ),
    (
        "Hella's math rock featured Zach Hill's drumming before Death Grips, his technical prowess already evident in "
        "instrumental chaos."
    ),
    (
        "Don Caballero's instrumental math rock influenced countless bands, Damon Che's drumming as compositionally "
        "central as any guitar part."
    ),
    (
        "Battles' 'Mirrored' brought math rock to wider audiences, their loop based approach creating something both "
        "cerebral and visceral."
    ),
    (
        "Tortoise's post rock incorporated jazz, dub, and electronic music, their Chicago scene influence extending to "
        "Wilco and beyond."
    ),
    (
        "Slint's 'Spiderland' invented post rock's quiet loud dynamics, its influence on Mogwai, Godspeed, and "
        "Explosions in the Sky immeasurable."
    ),
    (
        "Godspeed You! Black Emperor's orchestral post rock soundtracked apocalyptic visions, their anti capitalist "
        "politics matching their monumental compositions."
    ),
    (
        "Explosions in the Sky's cinematic instrumentals soundtracked 'Friday Night Lights' and countless emotional "
        "moments in film and television."
    ),
    (
        "Mogwai's Scottish post rock balanced beauty and brutality, Stuart Braithwaite's guitar creating walls of "
        "sound that could be tender or terrifying."
    ),
    (
        "Sigur Rós' Icelandic post rock created a language of its own, Jónsi's falsetto and bowed guitar unlike "
        "anything before."
    ),
    (
        "múm's Icelandic electronic folk incorporated music boxes and found sounds, their delicate textures "
        "influencing bedroom producers worldwide."
    ),
    (
        "Boards of Canada's nostalgic electronics evoked childhood memories through degraded samples and unsettling "
        "undertones beneath beautiful melodies."
    ),
    (
        "Autechre's abstract electronics pushed IDM to its limits, their recent eight hour releases challenging any "
        "notion of accessibility."
    ),
    (
        "Squarepusher's virtuoso bass playing merged with drum and bass programming, Tom Jenkinson's jazz fusion "
        "background evident throughout."
    ),
    (
        "\u00b5 Ziq's playful electronics balanced accessibility with experimentation, Mike Paradinas' Planet Mu label "
        "nurturing generations of electronic artists."
    ),
    (
        "Venetian Snares' breakcore incorporated classical samples and impossible drum programming, Aaron Funk's "
        "prolific output spanning multiple aliases."
    ),
    (
        "Amon Tobin's sample based productions evolved into Foley heavy sound design, his ISAM live show a landmark in "
        "audiovisual performance."
    ),
    (
        "Four Tet's organic electronics bridge folk and dance music, Kieran Hebden's DJ sets as influential as his "
        "studio productions."
    ),
    (
        "Caribou's psychedelic electronics evolved from folktronica to dance floor anthems, Dan Snaith's PhD in "
        "mathematics informing his precise productions."
    ),
    (
        "Gold Panda's sample based electronics captured urban loneliness, his UK bass influences filtered through a "
        "more contemplative sensibility."
    ),
    (
        "Mount Kimbie's post dubstep influenced James Blake and the entire UK bass scene, their guitar textures adding "
        "warmth to electronic productions."
    ),
    (
        "Actress' abstract electronics resist easy categorization, Darren Cunningham's productions feeling like "
        "transmissions from parallel dimensions."
    ),
    (
        "Dean Blunt's elusive output spans noise, R&B, and ambient, his Hype Williams project with Inga Copeland "
        "equally mysterious."
    ),
    (
        "Oneohtrix Point Never's synthesizer explorations evolved from new age pastiche to operatic productions for "
        "The Weeknd."
    ),
    (
        "Tim Hecker's ambient noise creates cathedrals of sound, his processed organ and guitar textures overwhelming "
        "in the best way."
    ),
    (
        "Fennesz's glitchy guitar processing created ambient music that felt organic despite its digital manipulation "
        "and software origins."
    ),
]

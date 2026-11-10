"""Music prompts of thirty to thirty-seven words about artists, albums, and genres."""

from __future__ import annotations

GENRES: list[str] = [
    (
        "Frank Ocean's decision to release 'Blonde' independently after fulfilling his contract showed that artists "
        "could succeed outside the major label system if they had built a truly dedicated fanbase."
    ),
    (
        "The production on Kendrick Lamar's 'To Pimp a Butterfly' draws from jazz, funk, and spoken word in ways that "
        "expand what hip hop can be sonically and thematically at once."
    ),
    (
        "Taylor Swift's ability to pivot from country to pop to indie folk while maintaining her fanbase demonstrates "
        "remarkable artistic flexibility and an understanding of her audience's willingness to follow her anywhere."
    ),
    (
        "When Prince performed 'While My Guitar Gently Weeps' at the Rock Hall induction, his solo at the end proved "
        "he was one of the greatest guitarists who ever lived on Earth."
    ),
    (
        "The way Billie Eilish and Finneas create entire albums in a bedroom challenges the notion that great music "
        "requires expensive studios and teams of professional engineers to produce something truly special."
    ),
    (
        "I've been listening to D'Angelo's 'Voodoo' for over twenty years now and I still hear new details in the "
        "production, new rhythmic pockets, new harmonic choices I hadn't noticed before."
    ),
    (
        "Stevie Wonder's run of albums from 'Music of My Mind' through 'Songs in the Key of Life' represents one of "
        "the greatest creative peaks in the history of popular music."
    ),
    (
        "The way Tyler, the Creator evolved from the shock value of 'Goblin' to the lush orchestration of 'Call Me If "
        "You Get Lost' shows genuine artistic growth and maturation over time."
    ),
    (
        "When I saw Kendrick Lamar perform 'Alright' at the BET Awards with the police car and American flag imagery, "
        "I knew I was watching a cultural moment unfold in real time."
    ),
    (
        "I can't believe how many times I've listened to 'Random Access Memories' by Daft Punk and still find new "
        "textures and details in the immaculately layered production work throughout."
    ),
    (
        "Adele's ability to make heartbreak anthems that resonate across demographics shows her gift for expressing "
        "universal emotions through specific personal experiences in ways that feel authentic and true to life."
    ),
    (
        "The way SZA's 'Ctrl' captured the anxieties and contradictions of modern relationships made it the defining "
        "R&B album of its era, speaking to a generation navigating love and self worth."
    ),
    (
        "When I heard 'Alright' by Kendrick Lamar for the first time, I understood immediately why it became an anthem "
        "for the Black Lives Matter movement and a generation's rallying cry."
    ),
    (
        "The production choices on Bon Iver's 'For Emma, Forever Ago' perfectly capture the isolation of its creation, "
        "Justin Vernon alone in a Wisconsin cabin processing heartbreak through layers of falsetto."
    ),
    (
        "I remember the first time I heard 'Bohemian Rhapsody' all the way through, not understanding how a six minute "
        "song with opera sections could work as a rock single, yet it does."
    ),
    (
        "The way Lauryn Hill raps and sings with equal conviction on 'The Miseducation of Lauryn Hill' broke down "
        "barriers between genres and proved hip hop and soul were always connected deeply."
    ),
    (
        "Erykah Badu's 'Baduizm' introduced neo soul to the mainstream, her combination of jazz scatting, hip hop "
        "sensibility, and Billie Holiday influenced phrasing creating something entirely new and deeply influential "
        "for others."
    ),
    (
        "The British Invasion of the nineteen sixties saw bands like The Beatles, The Rolling Stones, and The Who "
        "transform American blues and rock into something distinctly their own and revolutionary."
    ),
    (
        "Detroit's Motown Records created a hit factory that produced timeless songs by The Supremes, The Temptations, "
        "Stevie Wonder, and Marvin Gaye throughout the sixties and seventies with remarkable consistency."
    ),
    (
        "The punk explosion of nineteen seventy seven in both New York and London rejected the bloated excess of "
        "progressive rock in favor of raw energy and DIY ethics that anyone could embrace."
    ),
    (
        "Hip hop's golden age in the late eighties and early nineties produced artists like Public Enemy, A Tribe "
        "Called Quest, and De La Soul who expanded the genre's creative possibilities."
    ),
    (
        "The Seattle grunge scene gave the world Nirvana, Pearl Jam, Soundgarden, and Alice in Chains, bands that "
        "channeled Gen X alienation into heavy, emotional rock music that defined an era."
    ),
    (
        "Chicago house music emerged from underground clubs in the mid eighties, with producers like Frankie Knuckles "
        "and Marshall Jefferson creating the template for electronic dance music that would sweep the world."
    ),
    (
        "The Laurel Canyon scene of the late sixties brought together Joni Mitchell, Crosby, Stills, Nash and Young, "
        "and The Byrds in a creative community that defined folk rock's sound."
    ),
    (
        "Manchester's Haçienda club and Factory Records fostered bands like Joy Division, New Order, and The Smiths, "
        "creating a distinctive post punk sound that influenced decades of British music afterward."
    ),
    (
        "The Memphis soul sound of Stax Records, featuring Otis Redding, Sam and Dave, and Booker T. and the M.G.s, "
        "rivaled Motown with its grittier, more organic approach to soul."
    ),
    (
        "The CBGB club in New York's Bowery launched the careers of The Ramones, Blondie, Television, and Patti Smith, "
        "becoming the birthplace of American punk rock and new wave music."
    ),
    (
        "Jamaican sound system culture gave rise to ska, rocksteady, reggae, and eventually dancehall, with producers "
        "like Lee Scratch Perry pioneering dub's revolutionary studio experimentation with echo and reverb effects."
    ),
    (
        "The Paisley Park studio complex became Prince's creative laboratory, where he recorded himself playing "
        "virtually every instrument on albums that blended funk, rock, pop, and soul seamlessly together."
    ),
    (
        "Sun Records in Memphis launched the careers of Elvis Presley, Johnny Cash, Jerry Lee Lewis, and Carl Perkins, "
        "creating the rockabilly sound that birthed rock and roll itself in America."
    ),
    (
        "The Wrecking Crew session musicians played on countless sixties hits, their anonymous contributions backing "
        "everyone from The Beach Boys to Simon and Garfunkel on records that shaped popular music history."
    ),
    (
        "The Atlanta trap scene that gave us Future, Young Thug, and Migos fundamentally changed hip hop production, "
        "with 808 drums and atmospheric synths becoming the dominant sound of the twenty tens era."
    ),
    (
        "Chicago drill music emerged from the South Side in the early twenty tens, its dark production and unflinching "
        "lyrics influencing artists from the UK to Brooklyn and beyond worldwide today."
    ),
    (
        "The London grime scene that produced Skepta, Stormzy, and Dizzee Rascal created a distinctly British form of "
        "hip hop that finally broke through to American audiences in the mid twenty tens era."
    ),
    (
        "Detroit techno pioneers Juan Atkins, Derrick May, and Kevin Saunderson created a futuristic sound that would "
        "influence electronic music globally while remaining rooted in their city's industrial landscape and history."
    ),
    (
        "The Bronx block parties where DJ Kool Herc extended the breaks of funk records laid the foundation for hip "
        "hop culture, a moment of innovation that changed music history forever worldwide."
    ),
    (
        "Nashville's country music industry has always balanced tradition and innovation, with each generation of "
        "artists pushing boundaries while respecting the genre's storytelling roots and instrumental heritage from the "
        "past."
    ),
    (
        "The Los Angeles beat scene that produced Flying Lotus, Thundercat, and Kamasi Washington blurred lines "
        "between jazz, hip hop, and electronic music in ways that continue to influence producers worldwide."
    ),
    (
        "New Orleans second line rhythms have influenced everything from jazz to funk to hip hop, the city's musical "
        "traditions providing a foundation for countless innovations in American popular music history."
    ),
    (
        "The Bristol trip hop scene that gave us Massive Attack, Portishead, and Tricky created atmospheric, sample "
        "heavy music that influenced film scores, advertising, and electronic music for decades afterward worldwide."
    ),
    (
        "The Seattle grunge explosion of nineteen ninety one transformed alternative rock from college radio curiosity "
        "to mainstream phenomenon, with Nirvana's 'Nevermind' becoming the unlikely soundtrack of a generation of "
        "youth."
    ),
    (
        "Philadelphia's neo soul movement in the late nineties, centered around The Roots and artists like Jill Scott "
        "and Musiq Soulchild, revived organic R&B production in an era of synthetic sounds."
    ),
    (
        "The Jamaican dancehall scene has continuously evolved from roots reggae through digital rhythms to modern "
        "fusions with hip hop and pop, influencing global music while maintaining its distinct identity always."
    ),
    (
        "Berlin's techno scene emerged after the Wall fell, with clubs like Tresor and Berghain becoming temples of "
        "electronic music that attracted pilgrims from around the world seeking transcendence through sound."
    ),
    (
        "The Memphis rap scene that produced Three 6 Mafia, 8Ball and MJG, and later Yo Gotti created a dark, bass "
        "heavy sound that would later influence trap music's development significantly."
    ),
    (
        "Hip hop has become the dominant cultural force of the twenty first century, its influence extending beyond "
        "music into fashion, language, politics, and every aspect of global popular culture today worldwide."
    ),
    (
        "The way streaming algorithms shape what music gets heard raises questions about whether we're discovering new "
        "artists or just being fed what platforms think will keep us engaged longer."
    ),
    (
        "Vinyl's resurgence among younger listeners suggests a desire for tangible, intentional music experiences in "
        "an age of infinite digital access and algorithmic recommendation systems that feel impersonal and cold."
    ),
    (
        "The democratization of music production through affordable software has created more music than ever, but "
        "also made it harder for artists to stand out in an oversaturated market today."
    ),
    (
        "Music festivals have evolved from countercultural gatherings to corporate sponsored experiences, raising "
        "questions about authenticity and the commodification of communal musical experiences that once felt "
        "revolutionary and free spirited."
    ),
    (
        "Sample based music forces us to reconsider what originality means, as producers create new art from fragments "
        "of existing recordings in ways that challenge traditional notions of authorship and creativity."
    ),
    (
        "The decline of music criticism in traditional media has been offset by the rise of fan communities and "
        "YouTube essayists who analyze music with unprecedented depth and genuine enthusiasm today."
    ),
    (
        "Regional music scenes still matter despite the internet's flattening effect, with cities like Atlanta, "
        "London, and Lagos continuing to produce distinctive sounds that eventually go global and influence everyone."
    ),
    (
        "The tension between artistic integrity and commercial viability has always existed, but streaming economics "
        "have made it harder than ever for musicians to sustain careers on their own creative terms."
    ),
    (
        "The production on Massive Attack's 'Mezzanine' is so dark and atmospheric that it's been used in countless "
        "film trailers, its influence extending far beyond the trip hop genre it defined."
    ),
]

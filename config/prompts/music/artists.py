"""Music prompts: artist names, reactions, short statements and questions, then the first long prompts."""

from __future__ import annotations

ARTISTS: list[str] = [
    # ULTRA SHORT - ARTIST NAMES & REACTIONS (50)
    "Beyoncé!",
    "Drake's new album!",
    "Taylor Swift era!",
    "Kendrick dropped!",
    "The Beatles forever.",
    "Radiohead vibes.",
    "Daft Punk legends.",
    "Billie Eilish mood.",
    "Frank Ocean masterpiece.",
    "Adele's voice!",
    "Queen rocks!",
    "Nirvana grunge.",
    "Mozart genius.",
    "Bach perfection.",
    "Coltrane magic.",
    "Miles Davis cool.",
    "Stevie Wonder!",
    "Prince iconic.",
    "Bowie legendary.",
    "Aretha Franklin!",
    "Whitney Houston!",
    "Michael Jackson!",
    "Elvis Presley!",
    "Bob Marley vibes.",
    "Tupac lives.",
    "Biggie Smalls!",
    "Eminem bars.",
    "Jay Z empire.",
    "Kanye genius.",
    "SZA vocals.",
    "The Weeknd!",
    "Rihanna!",
    "Bruno Mars!",
    "Lady Gaga!",
    "Ed Sheeran.",
    "Post Malone vibes.",
    "Travis Scott!",
    "Tyler, the Creator!",
    "Childish Gambino.",
    "Arctic Monkeys!",
    "Tame Impala!",
    "Fleetwood Mac.",
    "Pink Floyd.",
    "Led Zeppelin!",
    "The Rolling Stones.",
    "Coldplay.",
    "U2 classics.",
    "Metallica!",
    "AC/DC rocks.",
    "Foo Fighters!",
    # SHORT STATEMENTS (50)
    "Bohemian Rhapsody by Queen is a six minute masterpiece.",
    "Billie Jean's bassline is instantly recognizable worldwide.",
    "Stairway to Heaven remains Led Zeppelin's defining song.",
    "Smells Like Teen Spirit changed rock music forever.",
    "Purple Rain showcases Prince's incredible guitar work.",
    "Hotel California's guitar solo is absolutely legendary.",
    "Imagine by John Lennon still resonates today.",
    "Hey Jude builds to an unforgettable coda.",
    "What's Going On by Marvin Gaye addressed social issues.",
    "Respect became Aretha Franklin's signature anthem.",
    "Superstition features Stevie Wonder's iconic clavinet riff.",
    "Born to Run defined Bruce Springsteen's sound.",
    "London Calling mixed punk with reggae and jazz.",
    "God Only Knows is Brian Wilson's greatest achievement.",
    "Thriller's music video changed pop culture forever.",
    "Sweet Child O' Mine opens with that iconic riff.",
    "Lose Yourself won Eminem an Academy Award.",
    "Rolling in the Deep showcases Adele's powerful vocals.",
    "Crazy in Love launched Beyoncé's solo career.",
    "Uptown Funk is Bruno Mars at his funkiest.",
    "Bad Guy became Billie Eilish's breakthrough hit.",
    "Blinding Lights brought The Weeknd to new heights.",
    "Old Town Road broke Billboard chart records.",
    "Shape of You dominated radio for months.",
    "Hotline Bling's dance moves went viral instantly.",
    "Formation was a cultural and political statement.",
    "Jazz originated in New Orleans in the early twentieth century.",
    "Blues influenced virtually every genre of popular music.",
    "Rock and roll emerged from rhythm and blues.",
    "Hip hop started in the Bronx in nineteen seventy three.",
    "Electronic dance music dominates festival culture today.",
    "Country music tells stories of love and heartbreak.",
    "Reggae carries messages of peace and resistance.",
    "Punk rock rejected mainstream commercial values.",
    "Heavy metal pushed guitar distortion to extremes.",
    "Soul music expresses deep emotional authenticity.",
    "R&B blends rhythm, blues, and gospel influences.",
    "Folk music preserves cultural traditions through song.",
    "Disco brought dance floors to life in the seventies.",
    "Grunge combined punk attitude with heavy guitars.",
    "Indie rock values artistic independence above all.",
    "K pop has become a global phenomenon.",
    "Afrobeats is taking over international charts.",
    "Latin trap blends reggaeton with hip hop beats.",
    "Lo fi hip hop provides the perfect study soundtrack.",
    "Fela Kuti combined Nigerian highlife with American funk.",
    "BTS brought K pop to mainstream Western audiences.",
    "Ravi Shankar introduced Indian classical music to the West.",
    "Bad Bunny has made reggaeton globally dominant.",
    "The 808 kick drum defines modern trap music.",
    # SHORT QUESTIONS & EXCLAMATIONS (50)
    "Have you heard the new Kendrick Lamar album yet?",
    "What's your favorite Taylor Swift era?",
    "Did you catch Beyoncé's Renaissance tour?",
    "Who do you think is the greatest guitarist of all time?",
    "Have you listened to Frank Ocean's Blonde?",
    "What's your go to karaoke song?",
    "Why does Bohemian Rhapsody still give me chills?",
    "What's your most played Spotify track this year?",
    "Have you ever seen your favorite artist live?",
    "What album changed your life?",
    "Why does vinyl sound warmer than digital?",
    "What's the best concert you've ever attended?",
    "Have you discovered any new artists lately?",
    "Why do sad songs feel so cathartic?",
    "What's on your road trip playlist?",
    "That guitar solo absolutely shredded!",
    "The drop in this song is insane!",
    "Her voice gives me actual goosebumps!",
    "This beat is absolutely fire!",
    "The lyrics hit so different today!",
    "I can't stop replaying this track!",
    "That key change was everything!",
    "The production on this album is flawless!",
    "This song is criminally underrated!",
    "The harmony in this chorus is perfection!",
    "I've had this stuck in my head all week!",
    "This live version is even better than the studio!",
    "The bass on this track is ridiculous!",
    "That falsetto was absolutely stunning!",
    "This remix completely transforms the original!",
    "There's something about 'Dreams' by Fleetwood Mac that never gets old.",
    "When the beat drops on 'Sicko Mode,' the whole club loses their minds.",
    "I can't hear 'September' by Earth, Wind & Fire without dancing.",
    "Every time 'Mr. Brightside' comes on, everyone sings along.",
    "The guitar tone on 'Little Wing' by Jimi Hendrix is heavenly.",
    "'Clair de Lune' by Debussy makes me feel things I can't describe.",
    "When Nina Simone sings 'Feeling Good,' you believe every word.",
    "I saw Radiohead at Madison Square Garden and it was electric.",
    "Seeing Daft Punk's pyramid at Coachella 2006 changed everything.",
    "I'll die on this hill: Revolver is better than Sgt. Pepper's.",
    "Hot take: Yeezus is Kanye's most important album.",
    "Auto Tune is a legitimate artistic tool, not cheating.",
    "This song played at my wedding and now I can't hear it without crying.",
    "I discovered this album during the hardest year of my life.",
    "My dad used to play this in the car, and now he's gone.",
    "We had our first kiss while this song played.",
    "This was the last song my grandmother requested.",
    "Every time I hear this, I'm transported back to childhood.",
    "Streaming saved the music industry but destroyed artist compensation.",
    "Album sequencing is a lost art in the shuffle era.",
    # LONG PROMPTS (30-37 WORDS)
    (
        "Miles Davis reinvented himself multiple times throughout his long career, from bebop to cool jazz to fusion, "
        "always staying ahead of the curve and influencing generations of musicians who followed in his innovative "
        "footsteps."
    ),
    (
        "Joni Mitchell's Blue is considered one of the greatest albums ever recorded by critics and fans alike, with "
        "its confessional lyrics and innovative open tunings creating an intimacy that still feels revolutionary and "
        "deeply personal today."
    ),
    (
        "The way Pharrell Williams produces beats that sound simultaneously futuristic and nostalgic is a true "
        "testament to his deep understanding of rhythm, texture, and the emotional power of sound and groove in "
        "popular music."
    ),
    (
        "Aretha Franklin's legendary version of Respect transformed Otis Redding's original song into a powerful "
        "feminist anthem, her commanding vocal performance demanding attention and defining the cultural conversation "
        "of the entire civil rights era."
    ),
    (
        "David Bowie's constant artistic reinvention from Ziggy Stardust to the Thin White Duke to his Berlin trilogy "
        "showed an artist completely unwilling to rest on past successes or repeat himself in any way ever."
    ),
    (
        "Nina Simone's remarkable ability to blend classical training with jazz, blues, and soul created a unique "
        "voice that addressed civil rights with both beauty and righteous anger that still resonates powerfully today."
    ),
    (
        "The Beach Boys' Pet Sounds pushed studio production to unprecedented new heights, with Brian Wilson's layered "
        "arrangements inspiring The Beatles to create Sgt. Pepper's Lonely Hearts Club Band in direct response to it."
    ),
    (
        "Talking Heads merged punk energy with African rhythms and art school sensibilities, creating a sound that was "
        "simultaneously intellectual and irresistibly danceable on groundbreaking albums like Remain in Light and Fear "
        "of Music."
    ),
    (
        "Run DMC's historic collaboration with Aerosmith on Walk This Way broke down barriers between rock and hip "
        "hop, paving the way for future genre crossing collaborations and mainstream acceptance of rap music in "
        "America."
    ),
    (
        "Missy Elliott's innovative music videos and futuristic production with Timbaland redefined what was possible "
        "in hip hop, pushing both sonic and visual boundaries simultaneously throughout the late nineties and early "
        "two thousands era."
    ),
    (
        "Jeff Buckley's transcendent version of Hallelujah transformed Leonard Cohen's original song into something "
        "otherworldly, his voice conveying depths of emotion that have made it a modern standard performed at "
        "countless weddings and funerals."
    ),
    (
        "Fela Kuti invented Afrobeat by combining traditional Yoruba music with American jazz, funk, and highlife, "
        "creating politically charged music that challenged Nigerian government corruption and inspired generations of "
        "African musicians worldwide."
    ),
    (
        "Kate Bush's Hounds of Love demonstrated her visionary approach to production and songwriting, with the second "
        "side's conceptual suite showing her ambitious artistic vision and willingness to take creative risks that "
        "others wouldn't."
    ),
    (
        "Marvin Gaye's What's Going On broke from Motown's hit factory approach, addressing Vietnam, poverty, and "
        "ecology with a lush orchestral soul sound that changed what popular music could say and mean to audiences."
    ),
    (
        "The Cure's Disintegration balanced Robert Smith's melancholic lyrics with lush, layered production, creating "
        "a gothic masterpiece that remains their most beloved and influential album among fans and critics alike to "
        "this day."
    ),
    (
        "Ella Fitzgerald's Songbook series defined the American popular song canon for generations, her impeccable "
        "phrasing and scatting ability setting the standard for jazz vocal performance for generations of singers who "
        "followed her."
    ),
    (
        "Kraftwerk's electronic innovations in the seventies laid the groundwork for synth pop, techno, hip hop, and "
        "virtually every form of electronic music that followed their pioneering work with synthesizers and drum "
        "machines."
    ),
    (
        "Dolly Parton's songwriting genius is often overshadowed by her larger than life persona, but songs like "
        "Jolene and I Will Always Love You showcase her profound emotional intelligence and ability to craft timeless "
        "melodies."
    ),
    (
        "Curtis Mayfield's Superfly soundtrack elevated blaxploitation film music to high art, his socially conscious "
        "lyrics and lush arrangements creating a template for cinematic soul music that influenced countless film "
        "scores afterward."
    ),
    (
        "Tame Impala's Kevin Parker creates entire albums completely alone, layering psychedelic guitars, "
        "synthesizers, and drums into productions that sound both vintage and futuristic at once, a true one man "
        "studio genius."
    ),
    (
        "LCD Soundsystem's Sound of Silver captured the anxiety of aging in the indie rock scene perfectly, with "
        "tracks like All My Friends becoming generational anthems for millennials confronting mortality and nostalgia."
    ),
    (
        "Rihanna's ability to work with diverse producers from Calvin Harris to Diplo while maintaining her "
        "distinctive voice shows remarkable artistic flexibility and commercial instinct that made her a global "
        "superstar."
    ),
    (
        "The Weeknd's transition from mysterious mixtape artist to global pop star happened without sacrificing his "
        "dark, atmospheric production style or provocative lyrical content, proving authenticity and commercial "
        "success can coexist."
    ),
    (
        "Anderson .Paak's drumming and singing simultaneously while performing shows a level of musicianship that sets "
        "him apart in contemporary R&B and hip hop, his energy and skill unmatched on any stage."
    ),
    (
        "Solange's A Seat at the Table addressed Black identity and self care with a quiet intensity, her artistic "
        "vision distinct from her sister Beyoncé's maximalist approach yet equally powerful and meaningful."
    ),
    (
        "Japanese Breakfast's Michelle Zauner channels grief and joy through shimmering synth pop, her memoir Crying "
        "in H Mart revealing the personal depth behind her music and her journey through loss and healing."
    ),
    (
        "Blood Orange's Dev Hynes produces for everyone from Solange to Sky Ferreira while creating his own albums "
        "that blend eighties boogie with contemporary R&B sensibilities and experimental art pop sounds."
    ),
    (
        "Caroline Polachek's operatic vocal training combined with experimental pop production creates a sound that "
        "feels both classical and cutting edge, familiar yet entirely original in the current pop landscape today."
    ),
    (
        "When I first heard Radiohead's 'Kid A,' I didn't understand it at all, but after dozens of listens, it "
        "completely changed my understanding of what rock music could be and sound like."
    ),
    (
        "The way Beyoncé transformed from Destiny's Child member to global icon while constantly reinventing her sound "
        "and visual presentation shows an artist who refuses to rest on past achievements ever."
    ),
    (
        "I remember exactly where I was when I first heard 'Runaway' by Kanye West, that single piano note hitting "
        "like a revelation before the drums and strings came crashing in hard."
    ),
]

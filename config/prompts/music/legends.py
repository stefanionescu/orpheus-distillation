"""Music prompts about more artists, songs, and genres, the last third."""

from __future__ import annotations

LEGENDS: list[str] = [
    (
        "Stars of the Lid's drone ambient stretched time itself, their orchestral textures perfect for contemplation "
        "or falling asleep."
    ),
    (
        "William Basinski's 'Disintegration Loops' captured tape decay as elegy, their September eleventh context "
        "adding weight to already heavy music."
    ),
    (
        "Éliane Radigue's analog synthesizer drones require patience, her Buddhist practice informing compositions "
        "that unfold over hours."
    ),
    (
        "Pauline Oliveros' deep listening practice influenced generations of experimental musicians, her accordion "
        "drones meditative and transformative."
    ),
    (
        "Meredith Monk's extended vocal techniques predated Björk by decades, her compositions blending theater, "
        "dance, and avant garde music."
    ),
    (
        "Laurie Anderson's multimedia performances merged technology and storytelling, 'O Superman' an unlikely hit "
        "that introduced art rock to MTV."
    ),
    (
        "Diamanda Galás' operatic extremity addressed AIDS and genocide, her three octave range deployed in service of "
        "political fury."
    ),
    "Lydia Lunch's no wave confrontations with Teenage Jesus and the Jerks influenced noise rock's entire trajectory.",
    (
        "Yoko Ono's avant garde vocals predated punk's primal screams, her influence on John Lennon's experimental "
        "Beatles work often overlooked."
    ),
    "Nico's icy vocals on 'Chelsea Girl' and 'Marble Index' created gothic folk before the genre existed.",
    (
        "Joni Mitchell's 'Hejira' featured Jaco Pastorius' fretless bass, her jazz explorations confounding fans "
        "expecting folk confessionals."
    ),
    (
        "Carole King's 'Tapestry' sold millions while maintaining artistic integrity, her Brill Building songwriting "
        "translated to personal expression."
    ),
    (
        "Laura Nyro's baroque pop influenced everyone from Elton John to Todd Rundgren, her emotional intensity ahead "
        "of its time."
    ),
    (
        "Judee Sill's baroque folk incorporated Bach and mysticism, her two albums cult classics rediscovered by each "
        "generation."
    ),
    (
        "Vashti Bunyan's 'Just Another Diamond Day' flopped in nineteen seventy then influenced freak folk's twenty "
        "first century revival."
    ),
    (
        "Linda Perhacs' 'Parallelograms' mixed folk with electronic experimentation, her only album until a twenty "
        "fourteen comeback."
    ),
    (
        "Sibylle Baier's home recordings from the seventies surfaced decades later, her intimate folk finally finding "
        "its audience."
    ),
    (
        "Karen Dalton's weathered voice interpreted folk and blues standards, her heroin addiction cutting short a "
        "singular talent."
    ),
    (
        "Connie Converse's fifties recordings predated the folk revival, her disappearance in nineteen seventy four "
        "adding mystery to her legacy."
    ),
    (
        "Molly Drake's home recordings emerged after her son Nick's death, revealing the source of his melancholic "
        "sensibility."
    ),
    (
        "Nick Drake's three albums sold nothing in his lifetime, 'Pink Moon' now recognized as a masterpiece of "
        "intimate folk."
    ),
    "John Martyn's 'Solid Air' for Nick Drake featured Echoplex treated guitar that influenced The xx and Bon Iver.",
    (
        "Richard Thompson's guitar work with Fairport Convention and solo defined British folk rock's electric "
        "possibilities."
    ),
    (
        "Sandy Denny's voice graced Fairport Convention and Led Zeppelin's 'The Battle of Evermore,' her early death a "
        "tragedy."
    ),
    (
        "Bert Jansch's acoustic guitar influenced Jimmy Page and countless fingerstyle players, his Pentangle work "
        "blending folk and jazz."
    ),
    "John Fahey's American Primitive guitar created a genre, his Takoma Records nurturing Leo Kottke and Robbie Basho.",
    (
        "Robbie Basho's twelve string explorations drew from Indian classical music, his intensity unmatched in "
        "American fingerstyle guitar."
    ),
    "Leo Kottke's virtuoso twelve string playing earned him a cult following, his humor balancing technical precision.",
    (
        "Michael Hedges' two handed tapping techniques expanded acoustic guitar's possibilities, his Windham Hill "
        "recordings influential on new age."
    ),
    "Kaki King's percussive acoustic style earned her a spot on Rolling Stone's guitarist list, rare for a woman.",
    (
        "Marisa Anderson's instrumental Americana channels John Fahey through a Pacific Northwest lens, her guitar "
        "both delicate and powerful."
    ),
    (
        "William Tyler's instrumental country draws from Fahey and Nashville session work, his compositions cinematic "
        "without being soundtracks."
    ),
    (
        "Steve Gunn's psychedelic folk rock channels Fahey and Television, his guitar explorations never losing sight "
        "of songs."
    ),
    (
        "Ryley Walker's jazz folk channels John Martyn and Tim Buckley, his Chicago scene connections adding "
        "experimental edges."
    ),
    (
        "Gwenifer Raymond's Appalachian fingerpicking honors the tradition while pushing toward noise and drone "
        "territories."
    ),
    (
        "Yasmin Williams' lap tapping technique creates orchestral textures from solo acoustic guitar, her approach "
        "entirely her own."
    ),
    (
        "Mdou Moctar's Tuareg guitar brings Saharan traditions to rock audiences, his 'Afrique Victime' a crossover "
        "success."
    ),
    (
        "Bombino's desert blues earned him a Grammy nomination, his collaboration with Dan Auerbach introducing him to "
        "rock fans."
    ),
    (
        "Tinariwen's collective approach to Tuareg rock influenced countless Western artists seeking authentic global "
        "sounds."
    ),
    (
        "Songhoy Blues' Malian rock emerged from displacement, their Damon Albarn produced debut bringing Saharan "
        "sounds to festival stages."
    ),
    "Amadou and Mariam's Malian pop crossed over internationally, their blindness adding poignancy to joyful Afropop.",
    (
        "Oumou Sangaré's Wassoulou music addresses women's rights in Mali, her powerful voice matched by political "
        "conviction."
    ),
    (
        "Salif Keita's golden voice earned him the title of Africa's greatest singer, his albinism once a source of "
        "shame now pride."
    ),
    (
        "Youssou N'Dour's mbalax rhythms made him Senegal's biggest star, his 'Egypt' album winning a Grammy for world "
        "music."
    ),
    (
        "Baaba Maal's Senegalese music balances tradition and modernity, his collaborations with Brian Eno expanding "
        "his audience."
    ),
    "Orchestra Baobab's Senegalese Cuban fusion created some of West Africa's most sophisticated pop music.",
    (
        "Femi Kuti carries his father Fela's Afrobeat legacy while addressing contemporary Nigerian politics with his "
        "own voice."
    ),
    "Seun Kuti leads Egypt 80, his father Fela's band, keeping Afrobeat's political fire burning for new generations.",
    (
        "Tony Allen's drumming defined Afrobeat's rhythm, his solo work and collaborations with Damon Albarn extending "
        "his influence."
    ),
    "Antibalas' Brooklyn Afrobeat kept the flame burning in America, their horn section rivaling any Lagos ensemble.",
    "Budos Band's instrumental Afro soul from Staten Island soundtracked countless film trailers and television shows.",
    "Menahan Street Band's soul instrumentals provided samples for hip hop while standing alone as sophisticated funk.",
    (
        "Sharon Jones and the Dap Kings revived classic soul, her powerful voice and the band's Daptone productions "
        "influencing Amy Winehouse."
    ),
    (
        "Charles Bradley's late career soul success proved it's never too late, his screaming eagle persona earned "
        "through decades of struggle."
    ),
    "Lee Fields' fifty year career saw him finally recognized as a soul legend, his voice weathered but powerful.",
    "Curtis Harding's soul rock blend earned comparisons to Sly Stone, his Atlanta roots adding Southern grit.",
    (
        "Michael Kiwanuka's orchestral soul earned Mercury Prize recognition, his 'Black Man in a White World' "
        "addressing identity."
    ),
    (
        "Celeste's voice earned her a Brit Award before her debut album, her Bond theme continuing a tradition of "
        "powerful singers."
    ),
    (
        "Cleo Sol's neo soul earned her a devoted following, her collaborations with Inflo's SAULT project equally "
        "acclaimed."
    ),
    (
        "SAULT's anonymous collective released multiple albums during the pandemic, their political soul addressing "
        "Black Lives Matter."
    ),
    "Gabriels' orchestral soul emerged from a chance meeting, Jacob Lusk's voice earning comparisons to Marvin Gaye.",
    (
        "Yola's country soul earned her Grammy nominations and a star turn in 'Elvis,' her voice crossing genre "
        "boundaries."
    ),
    "Brittany Howard's solo work extended Alabama Shakes' soul rock into more experimental territory.",
    "Leon Bridges' throwback soul updated the genre for streaming playlists without losing its emotional core.",
    "Anderson East's blue eyed soul earned him Nashville credibility, his voice raw and powerful.",
    "Durand Jones and the Indications' vintage soul captured the Daptone aesthetic for a new generation.",
    (
        "The Frightnrs' rocksteady revived Jamaican rhythms, Dan Klein's death before their album's release adding "
        "tragedy."
    ),
    "Protoje's reggae revival earned him crossover success, his 'Ancient Future' album balancing roots and modernity.",
    "Chronixx's conscious reggae addressed Jamaican politics while earning international festival slots.",
    "Koffee's Grammy win made her the youngest reggae winner, her positivity refreshing in a sometimes heavy genre.",
    "Popcaan's dancehall earned Drake collaborations, his 'Unruly' brand extending beyond music into lifestyle.",
    "Vybz Kartel's influence persists despite his imprisonment, his productions and protégés dominating dancehall.",
    "Shenseea's dancehall pop crossover earned her a Kanye West feature, her ambition matching her talent.",
    "Skillibeng's 'Crocodile Teeth' went viral, his aggressive dancehall style earning international attention.",
    "Spice's dancehall feminism challenged the genre's male dominance, her 'So Mi Like It' an anthem.",
]

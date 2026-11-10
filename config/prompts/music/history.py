"""Music prompts of thirty to thirty-seven words about artists, albums, and music history."""

from __future__ import annotations

HISTORY: list[str] = [
    (
        "James Brown's 'The One' concept—emphasizing the first beat of every measure—fundamentally changed how rhythm "
        "works in popular music, influencing funk, hip hop, and electronic dance music globally forever."
    ),
    (
        "Joni Mitchell's use of open tunings on 'Blue' allowed her to create chord voicings impossible in standard "
        "tuning, giving the album its distinctive harmonic color and emotional depth throughout."
    ),
    (
        "The Notorious B.I.G.'s storytelling ability on 'Ready to Die' combined street narratives with cinematic "
        "detail, his flow adapting to each track's mood with remarkable versatility and natural charisma."
    ),
    (
        "Björk's 'Homogenic' merged Icelandic string arrangements with glitchy electronic beats, creating a template "
        "for art pop that artists like FKA twigs and Arca would later expand upon significantly."
    ),
    (
        "The way J Dilla programmed drums with intentional imperfection on 'Donuts' humanized electronic music, his "
        "influence audible in virtually every hip hop and R&B production that came after him."
    ),
    (
        "Sly and the Family Stone's integration of rock, soul, funk, and psychedelia on 'There's a Riot Goin' On' "
        "created a dark masterpiece that influenced everyone from Prince to D'Angelo."
    ),
    (
        "The Clash's 'London Calling' proved punk could be musically ambitious without losing its political edge, "
        "incorporating reggae, jazz, and rockabilly into a sprawling double album statement of intent."
    ),
    (
        "Aphex Twin's 'Selected Ambient Works 85 92' created a template for ambient electronic music that still sounds "
        "futuristic, its influence spanning from Boards of Canada to modern lo fi producers today."
    ),
    (
        "Public Enemy's 'It Takes a Nation of Millions to Hold Us Back' combined dense sample collages with Chuck D's "
        "political lyrics, creating hip hop's most sonically radical and influential statement."
    ),
    (
        "Why do you think vinyl records have made such a strong comeback when streaming offers unlimited access to "
        "virtually every song ever recorded at the touch of a button today?"
    ),
    (
        "How did sampling transform hip hop production, and what are the ethical implications of building new art from "
        "pieces of existing recordings without always crediting the original artists properly and fairly?"
    ),
    (
        "What makes certain albums feel like complete artistic statements while others feel like collections of "
        "singles, and does the distinction even matter in the streaming era anymore to listeners?"
    ),
    (
        "Why do some artists like Radiohead and Kendrick Lamar receive critical acclaim while also achieving "
        "commercial success, when those two things often seem mutually exclusive in music today?"
    ),
    (
        "How has the decline of the major label system affected the kind of music that gets made and promoted, and has "
        "independence been good for artistic creativity overall in music?"
    ),
    (
        "What responsibility do artists have to address social and political issues in their music, and can pop songs "
        "actually change hearts and minds or just reflect existing attitudes?"
    ),
    (
        "Why do certain songs become wedding standards while others become funeral staples, and what makes music "
        "appropriate for life's most significant moments and ceremonies we all experience together?"
    ),
    (
        "How do you think artificial intelligence will change music creation, and will AI generated songs ever be able "
        "to capture the human emotion that makes music meaningful to us?"
    ),
    (
        "What makes a cover version successful, and why do some covers like Jeff Buckley's Hallelujah or Johnny Cash's "
        "Hurt transcend the originals in cultural significance and emotional impact?"
    ),
    (
        "Why do we form such strong attachments to the music we discover during adolescence, and does the music "
        "actually sound better or is it purely nostalgic association playing tricks?"
    ),
    (
        "How has the algorithm driven discovery of streaming platforms changed the way we find new music, and are we "
        "losing something by not browsing record store shelves anymore today?"
    ),
    (
        "What separates a technically proficient musician from a truly great artist, and why do some untrained singers "
        "move us more than classically trained vocalists with perfect technique always?"
    ),
    (
        "How do you think the pandemic changed music, both in terms of how it's created and how we experience it as "
        "listeners seeking connection during isolation and uncertainty?"
    ),
    (
        "Why does live music feel so different from recorded music, and what is it about sharing physical space with "
        "performers and other fans that creates that irreplaceable magic?"
    ),
    (
        "What makes certain genres feel timeless while others become dated, and why does seventies funk still sound "
        "fresh while some eighties production sounds trapped in its era?"
    ),
    (
        "Do you think the Beatles or the Rolling Stones had more influence on rock music, or is that debate missing "
        "the point since they pushed each other to greatness?"
    ),
    (
        "How do you discover new music in the streaming era, through algorithmic recommendations, friend suggestions, "
        "music publications, or just random exploration of related artists and curated playlists online?"
    ),
    (
        "What makes you connect emotionally with certain songs while others leave you cold, even when they're "
        "technically well crafted and critically acclaimed by experts and fellow music lovers alike?"
    ),
    (
        "Do you think music was better in a particular decade, or does nostalgia color our perception of the past "
        "while we overlook the great music being made now?"
    ),
    (
        "How has your music taste evolved over time, and are there artists you dismissed when younger that you've come "
        "to appreciate with age, experience, and changed perspective now?"
    ),
    (
        "I cannot believe how perfectly Quincy Jones produced Off the Wall, every single track is a masterpiece and "
        "Michael Jackson's vocals are absolutely flawless throughout the entire album!"
    ),
    (
        "The way Kendrick Lamar weaves together narrative threads across entire albums while still making each song "
        "work individually is something I've never seen any other rapper accomplish before!"
    ),
    (
        "This Dilla beat is so ahead of its time that producers are still trying to figure out how he made drums swing "
        "like that almost twenty years later today!"
    ),
    (
        "I've listened to In Rainbows hundreds of times and I still discover new details in the production, "
        "Radiohead's attention to sonic texture is absolutely unparalleled in rock music!"
    ),
    (
        "The fact that Prince played every single instrument on his first album when he was only nineteen years old "
        "still blows my mind every time I think about it!"
    ),
    (
        "Beyoncé's Coachella performance was the greatest live show I've ever witnessed, the choreography, the band, "
        "the Destiny's Child reunion, everything was executed with absolute perfection and precision!"
    ),
    (
        "I can't stop listening to this Burial track, the way he chops up vocal samples and buries them in crackle and "
        "static creates such a haunting atmosphere throughout!"
    ),
    (
        "The string arrangement on Eleanor Rigby was revolutionary for pop music, George Martin's production elevated "
        "The Beatles from a great band to genuine artistic innovators in music!"
    ),
    (
        "This Frank Ocean album has so many layers that I hear something completely new every single time I put on my "
        "headphones and really focus on the details!"
    ),
    (
        "I'm absolutely obsessed with how Rosalía blends flamenco traditions with modern production, she's creating "
        "something entirely new while honoring centuries of Spanish musical heritage and tradition beautifully!"
    ),
    (
        "The way Thundercat's bass playing combines jazz virtuosity with funk grooves and weird humor is unlike "
        "anything else in contemporary music, he's truly in a league of his own!"
    ),
    (
        "I still get emotional every time I hear the climax of A Day in the Life, that orchestral crescendo followed "
        "by the final chord is pure musical genius!"
    ),
    (
        "This Charli XCX album pushed hyperpop to its absolute limits, the production is so aggressive and futuristic "
        "that it makes everything else sound dated by comparison today!"
    ),
    (
        "I cannot believe how good this live Snarky Puppy performance is, the way they build grooves together and "
        "respond to each other in real time is absolutely incredible!"
    ),
    (
        "The fact that Joni Mitchell wrote Both Sides Now at twenty three and then re recorded it at fifty seven with "
        "completely different meaning shows the depth of her artistic vision!"
    ),
    (
        "I cannot believe how hard this 808 hits on the new Travis Scott track, the bass is so deep it feels like my "
        "chest is vibrating with every beat!"
    ),
    (
        "The way Beyoncé commands the stage during her live performances is absolutely unmatched, every movement "
        "precise, every note perfect, every moment designed to create maximum impact on audiences!"
    ),
    (
        "I've been listening to this Tame Impala album on repeat for three weeks straight and I still can't get over "
        "how perfectly the production captures that psychedelic feeling!"
    ),
    (
        "The guitar tone on this John Mayer live recording is absolutely gorgeous, you can hear every nuance of his "
        "playing and the way he bends notes is pure emotion!"
    ),
    (
        "I just discovered this obscure jazz album from nineteen sixty seven and I can't believe it's not more famous, "
        "the playing is absolutely incredible from first note to last!"
    ),
    (
        "The way the strings come in on this Sufjan Stevens song literally makes me cry every single time, the "
        "arrangement is so beautiful it physically affects my heart!"
    ),
    (
        "I saw this band in a tiny club before they got famous and I knew immediately they were going to be huge, the "
        "energy in that room was electric!"
    ),
    (
        "The production on this Pharrell beat is so clean and funky that I've listened to it maybe five hundred times "
        "and I still notice new details every play!"
    ),
    (
        "I can't get over how good this live version of 'Comfortably Numb' is, David Gilmour's guitar solo at the end "
        "is one of the greatest moments in rock!"
    ),
    (
        "The way Anderson .Paak plays drums while singing with that much soul and energy should be physically "
        "impossible, but he does it effortlessly and makes it look easy!"
    ),
    (
        "I just heard this underground rapper for the first time and their flow is absolutely insane, switching "
        "between double time and half time like it's nothing, pure technical mastery!"
    ),
    (
        "The harmonies on this Fleet Foxes song are so angelic and layered that I feel like I'm floating when I "
        "listen, it's the most beautiful thing I've heard!"
    ),
    (
        "I cannot stop listening to this new Rosalía album, the way she blends flamenco traditions with modern "
        "production is unlike anything else in contemporary music right now today!"
    ),
    (
        "The drop on this Skrillex track still hits as hard as it did when I first heard it, absolutely revolutionary "
        "production that changed electronic music forever and completely!"
    ),
    (
        "I've been obsessed with this Fiona Apple album since it came out and every listen reveals new layers of "
        "meaning in her lyrics and new textures in production!"
    ),
]

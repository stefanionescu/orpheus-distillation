"""Multi-sentence prompts: mixed conversation."""

from __future__ import annotations

CONVERSATIONS: list[str] = [
    (
        "The weather app says partly cloudy but I see only gray expanse. Our definitions of partly clearly differ "
        "significantly today."
    ),
    (
        "The deadline that seemed far away is suddenly uncomfortably close now. Time compression happens most "
        "aggressively when least convenient."
    ),
    (
        "The coffee maker is making sounds it definitely didn't make before recently. Adding appliance replacement to "
        "the growing to do list."
    ),
    (
        "The alarm I set for the wrong time zone cost me a meeting. International scheduling remains my personal "
        "nemesis consistently."
    ),
    (
        "The outfit I planned doesn't match as well in daylight as it did inside. Too late to change now so confidence "
        "it is."
    ),
    (
        "The conversation I overheard wasn't meant for my ears clearly. Now I possess awkward knowledge I can never "
        "acknowledge publicly."
    ),
    "The song stuck in my head has been there for three days solid. I don't even like it which makes this worse.",
    (
        "The homework assignment my child forgot about is due tomorrow morning. The family scramble to complete it "
        "begins now urgently."
    ),
    (
        "The text I sent to the wrong person created unnecessary drama instantly. Double checking recipients should "
        "really be automatic for me."
    ),
    (
        "The printer decided today was the day to finally rebel completely. Of course this happens when I actually "
        "need something printed."
    ),
    (
        "The recipe called for an ingredient I've never heard of before. Substitutions were made with questionable "
        "confidence in the outcome."
    ),
    (
        "The chair I've sat in daily for years finally broke dramatically. My dignity suffered more than any physical "
        "injury thankfully."
    ),
    (
        "The phone battery died at the exact moment I needed directions. The universe has interesting timing with "
        "these inconveniences."
    ),
    (
        "The stain on my shirt appeared from nowhere after I left home. Visible enough to notice, impossible to "
        "explain the origin."
    ),
    "The WiFi password posted on the wall doesn't actually work correctly. Staff seems as confused about this as I am.",
    (
        "The escalator being broken turned stairs into an inconvenient surprise. First world problems but still "
        "annoying when unexpected completely."
    ),
    (
        "The door that's always locked was mysteriously open when I tried it. Small victories in navigating familiar "
        "spaces differently."
    ),
    (
        "The headphones I packed apparently belong to a different device entirely. Silence for this journey wasn't in "
        "my plan today."
    ),
    (
        "The snack I was looking forward to all day was gone when I reached for it. Someone in this house has "
        "explanations to provide."
    ),
    (
        "The sunset was spectacular but my camera couldn't capture the colors right. Some beauty exists only in the "
        "moment itself."
    ),
    (
        "The stranger who smiled at me genuinely improved my entire afternoon significantly. Human connection in small "
        "doses still matters greatly."
    ),
    (
        "The old photograph I found while cleaning brought back memories vividly. Younger versions of ourselves seem "
        "like different people almost."
    ),
    (
        "The handwritten letter from years ago still carries emotional weight somehow. Words on paper feel more "
        "permanent than digital ones."
    ),
    (
        "The vintage store find fits perfectly against all statistical probability somehow. Fashion luck is real and "
        "today it favored me."
    ),
    (
        "The childhood toy I found in storage still triggers specific memories instantly. Objects hold time in ways we "
        "don't fully appreciate."
    ),
    (
        "The playlist from that summer brings back feelings I thought I'd processed. Music stores emotion more "
        "reliably than memory does."
    ),
    (
        "The perfume she used to wear transported me across decades instantly. Scent memory bypasses conscious thought "
        "entirely and directly."
    ),
    (
        "The house we drove past was where I had my first kiss actually. Places hold stories that only certain people "
        "know."
    ),
    (
        "The teacher's comments on my old report card made me laugh. Their observations remain accurate decades later "
        "unfortunately."
    ),
    (
        "The recipe my grandmother wrote in her handwriting is irreplaceable now. Family history in ingredient lists "
        "and temperatures preserved."
    ),
    (
        "The voicemail I saved from before they passed still brings comfort sometimes. Technology preserves voices we "
        "can no longer hear otherwise."
    ),
    (
        "The award I received in childhood still sits on my parents' shelf proudly. Their belief in me predates my own "
        "self belief."
    ),
    (
        "The jersey from my playing days doesn't fit anymore obviously. Bodies change but memories of who we were "
        "persist regardless."
    ),
    (
        "The map I used before smartphones existed seems charmingly antiquated now. Navigation used to require actual "
        "skill and attention."
    ),
    (
        "The camera from my first trip abroad was film not digital. Waiting for photos to develop built anticipation "
        "we've lost."
    ),
    (
        "The diary I kept as a teenager is simultaneously cringeworthy and precious. Past selves deserve compassion "
        "for their earnest attempts."
    ),
    (
        "The cassette tape with the mix someone made me still exists somewhere. Physical music gifts meant something "
        "different then."
    ),
    (
        "The textbook I kept has marginalia from a more diligent version of myself. Evidence that I once took notes "
        "seriously."
    ),
    (
        "The poster on my childhood bedroom wall reflected who I wanted to become. Some aspirations we outgrow; others "
        "we achieve differently."
    ),
    (
        "The birthday card signed by people no longer in my life holds complicated feelings. Relationships end but "
        "artifacts remain."
    ),
    (
        "The newspaper from an important historical date sits in a drawer still. We thought preserving the moment "
        "mattered then."
    ),
    (
        "The shoes I wore to that interview still remind me of nervous energy. Objects absorb the emotional residue of "
        "significant moments."
    ),
    (
        "The book my father gave me before college has his inscription inside. His handwriting is something I can "
        "still touch."
    ),
    "The shell I collected from that beach vacation sits on my windowsill. A small piece of a place I loved.",
    "The ticket stub from the concert I went to alone marks a turning point. Some experiences change us in solitude.",
    (
        "The mug from the place that closed down is the only evidence it existed. Businesses disappear but their "
        "merchandise survives."
    ),
    (
        "The keychain from a trip I barely remember holds more nostalgia than photos. Small objects trigger bigger "
        "memories unexpectedly."
    ),
    (
        "The blanket that's falling apart still provides comfort nothing else matches. Replacement isn't the same as "
        "the original somehow."
    ),
    (
        "The clock that stopped working still hangs on the wall for sentimental reasons. Function matters less than "
        "feeling sometimes."
    ),
    (
        "The plant cutting from my grandmother's garden survived the cross country move miraculously. Living things "
        "connect generations across distance."
    ),
    (
        "The street I grew up on looks smaller every time I visit now. Childhood perception scaled everything "
        "differently than adult eyes."
    ),
    (
        "The bench where we used to sit after school is still there surprisingly. Some things persist while we change "
        "around them."
    ),
    (
        "The library where I spent countless hours has been renovated beyond recognition now. Progress sometimes feels "
        "like loss to those who remember."
    ),
    (
        "The corner store that knew my name closed years ago permanently. Neighborhood relationships disappear when "
        "businesses change ownership."
    ),
    (
        "The playground equipment I thought was enormous is actually quite small. Memory distorts scale in predictable "
        "but still surprising ways."
    ),
    (
        "The tree I climbed as a child was cut down for development recently. Physical landmarks of personal history "
        "can vanish abruptly."
    ),
    (
        "The restaurant where we celebrated every milestone changed owners and menus completely. Traditions require "
        "places that cooperate with our sentimentality."
    ),
    (
        "The walking path I used daily became unrecognizable after construction nearby. Routes we thought permanent "
        "turn out to be temporary."
    ),
    (
        "The neighbors who watched me grow up have all moved away now. Communities transform while our memories of "
        "them remain static."
    ),
    (
        "The house number is the same but nothing else about the block matches memory. Time edits places without "
        "asking our permission."
    ),
    (
        "The school I attended merged with another and lost its original name entirely. Institutional identity changes "
        "affect personal history strangely."
    ),
    (
        "The field where we played is now a parking structure unfortunately. Open spaces become premium real estate "
        "eventually everywhere."
    ),
    (
        "The view from my old bedroom window is blocked by new construction now. Perspectives we took for granted "
        "become inaccessible."
    ),
    (
        "The sound of trains at night used to lull me to sleep there. Environmental soundscapes become part of "
        "personal history."
    ),
    (
        "The route I walked to school included landmarks that no longer exist. Mental maps require constant updating "
        "as cities evolve."
    ),
    (
        "The coffee shop where I wrote my first manuscript closed during the pandemic. Creative spaces hold "
        "significance beyond their function."
    ),
    (
        "The intersection where I had my first accident still makes me anxious. Locations absorb emotional experiences "
        "and retain them."
    ),
    (
        "The hospital where I was born is now luxury condominiums instead. Birth and death become real estate "
        "eventually it seems."
    ),
    (
        "The church where my parents married looks exactly the same decades later. Some institutions resist change "
        "more successfully than others."
    ),
    (
        "The bridge I crossed daily for years was finally replaced with something modern. Functional improvements "
        "don't always feel like improvements."
    ),
    (
        "The movie theater with the sticky floors and terrible sound had personality though. Chain replacements lack "
        "character and history completely."
    ),
    (
        "The arcade that consumed my quarters no longer exists anywhere nearby. Childhood entertainment becomes "
        "nostalgic faster than we expect."
    ),
    (
        "The museum I found boring as a child fascinates my adult self now. Appreciation develops with experience and "
        "patience apparently."
    ),
]

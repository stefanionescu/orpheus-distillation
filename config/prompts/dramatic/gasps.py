"""Dramatic prompts: short gasps, accusations, and revelations, then medium scenes and long monologues."""

from __future__ import annotations

GASPS: list[str] = [
    # ULTRA SHORT - GASPS & EXCLAMATIONS
    "No! It cannot be!",
    "This is impossible!",
    "My heart! It breaks!",
    "Betrayal! Pure betrayal!",
    "I am devastated!",
    "Everything is ruined!",
    "The horror! The agony!",
    "I cannot breathe!",
    "My world crumbles!",
    "This changes everything!",
    "You monster!",
    "I am destroyed!",
    "Unforgivable! Absolutely unforgivable!",
    "The pain! Oh, the pain!",
    "My life is over!",
    "The tragedy! Oh, the tragedy!",
    "I shall never recover!",
    "You fiend!",
    # ULTRA SHORT - DRAMATIC REACTIONS
    "I'm going to faint!",
    "Hold me, I'm collapsing!",
    "I need air!",
    "My heart stopped!",
    "I cannot go on!",
    "Everything spins!",
    "I'm seeing stars!",
    "My knees buckle!",
    "I'm trembling uncontrollably!",
    "I can't feel my face!",
    "The room is spinning!",
    "I might die!",
    "I'm hyperventilating!",
    "My soul is shattered!",
    "I'm about to scream!",
    # ULTRA SHORT - ACCUSATIONS & CONFRONTATIONS
    "You lied to me!",
    "How could you?!",
    "You've destroyed everything!",
    "This is your fault!",
    "You betrayed my trust!",
    "You're a snake!",
    "You disgust me!",
    "I despise you!",
    "You vile creature!",
    "You heartless wretch!",
    "You absolute villain!",
    "I curse the day!",
    "You'll pay for this!",
    "Vengeance will be mine!",
    "You're dead to me!",
    # SHORT - BETRAYAL & HEARTBREAK
    "You've ripped my heart from my chest and stomped on it!",
    "I gave you everything, and you threw it away like garbage!",
    "The knife in my back has your fingerprints all over it!",
    "You've shattered every dream I ever dared to dream!",
    "My heart lies in a million pieces at your feet!",
    "You've turned my world into ashes and dust!",
    "I trusted you with my soul, and you crushed it!",
    "The betrayal cuts deeper than any blade ever could!",
    "You've poisoned every beautiful memory we ever shared!",
    "My love for you was pure, and you tainted it!",
    "You've broken me in ways I never knew were possible!",
    "The tears I've cried could fill an entire ocean!",
    "You trampled on my heart like it meant nothing!",
    "I opened my soul to you and you set it on fire!",
    "You've destroyed the very essence of who I am!",
    # SHORT - REVELATIONS & SECRETS
    "I know your terrible secret, and it changes everything!",
    "The truth has finally come to light after all these years!",
    "Your lies are unraveling like a cheap sweater in a hurricane!",
    "I've discovered something that will rock this family to its core!",
    "The skeleton in your closet has finally escaped!",
    "Your web of deception is crumbling before my very eyes!",
    "The mask has fallen and I see your true hideous face!",
    "Everything I believed was a carefully constructed lie!",
    "The shocking truth has been revealed at last, you monster!",
    "Your dark past has finally caught up with you!",
    "I found the evidence that exposes your treachery completely!",
    "The secret you've been hiding is destroying us all!",
    "Your facade of innocence has crumbled into dust!",
    "The truth is more horrifying than I ever imagined possible!",
    "I've uncovered the conspiracy that threatens to destroy everything!",
    # SHORT - EXAGGERATED MINOR PROBLEMS
    "The coffee is cold! My entire morning is absolutely ruined!",
    "They're out of my favorite yogurt! This is a catastrophe!",
    "My phone died! How will I survive this nightmare?!",
    "There's traffic! My life is spiraling into chaos!",
    "The WiFi is slow! I'm living in the dark ages!",
    "My shoelace broke! Why does the universe hate me?!",
    "It's raining! My existence is awash in misery!",
    "The elevator is broken! I must climb stairs like a peasant!",
    "My hair won't cooperate! I look like an absolute monster!",
    "They canceled my favorite show! My reason for living is gone!",
    "The line is so long! I'll grow old and die waiting!",
    "My sandwich has too much mayo! This is unacceptable torture!",
    "I got a paper cut! I'm literally bleeding to death!",
    "Someone took my parking spot! This is war!",
    "My pen ran out of ink! How am I supposed to function?!",
    # SHORT - DECLARATIONS & ULTIMATUMS
    "I will never, ever, ever forgive you for this!",
    "If you walk out that door, you're dead to me forever!",
    "I swear on my mother's grave, you will regret this!",
    "Choose right now: it's either me or them, forever!",
    "This is the end of everything we ever had together!",
    "I am drawing a line in the sand that cannot be crossed!",
    "Mark my words, karma will find you and destroy you!",
    "You have made a powerful enemy this day!",
    "I will make sure everyone knows exactly what you are!",
    "From this moment forward, we are strangers, nothing more!",
    "You've forced my hand, and now you'll face the consequences!",
    "I wash my hands of you and your wretched existence!",
    "This betrayal has sealed your fate permanently!",
    "Consider yourself erased from my life completely!",
    "You've just made the biggest mistake of your miserable life!",
    # MEDIUM - SOAP OPERA SCENARIOS
    "After twenty years, I discover that my twin sister has been living my life while I rotted away!",
    "You mean to tell me that my husband is actually my long lost brother? This cannot be happening!",
    "I faked my own death to escape your cruelty, and now I've returned for my revenge!",
    "The baby isn't yours! It belongs to your best friend, who I've been seeing behind your back!",
    "I've lost my memory, and everyone I trusted is lying to me about who I really am!",
    "My inheritance has been stolen by that scheming gold digger who seduced my dying father in his final days!",
    "The DNA test proves everything! You are not the person you've been pretending to be all along!",
    "I watched you die in that fire, yet here you stand before me as if nothing happened!",
    "Your new wife is actually my daughter who was kidnapped at birth by your evil mother!",
    (
        "The company is bankrupt because your secret gambling addiction has destroyed everything our family built for "
        "generations!"
    ),
    "I've been poisoning your tea for months while you suspected nothing, you foolish, trusting creature!",
    "The man you married is a wanted criminal with three other families he's been hiding from you!",
    "Your precious son is actually mine, switched at birth by the jealous nurse who loved your husband!",
    "I've come back from the dead to claim what is rightfully mine and to destroy everyone who wronged me!",
    "The wedding is off because I just discovered the groom has been having an affair with my mother!",
    # MEDIUM - EMOTIONAL BREAKDOWNS
    "I am literally falling apart at the seams! My entire being is unraveling like a frayed tapestry of despair!",
    "Every fiber of my existence screams in agony! The pain is absolutely unbearable and consuming my very soul!",
    "I cannot eat, I cannot sleep, I cannot breathe! You have destroyed my ability to function as human!",
    "My heart has been reduced to rubble and ashes! There is nothing left of me but hollow suffering!",
    "I am drowning in an endless ocean of sorrow! The waves of grief are pulling me under completely!",
    "The darkness consumes me entirely! I am lost in an abyss of despair with no hope of escape!",
    "I feel like I've been hit by a train, a bus, and lightning simultaneously! The devastation is complete!",
    "My soul has been ripped from my body! I am just an empty shell wandering through this cruel existence!",
    "The tears won't stop flowing! I've cried rivers, lakes, entire seas of salty, bitter tears of anguish!",
    "I am shattered into a billion irreparable pieces! No amount of glue could ever put me back together!",
    "My sanity hangs by the thinnest thread! One more tragedy and I will spiral into complete and utter madness!",
    "The weight of this betrayal is crushing my chest! I cannot draw breath through the suffocating pain!",
    "I have aged a thousand years from this heartbreak! My youth and vitality have withered and died completely!",
    "Every nerve ending screams with torment! My body cannot contain the magnitude of this emotional destruction!",
    "I am but a ghost of my former self! You have murdered the person I used to be!",
    # MEDIUM - QUESTIONS
    "How could you look me in the eyes every single day while hiding such a monstrous secret from me?!",
    "Do you have any idea what you've done to this family with your lies and your selfish betrayal?!",
    "After everything I sacrificed for you, this is how you repay me?! With treachery and deceit?!",
    "Who are you?! Because the person I loved would never, ever be capable of such cruelty!",
    "Did you ever truly love me, or was our entire relationship just an elaborate, heartless performance?!",
    "How am I supposed to go on living knowing that everything I believed was a complete lie?!",
    "What kind of monster destroys someone's entire world without even a shred of remorse or guilt?!",
    "Were you laughing at me behind my back this entire time while I trusted you blindly?!",
    "Is there no limit to your depravity?! How deep does your wickedness actually go?!",
    "Do you expect me to simply forgive and forget after you've committed the ultimate betrayal against me?!",
    # MEDIUM - EXCLAMATIONS
    "I would rather die a thousand deaths than spend one more moment breathing the same air as you!",
    "The audacity! The sheer, unmitigated gall to stand there and pretend you've done nothing wrong!",
    "This is the absolute worst day of my entire existence! Nothing will ever be this catastrophic again!",
    "I am shocked! Appalled! Disgusted beyond all measure by your despicable, unforgivable actions!",
    "The scandal! The shame! Our family name has been dragged through mud and filth by your behavior!",
    "I have been stabbed in the heart by the one person I trusted more than anyone in this world!",
    "This is madness! Pure, unadulterated insanity! Nothing about this situation makes any sense whatsoever!",
    "You have unleashed forces that you cannot possibly comprehend or control! Chaos will follow in your wake!",
    "I am seething with a rage so powerful it could burn this entire building to the ground!",
    "The nerve! The absolute audacity to betray me and then have the gall to ask for forgiveness!",
    # LONG - BETRAYAL MONOLOGUES
    (
        "You stood before me at the altar and promised to love me forever, and every single word that came out of your "
        "lying mouth was pure poison!"
    ),
    (
        "I defended you when everyone said you were no good, I believed in you when the whole world turned against "
        "you, and this is how you repay my loyalty!"
    ),
    (
        "Twenty years! Twenty years I gave you, the best years of my life, and you threw them away like yesterday's "
        "garbage for that thing you call love!"
    ),
    (
        "I would have walked through fire for you, I would have moved mountains, I would have given you my last "
        "breath, and you couldn't even give me honesty!"
    ),
    (
        "The knife you've plunged into my back goes so deep I can feel it piercing my very soul, and you twist it with "
        "every lie you continue to tell!"
    ),
    (
        "You've taken everything from me: my trust, my love, my dignity, my faith in humanity itself, and you dare to "
        "stand there looking innocent and confused!"
    ),
    (
        "I built my entire world around you, every dream I had included you in it, and you've demolished that world "
        "with a wrecking ball of betrayal!"
    ),
    (
        "The day I met you was the beginning of my downfall, and I was too blind, too foolish, too desperately in love "
        "to see the destruction coming!"
    ),
    (
        "You smiled at me while plotting my destruction, you held me while planning your escape, you whispered sweet "
        "lies while your heart belonged to another!"
    ),
    (
        "My mother warned me about people like you, but I was young and naive and so desperately wanted to believe "
        "that true love could conquer all!"
    ),
    (
        "I've spent countless sleepless nights wondering where I went wrong, what I could have done differently, when "
        "the truth is you were the problem all along!"
    ),
    (
        "You've turned me into someone I don't recognize anymore, a bitter, broken shell of the trusting, loving "
        "person I used to be before you destroyed me!"
    ),
    (
        "Every time I close my eyes, I see your face and the lies that dripped from your tongue like honey coated "
        "venom designed to poison my soul!"
    ),
    (
        "I gave you access to the most vulnerable parts of my heart, and you used that access to systematically tear "
        "me apart from the inside out!"
    ),
    (
        "The trust I placed in you was sacred, a precious gift that took me years to build, and you shattered it in a "
        "single moment of selfish betrayal!"
    ),
    # LONG - REVELATION DRAMA
    (
        "For fifteen years I've lived a lie, believing I was a simple orphan, when in reality I am the heir to an "
        "empire stolen by treacherous relatives!"
    ),
    (
        "The man I called father for my entire life isn't my father at all! My real father is the gardener who was "
        "banished when I was born!"
    ),
    (
        "I've discovered documents proving that our entire family fortune was built on fraud, deception, and the "
        "systematic destruction of innocent people who trusted us!"
    ),
    (
        "The woman in that photograph isn't just some random stranger, she's my mother, who everyone told me died in "
        "childbirth but was actually sent away in disgrace!"
    ),
    (
        "Your precious grandmother, the matriarch everyone worships, orchestrated the murder of my family and stole "
        "our birthright, and I have the proof right here in my hands!"
    ),
    (
        "I found the letters hidden in the attic, decades of correspondence revealing an affair so scandalous it would "
        "destroy every family member's reputation if it came to light!"
    ),
    (
        "The fire that killed my parents wasn't an accident! It was arson, committed by someone in this very room who "
        "is smiling at me right now!"
    ),
    (
        "Your sister isn't dead! She's been locked away in a mental institution for thirty years because she "
        "discovered a secret that could bring down the entire family!"
    ),
    (
        "I've been living under an assumed identity, hiding from the people who destroyed my life, and now I've "
        "returned to claim my vengeance on everyone who wronged me!"
    ),
    (
        "The DNA results are in, and they prove beyond any doubt that the child you've been raising as your own "
        "belongs to your business partner and your wife!"
    ),
    (
        "I intercepted the wire transfer that proves you've been embezzling millions from the company while your own "
        "brother's family starved, thinking the business was failing!"
    ),
    (
        "The journal I found reveals that our family has been cursed for seven generations, and every tragedy we've "
        "suffered was predicted on these yellowed, terrifying pages!"
    ),
    (
        "Your beloved mentor, the man you trusted with your career, has been sabotaging you from day one because he's "
        "secretly in love with your wife and wants you gone!"
    ),
    (
        "I have recordings, photographs, testimonies from witnesses, an entire file cabinet of evidence proving that "
        "you are the mastermind behind every misfortune we've ever suffered!"
    ),
    (
        "The grave we've been visiting for ten years is empty! The person we mourned, the person we buried, is alive "
        "and has been watching us this entire time!"
    ),
]

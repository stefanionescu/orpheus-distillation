"""Multi-sentence prompts: mixed conversation, then hysteria, rage, joy, despair, and nervous excitement."""

from __future__ import annotations

CHATTER: list[str] = [
    (
        "The amusement park seems less magical than it did when I was eight. Scale and wonder diminish with age "
        "unfortunately."
    ),
    (
        "The zoo animals I memorized as a child have been reorganized differently. Institutional knowledge becomes "
        "obsolete alongside everything else."
    ),
    (
        "The mountain I thought was enormous is actually modest by global standards. Travel adjusts our sense of "
        "relative significance."
    ),
    (
        "The lake we swam in every summer has warnings posted about water quality now. Environmental changes affect "
        "personal histories directly."
    ),
    (
        "The cabin we rented for family vacations was sold and renovated completely. Other people's improvements erase "
        "our specific memories."
    ),
    (
        "The campground we loved has reviews now calling it overpriced and crowded. Popular places change under the "
        "weight of popularity itself."
    ),
    (
        "The trail we hiked is closed indefinitely for erosion repairs currently. Access to nature requires "
        "infrastructure that nature itself damages."
    ),
    (
        "The beach where we scattered ashes seems less special to other visitors somehow. Personal significance "
        "doesn't translate to strangers obviously."
    ),
    (
        "The overlook with the best view now has a guardrail blocking it partially. Safety and beauty compete for "
        "priority constantly."
    ),
    (
        "The waterfall we hiked six miles to reach is now accessible by road. Effort and reward no longer correlate as "
        "they once did."
    ),
    (
        "The wilderness area we explored is now designated and regulated formally. Protection sometimes means "
        "restriction of the very access we valued."
    ),
    (
        "The night sky from that location has more light pollution than before now. Darkness becomes scarce as "
        "development spreads outward."
    ),
    (
        "The wildlife we saw regularly has apparently relocated due to habitat changes. Animals adapt to human impact "
        "by avoiding us."
    ),
    (
        "The quiet spot I treasured was discovered and popularized by social media unfortunately. Secrecy can't "
        "survive the age of sharing."
    ),
    (
        "The fishing hole my grandfather showed me has been stocked artificially now. Wild places become managed "
        "resources eventually."
    ),
    (
        "The cave we explored as teenagers is gated and requires permits now. Adventure becomes bureaucracy when "
        "safety concerns accumulate."
    ),
    (
        "The hot springs we soaked in privately are now a commercial operation entirely. Commodification follows "
        "discovery as reliably as anything."
    ),
    (
        "The forest where we got lost on purpose is now mapped and signed thoroughly. Getting lost requires more "
        "effort than it used to."
    ),
    (
        "The meadow full of wildflowers we photographed was developed into housing sadly. Natural beauty becomes "
        "luxury views for new residents."
    ),
    (
        "The river we tubed down requires reservations and has capacity limits now. Recreation becomes regulated as "
        "demand exceeds supply."
    ),
    (
        "The mountain summit where we watched sunrise now has a webcam broadcasting constantly. Solitude competes with "
        "connectivity everywhere."
    ),
    (
        "The glacier we visited has retreated visibly since the photographs were taken then. Climate change makes "
        "comparison photos devastating."
    ),
    (
        "The coral reef we snorkeled shows bleaching that wasn't present a decade ago. Underwater landscapes are "
        "changing faster than terrestrial ones."
    ),
    (
        "The coastline we walked has eroded significantly since childhood visits there. Shorelines don't wait for our "
        "memories to catch up."
    ),
    (
        "The storm patterns feel different than they used to when I was younger. Weather itself seems to be changing "
        "with everything else."
    ),
    (
        "The seasons don't arrive when they used to according to my memory anyway. Calendars disagree with climate "
        "more often now."
    ),
    (
        "The birds I expect to hear in spring arrive at different times lately. Migration patterns respond to changes "
        "we cause."
    ),
    (
        "The flowers that bloomed predictably now appear weeks earlier than before. Gardens follow schedules we no "
        "longer set accurately."
    ),
    (
        "The fireflies I remember from childhood are scarcer in the same locations now. Light pollution and habitat "
        "loss affect magic too."
    ),
    (
        "The frogs that sang at night have gone quiet in familiar places sadly. Amphibian decline happens silently "
        "where we notice eventually."
    ),
    (
        "The butterflies that covered certain fields are fewer each passing year apparently. Beautiful things diminish "
        "while we're not watching carefully."
    ),
    (
        "The stars visible from my backyard are fewer than when I was young there. The sky itself becomes less "
        "available to us."
    ),
    (
        "The darkness I took for granted is now something I have to travel toward. Light follows civilization and "
        "crowds out the night."
    ),
    (
        "The silence I remember from certain places no longer exists in the same way. Sound pollution is omnipresent "
        "even in nature now."
    ),
    (
        "The wildness I knew as a child has been tamed into something manageable. Untamed places become endangered "
        "alongside the species in them."
    ),
    (
        "The certainty I had about my future at eighteen seems almost comical now. Life has a way of humbling our "
        "confident predictions."
    ),
    (
        "The conversations I replay in my head always go better than the originals did. Retrospective eloquence is a "
        "special kind of torture."
    ),
    (
        "The energy I have for certain people versus others reveals something about compatibility. Some connections "
        "energize; others quietly deplete us."
    ),
    (
        "The patience I show strangers often exceeds what I give to people I love most. Familiarity breeds a strange "
        "kind of carelessness."
    ),
    (
        "The version of events I remember probably differs from what actually happened objectively. Memory is creative "
        "reconstruction not faithful recording."
    ),
    (
        "The assumptions I make about others usually say more about me than them. Projection is the lens we don't "
        "notice we're wearing."
    ),
    (
        "The fears that kept me up at night mostly never materialized at all. Anxiety creates futures that reality "
        "rarely delivers."
    ),
    (
        "The changes I resisted hardest often turned out to be exactly what I needed. Resistance indicates importance "
        "more than actual threat."
    ),
    (
        "The person I'm becoming isn't finished yet and probably never will be completely. Growth continues until it "
        "doesn't anymore."
    ),
    (
        "The story I tell about my life keeps getting revised with each telling naturally. We are unreliable narrators "
        "of our own experience."
    ),
    # HYSTERIA & PANIC
    "I can not breathe! I literally cannot breathe right now! My chest is closing in and everything is spinning!",
    "This is a nightmare! Wake me up! Someone please wake me up because this cannot be happening to me!",
    "They found out! Oh god, they found out everything! What am I going to do? What am I going to do?",
    "The walls are closing in on me! I swear I can feel them getting closer! Get me out of here now!",
    "I think I am dying! Something is wrong with my heart! It is beating too fast! I cannot make it stop!",
    "Everyone is staring at me! They are all watching and judging! I need to leave! I need to get out now!",
    "It is gone! Everything is gone! Years of work just vanished! I cannot process this! My brain is breaking!",
    "The ground is shaking! Is this an earthquake? Oh god, oh god, we need to get outside right now!",
    "I heard something downstairs! There is someone in my house! I am trapped up here! What do I do?",
    "The test came back positive! Positive! Do you understand what this means? My whole life is over!",
    "I forgot to submit it! The deadline passed an hour ago! My entire semester is ruined! I am going to fail!",
    "They are going to fire me! I just know it! The way she looked at me in that meeting! I am finished!",
    "My phone is at one percent! I have no charger! I am lost in the middle of nowhere! Help me!",
    "The brakes are not working! I keep pressing but nothing is happening! Oh my god, oh my god!",
    "I cannot find my child! They were right here! They were right here a second ago! Where are they?",
    "There is blood everywhere! So much blood! I do not know what to do! Someone call an ambulance!",
    "The plane is shaking! This is not normal turbulence! Look at the flight attendants! They look scared too!",
    "I am locked out! My keys, my phone, everything is inside! It is freezing out here! What do I do?",
    "The water is rising! It is already at my ankles! We need to get to higher ground! Move, move, move!",
    "I think I saw something move in the corner! There it is again! There is something in this room with me!",
    # EXPLOSIVE RAGE
    "You absolute monster! You destroyed everything I ever loved and you have the nerve to stand there smiling!",
    "I gave you everything! Every single piece of my soul! And you threw it away like garbage!",
    "Get out of my face before I do something I will regret! I am warning you! Get out now!",
    "You think this is funny? You think ruining my life is some kind of joke? I will show you funny!",
    "I trusted you! I defended you to everyone! And this is how you repay me? With this betrayal?",
    "The audacity! The absolute audacity of you showing up here after what you did! Unbelievable!",
    "Do not touch me! Do not you dare touch me! You lost that right the moment you chose to lie!",
    "I am so angry I cannot see straight! My vision is literally red! You did this to me!",
    "You spineless coward! Running away instead of facing what you did! Stand here and look at the damage!",
    "Every word that comes out of your mouth is poison! Lies upon lies upon lies! I am drowning in them!",
    "You want to see rage? You want to see what happens when you push someone too far? Watch closely!",
    "I could scream! I could absolutely scream right now! The injustice of this situation is suffocating me!",
    "They had no right! No right at all! Who do they think they are? I will not stand for this!",
    "My blood is boiling! I can feel it coursing through my veins like fire! Someone is going to pay!",
    "You think you can treat people like this and get away with it? Not this time! Not with me!",
    "I have never hated anyone the way I hate you in this moment! You are dead to me!",
    "The disrespect! The utter disrespect you have shown me is beyond comprehension! Beyond forgiveness!",
    "I worked for years! Years! And you swept it away in seconds! Do you even understand what you took?",
    "Say it to my face! Come on! Say it again! I dare you to repeat those words while looking at me!",
    "I am shaking with fury! My hands will not stop trembling! This is what you have reduced me to!",
    # ECSTATIC JOY
    "I got in! I actually got in! After everything, after all those rejections, they said yes! They said yes!",
    "We are having a baby! A baby! I cannot stop crying! These are the happiest tears of my life!",
    "I won! Against all odds, against everyone who doubted me, I actually won! Someone pinch me!",
    "They are alive! Oh thank god, thank god! They are alive! I thought I lost them forever!",
    "This is the best day of my entire existence! Nothing will ever top this moment! Nothing ever!",
    "I found it! After twenty years of searching, I finally found it! I cannot believe my eyes!",
    "We are going to be okay! Everything is going to be okay! I can finally breathe again!",
    "The results came back and it is benign! Benign! I am going to live! I have my whole life ahead!",
    "You said yes! You actually said yes! I have been dreaming of this moment for years!",
    "I passed! Not just passed, I got the highest score! Me! The kid they said would never amount to anything!",
    "We did it! Together! Against impossible odds! I love this team! I love every single one of you!",
    "This view! This incredible, breathtaking view! I am standing on top of the world! Literally!",
    "They published my book! My words are going to be read by thousands! I am a real author now!",
    "The check cleared! We are out of debt! After ten years of struggling, we are finally free!",
    "I found my soulmate! This is the person I want to spend forever with! I have never been so sure!",
    "Everything clicked! All those pieces fell into place! I understand now! I finally understand!",
    "They forgave me! After everything I did, they actually forgave me! I have a second chance!",
    "I am going to be a grandmother! My baby is having a baby! The circle of life continues!",
    "This is real! This is not a dream! I keep checking and it is really, truly happening!",
    "I cannot contain this joy! It is bursting out of me! I want to hug every stranger I see!",
    # CRUSHING DESPAIR
    "I have nothing left. Absolutely nothing. Everyone I loved is gone and I am completely alone.",
    "What is even the point anymore? Every time I try, I fail. Every single time without exception.",
    "The darkness is swallowing me whole. I can feel myself disappearing and I lack the strength to fight it.",
    "They left. Just like everyone always leaves. I must be fundamentally unlovable. That is the only explanation.",
    "I am so tired. Not sleepy tired. Soul tired. The kind of exhaustion that sleep cannot fix.",
    "Watching everyone else be happy just reminds me of everything I will never have. It is torture.",
    "I am drowning in this pain. Wave after wave after wave. There is no surface to reach for.",
    "Nobody notices. Nobody ever notices. I could vanish tomorrow and the world would keep spinning.",
    "I gave it everything. Every last drop of hope I had. And it still was not enough. I am still not enough.",
    "The emptiness inside me has become so vast. I do not even recognize myself anymore.",
    "I miss who I used to be. That person who could smile without forcing it. Where did they go?",
    "Every morning I wake up disappointed. Disappointed that I have to do this all over again.",
    "The grief is eating me alive. From the inside out. There is nothing left but this aching void.",
    "I thought I had hit rock bottom. Then the floor gave way and I fell even further.",
    "I am fading. Day by day. Piece by piece. Soon there will be nothing left at all.",
    "They took everything from me. My dignity. My hope. My reason for getting out of bed.",
    "I cannot remember the last time I felt genuine joy. It has been so long. Too long.",
    "This pain is my only companion now. The only constant in a world that keeps abandoning me.",
    "I used to believe things would get better. I used to have hope. Now I have only questions.",
    "The silence in this empty house is deafening. It echoes with all the voices that used to fill it.",
    # NERVOUS EXCITEMENT
    "It is almost time! Five more minutes! I think I might faint from anticipation! My legs are jelly!",
    "What if they love it? What if they actually love it? Oh god, what if they hate it? I cannot look!",
    "My heart is doing backflips! This is really happening! After all this planning, it is finally here!",
    "I have butterflies! No, not butterflies! Pterodactyls! An entire prehistoric zoo in my stomach!",
    "The countdown is starting! Ten! Nine! I cannot feel my fingers! Is that normal? Eight! Seven!",
    "They are about to announce it! I might throw up! From excitement! Is that a thing? I think that is a thing!",
    "I keep pacing! I cannot sit still! The energy coursing through me needs somewhere to go!",
    "What if this is the moment everything changes? What if my whole life pivots right here, right now?",
    "I have practiced this a thousand times but now my mind is completely blank! Where did all the words go?",
    "The anticipation is killing me! In the best way! Like sweet torture that I never want to end!",
    "I am about to meet my hero! The person whose work changed my life! I might actually cry!",
    "Everything I have worked for leads to this one moment! This one beautiful terrifying moment!",
    "I can hear the crowd! They are chanting! For me! They are actually chanting my name!",
    "The envelope is in my hands! The answer to everything is inside! I am too scared to open it!",
    "We are next! Oh my goodness, we are next! Someone hold my hand! I need moral support!",
    "I think I am going to explode! Not literally! But the excitement has nowhere else to go!",
    "This is the moment I have been dreaming about since I was a child! And now it is real!",
    "I cannot eat! I cannot sleep! All I can do is think about what happens tomorrow!",
    "My whole body is vibrating with anticipation! Like I swallowed a hummingbird! Or several!",
    "The suspense is absolutely delicious! And also completely unbearable! Both at once somehow!",
]

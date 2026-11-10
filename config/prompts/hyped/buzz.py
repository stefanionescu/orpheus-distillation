"""Excited prompts: short and medium exclamations and statements, then the first long celebrations."""

from __future__ import annotations

BUZZ: list[str] = [
    # ULTRA SHORT
    "Let's go!",
    "Yes yes yes!",
    "This is it!",
    "Finally happening!",
    "I can't even!",
    "So pumped right now!",
    "Best day ever!",
    "Here we go!",
    "It's happening!",
    "I'm so ready!",
    "Oh my gosh!",
    "No way, no way!",
    "I'm screaming!",
    "This is everything!",
    "I literally can't!",
    "Dreams coming true!",
    "So freaking excited!",
    "I'm shaking right now!",
    "The vibes are immaculate!",
    "I'm losing my mind!",
    "This is insane!",
    "I'm dying of excitement!",
    "Best news ever!",
    "My heart is racing!",
    "Can't contain myself!",
    "This is unreal!",
    "I'm so here for this!",
    "Absolutely incredible!",
    "Living my best life!",
    "I'm obsessed already!",
    "The moment is here!",
    "Pure happiness right now!",
    "I've waited so long!",
    "Finally, finally, finally!",
    "This is legendary!",
    "I'm freaking out!",
    "Beyond excited right now!",
    "Can you believe it!",
    "My dreams are real!",
    "I'm over the moon!",
    "So incredibly hyped!",
    "This is monumental!",
    "Absolutely buzzing right now!",
    "The anticipation is killing me!",
    "I'm genuinely speechless!",
    "Everything is perfect!",
    "I'm on cloud nine!",
    "Greatest feeling ever!",
    # SHORT EXCLAMATIONS
    "I've been waiting for this moment my entire life and now it's finally here!",
    "The energy in this room is absolutely electric and I'm feeding off every bit of it!",
    "My hands are literally shaking because I'm so excited about what's about to happen!",
    "I don't think you understand how long I've been dreaming about this exact moment!",
    "Every single cell in my body is vibrating with pure excitement right now!",
    "This is the kind of news that makes you want to run around screaming with joy!",
    "I'm trying so hard to stay calm but my excitement is completely taking over!",
    "You could not pay me to be any happier than I am at this very second!",
    "The butterflies in my stomach have butterflies and they're all doing backflips!",
    "I've replayed this moment in my head a thousand times and it's finally real!",
    "Someone pinch me because there's no way this is actually happening right now!",
    "My excitement levels are through the roof and climbing higher by the second!",
    "I'm pretty sure my neighbors can hear me screaming but I don't even care!",
    "This is exactly what I needed and I couldn't be more thrilled about it!",
    "The countdown is finally over and I'm absolutely losing my mind with joy!",
    "I've never felt this level of excitement before and it's completely overwhelming!",
    "Everything is coming together so perfectly and I'm here for every single second!",
    "My heart is beating so fast that I can actually feel it in my throat!",
    "This announcement just made my entire week, month, and honestly maybe year!",
    "I'm bouncing off the walls and there's nothing anyone can do to stop me!",
    "The hype is so real right now and I'm completely swept up in it!",
    "I'm grinning from ear to ear and my face actually hurts from smiling!",
    "You have no idea how much this means to me and I'm absolutely thrilled!",
    "Every nerve ending in my body is on fire with pure unadulterated excitement!",
    "I'm going to remember this feeling for the rest of my entire life!",
    "The anticipation has been building and building and now it's finally paying off!",
    "I'm trying to form coherent sentences but my brain is just screaming with joy!",
    "This is the kind of moment that makes everything else worth it!",
    "I didn't think I could get any more excited but here I am proving myself wrong!",
    "My excitement is contagious and everyone around me is catching the bug!",
    "I'm so hyped that I might spontaneously combust from sheer happiness!",
    "The wait has been torture but now that it's here I can't stop celebrating!",
    "I'm practically vibrating with anticipation and I love every second of it!",
    "This has exceeded every single one of my expectations and then some!",
    "I'm running on pure adrenaline and excitement and I never want it to end!",
    "My whole body is tingling with excitement and I don't know what to do with myself!",
    "I've been counting down the days and now that it's here I'm completely overwhelmed!",
    "The joy I'm feeling right now is absolutely indescribable and I love it!",
    "I'm so pumped that I could probably run a marathon without breaking a sweat!",
    "Everything I've been hoping for is finally happening and it's even better than I imagined!",
    "I can't remember the last time I was this excited about anything!",
    "My enthusiasm is off the charts and there's no bringing it down!",
    "This is giving me all the feels and I'm completely here for it!",
    "I'm so stoked that I can barely sit still long enough to tell you about it!",
    "The thrill of this moment is absolutely coursing through my veins!",
    "I'm over here doing a happy dance and I don't care who sees!",
    "My excitement is physically manifesting and I'm shaking with pure joy!",
    "This is hands down one of the best things that has ever happened to me!",
    "I'm so fired up right now that I could take on the entire world!",
    "The feeling of pure elation is washing over me and it's absolutely incredible!",
    # MEDIUM STATEMENTS
    "I just found out the best news and I'm literally jumping up and down with pure joy!",
    "My excitement right now is absolutely unmatched and I need everyone to know about it!",
    "I can feel the adrenaline pumping through my body and it's the best feeling ever!",
    "This moment is everything I've been working toward and it's finally paying off!",
    "I'm so hyped that words cannot even begin to describe what I'm feeling right now!",
    "The energy is absolutely unreal and I'm soaking up every single bit of it!",
    "I've never been more ready for anything in my entire life than I am right now!",
    "My soul is literally singing with happiness and I want the whole world to hear!",
    "This is the news I've been waiting to hear and it's even sweeter than expected!",
    "I'm on an emotional high that I never want to come down from!",
    "Every dream I've ever had is coming true and I'm here living through it!",
    "The pure joy radiating from my entire being is absolutely contagious right now!",
    "I'm so thrilled that I could burst into spontaneous happy tears at any moment!",
    "This feeling of excitement is something I want to bottle up and keep forever!",
    "My happiness meter just broke because it went way past maximum capacity!",
    "I'm experiencing levels of hype that I didn't even know were humanly possible!",
    "The butterflies in my stomach have evolved into full on fireworks of excitement!",
    "I'm so incredibly grateful and excited that my heart might actually explode!",
    "This is the moment I've been visualizing and manifesting for so incredibly long!",
    "I'm radiating pure excitement and everyone in my vicinity can feel it too!",
    "My inner child is doing cartwheels because this is literally a dream come true!",
    "The exhilaration I'm feeling right now is absolutely out of this world!",
    "I'm so amped up that I could probably power a small city with my energy!",
    "This news has me floating on air and I never want my feet to touch the ground!",
    "I'm overwhelmed in the absolute best way possible and I'm embracing every second!",
    "The happiness bubbling inside me is threatening to overflow at any moment!",
    "I'm so electrified with excitement that I can practically hear myself buzzing!",
    "This is peak excitement and I'm savoring every single millisecond of it!",
    "My enthusiasm is reaching astronomical levels and showing no signs of slowing down!",
    "I'm living for this moment and it's exceeding every expectation I ever had!",
    "The thrill running through me right now is absolutely indescribable and amazing!",
    "I'm so pumped that I feel like I could leap tall buildings in a single bound!",
    "This excitement is hitting different and I'm completely here for the ride!",
    "My heart is so full of joy that it might actually burst at the seams!",
    "I'm riding the biggest wave of happiness and I never want it to end!",
    "The anticipation finally paid off and it was worth every agonizing second of waiting!",
    "I'm so ecstatic that I can barely contain myself long enough to tell you!",
    "This moment is pure magic and I'm absolutely spellbound by the excitement!",
    "My whole being is consumed with the most incredible feeling of elation!",
    "I'm so ready to celebrate that I've already started my victory dance!",
    "The hype train has arrived and I've got a front row seat on it!",
    "I'm experiencing such pure joy that everything else has faded into the background!",
    "This is the highlight I've been waiting for and it's absolutely delivering!",
    "My excitement is building like a crescendo and it's about to reach its peak!",
    "I'm so wired with anticipation that sleep is absolutely not an option tonight!",
    "The rush of excitement I'm feeling right now is better than any caffeine!",
    "I'm so deliriously happy that I might actually be floating off the ground!",
    "This news has me absolutely buzzing and I can't stop talking about it!",
    "My joy is overflowing and spilling onto everyone around me right now!",
    "I'm experiencing the kind of excitement that makes you feel truly alive!",
    "The pure elation coursing through me is absolutely unlike anything I've felt before!",
    "I'm so hyped that my excitement has its own excitement and they're both celebrating!",
    "This feeling is everything I hoped it would be and so much more!",
    "My happiness is radiating outward in waves and touching everyone nearby!",
    "I'm so incredibly stoked that I could probably fly if I tried right now!",
    "The joy I'm experiencing is making me want to hug absolutely everyone!",
    "I'm vibrating at a frequency of pure excitement and bliss right now!",
    "This moment is chef's kiss and I'm savoring every delicious second of it!",
    "My enthusiasm has reached a fever pitch and there's no cooling it down!",
    "I'm so thrilled that I keep pinching myself to make sure this is real life!",
    "The excitement building inside me is like a volcano about to erupt with joy!",
    "I'm experiencing such intense happiness that I might need to sit down!",
    "This is giving me life in ways I didn't even know I needed!",
    "My spirit is absolutely soaring and nothing can bring me back down!",
    "I'm so pumped that I want to share this feeling with the entire world!",
    "The rush of adrenaline and joy is making my head spin in the best way!",
    "I'm so completely and utterly thrilled that I've lost the ability to chill!",
    "This excitement is the fuel I needed and now I'm running on all cylinders!",
    "My happiness levels have officially gone into overdrive and I love it!",
    "I'm so hyped that I need to tell everyone I know about this immediately!",
    "The sheer magnitude of my excitement cannot be measured by any known scale!",
    "I'm bouncing with so much energy that I might achieve liftoff any second now!",
    "This feeling of pure excitement is exactly what I needed in my life!",
    "My entire body is humming with anticipation and joyful energy right now!",
    "I'm so ready for this that I've been ready since before I even knew about it!",
    "The wave of euphoria washing over me is absolutely breathtaking!",
    "I'm experiencing peak happiness and I want to freeze this moment forever!",
    "My excitement is so real that you could probably see it from outer space!",
    "This is the kind of thrill that makes your whole body tingle with joy!",
    "I'm so incredibly amped that I might spontaneously break into song and dance!",
    "The pure unadulterated joy I'm feeling is making everything seem brighter!",
    "I'm so excited that I've already told my plants, my pets, and my pillow about it!",
    "This moment is absolutely surreal and I'm living for every second of it!",
    "My heart is doing backflips and my soul is doing a standing ovation!",
    "I'm riding such a high right now that I never want to come back down!",
    "The excitement pulsing through me is giving me superhuman levels of energy!",
    "I'm so jazzed up that my excitement is literally oozing out of my pores!",
    "This is the news that makes you want to scream from the rooftops!",
    "My enthusiasm is reaching new heights that I didn't know existed!",
    "I'm so overcome with joy that I'm having trouble forming complete sentences!",
    "The thrill of this moment is something I'll treasure for years to come!",
    "I'm experiencing such overwhelming happiness that I might actually cry!",
    "This excitement is consuming me in the most wonderful way possible!",
    "My energy levels have skyrocketed and I'm absolutely loving every minute!",
    "I'm so fired up that you could probably roast marshmallows on my enthusiasm!",
    "The anticipation paid off in the most spectacular way imaginable!",
    "I'm bursting with so much joy that I can't decide what to do first!",
    "This is hands down the most exciting thing that's happened to me in forever!",
    "My whole world just got brighter and I'm basking in the glow!",
    "I'm so amped that I could run laps around my excitement and still have energy left!",
    # LONG CELEBRATIONS
    (
        "I cannot believe this is actually happening right now because I've been dreaming about this moment for so "
        "long and now that it's here I'm completely overwhelmed with joy!"
    ),
    (
        "The level of excitement I'm experiencing right now is something I never thought possible and I want to share "
        "this incredible feeling with absolutely everyone I know!"
    ),
    (
        "My heart is pounding so hard in my chest that I can hear it in my ears and my hands are shaking because the "
        "anticipation has finally given way to pure elation!"
    ),
    (
        "I've been waiting and hoping and wishing for this exact moment and now that it's finally arrived I don't even "
        "know how to properly express my overwhelming gratitude and joy!"
    ),
    (
        "Every fiber of my being is vibrating with such intense excitement that I feel like I might actually levitate "
        "off the ground from the sheer force of my happiness right now!"
    ),
    (
        "This news has completely made my entire existence and I'm going to be riding this wave of euphoria for weeks, "
        "months, maybe even years to come because it's just that incredible!"
    ),
    (
        "The feeling of pure unadulterated joy that's washing over me right now is unlike anything I've ever "
        "experienced before and I never want this magical moment to end!"
    ),
    (
        "I'm so incredibly hyped that I've already texted everyone in my contacts, posted on all my social media, and "
        "now I'm telling complete strangers because I can't contain it!"
    ),
    (
        "My excitement has reached such astronomical proportions that I'm pretty sure scientists could measure it from "
        "space if they pointed their instruments in my direction right now!"
    ),
    (
        "I cannot stop smiling and my face muscles are actually starting to hurt but I don't even care because this "
        "feeling of pure joy is absolutely worth every bit of discomfort!"
    ),
    (
        "The anticipation that's been building up inside me has finally reached its peak and now it's exploding into "
        "the most magnificent fireworks display of happiness and celebration!"
    ),
    (
        "I'm experiencing the kind of thrill that makes you feel completely alive and connected to every good thing in "
        "the universe and I want to hold onto this feeling forever!"
    ),
    (
        "My soul is singing a symphony of joy right now and every note is hitting perfectly because this is exactly "
        "what I've been hoping and praying and manifesting for so long!"
    ),
    (
        "The energy coursing through my veins right now is pure liquid excitement and it's giving me the strength and "
        "motivation to take on absolutely anything the world throws at me!"
    ),
    (
        "I've replayed this scenario in my head countless times but the reality is so much sweeter than anything I "
        "could have possibly imagined and I'm absolutely living for it!"
    ),
    (
        "My happiness is so overwhelming that I'm having trouble processing it all and I keep having to remind myself "
        "that this is actually real life and not just a beautiful dream!"
    ),
    (
        "The sheer magnitude of this moment has me completely speechless yet somehow I can't stop talking about it "
        "because the excitement just keeps bubbling up and overflowing out of me!"
    ),
    (
        "I'm so incredibly pumped right now that I feel like I could accomplish anything and everything because this "
        "feeling of unstoppable joy is giving me superpowers I never knew I had!"
    ),
    (
        "Every dream I've ever dreamed and every wish I've ever made is coming true right before my very eyes and I'm "
        "standing here in absolute awe of how beautiful this moment is!"
    ),
    (
        "The joy radiating from my core is so intense that I'm pretty sure I'm glowing and everyone around me can see "
        "the literal light of happiness emanating from my entire being!"
    ),
    (
        "I've never felt more alive than I do right now in this exact moment and I want to freeze time and stay here "
        "forever because this is what pure bliss feels like!"
    ),
    (
        "My excitement is so contagious that everyone who comes near me immediately starts smiling and laughing and I "
        "love that I can spread this incredible joy to others around me!"
    ),
    (
        "The waiting and the wondering and the hoping has finally come to an end and the payoff is so incredibly sweet "
        "that I'm savoring every single second of this magnificent moment!"
    ),
]

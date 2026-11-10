"""Multi-sentence prompts: confrontations and vulnerable moments, then longer romance and confessions."""

from __future__ import annotations

CONFRONTATIONS: list[str] = [
    # EMOTIONAL CONFRONTATIONS & INTENSE ARGUMENTS
    "How could you do this to me after everything? I gave you my complete trust and you shattered it entirely.",
    "Don't you dare walk away from me right now! We are going to finish this conversation whether you like it or not.",
    "I saw the messages, so don't even try lying. Every single word, every emoji, everything between you two.",
    "You've been making me feel crazy for months now. Gaslighting me, making me question my own reality constantly.",
    (
        "I'm not going to apologize for having feelings again. Stop expecting me to suppress everything uncomfortable "
        "for you."
    ),
    "The way you treat me in front of your friends stings. Like I'm an embarrassment, a joke, something to tolerate.",
    "We need to talk about what happened last night seriously. You can't just pretend everything is fine afterward.",
    "I've been defending you to everyone I know constantly. But maybe they were right about you all along.",
    "Your silence is louder than any words could be now. It's a weapon, and you wield it deliberately.",
    "Stop bringing up things I did years ago constantly! I've apologized, I've changed, when does forgiveness come?",
    "I can't keep being the only one who tries here. Relationships require two people, not just one begging.",
    "The contempt in your voice when you talk to me is devastating. Like you've already given up completely.",
    "You promised me you would change this time sincerely. And I believed you again like a complete fool.",
    "I'm not crazy for noticing something is wrong between us. Trust your gut, my friends said, and I finally am.",
    "Every fight we have feels like the end of everything. We tear each other apart instead of solving anything.",
    "You've been withdrawing from me for weeks now slowly. Creating distance, building walls, preparing to leave.",
    "I refuse to be someone's second choice any longer. Either I'm your priority or I'm nothing at all.",
    (
        "The passive aggression is exhausting me completely daily. Just say what you mean instead of punishing me "
        "silently."
    ),
    "We've been having the same argument for three years now. Something has to change or we both break.",
    "I'm starting to hate who I become around you lately. This angry, defensive, insecure version of myself.",
    "You used my deepest insecurities against me deliberately. Weaponized the vulnerabilities I trusted you with.",
    "Don't tell me to calm down when you caused this situation! Your actions have consequences, deal with them.",
    "I've been walking on eggshells around you for months now. Terrified of triggering another explosive episode.",
    "The things you said last night cannot be unsaid ever. They're carved into my memory, permanent and painful.",
    (
        "You've been emotionally unavailable for our entire relationship honestly. I fell in love with potential, not "
        "reality."
    ),
    "I deserve better than crumbs of affection occasionally given. I deserve someone who shows up consistently.",
    "Stop minimizing my feelings like they don't matter to you. My pain is valid even if you don't understand it.",
    "The resentment I've been building is reaching breaking point now. I can't swallow anymore anger and pretend.",
    "You're projecting your own guilt onto me constantly daily. I'm not the one who did anything wrong here.",
    "I've been mourning this relationship while still in it. Grieving what we used to be, what we'll never be again.",
    "Your apologies mean nothing without changed behavior following. Words are empty without actions to back them up.",
    (
        "I caught you in a lie and now I question everything completely. Every word, every promise, every moment "
        "between us."
    ),
    "We need professional help to navigate this mess together. I can't fix this alone, and neither can you.",
    (
        "The way you dismiss my concerns is incredibly hurtful actually. Like my perspective doesn't even deserve "
        "consideration."
    ),
    "I've given you more chances than you ever deserved already. This is the last time I let you hurt me.",
    "You've been comparing me to your ex constantly lately. I'll never be them, and I don't want to be.",
    "The disrespect you showed me in front of everyone was humiliating. You owe me a public apology at minimum.",
    "I'm exhausted from being the emotional manager of this relationship. When do you start carrying some weight?",
    "We've lost ourselves trying to make this work somehow. Neither of us is happy, we're just surviving together.",
    "You've changed, and not in the ways you promised me. I barely recognize the person standing before me now.",
    # VULNERABLE MOMENTS & TENDER REVELATIONS
    "I'm scared of being loved by you completely. Because that means I have something precious to lose now.",
    "You're the first person I've let see my scars openly. Both the visible ones and the invisible ones too.",
    "Sometimes I wake up and watch you sleep peacefully. Just to convince myself this is real, you're real.",
    "I've never told anyone about my childhood honestly. But with you, the words want to finally come out.",
    "You make me feel safe in a way no one else ever has before. Like I can finally lower my guard.",
    "I'm terrified that one day you'll realize I'm not enough. That you could do better, deserve better.",
    "The way you hold me makes everything else disappear completely. All the noise, all the chaos, just silence.",
    "I've been independent my whole life by necessity always. Letting you in feels like learning to walk again.",
    "You remembered something I mentioned months ago casually once. No one ever listens to me that closely.",
    "I write about you in my journal every single night. Pages and pages about how you make me feel.",
    "My biggest fear is waking up and this being a dream somehow. That you never existed, never loved me.",
    "I've never been good at accepting help from anyone ever. But you make me want to try, to lean.",
    "The tenderness you show me brings me to tears sometimes. I didn't know love could feel this gentle.",
    "You've seen me ugly cry and didn't run away afterward. That's when I knew this might actually last.",
    "I used to think I was fundamentally unlovable deep down. You're slowly convincing me otherwise, daily.",
    "The first time you said you loved me, I panicked completely. Not because I didn't believe you, but because I did.",
    "I've practiced being alone for so many years carefully. Now the thought of loneliness terrifies me again.",
    "You touch me like I'm something precious and breakable almost. Like I matter, like I'm worth being careful with.",
    (
        "My walls took years to build but crumbled instantly for you. That vulnerability is exhilarating and "
        "terrifying simultaneously."
    ),
    "I've been waiting my whole life to feel this understood finally. Like someone actually sees the real me.",
    (
        "The way you defend me to others means everything honestly. Having someone in my corner unconditionally "
        "changes everything."
    ),
    "I'm not used to someone staying after seeing my darkness completely. Most people leave once the shine wears off.",
    "You've become my safe place in this chaotic world now. The one constant I can always depend on.",
    "I've shared things with you I've never verbalized before ever. Secrets I planned to carry to my grave.",
    "The patience you have for my healing process astounds me. Not everyone would wait while I figure myself out.",
    "I've been someone's last choice so many times before now. Being your first choice feels like a miracle.",
    "You make me want to be braver than I actually am inside. To grow, to stretch, to become more.",
    "The way you look at me makes me feel genuinely beautiful. Not just attractive, but seen and valued.",
    "I've apologized for my existence my entire life reflexively. You're the first person who told me to stop.",
    "My anxiety tells me you'll leave eventually like everyone does. But you keep proving those fears wrong daily.",
    "I've never let anyone take care of me when sick before. Being that vulnerable with you felt revolutionary.",
    "The gentle way you correct me without shaming means everything. I can grow without feeling worthless.",
    "I've measured every relationship against a fantasy until you. You're better than anything I ever imagined.",
    "You love parts of me I've hidden from myself in shame. Seeing them through your eyes changes everything.",
    (
        "I'm learning to receive love without waiting for conditions attached. It's harder than it sounds, but you're "
        "teaching me."
    ),
    "The first time you met my family, I was terrified completely. But you loved them despite everything chaotic.",
    (
        "I've spent years performing acceptable versions of myself constantly. You're the first person who wants the "
        "unedited one."
    ),
    (
        "You've witnessed my lowest moment and stayed anyway consistently. That loyalty rebuilt something broken "
        "inside me."
    ),
    "I used to flinch when people raised their voices around me. You've never once given me reason to flinch.",
    "Falling asleep in your arms feels like coming home finally. Like my body recognizes a safety it always craved.",
    # EXTENDED ROMANTIC & PASSIONATE (LONGER FORM)
    (
        "I want to wake up next to you every single morning for the rest of my existence. Your face is the first thing "
        "I want to see when I open my eyes, forever and always."
    ),
    (
        "You've completely shattered every expectation I ever had about love and relationships. What we have is so "
        "much better than anything I could have possibly imagined or dreamed."
    ),
    (
        "The universe must have conspired for millions of years just to bring us together in this exact moment. I "
        "believe in fate now because of you, because of us."
    ),
    (
        "When I look into your eyes, I see our entire future unfolding beautifully before me. Children, grandchildren, "
        "growing old together on a porch somewhere watching sunsets."
    ),
    (
        "I want to memorize the way your voice sounds when you first wake up. That raspy, sleepy tone is my absolute "
        "favorite sound in this entire world."
    ),
    (
        "My heart physically aches with how much I love you sometimes. It's overwhelming, consuming, and absolutely "
        "the best feeling I've ever experienced in my life."
    ),
    (
        "I've replayed our first kiss thousands of times in my memory. Every sensation, every breath, every heartbeat "
        "is permanently etched into my soul forever."
    ),
    (
        "You make me want to believe in things I'd given up on years ago. Hope, faith, unconditional love, happily "
        "ever after, all of it feels possible with you."
    ),
    (
        "I never understood why people wrote love songs until I met you finally. Now I want to compose symphonies "
        "about the way you make me feel daily."
    ),
    (
        "The sound of your laughter is the most beautiful music that has ever graced my ears. I would do anything, say "
        "anything, just to hear it again."
    ),
    # EXTENDED EXPLICIT DESIRE (LONGER FORM)
    (
        "I've been fantasizing about pinning you against the wall and kissing you until neither of us can breathe "
        "anymore. Then I want to do unspeakable things to your body."
    ),
    (
        "The way you moan my name when I touch you in that special spot drives me absolutely insane. I think about it "
        "constantly, replaying it over and over."
    ),
    (
        "I want to spend hours exploring every single inch of your body with my tongue tonight. Find every sensitive "
        "spot, learn every reaction, worship you completely."
    ),
    (
        "My entire body trembles with anticipation whenever I know we're going to be alone together. The desire that "
        "builds is almost too intense to handle."
    ),
    (
        "I dreamed about you again last night, and when I woke up I was drenched in sweat and absolutely aching for "
        "your touch. It was so vivid."
    ),
    (
        "You have no idea the effect you have on me when you wear that outfit. I can barely concentrate on anything "
        "else, my mind goes to very dirty places."
    ),
    (
        "I want to tie your hands to the headboard and tease you until you're begging and crying for release. Then "
        "I'll decide if you deserve it."
    ),
    (
        "The taste of you is still on my lips from last night and I can't stop thinking about it. I need more, I'm "
        "addicted, I can't get enough."
    ),
    (
        "Watching you touch yourself for me was the hottest thing I have ever witnessed in my entire life. I almost "
        "lost control just from watching you."
    ),
    (
        "I want you to use me however you please tonight, no limits, no boundaries, just pure primal passion. I'm "
        "completely yours to do whatever you want with."
    ),
    # EXTENDED DRAMATIC CONFESSIONS (LONGER FORM)
    (
        "I need to tell you something that has been eating away at my conscience for years now. Please sit down, "
        "because this is going to change everything between us."
    ),
    (
        "The person you married isn't the person I actually am inside. I've been hiding behind a carefully constructed "
        "facade this entire time and I can't do it anymore."
    ),
    (
        "There's a document hidden in our safe deposit box that explains everything about my past. I think it's time "
        "you finally knew the truth about who I was."
    ),
    (
        "I witnessed something terrible that night, something that I've never told another living soul about. But you "
        "deserve to know what's been haunting me."
    ),
    (
        "My family has been keeping a devastating secret from you since the day we met. I've been complicit in the "
        "deception and I hate myself for it."
    ),
    (
        "The reason I disappear sometimes isn't what I told you at all. I've been living a double life and the guilt "
        "is finally destroying me completely."
    ),
    (
        "Before I met you, I did things I'm deeply ashamed of to survive. Things that would make you see me completely "
        "differently if you knew."
    ),
    (
        "Someone from my past has resurfaced and they're threatening to reveal everything unless I comply with their "
        "demands. I don't know what to do anymore."
    ),
    (
        "I found evidence of something disturbing last week that changes my entire understanding of our relationship. "
        "We need to have a very serious conversation."
    ),
    (
        "The accident that changed everything wasn't actually an accident at all, it was deliberate. I've been "
        "carrying this knowledge alone for far too long now."
    ),
    # EXTENDED EMOTIONAL BREAKDOWNS (LONGER FORM)
    (
        "I feel like I'm standing at the edge of an abyss and the ground beneath my feet is crumbling rapidly. I don't "
        "know how much longer I can hold on."
    ),
    (
        "Sometimes the weight of existence feels so heavy that I can barely lift my head off the pillow in the "
        "morning. Everything takes monumental effort."
    ),
    (
        "I've been smiling and saying I'm fine for so long that I've forgotten what genuine happiness actually feels "
        "like. It's all performance now."
    ),
    (
        "The panic attacks have been getting worse lately, coming without warning and leaving me gasping for air on "
        "the bathroom floor. I'm terrified."
    ),
    (
        "I look around at everyone else living their lives so effortlessly. Why does everything feel so impossibly "
        "hard for me all the time?"
    ),
    (
        "There's this emptiness inside of me that nothing seems to fill. No matter what I try or how hard I work, I "
        "can't seem to be okay."
    ),
    (
        "I've been self medicating with things I shouldn't to numb the constant pain that follows me everywhere I go. "
        "It's the only relief I know."
    ),
    (
        "My mind is a prison of intrusive thoughts and worst case scenarios. They play on an endless loop, never "
        "giving me a moment of peace."
    ),
    (
        "I'm exhausted from pretending that I have everything together. In reality, I'm falling apart at the seams "
        "every single day."
    ),
    (
        "The loneliness is unbearable even when I'm surrounded by people who supposedly care about me. I've never felt "
        "more isolated in my life."
    ),
]

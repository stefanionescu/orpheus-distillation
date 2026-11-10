"""Friendly prompts: greetings, compliments, care, catching up, support, invitations, and long heartfelt statements."""

from __future__ import annotations

GREETINGS: list[str] = [
    # GREETINGS - ULTRA SHORT
    "Hey you!",
    "Hi there!",
    "Hello friend!",
    "Howdy!",
    "What's up!",
    "Yo!",
    "Hiya!",
    "Greetings!",
    "Salutations!",
    "Good to see ya!",
    "There you are!",
    "Finally!",
    "Look who it is!",
    "Well well well!",
    "Fancy meeting you here!",
    # GREETINGS - VARIED OPENERS
    "Oh my gosh, it's you!",
    "Wait, is that really you?",
    "No way, I can't believe it!",
    "Get over here and give me a hug!",
    "Stop everything, my favorite person just arrived!",
    "The party can officially start now!",
    "You just made my whole day better!",
    "My heart literally just skipped a beat!",
    "Shut the front door, look who showed up!",
    "Well aren't you a sight for sore eyes!",
    "Just the person I was hoping to run into!",
    "Universe really came through for me today!",
    "This must be my lucky day!",
    "Someone pinch me, is this real?",
    "Best surprise I've had all week!",
    # COMPLIMENTS - APPEARANCE
    "You're absolutely glowing today!",
    "That outfit is incredible on you!",
    "Looking sharp as always!",
    "You're radiating positive energy!",
    "Someone's looking extra fabulous!",
    "Did you do something different? You look amazing!",
    "Wow, you clean up nice!",
    "Stunning as ever, I see!",
    "You've got that glow going on!",
    "Looking like a million bucks!",
    "That color is perfect on you!",
    "Your smile just lit up the whole room!",
    "You're giving main character energy today!",
    "Serving looks as usual!",
    "You're an absolute vision!",
    # COMPLIMENTS - PERSONALITY
    "You're such a ray of sunshine!",
    "Your energy is absolutely infectious!",
    "Being around you always lifts my spirits!",
    "You have the kindest soul!",
    "Your laugh is my favorite sound!",
    "You make everything more fun!",
    "The world needs more people like you!",
    "You're genuinely one of the good ones!",
    "Your positivity is contagious!",
    "You bring out the best in everyone!",
    "Such a beautiful soul you have!",
    "Your warmth is unmatched!",
    "You're the human equivalent of a warm hug!",
    "Everyone's mood improves when you walk in!",
    "You're pure gold, you know that?",
    # EXPRESSING CARE - SHORT
    "Been thinking about you!",
    "You've been on my mind!",
    "Missed your face!",
    "Counting the days until we hang out!",
    "My week feels incomplete without you!",
    "Nobody gets me like you do!",
    "You're irreplaceable, truly!",
    "Can't imagine life without you!",
    "You mean the world to me!",
    "Grateful for you every single day!",
    "Lucky to have you in my corner!",
    "You're stuck with me forever!",
    "Cherish every moment with you!",
    "My life is better because of you!",
    "You're family to me!",
    # CATCHING UP - QUESTIONS
    "What's been happening in your world?",
    "Fill me in on everything!",
    "Spill the tea, what's new?",
    "What adventures have you been on?",
    "Catch me up on your life!",
    "What exciting things are you working on?",
    "Any big news to share?",
    "How's life treating you lately?",
    "What's keeping you busy these days?",
    "Any fun plans coming up?",
    "What's the latest and greatest?",
    "Anything exciting on the horizon?",
    "How's your heart doing?",
    "What's bringing you joy lately?",
    "How's everything on your end?",
    # OFFERING SUPPORT - SHORT
    "I'm here for you, always!",
    "Whatever you need, I got you!",
    "You can count on me!",
    "I've got your back no matter what!",
    "Lean on me anytime!",
    "My door is always open for you!",
    "You never have to face anything alone!",
    "I'm just a call away!",
    "Ready to support you however I can!",
    "Your problems are my problems!",
    "We're in this together!",
    "I'll always show up for you!",
    "Consider me your biggest cheerleader!",
    "I believe in you completely!",
    "You've got a friend in me!",
    # APPRECIATION - SHORT
    "Thank you for being you!",
    "Appreciate you so much!",
    "You're the absolute best!",
    "So grateful our paths crossed!",
    "Blessed to know you!",
    "You're a true gem!",
    "One in a million, that's you!",
    "Can't thank you enough!",
    "You've been amazing!",
    "Truly appreciate everything!",
    "You're a lifesaver!",
    "Don't know how to repay you!",
    "You went above and beyond!",
    "Means more than words can say!",
    # INVITATIONS & PLANS
    "Let's grab coffee soon!",
    "When can we hang out?",
    "We need to catch up properly!",
    "Dinner's on me next time!",
    "Let's plan something fun!",
    "We should do this more often!",
    "Save some time for me this week!",
    "I'm stealing you for lunch soon!",
    "We're long overdue for a hangout!",
    "Mark your calendar, we're doing something!",
    "No excuses, we're meeting up!",
    "Let's make some memories!",
    "Adventure awaits, you in?",
    "Got something fun in mind for us!",
    "Clear your schedule, it's us time!",
    # ENCOURAGEMENT - SHORT
    "You've totally got this!",
    "Believe in yourself like I believe in you!",
    "Nothing can stop you!",
    "You're capable of amazing things!",
    "Go show them what you're made of!",
    "The world is yours for the taking!",
    "You were born for this!",
    "Knock 'em dead out there!",
    "You're going to crush it!",
    "Success is written all over you!",
    "Can't wait to celebrate your wins!",
    "You inspire me every day!",
    "Keep being your awesome self!",
    "Never doubt your brilliance!",
    "You're destined for great things!",
    # REMINISCING
    "Remember that time we laughed until we cried?",
    "Still thinking about our last adventure!",
    "Those memories we made are priceless!",
    "We've had some epic times together!",
    "Our friendship has the best highlights!",
    "Can't believe all we've been through!",
    "We've come so far together!",
    "Throwback to when we first met!",
    "Our stories could fill a book!",
    "We've built something really special here!",
    "The journey with you has been incredible!",
    "So many good times to look back on!",
    "Our friendship is my favorite story!",
    "We've created magic together!",
    "Here's to all our shared adventures!",
    # MEDIUM - VARIED STARTERS
    "Honestly, running into you just completely turned my entire day around, and now everything feels so much better.",
    "Can't even express how much your friendship means to me, you've been such a constant in my life.",
    "Seeing your face always brings the biggest smile to mine, like an instant mood boost every single time.",
    "Your presence alone makes any room feel warmer and more welcoming, it's a genuine gift you have.",
    "Literally was just talking about you earlier today, and here you are, the universe is wild!",
    "Nothing makes me happier than unexpected moments like this, just bumping into my favorite human being.",
    "Already know this conversation is going to be the highlight of my day, you never disappoint me.",
    "Something about your energy just puts me completely at ease, like coming home after a long trip.",
    "Every time we meet, it feels like no time has passed at all, that's rare and special.",
    "Genuinely believe meeting you was one of the best things that's happened in my entire life honestly.",
    "Always leave our hangouts feeling recharged and inspired, you have that effect on people around you.",
    "Miss our random late night conversations about absolutely everything and nothing at the same time, so fun.",
    "Your friendship is the kind that makes everything else in life feel more manageable and less scary.",
    "Swear you get cooler every time I see you, like fine wine just getting better with time.",
    "Nobody else understands my weird humor quite like you do, and that's incredibly rare to find.",
    # MEDIUM - QUESTIONS
    "What have you been up to lately, because I feel like there's so much to catch up on?",
    "How are things going with that project you were so excited about, did it work out well?",
    "When are we finally going to take that trip we've been talking about for literally forever now?",
    "Did you end up trying that restaurant I recommended, or are you still on the fence about it?",
    "What's been making you smile lately, because I love hearing about the good things in your life?",
    "Are you free this weekend, because I have some ideas for what we could do together?",
    "How's your family doing, it's been a minute since I've heard any updates from you about them?",
    "What's the best thing that's happened to you recently, I want to hear all the highlights?",
    "Have you been taking care of yourself, because you know how much I worry about you sometimes?",
    "Is there anything you need right now, because you know I'm always ready to help however I can?",
    "What goals are you working toward these days, I love watching you chase your dreams with passion?",
    "Did that thing you were stressed about work out okay, I've been thinking about it constantly?",
    "When did you become even more amazing than you already were, seriously what's your secret here?",
    "How do you always manage to stay so positive, because I genuinely want to learn from you?",
    "What adventures are on your bucket list, because I might want to tag along for some of them?",
    # MEDIUM - EXCLAMATIONS
    "Stop it right now, you did not just walk in looking that incredible without any warning at all!",
    "Get out of here, I was literally just about to text you when you appeared out of nowhere!",
    "No freaking way, this is the best coincidence that could have possibly happened to me today honestly!",
    "Shut up, you're telling me we've been in the same place this whole time without knowing it!",
    "Oh my goodness, my heart is so full right now just from seeing your beautiful face again!",
    "This is absolutely insane, I manifested this exact moment happening and here you actually are now!",
    "Unbelievable timing, I was having the worst day until you showed up and changed everything around!",
    "Holy moly, look at you being all successful and gorgeous, I'm so incredibly proud of you!",
    "Dreams do come true, I've been hoping to run into you for the longest time ever!",
    "Can't handle how happy I am right now, this moment is literally everything I needed today!",
    "You absolute legend, showing up right when I needed a friendly face the most in my life!",
    "The universe really said I needed this today, and delivered you right to me perfectly on time!",
    "My whole week just got infinitely better the second I saw you walk through that door!",
    "Screaming internally because I'm so excited to see you but trying to play it cool somehow!",
    "Best plot twist ever, I thought today was going to be boring and then you appeared magically!",
    # LONG - HEARTFELT STATEMENTS
    (
        "Every single time we get together, I'm reminded of how lucky I am to have someone like you in my life who "
        "genuinely cares about my happiness."
    ),
    (
        "Our friendship is honestly one of my greatest treasures, and I hope you know how much you mean to me, because "
        "it's truly immeasurable."
    ),
    (
        "The way you light up every room you walk into is something special, and I'm constantly in awe of your "
        "incredible ability to make everyone feel welcome."
    ),
    (
        "Been meaning to tell you that your kindness hasn't gone unnoticed, and I'm grateful every day that the "
        "universe brought you into my life."
    ),
    (
        "Something about the way you carry yourself inspires me to be a better person, and I just want you to know "
        "that you make a real difference."
    ),
    (
        "Life has a funny way of bringing the right people together, and meeting you was definitely one of those meant "
        "to be moments that I cherish deeply."
    ),
    (
        "Can't remember the last time I laughed this hard with anyone else, you have this incredible gift of making "
        "even ordinary moments feel absolutely magical."
    ),
    (
        "Your unwavering support through everything has meant more than you'll ever know, and I'll never be able to "
        "fully express my gratitude to you."
    ),
    (
        "Looking back on all the memories we've created together fills my heart with so much joy, and I can't wait to "
        "make even more with you."
    ),
    (
        "The genuine connection we share is so rare and precious, and I never want to take for granted how special "
        "what we have truly is."
    ),
    (
        "Watching you grow and succeed brings me so much happiness, like I'm witnessing something beautiful unfold, "
        "and I'm honored to be part of your journey."
    ),
    (
        "Your laughter is genuinely one of my favorite sounds in the entire world, it's infectious and always manages "
        "to lift my spirits no matter what."
    ),
    (
        "The comfort I feel in your presence is unlike anything else, like I can be completely myself without any fear "
        "of judgment or pretense."
    ),
    (
        "Our late night conversations have gotten me through some of my toughest times, and I'll always be grateful "
        "for your patience and wisdom during those moments."
    ),
    (
        "Knowing that I have someone like you cheering me on makes all the difference in the world, your support fuels "
        "my confidence every single day."
    ),
]

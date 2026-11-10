"""Name prompts: long examples with names, then technology, streaming, retail, fashion, beauty, and car brands."""

from __future__ import annotations

BRANDS: list[str] = [
    # ADDITIONAL LONG EXAMPLES - STATEMENTS WITH NAMES
    (
        "Jennifer called me this morning to let me know that she's finally moving to Seattle after thinking about it "
        "for years."
    ),
    (
        "Marcus has been teaching English as a second language for over a decade, and he's helped hundreds of students "
        "improve their skills."
    ),
    (
        "Samantha is organizing a surprise birthday party for her mother next weekend, and she's keeping it completely "
        "secret."
    ),
    "Nathan works as a paramedic and regularly saves lives, which makes him one of the most dedicated people I know.",
    (
        "Rebecca has been training for the triathlon since January, and she's determined to finish in the top ten this "
        "year."
    ),
    (
        "Christopher is developing a mobile app that helps people track their spending habits and save money more "
        "effectively."
    ),
    (
        "Vanessa is studying to become a veterinarian because she's passionate about animal welfare and wants to help "
        "pets."
    ),
    (
        "Theodore has been volunteering at the homeless shelter every Sunday for the past three years without missing "
        "a week."
    ),
    "Monica is a talented pastry chef who creates the most beautiful wedding cakes I've ever seen in my life.",
    (
        "Brandon is learning sign language so he can communicate better with his deaf coworker and make her feel more "
        "included."
    ),
    "Stephanie has been working from home for two years now, and she's finally found a good work life balance.",
    "Derek is training to run his first marathon next spring, and he's been following a strict exercise routine.",
    (
        "Amanda runs a small bookstore downtown that has become a favorite gathering place for the local literary "
        "community."
    ),
    (
        "Jonathan is a documentary filmmaker who travels the world telling stories about endangered cultures and "
        "traditions."
    ),
    "Kristina has been saving money for years to open her own yoga studio, and she's finally ready to make it happen.",
    # ADDITIONAL LONG EXAMPLES - QUESTIONS WITH NAMES
    "Did you hear that Nicole got engaged last weekend, and she's planning the wedding for next summer already?",
    "Have you spoken to Gregory recently, because I heard he's thinking about changing careers completely?",
    "Can you believe that Patricia won the lottery last month, and she's donating half of it to charity?",
    "Do you know if Kenneth is still looking for an apartment, because my neighbor is moving out soon?",
    "Have you met Victoria yet, because she just moved into the building and seems really friendly?",
    "Did Thomas mention anything about the company restructuring, because I'm worried about my position?",
    "Can you tell me where Christina works now, because I want to send her an invitation to the reunion?",
    "Do you remember if Daniel said he was coming to the barbecue, because I need to know how much food to prepare?",
    "Have you heard anything from Margaret lately, because she hasn't responded to my messages in weeks?",
    "Did you know that Anthony is actually trilingual, and he learned his third language just last year?",
    "Can you ask Catherine if she's free for coffee next Tuesday, because I'd love to catch up with her?",
    "Do you think Steven would be interested in joining our book club, because he reads constantly?",
    "Have you talked to Elizabeth about the project deadline, because I'm not sure if she's aware it changed?",
    "Did Richard ever find a new job, because I remember he was interviewing at several places?",
    "Can you believe that Melissa is already a grandmother, because she looks so young for her age?",
    # ADDITIONAL LONG EXAMPLES - EXCLAMATIONS WITH NAMES
    "I can't believe Jessica is already graduating from medical school, it feels like just yesterday she started!",
    "Andrew just told me he's getting married next month, and I had no idea he was even dating anyone!",
    "Lauren has been promoted to vice president, which is incredible because she's only thirty years old!",
    "Timothy surprised everyone by announcing he's moving to Japan to teach English for a year!",
    "Michelle just ran her first half marathon in under two hours, and she only started running six months ago!",
    "Raymond won the company's innovation award for his brilliant idea that saved thousands of dollars!",
    "Danielle is expecting twins, which is so exciting because she's been wanting to start a family for years!",
    "Patrick just got accepted into Harvard Law School, and everyone is so proud of his achievement!",
    "Angela's art exhibition was a huge success, and she sold every single piece on opening night!",
    "Scott just announced that he's opening his own restaurant after working as a chef for fifteen years!",
    "Kimberly has been selected to speak at the international conference, which is such an honor!",
    "Vincent finished writing his novel after working on it for five years, and it's finally getting published!",
    "Heather just ran into her college roommate at the airport, and they hadn't seen each other in twenty years!",
    "Dennis has been selected for the Olympic trials, which is the culmination of years of hard work!",
    "Dorothy's charity raised over a million dollars this year, making it their most successful fundraiser ever!",
    # ADDITIONAL LONG EXAMPLES - MIXED CONTEXTS WITH NAMES
    "When I first met Gabriella at the conference, I never imagined we would become such close friends over the years.",
    "Ryan has this incredible ability to make everyone around him feel comfortable, which is why he's so popular.",
    "Laura spent three months backpacking through Southeast Asia, and she came back with amazing stories to tell.",
    "Jeffrey has been my mentor since I started this job, and I owe so much of my success to his guidance.",
    "Cynthia is the kind of person who remembers everyone's birthday and always sends a thoughtful card or gift.",
    "Roger used to be my neighbor before he moved across the country, and I still miss our weekly chess games.",
    "Deborah has been studying French for years, and she's finally fluent enough to hold conversations.",
    "Keith works the night shift at the hospital, but he still finds time to coach his son's soccer team.",
    "Sharon is renovating her grandmother's old house, turning it into a beautiful bed and breakfast.",
    "Gerald has the most extensive vinyl record collection I've ever seen, with over three thousand albums.",
    # NEW BRAND NAMES - TECH AND SOFTWARE
    (
        "We organized the entire product roadmap in Notion and now the whole team can see what's coming up for the "
        "next quarter."
    ),
    "The design team spent all week in Figma creating those beautiful mockups for the new mobile app launch.",
    "Our project manager loves using Trello because she can see at a glance which tasks are stuck in review.",
    (
        "Ever since we switched to Asana for task management, our team meetings have become so much more productive "
        "and focused."
    ),
    "The developers filed seventeen bug reports in Jira this morning alone, and we still have to triage all of them.",
    "All of our technical documentation lives in Confluence now, which makes onboarding new engineers so much easier.",
    (
        "We did a massive brainstorming session on Miro with sticky notes and diagrams, and it actually felt like "
        "being in person."
    ),
    (
        "The marketing team built an entire customer database in Airtable that connects to all our other tools "
        "automatically."
    ),
    "I shared the entire project folder through Dropbox so everyone on the team can access the files from anywhere.",
    "My company uses OneDrive for everything, so I have all my documents synced across my laptop, tablet, and phone.",
    (
        "We store all our client presentations in Box because it has better enterprise security features than the "
        "alternatives."
    ),
    (
        "The video file was too large for email, so I had to WeTransfer it to the client and hope they check their "
        "spam folder."
    ),
    "I've been using Evernote to organize my research notes for years, and I have thousands of clippings saved there.",
    (
        "During meetings I take all my notes in OneNote because it syncs instantly and I can search through everything "
        "later."
    ),
    (
        "My personal productivity system is built entirely around Todoist, with projects for work, home, and side "
        "projects."
    ),
    "The entire company workflow runs through Monday dot com, from sales pipelines to product development sprints.",
    (
        "Our remote team stays connected through Basecamp, where we post updates, share files, and have threaded "
        "discussions."
    ),
    "We migrated all our projects to ClickUp last month and the customization options are honestly overwhelming.",
    (
        "Instead of endless email chains about scheduling, we just send a Calendly link and let people pick their own "
        "time."
    ),
    "We needed to find a time that worked for fifteen people across four time zones, so we created a Doodle poll.",
    # NEW BRAND NAMES - STREAMING AND ENTERTAINMENT
    "I spent the entire weekend binge watching that new crime documentary series on Hulu and now I have trust issues.",
    (
        "The kids have watched Frozen on Disney Plus approximately four hundred times and I know every single word by "
        "heart."
    ),
    "That new prestige drama on HBO Max has been getting incredible reviews, so I'm adding it to my watchlist tonight.",
    "Paramount Plus has all the old Star Trek series, so my dad finally cut the cord and streams everything now.",
    "I was trying to watch the Olympics on Peacock but the app kept buffering during the most important moments.",
    (
        "Apple TV Plus has some of the best production quality I've ever seen, even if their library is still pretty "
        "small."
    ),
    (
        "We subscribed to Prime Video mainly for the free shipping, but now we actually watch more shows there than "
        "anywhere else."
    ),
    "My roommate is obsessed with anime and watches Crunchyroll for like six hours every single day without fail.",
    "I prefer the dubbed versions of anime, so I usually check Funimation first before looking anywhere else.",
    "He streams his gameplay on Twitch every night and has somehow built a community of ten thousand loyal followers.",
    (
        "Back when Mixer was still around, some streamers got paid millions to switch platforms, and then it shut down "
        "anyway."
    ),
    (
        "Independent filmmakers often upload their short films to Vimeo because the video quality is better than other "
        "platforms."
    ),
    (
        "That viral video from last week is still circulating on Dailymotion even though it got removed from "
        "everywhere else."
    ),
    "She uploaded her first song to SoundCloud three years ago and now she's touring with a major record label.",
    (
        "Underground artists sell their music directly to fans on Bandcamp, where they actually get to keep most of "
        "the money."
    ),
    (
        "Audiophiles swear by Tidal because of the lossless audio quality, even though most people can't hear the "
        "difference."
    ),
    "I discovered so many great international artists through Deezer's recommendation algorithm when I lived abroad.",
    "My parents still use Pandora and just let it play the same station all day while they work in the garden.",
    "I listen to iHeartRadio during my commute because they have live radio stations from my hometown.",
    (
        "I've been listening to audiobooks on Audible during my commute and I've finished more books this year than "
        "ever before."
    ),
    # NEW BRAND NAMES - SHOPPING AND RETAIL
    "We furnished our entire apartment through Wayfair and the delivery guys probably know our address by heart now.",
    "I found the exact same lamp on Overstock for half the price, so always compare before you buy anything.",
    "Zappos has the best return policy for shoes, so I ordered five pairs and sent back the four that didn't fit.",
    "My sister works at Nordstrom and gets an amazing employee discount, so she does all my fancy shopping for me.",
    "Macy's has their big sale coming up next week, and I've been waiting months to buy that kitchen appliance.",
    "She only shops at Bloomingdale's for special occasions because everything there is ridiculously overpriced.",
    "I can't believe people actually pay full price at Saks when you can find the same designer stuff at outlets.",
    (
        "My grandmother has been a loyal Neiman Marcus customer for fifty years and they send her birthday flowers "
        "every year."
    ),
    (
        "I stacked three different Kohl's coupons and got that comforter set for basically nothing, which felt like a "
        "heist."
    ),
    "JCPenney was where my mom always took us shopping for back to school clothes when we were kids.",
    "We registered for our wedding at Bed Bath and Beyond and received approximately seventeen different blenders.",
    "All of our kitchen gadgets come from Williams Sonoma because my husband is obsessed with cooking equipment.",
    "The aesthetic of everything at Crate and Barrel is exactly my style, minimalist and modern but still warm.",
    "We bought our first couch from Pottery Barn when we moved in together, and we still have it ten years later.",
    "West Elm has beautiful furniture but everything takes three months to arrive, so plan ahead.",
    (
        "That Restoration Hardware catalog is basically a coffee table book at this point, with all those lifestyle "
        "photos."
    ),
    "We spent an entire Saturday at IKEA and came home with a car full of flat pack furniture and Swedish meatballs.",
    "My dad practically lives at Home Depot on weekends, always working on some new project around the house.",
    "The contractor said to pick up the materials at Lowe's because they have better lumber selection in our area.",
    "Menards is a Midwest thing, so my friends from the coasts have never even heard of it.",
    # NEW BRAND NAMES - FASHION AND APPAREL
    "Everything at Zara looks like it came straight off a runway in Paris, but at prices normal people can afford.",
    (
        "H and M does those designer collaborations where people literally camp outside the store to get the limited "
        "pieces."
    ),
    "I love Uniqlo for basics because their quality is incredible and the clothes actually last for years.",
    "When I was in college, Forever 21 was where I bought all my going out clothes because everything was so cheap.",
    "Urban Outfitters has that specific aesthetic that every college apartment in America seems to have.",
    "My mom shops exclusively at Anthropologie and her house looks like a bohemian dream from a magazine.",
    "Free People dresses are my weakness, even though I can't really afford them and have nowhere to wear them.",
    "Since I started working from home, I basically live in Lululemon leggings and haven't worn real pants in months.",
    "Athleta makes workout clothes that actually fit women's bodies instead of just shrinking men's designs.",
    "He's one of those sneakerheads who waits in line for hours whenever Nike drops a new limited edition shoe.",
    "The new Adidas collaboration with that designer sold out in literally three minutes online.",
    "My running coach swears by Puma for track and field because of their lighter weight and better grip.",
    "I've been wearing the same pair of Reebok classics since high school and they're finally falling apart.",
    "Podiatrists apparently love New Balance because they have better arch support than most athletic shoes.",
    (
        "Under Armour started as a compression shirt company and now they sponsor some of the biggest athletes in the "
        "world."
    ),
    "That North Face puffer jacket is basically the unofficial uniform of everyone who lives in a cold climate city.",
    "Patagonia customers are weirdly loyal, like it's a lifestyle brand and not just outdoor clothing.",
    "My Columbia rain jacket has survived five years of Pacific Northwest weather and still looks brand new.",
    "We geared up for our camping trip at REI and the staff there actually knew what they were talking about.",
    "My grandparents have been ordering from L.L. Bean since before I was born and they still get the catalog.",
    # NEW BRAND NAMES - BEAUTY AND PERSONAL CARE
    "I spent two hours in Sephora trying on different lipstick shades and walked out with way more than I planned.",
    "The Ulta near my house is dangerous because I always go in for one thing and leave with a full bag.",
    "Makeup artists on film sets almost always use MAC because the pigments photograph so beautifully on camera.",
    "My dermatologist recommended Clinique because their products are formulated for sensitive skin types.",
    "Estée Lauder has been around since my grandmother's generation and the quality has stayed consistently excellent.",
    "That Lancôme mascara is expensive but it makes my lashes look absolutely incredible without clumping.",
    "Maybelline proves you don't need to spend a fortune to get drugstore makeup that actually performs well.",
    "L'Oréal has some of the best hair color formulations, which is why so many salons use their professional line.",
    "I've been wearing the same Revlon lipstick shade for twenty years because they never discontinued it.",
    "CoverGirl was the first makeup brand I ever used, back when my mom let me wear lip gloss to school.",
    "NYX has the best affordable eyeshadow palettes with colors that actually show up on darker skin tones.",
    "Rihanna's Fenty Beauty line revolutionized the industry by launching with forty different foundation shades.",
    "Glossier built their entire brand on Instagram with that natural, dewy, no makeup makeup aesthetic.",
    "The Ordinary sells clinical skincare ingredients at drugstore prices, which disrupted the whole beauty industry.",
    (
        "Drunk Elephant products are so popular that people actually call their skincare routine the Drunk Elephant "
        "smoothie."
    ),
    "Tatcha is inspired by Japanese beauty rituals and their rice enzyme powder is absolutely incredible.",
    "My mom has used Olay religiously since she was thirty, and honestly her skin looks amazing for her age.",
    "Neutrogena is what every dermatologist recommends as a basic, affordable, no nonsense skincare brand.",
    "Cetaphil is so gentle that they recommend it for babies, which is why I use it on my sensitive skin.",
    "CeraVe went viral on TikTok and now it's constantly sold out at every drugstore in my neighborhood.",
    # NEW BRAND NAMES - AUTOMOTIVE AND TRANSPORTATION
    "I took a Lyft to the airport because parking there for a week would have cost more than the ride itself.",
    "We rented a convertible from Hertz for our road trip down the Pacific Coast Highway and it was worth every penny.",
    "Enterprise picked us up from the mechanic while our car was being repaired, which was incredibly convenient.",
    "We needed a van for the move, so we booked one through Budget and returned it the same day.",
    "Avis had the only available rental car at the airport, so we paid way more than we should have.",
    "National has that Emerald Club thing where you can just pick any car in the aisle, which saves so much time.",
    "I rented a neighbor's car through Turo for the weekend and it was half the price of a traditional rental.",
    "Getaround lets you rent cars by the hour, which is perfect for quick errands when you don't own a car.",
    "We use Zipcar for grocery runs because it's cheaper than owning a car in the city with parking costs.",
    "My brother bought his truck from CarMax because he didn't want to deal with negotiating at a dealership.",
    "Carvana literally delivered the car to our driveway and we had seven days to decide if we wanted to keep it.",
    "I spent hours on AutoTrader comparing prices before I even stepped foot in a dealership.",
    "According to Kelley Blue Book, our trade in is worth way less than we thought, which is disappointing.",
    "The Edmunds review said this model has transmission problems, so I'm looking at other options now.",
    "CarGurus shows you whether you're getting a good deal compared to similar cars in your area.",
    "My neighbor just got a Tesla and won't stop talking about how he never has to go to a gas station anymore.",
    "Ford has been making trucks for over a century, and the F 150 is still the best selling vehicle in America.",
    "My dad has driven nothing but Chevrolet his entire life and refuses to even consider other brands.",
    "Toyota has a reputation for reliability that's so strong, their used cars hold their value incredibly well.",
    "We've had our Honda Civic for fifteen years and it still runs perfectly with just regular maintenance.",
]

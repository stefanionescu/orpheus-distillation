"""Name prompts with fictional names, then longer sentences with names."""

from __future__ import annotations

FICTIONAL: list[str] = [
    # FICTIONAL NAMES
    "It's giving very Voldemort vibes.",
    "Who do you think you are, Batman?",
    "That's so Harry Potter.",
    "She's acting like Hermione.",
    "He thinks he's Superman.",
    "They're channeling Wonder Woman.",
    "I feel like Spiderman.",
    "She's got that Catwoman energy.",
    "He's being such a Joker.",
    "They're acting like the Avengers.",
    "That's very Iron Man.",
    "She's got Captain America vibes.",
    "He's being a Hulk.",
    "They're channeling Thor.",
    "I feel like Black Widow.",
    "She's acting like Loki.",
    "He thinks he's Doctor Strange.",
    "They're being like the Guardians.",
    "That's so Star Wars.",
    "She's got Darth Vader energy.",
    "He's being such a Yoda.",
    "They're acting like Luke Skywalker.",
    "I feel like Princess Leia.",
    "She's channeling Han Solo.",
    "He thinks he's Obi Wan.",
    "They're being like Anakin.",
    "That's very Game of Thrones.",
    "She's got Daenerys vibes.",
    "He's acting like Jon Snow.",
    "They're channeling Tyrion.",
    "I feel like Arya Stark.",
    "She's being such a Cersei.",
    "He thinks he's Ned Stark.",
    "They're acting like the Starks.",
    "That's so Breaking Bad.",
    "She's got Walter White energy.",
    "He's being such a Jesse.",
    "They're channeling Saul Goodman.",
    "I feel like Mike Ehrmantraut.",
    "She's acting like Gus Fring.",
    "He thinks he's Hank Schrader.",
    "They're being like Skyler.",
    "That's very The Office.",
    "She's got Michael Scott vibes.",
    "He's acting like Dwight.",
    "They're channeling Jim Halpert.",
    "I feel like Pam Beesly.",
    "She's being such a Stanley.",
    "He thinks he's Kevin.",
    "They're acting like Angela.",
    "That's so Friends.",
    "She's got Rachel energy.",
    "He's being such a Ross.",
    "They're channeling Monica.",
    "I feel like Chandler.",
    "She's acting like Joey.",
    "He thinks he's Phoebe.",
    "They're being like the Friends.",
    "That's very Seinfeld.",
    "She's got Jerry vibes.",
    "He's acting like George.",
    "They're channeling Elaine.",
    "I feel like Kramer.",
    "She's being such a Newman.",
    "He thinks he's Jerry.",
    "They're acting like the Seinfeld crew.",
    "That's so The Simpsons.",
    "She's got Homer energy.",
    "He's being such a Bart.",
    "They're channeling Marge.",
    "I feel like Lisa.",
    "She's acting like Maggie.",
    "He thinks he's Ned Flanders.",
    "They're being like Mr. Burns.",
    "That's very South Park.",
    "She's got Cartman vibes.",
    "He's acting like Stan.",
    "They're channeling Kyle.",
    "I feel like Kenny.",
    "She's being such a Butters.",
    "He thinks he's Randy.",
    "They're acting like the South Park kids.",
    "That's so Rick and Morty.",
    "She's got Rick energy.",
    "He's being such a Morty.",
    "They're channeling Summer.",
    "I feel like Beth.",
    "She's acting like Jerry.",
    "He thinks he's Mr. Poopybutthole.",
    "They're being like the Smiths.",
    "That's very Family Guy.",
    "She's got Peter vibes.",
    "He's acting like Stewie.",
    "They're channeling Brian.",
    "I feel like Lois.",
    "She's being such a Meg.",
    "He thinks he's Chris.",
    "They're acting like the Griffins.",
    "That's so Futurama.",
    "She's got Fry energy.",
    "He's being such a Bender.",
    "They're channeling Leela.",
    "I feel like Zoidberg.",
    "She's acting like Amy.",
    "He thinks he's Hermes.",
    "They're being like the Planet Express crew.",
    # LONGER WITH NAMES
    "I've known Sarah for over ten years now, and she's one of the most reliable people I've ever met.",
    "Michael called me yesterday to tell me about his new job opportunity at the tech startup downtown.",
    "Emma has been working at the hospital for three years, and she absolutely loves helping people every day.",
    "David moved to New York last month because he got a promotion at his company's headquarters there.",
    "Sophia loves reading books so much that she finishes at least two novels every single week without fail.",
    "James plays guitar really well, and he's been practicing every day since he was twelve years old.",
    "Olivia is coming over tonight for dinner, and I'm really excited to catch up with her after so long.",
    "William has three children who are all very talented in different areas like music, sports, and academics.",
    "Isabella speaks four languages fluently, which makes her perfect for her job as an international translator.",
    "Benjamin is a great cook who can make almost any dish you can imagine, from Italian to Asian cuisine.",
    "Mia just got a promotion at work, and everyone is so proud of her because she really deserves it.",
    "Lucas moved to California last year to pursue his dream of becoming a professional actor in Hollywood.",
    "Charlotte is studying medicine at the university, and she wants to become a pediatrician when she graduates.",
    "Henry works as an engineer at a major tech company, and he's been there for almost five years now.",
    "Amelia loves traveling the world, and she's visited over thirty different countries in the past decade.",
    "Alexander is my older brother who always looks out for me, even though we don't see each other often.",
    "Harper writes poetry in her spare time, and she's actually published a few pieces in literary magazines.",
    "Mason is training for a marathon that's happening next month, and he runs ten miles every single day.",
    "Evelyn teaches at the university where she's been a professor for fifteen years, specializing in history.",
    (
        "Priya has been working as a data scientist for the past three years, and she's developed several machine "
        "learning models that are now being used in production."
    ),
    (
        "Ahmed moved to Toronto from Cairo two years ago to pursue better career opportunities, and he's already been "
        "promoted twice at his engineering firm."
    ),
    (
        "Yuki is studying marine biology at the university because she's passionate about ocean conservation and wants "
        "to help protect endangered sea creatures."
    ),
    (
        "Fatima has been volunteering at the local food bank every Saturday morning for the past year, helping "
        "distribute meals to families in need throughout the community."
    ),
    (
        "Diego started his own landscaping business six months ago, and he's already hired three employees because the "
        "demand for his services has been overwhelming."
    ),
    (
        "Aisha is a talented makeup artist who specializes in bridal looks, and she's booked for weddings every "
        "weekend for the next six months straight."
    ),
    (
        "Raj has been teaching physics at the university for over fifteen years, and he's published numerous research "
        "papers on quantum mechanics in prestigious journals."
    ),
    (
        "Hassan works as a project manager for a construction company, and he's currently overseeing the development "
        "of a new residential complex downtown."
    ),
    (
        "Mei is learning how to play the cello because she's always been fascinated by orchestral music, and she "
        "practices for three hours every evening after work."
    ),
    (
        "Carlos moved back to Buenos Aires from Madrid last year to start a family, and he's been working as a "
        "financial consultant for several local businesses."
    ),
    (
        "Noor is a speech therapist who works with children who have communication disorders, and she's helped dozens "
        "of kids improve their language skills over the years."
    ),
    (
        "Kenji has been practicing judo since he was five years old, and he recently won a regional championship after "
        "years of dedicated training and discipline."
    ),
    (
        "Layla is writing a memoir about her experiences immigrating to Canada as a teenager, and she hopes to inspire "
        "other young immigrants with her story."
    ),
    (
        "Vikram is a software architect who designs complex systems for financial institutions, and he's known for his "
        "innovative solutions to challenging technical problems."
    ),
    (
        "Amara works as a community organizer helping residents advocate for better public services, and she's "
        "successfully lobbied for several improvements to local infrastructure."
    ),
    (
        "Takeshi is learning how to brew craft beer because he wants to open his own microbrewery that combines "
        "traditional Japanese flavors with modern brewing techniques."
    ),
    (
        "Zara has been studying urban planning for the past five years, and she's already worked on several city "
        "development projects that have won design awards."
    ),
    (
        "Mohammed is a structural engineer who specializes in earthquake resistant buildings, and he's currently "
        "working on a major skyscraper project in a seismic zone."
    ),
    (
        "Ananya is a meditation instructor who teaches mindfulness classes at three different wellness centers, and "
        "she's helped hundreds of people reduce their stress levels."
    ),
]

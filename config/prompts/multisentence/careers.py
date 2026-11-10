"""Multi-sentence prompts: natural talk about occupations, food, travel, technology, and health."""

from __future__ import annotations

CAREERS: list[str] = [
    # OCCUPATIONAL CONVERSATIONS - NATURAL
    (
        "The anesthesiologist explained the procedure thoroughly beforehand. She made sure I understood all the "
        "potential risks involved."
    ),
    "Our sommelier recommended a beautiful Burgundy with the lamb. His pairing suggestion was absolutely spot on.",
    "The archaeologist uncovered a significant pottery fragment today. It could date back nearly three thousand years.",
    (
        "My physical therapist assigned new exercises for my knee. The rehabilitation process is slow but definitely "
        "progressing."
    ),
    (
        "The marine biologist tagged another great white shark yesterday. Her research on migration patterns is "
        "groundbreaking work."
    ),
    "Our accountant found several deductions we had overlooked. We're getting a much larger refund than expected.",
    (
        "The ornithologist identified a rare warbler in the preserve. Birdwatchers from across the state are arriving "
        "to see it."
    ),
    "My orthodontist says I only need braces for eighteen months. The invisible aligners make it much more manageable.",
    (
        "The curator is organizing a retrospective of the artist's work. The exhibition will feature pieces never "
        "shown publicly before."
    ),
    (
        "Our contractor estimates the renovation will take six weeks. That's assuming there are no unexpected "
        "complications with permits."
    ),
    (
        "The epidemiologist is tracking the outbreak to its source. Contact tracing has been incredibly thorough and "
        "methodical."
    ),
    (
        "My allergist recommended immunotherapy for my seasonal symptoms. The shots should reduce my sensitivity over "
        "time."
    ),
    (
        "The paleontologist discovered a nearly complete fossil skeleton. It's one of the best preserved specimens "
        "ever found here."
    ),
    (
        "Our landscape architect designed a beautiful native plant garden. It requires much less water and maintenance "
        "than traditional lawns."
    ),
    (
        "The forensic analyst matched the fingerprints to the suspect. The evidence should be admissible in court "
        "proceedings."
    ),
    "My podiatrist fitted me for custom orthotic insoles. The arch support has made a tremendous difference already.",
    (
        "The astrophysicist published her findings on dark matter. The scientific community is still debating the "
        "implications."
    ),
    (
        "Our nutritionist created a meal plan tailored to my goals. She emphasized whole foods and balanced "
        "macronutrients."
    ),
    (
        "The archivist cataloged hundreds of historical documents today. Some letters date back to the revolutionary "
        "war era."
    ),
    (
        "My optometrist detected early signs of glaucoma. We're starting treatment immediately to prevent further "
        "progression."
    ),
    # FOOD & CULINARY - NATURAL
    "The risotto was perfectly al dente with a creamy consistency. The chef added a generous amount of aged parmesan.",
    "This sourdough has an incredible tangy flavor and chewy texture. The fermentation process took over three days.",
    "The miso glaze on the black cod was absolutely divine. It had just the right balance of sweet and umami.",
    (
        "We tried authentic pad thai from a street vendor in Bangkok. Nothing I've had since has compared to that "
        "experience."
    ),
    (
        "The charcuterie board featured prosciutto aged for twenty four months. The paper thin slices melted on the "
        "tongue."
    ),
    (
        "Her grandmother's goulash recipe has been passed down for generations. The paprika she uses is imported from "
        "Hungary."
    ),
    "The brioche was incredibly buttery and light as air. Perfect for making French toast on lazy Sunday mornings.",
    (
        "They dry age their steaks for a minimum of forty five days. The flavor concentration is remarkable and worth "
        "the wait."
    ),
    "The tahini dressing on this falafel is perfectly balanced. There's a hint of lemon that brightens everything up.",
    "We harvested our first batch of heirloom tomatoes yesterday. The variety of colors and flavors is incredible.",
    "The espresso had notes of dark chocolate and cherry. The barista's extraction timing was absolutely impeccable.",
    "This aged gouda has those lovely crystalline bits throughout. It pairs wonderfully with fig jam and crusty bread.",
    (
        "The broth for the pho had been simmering for eighteen hours. You could taste every aromatic spice in each "
        "spoonful."
    ),
    "Her croissants are shatteringly crisp with hundreds of delicate layers. She trained at a patisserie in Paris.",
    "The ceviche was incredibly fresh with just the right acidity. The lime juice had perfectly cured the snapper.",
    "They roast their own coffee beans on site every morning. The aroma alone is worth the visit to this cafe.",
    "The aioli was infused with roasted garlic and fresh herbs. It elevated the simple sandwich to something special.",
    (
        "We're trying to eat more plant based meals this month. The lentil bolognese was surprisingly hearty and "
        "satisfying."
    ),
    (
        "The gelato here is made fresh daily with local ingredients. The pistachio flavor is their signature and "
        "bestseller."
    ),
    (
        "His knife skills are extraordinary after culinary school training. The julienne cuts are perfectly uniform "
        "every time."
    ),
    # TRAVEL & PLACES - NATURAL
    (
        "The cobblestone streets of Prague were magical at night. The medieval architecture made us feel transported "
        "back in time."
    ),
    "Our ryokan in Kyoto had traditional tatami mat flooring. Sleeping on futons took some getting used to initially.",
    (
        "The fjords of Norway were more stunning than any photograph. The scale of those glacial valleys is "
        "incomprehensible."
    ),
    (
        "We took a gondola through the canals of Venice at sunset. The city has a melancholy beauty that's hard to "
        "describe."
    ),
    (
        "The ancient ruins of Machu Picchu exceeded all expectations. The Inca engineering at that altitude is truly "
        "remarkable."
    ),
    (
        "Our safari guide spotted a leopard resting in an acacia tree. Without his trained eye, we never would have "
        "noticed it."
    ),
    "The night market in Taipei was a sensory overload. So many unfamiliar foods and fascinating smells to explore.",
    "We watched the sunrise over Angkor Wat at dawn. The temple silhouette against the orange sky was unforgettable.",
    "The Amalfi Coast road was terrifying but absolutely worth it. Those cliffside villages are postcard perfect.",
    (
        "Our overnight train from Bangkok to Chiang Mai was an adventure. The sleeper car was surprisingly comfortable "
        "and scenic."
    ),
    "The souk in Marrakech was a labyrinth of colors and textures. We got wonderfully lost for several hours there.",
    (
        "We hiked to the base camp of Everest last spring. The altitude sickness was challenging but the views were "
        "extraordinary."
    ),
    (
        "The Northern Lights in Iceland exceeded our expectations. The green and purple ribbons danced across the "
        "entire sky."
    ),
    (
        "Our cooking class in Tuscany was the highlight of the trip. We learned to make fresh pasta from a local "
        "grandmother."
    ),
    (
        "The Great Barrier Reef is showing signs of coral bleaching. We're grateful we got to dive there before more "
        "degradation."
    ),
    "We rented a houseboat and cruised the backwaters of Kerala. The pace of life there is beautifully unhurried.",
    "The Blue Mosque in Istanbul was breathtakingly ornate inside. The geometric tile patterns seem to go on forever.",
    (
        "Our helicopter tour of the Grand Canyon was spectacular. The scale of that geological wonder is hard to "
        "comprehend."
    ),
    "The terracotta warriors in Xi'an number over eight thousand. Each face is uniquely detailed and individual.",
    "We attended a traditional tea ceremony in a Kyoto temple. The ritualized movements were meditative and calming.",
    # TECHNOLOGY & MODERN LIFE - NATURAL
    (
        "The algorithm keeps suggesting videos I've already watched. The recommendation system seems to be stuck in a "
        "loop."
    ),
    "My phone's battery has been draining much faster lately. I think the latest software update caused some issues.",
    "The wireless charging pad is so much more convenient now. I don't have to fumble with cables before bed anymore.",
    (
        "Our smart thermostat has reduced our energy bill significantly. It learns our schedule and adjusts "
        "temperatures automatically."
    ),
    "The noise cancelling headphones are worth every penny spent. I can finally focus in this open office environment.",
    "My fitness tracker says I haven't hit my step goal today. I should probably take a walk during my lunch break.",
    (
        "The video call kept freezing at the worst possible moments. Our internet bandwidth couldn't handle all the "
        "participants."
    ),
    "Password managers have made my digital life so much easier. I used to reuse the same weak password everywhere.",
    (
        "The augmented reality app overlays historical images on locations. You can see what buildings looked like "
        "centuries ago."
    ),
    (
        "My ebook reader's battery lasts for weeks between charges. It's perfect for traveling without carrying heavy "
        "books."
    ),
    (
        "The streaming service increased their subscription price again. At this point, cable might actually be "
        "cheaper overall."
    ),
    (
        "Voice assistants have become surprisingly accurate at understanding context. Though sometimes the responses "
        "are hilariously wrong."
    ),
    (
        "The drone footage captured perspectives we couldn't get otherwise. Aerial cinematography has become so "
        "accessible now."
    ),
    (
        "Our security cameras have motion detection and night vision. The peace of mind is definitely worth the "
        "investment."
    ),
    "The podcast app automatically downloads episodes while I sleep. My commute entertainment is always ready to go.",
    "Cloud storage has eliminated my fear of hard drive failures. Everything important is backed up automatically now.",
    (
        "The translation app works offline which is perfect for traveling. It even handles handwritten text and "
        "restaurant menus."
    ),
    "My smartwatch detected an irregular heartbeat last month. The doctor confirmed it was worth getting checked out.",
    (
        "The electric vehicle's range has improved dramatically in newer models. Range anxiety is becoming much less "
        "of an issue."
    ),
    (
        "Two factor authentication adds an extra layer of security online. It's a minor inconvenience for significant "
        "protection."
    ),
    # HEALTH & WELLNESS - NATURAL
    (
        "My chiropractor identified the source of my chronic back pain. Apparently my posture while working has been "
        "terrible."
    ),
    (
        "The meditation app has helped reduce my anxiety significantly. Even just ten minutes daily makes a noticeable "
        "difference."
    ),
    "Her blood pressure has stabilized since changing her diet. Reducing sodium intake had an almost immediate effect.",
    (
        "The physical exam revealed no concerning abnormalities thankfully. All my bloodwork came back within normal "
        "ranges."
    ),
    (
        "Acupuncture has been surprisingly effective for my migraines. I was skeptical initially but the results speak "
        "for themselves."
    ),
    "The sleep study showed I have mild sleep apnea. A CPAP machine should help me get better rest nightly.",
    (
        "My therapist suggested cognitive behavioral techniques for coping. The reframing exercises have been "
        "genuinely helpful."
    ),
    "The antihistamines work well but they make me drowsy. I have to take them before bed to avoid feeling groggy.",
    (
        "Her cholesterol levels improved dramatically with dietary changes. She didn't even need to start medication "
        "after all."
    ),
    (
        "The cortisone injection provided relief within forty eight hours. The inflammation in my knee is finally "
        "subsiding."
    ),
    "Stretching before my runs has prevented so many injuries. I used to skip warmups and paid the price repeatedly.",
    (
        "The genetic screening revealed no markers for hereditary conditions. It was a relief to get those results "
        "back negative."
    ),
    (
        "My vitamin D levels were dangerously low last winter. The supplements have made a noticeable improvement in "
        "my energy."
    ),
    (
        "The elimination diet helped identify my food sensitivities. Turns out dairy was causing most of my digestive "
        "issues."
    ),
    (
        "Her rehabilitation after the surgery is progressing well. The doctors are pleased with her range of motion "
        "improvement."
    ),
    "The vaccination schedule for the trip requires several appointments. Some boosters need to be spaced weeks apart.",
    (
        "Mindful breathing techniques have helped manage my stress levels. I practice them during particularly tense "
        "meetings."
    ),
    (
        "The dermatologist removed a suspicious mole for biopsy. Better to be cautious with anything that changes "
        "appearance."
    ),
    (
        "His resting heart rate has dropped after consistent cardio training. The fitness improvements are measurable "
        "and motivating."
    ),
    (
        "The probiotic supplements have improved my gut health noticeably. My digestion has been much more regular "
        "since starting them."
    ),
]

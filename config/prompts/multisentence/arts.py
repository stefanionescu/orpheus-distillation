"""Multi-sentence prompts: natural talk about music, home life, nature, and education."""

from __future__ import annotations

ARTS: list[str] = [
    # MUSIC & ARTS - NATURAL
    (
        "The symphony's interpretation of the adagio was hauntingly beautiful. The cellist's solo brought tears to "
        "many eyes."
    ),
    (
        "Her brushwork captures light in the most extraordinary way. The impasto technique adds incredible texture and "
        "depth."
    ),
    (
        "The jazz quartet improvised for nearly twenty minutes straight. Their musical communication was telepathic "
        "and seamless."
    ),
    (
        "His baritone voice has incredible warmth and resonance. The acoustics in that cathedral made it even more "
        "powerful."
    ),
    (
        "The choreography seamlessly blended classical ballet with contemporary movement. The dancers made the "
        "transitions look effortless."
    ),
    (
        "That documentary about the street artist changed my perspective entirely. The social commentary in their work "
        "is profound."
    ),
    (
        "The gallery's new installation uses light and shadow brilliantly. You have to walk through it to fully "
        "appreciate the effect."
    ),
    "Her poetry reading was intimate and deeply moving. You could hear a pin drop in that crowded bookshop.",
    "The film's cinematography deserved every award it received. Each frame was composed like a Renaissance painting.",
    (
        "The conductor's tempo choices were unconventional but effective. He brought out nuances I'd never noticed in "
        "the piece before."
    ),
    (
        "That ceramic artist has been perfecting her glaze techniques for decades. The depth of color she achieves is "
        "remarkable."
    ),
    (
        "The playwright explores themes of identity and belonging beautifully. The dialogue feels authentic and "
        "emotionally resonant."
    ),
    (
        "His guitar fingerpicking style is technically brilliant yet soulful. You can hear the Delta blues influences "
        "throughout."
    ),
    (
        "The museum's restoration of the fresco revealed hidden details. Centuries of grime had obscured the original "
        "vibrant colors."
    ),
    (
        "That indie album has been on constant rotation for weeks. The lyrics are poetic without being pretentious or "
        "obscure."
    ),
    (
        "The sculptor works exclusively with reclaimed materials now. Each piece tells a story about consumption and "
        "waste."
    ),
    (
        "Her soprano range is truly extraordinary and seemingly effortless. The coloratura passages were executed "
        "flawlessly."
    ),
    (
        "The theater company's immersive production was unlike anything traditional. Audience members became part of "
        "the narrative itself."
    ),
    (
        "That photographer's black and white portraits are incredibly intimate. She captures vulnerability in her "
        "subjects beautifully."
    ),
    (
        "The string quartet's rendition of that folk song was moving. They added subtle harmonies that enhanced the "
        "original melody."
    ),
    # HOME & DOMESTIC - NATURAL
    (
        "The grout between the bathroom tiles needs to be resealed. Water has been seeping through and causing mold "
        "issues."
    ),
    (
        "Our new memory foam mattress has transformed my sleep quality. The old spring mattress was causing terrible "
        "back pain."
    ),
    "The herb garden on the windowsill is thriving nicely. Fresh basil and rosemary make such a difference in cooking.",
    (
        "We finally replaced the ancient water heater last week. The new tankless unit provides endless hot water "
        "instantly."
    ),
    (
        "The hardwood floors need to be refinished next summer. Years of foot traffic have worn through the protective "
        "coating."
    ),
    (
        "Our composting bin has reduced our kitchen waste dramatically. The garden is benefiting from the nutrient "
        "rich soil amendment."
    ),
    (
        "The ceiling fan makes such a difference in the bedroom. We've been able to reduce our air conditioning usage "
        "significantly."
    ),
    "The coat of paint really brightened up the living room. The previous beige walls made the space feel so dreary.",
    "Our dishwasher finally gave out after fifteen years of service. The new model is much quieter and more efficient.",
    (
        "The blackout curtains have helped regulate the bedroom temperature. Plus the morning sunlight doesn't wake us "
        "up anymore."
    ),
    (
        "We're converting the spare bedroom into a home office. Working from home requires a dedicated and organized "
        "space."
    ),
    (
        "The leaky faucet was wasting more water than we realized. A simple washer replacement fixed the problem "
        "completely."
    ),
    (
        "Our new induction cooktop heats up incredibly quickly. It's also much safer since the surface stays "
        "relatively cool."
    ),
    (
        "The pantry organization system has been life changing honestly. We can actually find ingredients without "
        "digging around now."
    ),
    (
        "The smoke detector batteries need replacing before they start chirping. That middle of the night beeping is "
        "so annoying."
    ),
    (
        "We installed motion sensor lights on the exterior walls. They deter potential intruders and save energy "
        "simultaneously."
    ),
    (
        "The area rug really ties the whole room together nicely. It adds warmth and defines the seating arrangement "
        "perfectly."
    ),
    (
        "Our HEPA air purifier has helped with my seasonal allergies. The air quality monitor shows a significant "
        "improvement indoors."
    ),
    (
        "The garage door opener has been making concerning grinding noises. We should get it serviced before it fails "
        "completely."
    ),
    (
        "Our rainwater collection barrel provides water for the garden. It's surprisingly effective even with moderate "
        "rainfall."
    ),
    # NATURE & OUTDOORS - NATURAL
    "The bioluminescent algae lit up the waves at night. Each breaking wave glowed an ethereal blue green color.",
    "The old growth forest has trees over five hundred years old. Walking among them feels like entering a cathedral.",
    (
        "The tide pools were teeming with colorful sea anemones. The children were fascinated by the starfish and "
        "hermit crabs."
    ),
    "We found a secluded waterfall after a three hour hike. The swimming hole at its base was refreshingly cold.",
    (
        "The wildflower meadow was absolutely stunning in late spring. Lupines and Indian paintbrush covered the "
        "entire hillside."
    ),
    "A massive thunderhead was building on the western horizon. We decided to head back before the storm arrived.",
    (
        "The petrified forest is over two hundred million years old. Each fallen log has been transformed into "
        "colorful stone."
    ),
    "We kayaked through the mangrove tunnels at sunrise. The root systems create these incredible natural archways.",
    "The desert comes alive with flowers after the rare rainfall. We timed our visit perfectly to see the superbloom.",
    (
        "The glacial lake's color was an impossible turquoise hue. The suspended rock flour creates that distinctive "
        "appearance."
    ),
    (
        "We watched the geyser erupt right on its predicted schedule. The steam and boiling water shot nearly a "
        "hundred feet high."
    ),
    "The cave system extends for miles beneath the limestone plateau. Only a fraction of it has been fully explored.",
    "The redwood canopy blocks out most of the sunlight below. The forest floor has a mystical, primeval quality.",
    (
        "We spotted fresh bear tracks along the muddy riverbank. Our guide estimated it had passed through just hours "
        "earlier."
    ),
    (
        "The volcanic hot springs were the perfect temperature for soaking. Mineral deposits had created terraced "
        "pools naturally."
    ),
    "A family of deer emerged from the treeline at dusk. The fawn was still covered in white spots on its coat.",
    (
        "The sandstone arches were carved by millions of years of erosion. Each formation seems more improbable than "
        "the last."
    ),
    (
        "We found fossils embedded in the exposed cliff face. Shells from an ancient sea now sit thousands of feet "
        "above water."
    ),
    (
        "The wetlands are critical habitat for migratory waterfowl. Thousands of birds stop here during their annual "
        "journey."
    ),
    "The meteor shower was spectacular away from city lights. We counted over fifty shooting stars within an hour.",
    # EDUCATION & LEARNING - NATURAL
    (
        "The professor's lecture on quantum mechanics was surprisingly accessible. She has a gift for explaining "
        "complex concepts simply."
    ),
    (
        "My language tutor says my pronunciation has improved significantly. Consistent practice with native speakers "
        "makes all the difference."
    ),
    (
        "The research methodology class was challenging but essential. I finally understand how to design proper "
        "controlled experiments."
    ),
    (
        "Her dissertation defense lasted nearly three hours yesterday. The committee asked tough but fair questions "
        "throughout."
    ),
    (
        "The online course platform allows me to learn at my own pace. I can revisit difficult concepts as many times "
        "as needed."
    ),
    (
        "My study group meets every Thursday evening at the library. We've been preparing for the certification exam "
        "together."
    ),
    (
        "The seminar on critical thinking skills was genuinely useful. I've started applying those frameworks in my "
        "daily decisions."
    ),
    (
        "His thesis advisor provided incredibly detailed feedback. The revision process was intensive but made the "
        "work much stronger."
    ),
    (
        "The laboratory portion of the chemistry course is fascinating. Seeing reactions happen in person reinforces "
        "the theory completely."
    ),
    (
        "My academic counselor helped me plan my course schedule carefully. The prerequisites need to be taken in a "
        "specific order."
    ),
    (
        "The scholarship committee selected her from over five hundred applicants. Her research proposal was "
        "exceptionally well crafted."
    ),
    (
        "We're reading primary sources rather than relying on textbooks. Analyzing original documents provides much "
        "richer understanding."
    ),
    "The peer review process caught several errors I had overlooked. Having fresh eyes on your work is invaluable.",
    (
        "My statistics professor uses real world datasets in every lesson. Applying concepts to actual data makes them "
        "stick better."
    ),
    (
        "The guest lecturer shared insights from decades of field experience. Her stories brought the theoretical "
        "concepts to life."
    ),
    (
        "I've been using spaced repetition for vocabulary memorization. The technique has dramatically improved my "
        "retention rates."
    ),
    (
        "The writing center helped me structure my argument more effectively. The tutors there are genuinely skilled "
        "at their craft."
    ),
    (
        "Our capstone project requires collaboration with industry partners. The real world experience is invaluable "
        "for our portfolios."
    ),
    (
        "The teaching assistant's office hours are always packed with students. She explains things differently than "
        "the professor does."
    ),
    (
        "My learning disability accommodation allows extra time on exams. The support services have been absolutely "
        "essential for my success."
    ),
]

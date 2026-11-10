"""Multi-sentence prompts: natural talk about books, movies, and gardening."""

from __future__ import annotations

BOOKS: list[str] = [
    # BOOKS & READING - NATURAL
    "The author's prose style is lyrical yet accessible somehow. Each sentence feels carefully crafted and deliberate.",
    (
        "I've been on the library's waitlist for that novel for months. Bestsellers always have the longest "
        "reservation queues."
    ),
    (
        "The plot twist in the final chapter recontextualized everything before. I immediately started rereading from "
        "the beginning."
    ),
    (
        "Her memoir chronicles three generations of family immigration stories. The narrative weaves historical events "
        "with personal experiences."
    ),
    (
        "The annotated edition includes fascinating marginalia and scholarly notes. Understanding the historical "
        "context enriches the reading."
    ),
    (
        "I exclusively listen to audiobooks during my commute now. The narrator's performance really brings characters "
        "to life."
    ),
    (
        "The independent bookstore hosts author readings every Thursday evening. The intimate setting allows for "
        "meaningful discussions."
    ),
    (
        "His debut novel received mixed reviews from literary critics. Commercial success doesn't always correlate "
        "with critical acclaim."
    ),
    (
        "The graphic novel format suited this particular story perfectly. Visual storytelling added dimensions words "
        "alone couldn't capture."
    ),
    (
        "I prefer physical books despite the convenience of ebooks. The tactile experience of turning pages feels "
        "irreplaceable."
    ),
    (
        "The biography revealed aspects of her life I never knew. Primary source research uncovered previously hidden "
        "correspondence."
    ),
    (
        "Our reading challenge encourages exploring different genres monthly. I've discovered authors I never would "
        "have found otherwise."
    ),
    (
        "The translation preserved the original work's poetic rhythm beautifully. The translator's notes explain "
        "cultural nuances throughout."
    ),
    (
        "His writing workshop provided constructive critique and encouragement. The feedback on my manuscript was "
        "genuinely helpful."
    ),
    (
        "The anthology collects short stories from emerging diverse voices. Each piece offers a unique perspective on "
        "contemporary life."
    ),
    (
        "I annotate extensively in the margins while reading nonfiction. Engaging actively with the text improves my "
        "retention."
    ),
    (
        "The rare books collection requires special handling and appointments. The archivist guided me through proper "
        "preservation protocols."
    ),
    (
        "Her children's picture book addresses complex emotions with simplicity. The illustrations perfectly "
        "complement the gentle narrative."
    ),
    (
        "The podcast discusses one book in depth across multiple episodes. The analysis reveals layers I missed during "
        "my reading."
    ),
    "My goal is to read at least fifty books this year. Tracking progress keeps me accountable and motivated.",
    # MOVIES & ENTERTAINMENT - NATURAL
    (
        "The director's cut includes thirty minutes of additional footage. The theatrical release apparently had to "
        "trim significantly."
    ),
    (
        "Her performance carried an otherwise mediocre screenplay admirably. The Oscar nomination was thoroughly "
        "deserved this year."
    ),
    (
        "The special effects have aged remarkably well for a nineties film. Practical effects often hold up better "
        "than early CGI."
    ),
    (
        "We waited in line for three hours for premiere tickets. The fan community made the experience enjoyable "
        "regardless."
    ),
    (
        "The documentary challenged my assumptions about the subject matter. Well researched journalism can genuinely "
        "change perspectives."
    ),
    (
        "His cameo appearance was the highlight of the entire film. The audience erupted in cheers when he appeared "
        "onscreen."
    ),
    (
        "The streaming platform's algorithm keeps recommending the same genres. I wish it would surface more "
        "unexpected suggestions."
    ),
    (
        "The score perfectly complemented the emotional beats of each scene. The composer's work elevated good scenes "
        "to great ones."
    ),
    (
        "That indie film had a limited theatrical release unfortunately. Smaller productions struggle for screen time "
        "against blockbusters."
    ),
    "The sequel failed to capture the magic of the original. Sometimes beloved stories should remain self contained.",
    (
        "Her stand up special touched on personal experiences with vulnerability. Comedy that reveals truth resonates "
        "most deeply."
    ),
    (
        "The cinematographer's use of natural lighting was stunning throughout. Each frame could be extracted as a "
        "photograph."
    ),
    (
        "We subscribe to too many streaming services at this point. The fragmented content landscape is expensive and "
        "frustrating."
    ),
    (
        "The theater's reclining seats and reserved seating transformed the experience. Premium amenities justify the "
        "higher ticket prices."
    ),
    "His directorial debut showed remarkable confidence and vision. I'm excited to see what he creates next.",
    (
        "The foreign film required my full attention to follow subtitles. Multitasking while watching simply wasn't "
        "possible."
    ),
    (
        "The franchise has announced three more sequels already. The studio is clearly prioritizing brand extension "
        "over creativity."
    ),
    (
        "Her portrayal humanized a historical figure often depicted one dimensionally. The nuanced performance avoided "
        "hagiography and demonization."
    ),
    (
        "The restoration process preserved this classic for future generations. Seeing it on the big screen was "
        "revelatory."
    ),
    "My watchlist has grown longer than I could ever possibly complete. There's simply too much content to consume.",
    # GARDENING & PLANTS - NATURAL
    (
        "The perennials are finally establishing themselves after three seasons. The patience required for gardening "
        "teaches valuable lessons."
    ),
    (
        "My tomato plants succumbed to blight despite preventive measures. Next year I'll try more resistant heirloom "
        "varieties."
    ),
    (
        "The raised beds improved drainage significantly in our clay soil. Root vegetables finally grow properly "
        "without rotting."
    ),
    (
        "Her orchid collection requires precise humidity and temperature control. The greenhouse conditions mimic "
        "their native tropical habitat."
    ),
    (
        "The pollinator garden attracts butterflies, bees, and hummingbirds daily. Native plant species provide "
        "essential food sources."
    ),
    (
        "Companion planting reduced pest problems naturally this summer. Marigolds and basil seem to deter common "
        "garden insects."
    ),
    (
        "The autumn leaf mulch will decompose and enrich the soil. Nature's recycling system requires minimal "
        "intervention from us."
    ),
    (
        "My indoor fiddle leaf fig has been struggling with brown spots. Inconsistent watering is apparently the "
        "likely culprit."
    ),
    (
        "The botanical garden's rose collection blooms spectacularly in June. The fragrance alone makes the visit "
        "worthwhile."
    ),
    (
        "We're converting more lawn to native meadow every year. The reduced maintenance and increased biodiversity "
        "benefit everyone."
    ),
    (
        "The succulent arrangement in the ceramic planter is thriving nicely. Their drought tolerance makes them "
        "perfect for forgetful people."
    ),
    (
        "His bonsai practice spans over four decades of patient cultivation. The miniature trees are living sculptures "
        "requiring constant attention."
    ),
    (
        "The seed starting setup includes grow lights and heat mats. Indoor germination gives seedlings a significant "
        "head start."
    ),
    (
        "Our fruit trees finally produced a substantial harvest this year. The initial years of establishment are "
        "finally paying off."
    ),
    (
        "The Japanese maple's foliage turns brilliant crimson each autumn. It's become the focal point of our entire "
        "landscape."
    ),
    (
        "Pruning the roses properly encourages more vigorous blooming cycles. The technique seems counterintuitive but "
        "genuinely works."
    ),
    (
        "The community garden plot provides fresh vegetables all summer. Sharing space with other gardeners builds "
        "neighborhood connections."
    ),
    (
        "Her propagation skills have filled the house with healthy plants. Starting from cuttings is economical and "
        "satisfying."
    ),
    (
        "The soil test revealed deficiencies in nitrogen and phosphorus. Targeted amendments should address the "
        "imbalances naturally."
    ),
    "The vertical garden maximizes growing space on our small balcony. Even limited outdoor areas can be productive.",
]

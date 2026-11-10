"""Color prompts from single colors to long scenes of nature, fashion, and interiors."""

from __future__ import annotations

SHADES: list[str] = [
    # ULTRA SHORT - BASIC COLORS
    "Crimson sunset fading.",
    "Azure skies above.",
    "Emerald forest glow.",
    "Ivory tower gleaming.",
    "Obsidian night falls.",
    "Amber waves rolling.",
    "Violet dusk approaching.",
    "Scarlet leaves falling.",
    "Indigo dreams swirling.",
    "Chartreuse spring buds.",
    # ULTRA SHORT - REDS/PINKS
    "Ruby lips smiling.",
    "Burgundy wine poured.",
    "Maroon velvet curtains.",
    "Vermillion flames dancing.",
    "Carmine roses blooming.",
    "Cerise petals scattered.",
    "Magenta neon glowing.",
    "Fuchsia flowers vibrant.",
    "Coral reef shimmering.",
    "Salmon sky at dawn.",
    # ULTRA SHORT - BLUES/GREENS
    "Cerulean waves crashing.",
    "Cobalt bottles arranged.",
    "Sapphire eyes sparkling.",
    "Navy uniforms pressed.",
    "Turquoise jewelry displayed.",
    "Teal walls painted.",
    "Jade pendant hanging.",
    "Olive groves stretching.",
    "Mint leaves fresh.",
    "Sage brush fragrant.",
    # ULTRA SHORT - YELLOWS/ORANGES
    "Golden honey dripping.",
    "Saffron robes flowing.",
    "Canary feathers bright.",
    "Mustard fields blooming.",
    "Tangerine slices arranged.",
    "Apricot blush spreading.",
    "Copper pots gleaming.",
    "Persimmon fruit ripening.",
    "Marigold petals opening.",
    "Ochre desert sand.",
    # ULTRA SHORT - PURPLES/NEUTRALS
    "Lavender fields endless.",
    "Plum velvet soft.",
    "Amethyst crystals glittering.",
    "Mauve silk draped.",
    "Lilac perfume wafting.",
    "Charcoal sketches displayed.",
    "Slate roof tiles.",
    "Pearl necklace elegant.",
    "Ebony piano keys.",
    "Alabaster skin pale.",
    # ULTRA SHORT - EXOTIC COLORS
    "Viridian depths mysterious.",
    "Aureolin sunshine bright.",
    "Gamboge pigment rich.",
    "Cinnabar ancient red.",
    "Zaffre blue intense.",
    "Smalt glazed pottery.",
    "Heliotrope sunset glow.",
    "Amaranth never fading.",
    "Glaucous sea foam.",
    "Incarnadine blood stained.",
    # SHORT - COLOR DESCRIPTIONS
    "The crimson sunset faded into lavender.",
    "Azure waters met the cerulean sky.",
    "Emerald leaves rustled in golden light.",
    "Ivory clouds drifted across sapphire blue.",
    "Obsidian rocks contrasted with pearl sand.",
    "Amber streetlights cast a warm glow.",
    "Violet flowers dotted the chartreuse meadow.",
    "Scarlet berries hung from jade branches.",
    "Indigo shadows crept across the terracotta.",
    "Burgundy wine reflected the candlelight beautifully.",
    "Turquoise waves lapped the coral shore.",
    "Magenta bougainvillea climbed the ochre wall.",
    "Slate gray clouds promised rain ahead.",
    "Champagne bubbles rose in crystal glasses.",
    "Vermillion flames licked the ebony logs.",
    # SHORT - FASHION/CLOTHING
    "She wore a stunning cobalt dress.",
    "His burgundy tie matched the cufflinks.",
    "The mauve scarf complemented her outfit.",
    "Teal heels clicked on marble floors.",
    "A mustard cardigan over ivory blouse.",
    "Charcoal suit with a crimson pocket square.",
    "Rose gold jewelry sparkled at the gala.",
    "Olive cargo pants with a khaki belt.",
    "Fuchsia nails against her bronze skin.",
    "Navy blazer paired with salmon chinos.",
    "Plum lipstick made her smile pop.",
    "Pewter cufflinks on French blue sleeves.",
    "Coral sundress with cerulean embroidery details.",
    "Graphite leather jacket, very sophisticated look.",
    "Champagne gown shimmered under chandeliers.",
    # SHORT - NATURE SCENES
    "Cherry blossoms painted the park pink.",
    "Rust colored leaves carpeted the forest floor.",
    "Periwinkle wildflowers swayed in meadows.",
    "Moss green covered the ancient stones.",
    "Tangerine monarchs migrated through the valley.",
    "Seafoam crested the aquamarine waves.",
    "Sienna cliffs rose above the canyon.",
    "Wisteria purple draped over garden gates.",
    "Pine green forests stretched for miles.",
    "Buttercup yellow dotted the spring fields.",
    "Mahogany bark peeled from the trunk.",
    "Celadon lichen grew on granite boulders.",
    "Flamingo pink filled the tropical lagoon.",
    "Eucalyptus silver leaves rustled softly.",
    "Poppy red blazed across the hillside.",
    # SHORT - INTERIOR/DESIGN
    "Taupe walls created a calming atmosphere.",
    "Ecru linen curtains filtered the sunlight.",
    "Aubergine accents added dramatic flair.",
    "Seafoam tiles refreshed the bathroom design.",
    "Umber leather sofa anchored the room.",
    "Blush pink pillows softened the space.",
    "Prussian blue kitchen cabinets, very bold.",
    "Cream trim against sage green walls.",
    "Terracotta pots lined the sunny windowsill.",
    "Gunmetal fixtures updated the vintage bathroom.",
    "Sable brown rugs warmed the floors.",
    "Mint green nursery with peach accents.",
    "Oxblood leather chairs in the study.",
    "Ivory marble countertops gleamed beautifully.",
    "Burnt sienna accent wall, stunning choice.",
    # MEDIUM - MIXED COLOR DESCRIPTIONS
    "The vermillion sunset melted into bands of tangerine, apricot, and finally soft lavender as night approached.",
    "Cerulean waters reflected the azure sky, while emerald palm fronds swayed gently in the tropical breeze.",
    "Her sapphire eyes sparkled beneath raven hair, and ruby lips curved into a knowing mysterious smile.",
    "Amber autumn leaves drifted past burgundy brick buildings, settling on the slate gray cobblestone streets below.",
    "The viridian forest canopy filtered golden sunlight, creating dappled patterns on the moss covered forest floor.",
    (
        "Magenta bougainvillea cascaded down ochre walls, while turquoise shutters framed the Mediterranean villa "
        "windows beautifully."
    ),
    "Charcoal thunderclouds gathered above the indigo mountains, promising a dramatic storm across the valley tonight.",
    (
        "Pearl moonlight illuminated the obsidian lake, casting silver ripples across the still midnight waters "
        "peacefully."
    ),
    "Coral reefs teemed with life in shades of chartreuse, cerulean, and vibrant fuchsia tropical fish.",
    "The mauve twilight sky deepened to plum, then finally to the inky black of true night.",
    (
        "Saffron monks walked through jade rice paddies, their robes brilliant against the verdant landscape "
        "stretching endlessly."
    ),
    "Champagne bubbles rose in crystal flutes, catching the warm amber glow of flickering candlelight romantically.",
    "Rust and sienna desert canyons glowed burnt orange under the relentless sun blazing in cloudless skies.",
    "Ivory snow blanketed the pine green forest, while cardinals added splashes of scarlet to branches.",
    "The heliotrope orchids bloomed beside amaranth and cerise flowers in the exotic botanical garden display.",
    # MEDIUM - QUESTIONS
    "Should we paint the bedroom in seafoam green, or would a soft lavender create a calmer atmosphere?",
    "Did you notice how the crimson maple leaves contrasted beautifully against the azure October sky yesterday?",
    "Would the cobalt vase look better on the mahogany shelf, or against the taupe wall instead?",
    "Can you see how the viridian and chartreuse plants create such a lush, tropical feeling here?",
    "Is that dress more of a burgundy or a wine color, because I genuinely cannot tell?",
    "Have you ever seen such a stunning gradient from tangerine to magenta in a sunset before?",
    "Should the bridesmaids wear blush pink or dusty rose, and which complements ivory better overall?",
    "Would copper or bronze fixtures work better with the slate gray tiles in the bathroom?",
    "Did the artist use vermillion or cadmium red for those striking flames in the painting?",
    "Can celadon and sage go together, or are they too similar in tone and saturation?",
    # MEDIUM - EXCLAMATIONS
    (
        "The aurora borealis painted the sky in ribbons of emerald, violet, and brilliant cerulean, absolutely "
        "breathtaking!"
    ),
    "That crimson dress against her porcelain skin with those sapphire earrings was absolutely stunning at the gala!",
    "The coral sunset melting into bands of peach, tangerine, and finally deep plum was pure magic!",
    "I've never seen such vibrant turquoise waters contrasting with ivory sand beaches, truly paradise on earth!",
    "The peacock displayed his iridescent plumage of emerald, sapphire, and gold, what a magnificent creature!",
    "Her ombre hair fading from raven black to burgundy to rose gold was incredible, so creative!",
    "The autumn forest blazing in shades of amber, rust, scarlet, and gold took my breath away!",
    "That vintage car in that perfect shade of seafoam green with chrome accents was absolutely gorgeous!",
    "The butterfly's wings showed impossible gradients of cerulean, violet, and black, nature's true masterpiece!",
    "Her garden exploded with marigold, lavender, fuchsia, and periwinkle blooms, like a living rainbow!",
    # LONG - SUNSET/NATURE SCENES
    (
        "The crimson sunset blazed across the horizon, melting into bands of tangerine, apricot, and rose before "
        "finally surrendering to the deep violet and indigo of approaching night."
    ),
    (
        "Cerulean waves crashed against the obsidian rocks, sending seafoam spray into the air while the golden sun "
        "painted everything in warm amber tones during the magical hour."
    ),
    (
        "The viridian forest stretched endlessly beneath the azure sky, with chartreuse new growth contrasting against "
        "the darker emerald of mature pines and moss covered ancient oaks."
    ),
    (
        "Amber autumn leaves drifted lazily down from the mahogany branches, carpeting the forest floor in shades of "
        "rust, sienna, burnt orange, and deep burgundy."
    ),
    (
        "The aurora borealis danced across the obsidian night sky in ribbons of emerald, violet, cerulean, and "
        "occasional flashes of magenta that took everyone's breath away."
    ),
    (
        "Coral reefs teemed with tropical fish in impossible shades of chartreuse, fuchsia, tangerine, and electric "
        "blue, creating an underwater rainbow of vibrant marine life."
    ),
    (
        "The lavender fields of Provence stretched to the horizon under the cerulean sky, their purple blooms creating "
        "waves of color as the breeze swept through them."
    ),
    (
        "Cherry blossoms in shades of blush, rose, and cream drifted down like pink snow, settling on the jade green "
        "grass of the ancient temple garden."
    ),
    (
        "The desert canyon glowed in bands of sienna, ochre, rust, and terracotta as the setting sun illuminated "
        "millions of years of geological history in warm tones."
    ),
    (
        "Peacock feathers displayed an iridescent palette of emerald, sapphire, cobalt, and gold, each eye spot rimmed "
        "in bronze and black creating nature's most extravagant display."
    ),
    # LONG - FASHION/STYLE
    (
        "She swept into the ballroom wearing a stunning ombre gown that faded from midnight navy at the bodice through "
        "sapphire, periwinkle, and finally powder blue at the hem."
    ),
    (
        "His impeccable style featured a charcoal three piece suit, burgundy silk tie, rose gold cufflinks, and "
        "oxblood leather brogues that commanded attention from everyone in the room."
    ),
    (
        "The fashion collection showcased bold color blocking with cobalt paired against tangerine, magenta alongside "
        "chartreuse, and unexpected combinations of teal and coral throughout the runway show."
    ),
    (
        "Her vintage look included a seafoam green swing dress, cherry red belt, ivory pearls, and blush pink heels "
        "that perfectly captured the elegance of the 1950s aesthetic."
    ),
    (
        "The bridesmaids wore elegant dresses in dusty rose, mauve, and blush pink, carrying bouquets of burgundy "
        "dahlias, ivory roses, and sage eucalyptus for the autumn wedding."
    ),
    (
        "His artistic style combined a mustard yellow blazer over a chambray shirt, olive chinos, and cognac leather "
        "boots that somehow worked perfectly together as an ensemble."
    ),
    (
        "The jewelry collection featured gems in every shade imaginable, from deep garnet and amethyst to brilliant "
        "citrine, peridot, aquamarine, and rare alexandrite that changed color."
    ),
    (
        "Her makeup look featured a bold wing of obsidian liner, champagne shimmer on the lids, peachy blush, and lips "
        "painted in the perfect shade of terracotta."
    ),
    (
        "The textile designer created fabrics in exotic hues of gamboge, heliotrope, incarnadine, and zaffre that "
        "pushed the boundaries of conventional color palettes in haute couture."
    ),
    (
        "His signature style always included something unexpected, like aubergine velvet paired with chartreuse silk, "
        "or prussian blue combined with persimmon in striking combinations."
    ),
    # LONG - INTERIOR DESIGN
    (
        "The living room featured taupe walls, a sable brown leather sofa, brass accents, and throw pillows in shades "
        "of rust, terracotta, and burnt sienna for warmth."
    ),
    (
        "Her kitchen renovation showcased prussian blue cabinets against carrara marble countertops, with copper "
        "pendant lights and sage green subway tile backsplash creating the perfect balance."
    ),
    (
        "The bohemian bedroom layered textures in shades of dusty rose, mauve, cream, and hints of gold, with macrame "
        "wall hangings and terracotta pots adding natural elements."
    ),
    (
        "Art deco glamour filled the space with black lacquer furniture, emerald velvet upholstery, brass geometric "
        "accents, and blush pink marble adding touches of feminine elegance throughout."
    ),
    (
        "The coastal cottage featured seafoam green shiplap walls, bleached driftwood furniture, navy and white "
        "striped textiles, and coral accents that captured the essence of seaside living."
    ),
    (
        "Her maximalist office exploded with color, including a chartreuse velvet chair, magenta curtains, cobalt blue "
        "desk accessories, and gallery walls featuring art in every hue."
    ),
    (
        "The minimalist space used a palette of cream, ivory, ecru, and hints of pale sage, with natural linen "
        "textures and bleached oak floors creating serene simplicity."
    ),
    (
        "The dining room made a statement with aubergine walls, a mahogany table, brass chandelier, and chair cushions "
        "upholstered in dusty rose velvet for intimate dinner parties."
    ),
    (
        "His study featured hunter green walls, cognac leather armchairs, brass library lamps, and built in mahogany "
        "bookshelves that created the perfect atmosphere for reading and reflection."
    ),
    (
        "The children's playroom burst with color, featuring sunshine yellow walls, grass green carpet, cherry red "
        "beanbags, and cobalt blue storage cubes in rainbow organization."
    ),
]

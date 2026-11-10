"""Color prompts: long art, food, questions, and exclamations, then exotic color names and variety."""

from __future__ import annotations

PALETTES: list[str] = [
    # LONG - ART/CREATIVE
    (
        "The artist's palette held pools of cadmium yellow, alizarin crimson, ultramarine blue, viridian green, and "
        "titanium white, ready to capture the sunset on canvas."
    ),
    (
        "Her watercolor technique created ethereal washes of cerulean, lavender, and rose that bled together at the "
        "edges, capturing the misty morning light over the mountains."
    ),
    (
        "The stained glass window depicted angels in robes of cobalt, emerald, and ruby, with golden halos that caught "
        "the morning sun and scattered rainbows across the floor."
    ),
    (
        "His abstract expressionist work featured violent slashes of vermillion and gamboge against a field of "
        "prussian blue, with drips of obsidian creating dramatic tension throughout."
    ),
    (
        "The ceramicist glazed her pieces in rare colors like celadon, sang de boeuf, tenmoku black, and jun blue that "
        "required precise kiln temperatures to achieve perfectly."
    ),
    (
        "Her embroidery work used silk threads in shades no one could name, somewhere between heliotrope and amaranth, "
        "creating florals that seemed to glow from within."
    ),
    (
        "The mosaic artist assembled tesserae in every shade of blue from palest powder to deepest navy, creating an "
        "ocean scene that rippled with reflected light beautifully."
    ),
    (
        "His digital art explored impossible color combinations, with neon magenta skies over viridian landscapes and "
        "figures rendered in shades of aureolin and incarnadine throughout."
    ),
    (
        "The textile artist wove threads of indigo, saffron, and cochineal red, using natural dyes that created colors "
        "with depth and variation impossible to achieve synthetically."
    ),
    (
        "Her glass sculptures captured light in pools of amber, citrine, and honey, with veins of cobalt running "
        "through like rivers through a golden landscape of beauty."
    ),
    # LONG - FOOD/CULINARY
    (
        "The charcuterie board displayed prosciutto pink, aged cheddar gold, fig purple, olive green, and crusty bread "
        "brown arranged beautifully on the slate gray serving platter."
    ),
    (
        "Her signature cocktail layered grenadine ruby, citrus gold, blue curacao azure, and cream ivory in a tall "
        "glass that looked like a drinkable sunset masterpiece."
    ),
    (
        "The patisserie window showcased macarons in every imaginable hue, from pistachio green and lavender purple to "
        "rose pink, lemon yellow, and chocolate brown treats."
    ),
    (
        "His plating featured the salmon coral center stage, ringed by avocado chartreuse puree, beet magenta "
        "reduction, and microgreen emerald garnish on the obsidian slate plate."
    ),
    (
        "The farmers market overflowed with tomatoes in shades from sunshine yellow through tangerine orange to deep "
        "ruby red, each variety more beautiful than the last."
    ),
    (
        "Her birthday cake featured ombre frosting from deep plum at the base through mauve, blush, and finally ivory "
        "at the top, decorated with fresh peony petals."
    ),
    (
        "The smoothie bowl showcased acai purple topped with golden mango, ruby pomegranate, emerald kiwi, and ivory "
        "coconut flakes creating an edible work of art."
    ),
    (
        "His curry presented a landscape of turmeric gold sauce, jade cilantro, ruby chili, ivory rice, and charred "
        "naan brown that tasted as good as it looked."
    ),
    (
        "The wedding cake tiers alternated between champagne and blush pink, decorated with cascading sugar flowers in "
        "shades of burgundy, peach, and sage green leaves."
    ),
    (
        "Her spice collection lined the shelf in jars of saffron gold, paprika rust, turmeric amber, cinnamon sienna, "
        "and dried herb green creating a beautiful display."
    ),
    # LONG - QUESTIONS
    (
        "Should we choose the seafoam green with hints of cerulean for the bathroom, or would the sage with undertones "
        "of olive create a more spa like atmosphere?"
    ),
    (
        "Did you see how the artist captured that exact moment when the crimson sky fades through tangerine and "
        "apricot into the deep violet of approaching twilight?"
    ),
    (
        "Would the burgundy velvet sofa clash with the terracotta walls, or would adding cream and brass accents tie "
        "the warm color scheme together harmoniously?"
    ),
    (
        "Can you believe how many shades of blue exist in that single peacock feather, from deepest cobalt through "
        "turquoise and teal to almost verdant green?"
    ),
    (
        "Is it possible to mix viridian and prussian blue to get that perfect shade of teal, or should we order the "
        "color pre mixed from the supplier?"
    ),
    (
        "Have you ever noticed how different the same coral paint looks in warm incandescent light versus cool "
        "daylight, shifting from peachy to almost pink?"
    ),
    (
        "Should the accent wall be painted in that rich aubergine we sampled, or would something lighter like dusty "
        "mauve feel less overwhelming in the space?"
    ),
    (
        "Would rose gold, copper, or brass fixtures complement the sage green cabinets better, and does the marble "
        "countertop have warm or cool undertones to consider?"
    ),
    (
        "Did the florist include enough variety, mixing burgundy dahlias, blush roses, ivory ranunculus, and those "
        "unusual chocolate cosmos in the bridal bouquet arrangement?"
    ),
    (
        "Can celadon and seafoam work together in the same room, or are they too similar in their blue green "
        "undertones to create visual interest and contrast?"
    ),
    # LONG - EXCLAMATIONS
    (
        "The northern lights put on a show like I've never seen, with ribbons of emerald, violet, and cerulean dancing "
        "across the obsidian arctic sky, absolutely magical!"
    ),
    (
        "That vintage 1957 Chevy in robin's egg blue with chrome accents and ivory leather interior was the most "
        "gorgeous car at the entire classic auto show!"
    ),
    (
        "Her garden in full bloom was a riot of color, with crimson roses, golden marigolds, purple lavender, and pink "
        "peonies creating a living rainbow masterpiece!"
    ),
    (
        "The reef dive revealed fish in colors I didn't know existed, from electric chartreuse to vibrant magenta to "
        "iridescent turquoise that seemed almost neon underwater!"
    ),
    (
        "That ombre sunset started at deep vermillion, melted through bands of tangerine and gold, then finally "
        "dissolved into soft lavender, simply the most beautiful ever!"
    ),
    (
        "Her wedding color palette of dusty rose, sage green, ivory, and touches of gold created the most romantic, "
        "elegant atmosphere I've ever seen at a celebration!"
    ),
    (
        "The autumn foliage in New England was absolutely spectacular this year, with maples blazing in shades of "
        "scarlet, amber, rust, and gold covering the hillsides!"
    ),
    (
        "That peacock displaying his tail was breathtaking, each feather an iridescent masterpiece of emerald, "
        "sapphire, and gold that shimmered with every slight movement!"
    ),
    (
        "The artist's use of color was revolutionary, combining gamboge and heliotrope with prussian blue and "
        "vermillion in ways that shouldn't work but absolutely did brilliantly!"
    ),
    (
        "Her collection of antique bottles caught the sunlight perfectly, casting shadows in cobalt, amber, emerald, "
        "and amethyst across the windowsill, absolutely stunning arrangement!"
    ),
    # ADDITIONAL - EXOTIC COLOR NAMES (short)
    "Puce walls in the Victorian parlor.",
    "Feldgrau military uniforms lined up.",
    "Mikado yellow silk from Japan.",
    "Fulvous lion prowled the savanna.",
    "Watchet blue medieval tapestry displayed.",
    "Gingerline monks walking at dawn.",
    "Coquelicot poppies in the field.",
    "Nacarat silk ribbons tied beautifully.",
    "Sinoper red earth pigment ancient.",
    "Sarcoline skin toned vintage mannequin.",
    "Smaragdine emerald like gemstone glittering.",
    "Glaucous waxy coating on grapes.",
    "Amaranth unfading purple immortal flowers.",
    "Incarnadine flesh colored or blood stained.",
    "Zinnwaldite brown rare mineral color.",
    # ADDITIONAL - MORE SHORT VARIETY
    "Wenge wood furniture, very dark.",
    "Xanadu gray green mysterious shade.",
    "Razzmatazz pink neon sign glowing.",
    "Malachite green banded gemstone beautiful.",
    "Isabelline pale gray yellow horse coat.",
    "Byzantium purple ancient empire color.",
    "Caput mortuum brownish purple pigment.",
    "Falu red Swedish barn paint.",
    "Hooker's green botanical illustration hue.",
    "Indian yellow historic pigment shade.",
    "Tyrian purple ancient royal dye.",
    "Venetian red earth pigment warm.",
    "Zinnober cinnabar red mercuric sulfide.",
    "Quercitron yellow natural tree dye.",
    "Orpiment arsenic yellow dangerous pigment.",
    # ADDITIONAL - MEDIUM VARIETY
    (
        "The gamboge and aureolin yellows in the manuscript illumination glowed like captured sunlight against the "
        "vellum page beautifully."
    ),
    "Tyrian purple, once worth more than gold, adorned only emperors and royalty in the ancient Mediterranean world.",
    (
        "Her collection of rare pigments included orpiment yellow, cinnabar red, azurite blue, and malachite green "
        "minerals."
    ),
    (
        "The falu red Swedish cottages dotted the emerald landscape, their traditional color unchanged for three "
        "centuries."
    ),
    "Caput mortuum, that brownish purple made from mummy wrappings, was prized by Renaissance painters for shadows.",
    "His palette featured exotic names like smaragdine, feldgrau, nacarat, and coquelicot that few could identify.",
    "The byzantium purple tapestry hung in the castle hall, its color fit for emperors and kings.",
    "Isabelline horses with their pale cream coats cantered across the Spanish riding school arena gracefully.",
    "The xanadu gray green of the distant mountains faded into the hazy horizon at twilight beautifully.",
    "Wenge and mahogany woods combined in the furniture, creating rich warm tones throughout the study.",
    # ADDITIONAL - LONG EXOTIC
    (
        "The medieval manuscript featured pigments now lost to time, including rare orpiment yellow, genuine "
        "ultramarine from lapis lazuli, and vermillion derived from precious cinnabar minerals."
    ),
    (
        "Her expertise in historic colors led her to recreate tyrian purple from murex shells, indian yellow from "
        "mango leaves, and carmine red from cochineal insects."
    ),
    (
        "The museum restoration revealed layers of caput mortuum, smalt blue, and verdigris green beneath centuries of "
        "varnish and overpainting on the Renaissance masterpiece panel."
    ),
    (
        "His obsession with rare pigments led him to collect gamboge from southeast Asia, zaffre from cobalt ore, and "
        "the legendary dragon's blood red from tree resin."
    ),
    (
        "The historic paint analysis revealed surprising use of scheele's green, paris green, and orpiment, all highly "
        "toxic arsenical pigments popular in the Victorian era."
    ),
    (
        "Her traditional dyeing workshop used natural sources for indigo blue, madder red, weld yellow, and the rare "
        "and expensive tyrian purple from sea snails."
    ),
    (
        "The conservator identified the original palette as containing lead white, bone black, yellow ochre, "
        "vermillion, azurite, and the expensive genuine ultramarine from Afghanistan."
    ),
    (
        "His studio walls displayed samples of every historic pigment from egyptian blue and maya blue to indian "
        "yellow and the notorious emerald green arsenical compound."
    ),
    (
        "The textile historian traced the journey of cochineal red from the Aztec empire to European courts, where it "
        "became more valuable than gold by weight."
    ),
    (
        "Her research into byzantine mosaics revealed the use of gold tesserae, smalt blue glass, and rare porphyry "
        "purple stone from imperial Egyptian quarries."
    ),
]

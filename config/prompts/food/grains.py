"""Food prompts about grains, legumes, oils, vinegars, condiments, and herbs."""

from __future__ import annotations

GRAINS: list[str] = [
    # GRAINS AND LEGUMES
    (
        "I'm cooking farro in salted water until it's tender but still chewy, perfect for this Mediterranean grain "
        "salad with roasted vegetables."
    ),
    (
        "The French green lentils du Puy hold their shape beautifully when cooked and have a peppery, earthy flavor "
        "ideal for warm salads."
    ),
    (
        "Would you try the freekeh? It's young green wheat that's been roasted, giving it a smoky, nutty flavor "
        "perfect for pilafs."
    ),
    (
        "This black forbidden rice turns a beautiful deep purple when cooked and has a slightly sweet, nutty flavor "
        "with a chewy texture."
    ),
    (
        "I'm soaking dried chickpeas overnight to make the creamiest hummus from scratch, much better than using "
        "canned beans for this recipe."
    ),
    (
        "The red quinoa has a slightly earthier, nuttier flavor than white quinoa and holds its shape better in cold "
        "grain salads."
    ),
    (
        "Would you like some teff? It's the tiny grain used to make Ethiopian injera and has a mild, slightly molasses "
        "like flavor."
    ),
    (
        "This amaranth porridge is creamy and slightly sticky when cooked, with a grassy, peppery flavor that pairs "
        "well with honey and fruit."
    ),
    (
        "I'm making mujadara with brown lentils and basmati rice, topped with deeply caramelized onions that take "
        "nearly an hour to make properly."
    ),
    (
        "The black eyed peas are simmering with smoked ham hock, onions, and bay leaves for a traditional Southern "
        "Hoppin' John recipe."
    ),
    (
        "Would you try the buckwheat kasha? Despite its name, it's not wheat at all and has a distinctive earthy, "
        "nutty flavor when toasted."
    ),
    (
        "This spelt flour gives the bread a slightly sweet, nutty flavor and more complex nutrition than regular all "
        "purpose wheat flour."
    ),
    (
        "I'm cooking beluga lentils, named for their resemblance to caviar, which stay firm and glossy, perfect for "
        "this elegant appetizer dish."
    ),
    (
        "The mung beans split and cook quickly into a creamy dal, seasoned with turmeric, cumin, and a tadka of "
        "mustard seeds and curry leaves."
    ),
    (
        "Would you like some kamut? It's an ancient Egyptian wheat variety with large kernels and a rich, buttery "
        "flavor for hearty salads."
    ),
    (
        "This wild rice isn't actually rice but an aquatic grass seed with a chewy texture and nutty, slightly vegetal "
        "flavor profile."
    ),
    (
        "I'm making falafel from dried chickpeas that were soaked overnight, never from canned beans, which would make "
        "them too wet and mushy."
    ),
    (
        "The adzuki beans are sweetened and made into anko paste, the traditional filling for Japanese mochi, "
        "dorayaki, and taiyaki desserts."
    ),
    (
        "Would you try the sorghum? It's a gluten free ancient grain with a mild, slightly sweet flavor, perfect for "
        "popping like popcorn."
    ),
    (
        "This barley risotto, called orzotto, has a nuttier flavor and chewier texture than traditional Arborio rice "
        "risotto with the same creaminess."
    ),
    # OILS, VINEGARS AND CONDIMENTS
    (
        "I'm finishing this dish with a drizzle of high quality extra virgin olive oil from Puglia that has notes of "
        "artichoke and fresh grass."
    ),
    (
        "The aged sherry vinegar from Jerez has a complex, nutty sweetness that makes this vinaigrette far more "
        "interesting than plain red wine vinegar."
    ),
    (
        "Would you try the toasted sesame oil? Just a few drops at the end add an intense, nutty aroma to Asian stir "
        "fries and dressings."
    ),
    (
        "This Champagne vinegar is lighter and more delicate than other wine vinegars, perfect for dressing butter "
        "lettuce without overpowering it."
    ),
    (
        "I'm using walnut oil in this endive salad because its rich, nutty flavor pairs beautifully with the bitter "
        "greens and blue cheese."
    ),
    (
        "The pomegranate molasses adds a tangy, fruity sweetness to this muhammara dip made with roasted red peppers "
        "and toasted walnuts."
    ),
    (
        "Would you like some fish sauce? It adds an incredible savory depth, that umami quality, to Thai and "
        "Vietnamese dishes when used properly."
    ),
    (
        "This aged balsamic vinegar from Modena is syrupy thick and sweet enough to drizzle over fresh strawberries or "
        "vanilla gelato for dessert."
    ),
    (
        "I'm deglazing the pan with a splash of Cognac to create a rich, complex sauce for these pan seared peppercorn "
        "crusted filet mignons."
    ),
    (
        "The gochujang paste adds a sweet, fermented heat to Korean dishes that's completely different from fresh "
        "chili peppers or dried flakes."
    ),
    (
        "Would you try the black vinegar from Chinkiang? It has a malty, slightly smoky flavor essential for authentic "
        "Chinese dumplings and braises."
    ),
    (
        "This truffle oil should be used sparingly as a finishing touch, adding an earthy, musky aroma to risotto, "
        "eggs, or fresh pasta dishes."
    ),
    (
        "I'm making a gastrique with apple cider vinegar and honey to balance the richness of this seared duck breast "
        "with its crispy skin."
    ),
    (
        "The mirin adds a subtle sweetness and sheen to Japanese teriyaki sauce that you can't replicate with just "
        "sugar and rice wine."
    ),
    (
        "Would you like some preserved lemon paste? It has an intensely bright, fermented citrus flavor perfect for "
        "North African tagines and dressings."
    ),
    (
        "This pumpkin seed oil from Styria has a deep green color and intense nutty flavor, traditionally drizzled "
        "over vanilla ice cream in Austria."
    ),
    (
        "I'm whisking Dijon mustard into the vinaigrette to help emulsify the oil and add a sharp, tangy heat to this "
        "French bistro salad."
    ),
    (
        "The sambal oelek is a simple Indonesian chili paste that adds pure, bright heat without the sweetness of "
        "sriracha or complexity of gochujang."
    ),
    (
        "Would you try the colatura di alici? It's an Italian fish sauce made from anchovies that adds incredible "
        "depth to pasta and vegetables."
    ),
    (
        "This aged red wine vinegar has mellowed over years in wooden barrels, developing a smooth, complex flavor for "
        "hearty meat based sauces."
    ),
    # HERBS FRESH AND DRIED
    (
        "I'm adding fresh Thai basil at the very end of cooking because its anise like flavor and purple stems add "
        "brightness to the curry."
    ),
    (
        "The dried Mexican oregano has a more citrusy, earthy flavor than Mediterranean oregano and is essential for "
        "authentic chili and mole sauces."
    ),
    (
        "Would you try the fresh shiso leaves? They have a unique flavor combining mint, basil, and anise that's "
        "perfect with sashimi."
    ),
    (
        "This bouquet garni contains fresh thyme, bay leaves, and parsley stems tied together to infuse the stock "
        "without leaving bits behind."
    ),
    (
        "I'm using epazote in these black beans, a pungent Mexican herb that's said to reduce the gas causing "
        "compounds in legumes naturally."
    ),
    (
        "The culantro looks like long serrated leaves and has a stronger, more pungent flavor than cilantro for "
        "Caribbean and Asian dishes."
    ),
    (
        "Would you like some fresh lovage? It tastes like an intense combination of celery and parsley with a hint of "
        "anise flavor."
    ),
    (
        "This herbes de Provence blend contains lavender, thyme, rosemary, marjoram, and savory, perfect for grilled "
        "meats and roasted vegetables."
    ),
    (
        "I'm infusing cream with fresh lemon verbena to make a delicate, citrusy panna cotta that's lighter than "
        "traditional lemon desserts."
    ),
    (
        "The dried makrut lime leaves add an intense citrus floral aroma to Thai curries that fresh lime juice simply "
        "cannot replicate."
    ),
    (
        "Would you try the fresh chervil? It has a delicate anise parsley flavor and is one of the classic French "
        "fines herbes."
    ),
    (
        "This perilla leaf, also called sesame leaf, has a minty, slightly spicy flavor and is essential for wrapping "
        "Korean barbecue bites."
    ),
    (
        "I'm pounding fresh curry leaves with coconut and spices to make a South Indian chutney that's fragrant and "
        "intensely flavorful."
    ),
    (
        "The dried savory is sometimes called the bean herb because it pairs so well with lentils, beans, and other "
        "legumes in cooking."
    ),
    (
        "Would you like some fresh sorrel? Its bright, lemony acidity makes a classic French sauce for fish without "
        "any actual citrus."
    ),
    (
        "This fresh tarragon has a distinctive anise flavor that's essential for authentic béarnaise sauce and French "
        "chicken salad preparations."
    ),
    (
        "I'm using dried lime leaves, also called loomi, to add a sour, fermented citrus flavor to this Persian rice "
        "with lamb."
    ),
    (
        "The fresh lemon balm adds a subtle citrus mint flavor to this summer fruit salad and also makes a lovely "
        "herbal tea."
    ),
    (
        "Would you try the fresh hyssop? It has a minty, slightly bitter flavor that was used in medieval cooking and "
        "some liqueurs."
    ),
    (
        "This dried oregano from the mountains of Greece is more pungent and less sweet than Italian oregano, perfect "
        "for lamb dishes."
    ),
]

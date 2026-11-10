"""Food prompts about sweeteners, world cuisines, and beverages."""

from __future__ import annotations

SWEETENERS: list[str] = [
    # SWEETENERS AND SUGARS
    (
        "I'm using muscovado sugar, which has a deep molasses flavor and moist, sandy texture perfect for gingerbread "
        "and dark fruit cakes."
    ),
    (
        "The date syrup adds a caramel like sweetness with hints of butterscotch and is traditional in Middle Eastern "
        "desserts and marinades."
    ),
    (
        "Would you try palm sugar? It has a complex, caramelized flavor that's essential for authentic Thai curries "
        "and Indonesian desserts."
    ),
    (
        "This turbinado sugar has large, golden crystals that add crunch when sprinkled on top of muffins and quick "
        "breads before baking."
    ),
    (
        "I'm making a simple syrup infused with lavender and lemon verbena for cocktails and drizzling over fresh "
        "summer fruit salads."
    ),
    (
        "The blackstrap molasses is the darkest, most bitter variety with an intense mineral flavor that adds depth to "
        "gingerbread and baked beans."
    ),
    (
        "Would you like some birch syrup? It's rarer than maple syrup with a more complex, spicy, and slightly bitter "
        "flavor profile."
    ),
    (
        "This panela is unrefined whole cane sugar from Colombia, with a complex flavor of caramel, honey, and slight "
        "smokiness."
    ),
    (
        "I'm caramelizing piloncillo, Mexican unrefined sugar, to make a rich sauce for the churros with hints of rum "
        "and molasses."
    ),
    (
        "The sorghum syrup has a mild, slightly tangy sweetness that's traditional in Southern biscuits, cornbread, "
        "and pecan pie recipes."
    ),
    (
        "Would you try coconut sugar? It has a lower glycemic index and tastes like brown sugar with hints of caramel "
        "and butterscotch."
    ),
    (
        "This golden syrup from Britain has a buttery, caramelized flavor that's essential for authentic treacle tart "
        "and flapjacks."
    ),
    (
        "I'm using monk fruit sweetener, which is intensely sweet but has zero calories and doesn't spike blood sugar "
        "like regular sugar."
    ),
    (
        "The yacon syrup tastes like molasses mixed with apple and has prebiotic properties that support healthy gut "
        "bacteria growth."
    ),
    (
        "Would you like some honey from buckwheat flowers? It's dark, robust, and malty, almost like molasses but with "
        "floral notes."
    ),
    (
        "This light corn syrup prevents crystallization in this pecan pie filling, keeping it smooth and glossy "
        "without adding much flavor."
    ),
    (
        "I'm making a gastrique with aged sherry vinegar and wildflower honey to balance the richness of this seared "
        "duck breast."
    ),
    (
        "The barley malt syrup adds a distinctive malty sweetness and helps create the chewy texture in authentic New "
        "York style bagels."
    ),
    (
        "Would you try lucuma powder? It's a Peruvian fruit that's dried and ground, with a maple butterscotch flavor "
        "for smoothies."
    ),
    (
        "This demerara sugar has large, crunchy golden crystals and a subtle molasses flavor, perfect for sweetening "
        "coffee or tea."
    ),
    # WORLD CUISINES - ADDITIONAL
    (
        "I'm preparing a traditional Finnish kalakukko, a rye bread stuffed with fish and pork, slowly baked until the "
        "crust is dark brown."
    ),
    (
        "The Georgian khinkali dumplings are filled with spiced meat and broth, twisted on top, and eaten by biting "
        "and sipping the juices."
    ),
    (
        "Would you try the Burmese mohinga? It's a fish and rice noodle soup considered the national dish, eaten for "
        "breakfast with fritters."
    ),
    (
        "This Basque pintxos spread includes gildas with olives, peppers, and anchovies on skewers, plus crispy "
        "croquetas and tortilla slices."
    ),
    (
        "I'm making Oaxacan tlayudas, large crispy tortillas topped with black bean paste, quesillo cheese, tasajo "
        "beef, and avocado slices."
    ),
    (
        "The Peruvian causa is layered mashed potatoes seasoned with lime and aji amarillo, filled with chicken or "
        "seafood salad."
    ),
    (
        "Would you like some Filipino sisig? It's a sizzling dish of chopped pig face and ears with onions, chili, and "
        "calamansi."
    ),
    (
        "This Senegalese thieboudienne is the national dish of fish and rice cooked in tomato sauce with vegetables "
        "and tamarind."
    ),
    (
        "I'm preparing Hungarian chicken paprikash with sweet paprika, sour cream sauce, and homemade nokedli "
        "dumplings on the side."
    ),
    (
        "The Jamaican ackee and saltfish features the national fruit, which looks like scrambled eggs, cooked with "
        "salted cod and peppers."
    ),
    (
        "Would you try the Laotian larb? It's a minced meat salad with lime, fish sauce, toasted rice powder, and "
        "fresh herbs."
    ),
    (
        "This Polish bigos, hunter's stew, combines sauerkraut, fresh cabbage, various meats, and dried mushrooms "
        "simmered for days."
    ),
    (
        "I'm making Tunisian brik, a crispy fried pastry filled with egg, tuna, capers, and harissa, eaten by biting "
        "carefully."
    ),
    (
        "The Ecuadorian ceviche is different, made with shrimp cooked in lime juice and served with popcorn and "
        "plantain chips."
    ),
    (
        "Would you like some Haitian griot? It's marinated pork shoulder that's braised then fried, served with pikliz "
        "pickled vegetables."
    ),
    (
        "This Sri Lankan hoppers are bowl shaped fermented rice flour pancakes, served with egg in the center and "
        "coconut sambol."
    ),
    (
        "I'm preparing Uzbek plov, the Central Asian rice dish cooked with lamb, carrots, chickpeas, and whole heads "
        "of garlic."
    ),
    (
        "The Icelandic hákarl is fermented shark that's been buried for months, with an intense ammonia smell and "
        "acquired taste."
    ),
    (
        "Would you try the Malaysian rendang? It's beef slowly cooked in coconut milk and spices until dry and "
        "intensely flavored."
    ),
    (
        "This Bolivian salteñas are baked empanadas with a sweet dough and juicy filling of meat, potatoes, olives, "
        "and spiced broth."
    ),
    # BEVERAGES AND DRINKS
    (
        "I'm brewing Turkish coffee in a cezve, letting it foam three times before pouring the thick, unfiltered "
        "coffee into small cups."
    ),
    (
        "The matcha is being whisked vigorously with a bamboo chasen until it's frothy and bright green with no lumps "
        "remaining."
    ),
    (
        "Would you try this yerba mate? It's a traditional South American caffeinated drink sipped through a metal "
        "straw from a gourd."
    ),
    (
        "This masala chai is simmered with cardamom, cinnamon, ginger, cloves, and black pepper, then strained and "
        "mixed with milk."
    ),
    (
        "I'm making a traditional Mexican horchata with rice, almonds, cinnamon, and vanilla, blended and strained "
        "until creamy smooth."
    ),
    (
        "The Italian affogato is simply a shot of hot espresso poured over a scoop of vanilla gelato, melting it into "
        "coffee cream."
    ),
    (
        "Would you like some Moroccan mint tea? It's green tea steeped with fresh spearmint and lots of sugar, poured "
        "from a height."
    ),
    (
        "This Vietnamese egg coffee is made by whipping egg yolks with sweetened condensed milk and pouring it over "
        "strong coffee."
    ),
    (
        "I'm preparing a proper British high tea with Darjeeling, the champagne of teas, served with milk and sugar on "
        "the side."
    ),
    (
        "The Japanese genmaicha combines green tea with toasted brown rice, giving it a nutty, popcorn like flavor and "
        "aroma."
    ),
    (
        "Would you try the Peruvian chicha morada? It's a sweet drink made from purple corn boiled with pineapple, "
        "cinnamon, and cloves."
    ),
    (
        "This Hong Kong style milk tea uses evaporated milk and is strained through a silk stocking for an incredibly "
        "smooth texture."
    ),
    (
        "I'm making dalgona coffee by whipping instant coffee, sugar, and hot water into a thick foam to spoon over "
        "cold milk."
    ),
    (
        "The Russian samovar keeps the tea concentrate warm while hot water is added to dilute each cup to the "
        "drinker's preference."
    ),
    "Would you like some Swedish glögg? It's a warm spiced wine with almonds, raisins, cardamom, cinnamon, and cloves.",
    "This taro milk tea has a beautiful purple color and sweet, nutty flavor with chewy tapioca pearls at the bottom.",
    (
        "I'm brewing Ethiopian coffee in a jebena clay pot, a ceremony that involves roasting green beans and burning "
        "frankincense."
    ),
    (
        "The agua fresca stand has jamaica made from hibiscus flowers, tamarindo, and horchata, all served over ice in "
        "plastic bags."
    ),
    (
        "Would you try the Korean sikhye? It's a sweet rice punch with cooked rice grains floating in it, served cold "
        "after meals."
    ),
    (
        "This golden milk is made with turmeric, ginger, black pepper, and honey simmered in coconut milk until warm "
        "and fragrant."
    ),
]

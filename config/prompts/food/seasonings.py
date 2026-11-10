"""Food prompts: long descriptions of complex dishes, then spices and seasonings."""

from __future__ import annotations

SEASONINGS: list[str] = [
    # LONG EXAMPLES - COMPLEX DISHES Part 4
    (
        "I'm making a traditional French galette des rois with flaky puff pastry and a rich almond frangipane filling, "
        "complete with a hidden fève inside."
    ),
    (
        "The restaurant's signature appetizer is hamachi crudo with yuzu kosho, pickled jalapeño, micro cilantro, and "
        "a drizzle of high quality olive oil."
    ),
    (
        "Would you try the elaborate Indonesian rijsttafel with its twenty small dishes including satay, rendang, gado "
        "gado, and various sambals with rice?"
    ),
    (
        "This stunning chocolate dessert features a dark chocolate cremeux, hazelnut praline, milk chocolate mousse, "
        "and a shiny mirror glaze on top."
    ),
    (
        "I'm preparing a classic steak Diane tableside with the filet flambéed in cognac, finished with a rich "
        "mushroom cream sauce and fresh herbs."
    ),
    (
        "The chef's creation is a whole salt baked fish that's cracked open at the table, revealing perfectly moist "
        "flesh infused with herbs and lemon."
    ),
    (
        "Would you like the traditional Cantonese dim sum brunch with its rolling carts of steaming baskets, congee, "
        "and chrysanthemum tea service?"
    ),
    (
        "This elaborate French charcuterie board includes house made pâté, rillettes, saucisson, cornichons, grainy "
        "mustard, and fresh baguette slices."
    ),
    (
        "I'm making a stunning opera cake with layers of almond joconde, coffee buttercream, dark chocolate ganache, "
        "and a shiny chocolate glaze."
    ),
    (
        "The tasting menu features a perfectly executed eggs Benedict with house cured Canadian bacon, poached eggs, "
        "and silky hollandaise on brioche."
    ),
    (
        "Would you try the elaborate Vietnamese seven courses of beef, progressing from raw to grilled, each prepared "
        "with different techniques and sauces?"
    ),
    (
        "This traditional English trifle has layers of sherry soaked sponge cake, fresh berries, vanilla custard, and "
        "billowy whipped cream on top."
    ),
    (
        "I'm preparing a stunning crown roast of lamb with the bones frenched and crossed, filled with an herb "
        "stuffing and served with mint jelly."
    ),
    (
        "The restaurant's famous bananas Foster is prepared tableside with the bananas flambéed in rum and served over "
        "vanilla bean ice cream."
    ),
    (
        "Would you like the elaborate Japanese shabu shabu with thinly sliced Wagyu beef, vegetables, and tofu swished "
        "in a kombu dashi broth?"
    ),
    (
        "This stunning pavlova has a crisp meringue shell with a marshmallow center, topped with fresh whipped cream "
        "and seasonal tropical fruits."
    ),
    (
        "I'm making a traditional Provençal daube with beef slowly braised in red wine with olives, tomatoes, and "
        "herbs de Provence for hours."
    ),
    (
        "The chef's dessert is a deconstructed key lime pie with graham cracker soil, lime curd dots, and a quenelle "
        "of whipped cream."
    ),
    (
        "Would you try the elaborate Ethiopian feast served on injera bread with doro wat, kitfo, tibs, and various "
        "vegetable stews to share?"
    ),
    (
        "This spectacular whole roasted suckling pig has crackling crispy skin, tender meat, and is served with apple "
        "sauce and roasted vegetables."
    ),
    # LONG EXAMPLES - COMPLEX DISHES Part 5
    (
        "I'm preparing a stunning lobster fra diavolo with whole lobster, mussels, clams, and shrimp in a spicy tomato "
        "sauce over fresh linguine pasta."
    ),
    (
        "The restaurant's signature is a twelve layer mille crêpe cake with alternating layers of delicate crêpes and "
        "pastry cream, finished with caramelized sugar."
    ),
    (
        "Would you like the elaborate Spanish cochinillo, a whole roasted suckling pig that's so tender it's "
        "traditionally carved with a ceramic plate?"
    ),
    (
        "This traditional French boudin blanc is a delicate white sausage made with pork, cream, and eggs, served with "
        "sautéed apples and mashed potatoes."
    ),
    (
        "I'm making an impressive charlotte royale with the Swiss roll exterior spiraling around a Bavarian cream "
        "center and fresh raspberry filling."
    ),
    (
        "The chef's amuse bouche is a single perfect oyster topped with champagne mignonette, caviar, and a delicate "
        "cucumber granita on the side."
    ),
    (
        "Would you try the elaborate Szechuan hot pot with its bubbling spicy broth, thinly sliced meats, fresh "
        "vegetables, and various dipping sauces?"
    ),
    (
        "This stunning tarte Tatin features caramelized apples arranged in a beautiful rosette pattern, baked under "
        "buttery puff pastry and inverted to serve."
    ),
    (
        "I'm preparing a traditional Brazilian churrasco feast with multiple cuts of meat carved tableside, farofa, "
        "black beans, and fried plantains."
    ),
    (
        "The dessert course is an elaborate Paris Brest with praline mousseline cream piped into a ring of choux "
        "pastry, topped with sliced almonds."
    ),
    (
        "Would you like the traditional Japanese kaiseki course featuring seasonal ingredients prepared with precise "
        "techniques and artistic presentation throughout?"
    ),
    (
        "This impressive beef carpaccio is pounded paper thin, dressed with lemon, olive oil, capers, and shaved "
        "parmesan with arugula and truffle oil."
    ),
    (
        "I'm making a stunning Saint Honoré cake with caramel dipped profiteroles arranged around a puff pastry base "
        "filled with pastry cream."
    ),
    (
        "The chef's creation is a whole deboned chicken stuffed with foie gras and truffles, wrapped in caul fat and "
        "roasted until golden brown."
    ),
    (
        "Would you try the elaborate Venetian fritto misto with lightly battered and fried calamari, shrimp, zucchini, "
        "and artichokes with aioli?"
    ),
    (
        "This traditional French pot au feu features beef short ribs, marrow bones, and vegetables slowly poached, "
        "served with mustard and coarse salt."
    ),
    (
        "I'm preparing a stunning entremet with layers of chocolate mousse, praline crunch, and vanilla crémeux, all "
        "covered in a perfect mirror glaze."
    ),
    (
        "The restaurant's famous duck à l'orange features a perfectly roasted duck with crispy skin, served with a "
        "classic bigarade sauce made tableside."
    ),
    (
        "Would you like the elaborate Korean royal court cuisine with its many small dishes, including japchae, "
        "bulgogi, and various namul preparations?"
    ),
    (
        "This impressive whole baked salmon en croûte is wrapped in puff pastry with spinach and dill, served with a "
        "champagne beurre blanc sauce."
    ),
    # SPICES AND SEASONINGS
    (
        "The cardamom pods release their fragrant aroma when you crush them gently, adding a warm floral note to the "
        "rice pudding dessert."
    ),
    (
        "I'm toasting whole cumin seeds in a dry pan until they become fragrant and slightly darker, then grinding "
        "them fresh for the curry."
    ),
    (
        "Would you try adding some sumac to the fattoush salad? It gives a beautiful tangy, lemony flavor without the "
        "actual citrus juice."
    ),
    (
        "The fenugreek leaves add a slightly bitter, maple like flavor to this Ethiopian berbere spice blend that I'm "
        "preparing from scratch."
    ),
    (
        "I'm infusing saffron threads in warm milk to release their golden color and delicate honey like flavor for "
        "the biryani rice."
    ),
    (
        "This Ras el Hanout blend contains over twenty spices including rose petals, cubeb pepper, grains of paradise, "
        "and long pepper."
    ),
    (
        "Would you like me to add some Aleppo pepper flakes? They have a fruity, mild heat that's perfect for "
        "finishing grilled meats."
    ),
    (
        "The juniper berries are essential for this venison dish, adding a piney, slightly citrusy flavor that "
        "complements the gamey meat perfectly."
    ),
    (
        "I'm grinding Szechuan peppercorns to add their unique numbing, citrusy tingle to this mapo tofu with "
        "fermented black beans and chili oil."
    ),
    (
        "This garam masala contains cinnamon, cloves, green cardamom, nutmeg, and bay leaves toasted and ground "
        "together fresh."
    ),
    (
        "Would you try the grains of paradise? They taste like a peppery ginger with hints of cardamom and citrus, "
        "perfect for West African dishes."
    ),
    (
        "The annatto seeds give this achiote paste its vibrant orange red color and earthy, slightly peppery flavor "
        "for the cochinita pibil."
    ),
    (
        "I'm blooming asafoetida in hot oil to mellow its pungent sulfurous aroma into a savory, onion like flavor for "
        "this South Indian dal."
    ),
    (
        "This za'atar blend combines dried thyme, oregano, marjoram, toasted sesame seeds, and tangy sumac for the "
        "perfect Middle Eastern seasoning."
    ),
    (
        "Would you like some urfa biber on your eggs? It has a smoky, raisin like sweetness with moderate heat that "
        "builds slowly."
    ),
    (
        "The black lime adds an intensely sour, fermented citrus flavor to this Persian ghormeh sabzi stew with kidney "
        "beans and dried herbs."
    ),
    (
        "I'm using mahlab, ground from cherry pits, to add an almond cherry flavor to these traditional Greek Easter "
        "bread tsoureki loaves."
    ),
    (
        "This dukkah contains toasted hazelnuts, coriander, cumin, sesame seeds, and black pepper, perfect for dipping "
        "bread with olive oil."
    ),
    (
        "Would you try adding some amchur powder? It's made from dried unripe mangoes and adds a tangy, fruity "
        "sourness to chutneys and curries."
    ),
    (
        "The long pepper has a more complex flavor than black pepper, with hints of nutmeg, cinnamon, and a slow "
        "building heat."
    ),
]

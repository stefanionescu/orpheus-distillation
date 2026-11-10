"""Food prompts: long descriptions of complex dishes."""

from __future__ import annotations

DISHES: list[str] = [
    # LONG EXAMPLES - COMPLEX DISHES Part 1
    (
        "I'm preparing a traditional coq au vin with pearl onions, mushrooms, and bacon lardons, all braised in a rich "
        "burgundy wine sauce for hours."
    ),
    (
        "The chef's tasting menu features a stunning amuse bouche of compressed watermelon with feta mousse, basil "
        "oil, and aged balsamic reduction."
    ),
    (
        "Would you like to try the pan seared duck breast with cherry gastrique, served alongside a celery root puree "
        "and haricots verts?"
    ),
    (
        "This authentic Neapolitan pizza has a beautifully charred leopard spotted crust, San Marzano tomatoes, fresh "
        "mozzarella di bufala, and fragrant basil leaves."
    ),
    (
        "I'm making a classic bouillabaisse with fresh mussels, clams, shrimp, and firm white fish in a saffron tomato "
        "broth with rouille and crusty bread."
    ),
    (
        "The deconstructed lemon tart features a buttery sablé crumble, silky lemon curd, Italian meringue kisses, and "
        "candied lemon zest on the plate."
    ),
    (
        "Would you try the slow braised lamb shank with gremolata, served over creamy polenta with roasted root "
        "vegetables and a red wine reduction sauce?"
    ),
    (
        "This elaborate sushi omakase includes uni from Hokkaido, otoro from bluefin tuna, and sweet amaebi shrimp, "
        "all served on perfectly seasoned rice."
    ),
    (
        "I'm preparing a Moroccan lamb tagine with preserved lemons, green olives, saffron, and warm spices, served "
        "over fluffy couscous with toasted almonds."
    ),
    (
        "The molecular gastronomy dessert features a chocolate sphere that melts when warm raspberry coulis is poured "
        "over it, revealing a hidden mousse inside."
    ),
    (
        "Would you like the beef Wellington with a layer of mushroom duxelles and prosciutto wrapped in flaky golden "
        "puff pastry, served with a Madeira sauce?"
    ),
    (
        "This authentic Thai green curry has tender chicken, Thai eggplant, bamboo shoots, and fresh basil in a creamy "
        "coconut milk sauce with kaffir lime."
    ),
    (
        "I'm making homemade ravioli filled with ricotta and spinach, served in a brown butter sage sauce with toasted "
        "pine nuts and shaved parmesan."
    ),
    (
        "The tasting menu's fish course is butter poached halibut with champagne beurre blanc, caviar, and a delicate "
        "fennel and citrus salad on the side."
    ),
    (
        "Would you try the traditional cassoulet with duck confit, Toulouse sausages, and white beans slowly baked "
        "with breadcrumbs until golden and bubbling?"
    ),
    (
        "This elaborate mole negro from Oaxaca contains over thirty ingredients including multiple dried chilies, "
        "chocolate, spices, and takes three days to prepare."
    ),
    (
        "I'm preparing a classic lobster thermidor with the meat returned to the shell, covered in a creamy mustard "
        "sauce, and gratinéed until golden brown."
    ),
    (
        "The Japanese kaiseki dinner begins with a seasonal appetizer of persimmon with white miso sauce, followed by "
        "sashimi and a delicate clear soup."
    ),
    (
        "Would you like the whole roasted chicken with truffle butter under the skin, served with roasted fingerling "
        "potatoes and a pan jus reduction?"
    ),
    (
        "This Vietnamese pho has a complex beef broth simmered for eighteen hours with charred onions, ginger, star "
        "anise, cinnamon, and fish sauce."
    ),
    # LONG EXAMPLES - COMPLEX DISHES Part 2
    (
        "I'm making a traditional Spanish paella valenciana with rabbit, chicken, snails, green beans, and white beans "
        "cooked over an open flame with bomba rice."
    ),
    (
        "The dessert course features a warm chocolate fondant with a molten center, accompanied by salted caramel ice "
        "cream and a cocoa nib tuile cookie."
    ),
    (
        "Would you try the Peking duck carved tableside, served with thin pancakes, hoisin sauce, julienned scallions, "
        "and crispy duck skin with sugar?"
    ),
    (
        "This elaborate Indian thali includes dal makhani, palak paneer, butter chicken, biryani rice, raita, pickles, "
        "papadum, and freshly baked naan bread."
    ),
    (
        "I'm preparing a classic French sole meunière with the fish pan fried in brown butter, finished with lemon "
        "juice, capers, and fresh parsley."
    ),
    (
        "The restaurant's signature dish is a forty day dry aged ribeye with bone marrow butter, truffle fries, and a "
        "side of creamed spinach."
    ),
    (
        "Would you like the handmade pappardelle with slow braised wild boar ragù, porcini mushrooms, and a generous "
        "grating of pecorino romano cheese?"
    ),
    (
        "This traditional Korean barbecue spread includes marinated bulgogi, spicy pork belly, various banchan, "
        "ssamjang sauce, and fresh lettuce wraps."
    ),
    (
        "I'm making a show stopping baked Alaska with three flavors of ice cream, Italian meringue torched tableside, "
        "and a pool of raspberry sauce."
    ),
    (
        "The chef's special is butter poached Maine lobster tail with uni butter, served alongside lobster roe risotto "
        "and a champagne foam."
    ),
    (
        "Would you try the traditional Peruvian ceviche mixto with fresh sea bass, shrimp, octopus, and squid cured in "
        "tiger's milk with sweet potato?"
    ),
    (
        "This elaborate dim sum feast includes har gow, siu mai, char siu bao, cheung fun, and turnip cake, all "
        "steamed fresh to order."
    ),
    (
        "I'm preparing a classic beef bourguignon with pearl onions, lardons, mushrooms, and carrots, all slowly "
        "braised in a full bottle of burgundy wine."
    ),
    (
        "The tasting menu finale is a passion fruit soufflé that rises perfectly above the ramekin, served with a "
        "coconut sorbet on the side."
    ),
    (
        "Would you like the whole roasted branzino stuffed with herbs and lemon, served with a salsa verde and roasted "
        "cherry tomatoes on the vine?"
    ),
    (
        "This authentic Mexican birria features slow braised beef in a complex chile consommé, served with fresh "
        "tortillas, onions, cilantro, and lime wedges."
    ),
    (
        "I'm making a traditional French croissant aux amandes with almond cream filling, sliced almonds on top, and a "
        "dusting of powdered sugar."
    ),
    (
        "The restaurant's famous dessert is a towering croquembouche of cream filled profiteroles held together with "
        "spun caramel and decorated with gold leaf."
    ),
    (
        "Would you try the seared foie gras with a Sauternes reduction, brioche toast points, and a quenelle of fig "
        "compote with fleur de sel?"
    ),
    (
        "This Japanese chirashi bowl features an artistic arrangement of sashimi grade fish, tamago, ikura, uni, and "
        "pickled vegetables over sushi rice."
    ),
    # LONG EXAMPLES - COMPLEX DISHES Part 3
    (
        "I'm preparing an elaborate mezze platter with homemade hummus, baba ganoush, muhammara, labneh, falafel, and "
        "warm pita with za'atar olive oil."
    ),
    (
        "The tasting menu appetizer is a delicate tuna tartare with avocado mousse, crispy shallots, sesame tuile, and "
        "a drizzle of ponzu sauce."
    ),
    (
        "Would you like the traditional osso buco alla Milanese with gremolata, served over saffron risotto with a "
        "rich marrow bone in the center?"
    ),
    (
        "This spectacular seafood tower features oysters, clams, shrimp cocktail, lobster tail, king crab legs, and "
        "ceviche arranged on crushed ice."
    ),
    (
        "I'm making a classic French pâté en croûte with a forcemeat of pork and veal, pistachios, and cognac, all "
        "wrapped in decorative pastry."
    ),
    (
        "The chef's signature creation is a deconstructed tiramisu with espresso caviar, mascarpone clouds, and cocoa "
        "soil on a white ceramic canvas."
    ),
    (
        "Would you try the traditional Singaporean chili crab with its sweet and spicy tomato sauce, served with fried "
        "mantou buns for dipping?"
    ),
    (
        "This elaborate Sunday roast includes prime rib, Yorkshire pudding, roasted potatoes, honey glazed parsnips, "
        "and homemade horseradish cream sauce."
    ),
    (
        "I'm preparing a stunning gravlax with dill mustard sauce, pickled cucumber ribbons, capers, and pumpernickel "
        "crisps for an elegant appetizer course."
    ),
    (
        "The restaurant's famous soufflé au chocolat rises dramatically at the table, with a pitcher of warm crème "
        "anglaise poured into its center."
    ),
    (
        "Would you like the whole Dungeness crab with drawn butter, served alongside a fresh corn salad and crispy "
        "garlic bread for dipping?"
    ),
    (
        "This traditional Turkish breakfast spread includes menemen, sucuk, kaymak, honey, olives, fresh tomatoes, "
        "cucumbers, and warm simit bread."
    ),
    (
        "I'm making a classic veal blanquette with a creamy white sauce, pearl onions, and mushrooms, served over "
        "buttered egg noodles with fresh parsley."
    ),
    (
        "The avant garde dessert features a nitrogen frozen parfait that shatters when tapped, revealing layers of "
        "fruit, cream, and crunchy meringue inside."
    ),
    (
        "Would you try the elaborate Georgian khachapuri Adjaruli with its boat shaped bread, pool of melted cheese, "
        "runny egg yolk, and butter?"
    ),
    (
        "This spectacular Peking duck dinner is a two course affair with the crispy skin served first, followed by "
        "stir fried duck meat with vegetables."
    ),
    (
        "I'm preparing a traditional British afternoon tea with finger sandwiches, warm scones with clotted cream and "
        "jam, and an assortment of petit fours."
    ),
    (
        "The chef's tasting features an impossibly thin slice of A5 Wagyu beef seared tableside on a hot stone with "
        "just a touch of sea salt."
    ),
    (
        "Would you like the elaborate Indian biryani with layers of fragrant basmati rice, tender lamb, saffron, fried "
        "onions, and a raita on the side?"
    ),
    (
        "This stunning crab cake is made with jumbo lump meat, minimal filler, and is served with a remoulade sauce "
        "and a fennel apple slaw."
    ),
]

"""Food prompts about world cuisines, cooking techniques, baking, American regional food, desserts, and street food."""

from __future__ import annotations

CUISINES: list[str] = [
    # MORE WORLD CUISINES
    (
        "I'm preparing Tibetan momos, steamed dumplings filled with yak meat and served with a fiery tomato and chili "
        "achar sauce."
    ),
    (
        "The Bhutanese ema datshi is the national dish of chilies cooked in a cheese sauce, incredibly spicy and "
        "comforting."
    ),
    (
        "Would you try the Mongolian buuz? They're steamed dumplings filled with mutton and onions, eaten during lunar "
        "new year."
    ),
    "This Nepali dal bhat is the everyday meal of lentil soup, rice, vegetable curries, and pickles eaten twice daily.",
    (
        "I'm making Somali canjeero, a spongy fermented pancake similar to Ethiopian injera but made with different "
        "grains."
    ),
    (
        "The Malagasy romazava is a beef stew with mixed greens considered the national dish of Madagascar, served "
        "with rice."
    ),
    "Would you like some Eritrean zigni? It's a spicy beef stew with berbere spices, served with injera flatbread.",
    "This Paraguayan sopa paraguaya is actually a savory corn cake, not a soup, made with cheese, onions, and eggs.",
    (
        "I'm preparing Bruneian ambuyat, a starchy, glue like dish made from sago palm, eaten by twirling on bamboo "
        "sticks."
    ),
    "The Samoan palusami is taro leaves baked in coconut cream, wrapped in banana leaves until rich and creamy.",
    (
        "Would you try the Tongan lu pulu? It's corned beef cooked with taro leaves in coconut milk, a Pacific island "
        "staple."
    ),
    "This Greenlandic suaasat is a traditional soup of seal, whale, or reindeer meat with onions and potatoes.",
    "I'm making Faroese ræst, fermented and wind dried mutton that develops an intense, funky flavor over months.",
    "The Maltese rabbit stew, fenkata, is braised in wine with tomatoes and is the national dish of the islands.",
    "Would you like some Mauritian dholl puri? It's a flatbread stuffed with yellow split peas, served with curry.",
    "This Surinamese roti is an Indian influenced flatbread served with curried chicken and potatoes with boiled eggs.",
    (
        "I'm preparing Belizean rice and beans cooked in coconut milk with red kidney beans and served with stewed "
        "chicken."
    ),
    (
        "The Guyanese pepperpot is a meat stew made with cassareep, a thick cassava syrup that preserves and flavors "
        "the dish."
    ),
    "Would you try the Curaçaoan stoba? It's a slow cooked stew of goat or beef with local spices and vegetables.",
    "This Aruban keshi yena is a stuffed cheese ball filled with spiced meat, olives, and raisins, then baked golden.",
    # MORE COOKING TECHNIQUES AND PREPARATIONS
    (
        "I'm using the sous vide method to cook this steak at exactly one hundred twenty nine degrees for two hours "
        "perfectly."
    ),
    (
        "The Maillard reaction creates those delicious brown, caramelized flavors when proteins and sugars are heated "
        "together."
    ),
    (
        "Would you try the ceviche technique? The acid from lime juice denatures the fish proteins, effectively "
        "cooking it raw."
    ),
    (
        "This confit method involves slowly cooking the duck legs submerged in their own fat until incredibly tender "
        "and rich."
    ),
    (
        "I'm dry brining the turkey by rubbing it with salt and letting it rest uncovered in the refrigerator for "
        "three days."
    ),
    (
        "The spherification technique uses sodium alginate and calcium to create caviar like spheres that burst with "
        "flavor."
    ),
    (
        "Would you like to try the tempering technique? It involves carefully heating chocolate to create a shiny, "
        "snappy finish."
    ),
    (
        "This reverse sear method cooks the steak low and slow first, then finishes with a blazing hot sear for "
        "perfect crust."
    ),
    "I'm using the bain marie, or water bath, to gently cook this custard without curdling from direct heat exposure.",
    (
        "The smoking technique with applewood chips adds a sweet, fruity smoke flavor to this pork shoulder over eight "
        "hours."
    ),
    (
        "Would you try the blooming technique? Heating spices in oil releases their essential oils and intensifies "
        "their flavors."
    ),
    "This braising method combines searing with slow, moist cooking to break down tough collagen into silky gelatin.",
    (
        "I'm using the beurre monté technique, emulsifying butter with water to create a stable cooking medium for the "
        "lobster."
    ),
    (
        "The lacto fermentation process uses salt to encourage beneficial bacteria, creating tangy flavors in "
        "vegetables naturally."
    ),
    (
        "Would you like to try the resting technique? Letting meat rest allows the juices to redistribute evenly "
        "throughout."
    ),
    "This blanching and shocking method preserves the bright green color and crisp texture of vegetables for salads.",
    "I'm using the deglazing technique to lift the fond from the pan with wine, creating the base for this pan sauce.",
    "The curing process uses salt, sugar, and time to preserve and flavor the salmon for this homemade gravlax.",
    (
        "Would you try the clarification technique? Egg whites trap impurities, creating crystal clear consommé from "
        "cloudy stock."
    ),
    (
        "This emulsification technique creates a stable mixture of oil and water, essential for mayonnaise and "
        "vinaigrettes."
    ),
    # MORE BAKING AND PASTRY
    "I'm laminating the croissant dough, folding butter into the dough repeatedly to create hundreds of flaky layers.",
    (
        "The tangzhong method uses a cooked flour paste to create incredibly soft, fluffy Japanese milk bread that "
        "stays fresh."
    ),
    "Would you try the creaming method? Beating butter and sugar incorporates air for lighter cakes and cookies.",
    "This autolyse technique rests flour and water before adding yeast, developing gluten and improving bread texture.",
    (
        "I'm using the rubbing in method, working cold butter into flour with fingertips to create a crumbly scone "
        "texture."
    ),
    (
        "The poolish is a wet preferment that ferments overnight, adding complex flavors and better texture to French "
        "bread."
    ),
    (
        "Would you like to try the choux paste? It's cooked on the stovetop before baking into airy profiteroles and "
        "éclairs."
    ),
    "This genoise sponge is made by whipping whole eggs with sugar over heat, then folding in flour for a light cake.",
    (
        "I'm using the Swiss meringue method, heating egg whites and sugar together before whipping for stable "
        "buttercream."
    ),
    "The blind baking technique pre bakes the empty pie crust with weights to prevent soggy bottoms in custard pies.",
    "Would you try the Italian meringue? Hot sugar syrup is poured into whipping egg whites for the most stable foam.",
    "This biga is a stiff Italian preferment that adds nutty, complex flavors to ciabatta and other rustic breads.",
    "I'm using the windowpane test to check if the bread dough has developed enough gluten to stretch paper thin.",
    "The pâte à bombe technique whips hot sugar syrup into egg yolks, creating a stable base for mousses and parfaits.",
    "Would you like to try the invert sugar? It keeps baked goods moist and prevents crystallization in candies.",
    "This pâte sucrée is a sweet, cookie like tart dough that's sturdier than regular pie crust for fruit tarts.",
    "I'm using the fold and stretch method for this sourdough, building gluten strength without traditional kneading.",
    "The crumb coat is a thin layer of frosting that seals in crumbs before applying the final smooth coat.",
    (
        "Would you try the mirror glaze? It's a shiny, reflective coating made with gelatin that covers entremets "
        "perfectly."
    ),
    "This levain is a mature sourdough starter that adds tangy flavor and natural leavening to artisan bread loaves.",
    # MORE REGIONAL AMERICAN FOODS
    (
        "I'm making authentic Texas brisket, smoked low and slow over post oak for sixteen hours until the bark is "
        "perfect."
    ),
    (
        "The New Orleans gumbo starts with a dark chocolate colored roux cooked slowly for nearly an hour before "
        "adding stock."
    ),
    (
        "Would you try the Cincinnati chili? It's a Greek influenced meat sauce with cinnamon and allspice, served "
        "over spaghetti."
    ),
    "This Philly cheesesteak uses thinly sliced ribeye, griddled onions, and your choice of provolone or cheese whiz.",
    "I'm preparing authentic New England clam chowder with fresh quahogs, salt pork, potatoes, and heavy cream.",
    "The Detroit style pizza has a thick, crispy crust with cheese that caramelizes against the edges of the pan.",
    (
        "Would you like some Nashville hot chicken? It's fried chicken brushed with cayenne lard paste, served on "
        "white bread."
    ),
    "This Carolina pulled pork is slow smoked and served with a tangy, vinegar based sauce with red pepper flakes.",
    (
        "I'm making Kansas City burnt ends, the caramelized, crispy cubes of brisket point that are incredibly rich "
        "and smoky."
    ),
    (
        "The Chicago deep dish pizza has a buttery crust pressed up the sides, layered with cheese, toppings, then "
        "chunky tomato sauce."
    ),
    (
        "Would you try the Maryland crab cakes? They're made with jumbo lump meat and minimal filler, broiled until "
        "golden."
    ),
    (
        "This San Francisco cioppino is a tomato based seafood stew with Dungeness crab, clams, mussels, and crusty "
        "sourdough."
    ),
    "I'm preparing authentic Louisiana boudin, a rice and pork sausage with liver, served with crackers and mustard.",
    "The St. Louis style ribs are spare ribs with the tips removed, grilled and glazed with a sweet, sticky sauce.",
    "Would you like some Hawaiian poke? It's cubed raw ahi tuna marinated in soy sauce, sesame oil, and seaweed.",
    "This New Mexican green chile stew features roasted Hatch chiles, pork, potatoes, and tomatoes in a savory broth.",
    "I'm making authentic Maine lobster rolls, chunks of fresh lobster in mayo on a buttered, griddled split top bun.",
    "The Memphis dry rub ribs are coated in a spice blend without sauce, letting the smoke and pork flavor shine.",
    (
        "Would you try the Buffalo wings? They're deep fried and tossed in a butter and hot sauce mixture, served with "
        "blue cheese."
    ),
    "This Lowcountry shrimp and grits features creamy stone ground grits topped with shrimp, bacon, and a rich gravy.",
    # MORE DESSERTS AND SWEETS
    (
        "I'm making Turkish künefe with shredded phyllo dough, melted cheese, and a fragrant rosewater and orange "
        "blossom syrup."
    ),
    "The Japanese mochi ice cream has a chewy rice cake exterior wrapped around a ball of creamy green tea ice cream.",
    (
        "Would you try the Indian gulab jamun? They're fried milk dumplings soaked in a cardamom and saffron scented "
        "syrup."
    ),
    (
        "This Filipino halo halo is a shaved ice dessert with sweet beans, jellies, leche flan, ube ice cream, and "
        "evaporated milk."
    ),
    (
        "I'm preparing French canelés with their caramelized, almost burnt exterior and soft, custardy rum and vanilla "
        "interior."
    ),
    "The Portuguese pastel de nata has a flaky crust and creamy egg custard filling with caramelized spots on top.",
    (
        "Would you like some Middle Eastern knafeh? It's shredded phyllo with sweet cheese, soaked in orange blossom "
        "syrup."
    ),
    "This Austrian sachertorte is a dense chocolate cake with apricot jam, covered in dark chocolate glaze.",
    (
        "I'm making Brazilian brigadeiros, chocolate truffles made with condensed milk and cocoa, rolled in chocolate "
        "sprinkles."
    ),
    "The Korean bingsu is shaved ice milk topped with sweet red beans, fruit, condensed milk, and chewy rice cakes.",
    "Would you try the Mexican churros? They're fried dough coated in cinnamon sugar, served with thick hot chocolate.",
    "This Vietnamese chè has layers of mung beans, coconut cream, tapioca pearls, and pandan jelly over crushed ice.",
    "I'm preparing Polish pączki, rich filled doughnuts traditionally eaten before Lent with rose hip jam inside.",
    "The Indian kulfi is a dense, creamy frozen dessert flavored with cardamom, pistachios, and saffron, set in molds.",
    (
        "Would you like some Greek galaktoboureko? It's crispy phyllo filled with semolina custard and soaked in lemon "
        "syrup."
    ),
    "This Taiwanese pineapple cake has a buttery, crumbly crust with a sweet and tangy pineapple jam filling inside.",
    "I'm making South African malva pudding, a sticky, spongy cake soaked in a hot cream and butter sauce.",
    "The Thai mango sticky rice has sweet coconut sticky rice topped with ripe mango slices and coconut cream.",
    "Would you try the Argentinian dulce de leche? It's caramelized milk spread on everything from toast to ice cream.",
    (
        "This Lebanese maamoul are shortbread cookies filled with dates, pistachios, or walnuts, dusted with powdered "
        "sugar."
    ),
    # MORE STREET FOODS
    (
        "I'm making Japanese takoyaki, crispy octopus balls with a gooey center, topped with mayo, sauce, and bonito "
        "flakes."
    ),
    (
        "The Indian chaat papdi features crispy wafers topped with chickpeas, yogurt, tamarind chutney, and fresh "
        "coriander."
    ),
    "Would you try the Mexican elote? It's grilled corn slathered with mayo, cotija cheese, chili powder, and lime.",
    (
        "This Turkish döner kebab is thinly sliced meat from a rotating spit, served in flatbread with vegetables and "
        "sauce."
    ),
    (
        "I'm preparing Taiwanese gua bao, steamed buns filled with braised pork belly, pickled mustard greens, and "
        "peanuts."
    ),
    "The Colombian arepas are griddled corn cakes stuffed with cheese, shredded beef, or black beans and avocado.",
    (
        "Would you like some German currywurst? It's sliced sausage covered in curry ketchup, served with fries on the "
        "side."
    ),
    "This Vietnamese bánh tráng nướng is a grilled rice paper pizza topped with egg, dried shrimp, and green onions.",
    "I'm making South African bunny chow, a hollowed out bread loaf filled with spicy curry, eaten with your hands.",
    (
        "The Egyptian koshari layers rice, lentils, pasta, and chickpeas, topped with spicy tomato sauce and crispy "
        "onions."
    ),
    "Would you try the Peruvian anticuchos? They're grilled beef heart skewers marinated in aji panca and cumin.",
    "This Jamaican jerk chicken is marinated in scotch bonnet peppers, allspice, and thyme, grilled over pimento wood.",
    "I'm preparing Korean tteokbokki, chewy rice cakes in a sweet and spicy gochujang sauce with fish cakes.",
    "The Israeli sabich is pita stuffed with fried eggplant, hard boiled eggs, hummus, and amba mango pickle sauce.",
    (
        "Would you like some Singaporean satay? They're grilled meat skewers served with spicy peanut sauce and rice "
        "cakes."
    ),
    "This Greek souvlaki is grilled meat on skewers served in pita with tzatziki, tomatoes, onions, and fries inside.",
    (
        "I'm making Thai khao man gai, poached chicken over fragrant rice cooked in chicken fat, with ginger dipping "
        "sauce."
    ),
    "The Dutch stroopwafel is two thin waffles sandwiched with caramel syrup, warmed over a cup of hot coffee.",
    "Would you try the Chinese jianbing? It's a savory crepe with egg, crispy wonton, hoisin sauce, and fresh herbs.",
    "This Argentinian choripán is grilled chorizo sausage in crusty bread with chimichurri sauce, a stadium favorite.",
]

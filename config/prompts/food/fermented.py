"""Food prompts about fermented and preserved foods, nuts, seeds, dairy, and alternatives."""

from __future__ import annotations

FERMENTED: list[str] = [
    # FERMENTED AND PRESERVED FOODS
    (
        "I'm adding a spoonful of white miso paste to this butternut squash soup for a subtle umami depth that you "
        "can't quite identify."
    ),
    (
        "The house made kimchi has been fermenting for three weeks and now has that perfect balance of sour, spicy, "
        "and funky flavors."
    ),
    (
        "Would you try the century eggs? They have a creamy, cheese like yolk and a translucent amber white with "
        "complex savory flavors."
    ),
    (
        "This natto is fermented soybeans with a sticky, stringy texture and pungent aroma that's an acquired taste "
        "but incredibly nutritious."
    ),
    (
        "I'm using doenjang, Korean fermented soybean paste, which is funkier and more complex than Japanese miso in "
        "this hearty stew."
    ),
    (
        "The sauerkraut has been naturally fermenting in a crock for six weeks, developing complex sour flavors and "
        "beneficial probiotics."
    ),
    (
        "Would you like some pickled herring? It's cured in a sweet brine with onions and spices, a traditional "
        "Scandinavian delicacy."
    ),
    (
        "This tempeh is made from fermented whole soybeans pressed into a cake, with a nutty, mushroomy flavor and "
        "firm texture."
    ),
    (
        "I'm adding a splash of kombucha vinegar, which is more complex than regular vinegar, to this salad dressing "
        "with honey and mustard."
    ),
    (
        "The salt preserved anchovies need to be rinsed and filleted, but they have a much cleaner, meatier flavor "
        "than oil packed ones."
    ),
    (
        "Would you try the fermented black garlic? It's sweet, sticky, and has a complex umami flavor with notes of "
        "balsamic and molasses."
    ),
    (
        "This house cured gravlax has been buried in salt, sugar, and dill for three days, developing a silky texture "
        "and concentrated flavor."
    ),
    (
        "I'm making lacto fermented hot sauce with habaneros that will develop complex, tangy flavors over the next "
        "few weeks of fermentation."
    ),
    (
        "The dried shrimp paste, called belacan, adds an intense savory depth to Malaysian and Indonesian dishes when "
        "toasted and crumbled."
    ),
    (
        "Would you like some kvass? It's a traditional Slavic fermented beverage made from rye bread with a slightly "
        "sour, malty flavor."
    ),
    (
        "This koji rice has been inoculated with Aspergillus mold and is the starter for making miso, soy sauce, sake, "
        "and amazake."
    ),
    (
        "I'm using Chinese fermented black beans, which are salted and aged soybeans, to add a pungent, savory depth "
        "to this stir fry."
    ),
    (
        "The water kefir grains are fermenting sugar water into a probiotic, slightly effervescent drink that I'll "
        "flavor with ginger and lemon."
    ),
    (
        "Would you try the surströmming? It's a Swedish fermented herring with an extremely pungent smell that's "
        "traditionally eaten outdoors."
    ),
    (
        "This miso has been aging for three years, developing a deep, complex flavor that's much richer than younger "
        "white or yellow miso."
    ),
    # NUTS AND SEEDS
    (
        "I'm toasting Marcona almonds in olive oil with rosemary and sea salt for an elegant appetizer that pairs "
        "perfectly with sherry."
    ),
    (
        "The black sesame seeds add a striking visual contrast and nuttier, more bitter flavor than white sesame to "
        "this Japanese rice ball."
    ),
    (
        "Would you try the candied pepitas? They're pumpkin seeds coated in spiced sugar and roasted until crunchy for "
        "salad toppings."
    ),
    (
        "This tahini is made from unhulled sesame seeds, giving it a more bitter, robust flavor than the lighter "
        "hulled version."
    ),
    (
        "I'm grinding fresh flax seeds to add to the smoothie because pre ground flax oxidizes quickly and loses its "
        "nutritional benefits."
    ),
    (
        "The pine nuts are toasting in a dry pan, releasing their buttery, resinous aroma for the classic Genovese "
        "basil pesto sauce."
    ),
    (
        "Would you like some activated almonds? They've been soaked to reduce phytic acid and then dehydrated until "
        "crispy again."
    ),
    (
        "This pistachio paste from Sicily is made from the prized bright green Bronte pistachios and is essential for "
        "authentic gelato."
    ),
    (
        "I'm making dukkah with toasted hazelnuts, coriander, cumin, and sesame seeds for dipping crusty bread into "
        "olive oil."
    ),
    "The hemp seeds add a subtle nutty flavor and boost of protein and omega fatty acids to this açaí smoothie bowl.",
    (
        "Would you try the tiger nuts? They're actually tubers, not nuts, with a sweet, coconutty flavor used in "
        "Spanish horchata."
    ),
    (
        "This macadamia nut butter is incredibly rich and creamy, with a buttery flavor that's perfect on toast or in "
        "cookies."
    ),
    (
        "I'm coating the fish in crushed pecans before pan frying to create a crunchy, nutty crust with brown butter "
        "and sage."
    ),
    "The poppy seeds are soaked and ground into a paste for this traditional Hungarian poppy seed roll called beigli.",
    (
        "Would you like some sacha inchi seeds? They're a Peruvian superfood with a mild, nutty flavor and high omega "
        "content."
    ),
    "This walnut oil is cold pressed and unrefined, with an intense nutty flavor that's best used raw in dressings.",
    (
        "I'm making a nut roast with cashews, walnuts, chestnuts, and mushrooms as the centerpiece for a vegetarian "
        "holiday dinner."
    ),
    (
        "The sunflower seed butter is a great nut free alternative with a slightly bitter, earthy flavor that kids "
        "seem to love."
    ),
    (
        "Would you try the candied walnuts with rosemary and cayenne? They're the perfect balance of sweet, savory, "
        "and spicy."
    ),
    (
        "This almond flour is made from blanched almonds and is essential for French macarons and gluten free baking "
        "recipes."
    ),
    # DAIRY AND ALTERNATIVES
    (
        "I'm culturing crème fraîche by adding buttermilk to heavy cream and letting it thicken at room temperature "
        "for twenty four hours."
    ),
    (
        "The buffalo milk mozzarella from Campania has a tangier, more complex flavor than cow's milk mozzarella with "
        "a softer texture."
    ),
    (
        "Would you try the clotted cream? It's a thick, rich English cream with a slightly caramelized flavor, "
        "essential for scones."
    ),
    (
        "This labneh has been straining for two days, creating a thick, tangy cream cheese like consistency perfect "
        "for spreading on flatbread."
    ),
    (
        "I'm making ricotta from scratch by adding acid to hot milk and straining the curds, so much fresher than "
        "store bought."
    ),
    (
        "The aged manchego from Spain has been maturing for over a year, developing crystalline texture and intense "
        "nutty, lanolin flavors."
    ),
    (
        "Would you like some kefir? It's a fermented milk drink with a tart, tangy flavor and more probiotic strains "
        "than yogurt."
    ),
    (
        "This Icelandic skyr is technically a fresh cheese, not yogurt, with an incredibly thick, creamy texture and "
        "high protein content."
    ),
    (
        "I'm whipping mascarpone with espresso and marsala for the tiramisu filling, being careful not to overbeat and "
        "make it grainy."
    ),
    (
        "The aged Comté from the Jura mountains has complex flavors of brown butter, hazelnuts, and a slight "
        "fruitiness from the alpine milk."
    ),
    (
        "Would you try the oat milk? It has a naturally sweet, creamy flavor that froths beautifully for lattes "
        "without the nuttiness."
    ),
    (
        "This Époisses cheese is washed in marc de Bourgogne brandy, giving it an orange rind and pungent, meaty, "
        "earthy flavor."
    ),
    (
        "I'm making paneer by curdling hot milk with lemon juice, then pressing the curds into a firm block for this "
        "saag paneer."
    ),
    (
        "The coconut cream has separated from the coconut milk and will be used to start this Thai curry for a richer "
        "base."
    ),
    (
        "Would you like some quark? It's a German fresh cheese that's somewhere between yogurt and cream cheese in "
        "texture and tang."
    ),
    (
        "This aged Pecorino Sardo from Sardinia has a sharper, more piquant flavor than the Roman version, perfect for "
        "grating over pasta."
    ),
    (
        "I'm churning cultured butter, which has a tangier, more complex flavor than sweet cream butter and is "
        "traditional in European baking."
    ),
    (
        "The cashew cream is blended until silky smooth and will be used as a vegan substitute for heavy cream in this "
        "pasta sauce."
    ),
    (
        "Would you try the burrata? It's a fresh mozzarella shell filled with stracciatella, shreds of mozzarella "
        "mixed with cream."
    ),
    (
        "This aged Gruyère has been maturing in caves for eighteen months, developing a crystalline texture and "
        "intense, nutty, slightly sweet flavor."
    ),
]

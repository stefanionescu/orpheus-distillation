"""Unit prompts: short prompts by kind of measure, then long cooking and recipe prompts."""

from __future__ import annotations

MEASURES: list[str] = [
    # LENGTH AND DISTANCE - SHORT
    "The table is about six feet long.",
    "She's five foot nine inches tall.",
    "Cut it to twelve centimeters exactly.",
    "The gap is only three millimeters wide.",
    "Downtown is roughly two miles away.",
    "The trail stretches for fifteen kilometers.",
    "Add another quarter inch to that measurement.",
    "The fabric comes in thirty yard rolls.",
    "The marathon is twenty six point two miles.",
    "It's about one hundred meters to the corner.",
    "The closest star is four light years away.",
    "The ship traveled fifty nautical miles overnight.",
    "That tiny screw is only five millimeters.",
    "The fence needs to be eight feet tall.",
    "The room measures fourteen by sixteen feet.",
    # WEIGHT AND MASS - SHORT
    "The baby weighs seven pounds four ounces.",
    "Add two hundred grams of flour.",
    "The package is under fifty kilograms.",
    "She lost about fifteen pounds last month.",
    "Each tablet contains five hundred milligrams.",
    "The truck can carry three tons of cargo.",
    "He weighs around twelve stone.",
    "The gold bar is one kilogram exactly.",
    "Add just a pinch, about two grams.",
    "The luggage limit is twenty three kilos.",
    "Each serving is four ounces of protein.",
    "The medication is dosed in micrograms.",
    "That's roughly half a pound of butter.",
    "The shipment weighs two metric tons.",
    "Sprinkle about fifty milligrams on top.",
    # VOLUME - SHORT
    "Pour in two cups of water.",
    "The tank holds fifty gallons of fuel.",
    "Add three tablespoons of olive oil.",
    "The bottle contains seven hundred fifty milliliters.",
    "Use half a teaspoon of salt.",
    "The pool is twenty thousand gallons.",
    "Drink at least two liters daily.",
    "The recipe calls for one pint of cream.",
    "Add six fluid ounces of milk.",
    "The container holds five quarts.",
    "That's about two hundred cubic centimeters.",
    "The engine displacement is three point five liters.",
    "Use one quarter cup of sugar.",
    "The barrel holds fifty five gallons.",
    "Measure out exactly fifteen milliliters.",
    # TEMPERATURE - SHORT
    "Preheat the oven to three fifty degrees Fahrenheit.",
    "It's negative twenty degrees Celsius outside.",
    "Body temperature is ninety eight point six degrees.",
    "Water boils at one hundred degrees Celsius.",
    "The freezer is set to zero degrees Fahrenheit.",
    "Absolute zero is negative two seventy three Kelvin.",
    "Bake at one eighty degrees Celsius for an hour.",
    "It hit forty degrees Celsius in the shade.",
    "Room temperature is about seventy two degrees Fahrenheit.",
    "The metal melts at one thousand degrees.",
    "Keep refrigerated below forty degrees Fahrenheit.",
    "Summer highs reach ninety five degrees here.",
    "The liquid nitrogen is negative one ninety six degrees Celsius.",
    "Serve the wine at fifty five degrees Fahrenheit.",
    "The fever spiked to one oh three degrees.",
    # TIME - SHORT
    "The flight takes about three hours.",
    "Wait forty five seconds between sets.",
    "The movie runs two hours fifteen minutes.",
    "Response time is under fifty milliseconds.",
    "The contract expires in eighteen months.",
    "Light takes eight minutes to reach Earth.",
    "The battery lasts roughly seventy two hours.",
    "Fermentation takes about two weeks.",
    "The process completes in three nanoseconds.",
    "Allow twenty minutes for the glue to set.",
    "The warranty covers five years.",
    "Hold the stretch for thirty seconds.",
    "The event starts at fourteen hundred hours.",
    "Each lap takes about ninety seconds.",
    "The project deadline is in six weeks.",
    # SPEED - SHORT
    "The speed limit is sixty five miles per hour.",
    "Wind gusts reached fifty kilometers per hour.",
    "Light travels at three hundred thousand kilometers per second.",
    "The boat cruises at twenty knots.",
    "Sound travels at three forty three meters per second.",
    "The car tops out at one fifty miles per hour.",
    "Walking pace is about three miles per hour.",
    "The pitch was clocked at ninety eight miles per hour.",
    "Data transfers at five gigabits per second.",
    "The plane cruises at five hundred knots.",
    "The current flows at two meters per second.",
    "Average typing speed is forty words per minute.",
    "The conveyor runs at one point five feet per second.",
    "The bullet travels at nine hundred meters per second.",
    "Heart rate is seventy two beats per minute.",
    # AREA - SHORT
    "The apartment is eight hundred square feet.",
    "The farm covers two hundred acres.",
    "Each tile is one square meter.",
    "The park spans fifty hectares.",
    "Paint coverage is four hundred square feet per gallon.",
    "The lot is a quarter acre.",
    "The screen is fifteen square inches.",
    "The country is about one million square kilometers.",
    "Solar panels need twenty square meters.",
    "The carpet is twelve square yards.",
    "The wound is about three square centimeters.",
    "The forest covers ten thousand acres.",
    "Each plot is fifty square meters.",
    "The county spans four hundred square miles.",
    "The tabletop is six square feet.",
    # PRESSURE AND FORCE - SHORT
    "Tire pressure should be thirty two PSI.",
    "Atmospheric pressure is one bar at sea level.",
    "The tank holds gas at three thousand PSI.",
    "Blood pressure reading is one twenty over eighty.",
    "The vacuum reaches negative fifteen inches of mercury.",
    "Water pressure is about sixty pounds per square inch.",
    "The regulator is set to two hundred kilopascals.",
    "Cabin pressure equals point eight atmospheres.",
    "The force required is fifty newtons.",
    "Torque specification is ninety foot pounds.",
    "The pump delivers three hundred pascals.",
    "Impact force exceeded five thousand newtons.",
    "Set the compressor to one fifty PSI.",
    "The valve opens at ten bar.",
    "Engine produces four hundred newton meters of torque.",
    # ENERGY AND POWER - SHORT
    "The meal contains about five hundred calories.",
    "Monthly usage is around eight hundred kilowatt hours.",
    "The heater outputs fifteen thousand BTUs.",
    "Each battery stores fifty watt hours.",
    "The microwave runs at one thousand watts.",
    "Solar panels generate three kilowatts peak.",
    "Energy content is four point two kilojoules per gram.",
    "The motor draws fifteen amps at full load.",
    "That snack is only one hundred calories.",
    "Generator capacity is five thousand watts.",
    "The reaction releases two hundred joules.",
    "Power consumption is about sixty watts.",
    "The engine produces three hundred horsepower.",
    "Battery capacity is five thousand milliamp hours.",
    "The circuit runs on twelve volts DC.",
    # DATA AND COMPUTING - SHORT
    "The file is about two gigabytes.",
    "Download speed is one hundred megabits per second.",
    "Storage capacity is two terabytes.",
    "RAM is sixteen gigabytes.",
    "The image is five megabytes.",
    "Bandwidth is limited to fifty kilobytes per second.",
    "The database is four hundred gigabytes.",
    "Processor speed is three point five gigahertz.",
    "Cache size is eight megabytes.",
    "The video is streaming at four thousand kilobits.",
    "Total storage is one petabyte.",
    "Latency is under five milliseconds.",
    "The app uses about two hundred megabytes.",
    "Connection speed is one gigabit per second.",
    "Each record is about five hundred bytes.",
    # ELECTRICAL - SHORT
    "Standard outlet voltage is one twenty volts.",
    "The fuse is rated for fifteen amps.",
    "Resistance measures fifty ohms.",
    "The light bulb is sixty watts.",
    "Capacitance is one hundred microfarads.",
    "The battery outputs three point seven volts.",
    "Current draw is two amps maximum.",
    "The transformer steps down to twenty four volts.",
    "Inductance is about ten millihenries.",
    "Power factor is point nine five.",
    "The charger supplies five volts at two amps.",
    "Impedance should be eight ohms.",
    "The panel produces four hundred watts.",
    "Frequency is fifty hertz in Europe.",
    "The motor runs on two forty volts.",
    # SOUND AND LIGHT - SHORT
    "The concert reached one hundred ten decibels.",
    "Normal conversation is about sixty decibels.",
    "The bulb produces eight hundred lumens.",
    "Light intensity is five hundred lux.",
    "Whisper level is around thirty decibels.",
    "The projector outputs three thousand lumens.",
    "Workplace lighting should be three hundred lux.",
    "The jet engine hits one forty decibels.",
    "Candle power is about one candela.",
    "Reading light needs fifty lumens minimum.",
    "Pain threshold is around one twenty decibels.",
    "The flashlight is one thousand lumens.",
    "Street lighting is about ten lux.",
    "The alarm sounds at eighty five decibels.",
    "Sunlight intensity is one hundred thousand lux.",
    # LONG EXAMPLES - COOKING AND RECIPES
    (
        "The recipe calls for two cups of all purpose flour, one and a half teaspoons of baking powder, and exactly "
        "three quarters of a teaspoon of salt mixed together."
    ),
    (
        "Preheat your oven to three hundred seventy five degrees Fahrenheit and bake the casserole for forty five "
        "minutes until the internal temperature reaches one sixty five degrees."
    ),
    (
        "For the marinade, combine half a cup of soy sauce, three tablespoons of honey, two teaspoons of sesame oil, "
        "and let the meat soak for at least four hours."
    ),
    (
        "The bread dough needs to rise at room temperature, around seventy five degrees Fahrenheit, for about ninety "
        "minutes until it doubles in size."
    ),
    (
        "Add two hundred fifty grams of butter, softened to room temperature, and cream it with one hundred seventy "
        "five grams of sugar for about three minutes."
    ),
    (
        "Simmer the stock at one eighty five degrees Fahrenheit for three hours, being careful not to let it reach a "
        "full boil at two twelve degrees."
    ),
    (
        "The chocolate needs to be tempered between eighty eight and ninety degrees Fahrenheit for dark chocolate to "
        "achieve that perfect snap and glossy finish."
    ),
    (
        "Pour exactly one and three quarter cups of whole milk heated to one hundred ten degrees Fahrenheit over the "
        "yeast mixture and let it bloom for five minutes."
    ),
    (
        "The pressure cooker should reach fifteen PSI before you start the twenty five minute timer for the beans to "
        "become perfectly tender."
    ),
    (
        "For candy making, heat the sugar syrup to exactly three hundred degrees Fahrenheit, which is the hard crack "
        "stage on your thermometer."
    ),
    (
        "The pizza oven runs at seven hundred degrees Fahrenheit, cooking each pie in just ninety seconds compared to "
        "fifteen minutes in a regular oven."
    ),
    (
        "Steep the tea at one hundred seventy five degrees Fahrenheit for exactly three minutes, as boiling water at "
        "two twelve degrees would make it bitter."
    ),
    (
        "The ice cream base needs to chill to forty degrees Fahrenheit before churning, which usually takes about four "
        "hours in the refrigerator."
    ),
    (
        "Proof the dough in a warm spot at eighty degrees Fahrenheit for two hours, then cold ferment at thirty eight "
        "degrees for twelve more hours."
    ),
    (
        "The sauce should reduce by half, from four cups to two cups, which takes about twenty five minutes of "
        "simmering over medium heat."
    ),
]

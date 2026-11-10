"""Unit prompts: long construction, automotive, health, and science prompts."""

from __future__ import annotations

ENGINEERING: list[str] = [
    # LONG EXAMPLES - CONSTRUCTION AND ENGINEERING
    (
        "The foundation requires concrete footings that extend forty two inches below grade, with rebar placed every "
        "sixteen inches on center."
    ),
    (
        "Standard wall studs are placed sixteen inches on center, using two by four lumber for interior walls and two "
        "by six for exterior load bearing walls."
    ),
    (
        "The beam can support a maximum load of twelve thousand pounds distributed evenly across its twenty four foot "
        "span without exceeding deflection limits."
    ),
    (
        "Roof pitch is measured as rise over run, so a four in twelve pitch rises four inches vertically for every "
        "twelve inches of horizontal distance."
    ),
    (
        "The HVAC system needs to move four hundred cubic feet per minute per ton of cooling capacity, with ductwork "
        "sized to limit velocity to nine hundred feet per minute."
    ),
    (
        "Concrete should cure at temperatures between fifty and ninety degrees Fahrenheit for at least seven days to "
        "reach seventy percent of its twenty eight day strength."
    ),
    (
        "The steel column is rated for a compression load of fifty thousand pounds per square inch with a safety "
        "factor of two point five built into the design."
    ),
    (
        "Window specifications call for a U factor of point three or less and a solar heat gain coefficient under "
        "point two five for energy code compliance."
    ),
    (
        "The sewer line must slope at a minimum of one quarter inch per foot of run, dropping four inches over a "
        "sixteen foot horizontal distance."
    ),
    (
        "Fire sprinkler systems require water pressure of at least fifteen PSI at the highest sprinkler head, with "
        "pipe sized for fifty gallons per minute flow."
    ),
    (
        "The elevator cab dimensions are six feet eight inches deep by five feet four inches wide, with a weight "
        "capacity of two thousand five hundred pounds."
    ),
    (
        "Structural lumber graded as number two or better must have a modulus of elasticity of at least one point two "
        "million pounds per square inch."
    ),
    (
        "The acoustic ceiling tiles have a noise reduction coefficient of point seven and a ceiling attenuation class "
        "rating of thirty five decibels."
    ),
    (
        "Insulation requirements specify R thirty eight in the attic, R twenty one in exterior walls, and R ten for "
        "basement walls in climate zone five."
    ),
    (
        "The reinforced concrete slab is four inches thick with number four rebar at twelve inches on center, designed "
        "to support two hundred fifty pounds per square foot."
    ),
    # LONG EXAMPLES - AUTOMOTIVE AND MECHANICAL
    (
        "The engine produces three hundred fifty horsepower at six thousand RPM and four hundred foot pounds of torque "
        "at four thousand two hundred RPM."
    ),
    (
        "Tire pressure should be set to thirty five PSI in the front and thirty two PSI in the rear when cold, adding "
        "about three PSI when the tires are warm."
    ),
    (
        "The transmission fluid should be checked at operating temperature between one eighty and two hundred degrees "
        "Fahrenheit on a level surface with the engine running."
    ),
    (
        "Fuel economy is rated at thirty two miles per gallon highway and twenty six miles per gallon city, averaging "
        "about seven point five liters per hundred kilometers."
    ),
    (
        "The brake rotors have a minimum thickness specification of twenty two millimeters and should be replaced if "
        "worn below that or if runout exceeds point zero two millimeters."
    ),
    (
        "Oil capacity is five point seven quarts with a filter change, using zero W twenty weight synthetic oil "
        "changed every seven thousand five hundred miles."
    ),
    (
        "The turbocharger spools to fifteen PSI of boost at three thousand RPM, pushing intake air temperatures to "
        "over two hundred degrees Fahrenheit."
    ),
    (
        "Wheel alignment specifications call for negative point five degrees of camber, positive two degrees of "
        "caster, and total toe of point one degrees."
    ),
    (
        "The battery is rated at seven hundred cold cranking amps at zero degrees Fahrenheit and has a reserve "
        "capacity of one hundred twenty minutes at twenty five amps."
    ),
    (
        "Spark plugs should be gapped to point zero four four inches, and the ignition timing is set at twelve degrees "
        "before top dead center at idle."
    ),
    (
        "The air conditioning system holds one point eight pounds of R134a refrigerant and operates with a high side "
        "pressure of two hundred fifty PSI."
    ),
    (
        "Coolant mixture should be fifty percent antifreeze to protect against freezing at negative thirty four "
        "degrees Fahrenheit and boiling at two sixty five degrees."
    ),
    (
        "The differential gear ratio of three point seven three to one means the driveshaft rotates three point seven "
        "three times for each rotation of the wheels."
    ),
    (
        "Suspension travel is six inches of compression and four inches of rebound, with springs rated at four hundred "
        "fifty pounds per inch."
    ),
    (
        "The exhaust manifold studs should be torqued to eighteen foot pounds in a cross pattern, then retorqued to "
        "twenty two foot pounds after the engine cools."
    ),
    # LONG EXAMPLES - HEALTH AND FITNESS
    (
        "The recommended daily intake is two thousand calories for women and two thousand five hundred calories for "
        "men with moderate activity levels."
    ),
    (
        "Blood pressure should ideally be below one twenty over eighty millimeters of mercury, with readings above one "
        "forty over ninety considered hypertension."
    ),
    (
        "For strength training, rest periods of sixty to ninety seconds between sets are ideal for hypertrophy, while "
        "three to five minutes is better for maximum strength."
    ),
    (
        "The average resting heart rate is sixty to one hundred beats per minute, with athletes often recording rates "
        "as low as forty beats per minute."
    ),
    (
        "A healthy body mass index falls between eighteen point five and twenty four point nine kilograms per square "
        "meter, though this doesn't account for muscle mass."
    ),
    (
        "Running burns approximately one hundred calories per mile, so a five mile run at an eight minute per mile "
        "pace burns about five hundred calories."
    ),
    (
        "The recommended water intake is about three point seven liters for men and two point seven liters for women "
        "daily, including water from food sources."
    ),
    (
        "Vitamin D supplementation of one thousand to two thousand international units daily is often recommended for "
        "people in northern latitudes during winter."
    ),
    (
        "Optimal sleep temperature is between sixty and sixty seven degrees Fahrenheit, with most people sleeping best "
        "around sixty five degrees."
    ),
    (
        "High intensity interval training alternates between thirty seconds at ninety percent maximum heart rate and "
        "ninety seconds at sixty percent for twenty minutes."
    ),
    (
        "Protein intake for muscle building should be point seven to one gram per pound of body weight, so a one "
        "eighty pound person needs one twenty six to one eighty grams."
    ),
    (
        "The medication dosage is calculated at five milligrams per kilogram of body weight, so a seventy kilogram "
        "patient would receive three hundred fifty milligrams."
    ),
    (
        "Normal blood glucose levels are between seventy and one hundred milligrams per deciliter when fasting and "
        "under one forty two hours after eating."
    ),
    (
        "The maximum heart rate formula subtracts your age from two twenty, so a forty year old has a theoretical "
        "maximum of one eighty beats per minute."
    ),
    (
        "Core body temperature should be maintained between ninety seven and ninety nine degrees Fahrenheit, with "
        "hypothermia beginning below ninety five degrees."
    ),
    # LONG EXAMPLES - SCIENCE AND CHEMISTRY
    (
        "Water freezes at thirty two degrees Fahrenheit or zero degrees Celsius at standard atmospheric pressure of "
        "fourteen point seven pounds per square inch."
    ),
    (
        "The molar mass of water is eighteen point zero two grams per mole, meaning one mole of water molecules weighs "
        "exactly eighteen point zero two grams."
    ),
    (
        "Standard temperature and pressure is defined as zero degrees Celsius and one hundred one point three two five "
        "kilopascals or one atmosphere."
    ),
    (
        "The speed of light in a vacuum is exactly two hundred ninety nine million seven hundred ninety two thousand "
        "four hundred fifty eight meters per second."
    ),
    (
        "Avogadro's number tells us there are six point zero two two times ten to the twenty third particles in one "
        "mole of any substance."
    ),
    (
        "Absolute zero, the lowest possible temperature, is negative four fifty nine point six seven degrees "
        "Fahrenheit or negative two seventy three point one five degrees Celsius."
    ),
    (
        "The density of water at four degrees Celsius is exactly one gram per cubic centimeter or one thousand "
        "kilograms per cubic meter."
    ),
    (
        "Gold has a melting point of one thousand nine hundred forty eight degrees Fahrenheit and a density of "
        "nineteen point three grams per cubic centimeter."
    ),
    (
        "The half life of carbon fourteen is five thousand seven hundred thirty years, making it useful for dating "
        "organic materials up to fifty thousand years old."
    ),
    (
        "Atmospheric pressure decreases by about one inch of mercury for every one thousand feet of altitude gain "
        "above sea level."
    ),
    (
        "The pH scale runs from zero to fourteen, with seven being neutral, below seven being acidic, and above seven "
        "being basic or alkaline."
    ),
    (
        "Iron melts at two thousand eight hundred degrees Fahrenheit, while aluminum melts much lower at one thousand "
        "two hundred twenty one degrees."
    ),
    (
        "One calorie is defined as the energy needed to raise one gram of water by one degree Celsius at standard "
        "atmospheric pressure."
    ),
    (
        "The Planck constant is six point six two six times ten to the negative thirty fourth joule seconds, a "
        "fundamental constant in quantum mechanics."
    ),
    (
        "Uranium two thirty five has a critical mass of about fifty two kilograms in a bare sphere for sustaining a "
        "nuclear chain reaction."
    ),
]

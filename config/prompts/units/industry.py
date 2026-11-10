"""Unit prompts: long manufacturing, sports, finance, and mixed prompts."""

from __future__ import annotations

INDUSTRY: list[str] = [
    # LONG EXAMPLES - MANUFACTURING AND INDUSTRY
    (
        "The CNC machine operates with a positioning accuracy of plus or minus point zero zero one inches and a "
        "repeatability of point zero zero zero five inches."
    ),
    (
        "Surface finish requirements specify a maximum roughness average of thirty two micro inches, achieved with a "
        "feed rate of point zero zero two inches per revolution."
    ),
    (
        "The hydraulic press delivers two hundred fifty tons of force with a cylinder bore of twelve inches and "
        "operating pressure of three thousand PSI."
    ),
    (
        "Weld specifications require a minimum tensile strength of seventy thousand pounds per square inch with a "
        "maximum porosity of point five percent by volume."
    ),
    (
        "The injection molding cycle time is eighteen seconds with a shot size of six ounces and a clamping force of "
        "three hundred tons."
    ),
    (
        "Thread specifications of one quarter twenty UNC means a quarter inch diameter with twenty threads per inch in "
        "the Unified National Coarse series."
    ),
    (
        "The heat treatment process requires holding at fifteen fifty degrees Fahrenheit for one hour per inch of "
        "thickness, then oil quenching to room temperature."
    ),
    (
        "Tolerance stack up analysis shows the assembly dimension ranges from two point nine nine five to three point "
        "zero zero five inches."
    ),
    (
        "The conveyor belt runs at one hundred twenty feet per minute, moving twelve hundred units per hour at a "
        "spacing of six inches."
    ),
    (
        "Laser cutting speed for quarter inch mild steel is eighty inches per minute at three thousand watts with "
        "nitrogen assist gas at one fifty PSI."
    ),
    (
        "The anodizing process uses a current density of twelve amps per square foot in sulfuric acid at sixty eight "
        "degrees Fahrenheit for forty five minutes."
    ),
    (
        "Paint coating thickness specification is one point two to one point eight mils, applied in three coats with "
        "fifteen minutes flash time between coats."
    ),
    (
        "The gear ratio of four to one in the gearbox reduces the input speed from eighteen hundred RPM to four fifty "
        "RPM while quadrupling the torque."
    ),
    (
        "Tensile testing showed the material yield strength at sixty two thousand PSI and ultimate tensile strength at "
        "seventy eight thousand PSI."
    ),
    (
        "The robotic arm has a reach of six feet with a payload capacity of forty four pounds and a repeatability of "
        "plus or minus point zero two millimeters."
    ),
    # LONG EXAMPLES - SPORTS AND ATHLETICS
    (
        "The Olympic swimming pool is fifty meters long and twenty five meters wide with a depth of at least two "
        "meters for diving events."
    ),
    (
        "A regulation basketball court measures ninety four feet by fifty feet with the three point line at twenty "
        "three feet nine inches from the center of the basket."
    ),
    (
        "The marathon world record is two hours one minute and nine seconds, averaging four minutes thirty seven "
        "seconds per mile over twenty six point two miles."
    ),
    (
        "Baseball pitchers throw fastballs at speeds averaging ninety three miles per hour, with some reaching over "
        "one hundred miles per hour."
    ),
    (
        "A tennis serve at one thirty miles per hour reaches the receiver in about point four seconds, leaving almost "
        "no time to react."
    ),
    "The golf hole has a diameter of four and a quarter inches, while the ball diameter is one point six eight inches.",
    (
        "Olympic weightlifting records show athletes clean and jerking over five hundred pounds, or about two hundred "
        "twenty seven kilograms."
    ),
    (
        "The pole vault world record stands at twenty feet two inches, requiring the athlete to run at over twenty "
        "miles per hour on approach."
    ),
    (
        "A hockey puck can travel at speeds over one hundred miles per hour when slapped, reaching the goal in under "
        "half a second."
    ),
    (
        "The Tour de France covers about two thousand two hundred miles over twenty three days with total climbing of "
        "over one hundred fifty thousand feet."
    ),
    (
        "Usain Bolt reached a top speed of twenty seven point eight miles per hour during his nine point five eight "
        "second one hundred meter world record."
    ),
    (
        "A regulation soccer field is between one hundred and one hundred ten yards long and between seventy and "
        "eighty yards wide."
    ),
    (
        "The bowling lane is exactly sixty feet from the foul line to the head pin, with pins spaced twelve inches "
        "apart on center."
    ),
    (
        "An NFL football must be inflated to between twelve and a half and thirteen and a half pounds per square inch "
        "and weigh fourteen to fifteen ounces."
    ),
    (
        "The shot put throwing circle has a diameter of two point one three five meters with the sixteen pound shot "
        "weighing exactly seven point two six kilograms."
    ),
    # LONG EXAMPLES - FINANCE AND ECONOMICS
    (
        "The mortgage rate of six point five percent on a three hundred thousand dollar loan results in monthly "
        "payments of one thousand eight hundred ninety six dollars."
    ),
    (
        "Annual inflation of three percent means that one hundred dollars today will have the purchasing power of only "
        "seventy four dollars in ten years."
    ),
    (
        "A price to earnings ratio of twenty five means investors are paying twenty five dollars for every one dollar "
        "of annual company earnings."
    ),
    (
        "The bond yields five percent annually with a face value of one thousand dollars, paying fifty dollars per "
        "year in two semi annual payments."
    ),
    (
        "Currency exchange rate of one point two five means one Euro equals one dollar and twenty five cents, or "
        "eighty cents per Euro."
    ),
    (
        "Compound interest at seven percent annually doubles your investment in approximately ten years, following the "
        "rule of seventy two."
    ),
    (
        "The federal funds rate at five point two five percent affects all other interest rates across the economy "
        "from credit cards to mortgages."
    ),
    (
        "A mutual fund with an expense ratio of point seven five percent charges seven dollars fifty cents annually "
        "for every one thousand dollars invested."
    ),
    (
        "The stock dropped fifteen percent from its fifty two week high of one hundred twenty dollars to its current "
        "price of one hundred two dollars."
    ),
    (
        "Retail markup of forty percent on a wholesale cost of fifty dollars results in a selling price of seventy "
        "dollars."
    ),
    (
        "The trade deficit of eight hundred billion dollars represents about three percent of the twenty seven "
        "trillion dollar gross domestic product."
    ),
    (
        "Depreciation over five years using straight line method on a fifty thousand dollar asset results in ten "
        "thousand dollars per year expense."
    ),
    (
        "Dividend yield of three point two percent on a sixty two dollar stock means annual dividends of about two "
        "dollars per share."
    ),
    (
        "Sales tax of eight point two five percent adds four dollars thirteen cents to a fifty dollar purchase, "
        "totaling fifty four dollars thirteen cents."
    ),
    (
        "A leveraged investment with a five to one ratio means a ten percent gain doubles your money, but a twenty "
        "percent loss wipes out your investment."
    ),
    # LONG EXAMPLES - MISCELLANEOUS
    (
        "The human eye can detect a single candle flame from about one point six miles away on a clear dark night with "
        "fully adapted vision."
    ),
    (
        "A typical car battery has a capacity of about sixty amp hours, meaning it can deliver one amp for sixty hours "
        "or sixty amps for one hour."
    ),
    (
        "The loudest sound ever recorded was the Krakatoa eruption at one hundred seventy two decibels, audible three "
        "thousand miles away."
    ),
    (
        "Paper thickness is measured in points or mils, with standard copy paper being about three to four mils or "
        "seventy five to one hundred microns."
    ),
    "A grain of salt weighs about sixty micrograms, and there are approximately six thousand grains in a teaspoon.",
    (
        "The tensile strength of spider silk is one point one gigapascals, stronger per weight than steel at about two "
        "hundred seventy megapascals."
    ),
    (
        "Your smartphone screen has a pixel density of about four hundred sixty pixels per inch, far beyond the three "
        "hundred PPI threshold for retina display."
    ),
    (
        "Standard shipping container dimensions are twenty feet long by eight feet wide by eight feet six inches tall, "
        "holding about one thousand cubic feet."
    ),
    (
        "The average adult has about one point two to one point five gallons of blood, or about five to six liters, "
        "circulating through the body."
    ),
    (
        "An audiophile grade vinyl record spins at thirty three and a third RPM with frequency response from twenty to "
        "twenty thousand hertz."
    ),
    (
        "The Great Wall of China stretches approximately thirteen thousand miles or twenty one thousand kilometers if "
        "you include all branches and sections."
    ),
    (
        "A barrel of oil contains forty two gallons, producing about nineteen gallons of gasoline and twelve gallons "
        "of diesel fuel when refined."
    ),
    "Diamonds are rated on the Mohs hardness scale at ten, while talc is one and fingernails are about two point five.",
    (
        "The Empire State Building is one thousand four hundred fifty four feet tall to the antenna, with one hundred "
        "two floors above ground level."
    ),
    (
        "A USB three point two Gen two connection transfers data at ten gigabits per second, fast enough to transfer a "
        "twenty five gigabyte file in twenty seconds."
    ),
]

"""Money prompts about cryptocurrency, exchange rates, comparisons, negotiations, and slang, then long examples."""

from __future__ import annotations

MARKETS: list[str] = [
    # CRYPTOCURRENCY
    "Point zero five Bitcoin.",
    "Half a Bitcoin.",
    "One point two BTC.",
    "Three Bitcoin even.",
    "Ten BTC.",
    "Twenty five Bitcoin.",
    "Zero point eight Ethereum.",
    "Two point five ETH.",
    "Ten Ethereum.",
    "Fifty ETH.",
    "One hundred Ethereum.",
    "Five hundred Litecoin.",
    "Two thousand LTC.",
    "Ten thousand Dogecoin.",
    "One million DOGE.",
    # EXCHANGE RATES & CONVERSIONS
    "One dollar equals one forty three yen.",
    "Euro to dollar is one point oh eight.",
    "Pound sterling at one twenty seven.",
    "Swiss franc trading at point eighty nine.",
    "Yuan at seven point two per dollar.",
    "Rupee at eighty three point four.",
    "Australian dollar at point sixty five.",
    "Canadian at point seventy four.",
    "Mexican peso at seventeen point five.",
    "Real at four point ninety two.",
    # PERCENTAGES & RATES
    "Interest rate is four point seven five percent.",
    "APR of eighteen point nine nine.",
    "Mortgage at six point two five.",
    "Return of twelve percent annually.",
    "Inflation running at three point four.",
    "Commission is two point five percent.",
    "Fee of one point five percent.",
    "Tax rate at twenty two percent.",
    "Discount of thirty five percent off.",
    "Markup of forty percent.",
    "Yield of five point eight percent.",
    "Growth rate of seven percent.",
    "Down payment of twenty percent.",
    "Tip at eighteen percent.",
    "Savings rate of point five percent.",
    # PRICE COMPARISONS - QUESTIONS
    "How much did you pay for that, like two hundred?",
    "Is it really worth eight thousand dollars?",
    "Did they charge you full price or was it discounted?",
    "What's the going rate, around fifty an hour?",
    "Can you believe they want three million for that dump?",
    "You paid how much, fifteen hundred for shoes?",
    "What's your budget, somewhere around ten K?",
    "Did insurance cover the whole twelve thousand?",
    "How much did you lose, like twenty grand?",
    "What's the monthly, around four fifty?",
    # PRICE REACTIONS - EXCLAMATIONS
    "Twelve thousand for a watch, are you insane!",
    "That's highway robbery at five hundred bucks!",
    "Only ninety nine cents, what a steal!",
    "Three million dollars, I nearly choked!",
    "Fifty grand for a car, absolutely not!",
    "Two hundred thousand, sold!",
    "Eight dollars for a coffee, this city is ridiculous!",
    "One point five million, we're rich!",
    "Forty five dollars for parking, unbelievable!",
    "Six figures and she said no!",
    # NEGOTIATIONS
    "Best I can do is eighteen hundred.",
    "Meet me in the middle at two twenty five.",
    "Final offer, seven thousand five hundred.",
    "Started at forty, settled on thirty two.",
    "Knock off another five hundred and we got a deal.",
    "Counter with one point two million.",
    "Won't go below fifteen grand.",
    "Pushed them down to sixty five K.",
    "Asked for ninety, got eighty five.",
    "Split the difference, call it four seventy five.",
    # CASUAL SLANG AMOUNTS
    "Dropped a hundy on dinner.",
    "Cost me two bills.",
    "Blew a stack last night.",
    "Making six figures easy.",
    "Worth a cool mil.",
    "Pocket change, maybe forty bucks.",
    "Set me back a couple grand.",
    "In the hole five hundred.",
    "Pulling a quarter mil.",
    "Scored a Benjamin.",
    "That's a dub.",
    "Gimme a fitty.",
    "Lost a rack gambling.",
    "Sitting on a bag.",
    "Made a band today.",
    # SPECIFIC DECIMAL AMOUNTS
    "Forty seven dollars and sixty three cents.",
    "One hundred twenty three point four five.",
    "Eight hundred ninety one dollars and seventeen cents.",
    "Two thousand five hundred forty four point eight nine.",
    "Five thousand three hundred twenty one dollars even.",
    "Twelve thousand four hundred fifty six point seven eight.",
    "Thirty seven thousand eight hundred ninety two point zero three.",
    "Eighty four thousand five hundred sixty seven point twelve.",
    "One hundred forty three thousand two hundred eleven point forty five.",
    "Nine hundred eighty seven thousand six hundred fifty four point thirty two.",
    # LONG STATEMENTS - VARIED CONTEXTS
    (
        "Paid twelve thousand three hundred forty five dollars and sixty seven cents for the car, plus another two "
        "thousand in taxes and registration fees last month."
    ),
    (
        "Spent about forty seven thousand on the renovation, including twenty two K for the kitchen, fifteen for "
        "bathrooms, and ten on new flooring throughout."
    ),
    (
        "Salary jumped from sixty eight thousand to ninety two thousand after the promotion, plus they threw in a "
        "fifteen percent bonus and better stock options."
    ),
    (
        "Mortgage payment is two thousand three hundred fifty a month, but with property taxes of six hundred and "
        "insurance at one eighty, total is over three grand."
    ),
    (
        "Inherited about four hundred seventy five thousand from my grandmother, put half in index funds and used the "
        "rest to pay off the house."
    ),
    (
        "Wedding cost us sixty three thousand all in, venue was eighteen, catering twelve, photography five, flowers "
        "four, and the rest on random stuff."
    ),
    (
        "Medical bills totaled one hundred forty seven thousand before insurance kicked in their eighty percent, "
        "leaving me with about twenty nine grand out of pocket."
    ),
    (
        "Portfolio is up seventeen percent this year, turned my initial fifty thousand investment into about two "
        "hundred thirty five thousand over eight years."
    ),
    (
        "Daycare runs us twenty eight hundred a month per kid, times two kids, that's sixty seven thousand two hundred "
        "annually just for childcare."
    ),
    (
        "Bought Bitcoin at four thousand three hundred, sold half at sixty two thousand, kept the rest through the "
        "crash down to sixteen thousand."
    ),
    # LONG QUESTIONS
    (
        "How is it possible that a three bedroom house in this neighborhood went from two hundred fifty thousand to "
        "seven hundred eighty thousand in just eight years?"
    ),
    (
        "Would you rather have five hundred thousand right now or a guaranteed fifty thousand every year for the next "
        "twenty years, that's a million total?"
    ),
    (
        "Did you really spend fourteen thousand on a handbag when your car payment is three months behind and you owe "
        "the IRS twelve grand?"
    ),
    (
        "What's the point of saving six hundred a month if inflation at four percent is eating away at your purchasing "
        "power faster than you can accumulate?"
    ),
    (
        "Can someone explain how my health insurance premium is eight hundred forty a month but I still have a four "
        "thousand dollar deductible to meet?"
    ),
    (
        "How do people afford million dollar homes when the average salary is only fifty five thousand and mortgage "
        "rates are hovering around seven percent?"
    ),
    (
        "Is it worth paying thirty two thousand for a new car when a certified pre owned with low mileage is going for "
        "eighteen thousand five hundred?"
    ),
    (
        "Why would anyone buy a hundred thousand dollar Tesla when you could get a reliable Toyota for twenty five K "
        "and pocket the seventy five thousand difference?"
    ),
    (
        "Doesn't it bother you that CEOs make three hundred times more than average workers, we're talking fifteen "
        "million versus fifty thousand annually?"
    ),
    (
        "Should I put the extra ten thousand toward the mortgage at four point five percent or invest it where I might "
        "get eight percent returns?"
    ),
    # LONG EXCLAMATIONS
    (
        "I cannot believe they wanted forty eight thousand dollars for that beat up truck with one hundred eighty "
        "thousand miles, absolutely delusional pricing right there!"
    ),
    (
        "Just found out my neighbor sold their house for one point two million, we bought ours for three hundred fifty "
        "K just ten years ago!"
    ),
    (
        "The audacity of charging fifteen dollars for a cocktail, eighteen for an appetizer, and forty five for an "
        "entree, that's almost eighty bucks before tip!"
    ),
    (
        "Scored these concert tickets for two hundred when scalpers were asking twelve hundred, sometimes patience "
        "really does pay off big time!"
    ),
    (
        "Lost sixty three thousand in the crypto crash and my wife still doesn't know, I've been secretly working "
        "overtime trying to make it back!"
    ),
    (
        "The contractor said repairs would be eight thousand, then called back saying actually it's twenty two "
        "thousand, nearly tripled the quote overnight!"
    ),
    (
        "Won the lottery for fifty seven million but after taxes I only walked away with thirty one million, still not "
        "complaining though obviously!"
    ),
    (
        "My student loans have ballooned from forty five thousand to seventy eight thousand because I could only "
        "afford interest payments for the first five years!"
    ),
    (
        "Finally hit a million in net worth at age forty two, took twenty years of saving twelve hundred a month plus "
        "aggressive investing!"
    ),
    (
        "The insurance company totaled my car and offered nine thousand when the replacement cost is at least "
        "seventeen thousand, complete lowball!"
    ),
    # INTERNATIONAL COMPARISONS
    (
        "Same laptop costs eight hundred dollars here but only five hundred fifty euros in Germany, that's like six "
        "hundred twenty bucks with current exchange rates."
    ),
    (
        "Apartment in Tokyo runs about one hundred fifty thousand yen monthly, which converts to roughly one thousand "
        "dollars, not bad for a major city."
    ),
    (
        "Paid three thousand two hundred Brazilian reais for the phone, equivalent to about six hundred fifty USD at "
        "today's exchange rate of four point nine."
    ),
    (
        "Dinner for two in Switzerland cost us two hundred forty Swiss francs, that's around two hundred seventy "
        "dollars, everything is expensive there."
    ),
    (
        "Bought a tailored suit in Hong Kong for four thousand HKD, only five hundred twelve dollars American, same "
        "quality would be two thousand here."
    ),
    (
        "Gas in Norway is twenty one Norwegian krone per liter, works out to about eight dollars per gallon when you "
        "do all the conversions."
    ),
    (
        "Salary offer in London was seventy five thousand pounds, which sounds amazing until you realize that's only "
        "about ninety five K in dollar terms."
    ),
    (
        "Property in Dubai was quoted at three million UAE dirhams, roughly eight hundred seventeen thousand dollars, "
        "cheaper than comparable Manhattan real estate."
    ),
    (
        "Tuition at the Korean university is twelve million won per semester, converts to about nine thousand dollars, "
        "way cheaper than American schools."
    ),
    (
        "Cab from the airport in Mexico City was five hundred pesos, literally twenty nine dollars, same ride in New "
        "York would be seventy five easily."
    ),
]

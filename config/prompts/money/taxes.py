"""Money prompts: long statements about taxes, insurance, education, and vehicles, then questions and exclamations."""

from __future__ import annotations

TAXES: list[str] = [
    # ADDITIONAL LONG - TAXES & GOVERNMENT
    (
        "Federal refund was two thousand eight hundred forty seven, but state owed three hundred ninety two, net "
        "refund after both was two thousand four hundred fifty five."
    ),
    (
        "Property taxes increased from nine thousand two hundred to eleven thousand four hundred, that's a twenty four "
        "percent jump in just two years, absolutely insane."
    ),
    (
        "Estimated quarterly taxes are six thousand two hundred each, so twenty four thousand eight hundred annually, "
        "plus another four thousand to the state every quarter."
    ),
    (
        "Capital gains tax on the stock sale was fifteen percent long term, sold for eighty thousand with a cost basis "
        "of twenty, owed nine thousand in taxes."
    ),
    (
        "Tax bracket jumped from twenty two percent to twenty four percent after the raise, but only the income above "
        "ninety five thousand is taxed at the higher rate."
    ),
    (
        "Itemized deductions totaled twenty eight thousand between mortgage interest at fourteen K, property taxes at "
        "eleven K capped at ten, and charitable giving of four K."
    ),
    (
        "Self employment tax is killing me, fifteen point three percent on top of regular income tax, total effective "
        "rate is closer to thirty eight percent."
    ),
    (
        "Estate tax exemption is currently twelve point nine two million, anything over that gets taxed at forty "
        "percent, proper planning can save the heirs millions."
    ),
    (
        "Child tax credit gave us four thousand for two kids, plus three thousand two hundred in earned income credit, "
        "significantly reduced our tax liability."
    ),
    (
        "Audit adjustment cost me eighteen thousand four hundred in back taxes plus three thousand six hundred in "
        "penalties and interest, should've kept better records."
    ),
    # ADDITIONAL LONG - INSURANCE
    (
        "Auto insurance quotes ranged from one forty two to three twenty eight monthly for the same coverage, shopping "
        "around literally saved me two thousand two hundred yearly."
    ),
    (
        "Homeowner's insurance premium jumped to four thousand eight hundred after the claim, was paying three "
        "thousand two hundred before the water damage incident last year."
    ),
    (
        "Life insurance policy costs one hundred seventy eight monthly for a two million dollar death benefit, twenty "
        "year term, locked in while I was young and healthy."
    ),
    (
        "Umbrella policy adds another million in liability coverage for only thirty two dollars a month, considering "
        "potential lawsuits it's cheap peace of mind honestly."
    ),
    (
        "Health insurance through the marketplace with subsidies is three hundred forty seven monthly, without the "
        "subsidy it would be one thousand one hundred twenty."
    ),
    (
        "Disability insurance replaces sixty percent of income if I can't work, premium is two hundred forty two "
        "monthly for a eight thousand monthly benefit."
    ),
    (
        "Pet insurance is fifty eight a month, vet visit for the emergency surgery was twelve thousand, insurance "
        "covered eighty percent after the five hundred deductible."
    ),
    (
        "Long term care insurance started at two hundred eighty monthly at age fifty five, wait until sixty and the "
        "same coverage would be four hundred twenty."
    ),
    (
        "Dental insurance maximum benefit is two thousand annually, premium is forty seven monthly, so I'm paying five "
        "sixty four for two K in coverage, barely worth it."
    ),
    (
        "Vision plan covers one exam and either glasses or contacts annually for twelve dollars a month, basically "
        "saves me about two hundred on the eye exam alone."
    ),
    # ADDITIONAL LONG - EDUCATION
    (
        "Tuition for state school is fourteen thousand eight hundred per year, out of state would be forty two "
        "thousand, huge difference for essentially the same education."
    ),
    (
        "Private school K through twelve costs twenty eight thousand annually, times thirteen years that's three "
        "hundred sixty four thousand, plus uniforms, books, and activity fees."
    ),
    (
        "MBA program total cost is one hundred forty thousand including tuition, books, and living expenses, expected "
        "salary bump should recoup that within three years."
    ),
    (
        "Community college credits at one twenty nine per credit hour versus the university at six eighty, transferred "
        "sixty credits and saved thirty three thousand dollars."
    ),
    (
        "Scholarship covered forty five thousand of the sixty two thousand tuition, loans for the remaining seventeen "
        "thousand, way better than having the full amount in debt."
    ),
    (
        "Tutoring runs eighty dollars an hour, three sessions a week at two hours each, that's four hundred eighty "
        "weekly or about two thousand monthly for SAT prep."
    ),
    (
        "Student loan interest rate is six point eight percent, compared to my parents' generation who borrowed at "
        "three point four percent, nearly double the cost."
    ),
    (
        "Work study job pays fourteen fifty an hour for fifteen hours weekly, covers about eight hundred seventy "
        "monthly toward expenses, every bit helps with the costs."
    ),
    (
        "Textbooks this semester cost eight hundred forty seven, rented three for one sixty total, bought two used for "
        "two hundred ten, still spent almost five hundred new."
    ),
    (
        "College application fees added up to nine hundred twenty for twelve schools at fifty to ninety each, plus "
        "another three hundred for score reports and transcripts."
    ),
    # ADDITIONAL LONG - VEHICLES
    (
        "Traded in the old car for twelve thousand five hundred, new one was forty two thousand, financed the twenty "
        "nine five difference at four point nine percent."
    ),
    (
        "Electric vehicle saved about two hundred monthly in gas, charging at home costs roughly forty dollars worth "
        "of electricity, versus two forty I was spending on fuel."
    ),
    (
        "Lease payment is three eighty nine for thirty six months with twelve thousand miles annually, going over "
        "costs twenty five cents per mile, adds up fast."
    ),
    (
        "Depreciation hit hard, bought for thirty eight thousand three years ago, Kelley Blue Book now shows twenty "
        "one thousand, lost seventeen grand in value."
    ),
    (
        "Used car with sixty thousand miles for nineteen thousand versus new at thirty two, the thirteen thousand "
        "savings outweighs any potential repair costs realistically."
    ),
    (
        "Registration and fees in California came to eight hundred forty seven, includes DMV fees of four hundred "
        "twenty three plus smog and miscellaneous charges."
    ),
    (
        "Mechanic quoted brake job at eleven hundred, did it myself with parts from RockAuto for three hundred twenty "
        "seven, saved nearly eight hundred in labor."
    ),
    (
        "Motorcycle insurance is only two twenty eight annually compared to the car at eighteen hundred, granted I "
        "only ride it about three thousand miles a year."
    ),
    (
        "Totaled car payout was twenty three thousand four hundred from insurance, owed nineteen K on the loan, walked "
        "away with four thousand four hundred for a new down payment."
    ),
    (
        "Extended warranty was four thousand two hundred for five years, transmission failed at year three and repair "
        "would've been eight thousand, actually worked out."
    ),
    # ADDITIONAL LONG - QUESTIONS VARIED
    (
        "Why does the dealer want fourteen thousand nine hundred for an eight year old car with one hundred twenty "
        "thousand miles when private party is only eleven K?"
    ),
    (
        "What's the actual difference between the ninety nine dollar plan and the one forty nine plan when the "
        "features look almost identical to me?"
    ),
    (
        "Did you factor in the twelve hundred in closing costs when you calculated the savings from refinancing at the "
        "lower interest rate?"
    ),
    (
        "How are you supposed to save twenty percent for a down payment when rent alone is two thousand three hundred "
        "and you only make six thousand monthly?"
    ),
    (
        "Is the forty thousand dollar kitchen renovation really going to add that much value when comps in the "
        "neighborhood are only selling for three fifty?"
    ),
    (
        "Who decided that eighteen dollars for a movie ticket plus twelve for popcorn and eight for a drink was a "
        "reasonable amount to charge?"
    ),
    (
        "Would you take the job offer at eighty five thousand in a high cost of living city or the one at sixty five "
        "in a much cheaper area?"
    ),
    (
        "Should I pay off the car loan at three point nine percent or put that extra four hundred monthly into index "
        "funds averaging seven percent?"
    ),
    (
        "What's the point of a fifteen hundred dollar iPhone when the three hundred Android does basically everything "
        "I need it to do?"
    ),
    (
        "How does anyone justify spending forty five thousand on a wedding when that could be a house down payment or "
        "three years of retirement savings?"
    ),
    # ADDITIONAL LONG - EXCLAMATIONS VARIED
    (
        "The landlord raised rent from eighteen hundred to two thousand four hundred, that's a six hundred dollar "
        "increase, thirty three percent jump in one year!"
    ),
    (
        "Just paid off the last of the student loans, final payment was eight hundred forty seven, took twelve years "
        "but I'm finally free of that debt!"
    ),
    (
        "Credit score jumped from six forty to seven eighty two after paying down thirty two thousand in credit card "
        "debt over the past two years!"
    ),
    (
        "Found a first edition book at the estate sale for three dollars, got it appraised and it's worth between four "
        "and six thousand dollars!"
    ),
    (
        "The contractor who quoted sixty five thousand ended up charging ninety two thousand with all the change "
        "orders, thirty seven percent over budget is unacceptable!"
    ),
    (
        "My side business finally hit six figures in revenue, one hundred twelve thousand last year, almost matches my "
        "W two income of one eighteen!"
    ),
    (
        "Invested five thousand in Amazon stock twenty years ago and it's now worth over four hundred thousand, wish I "
        "had put in more back then!"
    ),
    (
        "The ER visit for a minor cut that took three stitches came to four thousand eight hundred sixty three "
        "dollars, American healthcare is absolutely insane!"
    ),
    (
        "Negotiated the salary from the initial seventy two K offer up to ninety one thousand with better benefits, "
        "never accept the first number they give you!"
    ),
    (
        "House appreciated from two ninety five to seven hundred twenty five thousand in fifteen years, made more on "
        "appreciation than my entire salary over that period!"
    ),
]

"""Money prompts: long statements about planning, real estate, investing, expenses, debt, shopping, and travel."""

from __future__ import annotations

BUDGETS: list[str] = [
    # FINANCIAL PLANNING
    (
        "Maxing out the 401k at twenty three thousand annually, plus six thousand in the Roth IRA, that's twenty nine "
        "K in tax advantaged retirement savings every year."
    ),
    (
        "Emergency fund finally hit six months of expenses at thirty six thousand, took three years of putting aside a "
        "thousand bucks every single month."
    ),
    (
        "Financial advisor says I need two point three million to retire comfortably at sixty five, currently at four "
        "hundred fifty K with twenty years to go."
    ),
    (
        "HSA balance is up to eighteen thousand, been maxing it at thirty eight fifty per year, triple tax advantage "
        "and it rolls over forever."
    ),
    (
        "Set up a 529 plan for each kid with ten thousand initial deposits, adding two hundred monthly, should have "
        "about ninety K each by college."
    ),
    (
        "Net worth breakdown is house equity at three hundred K, retirement accounts at five fifty K, taxable "
        "brokerage at one twenty K, total just under a million."
    ),
    (
        "Debt payoff plan targets the credit cards first at eighteen percent, then the car at six percent, then extra "
        "payments on the three point five mortgage."
    ),
    (
        "Social Security estimate shows two thousand eight hundred monthly at full retirement, but if I wait until "
        "seventy it jumps to three thousand six hundred."
    ),
    (
        "Life insurance policy is two million coverage for a monthly premium of one hundred forty two dollars, term "
        "life for the next twenty years."
    ),
    (
        "Asset allocation is sixty percent stocks, thirty percent bonds, ten percent alternatives, rebalancing "
        "quarterly when any category drifts more than five percent."
    ),
    # REAL ESTATE
    (
        "Listed at five hundred ninety nine thousand, offered five seventy five, they countered at five eighty five, "
        "we settled at five eighty with closing costs split."
    ),
    (
        "Put down twenty percent on the four hundred thousand house, so eighty K down payment, financed three twenty "
        "at six point two five percent."
    ),
    (
        "Rental income is three thousand two hundred monthly, mortgage plus expenses run about two thousand four "
        "hundred, cash flowing eight hundred a month positive."
    ),
    (
        "HOA fees jumped from four hundred fifty to six hundred twenty five monthly because they're funding a fifteen "
        "million dollar building renovation project."
    ),
    (
        "Appraised at seven hundred twenty thousand but we owe six hundred ten on the mortgage, so only one hundred "
        "ten K in equity after nine years."
    ),
    (
        "Property taxes are eleven thousand eight hundred annually in this county, works out to about nine hundred "
        "eighty three dollars per month in escrow."
    ),
    (
        "Bought the duplex for three hundred seventy five thousand, one unit rents for eighteen hundred, the other for "
        "sixteen fifty, total income forty one thousand four hundred yearly."
    ),
    (
        "Commercial lease is forty five dollars per square foot annually, times two thousand square feet, that's "
        "ninety thousand a year or seven thousand five hundred monthly."
    ),
    (
        "Closing costs came to eighteen thousand four hundred, including eight thousand in lender fees, four thousand "
        "in title insurance, and six thousand in prepaid taxes."
    ),
    (
        "Refinanced from six point eight to four point two percent, monthly payment dropped from two thousand nine "
        "hundred to two thousand three hundred fifty."
    ),
    # BUSINESS & INVESTING
    (
        "Revenue last quarter was four point seven million, operating costs were three point two million, leaving one "
        "point five million in operating profit before taxes."
    ),
    (
        "Startup raised twelve million in Series A at a forty eight million pre money valuation, founders still own "
        "sixty two percent after dilution from the new round."
    ),
    (
        "Stock went from eighteen dollars to ninety four dollars per share in three years, turned my twenty thousand "
        "investment into over a hundred thousand."
    ),
    (
        "Franchise fee is seventy five thousand upfront, plus five percent royalty on gross sales, need minimum three "
        "hundred thousand in liquid assets to qualify."
    ),
    (
        "PE ratio of twenty two seems high but earnings growth is running at fifteen percent annually, so the PEG "
        "ratio is only one point four seven."
    ),
    (
        "Dividend yield is four point three percent, pays quarterly at ninety four cents per share, so my eight "
        "hundred shares generate three thousand a year."
    ),
    (
        "Business valuation came in at three point two million using a two point five times revenue multiple on our "
        "one point three million in annual sales."
    ),
    (
        "Angel investors put in five hundred thousand for fifteen percent equity, that values the company at three "
        "point three million post money at the seed stage."
    ),
    (
        "Cost of goods sold is forty two percent of revenue, gross margin is fifty eight percent, but after operating "
        "expenses net margin drops to just eleven percent."
    ),
    (
        "Accounts receivable is running at ninety days, need to get that down to forty five, currently have three "
        "hundred thousand tied up in unpaid invoices."
    ),
    # EVERYDAY EXPENSES
    (
        "Grocery bill averages about eight hundred fifty monthly for a family of four, up from six hundred two years "
        "ago, inflation is killing us."
    ),
    (
        "Utilities run about three hundred forty in summer with AC and two twenty in winter, plus internet at eighty "
        "five, total around four hundred monthly average."
    ),
    (
        "Filled up the tank for sixty seven dollars at three eighty nine a gallon, used to pay thirty five when gas "
        "was two ten back in twenty nineteen."
    ),
    (
        "Monthly subscriptions add up fast, Netflix at fifteen, Spotify at ten, gym at fifty, streaming services "
        "totaling about a hundred twenty dollars monthly."
    ),
    (
        "Kids' activities cost a fortune, soccer is two hundred per season, piano lessons one sixty monthly, summer "
        "camp was two thousand for two weeks."
    ),
    (
        "Date night runs us about one fifty after dinner at eighty, drinks at forty, and the babysitter at thirty for "
        "three hours."
    ),
    (
        "Phone bill for the family plan is two hundred forty monthly, four lines at sixty each, should probably switch "
        "to a cheaper carrier honestly."
    ),
    (
        "Car maintenance this year totaled about two thousand three hundred between oil changes, new tires at eight "
        "hundred, and a brake job at six fifty."
    ),
    (
        "Birthday party for the eight year old cost four hundred at the trampoline park, plus another hundred fifty on "
        "the cake and decorations at home."
    ),
    (
        "Back to school shopping hit seven hundred for two kids, new clothes at four hundred, supplies at one fifty, "
        "and backpacks at seventy five each."
    ),
    # DEBT & LOANS
    (
        "Consolidated all the credit cards into a personal loan at eight percent, was paying nineteen percent average "
        "before, saving about two hundred monthly in interest."
    ),
    (
        "Student loan balance is one hundred forty seven thousand, monthly payment is eight hundred ninety two, at "
        "this rate I'll be paying until I'm fifty three."
    ),
    (
        "Auto loan was thirty two thousand at five point nine percent for seventy two months, monthly payment is five "
        "thirty eight, still owe nineteen thousand."
    ),
    (
        "HELOC limit is one hundred thousand, drew fifty to renovate the kitchen, interest only payments are about "
        "three hundred monthly at current rates."
    ),
    (
        "Medical debt is forty three thousand from the emergency surgery, hospital set up a payment plan at four "
        "hundred monthly, zero interest for three years."
    ),
    (
        "Credit card one has twelve thousand at twenty two percent, card two has eight thousand at eighteen percent, "
        "minimum payments barely cover the interest charges."
    ),
    (
        "Borrowed fifteen thousand from the 401k for the down payment, have to repay within five years or it counts as "
        "a taxable distribution plus penalty."
    ),
    (
        "Mortgage balance is two hundred eighty nine thousand, original loan was three hundred fifty K, fourteen years "
        "of payments and only sixty one thousand in principal paid."
    ),
    (
        "Personal loan of twenty five thousand at eleven percent for sixty months is costing me five forty three "
        "monthly, total interest over the life is seven thousand five hundred."
    ),
    (
        "Debt to income ratio is forty two percent, need to get it under thirty six to qualify for the mortgage, have "
        "to pay off at least ten thousand first."
    ),
    # ADDITIONAL LONG - SHOPPING & RETAIL
    (
        "Black Friday deal was insane, got the seventy inch TV for four hundred ninety nine instead of the regular "
        "price of twelve hundred, saved over seven hundred bucks."
    ),
    (
        "Designer bag retail is three thousand two hundred but found it at the outlet for eighteen hundred, still "
        "expensive but forty four percent off is significant."
    ),
    (
        "Bulk shopping at Costco this month was four hundred twenty seven, but the per unit savings compared to "
        "regular grocery stores probably saved us a hundred fifty."
    ),
    (
        "Clearance rack find, originally marked at two hundred forty, then marked down to one twenty, then additional "
        "fifty percent off, paid sixty bucks total."
    ),
    (
        "Online order came to two hundred eighteen plus tax, but free shipping kicked in at two hundred minimum, "
        "otherwise would've been fifteen dollars delivery fee."
    ),
    (
        "Price matched at Best Buy, Amazon had it for three forty nine and they matched plus beat it by ten percent of "
        "the difference, final was three thirty nine."
    ),
    (
        "Thrift store haul was ridiculous, vintage leather jacket for forty five dollars, retails for over eight "
        "hundred, plus designer jeans for twelve bucks originally two sixty."
    ),
    (
        "Furniture set was quoted at four thousand eight hundred, negotiated to four thousand two hundred cash, then "
        "they threw in free delivery worth another one fifty."
    ),
    (
        "Extended warranty costs one forty nine for three years, repair would be at least four hundred, so actually "
        "makes financial sense for once on electronics."
    ),
    (
        "Returned the three hundred dollar item within thirty days, got full refund minus the fifteen dollar "
        "restocking fee, lesson learned to check return policies."
    ),
    # ADDITIONAL LONG - TRAVEL & VACATION
    (
        "All inclusive resort was two hundred eighty per night for seven nights, totaled one thousand nine hundred "
        "sixty for the room, food and drinks were covered."
    ),
    (
        "Flight to Tokyo was eleven hundred round trip in economy, but I used miles for the upgrade to business class "
        "which would've been five thousand extra."
    ),
    (
        "Airbnb came out cheaper than the hotel, paid nine hundred fifty for the week versus the hotel rate of one "
        "eighty nine per night times seven."
    ),
    (
        "Travel insurance was one hundred forty seven for the trip, covered up to ten thousand in cancellation, "
        "totally worth it when my flight got cancelled."
    ),
    (
        "Rental car for the week was three hundred sixty two including insurance, gas added another ninety seven, "
        "still cheaper than twelve Uber rides at forty each."
    ),
    (
        "Cruise was eighteen hundred per person double occupancy, plus another six hundred in port excursions, two "
        "fifty in tips, and three hundred at the casino."
    ),
    (
        "Backpacked through Southeast Asia for three months on eight thousand dollars total, that's about eighty nine "
        "dollars a day including flights, food, and accommodation."
    ),
    (
        "Ski trip for the family was four thousand two hundred, lift tickets alone were one eighty per person per day "
        "times four people times three days."
    ),
    (
        "Road trip cost breakdown was five hundred forty in gas, four nights of hotels at one twenty average, food "
        "around three hundred, total about fourteen hundred."
    ),
    (
        "Travel hacking saved us about three thousand on the honeymoon, used credit card points for flights and hotel "
        "status got us upgraded to the suite."
    ),
]

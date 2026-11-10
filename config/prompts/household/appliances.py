"""Household prompts: long statements about appliances, bathrooms, and upkeep."""

from __future__ import annotations

APPLIANCES: list[str] = [
    (
        "We're thinking about converting the attached garage into living space, but losing the covered parking and "
        "storage would be a significant trade off."
    ),
    (
        "The refrigerator ice maker produces ice that tastes strange, and I think the water filter needs to be "
        "replaced even though it's not due yet."
    ),
    (
        "I finally hung all the pictures and artwork that have been leaning against walls for months, and the rooms "
        "finally feel complete and decorated."
    ),
    (
        "The exterior light fixtures are corroded from years of exposure, and replacing them with weather resistant "
        "options should prevent future deterioration."
    ),
    (
        "We added a ceiling fan in the sunroom to improve air circulation, and it's made the space comfortable even "
        "during the hottest summer afternoons."
    ),
    (
        "The kitchen drawer organizers we bought don't quite fit the drawer dimensions, and I need to either return "
        "them or modify the drawers somehow."
    ),
    (
        "I've been researching different types of water heaters, comparing traditional tank, tankless, heat pump, and "
        "solar options for efficiency and cost."
    ),
    (
        "The bathroom floor grout is stained and discolored despite regular cleaning, and I'm considering using a "
        "grout pen or regrouting the entire floor."
    ),
    (
        "We installed a whole house surge protector at the electrical panel to protect all our electronics and "
        "appliances from power surges and lightning."
    ),
    (
        "The bedroom window is painted shut and won't open no matter how hard I try, and I'll need to carefully cut "
        "through the paint seal."
    ),
    (
        "I spent hours comparing paint samples on the wall at different times of day, and the color looks completely "
        "different in morning versus evening light."
    ),
    (
        "The kitchen island has no electrical outlets, which means we always have cords running across the counter "
        "from the wall outlets to use appliances."
    ),
    (
        "We're planning to add a screened porch to the back of the house, and the quotes from different contractors "
        "vary by thousands of dollars."
    ),
    (
        "The bathroom towel bar pulled out of the wall because it was only mounted to drywall, and I need to reinstall "
        "it with proper anchors."
    ),
    (
        "I finally cleaned the dishwasher filter and spray arms, and the improvement in cleaning performance was "
        "immediate and honestly kind of embarrassing."
    ),
    (
        "The living room has a cold spot near the exterior wall that makes that corner uncomfortable during winter, "
        "and I suspect it's an insulation issue."
    ),
    (
        "We added a lazy susan to the corner cabinet in the kitchen, and accessing items in that previously unusable "
        "space is so much easier now."
    ),
    (
        "The front porch light fixture is controlled by a switch inside the house, and adding a motion sensor would be "
        "more convenient for arrivals."
    ),
    (
        "I've been researching different types of kitchen backsplash materials, comparing ceramic tile, glass tile, "
        "natural stone, and peel and stick options."
    ),
    (
        "The bedroom ceiling has a crack that seems to be getting longer, and I'm not sure if it's just settling or "
        "something more concerning."
    ),
    (
        "We installed a water hammer arrestor near the washing machine to stop the loud banging noise that happened "
        "every time the valve closed."
    ),
    (
        "The bathroom vanity drawers are too shallow to hold much of anything useful, and the cabinet design wastes so "
        "much potential storage space."
    ),
    (
        "I spent the afternoon adjusting all the cabinet doors and drawers in the kitchen so they close properly and "
        "align with each other."
    ),
    (
        "The outdoor faucet handle is frozen in place and won't turn, and I'm worried about forcing it and breaking "
        "the valve or pipe inside."
    ),
    (
        "We're considering adding skylights to the dark hallway, but the roof pitch and attic configuration might make "
        "installation complicated or impossible."
    ),
    (
        "The kitchen countertop has a burn mark from a hot pan that won't come out, and I'm researching whether it can "
        "be repaired or needs replacement."
    ),
    (
        "I finally installed the new mailbox that's been sitting in the garage for six months, and the old rusted one "
        "is finally gone."
    ),
    (
        "The bathroom exhaust fan pulls air so weakly that it doesn't clear steam from the shower, and I think the "
        "motor is dying."
    ),
    (
        "We added under stair storage by installing custom drawers and cabinets, and the previously wasted space now "
        "holds so much seasonal stuff."
    ),
    (
        "The kitchen sink garbage disposal splash guard is deteriorated and gross, and replacing it with a new rubber "
        "one was a quick and cheap fix."
    ),
    (
        "I've been comparing different types of garage flooring, looking at epoxy coating, interlocking tiles, and "
        "roll out mats for durability and appearance."
    ),
    (
        "The bedroom door squeaks loudly every time it opens, and no amount of lubricant on the hinges seems to "
        "completely eliminate the noise."
    ),
    (
        "We installed a programmable timer on the outdoor lights so they turn on at dusk and off at a set time "
        "automatically every night."
    ),
    (
        "The bathroom mirror is fogging up during showers despite running the exhaust fan, and I'm considering adding "
        "a heated mirror pad behind it."
    ),
    (
        "I spent the weekend power washing the deck and applying a fresh coat of stain, and it looks almost new again "
        "after years of neglect."
    ),
    (
        "The kitchen cabinet shelves are fixed and can't be adjusted, which means there's wasted space above shorter "
        "items that could be used better."
    ),
    (
        "We're thinking about adding a mudroom bench with storage to the garage entry, but the space is tight and "
        "might not fit standard sizes."
    ),
    (
        "The dryer drum makes a squealing noise when it spins, and I think the drum support rollers or belt might need "
        "to be replaced."
    ),
    (
        "I finally fixed the wobbly toilet by tightening the floor bolts and replacing the wax ring seal that had "
        "compressed over the years."
    ),
    (
        "The living room ceiling fan remote stopped working, and replacing the batteries didn't help, so the receiver "
        "unit probably needs replacement."
    ),
    (
        "We added a kitchen pot rack hanging from the ceiling to free up cabinet space and keep frequently used "
        "cookware within easy reach."
    ),
    (
        "The bathroom tile has a few cracked pieces that I'd like to replace, but finding matching tile after so many "
        "years seems impossible."
    ),
    (
        "I've been researching different types of front doors, comparing fiberglass, steel, and wood for security, "
        "insulation, durability, and appearance."
    ),
    (
        "The bedroom closet rod is sagging from the weight of clothes, and I need to add a center support bracket to "
        "prevent it from breaking."
    ),
    (
        "We installed a reverse osmosis water filter under the kitchen sink for drinking water, and the taste "
        "difference compared to tap is significant."
    ),
    (
        "The kitchen floor has a soft spot near the dishwasher that feels spongy when you step on it, which probably "
        "means water damage underneath."
    ),
    (
        "I spent hours trying to remove the old caulk from around the bathtub before applying new silicone, and the "
        "process was tedious but necessary."
    ),
    (
        "The exterior door threshold is worn and no longer seals properly against the bottom of the door, letting in "
        "drafts and possibly water."
    ),
    (
        "We're considering replacing the builder grade light fixtures throughout the house with more stylish options "
        "that better match our taste and decor."
    ),
    (
        "The refrigerator door shelves are cracked and broken from years of use, and ordering replacement parts "
        "directly from the manufacturer was surprisingly easy."
    ),
    (
        "I finally organized the spice cabinet with tiered shelves and labeled jars, and finding the right spice while "
        "cooking is no longer frustrating."
    ),
    (
        "The bathroom toilet tank lid is cracked and I'm having trouble finding a replacement that fits this older "
        "model that's no longer manufactured."
    ),
    (
        "We added a kitchen charging station inside a cabinet with built in outlets and USB ports to keep devices "
        "organized and counters clear."
    ),
    (
        "The bedroom window blinds are broken and won't raise or lower properly, and the internal cord mechanism seems "
        "to be tangled or jammed."
    ),
    (
        "I've been comparing different types of bathroom vanity tops, looking at cultured marble, quartz, granite, and "
        "solid surface for our renovation."
    ),
    (
        "The outdoor deck railing spindles are loose and wobbly, which is a safety concern that needs to be addressed "
        "before someone leans on them."
    ),
    (
        "We installed motion sensor lights in the closets so they turn on automatically when you open the door and off "
        "when you close it."
    ),
    (
        "The kitchen sink is stained and scratched after years of use, and I'm not sure if it can be refinished or "
        "needs to be replaced."
    ),
    (
        "I spent the afternoon cleaning and organizing the garage refrigerator that had become a graveyard for "
        "forgotten leftovers and expired condiments."
    ),
    (
        "The bathroom door doesn't close properly because the house has settled and the frame is no longer square with "
        "the door."
    ),
    (
        "We're planning to update the kitchen lighting with a combination of recessed cans, pendant lights over the "
        "island, and under cabinet strips."
    ),
    (
        "The washing machine vibrates violently during the spin cycle, and I think the leveling feet need to be "
        "adjusted or the drum is unbalanced."
    ),
    (
        "I finally installed the new doorbell camera after it sat in the box for three months, and the video quality "
        "is better than expected."
    ),
]

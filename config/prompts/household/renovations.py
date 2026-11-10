"""Household prompts: long statements about renovations, exteriors, and repairs."""

from __future__ import annotations

RENOVATIONS: list[str] = [
    # LONG STATEMENTS
    (
        "The kitchen renovation has been ongoing for three months now, and we're still waiting on the custom cabinets "
        "to arrive from the manufacturer before we can finish."
    ),
    (
        "I spent the entire weekend deep cleaning the house from top to bottom, including scrubbing the grout, washing "
        "all the windows, and organizing every closet."
    ),
    (
        "The old furnace finally gave out after twenty years of service, and the replacement cost was much higher than "
        "we anticipated for a high efficiency model."
    ),
    (
        "We've been slowly updating the house room by room, starting with the bathrooms and kitchen, and eventually "
        "working our way to the bedrooms and living spaces."
    ),
    (
        "The basement flooded during the last heavy rainstorm because the sump pump failed, and we had to throw away "
        "boxes of old photos and documents."
    ),
    (
        "I've been researching different types of countertops for weeks, comparing quartz, granite, marble, and "
        "butcher block to find the best option for our kitchen."
    ),
    (
        "The previous homeowners clearly did a lot of DIY projects without permits, and now we're dealing with "
        "electrical and plumbing issues throughout the house."
    ),
    (
        "We finally replaced all the old single pane windows with double pane energy efficient ones, and the "
        "difference in noise reduction and temperature control is remarkable."
    ),
    (
        "The master bathroom remodel included a new walk in shower, double vanity, heated floors, and updated lighting "
        "fixtures that completely transformed the space."
    ),
    (
        "I've been trying to fix the garbage disposal myself by watching tutorial videos, but I think I've made the "
        "problem worse and now need to call a professional."
    ),
    (
        "The living room furniture arrangement never felt right until we moved the sectional to the opposite wall and "
        "added a new area rug to anchor the space."
    ),
    (
        "We discovered during the inspection that the roof needs to be replaced within the next two years, which "
        "wasn't something we budgeted for when buying the house."
    ),
    (
        "The laundry room renovation added so much functionality with new cabinets, a folding station, and a utility "
        "sink that makes doing laundry actually enjoyable now."
    ),
    (
        "I spent three hours trying to unclog the kitchen sink with a plunger and drain snake before finally giving up "
        "and calling a plumber to handle it."
    ),
    (
        "The home office conversion required adding more electrical outlets, better lighting, and built in shelving to "
        "create a functional workspace for remote work."
    ),
    (
        "We've been dealing with a mouse problem in the garage for months, and despite setting traps and sealing entry "
        "points, they keep finding ways to get inside."
    ),
    (
        "The deck boards are rotting and need to be replaced before summer, but we're debating between traditional "
        "wood and composite materials for the new surface."
    ),
    (
        "I finally installed the new ceiling fan in the bedroom after watching several instructional videos, and it "
        "took much longer than the estimated thirty minutes."
    ),
    (
        "The bathroom exhaust fan wasn't properly vented to the outside, which explained why we always had moisture "
        "problems and mold growth on the ceiling."
    ),
    (
        "We hired a professional organizer to help with the closets and storage spaces, and the difference in how the "
        "house functions now is absolutely incredible."
    ),
    (
        "The old carpet in the basement had a musty smell that we couldn't get rid of, so we decided to tear it out "
        "and install vinyl plank flooring instead."
    ),
    (
        "I've been comparing quotes from different contractors for the kitchen remodel, and the prices range from "
        "reasonable to absolutely outrageous for the same work."
    ),
    (
        "The dishwasher started leaking from the bottom, and by the time we noticed, the water had damaged the "
        "hardwood floor and warped several planks."
    ),
    (
        "We added a mudroom entry from the garage with built in cubbies, hooks, and a bench, which has completely "
        "eliminated the clutter that used to pile up."
    ),
    (
        "The HVAC technician recommended replacing the entire system rather than repairing the twenty year old unit, "
        "which makes sense but is a significant expense."
    ),
    (
        "I've been slowly replacing all the light fixtures in the house with modern options, and the updated lighting "
        "has made each room feel completely different."
    ),
    (
        "The guest bathroom renovation was supposed to take two weeks but stretched into six weeks due to supply chain "
        "delays and unexpected plumbing issues."
    ),
    (
        "We finally addressed the drafty windows by adding storm windows and thermal curtains, which has made a "
        "noticeable difference in our heating bills this winter."
    ),
    (
        "The kitchen pantry organization project involved installing pull out drawers, lazy susans, and clear "
        "containers that make finding ingredients so much easier now."
    ),
    (
        "I spent the weekend pressure washing the driveway, patio, and siding, and I'm amazed at how much dirt and "
        "grime had accumulated over the years."
    ),
    (
        "The water heater started leaking last week, and we had to shut off the water supply and rush to find a "
        "plumber who could come same day."
    ),
    (
        "We converted the formal dining room into a playroom for the kids since we never used it for dining anyway, "
        "and it's been a great use of space."
    ),
    (
        "The exterior paint is peeling and fading after only five years, which makes me question the quality of the "
        "paint the previous owners used on the house."
    ),
    (
        "I've been researching smart home devices to automate the lights, thermostat, and security system, but the "
        "options are overwhelming and I can't decide what to buy."
    ),
    (
        "The bathroom vanity we ordered online looked nothing like the pictures, and the return process has been a "
        "nightmare of customer service calls and shipping labels."
    ),
    (
        "We finally got around to organizing the garage with wall mounted storage, ceiling racks, and labeled bins for "
        "all the seasonal items and tools."
    ),
    (
        "The kitchen sink faucet started spraying water in random directions, and replacing the cartridge inside fixed "
        "the problem without needing a whole new fixture."
    ),
    (
        "I've been meaning to clean out the refrigerator coils for years, and when I finally did, the amount of dust "
        "and pet hair was genuinely disgusting."
    ),
    (
        "The home inspection revealed several issues we weren't aware of, including outdated electrical panels, "
        "insufficient insulation, and a crack in the foundation wall."
    ),
    (
        "We installed a water filtration system under the kitchen sink, and the improvement in taste and quality of "
        "the drinking water is immediately noticeable."
    ),
    (
        "The bedroom closet organization system we installed ourselves saved thousands of dollars compared to the "
        "custom closet company quote we received initially."
    ),
    (
        "I've been slowly replacing all the doorknobs and cabinet hardware throughout the house with matching brushed "
        "nickel finishes for a more cohesive look."
    ),
    (
        "The landscaping in the backyard has become completely overgrown, and we need to hire someone to clear it out "
        "before we can even start planning improvements."
    ),
    (
        "We added a kitchen island during the renovation, and it's become the central gathering spot for the family "
        "during meal prep and casual conversations."
    ),
    (
        "The attic fan installation has made a huge difference in keeping the upstairs cool during summer without "
        "running the air conditioning constantly all day."
    ),
    (
        "I finally tackled the junk drawer in the kitchen, and I found items we've been looking for years mixed in "
        "with batteries, rubber bands, and old receipts."
    ),
    (
        "The bathroom floor tiles are cracked and some are loose, which means we'll need to remove everything and "
        "start fresh with new underlayment and tile."
    ),
    (
        "We've been debating between a gas and electric stove for the kitchen remodel, and both options have pros and "
        "cons that make the decision difficult."
    ),
    (
        "The front porch columns are showing signs of rot at the base, and we need to address it before the structural "
        "integrity becomes compromised."
    ),
    (
        "I spent the afternoon cleaning and organizing the medicine cabinet, throwing away expired medications and "
        "finally creating a system that makes sense."
    ),
    (
        "The new refrigerator is too tall for the cabinet opening, so we had to remove the upper cabinet entirely and "
        "adjust the layout of that wall."
    ),
    (
        "We hired a chimney sweep for the first time in years, and they found a bird's nest and significant creosote "
        "buildup that could have been dangerous."
    ),
    (
        "The bathroom mirror was glued directly to the wall by the previous owners, and removing it without damaging "
        "the drywall seems nearly impossible to do."
    ),
    (
        "I've been researching different types of insulation for the attic, comparing blown in cellulose, fiberglass "
        "batts, and spray foam for our climate zone."
    ),
    (
        "The kitchen exhaust hood wasn't venting properly to the outside, which explained why cooking odors lingered "
        "in the house for hours after every meal."
    ),
    (
        "We finally replaced the old brass light fixtures and door hardware with modern matte black finishes, and it's "
        "amazing how much it updated the look."
    ),
    (
        "The basement stairs are too steep and don't meet current building codes, which could be an issue when we "
        "eventually try to sell the house."
    ),
    (
        "I've been trying to match the existing trim paint color for touch ups, but after fifteen years, the original "
        "color has faded and nothing matches."
    ),
    (
        "The dishwasher door spring broke, causing the door to slam down violently every time it's opened, and finding "
        "the replacement part has been challenging."
    ),
    (
        "We added under cabinet lighting in the kitchen, and the improvement in visibility and ambiance during food "
        "prep and evening hours is remarkable."
    ),
    (
        "The living room ceiling has a textured popcorn finish that we want to remove, but testing revealed it might "
        "contain asbestos, which complicates everything."
    ),
    (
        "I finally organized the linen closet with shelf dividers and labeled baskets, and now finding towels, sheets, "
        "and toiletries is so much easier."
    ),
    (
        "The patio door sticks and is difficult to open, and I think the frame has shifted over time, causing the door "
        "to no longer align properly."
    ),
]

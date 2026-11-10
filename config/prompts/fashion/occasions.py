"""Fashion prompts: long occasion dressing, criticism, wardrobe organization, and garment care."""

from __future__ import annotations

OCCASIONS: list[str] = [
    # LONG - OCCASION DRESSING
    (
        "Black tie events call for floor length gowns or elegant cocktail dresses for women, while men should wear a "
        "tuxedo with a bow tie, cummerbund, and formal dress shoes."
    ),
    (
        "Garden party attire typically means floral prints, pastel colors, and romantic silhouettes like midi dresses "
        "and wide leg trousers, paired with comfortable heels or wedges for grass."
    ),
    (
        "Business formal requires conservative suiting in dark colors like navy, charcoal, or black, with minimal "
        "jewelry and closed toe pumps or oxford shoes in neutral leather."
    ),
    (
        "Beach wedding guest attire should include lightweight fabrics that won't show sweat, flat sandals or wedges "
        "that won't sink in sand, and secure updos that withstand wind."
    ),
    (
        "Cocktail attire falls between casual and formal, typically meaning knee length dresses or dressy separates "
        "for women and dark suits without ties for men at evening events."
    ),
    (
        "Job interview dressing should be one level more formal than the company's everyday dress code, with "
        "conservative colors and minimal distracting accessories or strong fragrances."
    ),
    (
        "Holiday party outfits offer opportunity for festive fabrics like velvet, sequins, and metallic accents, with "
        "jewel tones like emerald, ruby, and sapphire being seasonally appropriate."
    ),
    (
        "Art gallery openings call for creative, fashion forward looks that show personal style while remaining "
        "understated enough not to compete with the artwork on display."
    ),
    (
        "Country club dress codes often require collared shirts for men and prohibit denim, athletic wear, and casual "
        "flip flops regardless of the specific event being attended."
    ),
    (
        "Destination wedding packing requires versatile pieces that work for multiple events, wrinkle resistant "
        "fabrics that travel well, and shoes comfortable enough for dancing all night."
    ),
    (
        "First date outfits should feel authentic to your personal style while making some effort, avoiding anything "
        "too revealing or uncomfortable that might create self consciousness."
    ),
    (
        "Funeral attire traditionally means black or dark colors, conservative silhouettes, and minimal jewelry, "
        "though some celebrations of life may request colorful clothing instead."
    ),
    (
        "Music festival fashion balances style with practicality, requiring comfortable shoes for standing, layers for "
        "changing temperatures, and secure bags that won't get lost in crowds."
    ),
    (
        "Award show red carpet fashion showcases designer gowns, dramatic silhouettes, and statement jewelry, with "
        "stylists and celebrities coordinating looks months in advance of events."
    ),
    (
        "Polo match attire traditionally includes sundresses and fascinators for women, with blazers and khakis for "
        "men, embracing the preppy aesthetic of the sport."
    ),
    # LONG - FASHION CRITICISM & COMMENTARY
    (
        "The collection referenced nineteenth century military uniforms with epaulettes and brass buttons, but the "
        "oversized proportions and unexpected fabrications made the historical inspiration feel thoroughly modern."
    ),
    (
        "Critics praised the designer's restraint this season, noting that the pared back color palette and focus on "
        "impeccable tailoring allowed the quality of construction to speak loudly."
    ),
    (
        "The show's theatrical presentation, featuring performers and an elaborate set design, threatened to "
        "overshadow the actual garments which were elegant but less memorable than the spectacle."
    ),
    (
        "Fashion commentators noted the collection's clear response to the current economic climate, with more "
        "versatile, wearable pieces replacing the impractical statement designs of previous seasons."
    ),
    (
        "The designer's signature maximalism was evident in every look, with clashing prints, heavy embellishments, "
        "and voluminous silhouettes creating an exuberant celebration of excess and joy."
    ),
    (
        "Industry insiders questioned whether the artistic vision translated to commercial viability, as the avant "
        "garde shapes and unconventional materials seemed unlikely to appeal to everyday consumers."
    ),
    (
        "The collection told a cohesive narrative from opening look to finale, each piece building on themes of "
        "transformation and rebirth through butterfly motifs and emerging cocoons."
    ),
    (
        "Critics noted the homage to the house's archive, with several looks directly referencing iconic designs from "
        "the founder's heyday while updating proportions for contemporary tastes."
    ),
    (
        "The sustainable credentials of the collection were prominently featured, with deadstock fabrics, natural "
        "dyes, and transparent supply chain documentation accompanying each look on the runway."
    ),
    (
        "Fashion editors highlighted the clever merchandising, with immediately wearable pieces shown alongside more "
        "editorial showstoppers that would generate media coverage and social buzz."
    ),
    (
        "The diversity on the runway was notable, with models of various ages, sizes, and backgrounds wearing designs "
        "that appeared to be genuinely constructed for different body types."
    ),
    (
        "Some felt the collection played it too safe, retreading familiar territory rather than pushing creative "
        "boundaries, though commercial buyers likely appreciated the sellable, easy pieces."
    ),
    (
        "The designer's personal narrative infused every look, with childhood photographs printed on silk and "
        "traditional crafts from their homeland incorporated into thoroughly modern silhouettes."
    ),
    (
        "Fashion critics debated whether the see through fabrics and revealing cuts were empowering expressions of "
        "body positivity or problematic objectification dressed up as liberation."
    ),
    (
        "The finale look, a hand embroidered wedding gown requiring over two thousand hours of skilled labor, "
        "demonstrated the atelier's extraordinary craftsmanship and justified haute couture pricing."
    ),
    # LONG - WARDROBE ORGANIZATION
    (
        "Organizing your closet by category first, then by color within each category, makes getting dressed faster "
        "and helps you see gaps and redundancies in your wardrobe."
    ),
    (
        "Seasonal rotation involves storing off season clothing in vacuum sealed bags or cedar chests, freeing up "
        "closet space and protecting delicate fabrics from dust and pests."
    ),
    (
        "The KonMari method encourages keeping only items that spark joy, holding each piece and thanking items you "
        "donate for their service before letting them go."
    ),
    (
        "Investing in quality hangers, particularly velvet covered slim hangers for tops and wooden hangers for "
        "jackets, preserves garment shape and maximizes closet space significantly."
    ),
    (
        "A wardrobe inventory spreadsheet tracking every item, its purchase date, cost per wear, and outfit "
        "combinations can reveal spending patterns and inform smarter future purchasing decisions."
    ),
    (
        "Proper knitwear storage means folding sweaters rather than hanging them to prevent shoulder bumps, with "
        "tissue paper between heavier items to maintain shape long term."
    ),
    (
        "Cedar blocks and lavender sachets provide natural moth protection for wool and cashmere storage, while proper "
        "cleaning before storing removes the oils that attract pests."
    ),
    (
        "Transparent shoe boxes or photographed labels help you find specific pairs without opening every container, "
        "while storing boots with shapers prevents leather from creasing."
    ),
    (
        "Drawer organizers for accessories like scarves, belts, and jewelry keep smaller items visible and accessible "
        "rather than tangled in a forgotten heap at back."
    ),
    (
        "A dedicated alteration pile near your closet entrance ensures repairs actually happen, preventing unworn "
        "pieces from languishing simply because they need minor adjustments to fit."
    ),
    (
        "Hanging tank tops and camisoles on tiered hangers saves significant space while keeping them visible, rather "
        "than having them disappear in overstuffed dresser drawers."
    ),
    (
        "Grouping outfits together rather than individual pieces can streamline morning routines, with complete looks "
        "including accessories hanging together for grab and go convenience on busy days."
    ),
    (
        "Regular closet audits every season help identify items that no longer fit your lifestyle, allowing you to "
        "donate with intention rather than accumulating unworn clothes."
    ),
    (
        "Storing delicate items like silk scarves rolled rather than folded prevents permanent creasing, while acid "
        "free tissue paper protects vintage pieces from yellowing over time."
    ),
    (
        "A small section dedicated to outfit experimentation encourages trying new combinations without the pressure "
        "of immediate commitment to wearing them outside your bedroom mirror."
    ),
    # LONG - CARE & MAINTENANCE
    (
        "Leather shoes should be stored with cedar shoe trees to absorb moisture and maintain shape, with regular "
        "conditioning to prevent cracking and preserve the natural oils."
    ),
    (
        "Cashmere should be washed by hand in cool water with baby shampoo, then laid flat on a towel to dry rather "
        "than hung where it stretches."
    ),
    (
        "Removing pilling from knitwear with a fabric comb or sweater stone regularly keeps garments looking new, "
        "while preventing pills by turning items inside out before washing."
    ),
    (
        "Steaming rather than ironing most fabrics reduces the risk of shine and scorch marks while being gentler on "
        "delicate materials like silk and synthetic blends."
    ),
    (
        "Dry cleaning should be minimized for most garments as the chemical solvents can break down fibers over time; "
        "spot cleaning and airing out between wears is gentler."
    ),
    (
        "Denim enthusiasts recommend waiting as long as possible between washes, spot treating stains and freezing "
        "jeans overnight to kill bacteria rather than machine washing frequently."
    ),
    (
        "Storing handbags stuffed with tissue paper and in dust bags preserves their shape, while keeping them upright "
        "rather than stacked prevents bottom sagging and creasing."
    ),
    (
        "White sneakers can be cleaned with a paste of baking soda and hydrogen peroxide applied with a toothbrush, "
        "then wiped clean and air dried away from heat."
    ),
    (
        "Silk should be stored away from direct sunlight which causes fading, and pressed with a cool iron on the "
        "reverse side with a pressing cloth for protection."
    ),
    (
        "Zipping zippers and closing hooks before washing prevents snagging on other garments, while mesh laundry bags "
        "protect delicate items during the machine's agitation cycle."
    ),
    (
        "Suede requires regular brushing with a specialized suede brush to maintain the nap, with protective spray "
        "applied before first wear to repel water and stains."
    ),
    (
        "Removing deodorant marks from dark clothing can be done with the foam from a fabric appropriate detergent "
        "dabbed gently rather than rubbed to avoid setting stains."
    ),
    (
        "Pearl jewelry should be wiped with a soft cloth after wearing to remove oils and put on last after perfume "
        "and hairspray which can damage their luster."
    ),
    (
        "Wool coats should be brushed with a natural bristle clothes brush after wearing to remove surface dirt and "
        "restore nap before hanging in a breathable garment bag."
    ),
    (
        "Vintage garments require extra care, with gentle handling, proper support during hanging, and professional "
        "conservation for pieces with beading, sequins, or deteriorating fabrics."
    ),
]

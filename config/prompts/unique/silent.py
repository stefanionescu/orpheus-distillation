"""Pronunciation prompts with silent letters and unusual pronunciations, short to long."""

from __future__ import annotations

SILENT: list[str] = [
    # ULTRA SHORT - SILENT LETTERS
    "Knight moves.",
    "Gnome garden.",
    "Psalm singing.",
    "Subtle hint.",
    "Honest answer.",
    "Doubt it.",
    "Knife edge.",
    "Wreck ahead.",
    "Wrong turn.",
    "Climb higher.",
    "Ghost story.",
    "Heir apparent.",
    "Debt paid.",
    "Comb through.",
    "Lamb chops.",
    # ULTRA SHORT - UNUSUAL PRONUNCIATIONS
    "Colonel speaking.",
    "Queue forming.",
    "Choir practice.",
    "Quinoa salad.",
    "Facade crumbling.",
    "Debris everywhere.",
    "Rendezvous point.",
    "Bouquet arrived.",
    "Yacht club.",
    "Chaos ensued.",
    "Genre bending.",
    "Niche market.",
    "Recipe works.",
    "Depot closed.",
    "Corps marching.",
    # SHORT - SILENT K, G, P WORDS
    "The knight knelt and knocked.",
    "Gnats gnaw at the gnarled gnome.",
    "Psychology requires pneumonia free thinking.",
    "Knee injury from knitting accident.",
    "Knapsack full of knickknacks.",
    "Sign the design with a pseudonym.",
    "Gnash your teeth at the gnat.",
    "Psalm book near the pneumatic pump.",
    "Know when to knock it off.",
    "Pterodactyl fossils are fascinating.",
    "Campaign signs everywhere now.",
    "Foreign sovereign visited recently.",
    "Reign of the benign king.",
    "Paradigm shift in the diaphragm studies.",
    "Champagne for the campaign victory.",
    # SHORT - SILENT B, W, H WORDS
    "Subtle doubt about the debt.",
    "Climb the bomb shelter stairs.",
    "Plumber found the numb thumb.",
    "Lamb in the tomb of crumbs.",
    "Wrist wrap went wrong.",
    "Wrestle with the wrinkled sword.",
    "Answer about the sword handle.",
    "Write the wrong answer twice.",
    "Hour of honest honor here.",
    "Heir to the ghostly rhyme.",
    "Rhythm of the rhinoceros.",
    "Shepherd exhibited the vehicle.",
    "Exhaust from the exhibit hall.",
    "Wreath hung near the wren.",
    "Wreck near the wrestling ring.",
    # SHORT - SILENT L, T, C WORDS
    "Salmon with calm almond sauce.",
    "Palm trees in the balmy walk.",
    "Chalk talk about yolk and folk.",
    "Half a calf could talk.",
    "Listen to the castle whistle.",
    "Fasten the often softened latch.",
    "Mortgage on the depot property.",
    "Ballet at the buffet tonight.",
    "Gourmet bouquet with rapport.",
    "Science scene in the muscle study.",
    "Scissors ascend the crescent path.",
    "Fascinate the descending audience.",
    "Would you walk to the chalk store?",
    "Should the folk talk softly?",
    "Could the salmon calm down?",
    # SHORT - UNUSUAL PRONUNCIATIONS
    "Colonel ordered the choir quinoa.",
    "Queue for the quiche and croissant.",
    "Facade of the Arkansas depot.",
    "Debris from the yacht chaos.",
    "Rendezvous at the Wednesday buffet.",
    "Entrepreneur bought the lingerie boutique.",
    "Bureau approved the resume cache.",
    "Genre of the naive fiance.",
    "Cliche apropos of the debris.",
    "Illinois Wednesday schedule changed.",
    "Epitome of the hyperbole recipe.",
    "Connecticut Worcester sauce available.",
    "Leicester chocolate is comfortable.",
    "Edinburgh February temperature dropped.",
    "Worcestershire corps arrived today.",
    # MEDIUM - MIXED SILENT LETTERS
    "The knight knew the gnome had pneumonia, and the psychology of doubt was subtly affecting the whole campaign.",
    "Honest plumber fixed the tomb's wristwatch, while the heir listened to the ghost's rhythm by the castle.",
    (
        "Salmon walked calmly past the psalm singing choir near the gnarled foreign sovereign's champagne reception at "
        "the depot."
    ),
    (
        "Subtle knife work required the wrestler to knead dough while climbing past the numb lamb's crumb covered "
        "knapsack."
    ),
    (
        "Mortgage documents from Wednesday showed the gourmet buffet ballet would fascinate the muscle bound science "
        "enthusiasts thoroughly."
    ),
    (
        "Queue formed for the colonel's quinoa quiche, while the naive entrepreneur discussed the facade's debris "
        "carefully."
    ),
    "Yacht chaos ensued when the corps discovered the rendezvous point near the Arkansas bouquet depot location.",
    (
        "Genre bending recipe epitomized the hyperbole of the comfortable Wednesday chocolate temperature in Edinburgh "
        "that February."
    ),
    "Pseudonym on the design showed the benign paradigm shift in diaphragm psychology research had finally begun.",
    "Whistle from the castle softened as the rapport between the gourmet chef and bouquet artist grew stronger.",
    (
        "Pneumatic pterodactyl exhibit showcased the fascination with scissors ascending the crescent moon shaped "
        "science display beautifully."
    ),
    "Champagne flowed at the sovereign's campaign, while the knight's knapsack held knickknacks from the foreign land.",
    "Wren near the wreath wrestled with the sword answer while writing the wrong honest hour long speech carefully.",
    "Vehicle exhausted the rhinoceros shepherd who exhibited the ghost rhythm at the heir's honor ceremony event.",
    "Calf walked half the chalk path, talking folk wisdom about yolk and palm sized salmon cooking techniques.",
    # MEDIUM - QUESTIONS WITH UNUSUAL WORDS
    (
        "Did the knight know the gnome's psychology when signing the subtle foreign design at the campaign "
        "headquarters yesterday?"
    ),
    "Would the colonel queue for quinoa quiche, or does the choir prefer the croissant debris from the facade?",
    "Can the plumber climb past the numb thumb tomb, while the heir listens to the honest ghost rhythm?",
    (
        "Should the wrestler fasten the castle whistle before the mortgage buffet ballet fascinates the science muscle "
        "crowd?"
    ),
    "Why did the yacht chaos cause the corps rendezvous to move near the Wednesday Arkansas depot location?",
    "How does the entrepreneur's naive resume cache affect the genre of the cliche apropos debris situation entirely?",
    (
        "Is the sovereign's champagne campaign paradigm shifting the benign diaphragm psychology research forward "
        "effectively now?"
    ),
    "Could the salmon walk calmly past the psalm choir, while the gnarled gnome guards the foreign depot?",
    "Does the gourmet bouquet rapport justify the subtle doubt about the knight's knapsack of knickknacks here?",
    (
        "When will the Edinburgh February temperature affect the comfortable Wednesday chocolate recipe in Connecticut "
        "Worcestershire?"
    ),
    # MEDIUM - EXCLAMATIONS WITH UNUSUAL WORDS
    (
        "The knight knocked the gnome's psychology book right into the pneumonia ward, and the subtle chaos was "
        "incredible!"
    ),
    "Colonel, the queue for quinoa quiche has created complete choir chaos near the crumbling facade debris piles now!",
    (
        "That yacht rendezvous with the corps turned into such debris filled chaos that the Wednesday depot closed "
        "entirely!"
    ),
    "The plumber's subtle climb past the numb tomb lamb revealed the most honest ghost rhythm I've ever witnessed!",
    (
        "Absolutely fascinated by how the muscle science scissors ascend the crescent, while the castle whistle "
        "softens beautifully!"
    ),
    (
        "The entrepreneur's naive facade cache created such a cliche genre debut that the resume bureau was "
        "overwhelmed completely!"
    ),
    (
        "Champagne for the sovereign's campaign, and the knight's foreign knapsack holds the most paradigm shifting "
        "psychology research!"
    ),
    (
        "That salmon walked so calmly past the psalm choir that the gnarled gnome's foreign depot visit was upstaged "
        "entirely!"
    ),
    (
        "The wrestler's castle mortgage buffet ballet debut was so gourmet that the bouquet rapport became legendary "
        "instantly!"
    ),
    (
        "Edinburgh's February temperature dropped so fast that the comfortable Wednesday chocolate recipe from "
        "Connecticut became frozen solid!"
    ),
    # LONG - SILENT K, G, P COMBINATIONS
    (
        "The knight knew the gnome had been kneeling near the knotted knife, knitting a knapsack full of knickknacks, "
        "while the gnarled design campaign signs surrounded the pneumonia ward."
    ),
    (
        "Psychology research into pseudonyms revealed that the pterodactyl paradigm shift affected the diaphragm's "
        "pneumatic response, causing the benign sovereign's foreign campaign champagne reception to be postponed."
    ),
    (
        "Gnats gnawed at the gnome's gnarled knuckles, while the knight knocked on the psychology department door, "
        "knowing the pneumonia outbreak had caused subtle doubt among the campaign staff."
    ),
    (
        "Sign the design with your pseudonym, the foreign sovereign commanded, as the benign paradigm shift in "
        "pneumatic diaphragm research fascinated the campaign's psychology experts beyond measure."
    ),
    (
        "The knight's knowledge of the gnome's psychology proved invaluable when navigating the pneumonia affected "
        "ward, where subtle campaign signs hung near gnarled trees and foreign champagne bottles."
    ),
    (
        "Kneeling near the gnarled gnome, the knight knew the psychology of doubt would affect the pneumatic "
        "pterodactyl exhibit, causing a paradigm shift in the sovereign's campaign strategy."
    ),
    (
        "Foreign champagne flowed at the campaign reception as the knight discussed the gnome's psychology with the "
        "sovereign, whose benign paradigm shift had affected diaphragm research funding globally."
    ),
    (
        "The pseudonym on the design revealed the psychology behind the pneumonia outbreak, gnawing at the campaign's "
        "credibility like gnats around a gnarled gnome's foreign garden sculpture."
    ),
    (
        "Pneumatic pterodactyl fossils near the gnome's gnarled tree fascinated the knight, who knew the psychology of "
        "the subtle paradigm shift would affect the sovereign's campaign significantly."
    ),
    (
        "Campaign signs featuring the knight, gnome, and pneumonia awareness message used psychology research funded "
        "by the foreign sovereign, whose benign diaphragm paradigm had champagne worthy results."
    ),
    # LONG - SILENT B, W, H COMBINATIONS
    (
        "The subtle doubt about the debt climbed through the plumber's mind as the numb thumb examined the bomb "
        "shelter where the lamb's tomb held ancient crumbs and dumb relics."
    ),
    (
        "Wrist wraps went wrong during the wrestling match near the wrecked sword, while the answer to the wreath "
        "mystery remained written incorrectly on the wrinkled two page document."
    ),
    (
        "Honest hour of honor brought the heir to the ghost's rhythm chamber, where the rhinoceros shepherd exhibited "
        "the vehicle near the exhausted shepherd's exhibition hall quietly."
    ),
    (
        "The subtle climb past the bomb shelter revealed the plumber's doubt about the debt, while the numb thumb "
        "traced the lamb's tomb inscription through centuries of crumbs."
    ),
    (
        "Wrestle with the wrong answer about the sword, write it twice if needed, while the wreath near the wren "
        "reminds us that wrecks happen on wrist watching days."
    ),
    (
        "Ghost rhythm echoed through the heir's honor ceremony as the honest rhinoceros shepherd exhibited the "
        "vehicle, exhausting the exhibition attendees who had waited hours for the show."
    ),
    (
        "The subtle doubt about the debt payment made the plumber climb past the numb lamb's tomb, where the bomb "
        "shelter's crumb covered floor revealed ancient thumb prints everywhere."
    ),
    (
        "Wrong answer written on the wrist wrap packaging caused the wrestler to wreck the sword display, while the "
        "wreath and wren near the wrinkled curtains went unnoticed."
    ),
    (
        "Honest heir to the ghost's rhythm honored the rhinoceros at the shepherd's exhibition, while the exhausted "
        "vehicle sat in the exhibit hall for hours without moving."
    ),
    (
        "Subtle doubt about the climbing debt made the plumber's numb thumb trace the bomb shelter's tomb inscription, "
        "where the lamb's crumbs revealed the dumb but profound truth."
    ),
]

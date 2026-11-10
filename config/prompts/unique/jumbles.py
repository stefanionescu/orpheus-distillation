"""Pronunciation prompts: long statement and question variety, then short, medium, and long combinations."""

from __future__ import annotations

JUMBLES: list[str] = [
    # ADDITIONAL LONG - STATEMENT VARIETY
    (
        "Psychology research confirms that knights who know gnomes with pneumonia often exhibit subtle doubt, "
        "especially when the colonel's choir queues for Wednesday quinoa near yacht debris facades."
    ),
    (
        "The foreign sovereign's champagne campaign featured paradigm shifting diaphragm studies funded by the "
        "colonel's corps, while the subtle knight discussed gnome psychology with the Wednesday quinoa choir queue."
    ),
    (
        "Entrepreneurs with naive resume caches often queue near debris covered facades on Wednesday, where the "
        "colonel's corps arranges yacht rendezvous and the choir practices quinoa quiche recipes together."
    ),
    (
        "Honest heirs to ghost rhythms frequently join the colonel's Wednesday rendezvous near facades, where subtle "
        "yacht debris affects the quinoa quiche queue and champagne corps celebrations equally."
    ),
    (
        "The plumber who climbed past the numb tomb lamb discovered that the colonel's Wednesday choir had been "
        "queuing for quinoa near the subtle yacht debris facade all along."
    ),
    (
        "Salmon walking calmly past palm trees reminded the colonel of the Wednesday choir queue, where subtle facade "
        "debris and yacht chaos affected the quinoa quiche rendezvous plans."
    ),
    (
        "The knight's psychology paradigm suggested that gnomes with subtle doubt often affect the colonel's Wednesday "
        "campaign, especially when the choir queues for quinoa near yacht debris facades."
    ),
    (
        "Wrestlers whose wrist wraps went wrong near castle whistles often miss the colonel's Wednesday quinoa queue, "
        "where the choir sings about subtle yacht debris and facade chaos."
    ),
    (
        "That entrepreneur's naive genre cache changed the cliche debris landscape, affecting the colonel's Wednesday "
        "quinoa quiche queue near the subtle facade where the corps arranged their yacht rendezvous."
    ),
    (
        "The honest heir's ghost rhythm connection led to the colonel's corps rendezvous, where the Wednesday choir "
        "queued for quinoa near subtle facade debris and champagne yacht chaos."
    ),
    # ADDITIONAL LONG - QUESTION VARIETY
    (
        "Has the knight's gnome psychology research affected the subtle campaign paradigm, or is the colonel's "
        "Wednesday choir still queuing for quinoa near the yacht debris and champagne facade?"
    ),
    (
        "Will the foreign sovereign's diaphragm paradigm shift influence the colonel's corps, especially when the "
        "Wednesday choir queues for quinoa near subtle facade debris and yacht chaos scenes?"
    ),
    (
        "Is the entrepreneur's naive resume cache affecting the genre of cliche debris, or should we focus on the "
        "colonel's Wednesday quinoa quiche queue near the subtle facade instead?"
    ),
    (
        "Has the honest heir joined the ghost rhythm corps at the colonel's Wednesday rendezvous, where the choir "
        "queues for quinoa near subtle facade debris and yacht chaos events?"
    ),
    (
        "Did the plumber's numb tomb lamb climb reveal anything about the colonel's Wednesday choir, who queued for "
        "quinoa near subtle yacht debris and champagne facade rendezvous points?"
    ),
    (
        "Would the calm salmon walk past the colonel's Wednesday quinoa queue, or does the subtle facade debris and "
        "yacht chaos affect the choir's champagne buffet rendezvous plans?"
    ),
    (
        "Can the knight's subtle psychology paradigm influence the gnome's doubt about the colonel's Wednesday "
        "campaign, where the choir queues for quinoa near yacht debris and champagne facades?"
    ),
    (
        "Should the wrestler's wrist wrap failure near the castle whistle affect the colonel's Wednesday quinoa queue, "
        "where the choir sings about subtle yacht debris and facade chaos events?"
    ),
    (
        "Does the entrepreneur's naive genre cache create enough cliche debris for the colonel's Wednesday quinoa "
        "quiche queue near the subtle facade, yacht chaos, and champagne corps rendezvous?"
    ),
    (
        "When did the honest heir's ghost rhythm lead to the colonel's corps rendezvous, where the Wednesday choir "
        "queued for quinoa near subtle facade debris and champagne yacht chaos?"
    ),
    # MORE SHORT - ADDITIONAL UNUSUAL WORDS
    "Indict the comptroller now.",
    "Victuals for the banquet.",
    "Segue into the next topic.",
    "Hors d'oeuvres served elegantly.",
    "Faux pas at the gala.",
    "Coup d'etat announced.",
    "Bourgeois champagne tastes.",
    "Cologne from the beret shop.",
    "Chalet near the valet parking.",
    "Debut at the depot.",
    "Gaol or jail, same thing.",
    "Quay by the queue.",
    "Dengue fever concerns.",
    "Awry plans unfolded.",
    "Mischievous little sprite.",
    "Gauge the fatigue level.",
    "Tongue the plague carefully.",
    "Isthmus near the aisle.",
    "Asthma from the rhythm.",
    "Ghastly answer indeed.",
    # MORE MEDIUM - ADDITIONAL COMBINATIONS
    (
        "The comptroller's indict went awry when the bourgeois faux pas at the chalet debut affected the beret valet "
        "significantly."
    ),
    (
        "Victuals and hors d'oeuvres from the coup d'etat banquet featured cologne scented segue introductions near "
        "the quay queue line."
    ),
    (
        "Mischievous dengue researchers studied the isthmus aisle where asthma affected the ghastly rhythm of the "
        "tongue plague samples."
    ),
    (
        "Gauge the fatigue before the debut, the comptroller suggested, as the bourgeois chalet's faux pas had created "
        "awry situations."
    ),
    (
        "The beret wearing valet served hors d'oeuvres at the coup d'etat celebration, while the segue to victuals "
        "went completely awry."
    ),
    (
        "Quay near the queue featured a gaol exhibit, and the mischievous guide discussed dengue outbreaks affecting "
        "the isthmus population."
    ),
    (
        "Asthma from the ghastly rhythm affected the tongue plague research, while the indict against the comptroller "
        "remained awry all day."
    ),
    (
        "Bourgeois cologne from the chalet debut impressed the valet, whose beret matched the hors d'oeuvres served at "
        "the faux pas gala."
    ),
    (
        "The segue from victuals to coup d'etat discussions went awry when the comptroller's indict became the "
        "evening's main topic accidentally."
    ),
    (
        "Fatigue gauges at the quay showed the queue was mischievous, while dengue concerns affected the isthmus aisle "
        "asthma research team."
    ),
    # MORE LONG - MAXIMUM WORD VARIETY
    (
        "The comptroller's indict went awry at the bourgeois chalet debut, where hors d'oeuvres and cologne created a "
        "faux pas that the beret wearing valet couldn't fix."
    ),
    (
        "Victuals served near the quay queue featured mischievous segue introductions, while the coup d'etat banquet's "
        "ghastly tongue plague discussions made everyone uncomfortable."
    ),
    (
        "Gauge the fatigue carefully before the isthmus aisle asthma study, the comptroller warned, as the dengue "
        "research had created awry situations throughout the week."
    ),
    (
        "The bourgeois valet's beret matched the cologne at the chalet debut, where hors d'oeuvres and victuals "
        "created a faux pas that segued into chaos."
    ),
    (
        "Indict the comptroller for the awry coup d'etat planning, where the ghastly tongue plague research affected "
        "the mischievous dengue team at the isthmus aisle."
    ),
    (
        "Fatigue gauges showed the quay queue was reaching capacity, while the asthma rhythm study near the gaol "
        "affected the isthmus population's health significantly."
    ),
    (
        "The knight's subtle psychology affected the gnome's paradigm, while the comptroller's indict went awry at the "
        "bourgeois chalet debut near the facade debris."
    ),
    (
        "Colonel queued for quinoa quiche as the choir sang about the comptroller's awry indict, the bourgeois faux "
        "pas creating chaos near the champagne depot."
    ),
    (
        "Victuals and hors d'oeuvres from the coup d'etat celebration featured the knight's subtle psychology "
        "insights, while the gnome discussed pneumonia paradigms quietly."
    ),
    (
        "The honest heir's ghost rhythm echoed through the bourgeois chalet, where the comptroller's indict went awry "
        "and the faux pas affected the beret valet."
    ),
    (
        "Salmon walked calmly past the quay queue as the comptroller's fatigue gauge showed awry readings, while the "
        "mischievous dengue researcher studied the isthmus aisle."
    ),
    (
        "Wednesday's rendezvous near the facade debris featured victuals from the coup d'etat banquet, where the "
        "colonel's corps discussed the comptroller's awry indict thoroughly."
    ),
    (
        "The knight knew the gnome's subtle psychology would affect the bourgeois chalet debut, where hors d'oeuvres "
        "created a faux pas near the champagne facade."
    ),
    (
        "Gauge your fatigue before the isthmus aisle asthma study, the colonel ordered, as the Wednesday quinoa queue "
        "near the facade debris had gone awry."
    ),
    (
        "The comptroller's bourgeois cologne impressed the valet at the chalet debut, where the indict went awry and "
        "victuals segued into coup d'etat discussions unexpectedly."
    ),
    (
        "Honest heir joined the quay queue where the ghastly tongue plague research affected the mischievous dengue "
        "team, while the isthmus aisle asthma rhythm study continued."
    ),
    (
        "Psychology research into the knight's subtle doubt revealed that the comptroller's awry indict at the "
        "bourgeois chalet had affected the gnome's paradigm significantly."
    ),
    (
        "The colonel's Wednesday quinoa quiche featured hors d'oeuvres from the coup d'etat banquet, where the "
        "bourgeois faux pas created debris near the facade yacht chaos."
    ),
    (
        "Victuals near the quay queue went awry when the comptroller's indict affected the mischievous dengue "
        "research, while the isthmus aisle asthma study showed ghastly results."
    ),
    (
        "The knight's subtle gnome psychology paradigm shifted at the bourgeois chalet debut, where cologne and hors "
        "d'oeuvres created a faux pas the valet couldn't ignore."
    ),
    # MORE LONG - QUESTIONS
    (
        "Did the comptroller's awry indict affect the bourgeois chalet debut, where hors d'oeuvres and cologne created "
        "a faux pas that the beret wearing valet tried to fix?"
    ),
    (
        "Would the victuals near the quay queue segue into coup d'etat discussions, or should the ghastly tongue "
        "plague research take priority over mischievous dengue concerns?"
    ),
    (
        "Can the fatigue gauge show accurate readings at the isthmus aisle asthma study, or did the comptroller's awry "
        "indict affect the bourgeois research facility entirely?"
    ),
    (
        "Should the knight's subtle psychology paradigm affect the gnome's doubt about the comptroller's awry indict "
        "at the bourgeois chalet debut near the champagne facade debris?"
    ),
    (
        "Has the colonel's Wednesday quinoa queue been affected by the comptroller's awry indict, or do the victuals "
        "and hors d'oeuvres still flow at the depot?"
    ),
    (
        "Is the honest heir's ghost rhythm related to the quay queue fatigue gauge, where the mischievous dengue "
        "researchers studied the isthmus aisle asthma patterns carefully?"
    ),
    (
        "Would the bourgeois valet's beret match the cologne at the chalet debut, or did the faux pas create a segue "
        "into awry victuals discussions unexpectedly?"
    ),
    (
        "Did the comptroller's indict go awry because the coup d'etat banquet's ghastly tongue plague research "
        "affected the mischievous dengue team at the isthmus aisle location?"
    ),
    (
        "Can the knight's subtle gnome psychology help the colonel understand the comptroller's awry indict at the "
        "Wednesday quinoa queue near the bourgeois facade debris scene?"
    ),
    (
        "Should the fatigue gauge near the quay queue be recalibrated, or did the isthmus aisle asthma study produce "
        "ghastly results that the comptroller needs to address?"
    ),
]

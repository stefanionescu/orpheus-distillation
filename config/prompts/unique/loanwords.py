"""Pronunciation prompts: long exclamations and variety, then silent letters and loanwords."""

from __future__ import annotations

LOANWORDS: list[str] = [
    # MORE LONG - EXCLAMATIONS
    (
        "The comptroller's awry indict completely ruined the bourgeois chalet debut, where hors d'oeuvres and cologne "
        "had created the most elegant faux pas the beret valet ever witnessed!"
    ),
    (
        "Victuals near the quay queue segued perfectly into coup d'etat discussions, but the ghastly tongue plague "
        "research made the mischievous dengue concerns seem trivial by comparison!"
    ),
    (
        "Incredible how the fatigue gauge at the isthmus aisle asthma study went awry when the comptroller's bourgeois "
        "indict affected the entire research facility unexpectedly!"
    ),
    (
        "The knight's subtle psychology paradigm shifted the gnome's entire worldview, just as the comptroller's awry "
        "indict created chaos at the bourgeois chalet debut near the facade!"
    ),
    (
        "Colonel's Wednesday quinoa queue was absolutely affected by the comptroller's awry indict, and now the "
        "victuals and hors d'oeuvres at the depot are in complete disarray!"
    ),
    (
        "That honest heir's ghost rhythm connection to the quay queue fatigue gauge revealed the most mischievous "
        "dengue research findings about the isthmus aisle asthma patterns ever!"
    ),
    (
        "The bourgeois valet's beret matched the cologne perfectly at the chalet debut, but the faux pas segued into "
        "such awry victuals discussions that nobody could recover!"
    ),
    (
        "Unbelievable that the comptroller's indict went awry because the coup d'etat banquet's ghastly tongue plague "
        "research completely disrupted the mischievous dengue team at the isthmus!"
    ),
    (
        "The knight's subtle gnome psychology finally helped the colonel understand the comptroller's awry indict at "
        "the Wednesday quinoa queue near the bourgeois facade debris scene!"
    ),
    (
        "That fatigue gauge near the quay queue needed recalibration so badly that the isthmus aisle asthma study "
        "produced the most ghastly results the comptroller ever saw!"
    ),
    # ADDITIONAL - EVEN MORE VARIETY
    (
        "The mischievous comptroller's awry indict at the bourgeois chalet affected the knight's subtle psychology "
        "research, while the gnome queued for Wednesday quinoa near the facade debris."
    ),
    (
        "Victuals from the coup d'etat banquet featured ghastly tongue plague samples that the colonel's choir refused "
        "to touch, while the dengue researchers studied the isthmus aisle."
    ),
    (
        "Gauge your fatigue before joining the quay queue, the honest heir suggested, as the asthma rhythm study near "
        "the gaol had produced awry results all week."
    ),
    (
        "The knight knew the colonel's subtle psychology would be affected by the comptroller's awry indict at the "
        "bourgeois chalet debut near the Wednesday quinoa facade debris."
    ),
    (
        "Hors d'oeuvres and cologne from the beret valet impressed the coup d'etat attendees, while the segue to "
        "victuals went awry due to ghastly tongue plague concerns."
    ),
    (
        "The entrepreneur's naive resume featured bourgeois chalet experience, where the comptroller's awry indict had "
        "created a faux pas that affected the Wednesday quinoa queue chaos."
    ),
    (
        "Salmon walked calmly past the comptroller as the awry indict affected the bourgeois chalet debut, while the "
        "knight discussed subtle gnome psychology near the facade debris."
    ),
    (
        "The quay queue fatigue gauge went awry when the mischievous dengue researchers discovered the isthmus aisle "
        "asthma study had ghastly implications for the tongue plague samples."
    ),
    (
        "Wednesday's colonel ordered the choir to queue for quinoa near the comptroller's bourgeois chalet, where the "
        "awry indict had created subtle facade debris chaos everywhere."
    ),
    (
        "That honest heir's ghost rhythm connection fascinated the comptroller, whose awry indict at the bourgeois "
        "chalet debut had affected the knight's gnome psychology paradigm significantly."
    ),
    # ULTRA SHORT - MORE SILENT LETTERS
    "Hymn sung beautifully.",
    "Autumn leaves falling.",
    "Column collapsed suddenly.",
    "Condemn the action.",
    "Solemn ceremony held.",
    "Handsome stranger arrived.",
    "Sandwich looks delicious.",
    "Handkerchief in pocket.",
    "Through the thorough review.",
    "Daughter caught the ball.",
    "Weight and height measured.",
    "Ought to buy dough.",
    "Brought the drought news.",
    "Wrought iron gates.",
    "Borough council meeting.",
    "Island aisle walking.",
    "Biscuit and tongue treat.",
    "Guild built the circuit.",
    "Rogue in vogue.",
    "Colleague's fatigue showing.",
    # ULTRA SHORT - MORE UNUSUAL PRONUNCIATIONS
    "Meringue for dessert.",
    "Baroque antique found.",
    "Boutique critique written.",
    "Mystique of the oblique.",
    "Physique technique improved.",
    "Reservoir nearly full.",
    "Cognac and champagne.",
    "Negligee lingerie shop.",
    "Protégé performed well.",
    "Soufflé rose perfectly.",
    "Château on the plateau.",
    "Tableau nouveau displayed.",
    "Précis of the debris.",
    "Déjà vu feeling.",
    "Bon appétit everyone!",
    "Gnocchi and bruschetta.",
    "Focaccia with prosciutto.",
    "Cappuccino or espresso?",
    "Pho and sake ordered.",
    "Karaoke tsunami fun.",
    # SHORT - GH SILENT WORDS
    "Thought through the thorough plan.",
    "Daughter caught sight of the light.",
    "Weight brought the drought concern.",
    "Height ought to be measured right.",
    "Night fight with might and sight.",
    "Bought and sought what I ought.",
    "Wrought iron through the borough.",
    "Plough through the dough and bough.",
    "Though tough, the cough was rough.",
    "Enough hiccoughs through the night.",
    "Taught and caught by the daughter.",
    "Light shone bright through the sight.",
    "Right height for the knight's flight.",
    "Sought the thought that I brought.",
    "Borough's drought brought wrought havoc.",
    # SHORT - N SILENT WORDS
    "Hymn of the autumn column.",
    "Condemn the solemn damn decision.",
    "Autumn hymn in the column hall.",
    "Solemn column stood in autumn.",
    "Damn the condemned autumn column.",
    "Hymn sung with solemn autumn tones.",
    "Column of condemn notes in autumn.",
    "Solemn damn hymn for the column.",
    "Autumn column's solemn hymn echoed.",
    "Condemn not the solemn autumn hymn.",
    # SHORT - FRENCH LOANWORDS
    "Château plateau with a nouveau tableau.",
    "Soufflé at the café entrée.",
    "Cliché résumé from the protégé.",
    "Fiancé at the negligee boutique.",
    "Faux bureau with a plateau view.",
    "Lingerie in the baroque boutique.",
    "Champagne and cognac at the château.",
    "Reservoir near the baroque château.",
    "Nouveau tableau in the bureau.",
    "Entrée cliché at the café soufflé.",
    # SHORT - ITALIAN LOANWORDS
    "Gnocchi, bruschetta, and focaccia served.",
    "Prosciutto with cappuccino espresso.",
    "Espresso cappuccino and focaccia morning.",
    "Bruschetta gnocchi at the piazza.",
    "Focaccia prosciutto with espresso shot.",
    "Cappuccino and bruschetta breakfast special.",
    "Gnocchi focaccia from the trattoria.",
    "Prosciutto wrapped gnocchi arrived.",
    "Espresso with bruschetta and prosciutto.",
    "Focaccia gnocchi cappuccino combination.",
    # SHORT - ASIAN LOANWORDS
    "Pho, sake, and sushi night.",
    "Karaoke after tsunami relief.",
    "Origami and tsunami documentary.",
    "Sake with pho and sushi.",
    "Tsunami origami art exhibition.",
    "Karaoke sake night special.",
    "Sushi pho sake combination.",
    "Origami karaoke tsunami theme.",
    "Pho tsunami relief karaoke.",
    "Sake sushi origami evening.",
    # SHORT - GERMAN LOANWORDS
    "Zeitgeist doppelgänger appeared.",
    "Kindergarten angst memories.",
    "Angst about the zeitgeist.",
    "Doppelgänger at kindergarten reunion.",
    "Zeitgeist of kindergarten angst.",
    "Angst filled doppelgänger encounter.",
    "Kindergarten zeitgeist changed.",
    "Doppelgänger angst is real.",
    "Zeitgeist kindergarten doppelgänger tale.",
    "Angst from the doppelgänger zeitgeist.",
    # MEDIUM - MIXED UNUSUAL
    (
        "The handsome colonel caught his daughter's handkerchief, while the hymn echoed through the solemn autumn "
        "column ceremony."
    ),
    (
        "Thought and thorough review brought insight through the borough's drought, though the plough through dough "
        "remained tough."
    ),
    (
        "Château plateau featured a nouveau tableau with baroque antique furniture, while the boutique critique "
        "mystified the protégé."
    ),
    (
        "Gnocchi and bruschetta arrived with focaccia prosciutto, while the cappuccino espresso warmed the autumn "
        "solemn gathering."
    ),
    (
        "Zeitgeist doppelgänger stories filled the kindergarten with angst, though the karaoke tsunami relief brought "
        "sake and pho joy."
    ),
    (
        "Champagne cognac at the reservoir château featured soufflé, while the fiancé's negligee lingerie boutique "
        "opened nearby."
    ),
    (
        "Hymn of autumn's solemn column condemned the damn drought, while the daughter caught the weight of the "
        "wrought iron."
    ),
    (
        "Baroque boutique critique mystified the oblique physique technique, while the antique reservoir champagne "
        "flowed at the château."
    ),
    (
        "Gnocchi focaccia from the trattoria paired with prosciutto, while cappuccino espresso and bruschetta "
        "completed the breakfast tableau."
    ),
    (
        "Pho sake sushi karaoke night featured origami tsunami art, while the zeitgeist doppelgänger kindergarten "
        "angst stories entertained."
    ),
    (
        "Soufflé entrée at the café cliché featured protégé's résumé, while the fiancé's faux bureau plateau view "
        "impressed everyone."
    ),
    (
        "Daughter caught sight of the light through thorough thought, while the knight's height ought to be measured "
        "right."
    ),
    (
        "Through the borough's drought, the wrought plough brought dough, though tough cough hiccoughs made the night "
        "rough enough."
    ),
    (
        "Château nouveau tableau displayed baroque antique mystique, while the boutique critique of the physique "
        "technique continued obliquely."
    ),
    (
        "Condemned solemn hymn echoed through autumn's column, while the handsome stranger's handkerchief caught the "
        "sandwich crumbs carefully."
    ),
    # MEDIUM - QUESTIONS
    "Did the daughter catch the weight of the wrought iron through the borough's drought brought havoc yesterday?",
    (
        "Would the château plateau nouveau tableau impress the baroque antique boutique critique's mystique obsessed "
        "clientele thoroughly?"
    ),
    "Can gnocchi bruschetta focaccia prosciutto pair well with cappuccino espresso at the trattoria breakfast special?",
    (
        "Should the zeitgeist doppelgänger kindergarten angst stories include karaoke tsunami relief sake pho sushi "
        "celebrations?"
    ),
    (
        "Does the champagne cognac reservoir château soufflé menu feature the fiancé's negligee lingerie boutique "
        "specials?"
    ),
    "Has the hymn of autumn's solemn column condemned the damn drought through the handsome stranger's ceremony?",
    (
        "Will the baroque boutique critique mystify the oblique physique technique of the antique reservoir château "
        "guests?"
    ),
    "Is the protégé's cliché résumé from the café entrée soufflé menu affecting the fiancé's faux bureau?",
    "Could the pho sake sushi karaoke night feature origami tsunami art with zeitgeist doppelgänger entertainment?",
    "When did the daughter catch sight of the light through thorough thought at the knight's height ceremony?",
]

"""Fashion prompts: long questions and exclamations, then short garments, fabrics, accessories, and footwear."""

from __future__ import annotations

REACTIONS: list[str] = [
    # LONG - QUESTIONS
    (
        "Do you think investing in a classic Burberry trench coat is worth the price, or are there comparable options "
        "at more accessible price points from other brands?"
    ),
    (
        "Should I have this vintage dress altered to fit my body perfectly, or does altering it diminish its value as "
        "an original piece from that era?"
    ),
    (
        "What's the best way to style a statement necklace without it competing with my face, especially since I also "
        "love wearing bold lip colors regularly?"
    ),
    (
        "Is it still considered a fashion faux pas to wear navy and black together, or has that outdated rule finally "
        "been put to rest?"
    ),
    (
        "Do you think the quality of fast fashion has improved enough to justify occasional purchases, or should I "
        "exclusively buy sustainable and secondhand going forward?"
    ),
    (
        "What accessories would you recommend to transition this summer dress into fall without looking like I'm "
        "ignoring the change of season entirely?"
    ),
    (
        "Should I build a capsule wardrobe of basics first or buy statement pieces I love and fill in around them over "
        "time?"
    ),
    (
        "Is it worth investing in designer handbags that hold their resale value, or is the initial cost too "
        "prohibitive regardless of long term return?"
    ),
    (
        "Do you think visible logos and brand names are making a comeback, or does quiet luxury remain the dominant "
        "aesthetic in high fashion circles?"
    ),
    (
        "What's the most flattering way to wear wide leg trousers when you're petite without looking completely "
        "overwhelmed by all that fabric volume?"
    ),
    (
        "Should I follow trends that don't suit my personal style just to look current, or is authenticity more "
        "important than being fashionable?"
    ),
    (
        "Is it acceptable to repeat outfits at events where you might see the same people, or does social media "
        "pressure make outfit repeating awkward?"
    ),
    (
        "Do you think hiring a personal stylist is worth the investment for someone who feels lost when it comes to "
        "developing their personal style?"
    ),
    (
        "What's the best approach to building a professional wardrobe on a budget without looking like everyone else "
        "in basic corporate uniforms?"
    ),
    (
        "Should I prioritize comfort or style when choosing everyday shoes, or have brands finally figured out how to "
        "deliver both simultaneously?"
    ),
    # LONG - EXCLAMATIONS
    (
        "That hand beaded couture gown must have taken thousands of hours to create, the level of craftsmanship and "
        "attention to detail is absolutely extraordinary and breathtaking!"
    ),
    (
        "I cannot believe she found that vintage Hermès Kelly bag at a thrift store for twenty dollars, that's the "
        "fashion find of an absolute lifetime!"
    ),
    (
        "The way that bias cut silk skirt moves is absolutely hypnotic, it's like liquid mercury flowing around her "
        "body with every step she takes!"
    ),
    (
        "Those custom dyed ostrich feather sleeves are the most dramatic, show stopping thing I've ever seen walk down "
        "a runway in my entire career!"
    ),
    (
        "The transformation from that plain black dress to a total showstopper with just accessories proves that "
        "styling is truly an art form of its own!"
    ),
    (
        "I gasped out loud when she turned around and revealed the intricate hand embroidered back panel, the surprise "
        "element was executed so perfectly!"
    ),
    (
        "That collection managed to reference the archives while feeling completely fresh and modern, which is "
        "incredibly difficult to achieve and they nailed it!"
    ),
    (
        "The unexpected pairing of that punk leather jacket with the delicate tulle ball skirt shouldn't work but it "
        "absolutely does, I'm obsessed!"
    ),
    (
        "I would sell my soul for that limited edition collaboration piece, but it sold out in literally three minutes "
        "and I'm devastated about it!"
    ),
    (
        "The fact that entire gown was constructed from recycled ocean plastic is mind blowing, you would never guess "
        "it wasn't traditional couture fabric!"
    ),
    (
        "Those hand painted silk panels transform a simple shirt into a wearable work of art, I've never seen anything "
        "so beautiful in ready to wear!"
    ),
    (
        "The precision of that tailoring is absolutely unreal, every dart and seam hits exactly where it should for "
        "the most flattering silhouette possible!"
    ),
    (
        "I cannot get over how the jewelry from her grandmother, the vintage Chanel pieces, elevate that simple outfit "
        "into something truly special and meaningful!"
    ),
    (
        "The color combinations this season are so unexpected and delicious, I never would have thought to pair those "
        "shades but now I need everything!"
    ),
    (
        "That finale wedding dress with the twenty foot hand embroidered train left everyone in the audience "
        "completely speechless, including the most jaded fashion editors!"
    ),
    # ADDITIONAL SHORT - MORE GARMENTS
    "Love the bolero jacket.",
    "Nice shrug.",
    "Cute shacket.",
    "Great gilet.",
    "Love that spencer.",
    "Nice Norfolk jacket.",
    "Cute dirndl.",
    "Great lederhosen.",
    "Love the cheongsam.",
    "Nice qipao.",
    "Cute hanbok.",
    "Great kimono.",
    "Love the yukata.",
    "Nice sari.",
    "Cute salwar kameez.",
    "Great dashiki.",
    "Love the caftan.",
    "Nice djellaba.",
    "Cute ao dai.",
    "Great kente cloth.",
    # ADDITIONAL SHORT - MORE FABRICS
    "Soft bouclé.",
    "Fine ottoman.",
    "Rich taffeta.",
    "Smooth poplin.",
    "Delicate tulle.",
    "Luxe charmeuse.",
    "Crisp piqué.",
    "Soft jersey.",
    "Fine broadcloth.",
    "Rich matelassé.",
    "Smooth batiste.",
    "Delicate eyelet.",
    "Luxe mikado.",
    "Crisp faille.",
    "Soft interlock.",
    "Fine lawn.",
    "Rich grosgrain.",
    "Smooth sateen.",
    "Delicate point d'esprit.",
    "Luxe cloqué.",
    # ADDITIONAL SHORT - MORE ACCESSORIES
    "Nice opera gloves.",
    "Love the mantilla.",
    "Great snood.",
    "Cute bandeau.",
    "Nice pince nez.",
    "Love the lorgnette.",
    "Great monocle.",
    "Cute reticule.",
    "Nice chatelaine.",
    "Love the stomacher.",
    "Great épaulettes.",
    "Cute aiguilettes.",
    "Nice fob chain.",
    "Love the boutonniére.",
    "Great spats.",
    "Cute gaiters.",
    "Nice puttees.",
    "Love the sash.",
    "Great obi.",
    "Cute tabi socks.",
    # ADDITIONAL SHORT - MORE FOOTWEAR
    "Nice ghillies.",
    "Love those spectators.",
    "Great derbies.",
    "Stunning d'Orsay pumps.",
    "Nice driving mocs.",
    "Love those huaraches.",
    "Great jodhpur boots.",
    "Nice chukkas.",
    "Cute jellies.",
    "Love those clogs.",
    "Great sabots.",
    "Nice poulaines.",
    "Cute chopines.",
    "Love those winklepickers.",
    "Great creepers.",
    "Nice brothel creepers.",
    "Cute babouches.",
    "Love those mojaris.",
    "Great kolhapuris.",
    "Nice juttis.",
]

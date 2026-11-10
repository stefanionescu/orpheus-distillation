"""Fashion prompts: medium exclamations, then long outfits, fabrics, industry, and styling advice."""

from __future__ import annotations

OUTFITS: list[str] = [
    # MEDIUM - EXCLAMATIONS
    "That vintage Dior gown is absolutely breathtaking, I'm completely speechless right now!",
    "The craftsmanship on those hand beaded sleeves must have taken hundreds of hours!",
    "I cannot believe you found that sold out bag at a random consignment shop!",
    "The way that fabric moves when you walk is absolutely mesmerizing and elegant!",
    "Those custom couture shoes are the most beautiful things I have ever seen!",
    "I'm obsessed with how perfectly that color complements your skin tone and hair!",
    "The attention to detail on that embroidery is absolutely museum quality work!",
    "I gasped out loud when I saw the price tag on that cashmere sweater!",
    "That outfit is giving major old Hollywood glamour and I am living for it!",
    "The transformation with just accessories is absolutely incredible and inspiring!",
    "I cannot get over how perfectly tailored that suit is on your frame!",
    "Those vintage earrings are the perfect finishing touch to this whole ensemble!",
    "The sustainability story behind that brand makes it even more beautiful to wear!",
    "I'm absolutely dying over the intricate lacework on that couture wedding gown!",
    "That styling choice is so unexpected but absolutely genius and fashion forward!",
    # LONG - OUTFIT DESCRIPTIONS
    (
        "She paired a crisp white poplin button down with high waisted wide leg trousers in camel wool, finishing the "
        "look with cognac leather loafers and a silk scarf tied as a belt."
    ),
    (
        "The look featured a sequined midi skirt in champagne gold paired with an oversized cashmere turtleneck in "
        "cream, accessorized with sculptural gold earrings and strappy metallic heels."
    ),
    (
        "He wore a navy double breasted blazer with brass buttons over a chambray shirt, paired with stone colored "
        "chinos and brown suede desert boots for a smart casual aesthetic."
    ),
    (
        "The ensemble consisted of a pleated chiffon maxi dress in dusty rose, layered with a cropped leather moto "
        "jacket and finished with nude pointed toe pumps and a box clutch."
    ),
    (
        "She styled the vintage band tee with a tailored houndstooth blazer, distressed boyfriend jeans, and white "
        "leather sneakers, balancing casual and polished elements effortlessly throughout the look."
    ),
    (
        "The outfit featured a forest green velvet slip dress worn over a fitted black turtleneck, paired with knee "
        "high leather boots and a structured top handle bag in burgundy."
    ),
    (
        "He combined a charcoal herringbone overcoat with a burgundy cable knit sweater, dark indigo selvedge denim, "
        "and oxford brogues in burnished tan for a sophisticated weekend look."
    ),
    (
        "The look included a puff sleeve floral midi dress in a ditsy print, styled with a woven straw tote, "
        "espadrille wedges, and layered gold pendant necklaces for summer."
    ),
    (
        "She wore an oversized camel wool coat over a black cashmere mock neck, paired with leather leggings and "
        "pointed toe ankle boots, accessorized with oversized sunglasses and a logo belt."
    ),
    (
        "The ensemble featured a satin cowl neck blouse in emerald tucked into a high waisted pencil skirt in black "
        "crepe, with patent stilettos and a vintage brooch at the collar."
    ),
    (
        "He styled the olive bomber jacket over a white crew neck tee and black slim fit jeans, finishing with white "
        "leather sneakers and a silver watch for effortless cool."
    ),
    (
        "The outfit consisted of a caped wool coat in heather grey worn over a ribbed knit dress in oatmeal, "
        "accessorized with over the knee suede boots and a crossbody saddle bag."
    ),
    (
        "She paired a structured tweed jacket with gold buttons with a silk camisole in ivory, cropped black trousers, "
        "and slingback kitten heels for a Parisian inspired aesthetic throughout."
    ),
    (
        "The look featured a linen jumpsuit in sage green with a self tie belt, styled with tan leather sandals, a "
        "raffia basket bag, and delicate gold hoop earrings."
    ),
    (
        "He wore a shawl collar cardigan in heathered navy over an Oxford cloth button down, paired with tailored "
        "khakis and penny loafers in cordovan leather for classic Americana styling."
    ),
    (
        "The ensemble included a tulle midi skirt in blush layered under a chunky cable knit sweater in cream, "
        "finished with ballet flats and a pearl headband for romantic whimsy."
    ),
    (
        "She styled the leather blazer in cognac over a graphic tee with vintage Levi's and pointed toe mules, adding "
        "a chain link necklace and structured tote for downtown edge."
    ),
    (
        "The outfit featured a brocade cocktail dress with a fit and flare silhouette in jewel tones, paired with "
        "velvet pumps and a crystal embellished minaudière for black tie elegance."
    ),
    (
        "He combined a quilted vest in navy over a flannel shirt in Stewart tartan with corduroy trousers in rust and "
        "waterproof Chelsea boots for countryside weekend dressing."
    ),
    (
        "The look consisted of a silk charmeuse blouse in cobalt with bishop sleeves tucked into a pleated leather "
        "midi skirt, accessorized with statement earrings and strappy sandals."
    ),
    # LONG - FABRIC & MATERIAL DEEP DIVES
    (
        "The hand loomed Harris tweed from the Outer Hebrides features a beautiful fleck of heather purple running "
        "through the traditional herringbone weave that's been produced there for centuries."
    ),
    (
        "Japanese Kurume kasuri fabric is created using a resist dyeing technique where threads are tied and dyed "
        "before weaving, creating distinctive blurred geometric patterns unique to each piece."
    ),
    (
        "The Fortuny pleating technique, invented by Mariano Fortuny in the early twentieth century, creates permanent "
        "micro pleats in silk that have never been successfully replicated by modern machinery."
    ),
    (
        "Peau de soie, meaning 'skin of silk' in French, is a smooth satin weave fabric with a matte finish that was "
        "traditionally used for wedding gowns and formal evening wear."
    ),
    (
        "The vicuña fiber from wild South American camelids is the rarest and most expensive natural fiber in the "
        "world, requiring ethical shearing methods to protect endangered populations."
    ),
    (
        "Chantilly lace, named after the French town where it originated, features delicate floral patterns outlined "
        "with heavier thread on a fine mesh ground of silk or cotton."
    ),
    (
        "The warp and weft of ikat fabric are tie dyed before weaving, creating the characteristic blurred edges that "
        "distinguish authentic handwoven ikat from printed imitations in the marketplace."
    ),
    (
        "Shantung silk, originally woven in China's Shandong province, has distinctive irregular slubs and a crisp "
        "hand that makes it ideal for structured formal garments and bridal wear."
    ),
    (
        "The interlocking scales of genuine crocodile leather create a distinctive pattern, with belly skins being the "
        "most prized for their symmetrical rectangular tiles and suppleness."
    ),
    (
        "Seersucker fabric achieves its puckered texture through alternating slack and tight threads during weaving, "
        "creating natural air circulation that keeps the wearer cool in humid climates."
    ),
    (
        "The Jacquard loom, invented in eighteen oh four, revolutionized textile manufacturing by using punch cards to "
        "control complex woven patterns that previously required skilled handweaving techniques."
    ),
    (
        "Genuine Venetian glass beads, made on the island of Murano using centuries old techniques, contain swirled "
        "colors and gold leaf that distinguish them from mass produced imitations worldwide."
    ),
    (
        "The nap of velvet runs in one direction, which is why velvet garments must be cut with all pieces oriented "
        "the same way to avoid color variations."
    ),
    (
        "Sea Island cotton, grown in limited quantities in the Caribbean, has extra long staple fibers that create the "
        "smoothest, most lustrous cotton fabric available in the textile world."
    ),
    (
        "The hand rolled hem on a silk scarf requires skilled artisans to fold and stitch the edge without machines, "
        "creating a subtle rounded edge that lies flat."
    ),
    # LONG - FASHION INDUSTRY & BUSINESS
    (
        "The fashion calendar has evolved to include pre fall, resort, and couture shows in addition to the "
        "traditional spring/summer and fall/winter ready to wear collections shown at major fashion weeks."
    ),
    (
        "The see now buy now model disrupted the traditional fashion calendar by making runway pieces immediately "
        "available to consumers instead of waiting six months for production and delivery."
    ),
    (
        "Fast fashion brands can take a runway design and produce a similar garment for mass market retail in as "
        "little as two weeks using global supply chains."
    ),
    (
        "The made to measure process involves taking detailed measurements and creating a pattern specifically for one "
        "client, falling between ready to wear and full bespoke tailoring in customization."
    ),
    (
        "Vertical integration in fashion means a brand controls everything from raw material sourcing to retail sales, "
        "allowing greater quality control and faster response to market trends."
    ),
    (
        "The fashion industry's environmental impact includes water pollution from dyeing processes, textile waste in "
        "landfills, and carbon emissions from global shipping of garments and materials."
    ),
    (
        "Haute couture designation is legally protected in France and requires houses to meet strict criteria "
        "including handmade garments, multiple fittings, and showing collections twice yearly in Paris."
    ),
    (
        "The resale market for luxury goods has grown exponentially, with authentication services becoming crucial to "
        "verify genuine designer items from the flood of counterfeit products."
    ),
    (
        "Capsule collections are limited edition collaborations between designers and retailers or between fashion "
        "houses and celebrities that generate buzz and often sell out immediately."
    ),
    (
        "The atelier system trains apprentices in traditional couture techniques like hand sewing, beading, and "
        "embroidery over many years before they become qualified petites mains artisans."
    ),
    (
        "Showroom appointments during market weeks allow buyers from department stores and boutiques to view "
        "collections and place wholesale orders for the upcoming retail season."
    ),
    (
        "The fashion industry increasingly uses artificial intelligence for trend forecasting, analyzing social media "
        "data and street style photography to predict upcoming consumer preferences accurately."
    ),
    (
        "Deadstock fabric refers to unused surplus material from fashion production that sustainable brands repurpose "
        "to create limited edition pieces while reducing textile waste in landfills."
    ),
    (
        "The sample size used in runway shows and photo shoots is typically a size two or four, which has sparked "
        "ongoing debates about size diversity and representation."
    ),
    (
        "Licensing agreements allow fashion brands to extend into categories like eyewear, fragrance, and home goods "
        "by partnering with specialized manufacturers under the designer's name."
    ),
    # LONG - STYLING ADVICE
    (
        "When building a capsule wardrobe, invest in quality neutral basics that mix and match easily, then add "
        "personality through accessories and statement pieces each season."
    ),
    (
        "The rule of thirds suggests dividing your outfit visually into three parts, with either the top or bottom "
        "taking up two thirds for balanced and flattering proportions."
    ),
    (
        "Tonal dressing in varying shades of one color family creates an elongating effect and sophisticated look, "
        "while adding texture prevents the monochromatic outfit from appearing flat."
    ),
    (
        "When mixing patterns, vary the scale so one print is larger and one smaller, and ensure they share at least "
        "one common color to unify the look."
    ),
    (
        "A tailored blazer instantly elevates casual pieces like jeans and a t shirt, making it one of the most "
        "versatile investment pieces in any wardrobe regardless of style."
    ),
    (
        "The third piece rule suggests every outfit benefits from an additional layer like a jacket, cardigan, or "
        "scarf that adds visual interest and completes the overall look."
    ),
    (
        "Cuffing your jeans creates a deliberate, styled appearance and allows you to show off your footwear while "
        "also adjusting the length without permanent alterations to hemlines."
    ),
    (
        "Statement jewelry should be balanced with simpler clothing to avoid overwhelming the eye, while minimal "
        "outfits can handle bolder, more elaborate accessory choices without competition."
    ),
    (
        "Half tucking a shirt, where only the front is tucked in, creates a relaxed silhouette while still defining "
        "the waist and showing off belt or trouser details."
    ),
    (
        "Investing in quality footwear matters because shoes are often the first thing people notice, and well "
        "maintained leather shoes elevate even the most casual outfit significantly."
    ),
    (
        "The pop of color technique involves introducing one vibrant accent piece to an otherwise neutral outfit, "
        "immediately drawing the eye and adding personality to basics."
    ),
    (
        "Layering delicate necklaces of varying lengths creates a personalized jewelry moment, but keeping earrings "
        "and bracelets minimal prevents the accessories from competing with each other."
    ),
    (
        "French tucking, popularized by stylists, involves tucking just the front center of your shirt into your "
        "waistband to create a relaxed but intentional silhouette."
    ),
    (
        "When wearing prints, keeping your accessories in solid colors found within the pattern creates cohesion "
        "without the visual noise of competing designs and patterns."
    ),
    (
        "Rolling your sleeves once or twice creates a more relaxed and approachable look while also showing off "
        "watches and bracelets that might otherwise be hidden."
    ),
]

"""Art prompts: long statements and long questions."""

from __future__ import annotations

APPRECIATION: list[str] = [
    # LONG STATEMENTS
    (
        "Leonardo da Vinci spent over four years working on the Mona Lisa, and scholars believe he continued refining "
        "it until his death, never truly considering it finished."
    ),
    (
        "The Impressionist painters were initially rejected by the official Paris Salon, so they organized their own "
        "independent exhibitions that eventually revolutionized the art world."
    ),
    (
        "Vincent van Gogh created over two thousand artworks during his lifetime, including around eight hundred oil "
        "paintings, most produced during the final two years before his death."
    ),
    (
        "Michelangelo painted the Sistine Chapel ceiling while lying on his back on scaffolding, and the physical "
        "strain caused lasting damage to his neck and eyesight."
    ),
    (
        "The Dutch Masters achieved their luminous effects by building up thin layers of transparent glazes over "
        "carefully prepared underlayers, a technique that took years to master."
    ),
    (
        "Frida Kahlo began painting seriously after a devastating bus accident left her bedridden for months, using a "
        "mirror attached to her bed to create self portraits."
    ),
    (
        "The Pointillist technique developed by Seurat requires placing thousands of tiny dots of pure color that the "
        "viewer's eye blends together from a distance."
    ),
    (
        "Rembrandt's later self portraits are considered among the most honest and psychologically penetrating works "
        "in art history, revealing his aging and financial decline."
    ),
    (
        "The Pre Raphaelite Brotherhood chose their name to reject the academic traditions that dominated art since "
        "Raphael, seeking instead medieval purity and naturalistic detail."
    ),
    (
        "Claude Monet's obsession with capturing changing light led him to paint the same subjects repeatedly at "
        "different times of day and in different seasons."
    ),
    (
        "The invention of portable paint tubes in the 1840s freed artists from their studios and made the plein air "
        "painting of the Impressionists possible."
    ),
    (
        "Caravaggio's dramatic use of light emerging from darkness, known as tenebrism, influenced countless artists "
        "and became a defining characteristic of Baroque painting."
    ),
    (
        "Jackson Pollock developed his drip technique by laying canvases on the floor and using sticks and hardened "
        "brushes to fling and pour paint across the surface."
    ),
    (
        "The golden ratio, approximately 1.618 to 1, appears throughout Renaissance paintings in the proportions of "
        "figures, architectural elements, and overall composition."
    ),
    (
        "Vermeer's domestic scenes are remarkable for their intimate atmosphere and the way light enters through "
        "windows to illuminate the quiet moments of daily life."
    ),
    (
        "The Baroque period emerged as a response to the Protestant Reformation, with Catholic churches commissioning "
        "dramatic, emotionally engaging art to inspire religious devotion."
    ),
    (
        "Georgia O'Keeffe's enlarged flower paintings force viewers to see the intricate details and sensuous forms "
        "that we usually overlook when glancing at actual flowers."
    ),
    (
        "The Abstract Expressionists believed that the act of painting itself was more important than the finished "
        "product, emphasizing gesture, spontaneity, and emotional authenticity."
    ),
    (
        "Hieronymus Bosch's fantastical imagery in The Garden of Earthly Delights continues to puzzle art historians "
        "who debate whether it's a moral warning or celebration."
    ),
    (
        "The Hudson River School painters like Thomas Cole and Frederic Church portrayed American wilderness as a new "
        "Eden, promoting both nationalism and environmental awareness."
    ),
    (
        "Titian's revolutionary approach to color and loose brushwork in his later paintings anticipated techniques "
        "that wouldn't become common until the Impressionist movement centuries later."
    ),
    (
        "The camera obscura, a device that projects images through a small hole, was used by Vermeer and other Dutch "
        "painters to achieve photographic accuracy."
    ),
    (
        "Mary Cassatt's paintings of mothers and children challenged the male dominated art world by elevating "
        "domestic subjects to the level of serious artistic consideration."
    ),
    (
        "Salvador Dali developed his paranoiac critical method to access subconscious imagery, creating dreamlike "
        "paintings filled with melting clocks and distorted figures."
    ),
    (
        "The Fauvist painters, led by Henri Matisse, shocked the art world with their wild, non naturalistic colors "
        "that prioritized emotional expression over realistic representation."
    ),
    (
        "Goya's Black Paintings, created directly on the walls of his home during his final years, reveal a dark "
        "vision of humanity that anticipated Expressionism."
    ),
    (
        "The Art Nouveau movement drew inspiration from natural forms like flowers and vines, incorporating organic "
        "curves into architecture, furniture, and decorative arts."
    ),
    (
        "Whistler's Arrangement in Grey and Black, commonly known as Whistler's Mother, was controversial for treating "
        "a portrait as primarily an exercise in formal composition."
    ),
    (
        "The Ashcan School painters rejected idealized academic subjects in favor of gritty urban scenes depicting the "
        "everyday lives of working class Americans."
    ),
    (
        "Kandinsky is credited with creating the first purely abstract paintings, believing that colors and shapes "
        "could communicate spiritual truths without representing physical objects."
    ),
    (
        "The sfumato technique involves building up many thin layers of translucent paint to create soft, hazy "
        "transitions between colors without visible brushstrokes or lines."
    ),
    (
        "Botticelli's Birth of Venus represents the Renaissance revival of classical mythology and the celebration of "
        "beauty inspired by ancient Greek and Roman ideals."
    ),
    (
        "The Nabis group, including Pierre Bonnard and Edouard Vuillard, created intimate domestic scenes using flat "
        "patterns and decorative colors influenced by Japanese prints."
    ),
    (
        "Edward Hopper's paintings of isolated figures in urban settings capture the loneliness and alienation of "
        "modern American life with cinematic lighting and composition."
    ),
    (
        "The Mexican Muralist movement, led by Diego Rivera, Jose Clemente Orozco, and David Alfaro Siqueiros, used "
        "public art to communicate social and political messages."
    ),
    (
        "Albrecht Durer's detailed engravings and woodcuts elevated printmaking to a fine art and spread Renaissance "
        "ideas throughout Northern Europe."
    ),
    (
        "The Rococo style emerged in France as a lighter, more playful reaction to the heavy grandeur of Baroque, "
        "featuring pastel colors and romantic subjects."
    ),
    (
        "Turner's atmospheric landscapes, with their dissolving forms and luminous skies, anticipated Impressionism "
        "and influenced generations of painters interested in light and weather."
    ),
    (
        "The Vienna Secession, led by Gustav Klimt, rebelled against academic conservatism and embraced decorative "
        "arts, symbolism, and the integration of art into daily life."
    ),
    (
        "Winslow Homer's seascapes capture the power and danger of the ocean with a directness and honesty that made "
        "him one of America's greatest painters."
    ),
    (
        "The Bauhaus school sought to unite fine arts with crafts and design, believing that good design could improve "
        "society and be accessible to everyone."
    ),
    (
        "Modigliani's elongated figures and almond shaped eyes drew inspiration from African masks and Italian "
        "Renaissance painting, creating a distinctive and instantly recognizable style."
    ),
    (
        "The action painters of Abstract Expressionism, including Willem de Kooning and Franz Kline, emphasized the "
        "physical act of painting as an expression of inner emotion."
    ),
    (
        "Cezanne's experiments with geometric forms and multiple perspectives laid the groundwork for Cubism and "
        "earned him the title of father of modern art."
    ),
    (
        "The Mannerist painters who followed the High Renaissance deliberately distorted proportions and used unusual "
        "colors to create sophisticated and sometimes unsettling effects."
    ),
    (
        "Grant Wood's American Gothic has become one of the most parodied images in art history, though its original "
        "meaning remains debated among scholars."
    ),
    (
        "The Luminists, a branch of the Hudson River School, focused on atmospheric effects and the transcendent "
        "quality of light in American landscape painting."
    ),
    (
        "Artemisia Gentileschi overcame tremendous obstacles as a woman artist in the seventeenth century to become "
        "one of the most accomplished painters of her generation."
    ),
    (
        "The color field painters like Mark Rothko and Barnett Newman created large canvases of flat color intended to "
        "evoke emotional and spiritual responses in viewers."
    ),
    (
        "Constable's naturalistic approach to landscape painting, with its attention to changing weather and light, "
        "influenced the French Impressionists decades before their movement began."
    ),
    # LONG QUESTIONS
    (
        "Why do you think the Mona Lisa has become the most famous painting in the world when there are arguably more "
        "technically impressive works in the Louvre?"
    ),
    (
        "How did the social and political upheavals of the early twentieth century influence the development of "
        "abstract art and the rejection of traditional representation?"
    ),
    (
        "What techniques can contemporary artists use to achieve the luminous quality of Old Master paintings without "
        "spending years building up traditional glazes?"
    ),
    (
        "Why do some artists become famous during their lifetimes while others, like Van Gogh, only achieve "
        "recognition after their deaths?"
    ),
    (
        "How has the rise of digital art and artificial intelligence changed our understanding of what constitutes "
        "authentic artistic creation and expression?"
    ),
    (
        "What role did the art market and wealthy collectors play in determining which movements and artists became "
        "part of the accepted art historical canon?"
    ),
    (
        "Why do certain color combinations evoke specific emotional responses, and how can artists use color "
        "psychology to enhance the impact of their work?"
    ),
    (
        "How did the invention of photography force painters to reconsider the purpose of art and explore new "
        "directions beyond realistic representation?"
    ),
    (
        "What makes the brushwork of masters like Sargent and Velazquez appear so effortless when it actually requires "
        "tremendous skill and practice?"
    ),
    (
        "Why do museums continue to display works by artists whose personal lives involved problematic behavior, and "
        "should art be separated from the artist?"
    ),
    (
        "How can beginning painters develop the patience required for techniques like glazing that require waiting "
        "days between layers for proper drying?"
    ),
    (
        "What distinguishes the controlled spontaneity of Abstract Expressionism from random mark making, and how do "
        "artists achieve this balance?"
    ),
    (
        "Why did the Impressionists face such harsh criticism initially when their techniques now seem so beautiful "
        "and accessible to modern viewers?"
    ),
    (
        "How do art conservators decide when a damaged painting needs restoration versus when intervention would "
        "compromise the artist's original intentions?"
    ),
    (
        "What can contemporary artists learn from studying the techniques and materials used by Renaissance masters in "
        "their own creative practice?"
    ),
    (
        "Why do some abstract paintings sell for millions of dollars when they appear to be something anyone could "
        "create with minimal training?"
    ),
    (
        "How did Japanese aesthetics and woodblock prints influence Western art, and why were European artists so "
        "captivated by these foreign traditions?"
    ),
    (
        "What role does art education play in developing visual literacy and appreciation for both historical "
        "masterpieces and contemporary experimental work?"
    ),
    (
        "Why do certain paintings become cultural icons that transcend the art world and enter popular consciousness "
        "as universal symbols?"
    ),
    (
        "How can artists balance the need to develop technical skills with the equally important goal of finding their "
        "own authentic creative voice?"
    ),
]

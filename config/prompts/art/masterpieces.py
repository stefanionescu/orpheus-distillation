"""Art prompts about famous works and artists, then mixed examples."""

from __future__ import annotations

MASTERPIECES: list[str] = [
    # ADDITIONAL LONG EXAMPLES - FAMOUS WORKS & ARTISTS
    (
        "Botticelli's Primavera is filled with classical mythology and complex symbolism that scholars have debated "
        "for centuries without reaching consensus on its meaning."
    ),
    (
        "Raphael's School of Athens brings together the greatest philosophers of antiquity in an idealized "
        "architectural setting that demonstrates perfect Renaissance perspective."
    ),
    (
        "El Greco's elongated figures and unusual colors were considered bizarre in his time but later inspired "
        "Expressionists and other modern artists."
    ),
    (
        "Velazquez's Las Meninas is considered one of the most analyzed paintings in Western art history due to its "
        "complex composition and ambiguous meaning."
    ),
    (
        "Hokusai's Great Wave off Kanagawa became one of the most recognizable images in the world and profoundly "
        "influenced European artists."
    ),
    (
        "Manet's Olympia scandalized Paris by depicting a nude courtesan who stares directly at the viewer with an "
        "unapologetic, confrontational gaze."
    ),
    (
        "Degas captured the world of ballet dancers with a combination of precise draftsmanship and innovative "
        "compositions influenced by photography and Japanese prints."
    ),
    (
        "Renoir's paintings of leisure activities and beautiful women embody the joie de vivre that made Impressionism "
        "so popular with collectors."
    ),
    (
        "Toulouse Lautrec's posters of Parisian nightlife elevated commercial art and captured the decadent atmosphere "
        "of Montmartre's cabarets and dance halls."
    ),
    (
        "Caillebotte's Paris Street, Rainy Day demonstrates the Impressionist interest in modern urban life with its "
        "innovative composition and atmospheric effects."
    ),
    (
        "Seurat's Sunday Afternoon on the Island of La Grande Jatte took two years to complete and contains millions "
        "of carefully placed dots of color."
    ),
    (
        "Gauguin abandoned European civilization to paint in Tahiti, creating works that combined Post Impressionist "
        "color with Polynesian subjects and symbolism."
    ),
    (
        "Matisse's The Dance captures pure joy and movement through simplified forms and bold colors that influenced "
        "generations of artists."
    ),
    (
        "Mondrian's grid paintings with primary colors and black lines represent his search for universal harmony and "
        "spiritual truth through pure abstraction."
    ),
    (
        "Magritte's surrealist paintings challenge perception and reality with impossible juxtapositions and thought "
        "provoking visual paradoxes."
    ),
    (
        "Bacon's distorted figures trapped in geometric spaces express the anxiety and isolation of the human "
        "condition in the twentieth century."
    ),
    (
        "Hockney's swimming pool paintings capture the light and lifestyle of Los Angeles with a distinctive style "
        "that bridges Pop Art and traditional painting."
    ),
    (
        "Basquiat's neo expressionist works combine graffiti, text, and imagery to address themes of race, identity, "
        "and social commentary."
    ),
    (
        "Kusama's infinity rooms and polka dot installations create immersive environments that blur the boundaries "
        "between art and viewer."
    ),
    (
        "Koons' monumental sculptures of balloon animals and other kitsch objects challenge distinctions between high "
        "art and popular culture."
    ),
    # ADDITIONAL MIXED EXAMPLES
    (
        "Why do so many artists struggle financially during their lifetimes only to have their work sell for millions "
        "after they're gone?"
    ),
    (
        "The way this artist captures the texture of different fabrics in the same painting shows incredible "
        "observational skill and technical mastery!"
    ),
    (
        "Understanding the historical context in which a painting was created often reveals layers of meaning that "
        "aren't immediately apparent to modern viewers."
    ),
    (
        "I'm fascinated by how different cultures developed distinct artistic traditions that reflect their unique "
        "values, beliefs, and ways of seeing the world."
    ),
    (
        "The restoration of this damaged fresco revealed colors so vibrant that scholars had to reconsider everything "
        "they thought they knew about the artist."
    ),
    (
        "Should art students focus on mastering traditional techniques before experimenting with contemporary "
        "approaches, or is that limiting creative development?"
    ),
    (
        "The patrons who commissioned Renaissance paintings often dictated the subject matter, composition, and even "
        "specific details the artist had to include."
    ),
    (
        "I never realized how much chemistry and material science is involved in understanding why some paintings have "
        "survived centuries while others have deteriorated."
    ),
    (
        "The debate over whether photography is a legitimate art form echoed earlier controversies about printmaking, "
        "watercolor, and other media."
    ),
    (
        "This sketch reveals so much about the artist's thought process and how they worked through compositional "
        "problems before starting the final painting."
    ),
    (
        "Why do some people find abstract art meaningless while others are moved to tears by a canvas covered in a "
        "single color?"
    ),
    (
        "The way this portrait captures not just the subject's appearance but their personality and inner life is what "
        "separates great portraiture from mere likeness."
    ),
    (
        "I'm always amazed at how artists can suggest complex forms and textures with just a few confident strokes of "
        "the brush."
    ),
    (
        "The forgery scandal revealed how much the art market depends on provenance, authentication, and the mystique "
        "surrounding famous artists' names."
    ),
    (
        "Should museums return artworks that were acquired during colonial periods or through questionable means to "
        "their countries of origin?"
    ),
    (
        "The artist's palette, preserved in their studio, reveals the actual colors they mixed and provides insights "
        "into their working methods."
    ),
    (
        "I find it fascinating that some artists work from detailed preliminary drawings while others begin painting "
        "with only a vague idea in mind."
    ),
    (
        "The way natural light changes throughout the day in this gallery completely transforms how these paintings "
        "appear to visitors at different hours."
    ),
    (
        "Why do art critics sometimes praise works that the general public finds ugly, pretentious, or completely "
        "incomprehensible?"
    ),
    (
        "The artist's letters and journals provide intimate glimpses into their struggles, inspirations, and the "
        "personal circumstances that shaped their work."
    ),
    (
        "I'm struck by how this contemporary artist references art history while creating something that feels "
        "completely original and of our time."
    ),
    (
        "The physical presence of a large painting creates an immersive experience that no reproduction, no matter how "
        "accurate, can fully capture."
    ),
    (
        "Should beginning artists copy masterworks to learn technique, or does this approach stifle originality and "
        "personal expression?"
    ),
    (
        "The way this sculptor works with the natural qualities of the material rather than imposing a preconceived "
        "form shows deep respect for the medium."
    ),
    (
        "I wonder how artists working before electric lighting managed to paint such accurate colors when their "
        "studios were lit by candles or oil lamps."
    ),
    (
        "The collaborative nature of Renaissance workshops, where masters and apprentices worked together, challenges "
        "our modern notion of individual artistic genius."
    ),
    (
        "Why do certain subjects like flowers, landscapes, and portraits remain popular across centuries while others "
        "fall in and out of fashion?"
    ),
    (
        "The artist's decision to leave this painting unfinished actually makes it more interesting because we can see "
        "their process and technique."
    ),
    (
        "I'm curious whether future generations will value the digital art being created today or if the lack of "
        "physical presence will diminish its significance."
    ),
    (
        "The way this installation transforms the gallery space itself into part of the artwork challenges traditional "
        "boundaries between art and environment."
    ),
]

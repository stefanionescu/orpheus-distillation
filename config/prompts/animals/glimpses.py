"""Animal prompts of short and medium length about mammals, birds, reptiles, sea life, insects, and exotic animals."""

from __future__ import annotations

GLIMPSES: list[str] = [
    # ULTRA SHORT - MAMMALS
    "Majestic elephant trumpeting.",
    "Mischievous squirrel scampering.",
    "Prowling jaguar stalking.",
    "Playful otter swimming.",
    "Curious raccoon investigating.",
    "Sleepy koala dozing.",
    "Graceful gazelle leaping.",
    "Massive buffalo grazing.",
    "Cunning fox hunting.",
    "Gentle manatee floating.",
    "Ferocious wolverine snarling.",
    "Adorable hedgehog curling.",
    "Lumbering hippo yawning.",
    "Swift cheetah sprinting.",
    "Majestic lion roaring.",
    # ULTRA SHORT - BIRDS
    "Soaring eagle circling.",
    "Colorful macaw squawking.",
    "Elegant flamingo wading.",
    "Wise owl hooting.",
    "Magnificent peacock displaying.",
    "Tiny hummingbird hovering.",
    "Regal swan gliding.",
    "Clever crow cawing.",
    "Exotic toucan perching.",
    "Swift falcon diving.",
    "Proud rooster crowing.",
    "Penguin waddling adorably.",
    "Pelican diving deep.",
    "Majestic condor soaring.",
    "Kingfisher plunging swiftly.",
    # ULTRA SHORT - REPTILES/AMPHIBIANS
    "Coiled cobra hissing.",
    "Ancient tortoise plodding.",
    "Massive crocodile lurking.",
    "Colorful chameleon changing.",
    "Venomous viper striking.",
    "Tiny gecko climbing.",
    "Huge anaconda constricting.",
    "Komodo dragon hunting.",
    "Snapping turtle defending.",
    "Tree frog croaking.",
    "Salamander regenerating limbs.",
    "Iguana basking lazily.",
    "Python swallowing prey.",
    "Axolotl smiling sweetly.",
    "Alligator snapping suddenly.",
    # ULTRA SHORT - MARINE LIFE
    "Graceful dolphin leaping.",
    "Massive whale breaching.",
    "Octopus changing colors.",
    "Shark circling silently.",
    "Jellyfish pulsing gently.",
    "Seahorse dancing elegantly.",
    "Stingray gliding smoothly.",
    "Clownfish hiding safely.",
    "Lobster crawling slowly.",
    "Squid jetting away.",
    "Starfish regenerating arms.",
    "Nautilus floating ancient.",
    "Moray eel lurking.",
    "Barracuda hunting swiftly.",
    "Manta ray soaring.",
    # ULTRA SHORT - INSECTS/INVERTEBRATES
    "Butterfly emerging beautifully.",
    "Busy bee pollinating.",
    "Industrious ant marching.",
    "Firefly glowing softly.",
    "Dragonfly darting swiftly.",
    "Praying mantis waiting.",
    "Cricket chirping loudly.",
    "Scorpion tail raised.",
    "Tarantula crawling slowly.",
    "Ladybug spotted red.",
    "Cicada singing summer.",
    "Beetle scurrying quickly.",
    "Caterpillar munching leaves.",
    "Monarch migrating south.",
    "Spider spinning web.",
    # ULTRA SHORT - EXOTIC ANIMALS
    "Bizarre platypus swimming.",
    "Adorable quokka smiling.",
    "Strange pangolin curling.",
    "Elusive okapi hiding.",
    "Peculiar aye aye tapping.",
    "Tiny tarsier staring.",
    "Red panda climbing.",
    "Shoebill stork glaring.",
    "Slow loris blinking.",
    "Potoo camouflaging perfectly.",
    "Fossa prowling Madagascar.",
    "Binturong smelling popcorn.",
    "Tapir snuffling softly.",
    "Capybara lounging calmly.",
    "Numbat hunting termites.",
    # SHORT - MAMMAL BEHAVIORS
    "The majestic elephant sprayed water over its dusty back.",
    "A mischievous squirrel stole nuts from the birdfeeder.",
    "The prowling jaguar crept silently through the rainforest.",
    "Playful otters held hands while floating downstream together.",
    "The curious raccoon opened the trash can lid.",
    "A sleepy koala clung to the eucalyptus branch.",
    "The graceful gazelle bounded across the African savanna.",
    "Massive buffalo herds thundered across the open plains.",
    "The cunning fox outsmarted the pursuing hounds easily.",
    "A gentle manatee grazed on seagrass in the shallows.",
    "The ferocious wolverine defended its territory fiercely.",
    "An adorable hedgehog curled into a spiny ball.",
    "The lumbering hippo emerged from the muddy river.",
    "A swift cheetah reached incredible speeds chasing prey.",
    "The pride of lions rested beneath the acacia tree.",
    # SHORT - BIRD BEHAVIORS
    "The soaring eagle spotted its prey from above.",
    "A colorful macaw mimicked human speech perfectly.",
    "Elegant flamingos stood on one leg in the lagoon.",
    "The wise old owl hunted silently at night.",
    "A magnificent peacock fanned its iridescent tail feathers.",
    "Tiny hummingbirds beat their wings impossibly fast.",
    "The regal swan glided across the still pond.",
    "Clever crows used tools to retrieve hidden food.",
    "An exotic toucan tossed berries into its beak.",
    "The swift peregrine falcon reached terminal velocity diving.",
    "A proud rooster announced the breaking dawn loudly.",
    "Emperor penguins huddled together against Antarctic winds.",
    "The pelican's pouch expanded to catch swimming fish.",
    "Majestic Andean condors rode thermal currents effortlessly.",
    "A brilliant kingfisher emerged with its silver catch.",
    # SHORT - EXOTIC ANIMAL FACTS
    "The bizarre platypus is a venomous egg laying mammal.",
    "Adorable quokkas appear to smile in every photograph.",
    "Pangolins are the world's most trafficked wild mammals.",
    "The elusive okapi was unknown to science until 1901.",
    "Aye ayes tap trees to find grubs using echolocation.",
    "Tiny tarsiers have the largest eyes relative to body.",
    "Red pandas are more closely related to raccoons.",
    "The shoebill stork can stand motionless for hours.",
    "Slow lorises are the only venomous primates known.",
    "Potoos are masters of camouflage against tree bark.",
    "The fossa is Madagascar's largest carnivorous mammal.",
    "Binturongs smell exactly like buttered popcorn naturally.",
    "Tapirs are living fossils unchanged for millions of years.",
    "Capybaras are the world's largest living rodent species.",
    "Numbats eat up to twenty thousand termites daily.",
    # SHORT - MARINE LIFE FACTS
    "Dolphins sleep with one eye open for safety.",
    "Blue whales are the largest animals ever to exist.",
    "Octopuses have three hearts and blue colored blood.",
    "Great white sharks can detect one drop of blood.",
    "Box jellyfish are among the most venomous creatures.",
    "Male seahorses carry and birth their young offspring.",
    "Manta rays have the largest brains of any fish.",
    "Clownfish are immune to sea anemone stinging cells.",
    "Lobsters can live over one hundred years old.",
    "Giant squid have eyes the size of dinner plates.",
    "Starfish can regenerate entire bodies from one arm.",
    "Nautiluses have survived unchanged for 500 million years.",
    "Moray eels have a second set of hidden jaws.",
    "Barracudas can swim up to thirty six miles per hour.",
    "Whale sharks are filter feeders despite their size.",
    # MEDIUM - MAMMAL DESCRIPTIONS
    "The majestic African elephant led her herd to the watering hole, while calves played in the mud nearby.",
    "A mischievous red squirrel buried acorns in the garden, forgetting most of them to sprout into oak trees.",
    "The powerful Siberian tiger prowled through the snowy forest, its orange coat stark against the white landscape.",
    (
        "Clever meerkats took turns standing guard while others foraged, their sentinel system protecting against "
        "aerial predators efficiently."
    ),
    (
        "The massive grizzly bear caught salmon leaping upstream, demonstrating incredible patience and lightning fast "
        "reflexes during the run."
    ),
    "A playful pod of bottlenose dolphins surfed the wake, leaping and spinning in apparent joy and camaraderie.",
    (
        "The elusive snow leopard traversed the Himalayan peaks, perfectly camouflaged against the rocky gray mountain "
        "terrain."
    ),
    "Howler monkeys announced their territory with calls audible three miles away through the dense rainforest canopy.",
    "A mother orangutan taught her infant to use tools, passing down knowledge accumulated over generations carefully.",
    (
        "The African wild dog pack hunted with remarkable coordination, their success rate exceeding even lions "
        "significantly."
    ),
    "Playful river otters slid down muddy banks repeatedly, seeming to engage in recreation purely for enjoyment.",
    "A massive bull moose emerged from the misty lake, water streaming from its impressive palmate antlers.",
    (
        "The nocturnal aardvark used its powerful claws to demolish termite mounds, consuming thousands with its "
        "sticky tongue."
    ),
    "Arctic foxes changed coat color seasonally, white in winter and brown in summer for optimal camouflage.",
    "A colony of flying foxes erupted from their roost at dusk, darkening the twilight sky momentarily.",
    # MEDIUM - BIRD DESCRIPTIONS
    "The bald eagle soared majestically above the river canyon, scanning for fish with its incredibly keen eyesight.",
    "A flock of scarlet macaws painted the green canopy red, their raucous calls echoing through the rainforest.",
    (
        "The elaborate courtship dance of the bird of paradise mesmerized potential mates with impossible colors and "
        "movements."
    ),
    "Clever New Caledonian crows crafted hooked tools from twigs to extract grubs from tree bark efficiently.",
    "A parliament of snowy owls gathered in the Arctic tundra, their white plumage blending with the snow.",
    "The resplendent quetzal's iridescent green tail feathers can reach three feet in impressive length.",
    "Secretary birds stomped venomous snakes to death with their powerful legs on the African savanna grasslands.",
    "A charm of hummingbirds competed fiercely for nectar at the feeder, their wings a blur constantly.",
    (
        "The lyrebird perfectly mimicked chainsaws and camera shutters, incorporating human sounds into its elaborate "
        "song."
    ),
    (
        "Wandering albatrosses circumnavigated the globe without ever touching land, sleeping while gliding on ocean "
        "winds effortlessly."
    ),
    "A kettle of vultures circled overhead, their keen sense of smell detecting carrion from miles away.",
    "The Atlantic puffin emerged from its burrow with a beak full of small silvery fish.",
    "Cassowaries are among the most dangerous birds, capable of inflicting lethal wounds with their dagger like claws.",
    "A murmuration of starlings created breathtaking aerial patterns against the sunset sky in synchronized flight.",
    "The kakapo, a flightless parrot, is the world's heaviest and rarest parrot species, critically endangered.",
    # MEDIUM - QUESTIONS
    "Did you know that elephants can recognize themselves in mirrors, showing remarkable self awareness among mammals?",
    "Have you ever seen a pangolin roll into a perfect ball when threatened by potential predators?",
    "Can octopuses really squeeze through any opening larger than their beak, which is their only hard part?",
    "Why do flamingos stand on one leg, and does it actually help them conserve body heat?",
    "Is it true that crows can recognize individual human faces and hold grudges for years afterward?",
    (
        "Do hummingbirds really enter torpor every night to survive, lowering their metabolism dramatically until "
        "morning comes?"
    ),
    "Have you heard that mantis shrimp can see colors invisible to humans, including ultraviolet light?",
    "Why do wolves howl at the moon, or is that just a popular myth we believe?",
    "Can chameleons really change color to match any background, or is camouflage not their main purpose?",
    "Did you know that sea otters hold hands while sleeping to prevent drifting apart on currents?",
    # MEDIUM - EXCLAMATIONS
    "The massive humpback whale breached completely out of the water, crashing back down with an enormous splash!",
    "I can't believe that tiny poison dart frog contains enough toxin to kill ten grown men!",
    "That magnificent Bengal tiger is absolutely stunning with its orange coat and distinctive black stripes pattern!",
    "The peacock spider's elaborate courtship dance is one of nature's most incredible and entertaining displays ever!",
    "A blue whale's heart is so large that a small child could crawl through its arteries!",
    "The bombardier beetle can spray boiling hot chemicals at predators, what an amazing defense mechanism!",
    "I've never seen anything as adorable as a baby pygmy slow loris with those huge eyes!",
    "The Goliath birdeater tarantula is the largest spider in the world, with a leg span over eleven inches!",
    (
        "That mimic octopus just transformed itself to look exactly like a venomous lionfish, absolutely incredible "
        "camouflage!"
    ),
    "The pistol shrimp creates a cavitation bubble so hot it momentarily reaches the temperature of the sun!",
]

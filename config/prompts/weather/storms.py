"""Weather prompts: long rain, snow, storms, questions, and exclamations, then medium and short variety."""

from __future__ import annotations

STORMS: list[str] = [
    # LONG - RAIN/PRECIPITATION
    (
        "The torrential downpour overwhelmed storm drains within minutes, sending rivers of water cascading down "
        "streets and flooding underpasses where stranded motorists awaited rescue desperately."
    ),
    (
        "A gentle drizzle began at dawn and persisted throughout the day, the steady patter on the roof creating a "
        "cozy atmosphere perfect for staying indoors."
    ),
    (
        "Monsoon rains arrived with dramatic intensity, the sky darkening to near black before releasing walls of "
        "water that reduced visibility to nearly zero instantly."
    ),
    (
        "The sudden cloudburst caught thousands of concertgoers without shelter, drenching the crowd in seconds and "
        "turning the festival grounds into a muddy mess completely."
    ),
    (
        "Steady rainfall saturated the ground until no more water could be absorbed, creating dangerous conditions as "
        "hillsides became unstable and prone to mudslides everywhere."
    ),
    (
        "The deluge continued for forty straight hours, breaking rainfall records and causing rivers to crest well "
        "above flood stage throughout the entire watershed area."
    ),
    (
        "Light showers intermittently swept through the area, just enough to keep umbrellas out but never quite "
        "committing to a proper rainstorm throughout the day."
    ),
    (
        "Freezing rain coated every surface in a thick layer of ice, bringing down power lines and tree branches under "
        "the accumulated weight overnight."
    ),
    (
        "The petrichor after the storm was intoxicating, that distinctive earthy smell of rain on dry soil filling the "
        "air and making everyone feel refreshed."
    ),
    (
        "April showers proved relentless this year, with measurable rainfall every single day of the month setting a "
        "new record for the wettest April ever."
    ),
    # LONG - SNOW/WINTER
    (
        "The blizzard dropped three feet of snow in twenty four hours, with drifts piling up to roof level against "
        "buildings on the windward side of streets."
    ),
    (
        "Heavy snowfall transformed the familiar landscape into an alien world of white, muffling all sounds and "
        "creating an eerie silence throughout the buried neighborhood."
    ),
    (
        "Light flurries danced in the glow of streetlamps, each snowflake visible in the cone of light before settling "
        "gently on the accumulating blanket below."
    ),
    (
        "The nor'easter battered the coast for three days straight, combining heavy snow with coastal flooding and "
        "hurricane force winds in a devastating winter fury."
    ),
    (
        "Powder snow delighted skiers who had waited all season for conditions this perfect, the fresh accumulation "
        "providing the best skiing in years at the resort."
    ),
    (
        "The ice storm left a crystalline wonderland in its wake, every branch and twig encased in a glistening sheath "
        "of ice that sparkled beautifully."
    ),
    (
        "Whiteout conditions during the blizzard reduced visibility to zero, with highway patrols closing major "
        "interstates and urging everyone to shelter in place immediately."
    ),
    (
        "Sleet mixed with freezing rain created hazardous conditions on every surface, the icy mixture accumulating "
        "faster than road crews could treat the pavement effectively."
    ),
    (
        "The first snowfall of the season brought childlike joy to everyone, with kids rushing outside to build "
        "snowmen before the pristine white could be disturbed."
    ),
    (
        "Lake effect snow bands parked over the city for hours, dumping several inches per hour in a localized deluge "
        "that overwhelmed plow crews completely."
    ),
    # LONG - STORMS
    (
        "Thunder rumbled continuously for hours as the massive storm system moved through, the constant bass growl "
        "punctuated by sharp cracks of nearby lightning strikes."
    ),
    (
        "Lightning illuminated the entire sky in brilliant flashes, revealing the churning clouds of the supercell as "
        "it approached with tornado sirens already wailing in the distance."
    ),
    (
        "The hurricane made landfall with sustained winds of one hundred forty miles per hour, storm surge pushing the "
        "ocean fifteen feet above normal levels inland."
    ),
    (
        "Tornado sirens pierced the evening calm as the massive wedge touched down, the roar of the twister audible "
        "above the warning sounds alerting everyone."
    ),
    (
        "The derecho's hundred mile per hour straight line winds flattened forests and destroyed buildings across a "
        "four hundred mile swath from Iowa to Ohio in mere hours."
    ),
    (
        "Severe thunderstorm warnings scrolled continuously across the television screen, with meteorologists tracking "
        "multiple rotating supercells as they threatened populated areas throughout the region tonight."
    ),
    (
        "The electrical storm put on a spectacular display, with cloud to cloud lightning creating an almost "
        "continuous strobe effect across the entire darkened sky dramatically."
    ),
    (
        "Microbursts from the storm's downdraft created localized wind damage that resembled tornado paths, with "
        "debris scattered in patterns that confused damage surveyors initially."
    ),
    (
        "The squall line raced across the county at sixty miles per hour, bringing intense but brief winds and rain "
        "before moving on just as quickly."
    ),
    (
        "Flash flood warnings were issued as six inches of rain fell in just two hours, overwhelming every drainage "
        "system and sending water into streets and homes."
    ),
    # LONG - QUESTIONS
    (
        "Did you see the forecast calling for a major winter storm this weekend, with possible blizzard conditions and "
        "up to two feet of snow expected?"
    ),
    (
        "Is it true that the heatwave is supposed to break tomorrow, or are we in for another week of these unbearable "
        "triple digit temperatures?"
    ),
    (
        "Can you believe the tornado passed just two miles from our house? We could hear the roar like a freight train "
        "from the basement shelter!"
    ),
    (
        "Why does it always seem to rain on weekends when we have outdoor plans, but stay beautiful during the week "
        "when we're stuck inside working?"
    ),
    (
        "Have you ever experienced a haboob before? The wall of dust approaching the city looked like something from "
        "an apocalyptic movie scene this afternoon!"
    ),
    (
        "Is the hurricane expected to strengthen before making landfall, or are the cooler waters along the coast "
        "going to weaken it significantly beforehand?"
    ),
    (
        "Did the frost last night damage your garden? Mine looks terrible, with all the tender plants completely "
        "blackened by the unexpected late freeze."
    ),
    (
        "Can lightning really strike the same place twice, or is that just an old myth people repeat without "
        "understanding how electrical storms actually work?"
    ),
    (
        "Why do meteorologists always seem to overpredict snowfall? They promised eight inches and we barely got a "
        "dusting on the ground here."
    ),
    (
        "Have you noticed how the weather has become more extreme lately, with record breaking heat followed by "
        "unseasonable cold in rapid succession throughout the year?"
    ),
    # LONG - EXCLAMATIONS
    (
        "It's absolutely sweltering outside, I can't believe anyone is voluntarily exercising in this heat! The "
        "temperature feels like it's melting everything in sight today!"
    ),
    (
        "That was the most terrifying thunderstorm I've ever experienced! The lightning struck so close I could smell "
        "the ozone and feel the electricity in the air!"
    ),
    (
        "I can't believe how much snow fell overnight! We went to bed with bare ground and woke up to three feet of "
        "powder everywhere!"
    ),
    (
        "The wind is absolutely howling out there! I watched a trampoline cartwheel down the street and crash into "
        "someone's parked car just now!"
    ),
    (
        "What a stunning sunset! I've never seen the sky turn that exact shade of magenta before, the colors were "
        "absolutely otherworldly and breathtaking!"
    ),
    (
        "This fog is so thick I can barely see my hand in front of my face! Driving right now would be completely "
        "impossible!"
    ),
    (
        "The hail was terrifying! Stones the size of softballs were smashing through skylights and destroying "
        "everything in the open, absolute chaos everywhere!"
    ),
    (
        "Finally, the drought has broken! Look at that rain coming down, the first significant rainfall we've had in "
        "over four months of dryness!"
    ),
    (
        "That double rainbow is the most beautiful thing I've ever seen! Both arcs are complete and the colors are so "
        "vivid against the dark clouds!"
    ),
    (
        "The aurora last night was absolutely spectacular! Green curtains danced across the entire sky, brighter than "
        "I've ever seen them this far south!"
    ),
    # ADDITIONAL MEDIUM - VARIETY
    (
        "The barometric pressure dropped rapidly as the storm approached, triggering headaches and joint pain in "
        "weather sensitive individuals everywhere."
    ),
    (
        "Atmospheric instability created ideal conditions for severe thunderstorm development throughout the afternoon "
        "and evening hours today."
    ),
    (
        "The marine layer pushed inland overnight, bringing welcome relief from the heatwave to coastal communities "
        "finally."
    ),
    "Wind chill values plummeted to dangerous levels, with exposed skin at risk of frostbite within minutes.",
    (
        "The temperature inversion trapped pollutants near the surface, creating hazardous air quality throughout the "
        "valley region."
    ),
    (
        "Cumulus clouds built rapidly in the afternoon heat, their towering white columns promising afternoon "
        "thunderstorm activity."
    ),
    "The jet stream's unusual dip brought arctic air much farther south than typical for this season.",
    (
        "Relative humidity near one hundred percent made the moderate temperatures feel absolutely unbearable for "
        "everyone outside."
    ),
    (
        "The microburst struck without warning, its localized downburst flattening structures in a narrow path of "
        "destruction."
    ),
    (
        "Clear skies and calm winds created perfect conditions for radiational cooling, dropping temperatures rapidly "
        "after sunset."
    ),
    "The monsoon moisture surge brought daily afternoon thunderstorms to the normally arid desert landscape finally.",
    "Visibility dropped to near zero as dense advection fog rolled in from the cooling ocean waters.",
    "The heat dome settled over the region for the second consecutive week, breaking high temperature records daily.",
    (
        "Scattered thunderstorms popped up randomly across the region, with some areas receiving heavy rain while "
        "others stayed dry."
    ),
    "The cold front's passage was dramatic, dropping temperatures thirty degrees in less than an hour dramatically.",
    # ADDITIONAL SHORT - MORE VARIETY
    "Unseasonably warm today.",
    "Record cold overnight.",
    "Humidity crushing me.",
    "Perfect weather finally.",
    "Storm rolling in.",
    "Rainbow after the rain.",
    "Drought continuing sadly.",
    "Flash flood warning.",
    "Wind advisory issued.",
    "Heat dome persisting.",
    "Cold front approaching.",
    "Warm front stalling.",
    "Dew point soaring.",
    "Pressure dropping fast.",
    "Visibility near zero.",
    "Sunrise spectacular today.",
    "Cloudy with a chance.",
    "Partly sunny expected.",
    "Mostly cloudy skies.",
    "Temperature fluctuating wildly.",
]

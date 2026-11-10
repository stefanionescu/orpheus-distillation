"""Weather prompts of short and medium length, then long prompts about hot and cold weather."""

from __future__ import annotations

FORECAST: list[str] = [
    # ULTRA SHORT - HOT WEATHER
    "Absolutely sweltering today.",
    "Scorching heat unbearable.",
    "Blistering sun overhead.",
    "Sizzling pavement burning.",
    "Blazing hot afternoon.",
    "Stifling humidity everywhere.",
    "Sultry summer evening.",
    "Muggy and oppressive.",
    "Torrid heatwave continuing.",
    "Boiling temperatures recorded.",
    # ULTRA SHORT - COLD WEATHER
    "Freezing temperatures outside.",
    "Frigid arctic blast.",
    "Bitter cold morning.",
    "Biting wind piercing.",
    "Icy roads dangerous.",
    "Frosty windows beautiful.",
    "Chilly autumn breeze.",
    "Nippy out there.",
    "Brisk morning walk.",
    "Bone chilling cold snap.",
    # ULTRA SHORT - RAIN
    "Light drizzle falling.",
    "Sudden downpour starting.",
    "Torrential rain pouring.",
    "Gentle showers expected.",
    "Monsoon season arriving.",
    "Misty morning dew.",
    "Steady rainfall continuing.",
    "Scattered sprinkles likely.",
    "Relentless deluge flooding.",
    "Refreshing rain smell.",
    # ULTRA SHORT - SNOW/ICE
    "Heavy snowfall overnight.",
    "Blizzard warnings issued.",
    "Light flurries dusting.",
    "Sleet mixing in.",
    "Hail pounding rooftops.",
    "Frost covering everything.",
    "Powder snow perfect.",
    "Whiteout conditions dangerous.",
    "Ice storm approaching.",
    "Snowflakes gently falling.",
    # ULTRA SHORT - WIND
    "Gusty winds howling.",
    "Gentle breeze refreshing.",
    "Gale force warnings.",
    "Hurricane approaching fast.",
    "Tornado sirens blaring.",
    "Calm before storm.",
    "Blustery day ahead.",
    "Zephyr barely noticeable.",
    "Squall line forming.",
    "Whirlwind of leaves.",
    # ULTRA SHORT - SKY/CLOUDS
    "Crystal clear skies.",
    "Overcast and gloomy.",
    "Partly cloudy afternoon.",
    "Dense fog rolling.",
    "Hazy summer morning.",
    "Murky visibility today.",
    "Bright sunshine finally.",
    "Ominous clouds gathering.",
    "Radiant blue above.",
    "Gray skies depressing.",
    # SHORT - TEMPERATURE DESCRIPTIONS
    "It's absolutely sweltering today, must be over a hundred.",
    "The scorching heat made walking outside nearly impossible.",
    "Blistering temperatures broke records across the region.",
    "This stifling humidity makes it hard to breathe.",
    "The sultry evening air hung thick and heavy.",
    "Freezing temperatures plunged below zero overnight suddenly.",
    "The frigid arctic blast caught everyone off guard.",
    "Bitter cold kept the streets deserted all day.",
    "That biting wind cuts right through your coat.",
    "Bone chilling temperatures closed schools across the county.",
    "Finally, a pleasant and temperate spring day arrived.",
    "The balmy evening was perfect for outdoor dining.",
    "Comfortable temperatures made the hike enjoyable throughout.",
    "Moderate weather persisted for the entire week pleasantly.",
    "The oppressive heat index reached dangerous levels today.",
    # SHORT - PRECIPITATION DESCRIPTIONS
    "A light drizzle began as we left the restaurant.",
    "The sudden downpour caught everyone without umbrellas.",
    "Torrential rain flooded the streets within minutes.",
    "Gentle showers refreshed the parched garden overnight.",
    "The monsoon brought much needed relief to drought areas.",
    "Morning mist blanketed the valley in ethereal beauty.",
    "Steady rainfall persisted throughout the gloomy afternoon.",
    "Scattered sprinkles dotted the windshield sporadically.",
    "The relentless deluge caused widespread flooding damage.",
    "Petrichor filled the air after the summer storm.",
    "Heavy snowfall blanketed the city in pristine white.",
    "The blizzard dumped three feet of snow overnight.",
    "Light flurries danced in the streetlight's glow beautifully.",
    "Sleet made the morning commute treacherous today.",
    "Hail the size of golf balls damaged vehicles.",
    # SHORT - WIND DESCRIPTIONS
    "Gusty winds knocked over garbage cans everywhere.",
    "A gentle breeze carried the scent of flowers.",
    "Gale force winds toppled trees across the neighborhood.",
    "The hurricane approached with terrifying speed and power.",
    "Tornado warnings sent everyone rushing to shelter.",
    "The calm before the storm felt eerily unsettling.",
    "Blustery conditions made the outdoor event challenging.",
    "A warm zephyr rustled through the summer grass.",
    "The squall line brought intense but brief storms.",
    "A whirlwind of autumn leaves swirled beautifully.",
    "Strong winds delayed flights at the airport substantially.",
    "The nor'easter battered the coastline for three days.",
    "Chinook winds brought sudden warmth to the mountains.",
    "Trade winds made sailing conditions absolutely perfect.",
    "The jet stream dipped south bringing arctic air.",
    # SHORT - STORM DESCRIPTIONS
    "Thunder rumbled ominously in the distance tonight.",
    "Lightning illuminated the entire sky dramatically.",
    "The thunderstorm knocked out power for hours.",
    "Electrical storms lit up the night sky spectacularly.",
    "The tempest raged throughout the turbulent night.",
    "Severe weather warnings scrolled across the screen.",
    "The cyclone devastated coastal communities tragically.",
    "Typhoon force winds exceeded one hundred fifty miles per hour.",
    "Flash flood warnings were issued for the county.",
    "The supercell spawned multiple dangerous tornadoes.",
    "Shelf clouds signaled the approaching severe weather.",
    "Mammatus clouds bubbled ominously before the storm.",
    "The derecho caused widespread destruction across the state.",
    "Microbursts flattened crops in isolated areas today.",
    "A waterspout formed just offshore this afternoon.",
    # SHORT - ATMOSPHERIC PHENOMENA
    "A stunning rainbow arched across the clearing sky.",
    "The aurora borealis danced in green ribbons.",
    "A magnificent sunrise painted the clouds orange.",
    "The sunset blazed in shades of crimson.",
    "Morning dew sparkled like diamonds on the grass.",
    "Dense fog reduced visibility to near zero.",
    "The heat shimmer made the road appear wet.",
    "Sun dogs appeared on either side of the sun.",
    "A lunar halo circled the full moon tonight.",
    "The temperature inversion trapped smog in the valley.",
    "Virga fell from clouds but evaporated before landing.",
    "A glory rainbow circled the airplane's shadow.",
    "Ice crystals created a spectacular light pillar.",
    "The green flash appeared at sunset over the ocean.",
    "Crepuscular rays streamed through breaks in the clouds.",
    # MEDIUM - SEASONAL WEATHER
    (
        "The spring showers have been relentless this year, with April rainfall totals already exceeding normal "
        "averages significantly."
    ),
    "Summer heat arrived early with temperatures climbing into the triple digits before Memorial Day even passed.",
    (
        "Autumn brought a welcome chill after the sweltering summer, crisp mornings finally making the outdoors "
        "enjoyable again."
    ),
    (
        "Winter's first snowfall transformed the landscape into a pristine wonderland, delighting children and "
        "frustrating commuters equally."
    ),
    "The Indian summer extended warm weather well into October, confusing the trees about when to change colors.",
    "Spring arrived late this year, with frost persisting into May and delaying planting season considerably.",
    "The dog days of summer showed no signs of relenting, with the heat dome parked stubbornly overhead.",
    "Fall foliage peaked early due to the drought stress, colors already fading before October arrived.",
    "The polar vortex plunged temperatures to historic lows, breaking records set over a century ago.",
    "An early spring thaw caused flooding as snowpack melted faster than the ground could absorb it.",
    "The marine layer kept coastal temperatures mild while inland areas sweltered in the summer heat.",
    "Unseasonably warm February temperatures had the cherry blossoms blooming weeks ahead of their normal schedule.",
    "The lake effect snow machine buried the eastern shore under feet of continuous heavy snow.",
    "Drought conditions persisted through the sixth consecutive month, with no significant rainfall in the forecast.",
    "The wet El Niño winter filled reservoirs to capacity after years of devastating drought conditions.",
    # MEDIUM - QUESTIONS
    "Did you hear the thunder last night? It sounded like the storm was right on top of us!",
    "Is it supposed to rain all week, or will we get a break sometime before the weekend?",
    "Can you believe how hot it is already? It's only May and feels like mid July out there!",
    "Why does the humidity make ninety degrees feel so much worse than dry desert heat ever does?",
    "Have you checked the forecast for the weekend? I'm hoping we can still have the barbecue.",
    "Did the blizzard drop as much snow as they predicted, or was it another overblown forecast?",
    "Is the fog supposed to burn off by noon, or will it stay gloomy all day long?",
    "Can we trust this beautiful weather to hold, or should I bring an umbrella just in case?",
    "Did you feel that wind gust? It nearly knocked me off my feet walking across the parking lot!",
    "Is it true that tornadoes can't hit downtown areas, or is that just an urban myth?",
    # MEDIUM - EXCLAMATIONS
    "It's absolutely sweltering out there! I'm drenched in sweat just walking from the car to the door!",
    "That lightning strike was terrifyingly close! The thunder was instantaneous and shook the entire house violently!",
    "I can't believe how much snow fell overnight! We're completely snowed in and can't open the door!",
    "The wind nearly blew me over! I had to hold onto a street sign just to stay upright!",
    "What a gorgeous day! The sky is so blue and the temperature is absolutely perfect for anything!",
    "This fog is so thick! I can barely see ten feet in front of my car right now!",
    "The hail destroyed my car! Every panel is dented and the windshield is completely shattered from impact!",
    "Finally, some rain! The garden was dying and the grass was turning brown from the drought!",
    "That rainbow is spectacular! It's a complete double arc stretching from horizon to horizon so beautifully!",
    "The humidity is unbearable! My glasses fog up instantly every time I step outside the air conditioning!",
    # LONG - HOT WEATHER
    (
        "It's absolutely sweltering today, with the temperature already hitting one hundred and five degrees by noon, "
        "and the heat index making it feel even more oppressive."
    ),
    (
        "The scorching summer sun beat down mercilessly on the parched earth, cracking the soil and wilting every "
        "plant that hadn't been watered in the past week."
    ),
    (
        "Blistering heat waves shimmered off the asphalt parking lot, distorting the view of distant buildings and "
        "making the short walk to the car feel like a marathon."
    ),
    (
        "The stifling humidity made breathing difficult, with the air so thick and heavy that even standing still "
        "produced beads of sweat rolling down everyone's faces."
    ),
    (
        "Sultry summer nights offered no relief from the oppressive daytime heat, the temperature barely dropping "
        "below eighty degrees even in the hours before dawn approached."
    ),
    (
        "The torrid heatwave broke temperature records that had stood for over a century, overwhelming power grids as "
        "everyone cranked their air conditioning to maximum settings."
    ),
    (
        "Muggy conditions persisted throughout the week, with dew points in the seventies making the ninety degree "
        "temperatures feel absolutely brutal for anyone spending time outdoors."
    ),
    (
        "The blazing afternoon sun forced everyone indoors, seeking refuge in air conditioned spaces while the "
        "thermometer climbed past one hundred ten in the shade outside."
    ),
    (
        "Oppressive heat warnings were issued for the elderly and vulnerable populations, with cooling centers opened "
        "throughout the city to provide life saving relief from temperatures."
    ),
    (
        "The sweltering conditions melted asphalt on major roadways, with some highways buckling from the extreme "
        "thermal expansion caused by the relentless heatwave overhead."
    ),
    # LONG - COLD WEATHER
    (
        "Freezing temperatures gripped the region for the third consecutive week, with pipes bursting in homes "
        "throughout the neighborhood as the cold penetrated every uninsulated space."
    ),
    (
        "The frigid arctic blast plunged temperatures to thirty below zero, with wind chills making it dangerous to be "
        "outside for more than a few minutes."
    ),
    (
        "Bitter cold settled over the city like a frozen blanket, ice forming on the inside of windows despite heating "
        "systems running at full capacity continuously."
    ),
    (
        "Biting winds drove the feels like temperature well below zero, forcing schools to close and warning residents "
        "to limit any outdoor exposure to absolute necessities."
    ),
    (
        "The bone chilling cold snap caught everyone off guard, with many unprepared for temperatures forty degrees "
        "below normal for this time of year."
    ),
    (
        "Icy conditions made every surface treacherous, with black ice forming on roads and sidewalks that looked "
        "deceptively clear and safe to traverse."
    ),
    (
        "The frosty morning left intricate ice crystal patterns on every window, beautiful to admire from inside but "
        "indicative of the brutal cold beyond the glass."
    ),
    (
        "Sub zero temperatures forced water mains to freeze and burst, leaving entire neighborhoods without running "
        "water until crews could make emergency repairs in harsh conditions."
    ),
    (
        "The glacial cold persisted day after day, with the sun providing no warmth despite shining brightly through "
        "the crystalline air of the frozen landscape."
    ),
    (
        "Nippy autumn breezes hinted at the harsh winter to come, with temperatures dropping noticeably each evening "
        "as the season's transition accelerated rapidly now."
    ),
]

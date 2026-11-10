"""Weather prompts: long variety and the first long examples of weather events."""

from __future__ import annotations

SEASONS: list[str] = [
    # ADDITIONAL LONG - MORE VARIETY
    (
        "The weather whiplash continued with temperatures swinging forty degrees in a single day, from freezing at "
        "dawn to nearly seventy by afternoon before plunging again."
    ),
    (
        "Atmospheric rivers from the Pacific delivered relentless rainfall to the coast, with multiple feet of rain "
        "falling over several days and causing widespread catastrophic flooding."
    ),
    (
        "The unprecedented heat dome shattered temperature records across the region, with dozens of deaths attributed "
        "to the extreme conditions that persisted for over a week."
    ),
    (
        "Drought conditions reached their worst levels in over a millennium according to tree ring data, with "
        "reservoirs dropping to historic lows and water restrictions enacted."
    ),
    (
        "The bomb cyclone intensified rapidly as it approached the coast, its central pressure dropping so fast that "
        "meteorologists struggled to keep up with forecast updates."
    ),
    (
        "Persistent contrails from high altitude aircraft spread across the sky, creating artificial cirrus clouds "
        "that trapped heat and contributed to the unseasonably warm temperatures below."
    ),
    (
        "The supercell's mesocyclone was clearly visible on radar, its tight rotation indicating strong tornado "
        "potential as storm chasers positioned themselves along its projected path."
    ),
    (
        "Graupel bounced off every surface as the cold front passed, the soft ice pellets accumulating like small "
        "styrofoam balls before melting in the warmer air."
    ),
    (
        "The Santa Ana winds howled through the canyons, their hot dry gusts fanning wildfires and creating dangerous "
        "red flag conditions throughout Southern California today."
    ),
    (
        "Morning fog burned off by noon as the sun's warmth increased, revealing clear blue skies that had been hidden "
        "behind the gray marine layer since dawn."
    ),
    (
        "The subtropical moisture plume stretched from Hawaii to the West Coast, the atmospheric river promising days "
        "of heavy rainfall and potential flooding for many areas."
    ),
    (
        "Wind shear prevented the hurricane from strengthening further, tearing apart its organized structure and "
        "reducing it to a disorganized tropical depression before landfall occurred."
    ),
    (
        "The haboob rolled across the desert floor like a massive brown wall, reducing visibility to zero and coating "
        "everything in fine dust for miles around."
    ),
    (
        "Freezing fog deposited rime ice on every exposed surface, transforming the landscape into a crystalline "
        "wonderland with trees coated in white ice feathers completely."
    ),
    (
        "The temperature gradient across the front was extreme, with locations just fifty miles apart experiencing "
        "differences of over forty degrees simultaneously that afternoon."
    ),
    (
        "Convective available potential energy values reached unprecedented levels, indicating extreme instability "
        "that could fuel violent tornadoes if storms could develop ahead of the front."
    ),
    (
        "The sudden stratospheric warming event disrupted the polar vortex, sending arctic air plunging south and "
        "bringing historic cold to regions unaccustomed to such extreme temperatures."
    ),
    (
        "Persistent drought turned vegetation into kindling, with the fire weather watch warning that any spark could "
        "ignite a catastrophic wildfire in the tinderbox conditions."
    ),
    (
        "The sea breeze front pushed inland during the afternoon, bringing cooler temperatures and higher humidity to "
        "areas just miles from the sweltering interior valleys."
    ),
    (
        "Clear skies and light winds created perfect conditions for fog development overnight, with dense fog "
        "advisories issued for the morning commute across the entire region."
    ),
    # MORE LONG EXAMPLES
    (
        "The squall line raced across the plains at seventy miles per hour, its shelf cloud stretching from horizon to "
        "horizon in an ominous dark wall."
    ),
    (
        "Virga streaked below the distant thunderstorm, the rain evaporating before reaching the ground in the dry air "
        "beneath the clouds over the desert landscape."
    ),
    (
        "The temperature dropped twenty degrees in ten minutes as the cold front blasted through, strong winds and "
        "heavy rain accompanying the dramatic transition."
    ),
    (
        "Mammatus clouds bubbled beneath the storm's anvil, their ominous appearance signaling the severe weather that "
        "had just passed through the area moments before."
    ),
    (
        "The foghorn moaned repeatedly in the harbor as visibility dropped to nearly nothing, ships anchoring in place "
        "rather than risking collision in the murk."
    ),
    (
        "Brilliant sundogs flanked the winter sun, the ice crystal halos creating a spectacular display against the "
        "bitter cold blue sky of the arctic morning."
    ),
    (
        "The monsoon arrived with dramatic fanfare, the first storms of the season dropping heavy rain on parched "
        "desert soil and filling dry washes instantly."
    ),
    (
        "Wind driven snow created enormous drifts against buildings, some reaching second story windows while other "
        "areas remained nearly bare from the scouring gusts."
    ),
    (
        "The thermal lifted the hawk effortlessly on the hot afternoon air, the raptor circling higher and higher "
        "without a single flap of its wings."
    ),
    (
        "Cumulonimbus towers punched through forty thousand feet, their anvil tops spreading out against the "
        "tropopause as the severe storms intensified through the afternoon."
    ),
    (
        "The ice storm lasted three days, coating everything in up to two inches of clear ice and bringing down trees "
        "and power lines across the state."
    ),
    (
        "Persistent stratus clouds kept the region gray and gloomy for two solid weeks, the marine influence blocking "
        "any hope of sunshine until the pattern shifted."
    ),
    (
        "The dew point crashed as the dry air arrived, humidity dropping from oppressive to comfortable in less than "
        "an hour as relief finally swept through."
    ),
    (
        "Morning frost painted delicate patterns on every surface, the intricate ice crystals melting quickly once the "
        "sun rose above the trees in the east."
    ),
    (
        "The pressure gradient tightened dramatically, winds increasing from calm to fifty miles per hour in just a "
        "few hours as the system intensified rapidly."
    ),
    (
        "Funnel clouds repeatedly lowered from the rotating supercell, some touching down briefly while others "
        "remained aloft, each one prompting new tornado warnings immediately."
    ),
    (
        "The outflow boundary from the morning storms triggered new development in the afternoon heat, storms popping "
        "up along the invisible line of converging air."
    ),
    (
        "Radiational cooling on the clear night dropped temperatures into the teens, creating a hard freeze that ended "
        "the growing season abruptly and completely."
    ),
    (
        "The gust front preceded the storm by several miles, its sudden wind shift and temperature drop warning of the "
        "approaching severe weather behind it."
    ),
    (
        "Steam rose from the lake as cold air passed over the relatively warm water, creating lake effect clouds that "
        "dumped snow on the downwind shore."
    ),
    (
        "The inversion layer trapped smoke from distant wildfires, turning the sky an apocalyptic orange and reducing "
        "air quality to hazardous levels for sensitive groups."
    ),
    (
        "Beautiful lenticular clouds formed over the mountain peaks, their smooth disc shapes indicating strong upper "
        "level winds flowing over the terrain below them today."
    ),
    (
        "The heat burst struck after midnight, temperatures jumping thirty degrees and winds gusting to eighty miles "
        "per hour in the bizarre nocturnal phenomenon."
    ),
    (
        "Continuous lightning illuminated the horizon for hours, the distant storm complex too far away for thunder "
        "but putting on a spectacular light show nonetheless."
    ),
    (
        "The dewpoint temperature merged with the actual temperature, creating fog so thick that visibility dropped to "
        "zero and airports halted all operations completely."
    ),
    (
        "Saharan dust transported across the Atlantic created hazy skies and vivid sunsets, the particle laden air "
        "filtering light into dramatic reds and oranges beautifully."
    ),
    (
        "The MCS maintained its intensity throughout the night, the training storms dropping excessive rainfall on the "
        "same areas for hours and causing catastrophic flooding."
    ),
    (
        "Supercooled water droplets in the cloud instantly froze on contact with the aircraft, requiring immediate "
        "descent to warmer altitudes to shed the dangerous ice."
    ),
    (
        "The boundary layer decoupled from the surface overnight, winds aloft increasing to fifty knots while "
        "conditions at ground level remained calm and still."
    ),
    (
        "Fair weather cumulus dotted the afternoon sky, their puffy white forms indicating good weather and making for "
        "perfect conditions for outdoor activities everywhere."
    ),
]

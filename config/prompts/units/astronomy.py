"""Unit prompts: long astronomy, weather, aviation, and photography prompts."""

from __future__ import annotations

ASTRONOMY: list[str] = [
    # LONG EXAMPLES - ASTRONOMY AND SPACE
    (
        "The distance from Earth to the Sun is about ninety three million miles or one hundred fifty million "
        "kilometers, defined as one astronomical unit."
    ),
    (
        "Light from the Sun takes eight minutes and twenty seconds to reach Earth, traveling at one hundred eighty six "
        "thousand miles per second."
    ),
    (
        "The nearest star to our solar system, Proxima Centauri, is four point two four light years away, or about "
        "twenty five trillion miles."
    ),
    (
        "The International Space Station orbits at an altitude of approximately two hundred fifty miles and travels at "
        "seventeen thousand five hundred miles per hour."
    ),
    (
        "Temperature on the Moon ranges from negative two eighty degrees Fahrenheit at night to two sixty degrees "
        "Fahrenheit during the day."
    ),
    (
        "Mars is an average of one hundred forty million miles from Earth, and signals take between four and twenty "
        "four minutes to travel between the planets."
    ),
    (
        "The escape velocity from Earth's surface is twenty five thousand miles per hour or eleven point two "
        "kilometers per second."
    ),
    (
        "Jupiter's Great Red Spot is a storm roughly ten thousand miles wide, about one and a quarter times the "
        "diameter of Earth."
    ),
    (
        "The Milky Way galaxy is approximately one hundred thousand light years in diameter, containing an estimated "
        "two hundred billion stars."
    ),
    (
        "A year on Mercury is only eighty eight Earth days, while a day on Mercury lasts fifty nine Earth days due to "
        "its slow rotation."
    ),
    (
        "The Hubble Space Telescope orbits at three hundred forty miles above Earth and can detect objects with "
        "apparent magnitudes down to thirty one."
    ),
    (
        "Solar flares can heat plasma to tens of millions of degrees Celsius and eject billions of tons of material "
        "into space."
    ),
    (
        "The cosmic microwave background radiation has a temperature of two point seven two five Kelvin, just above "
        "absolute zero."
    ),
    (
        "Saturn's rings extend from four thousand three hundred miles to eighty thousand miles above the planet's "
        "equator but are only about thirty feet thick."
    ),
    (
        "A pulsar can rotate up to seven hundred sixteen times per second while emitting beams of electromagnetic "
        "radiation with clocklike precision."
    ),
    # LONG EXAMPLES - WEATHER AND CLIMATE
    (
        "Hurricane category five storms have sustained winds exceeding one hundred fifty seven miles per hour with a "
        "central pressure below nine twenty millibars."
    ),
    (
        "The highest temperature ever recorded on Earth was one thirty four degrees Fahrenheit in Death Valley on July "
        "tenth, nineteen thirteen."
    ),
    (
        "Tornado intensity is measured on the Enhanced Fujita scale, with EF five tornadoes having winds exceeding two "
        "hundred miles per hour."
    ),
    (
        "Annual rainfall in the Amazon basin averages about eighty inches, while Death Valley receives less than two "
        "inches of precipitation per year."
    ),
    (
        "Humidity above sixty percent makes temperatures feel warmer, with the heat index at ninety degrees and "
        "seventy percent humidity feeling like one hundred six."
    ),
    (
        "Wind chill calculations show that twenty degrees Fahrenheit with a fifteen mile per hour wind feels like six "
        "degrees Fahrenheit on exposed skin."
    ),
    (
        "Fog forms when the temperature drops to within two to three degrees of the dew point and visibility is "
        "reduced to less than one kilometer."
    ),
    (
        "Hail can fall at speeds up to one hundred miles per hour, with the largest recorded hailstone measuring eight "
        "inches in diameter."
    ),
    (
        "The coldest temperature ever recorded was negative one twenty eight point six degrees Fahrenheit at Vostok "
        "Station in Antarctica in nineteen eighty three."
    ),
    (
        "Average global sea level has risen about eight inches since eighteen eighty and is currently rising at a rate "
        "of about point thirteen inches per year."
    ),
    (
        "The ozone hole over Antarctica reached its maximum size of eleven point five million square miles in "
        "September two thousand six."
    ),
    (
        "Lightning bolts can reach temperatures of fifty four thousand degrees Fahrenheit, about five times hotter "
        "than the surface of the Sun."
    ),
    (
        "Atmospheric carbon dioxide concentration has risen from two eighty parts per million pre industrial to over "
        "four twenty parts per million today."
    ),
    (
        "Snowfall accumulation requires ground temperatures below thirty five degrees Fahrenheit with air temperatures "
        "at or below freezing at cloud level."
    ),
    (
        "Average sea surface temperature has increased by about one point five degrees Fahrenheit since nineteen "
        "hundred, with accelerating trends in recent decades."
    ),
    # LONG EXAMPLES - AVIATION AND NAVIGATION
    (
        "Commercial aircraft typically cruise at thirty five thousand feet and five hundred miles per hour, with cabin "
        "pressure maintained at eight thousand feet equivalent."
    ),
    (
        "A nautical mile equals one point one five statute miles or one point eight five kilometers, originally "
        "defined as one minute of arc along a meridian."
    ),
    (
        "Runway visual range must be at least one thousand two hundred feet for a Category One instrument landing "
        "approach in low visibility conditions."
    ),
    (
        "The standard rate turn in aviation is three degrees per second, completing a full three sixty degree turn in "
        "exactly two minutes."
    ),
    (
        "Aircraft climb performance is measured in feet per minute, with a typical rate of climb being five hundred to "
        "one thousand feet per minute."
    ),
    (
        "Fuel consumption at cruise for a Boeing seven thirty seven is about eight hundred gallons per hour carrying "
        "one fifty passengers."
    ),
    (
        "Decision height for a precision approach is typically two hundred feet above the runway, where the pilot must "
        "see the runway or execute a missed approach."
    ),
    (
        "True airspeed increases by approximately two percent for every one thousand feet of altitude gain at the same "
        "indicated airspeed."
    ),
    (
        "The GPS system provides position accuracy within about three meters for civilian users and centimeter level "
        "accuracy with differential corrections."
    ),
    (
        "Minimum safe altitude over mountainous terrain is two thousand feet above the highest obstacle within four "
        "nautical miles of the aircraft."
    ),
    (
        "A ship's draft of thirty feet means it requires at least thirty five feet of water depth to safely navigate "
        "with adequate under keel clearance."
    ),
    (
        "Visibility is reported in statute miles in the United States, with one mile equaling five thousand two "
        "hundred eighty feet."
    ),
    (
        "The compass variation in the eastern United States is about fifteen degrees west, meaning true north is "
        "fifteen degrees right of magnetic north."
    ),
    (
        "Crosswind component limits for most light aircraft are about fifteen to twenty knots perpendicular to the "
        "runway centerline."
    ),
    (
        "An altimeter setting of twenty nine point nine two inches of mercury indicates standard atmospheric pressure "
        "at sea level."
    ),
    # LONG EXAMPLES - PHOTOGRAPHY AND OPTICS
    (
        "The camera sensor is a full frame thirty five millimeter format measuring thirty six by twenty four "
        "millimeters with forty two megapixels."
    ),
    (
        "Lens focal length of fifty millimeters on a full frame camera provides roughly the same field of view as the "
        "human eye."
    ),
    (
        "At f two point eight and one sixtieth of a second shutter speed, the exposure value is nine, suitable for "
        "overcast outdoor conditions."
    ),
    (
        "The depth of field at f one point four with a subject at three feet is only about two inches, requiring "
        "precise focus on the eyes."
    ),
    (
        "Flash guide number of one forty at ISO one hundred means the flash can properly expose a subject at ten feet "
        "with an f fourteen aperture."
    ),
    (
        "Image stabilization rated at five stops allows handheld shooting at one thirtieth of a second with a two "
        "hundred millimeter lens."
    ),
    "The lens has a minimum focusing distance of eighteen inches and a maximum magnification ratio of one to four.",
    (
        "Sensor dynamic range of fourteen stops captures detail from shadows at negative seven EV to highlights at "
        "positive seven EV."
    ),
    (
        "A telephoto lens of four hundred millimeters has an angle of view of only about six degrees compared to forty "
        "seven degrees for a fifty millimeter lens."
    ),
    (
        "The flash recycle time is about three seconds at full power with a duration of one five thousandth of a "
        "second at minimum power."
    ),
    (
        "Macro photography at one to one magnification with an eighty millimeter lens has a depth of field of less "
        "than two millimeters at f eight."
    ),
    (
        "The projector throws a one hundred inch diagonal image from a distance of twelve feet with a brightness of "
        "three thousand lumens."
    ),
    (
        "Astronomical telescopes with a one thousand millimeter focal length and one hundred millimeter aperture have "
        "a focal ratio of f ten."
    ),
    (
        "Video resolution of four K equals three thousand eight hundred forty by two thousand one hundred sixty pixels "
        "at thirty frames per second."
    ),
    (
        "The polarizing filter reduces reflections by ninety percent when rotated to the optimal angle of ninety "
        "degrees from the light source."
    ),
]

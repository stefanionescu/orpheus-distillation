"""Phone number prompts: long expressions, then numbers from the United Kingdom to China."""

from __future__ import annotations

INTERNATIONAL: list[str] = [
    # LONG PHONE NUMBER EXPRESSIONS
    (
        "If you need to reach me for any reason at all, my cell phone number is three one zero, five five five, four "
        "eight two nine, and I'm available anytime after six."
    ),
    (
        "I've been trying to call this number all day, it's five five five, nine three eight two, and every single "
        "time it just goes straight to voicemail."
    ),
    (
        "Let me give you the customer service number, it's one, eight hundred, five five five, two three four five, "
        "and make sure you press two for billing inquiries."
    ),
    (
        "She left her number on a napkin at the bar, it was five five five, seven two six four, and I've been too "
        "nervous to call her for three days now."
    ),
    (
        "The doctor's office called and left a message saying to call them back at six one seven, five five five, "
        "eight nine zero one, as soon as possible."
    ),
    (
        "I accidentally gave him the wrong number, I said five five five, four five six seven when I meant to say five "
        "five five, four five seven six."
    ),
    (
        "My grandmother still has the same phone number she's had for forty years, it's two one two, five five five, "
        "one nine seven six, and she refuses to change it."
    ),
    (
        "If this is an emergency, please hang up and dial nine one one, otherwise you can reach our main office at "
        "five five five, three three zero zero."
    ),
    (
        "I wrote down the number on my hand but it got smudged, I think it was five five five, eight something "
        "something three, but I can't read the middle part."
    ),
    (
        "The pizza place on the corner has the easiest number to remember, it's five five five, seven four two nine, "
        "which spells out five five five, pizza on the keypad."
    ),
    (
        "I've had the same cell phone number since two thousand and five, it's four one five, five five five, two four "
        "six eight, and everyone knows it by heart."
    ),
    (
        "He blocked my number so I had to call him from my work phone instead, the number there is five five five, one "
        "zero zero zero, extension forty two."
    ),
    (
        "The scam callers keep calling from different numbers but they always start with eight eight eight, five five "
        "five, and then some random four digits."
    ),
    (
        "I need you to write this down because it's really important, the number is seven zero two, five five five, "
        "nine one three five, and ask for Michael when you call."
    ),
    (
        "My phone died and I don't have anyone's number memorized except my mom's, which is five five five, two two "
        "two two, because it's so easy to remember."
    ),
    (
        "The realtor said to call her personal cell if we have any questions, the number is three zero five, five five "
        "five, six seven eight nine, and she's available on weekends."
    ),
    (
        "I found this old phone number in my jacket pocket and I have no idea whose it is, it just says five five "
        "five, four eight two six with a heart next to it."
    ),
    (
        "If you want to leave a tip about the crime, call the anonymous hotline at one, eight hundred, five five five, "
        "tips, that's one, eight hundred, five five five, eight four seven seven."
    ),
    (
        "The vet's emergency line is different from their regular number, for emergencies call five five five, nine "
        "one one one, but for appointments call five five five, two five zero zero."
    ),
    (
        "I've called five five five, seven eight nine zero at least fifteen times today and nobody is picking up, I'm "
        "starting to think they gave me a fake number."
    ),
    (
        "My ex keeps texting me from new numbers, first it was five five five, one two three four, then five five "
        "five, five six seven eight, and now some other random number."
    ),
    (
        "The hotel concierge gave me the number for the best restaurant in town, it's five five five, three seven four "
        "nine, but you need reservations at least two weeks in advance."
    ),
    (
        "I'm going to read you back the number to make sure I have it right, so that's area code eight one eight, five "
        "five five, four four five five, is that correct?"
    ),
    (
        "When I was a kid, our home phone number was five five five, one nine eight seven, and I still remember it "
        "even though we moved out of that house twenty years ago."
    ),
    (
        "The tech support guy gave me a case number and a callback number, the callback is one, eight seven seven, "
        "five five five, help, and my case number is four five six seven eight nine."
    ),
    (
        "I met this amazing person at the conference and they gave me their card with their direct line, it's two zero "
        "two, five five five, one seven seven six, and I'm definitely going to call."
    ),
    (
        "The bank's fraud department number is on the back of your card, it should be one, eight hundred, five five "
        "five, two three two three, and they're available twenty four seven."
    ),
    (
        "My therapist's office has a new number now, it used to be five five five, four four zero zero, but they moved "
        "locations and now it's five five five, seven seven zero zero."
    ),
    (
        "I keep getting calls from five five five, zero zero zero one, and when I answer there's just silence for a "
        "few seconds before they hang up, it's really creepy."
    ),
    (
        "The wedding planner said to text her at five five five, eight six seven five, but if it's urgent I should "
        "call her office at five five five, eight six seven six instead."
    ),
    # INTERNATIONAL PHONE NUMBERS (Non-US)
    # UK Numbers (country code +44)
    "My London number is plus four four, two zero, seven nine four six, three two one eight.",
    "Call the Manchester office at plus four four, one six one, four nine six, eight three two one.",
    "The Birmingham hotel is at plus four four, one two one, three four five, six seven eight nine.",
    "Ring me in Edinburgh at plus four four, one three one, two two six, four five six seven.",
    "The Glasgow branch number is plus four four, one four one, three three two, one two three four.",
    "You can reach our Liverpool office at plus four four, one five one, seven zero eight, nine zero one two.",
    "The Bristol reception is plus four four, one one seven, nine two three, four five six seven.",
    "Call Leeds customer service at plus four four, one one three, two four six, eight zero two four.",
    "My UK mobile is plus four four, seven seven zero zero, nine eight seven, six five four.",
    "Text me on my British number, it's plus four four, seven nine one two, three four five, six seven eight.",
    "The Oxford university line is plus four four, one eight six five, two seven zero, zero zero zero.",
    "Cambridge admissions can be reached at plus four four, one two two three, three three two zero zero zero.",
    "The Sheffield office number is plus four four, one one four, two seven six, five four three two.",
    "Reach the Newcastle team at plus four four, one nine one, two three zero, four five six seven.",
    "The Cardiff branch is at plus four four, two nine, two zero two zero, three zero three zero.",
    # German Numbers (country code +49)
    "Call Berlin at plus four nine, three zero, one two three four, five six seven eight.",
    "The München office is plus four nine, eight nine, seven six five four, three two one zero.",
    "Reach Hamburg at plus four nine, four zero, nine eight seven six, five four three two.",
    "My Frankfurt number is plus four nine, six nine, two three four five, six seven eight nine.",
    "The Köln branch can be reached at plus four nine, two two one, three four five, six seven eight nine.",
    "Call our Düsseldorf office at plus four nine, two one one, nine eight seven, six five four three.",
    "The Stuttgart hotline is plus four nine, seven one one, one two three, four five six seven.",
    "Reach the Leipzig team at plus four nine, three four one, eight seven six, five four three two.",
    "My German mobile is plus four nine, one seven zero, nine eight seven six, five four three.",
    "The Dresden office number is plus four nine, three five one, two three four, five six seven eight.",
    "Call the Hannover branch at plus four nine, five one one, four five six, seven eight nine zero.",
    "The Nürnberg reception is plus four nine, nine one one, three three three, four four four four.",
    "Reach Bremen customer service at plus four nine, four two one, five five five, six six six six.",
    "The Dortmund line is plus four nine, two three one, seven seven seven, eight eight eight eight.",
    "My Essen number is plus four nine, two zero one, one two three, four five six seven.",
    # French Numbers (country code +33)
    "Call Paris at plus three three, one, four two, three four, five six, seven eight.",
    "The Lyon office is plus three three, four, seven two, eight three, nine four, zero five.",
    "Reach Marseille at plus three three, four, nine one, two three, four five, six seven.",
    "My Bordeaux number is plus three three, five, five six, seven eight, nine zero, one two.",
    "The Nice branch is plus three three, four, nine three, four five, six seven, eight nine.",
    "Call our Toulouse office at plus three three, five, six one, two three, four five, six seven.",
    "The Strasbourg hotline is plus three three, three, eight eight, nine nine, zero zero, one one.",
    "Reach the Nantes team at plus three three, two, four zero, five one, six two, seven three.",
    "My French mobile is plus three three, six, zero seven, zero eight, zero nine, one zero.",
    "The Lille office number is plus three three, three, two zero, three one, four two, five three.",
    "Call the Montpellier branch at plus three three, four, six seven, seven eight, eight nine, nine zero.",
    "The Rennes reception is plus three three, two, nine nine, eight eight, seven seven, six six.",
    "Reach Grenoble customer service at plus three three, four, seven six, five four, three two, one zero.",
    "The Dijon line is plus three three, three, eight zero, seven one, six two, five three.",
    "My Cannes number is plus three three, four, nine three, eight two, seven one, six zero.",
    # Spanish Numbers (country code +34)
    "Call Madrid at plus three four, nine one, one two three, four five, six seven.",
    "The Barcelona office is plus three four, nine three, nine eight seven, six five, four three.",
    "Reach Valencia at plus three four, nine six, three four five, six seven, eight nine.",
    "My Sevilla number is plus three four, nine five, four five six, seven eight, nine zero.",
    "The Bilbao branch is plus three four, nine four, six seven eight, nine zero, one two.",
    "Call our Málaga office at plus three four, nine five, two three four, five six, seven eight.",
    "The Zaragoza hotline is plus three four, nine seven six, one two three, four five six.",
    "Reach the Granada team at plus three four, nine five eight, three four five, six seven eight.",
    "My Spanish mobile is plus three four, six seven eight, nine zero one, two three four.",
    "The Alicante office number is plus three four, nine six five, four three two, one zero nine.",
    "Call the Córdoba branch at plus three four, nine five seven, six five four, three two one.",
    "The Valladolid reception is plus three four, nine eight three, two one zero, nine eight seven.",
    "Reach Murcia customer service at plus three four, nine six eight, seven six five, four three two.",
    "The Palma line is plus three four, nine seven one, eight nine zero, one two three.",
    "My San Sebastián number is plus three four, nine four three, four five six, seven eight nine.",
    # Italian Numbers (country code +39)
    "Call Roma at plus three nine, zero six, one two three four, five six seven eight.",
    "The Milano office is plus three nine, zero two, nine eight seven six, five four three two.",
    "Reach Napoli at plus three nine, zero eight one, three four five six, seven eight nine zero.",
    "My Torino number is plus three nine, zero one one, two three four five, six seven eight nine.",
    "The Firenze branch is plus three nine, zero five five, four five six seven, eight nine zero one.",
    "Call our Venezia office at plus three nine, zero four one, five six seven eight, nine zero one two.",
    "The Bologna hotline is plus three nine, zero five one, six seven eight nine, zero one two three.",
    "Reach the Genova team at plus three nine, zero one zero, seven eight nine zero, one two three four.",
    "My Italian mobile is plus three nine, three three nine, eight seven six five, four three two one.",
    "The Palermo office number is plus three nine, zero nine one, nine eight seven six, five four three two.",
    "Call the Catania branch at plus three nine, zero nine five, one two three four, five six seven eight.",
    "The Bari reception is plus three nine, zero eight zero, two three four five, six seven eight nine.",
    "Reach Verona customer service at plus three nine, zero four five, three four five six, seven eight nine zero.",
    "The Padova line is plus three nine, zero four nine, four five six seven, eight nine zero one.",
    "My Trieste number is plus three nine, zero four zero, five six seven eight, nine zero one two.",
    # Japanese Numbers (country code +81)
    "Call Tokyo at plus eight one, three, one two three four, five six seven eight.",
    "The Osaka office is plus eight one, six, nine eight seven six, five four three two.",
    "Reach Kyoto at plus eight one, seven five, three four five, six seven eight nine.",
    "My Yokohama number is plus eight one, four five, two three four, five six seven eight.",
    "The Nagoya branch is plus eight one, five two, four five six, seven eight nine zero.",
    "Call our Sapporo office at plus eight one, one one, five six seven, eight nine zero one.",
    "The Fukuoka hotline is plus eight one, nine two, six seven eight, nine zero one two.",
    "Reach the Kobe team at plus eight one, seven eight, seven eight nine, zero one two three.",
    "My Japanese mobile is plus eight one, nine zero, one two three four, five six seven eight.",
    "The Hiroshima office number is plus eight one, eight two, eight nine zero, one two three four.",
    "Call the Sendai branch at plus eight one, two two, nine zero one, two three four five.",
    "The Kawasaki reception is plus eight one, four four, zero one two, three four five six.",
    "Reach Chiba customer service at plus eight one, four three, one two three, four five six seven.",
    "The Saitama line is plus eight one, four eight, two three four, five six seven eight.",
    "My Shizuoka number is plus eight one, five four, three four five, six seven eight nine.",
    # Australian Numbers (country code +61)
    "Call Sydney at plus six one, two, nine eight seven six, five four three two.",
    "The Melbourne office is plus six one, three, one two three four, five six seven eight.",
    "Reach Brisbane at plus six one, seven, three four five six, seven eight nine zero.",
    "My Perth number is plus six one, eight, four five six seven, eight nine zero one.",
    "The Adelaide branch is plus six one, eight, five six seven eight, nine zero one two.",
    "Call our Gold Coast office at plus six one, seven, five five six seven, eight nine zero one.",
    "The Canberra hotline is plus six one, two, six two three four, five six seven eight.",
    "Reach the Darwin team at plus six one, eight, eight nine zero one, two three four five.",
    "My Australian mobile is plus six one, four, one two three four, five six seven eight.",
    "The Hobart office number is plus six one, three, six two three four, five six seven eight.",
    "Call the Newcastle branch at plus six one, two, four nine eight seven, six five four three.",
    "The Wollongong reception is plus six one, two, four two three four, five six seven eight.",
    "Reach Cairns customer service at plus six one, seven, four zero three four, five six seven eight.",
    "The Townsville line is plus six one, seven, four seven eight nine, zero one two three.",
    "My Geelong number is plus six one, three, five two three four, five six seven eight.",
    # Brazilian Numbers (country code +55)
    "Call São Paulo at plus five five, one one, nine eight seven six, five four three two.",
    "The Rio de Janeiro office is plus five five, two one, one two three four, five six seven eight.",
    "Reach Brasília at plus five five, six one, three four five six, seven eight nine zero.",
    "My Salvador number is plus five five, seven one, four five six seven, eight nine zero one.",
    "The Belo Horizonte branch is plus five five, three one, five six seven eight, nine zero one two.",
    "Call our Fortaleza office at plus five five, eight five, six seven eight nine, zero one two three.",
    "The Curitiba hotline is plus five five, four one, seven eight nine zero, one two three four.",
    "Reach the Recife team at plus five five, eight one, eight nine zero one, two three four five.",
    "My Brazilian mobile is plus five five, one one, nine nine eight seven, six five four three.",
    "The Porto Alegre office number is plus five five, five one, nine zero one two, three four five six.",
    "Call the Manaus branch at plus five five, nine two, zero one two three, four five six seven.",
    "The Belém reception is plus five five, nine one, one two three four, five six seven eight.",
    "Reach Goiânia customer service at plus five five, six two, two three four five, six seven eight nine.",
    "The Campinas line is plus five five, one nine, three four five six, seven eight nine zero.",
    "My Florianópolis number is plus five five, four eight, four five six seven, eight nine zero one.",
    # Mexican Numbers (country code +52)
    "Call Ciudad de México at plus five two, five five, one two three four, five six seven eight.",
    "The Guadalajara office is plus five two, three three, nine eight seven six, five four three two.",
    "Reach Monterrey at plus five two, eight one, three four five six, seven eight nine zero.",
    "My Cancún number is plus five two, nine nine eight, four five six seven, eight nine zero.",
    "The Puebla branch is plus five two, two two two, five six seven eight, nine zero one two.",
    "Call our Tijuana office at plus five two, six six four, six seven eight nine, zero one two three.",
    "The León hotline is plus five two, four seven seven, seven eight nine zero, one two three four.",
    "Reach the Mérida team at plus five two, nine nine nine, eight nine zero one, two three four five.",
    "My Mexican mobile is plus five two, one, five five, one two three four, five six seven eight.",
    "The Querétaro office number is plus five two, four four two, nine zero one two, three four five six.",
    "Call the Toluca branch at plus five two, seven two two, zero one two three, four five six seven.",
    "The Aguascalientes reception is plus five two, four four nine, one two three four, five six seven eight.",
    "Reach Morelia customer service at plus five two, four four three, two three four five, six seven eight nine.",
    "The San Luis Potosí line is plus five two, four four four, three four five six, seven eight nine zero.",
    "My Veracruz number is plus five two, two two nine, four five six seven, eight nine zero one.",
    # Indian Numbers (country code +91)
    "Call Mumbai at plus nine one, two two, one two three four, five six seven eight.",
    "The Delhi office is plus nine one, one one, nine eight seven six, five four three two.",
    "Reach Bangalore at plus nine one, eight zero, three four five six, seven eight nine zero.",
    "My Chennai number is plus nine one, four four, four five six seven, eight nine zero one.",
    "The Kolkata branch is plus nine one, three three, five six seven eight, nine zero one two.",
    "Call our Hyderabad office at plus nine one, four zero, six seven eight nine, zero one two three.",
    "The Pune hotline is plus nine one, two zero, seven eight nine zero, one two three four.",
    "Reach the Ahmedabad team at plus nine one, seven nine, eight nine zero one, two three four five.",
    "My Indian mobile is plus nine one, nine eight seven six, five four three two, one zero.",
    "The Jaipur office number is plus nine one, one four one, nine zero one two, three four five six.",
    "Call the Lucknow branch at plus nine one, five two two, zero one two three, four five six seven.",
    "The Chandigarh reception is plus nine one, one seven two, one two three four, five six seven eight.",
    "Reach Kochi customer service at plus nine one, four eight four, two three four five, six seven eight nine.",
    "The Goa line is plus nine one, eight three two, three four five six, seven eight nine zero.",
    "My Surat number is plus nine one, two six one, four five six seven, eight nine zero one.",
    # Chinese Numbers (country code +86)
    "Call Beijing at plus eight six, one zero, one two three four, five six seven eight.",
    "The Shanghai office is plus eight six, two one, nine eight seven six, five four three two.",
    "Reach Guangzhou at plus eight six, two zero, three four five six, seven eight nine zero.",
    "My Shenzhen number is plus eight six, seven five five, four five six seven, eight nine zero one.",
    "The Chengdu branch is plus eight six, two eight, five six seven eight, nine zero one two.",
    "Call our Hangzhou office at plus eight six, five seven one, six seven eight nine, zero one two three.",
    "The Wuhan hotline is plus eight six, two seven, seven eight nine zero, one two three four.",
    "Reach the Nanjing team at plus eight six, two five, eight nine zero one, two three four five.",
    "My Chinese mobile is plus eight six, one three nine, eight seven six five, four three two one.",
    "The Xi'an office number is plus eight six, two nine, nine zero one two, three four five six.",
    "Call the Tianjin branch at plus eight six, two two, zero one two three, four five six seven.",
    "The Suzhou reception is plus eight six, five one two, one two three four, five six seven eight.",
    "Reach Qingdao customer service at plus eight six, five three two, two three four five, six seven eight nine.",
    "The Dalian line is plus eight six, four one one, three four five six, seven eight nine zero.",
    "My Xiamen number is plus eight six, five nine two, four five six seven, eight nine zero one.",
]

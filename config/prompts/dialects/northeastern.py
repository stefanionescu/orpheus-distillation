"""Dialect prompts in New York, Boston, and Canadian English, short to long."""

from __future__ import annotations

NORTHEASTERN: list[str] = [
    # NEW YORK - SHORT
    "Fuggedaboutit!",
    "I'm walkin' here!",
    "Howya doin'?",
    "Get outta here!",
    "What are you, crazy?",
    "That's mad disrespectful.",
    "Word, that's facts.",
    "Deadass, I'm not lying.",
    "It's brick outside.",
    "That's tight, no cap.",
    "I'm good, you good?",
    "That's mad wack.",
    "Son, you bugging.",
    "I'm heated right now.",
    "That's lowkey fire.",
    # NEW YORK - MEDIUM
    "I've been standing on line for like an hour waiting for this bodega sandwich and I'm starving.",
    "You gotta take the express train to get there faster, local stops at every station and it takes forever.",
    "The pizza in this city is something else, nothing compares to a real New York slice honestly.",
    "He's acting real sus lately, something's definitely going on that he's not telling us about.",
    "I'm not gonna lie, that movie was mad boring, fell asleep like twenty minutes into it.",
    "We're going to the stoop later to hang out, you should come through if you're not doing anything.",
    "The landlord's raising the rent again, like we're not already paying an arm and a leg here.",
    "She's being real extra right now, making a big deal out of nothing as usual with the drama.",
    "I caught the A train downtown and it was packed like sardines, couldn't even move an inch.",
    "That new spot in Brooklyn is fire, the food is crazy good and the vibes are immaculate.",
    "He came at me sideways so I had to check him real quick, can't let that slide you know.",
    "I'm deadass tired of this weather, one day it's hot and the next day it's freezing outside.",
    "She's from the Bronx originally but moved to Queens a few years ago for work and family.",
    "You buggin if you think I'm paying that much for a drink, twenty dollars for a cocktail is insane.",
    "The bodega cat is the real owner of that place, just sits there judging everyone who walks in.",
    # NEW YORK - LONG
    (
        "I've been in this city for like fifteen years now and I still can't believe how crazy the rent is, paying "
        "more for a shoebox apartment than people pay for whole houses in other places."
    ),
    (
        "He's out here acting like he's the mayor or something, walking around with that big ego when really he's just "
        "some guy from Staten Island who thinks he's all that and a bag of chips."
    ),
    (
        "The subway was running late again this morning, big surprise, ended up having to take an Uber to work and "
        "that set me back like forty bucks just to get to Midtown on time."
    ),
    (
        "She's been living in Manhattan her whole life and still can't parallel park to save her life, but then again "
        "nobody really drives in the city anyway so it doesn't even matter."
    ),
    (
        "I'm telling you right now, the bagels here are the best in the world and I will fight anyone who disagrees, "
        "something about the water makes them taste completely different than anywhere else."
    ),
    # BOSTON - SHORT
    "Pahk the cah in Hahvahd Yahd.",
    "That's wicked pissah!",
    "I'm gonna take a packie run.",
    "No suh, not happening.",
    "She's a wicked smart kid.",
    "Get me a regulah coffee.",
    "It's colder than a witch's you know what.",
    "We got rotaries everywhere here.",
    "The T's running late again.",
    "I'll meet you at the Gahden.",
    "He's such a masshole driver.",
    "You want jimmies on that?",
    "That's down by the hahbah.",
    "Dunkin' runs on this city.",
    "Bang a uey up here.",
    # BOSTON - MEDIUM
    "The Sox are playing at Fenway tonight, you wanna grab some tickets and head down there?",
    "I grew up in Southie, been here my whole life and I'm never leaving this neighborhood.",
    "The chowdah at Legal Seafoods is the best in the city, don't let anyone tell you different.",
    "He's got a wicked bad attitude, been walking around like someone stole his candybah all day.",
    "We're heading down the Cape this weekend, gonna stay at my aunt's place in Provincetown.",
    "The traffic on the Pike was absolutely brutal this morning, took me two hours to get in.",
    "She's a real townie, knows everyone in the neighborhood and all their business too.",
    "I need to hit the packie before the party, we're almost out of beers and mixers already.",
    "The Pats are looking good this season, might actually make it to the playoffs if they keep winning.",
    "He's from Cambridge but acts like he's from the city, nobody's buying that act though.",
    "The nor'easter is supposed to hit tomorrow, better stock up on supplies just in case.",
    "I went to UMass for undergrad then came back here for grad school at Northeastern.",
    "She's wicked excited about the concert, been counting down the days for like three months now.",
    "The housing prices here are absolutely insane, can't afford anything decent within city limits anymore.",
    "He took the commuter rail in from Worcester, that's like an hour and a half each way daily.",
    # BOSTON - LONG
    (
        "I've been going to the same barbah for like twenty years, my fathah went there and his fathah before him, "
        "it's a whole family tradition at this point and I wouldn't change it for anything."
    ),
    (
        "The winter here is absolutely brutal, you've got to be tough to live in this city, between the snow and the "
        "cold and the wind off the harbor, it's not for the faint of heart."
    ),
    (
        "She's a true Bostonian through and through, bleeds green for the Celtics and has never missed a St. Patrick's "
        "Day parade in Southie her entire life since she was a little kid."
    ),
    (
        "We used to hang out at the Common after school, just sitting on the benches watching people walk by, those "
        "were simpler times before everyone got so busy with work and family stuff."
    ),
    (
        "The accent isn't going anywhere no matter how long I live outside the city, as soon as I get home it comes "
        "right back, my friends out west think it's hilarious when I slip back into it."
    ),
    # CANADIAN - SHORT
    "Sorry about that, eh?",
    "That's a real beauty, bud.",
    "Give'er, let's go!",
    "It's cold out there, eh?",
    "Timmies run anyone?",
    "That's a real keener.",
    "He's a total hoser.",
    "Let's have a dart.",
    "Just grabbing some Timbits.",
    "Out for a rip, bud?",
    "Yeah, no for sure.",
    "Take off, eh!",
    "Double double please.",
    "Going to the Soo this weekend.",
    "That's a real gongshow.",
    # CANADIAN - MEDIUM
    "I'm heading to the cabin this weekend for some ice fishing, should be a good time out there.",
    "The Leafs lost again last night, honestly at this point I don't know why I keep watching.",
    "She's a real beauty of a woman, met her at a hockey game and we've been together ever since.",
    "It's absolutely freezing out there today, must be like minus thirty with the windchill factor.",
    "We're gonna have a few wobbly pops after work, you should come down to the bar with us.",
    "He's being a real keener about the project, showing up early and staying late every single day.",
    "The moose are out this time of year, gotta be careful driving on the highway after dark.",
    "I got a flat tire on the 401 and some guy stopped to help me change it, real nice fella.",
    "We're having a house party Saturday night, byob and there'll be a bonfire out back eh.",
    "She's from Newfoundland originally but moved out to Alberta for the oil field jobs.",
    "The poutine at that chip truck is unreal, best gravy and cheese curds in the whole province.",
    "He's got a real thick Quebecois accent, sometimes I have trouble understanding what he's saying.",
    "The cottage is right on the lake, we go swimming and canoeing all summer long up there.",
    "I was so choked when they cancelled the concert, had been looking forward to it for months.",
    "You can't beat a good Canadian winter, as long as you've got the right gear you'll be fine.",
    # CANADIAN - LONG
    (
        "Listen bud, I know you're upset about what happened but you've gotta let it go, holding onto that anger isn't "
        "doing you any good and life's too short to be carrying around that kind of baggage eh."
    ),
    (
        "The winters up in Winnipeg are absolutely brutal, I'm talking forty below with the windchill and snow up to "
        "your waist, you've really gotta be built different to survive that kind of weather."
    ),
    (
        "We drove all the way from Vancouver to Toronto last summer, took us about a week with all the stops, but it "
        "was worth it to see the prairies and the mountains and everything in between."
    ),
    (
        "She's one of the nicest people you'll ever meet, always saying sorry even when it's not her fault, baking "
        "cookies for the neighbors, just a genuinely good person through and through."
    ),
    (
        "The hockey tournament this weekend is gonna be a real gongshow, twelve teams and only two rinks, gonna be "
        "games going from six in the morning till midnight for three days straight."
    ),
]

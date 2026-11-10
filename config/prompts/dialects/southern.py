"""Dialect prompts in Southern US, British, Australian, Scottish, and Irish English, short to long."""

from __future__ import annotations

SOUTHERN: list[str] = [
    # SOUTHERN US - SHORT
    "Y'all come back now, ya hear?",
    "Well, bless your heart.",
    "I'm fixin' to head out.",
    "That dog won't hunt.",
    "She's madder than a wet hen.",
    "I reckon so.",
    "He ain't got the sense God gave a goose.",
    "Well, I'll be.",
    "That's slicker than snot on a doorknob.",
    "Might could do that.",
    "I'm fixin' to tan your hide.",
    "She's prettier than a speckled pup.",
    "He's all hat and no cattle.",
    "Over yonder by the barn.",
    "That ain't my first rodeo.",
    # SOUTHERN US - MEDIUM
    "Y'all ain't from around here, are ya? I can tell by the way you talk.",
    "I'm so hungry I could eat the south end of a northbound mule right about now.",
    "Bless her heart, she's trying her best but that casserole ain't fit to eat.",
    "He's been running around like a chicken with its head cut off all morning.",
    "If the good Lord's willing and the creek don't rise, we'll be there by suppertime.",
    "She was fit to be tied when she found out what he did behind her back.",
    "That boy's about as useful as a screen door on a submarine, I tell you what.",
    "Mama's gonna pitch a fit when she sees what you done to her flower garden.",
    "We're fixin' to have ourselves a real good time at the church potluck this Sunday.",
    "He's so country he thinks a seven course meal is a possum and a six pack.",
    "Well butter my biscuit, I haven't seen you since you were knee high to a grasshopper.",
    "She's sweeter than sweet tea on a hot summer day sitting on the porch.",
    "That there's my daddy's truck, been in the family longer than I been alive.",
    "I ain't seen hide nor hair of him since he took off last Tuesday morning.",
    "You're preaching to the choir, honey, I already know all about that mess.",
    # SOUTHERN US - LONG
    (
        "Well I declare, if that ain't the most ridiculous thing I ever did hear in all my born days, and Lord knows "
        "I've heard some doozies in my time living here."
    ),
    (
        "Mama always said you catch more flies with honey than vinegar, and I reckon she was right about that because "
        "being nice gets you further than being ugly to folks."
    ),
    (
        "We're about to have a come to Jesus meeting with that boy because he's been acting a fool and somebody needs "
        "to set him straight before he embarrasses the whole family."
    ),
    (
        "I tell you what, it's hotter than blue blazes out here today, and if it gets any worse I'm fixin' to melt "
        "right into the pavement like butter on a hot biscuit."
    ),
    (
        "Y'all better get your behinds in this house before I count to three, and you don't want to see what happens "
        "when I get to three, I promise you that much."
    ),
    # BRITISH ENGLISH - SHORT
    "Bloody hell, that was close!",
    "That's absolutely brilliant, mate.",
    "You having a laugh, innit?",
    "Cheers for that, really appreciate it.",
    "I'm absolutely knackered.",
    "That's proper dodgy, that is.",
    "Bit of a sticky wicket.",
    "I'm chuffed to bits.",
    "Fancy a cuppa?",
    "That's bang out of order.",
    "Bob's your uncle!",
    "I'm gobsmacked, honestly.",
    "Don't be daft.",
    "She's having a whinge again.",
    "That's rubbish, absolute rubbish.",
    # BRITISH ENGLISH - MEDIUM
    "I couldn't be bothered to go out tonight, I'm absolutely cream crackered from work.",
    "He's gone and done a runner, left us with the bill and everything, cheeky sod.",
    "That film was proper mental, wasn't expecting that twist at the end at all, blimey.",
    "I'm not being funny, but that bloke's been giving me the evils all evening long.",
    "She's taken the mickey out of me one too many times, I've had it up to here.",
    "The queue at Tesco was absolutely mental, must've waited ages just for a pint of milk.",
    "He's lost the plot completely, going on about conspiracy theories and all that malarkey.",
    "That curry was absolutely lush, best one I've had in donkey's years to be honest.",
    "She's been rabbiting on for hours about her new boyfriend, my ears are bleeding here.",
    "I'm proper minted after that bonus, might splash out on a nice holiday somewhere warm.",
    "The weather's been absolutely pants lately, nothing but grey skies and drizzle for weeks.",
    "He's a bit of a numpty if I'm honest, always getting himself into daft situations.",
    "I was made redundant last month, still looking for work, it's been a right nightmare.",
    "That party was an absolute belter, didn't get home till half four in the morning.",
    "She's well fit, I've been trying to pluck up the courage to ask her out for ages.",
    # BRITISH ENGLISH - LONG
    (
        "Right, I'm absolutely gutted about the whole situation because I really thought we had a chance, but "
        "apparently the universe had other plans for us and that's just how it goes sometimes."
    ),
    (
        "He went down the pub last night for a quick pint and didn't come home till three in the morning, his missus "
        "was absolutely fuming and I don't blame her one bit."
    ),
    (
        "I haven't got a scooby what's going on with the trains lately, every single day there's delays and "
        "cancellations, you'd think they could sort it out after all these years of complaints."
    ),
    (
        "She's proper lovely, always helping out the neighbors and making sure everyone's alright, the kind of person "
        "who'd give you the shirt off her back without thinking twice about it."
    ),
    (
        "The lads are coming round for the match tonight, gonna order some pizza and have a few beers, should be a "
        "proper good time if we actually manage to win for once."
    ),
    # AUSTRALIAN - SHORT
    "No worries, mate.",
    "She'll be right.",
    "Fair dinkum, that's true.",
    "Strewth, that was close!",
    "He's a bit of a drongo.",
    "Good on ya, mate!",
    "That's heaps good.",
    "I'm flat out like a lizard drinking.",
    "Don't be a galah.",
    "Reckon it's arvo already.",
    "Chuck a sickie today.",
    "Having a barbie this weekend?",
    "That's bonzer, mate!",
    "He's gone walkabout again.",
    "Sweet as, bro.",
    # AUSTRALIAN - MEDIUM
    "I was out in the bush last weekend and saw a ripper of a sunset, absolutely stunning.",
    "The servo down the road has the cheapest fuel around, better fill up the ute there.",
    "We're having a few mates over for a barbie this arvo, bring your own tinnies yeah?",
    "He stacked it pretty hard on his bike but he's alright, just a few scratches and bruises.",
    "The mozzies are absolutely shocking this time of year, getting eaten alive out here mate.",
    "She's a hard yakka worker, always first one in and last one out at the office.",
    "That bloke's got a few kangaroos loose in the top paddock if you ask me personally.",
    "The beach was chockers yesterday, couldn't find a spot to put the towel down anywhere.",
    "I'm buggered after that hike, must have walked at least twenty kays through the scrub.",
    "He's off his chops at the moment, been acting strange ever since he got back from Bali.",
    "We had a blue with the neighbors about the fence line, got pretty heated for a bit.",
    "The footy was absolutely ripper last night, our team flogged them by sixty points easy.",
    "Grab some snags and a slab from the bottle shop on your way over this afternoon.",
    "It's stinking hot today, must be pushing forty degrees, gonna stay inside with the aircon.",
    "That comedian was an absolute pisser, haven't laughed that hard in ages, fair dinkum funny.",
    # AUSTRALIAN - LONG
    (
        "Mate, I reckon we should head down to the coast this weekend, surf's supposed to be pumping and we haven't "
        "had a proper beach day in yonks, bring the esky and some cold ones."
    ),
    (
        "The tradie who came to fix the dunny was a top bloke, sorted it out in no time flat and didn't even charge us "
        "through the nose like the last mob we called did."
    ),
    (
        "I'm absolutely rapt about the promotion, been working my ring off for years and finally the boss noticed, "
        "gonna shout the team a round at the pub to celebrate tonight."
    ),
    (
        "She's as Aussie as they come, grew up in the outback surrounded by nothing but red dirt and blue skies, "
        "toughest sheila you'll ever meet in your life, no kidding around."
    ),
    (
        "The drop bears aren't real but we love telling the tourists about them, the look on their faces when they "
        "start checking the trees is absolutely priceless every single time."
    ),
    # SCOTTISH - SHORT
    "Aye, that's pure dead brilliant.",
    "Och, away with ye!",
    "I'm absolutely scunnered.",
    "That's pure braw, so it is.",
    "Yer aff yer heid!",
    "Dinnae fash yerself.",
    "He's a right numpty.",
    "Gie it laldy!",
    "I'm fair puckled.",
    "That's boggin', that is.",
    "Haud yer wheesht!",
    "It's a wee bit nippy.",
    "What's the crack then?",
    "She's away with the fairies.",
    "That's mingin'!",
    # SCOTTISH - MEDIUM
    "I cannae be bothered going out tonight, it's absolutely teeming down and I'm knackered.",
    "She's been giving me pure evils all day and I haven't got a clue what I've done wrong.",
    "The lads are heading to the pub for a wee swally, you coming along or staying home then?",
    "That was a right good scran, haven't had a chippy that good since I left Glasgow honestly.",
    "He's been havering on about football for hours, my ears are about to fall off here.",
    "The wean's been greeting all morning, think she might be coming down with something nasty.",
    "I'm pure beelin' about what happened, they had no right to treat us like that at all.",
    "She's as mad as a box of frogs but she's good people, heart of gold that one has.",
    "The weather's been dreich all week, nothing but grey skies and horizontal rain nonstop.",
    "He's acting the maggot again, always causing trouble wherever he goes, that one does.",
    "We're planning a wee trip up to the Highlands for Hogmanay, should be a good craic.",
    "I'm absolutely famished, could murder a haggis supper right about now to be honest.",
    "That gadgie's been eyeing up your motor all afternoon, might want to keep an eye out.",
    "She's got a face like a skelped erse, been in a right mood since she woke up this morning.",
    "The match was a pure riddy, absolutely embarrassing performance from the whole team yesterday.",
    # SCOTTISH - LONG
    (
        "Och aye, I mind when this whole place was nothing but fields as far as the eye could see, now it's all fancy "
        "flats and coffee shops, times have changed something fierce around here."
    ),
    (
        "She's absolutely radge sometimes but you cannae help but love her, she'd give you her last penny and the coat "
        "off her back if you needed it, proper salt of the earth type."
    ),
    (
        "We went for a wee dram at the local last night and ended up staying till closing, the banter was absolutely "
        "top notch and the whisky was flowing like water, brilliant night."
    ),
    (
        "I'm pure done in after climbing Ben Nevis yesterday, my legs are absolutely shot to bits but the view from "
        "the top was worth every painful step up that mountain."
    ),
    (
        "He's always talking about moving down to London for work but I ken he'll never actually do it, his heart "
        "belongs here in Scotland and always will no matter what he says."
    ),
    # IRISH - SHORT
    "Ah sure, it'll be grand.",
    "Would ye ever stop!",
    "That's fierce cold today.",
    "He's away with the fairies.",
    "What's the craic?",
    "She's an awful eejit.",
    "That's gas altogether.",
    "I'm absolutely wrecked.",
    "Cop yourself on.",
    "He's acting the maggot.",
    "That's pure deadly.",
    "Will we have a go?",
    "Mind yourself now.",
    "I will yeah, sure.",
    "That's manky looking.",
    # IRISH - MEDIUM
    "Ah sure look, it could be worse, at least we've got our health and a roof over our heads.",
    "The weather's been absolutely shocking, haven't seen the sun in about three weeks now.",
    "He's been on the tear all weekend, arrived home looking like death warmed up yesterday.",
    "She's an absolute dote, always checking in on the neighbors and bringing round the biscuits.",
    "That match was absolutely brutal, we were robbed by that referee and everyone knows it.",
    "I'm absolutely scarlet after what happened, wanted the ground to swallow me up entirely.",
    "The session in the pub last night went on till all hours, the music was mighty craic.",
    "He hasn't got a notion what he's doing but sure he gives it a good go anyway bless him.",
    "I'm not made of money, do you think I have a money tree growing in the back garden or something?",
    "She's been giving out stink about the mess, reckons the place looks like a bomb hit it.",
    "That curry was absolutely gorgeous, best one I've had since I went to Dublin last month.",
    "The young fella's after failing his driving test again, that's the third time now sure.",
    "I'd murder a cup of tea right now, been gasping for one since about half nine this morning.",
    "He's full of himself since he got that promotion, walking around like he owns the place now.",
    "The kids are driving me up the wall, they've been cooped up inside all week with the rain.",
    # IRISH - LONG
    (
        "Ah sure, you know yourself how it is, one minute everything's grand and the next minute the whole thing's "
        "gone arseways, but that's life isn't it, you just have to roll with it."
    ),
    (
        "She's been doing ninety since she got up this morning, running around like a blue arsed fly trying to get "
        "everything done before the visitors arrive for dinner this evening."
    ),
    (
        "I haven't a bob to my name after Christmas, spent an absolute fortune on presents for everyone and now I'm "
        "eating beans on toast until payday comes around again next week."
    ),
    (
        "The craic was mighty at the wedding last weekend, everyone was up dancing till the early hours and the band "
        "was absolutely class, best night I've had in ages sure it was."
    ),
    (
        "He's a lovely fella once you get to know him, a bit quiet at first but sure aren't we all, and he's got a "
        "heart of gold underneath all that shyness when you see him open up."
    ),
]

"""Sports prompts: long soccer, hockey, and golf prompts, questions, and slang."""

from __future__ import annotations

JARGON: list[str] = [
    # LONG - SOCCER AUTHENTIC
    (
        "Tiki taka build up from the back, goalkeeper to center half to pivot to ten, quick one two on the edge of the "
        "box, through ball into the channel, first time finish into the far corner, proper team goal."
    ),
    (
        "Counter attack at pace after winning it in their half, three on two situation, played the overlapping "
        "fullback who whipped in a low cross, striker got across his man at the near post, and poked it home."
    ),
    (
        "Free kick from twenty five yards out, knuckleball technique made it wobble in the air, keeper took a step to "
        "his left but the ball dipped right, nestled into the bottom corner, unsavable really."
    ),
    (
        "Gegenpressing won the ball high up the pitch, quick transition before they could reset, one touch passing "
        "through the lines, number nine stayed onside by a toe, and slotted it past the onrushing keeper."
    ),
    (
        "Shithouse defending for the last ten minutes, bodies on the line, headers cleared at the back post, keeper "
        "making fingertip saves, held on for the clean sheet, and the celebrations were pure relief."
    ),
    # LONG - HOCKEY AUTHENTIC
    (
        "Power play unit cycling the puck down low, defenseman walking the line, one timer from the hashmarks went "
        "wide, but the winger crashed the net, jammed home the rebound in the crease, garbage goal but they all count."
    ),
    (
        "Breakout pass from behind the net sprung the forward on a two on one, patience to hold and let the trailer "
        "join the rush, drop pass at the top of the circles, one timer bar down, absolute snipe."
    ),
    (
        "Penalty kill was suffocating, blocked three shots in the same sequence, cleared the zone finally, sprung the "
        "speedy forward the other way, went backhand forehand and roofed it shortside, shorthanded dagger."
    ),
    (
        "Goalie standing on his head all night, robbing guys left and right, highlight reel glove save on the "
        "breakaway, post to post desperation stop, and the shootout win was entirely on his shoulders."
    ),
    (
        "Old time hockey fight at center ice after a questionable hit, gloves dropped and they went toe to toe, "
        "heavyweight tilt with haymakers flying, crowd was going absolutely nuts until the linesmen stepped in."
    ),
    # LONG - GOLF AUTHENTIC
    (
        "Standing over the par five eagle putt with the tournament on the line, read the subtle break left to right, "
        "committed to the speed, watched it track toward the hole, and when it disappeared into the cup the roar was "
        "deafening."
    ),
    (
        "Pulled driver on the reachable par four, absolutely striped it down the middle with a slight draw, landed in "
        "the fairway and released onto the front edge, left himself a twenty footer for albatross."
    ),
    (
        "Plugged lie in the greenside bunker with almost no green to work with, opened the face and took an aggressive "
        "swing, ball popped out soft with tons of spin, checked up and trickled to tap in range."
    ),
    (
        "Recovery shot from the pine straw, punched a low runner that scooted through the gap in the trees, kicked off "
        "the slope and fed down toward the green, somehow ended up inside ten feet, magician stuff."
    ),
    (
        "Sunday back nine with the lead, striped an iron off the tee on the par three, never left the flag, landed "
        "three feet behind and sucked back to gimme range, tap in birdie to extend the cushion."
    ),
    # LONG - OTHER SPORTS AUTHENTIC
    (
        "Slipped the jab, rolled under the follow up hook, countered with a left hook to the body that had him "
        "wincing, followed up with the straight right, and when he crumbled to the canvas the ref waved it off "
        "immediately."
    ),
    (
        "Sprinter exploded out of the blocks, transition phase was flawless, hit top speed at forty meters, maintained "
        "form through the finish line, dipped at the tape, and when the time flashed everyone knew it was a new record."
    ),
    (
        "Gymnast hit every rotation perfectly on the vault, Yurchenko with the full twist, stuck the landing with just "
        "a tiny hop backward, and when the score came up it was enough to clinch the all around title."
    ),
    (
        "Breakaway down the right wing, cut inside onto his stronger foot, curled it toward the top corner with the "
        "keeper beaten, but it rattled off the crossbar and the rebound fell kindly for the defender to clear."
    ),
    (
        "Wrestler shot in low for the double leg, opponent sprawled hard but couldn't get his hips back in time, got "
        "taken down and couldn't escape from bottom, gave up the riding time point that decided the match."
    ),
    # LONG QUESTIONS - AUTHENTIC
    (
        "Why do analytics guys keep telling teams to shoot threes and layups only when the mid range game still looks "
        "money against certain coverages?"
    ),
    (
        "How do front offices justify tanking for years when the draft lottery doesn't even guarantee you get the top "
        "pick anymore?"
    ),
    (
        "Is small ball really dead now that teams have figured out how to punish undersized lineups with post "
        "mismatches every possession?"
    ),
    (
        "Why do managers still bunt with their eight hitter when the expected run values clearly show swinging away is "
        "the better play?"
    ),
    (
        "How are pitchers throwing harder than ever but also getting hurt more often, doesn't that seem like the "
        "training methods are wrong?"
    ),
    (
        "Why does every young quarterback have to be a runner now when plenty of statues have won championships from "
        "the pocket?"
    ),
    (
        "How do you justify paying running backs when the position is so replaceable and the shelf life is only four "
        "or five years?"
    ),
    "Is the three true outcomes approach actually ruining baseball by making every at bat strikeout, walk, or homer?",
    (
        "Why do European clubs spend hundreds of millions on transfers when they could develop their own academy "
        "players for way less?"
    ),
    (
        "How do NHL teams still employ goons when fighting barely exists anymore and skill players are so much more "
        "valuable?"
    ),
    # ADDITIONAL SLANG & TERMS
    "Sauce me the rock, I'm feeling it tonight.",
    "Balled out on both ends, two way player stuff.",
    "Cooked him off the dribble, turned him around twice.",
    "Clamped him all game, locked in on the defensive assignment.",
    "Board man gets paid, crashed the glass all night.",
    "Garbage time minutes for the end of bench guys.",
    "DNP coach's decision for the veteran again.",
    "Load management for the star, sitting out back to backs.",
    "Mismatch hunting on every possession, targeting the weak link.",
    "Motion offense creating open looks, ball is popping.",
    "Iso ball taking over, hero mode activated.",
    "Blown coverage left the receiver wide open.",
    "Jumped the route for the easy pick.",
    "Holding flag came out late, bailed them out.",
    "Two minute drill execution was flawless.",
    "Ground and pound wearing down the defense.",
    "Air raid offense slinging it all over the yard.",
    "Philly special vibes on the trick play call.",
    "Squib kick gave them terrible field position.",
    "Touchback from the end zone, start at the twenty five.",
    "Walk year motivation hitting different.",
    "Arbitration case going ugly between player and team.",
    "Service time manipulation keeping him in the minors.",
    "Phantom tag on the stolen base attempt.",
    "Neighborhood play at second base was close.",
    "Balk call from first base ump was questionable.",
    "Infield fly rule confusion caused chaos.",
    "Checked swing appeal went to first base ump.",
    "Pine tar above the label, possible ejection.",
    "Sticky stuff crackdown changed everything for pitchers.",
    "Skipper got tossed arguing balls and strikes.",
    "Bench clearing brawl after the inside pitch.",
    "Unwritten rules nonsense ruining the game.",
    "Bat flip celebration triggered the other dugout.",
    "Shift ban has changed offensive approaches.",
    "Pitch clock violations killing the rhythm.",
    "Offside trap caught them three times in a row.",
    "Through ball splitting the center halves perfectly.",
    "Holding the line on the last defender.",
    "Time wasting in added time, proper dark arts.",
    "Tactical fouling breaking up the counter.",
    "Simulation earning him a yellow card.",
    "Crowding the ref after the controversial call.",
    "Extra man advantage in the attacking third.",
    "Diamond midfield giving them numerical superiority.",
    "False fullback inverting into the halfspace.",
    "Regista dictating tempo from deep.",
    "Trequartista floating between the lines.",
    "Sweeper keeper coming out to the edge of the box.",
    "Match fixing allegations rocking the league.",
    "Ultras section going absolutely mental.",
    # MORE AUTHENTIC SLANG & VOCAB
    "Putting the biscuit in the basket from the slot.",
    "Wheel snipe celly boys, dirty dangles all night.",
    "Top cheese from the faceoff dot, absolute rocket.",
    "Ferda boys, playing for the logo on the front.",
    "Pigeon riding shotgun on the top line all season.",
    "Grinder doing the dirty work along the boards.",
    "Tendy standing on his head, robbing everyone.",
    "Beauty apple on that tap in goal.",
    "Took a clapper right off the shin pads, warrior stuff.",
    "Lettuce flowing out the back of the bucket.",
    "Duster hasn't seen ice time in three weeks.",
    "Flow game is immaculate under that lid.",
    "Dropping mitts at center ice, old time hockey.",
    "Ring it around the boards and change on the fly.",
    "Cycling down low in the offensive zone.",
    "Point shot through traffic, screen worked perfectly.",
    "Shattered his stick on the one timer attempt.",
    "Pulling teeth trying to score on this goalie tonight.",
    "Cashing in the juicy rebound, right place right time.",
    "Headman the puck and stretch the ice.",
    "Chippy game after the whistle all night long.",
    "Launching bombs from the point, Shea Weber style.",
    "Absolutely undressed the defender with that dangle.",
    "Yard sale after that massive open ice hit.",
    "Sauce through three sticks, tape to tape.",
    "Bucket came flying off on the celly.",
    "Healthy scratch for the third straight game.",
    "Press box views for the underperforming veteran.",
    "Call up from the farm getting his shot tonight.",
    "Two way forward doing the dirty work both ends.",
    "Stay at home defenseman blocking shots all game.",
    "Puck moving blueliner quarterbacking the power play.",
    "Enforcer dropping the gloves to spark the team.",
    "Mucker digging pucks out of the corner.",
    "Cherry picker waiting at center for the outlet.",
    "Playing the body instead of chasing the puck.",
    "Finishing checks even when the puck is gone.",
    "Soft dump in and forecheck hard.",
    "Rim it around and get numbers back.",
    "Pinch at the blueline and keep it alive.",
    "Turning it over in the neutral zone again.",
    "Coughed it up at their own blueline, brutal.",
    "Zone entry on the rush was too predictable.",
    "Stretch pass sprung the winger on a breakaway.",
    "Backcheck harder or you're sitting next shift.",
    "Gassed after a long shift, couldn't make the change.",
    "Double minor for high sticking, four minutes to kill.",
    "Major and a game for boarding, ejected.",
    "Diving embellishment call, flopped like a fish.",
    "Matching roughing minors, four on four hockey.",
    "Goalie interference waved off the tying goal.",
    "Distinct kicking motion, no goal on review.",
    "High stick on the deflection, disallowed after challenge.",
    "Offside challenge overturned, goal stands after review.",
    "Skate in the crease negated the buzzer beater.",
    "Puck over glass delay of game, stupid penalty.",
    "Too many men on the ice, bench minor.",
    "Tripping from behind on the breakaway, penalty shot awarded.",
    "Slew foot behind the play, dirty move.",
    "Spearing in the pile, intent to injure.",
    "Game misconduct for abuse of officials.",
    "Cross check to the numbers, dangerous hit.",
    "Sucker punch after the whistle, ten and a game.",
    "Instigator penalty for starting the scrap.",
    "Third man in, automatic game misconduct.",
    "Spinning backfist connected clean, lights out.",
    "Rear naked choke sunk in deep, tapped immediately.",
    "Kimura from closed guard, textbook submission.",
    "Guillotine on the shot attempt, caught him coming in.",
    "Triangle choke from rubber guard, flexible hips.",
    "Arm bar from mount, nowhere to go.",
    "Leg kick compromised his mobility, couldn't move right.",
    "Checked the calf kick and broke his own leg.",
    "Ground and pound from half guard, elbows raining down.",
    "Clinch work against the cage, dirty boxing.",
    "Level change and double leg blast, perfect timing.",
    "Sprawl and brawl philosophy keeping it standing.",
    "Chain wrestling off the failed takedown attempt.",
    "Underhook battle in the clinch, jockeying for position.",
    "Hip escape back to the feet, scramble won.",
    "Cage walking back to standing, athletic freak.",
    "Toe hold from 50 50 guard, heel hook was there too.",
    "Imanari roll into the heel hook, sneaky entry.",
]

"""Sports prompts: short calls and reactions, slang, questions, and long basketball, football, and baseball prompts."""

from __future__ import annotations

CALLS: list[str] = [
    # ULTRA SHORT - REACTIONS & CALLS
    "Goal!",
    "Touchdown!",
    "Strike three!",
    "Foul ball!",
    "He scores!",
    "Offside!",
    "Penalty kick!",
    "Home run!",
    "Slam dunk!",
    "Hat trick!",
    "Grand slam!",
    "Birdie!",
    "Eagle!",
    "Bogey.",
    "Hole in one!",
    "Three pointer!",
    "Buzzer beater!",
    "Overtime!",
    "Sudden death!",
    "Photo finish!",
    "Personal best!",
    "World record!",
    "Knockout!",
    "Technical foul!",
    "Red card!",
    "Yellow card!",
    "Corner kick!",
    "Free throw!",
    "Interception!",
    "Fumble!",
    "Sack!",
    "Double fault!",
    "Match point!",
    "Game, set, match!",
    "Checkered flag!",
    "Pole position!",
    "Perfect ten!",
    "Triple axel!",
    "Bullseye!",
    # SHORT STATEMENTS
    "That crossover ankle breaker was absolutely filthy!",
    "Dropped back into the pocket and launched a fifty yard bomb.",
    "Sliced it into the rough on the eighteenth hole.",
    "Crushed that fastball right out of the park.",
    "Pulled off a between the legs dribble at full speed.",
    "Nailed the dismount with a stuck landing.",
    "Cleared the high jump bar on her third attempt.",
    "Sprinted through the tape in a new personal record.",
    "Dove into the end zone for the game winning score.",
    "Threaded the needle through traffic for the assist.",
    "Blasted a slap shot from the blue line.",
    "Executed a perfect pick and roll.",
    "Caught the alley oop and threw it down with authority.",
    "Chipped it onto the green from the bunker.",
    "Served an unreturnable ace down the T.",
    "Posted up in the paint and backed him down.",
    "Broke the pocket and scrambled for a first down.",
    "Launched a header off the corner kick.",
    "Threw a nasty curveball that froze the batter.",
    "Pulled guard and led the sweep around the edge.",
    # SHORT QUESTIONS
    "Did you see that no look pass through traffic?",
    "How did he get that much backspin on the approach shot?",
    "Was that pitch inside the strike zone or not?",
    "Who's starting at point guard tonight?",
    "Is the quarterback cleared from the concussion protocol yet?",
    "Why didn't the ref call that blatant holding penalty?",
    "Can anyone stop their fast break offense this season?",
    "What seed did they get in the tournament bracket?",
    "How many games behind first place are we now?",
    "Did the review overturn the call on the field?",
    "Is he playing through that hamstring injury tonight?",
    "Who's their closer coming out of the bullpen?",
    "What's the over under on this matchup?",
    "Did she qualify for the finals with that time?",
    "How many career triple doubles does he have now?",
    "Is that a two shot foul or are they in the bonus?",
    "Why is the manager pulling him in the seventh inning?",
    "Can they convert this fourth and one to extend the drive?",
    "What's his free throw percentage this season?",
    "Did the linebacker read that play action perfectly?",
    # MEDIUM STATEMENTS - VARIOUS SPORTS
    "Finessed that chip shot over the keeper and into the far post.",
    "Drilled a walk off grand slam to clinch the pennant race.",
    "Threw a devastating uppercut that ended the bout in the fourth round.",
    "Shattered the course record with a final round sixty two.",
    "Pulled off a textbook Fosbury Flop to clear two meters ten.",
    "Dominated the paint with twelve blocks and fifteen rebounds.",
    "Carved through the moguls with incredible edge control.",
    "Landed a clean roundhouse kick to score the deciding point.",
    "Ripped a forehand winner down the line on championship point.",
    "Juked three defenders on his way to the end zone.",
    "Sank a forty footer at the buzzer to force overtime.",
    "Executed a flawless parallel turn on the black diamond run.",
    "Caught the fly ball on the warning track to end the inning.",
    "Pedaled away from the peloton on the mountain stage.",
    "Powered through the final lap to take gold by a fingertip.",
    "Threw a devastating slider that buckled the cleanup hitter.",
    "Completed the Ironman triathlon in under ten hours.",
    "Stuck the landing on a double back tuck with a full twist.",
    "Fired a one timer past the sprawling goaltender.",
    "Cleared the pommel horse rotation without a single deduction.",
    "Unleashed a wicked knuckleball that danced across the plate.",
    "Charged the net and put away the overhead smash.",
    "Muscled through the scrum to secure possession.",
    "Launched a halfpipe run with back to back 1080s.",
    "Picked apart the zone defense with crisp ball movement.",
    "Rolled a perfect game with twelve consecutive strikes.",
    "Stroked a pure lag putt to within gimme range.",
    "Anchored the relay team to a new national record.",
    "Whipped a sidearm throw to nail the runner at home.",
    "Stuck a triple toe loop combination in the short program.",
    # MEDIUM QUESTIONS
    "Why does every pitcher seem to struggle against left handed batters?",
    "How do you defend against a team that shoots forty percent from three?",
    "What adjustments did the coaching staff make at halftime?",
    "Is the two minute warning going to give them enough time to score?",
    "Why didn't they challenge that obvious pass interference call?",
    "How is he still running routes after that vicious hit?",
    "What's the strategy behind icing the kicker before a field goal?",
    "Did the trainer clear her to return after tweaking her ankle?",
    "Why do they keep going to the same play on third and long?",
    "How many penalty minutes has he racked up this season?",
    "Is that a legal formation with the tight end lined up there?",
    "What's preventing them from establishing the ground game?",
    "Did the committee snub them from the playoff rankings?",
    "How do you practice recovering from a bad snap?",
    "Why is the pitch count so important for young arms?",
    "What makes his jab so effective at controlling distance?",
    "Is the hydration strategy different for marathon runners?",
    "How did the caddy read that break so perfectly?",
    "Why do goalies come so far off their line on corner kicks?",
    "What's the advantage of the neutral zone trap in hockey?",
    # SHORT - HOCKEY SLANG
    "Beauty snipe, went bardownski on that wrister.",
    "Greasy goal in the crease, garbage man special.",
    "Dangled through three guys, silky mitts.",
    "Celly was absolutely electric, bench went nuts.",
    "Bender on skates, couldn't keep his edges.",
    "Kronwalled at center ice, absolutely trucked.",
    "Turtled after the hit, wouldn't answer the bell.",
    "Chirping from the bench all night, getting under his skin.",
    "Gordie Howe hatty, goal, apple, and a scrap.",
    "Sauced it through traffic, tape to tape beauty.",
    "Clapped it from the point, bomb from the blueline.",
    "Five hole was wide open, went blocker side instead.",
    "Flashed the leather, robbed him with the glove.",
    "Stoned on the breakaway, brick wall performance.",
    "Garbage time goal to pad the stats, empty netter.",
    "Shorthanded breakaway the other way, killed the momentum.",
    "Tic tac toe passing, one timer buried.",
    "Wraparound attempt stuffed, tried to jam it home.",
    "Delayed penalty gave them the extra attacker.",
    "Pulled the goalie with two minutes left, empty net time.",
    # SHORT - GOLF SLANG
    "Nuked his driver, absolute piss missile off the tee.",
    "Stiffed the approach, spun it back to gimme range.",
    "Hosel rocket into the trees, shanked it bad.",
    "Thinned his wedge, bladed it over the green.",
    "Fat chunk, took a divot before the ball.",
    "Pure strike, flush contact on that iron.",
    "Butter cut around the dogleg, worked it perfectly.",
    "Stinger under the wind, kept it low and running.",
    "Flop shot over the bunker, Phil Mickelson style.",
    "Lag putt died in the jaws, horseshoed out.",
    "Buried the snake for birdie, drained the twenty footer.",
    "Came up short in the drink, found the water.",
    "Plugged in the bunker, fried egg lie.",
    "Lip out on the low side, misread the break.",
    "Double cross into the hazard, opposite miss.",
    "Bombed it past the fairway, driver went too far.",
    "Green in regulation but three jacked it, yips are real.",
    "Saved par from the cabbage, escaped the thick rough.",
    "Sunday pin position, tucked behind the bunker.",
    "Calcutta action on the first tee, money games.",
    # SHORT - TENNIS SLANG
    "Bageled him in the first set, six love demolition.",
    "Breadstick second set, only let him win one game.",
    "Moon ball tactics working, frustrating the power player.",
    "Inside out forehand winner, painted the line.",
    "Drop shot passing shot combo, deadly touch.",
    "Serve and volley on clay, old school tactics.",
    "Net cord luck on break point, lucky dribbler.",
    "Unforced errors piling up, gifting points away.",
    "Double fault on match point, nightmare scenario.",
    "Tweener lob from the baseline, ridiculous athleticism.",
    # SHORT - BOXING/MMA SLANG
    "Flash knockdown, more of a slip than a punch.",
    "Caught him with a check hook on the way in.",
    "Body shot folded him, liver punch does it again.",
    "Rabbit punches behind the head, dirty fighter.",
    "Clinching to survive, holding on for dear life.",
    "Corner should throw in the towel, he's done.",
    "Slipping punches like the Matrix, untouchable.",
    "Pitter patter combinations, volume over power.",
    "Phone booth fighting, both guys exchanging leather.",
    "Wrestle heavy gameplan, laying and praying.",
    # MEDIUM QUESTIONS - AUTHENTIC
    "Why do teams ice the kicker when there's no evidence it actually works?",
    "Is the prevent defense really just preventing you from winning?",
    "How does the shift affect lefty pull hitters differently than spray guys?",
    "Why do closers only pitch one inning when starters can go seven?",
    "Does load management actually prevent injuries or just rest guys?",
    "Why is the neutral zone trap so boring but so effective?",
    "How do you defend the pick and pop when the big man can shoot?",
    "Should teams go for it on fourth down more than analytics suggest?",
    "Why do goalies come so far off their line on corners?",
    "Is the designated hitter ruining the National League experience?",
    "How does the salary cap actually create parity in the league?",
    "Why are two way players so rare if they're so valuable?",
    "Does home field advantage still matter as much as it used to?",
    "Why do lefty specialists only face one batter before getting pulled?",
    "How do pitchers tip their pitches without realizing it?",
    "What's the point of the trapezoid behind the net in hockey?",
    "Why does icing exist and who thought it was a good rule?",
    "How do teams prepare for the altitude in Denver and Mexico City?",
    "Why do European leagues use promotion and relegation but American ones don't?",
    "Is tanking actually a viable strategy for rebuilding franchises?",
    # MEDIUM - EMOTIONAL AUTHENTIC
    "Absolutely mugged him in the box and the ref swallowed his whistle.",
    "That's ball don't lie, missed the free throw after the bad call.",
    "Flop of the century, should win an Oscar for that performance.",
    "Ref ball all game, we're playing against the stripes tonight.",
    "How is that not a penalty? Are we watching the same game?",
    "He's washed, needs to hang it up before he embarrasses himself.",
    "Bum contract, overpaid and underperforming for three straight years.",
    "Stat padder out there chasing his own numbers instead of wins.",
    "Empty calories, putting up numbers on a losing team means nothing.",
    "Winning plays don't show up in the box score.",
    "Culture guy, brings the energy even when he's not producing.",
    "Dawg mentality on the court, refuses to lose.",
    "That man got a bag and decided to coast, collecting checks.",
    "Playoff mode activated, completely different player in the postseason.",
    "Big game hunter, shows up when the lights are brightest.",
    "Choke artist, shrinks when the pressure is on.",
    "Bubble fraud, only performed in the empty arena.",
    "Mickey Mouse ring, that championship shouldn't count.",
    "Dynasty over, father time is undefeated.",
    "Generational talent, once in a lifetime type player.",
    # LONG - BASKETBALL AUTHENTIC
    (
        "Came off the pin down, caught it in his shooting pocket, rose up with the defender draped all over him, got "
        "the and one call, and hit the free throw to complete the four point play that swung the momentum completely."
    ),
    (
        "Point god running the show, dropped the pocket pass to the rolling big, who finished with the reverse slam "
        "through contact, and the whole arena absolutely erupted when he flexed on the defender afterwards."
    ),
    (
        "Jab step right, crossover left, between the legs hesitation, step back three from the wing with the shot "
        "clock winding down, nothing but net, and then he hit them with the shimmy celebration."
    ),
    (
        "Screen the screener action freed him on the baseline, curl was wide open, caught the dime in rhythm, pulled "
        "up from the mid range, and splashed it with that patented elbow jumper he's been drilling since high school."
    ),
    (
        "Full court pressure couldn't stop him, split the trap at half court, euro stepped through the help defender, "
        "finished with the left hand off glass, and got the foul call to boot, absolutely unstoppable."
    ),
    # LONG - FOOTBALL AUTHENTIC
    (
        "Pre snap motion revealed man coverage, QB checked into the go route, protection held up against the four man "
        "rush, threw a dime to the back pylon, receiver toe tapped in bounds, and the replay confirmed the touchdown."
    ),
    (
        "Play action fake held the linebackers just long enough, tight end leaked out into the flat uncovered, caught "
        "the checkdown with acres of space, rumbled for fifteen yards after the catch, and moved the sticks on third "
        "and long."
    ),
    (
        "Zone read option went to the tailback, bounced it outside when the hole closed, tight roped the sideline for "
        "an extra five yards, got shoved out at the one, and they punched it in on the next play."
    ),
    (
        "Shotgun formation, five wide empty set, quick slant to the slot receiver, broke one tackle at the catch "
        "point, turned upfield with his speed, and housed it for a seventy five yard walk off score."
    ),
    (
        "Fourth and inches in enemy territory, coach had the stones to go for it, quarterback sneak behind the center "
        "and guards combo block, crossed the plane by a nose, and the refs signaled first down after the measure."
    ),
    # LONG - BASEBALL AUTHENTIC
    (
        "Full count two outs bases juiced, batter fouled off five straight pitches to stay alive, worked the walk on a "
        "borderline pitch, forced in the tying run, and the dugout went absolutely ballistic with the winning run at "
        "third."
    ),
    (
        "Pitcher shook off three signs before getting what he wanted, went into the windup, uncorked a twelve to six "
        "yakker that fell off the table, batter waved at it helplessly, and the strikeout ended the threat."
    ),
    (
        "Absolutely barreled the hanging slider, launch angle was perfect, exit velo off the charts, ball cleared the "
        "bullpen in left center, pimped the bat flip, and admired his work before jogging the bases."
    ),
    (
        "Infield in with the tying run on third less than two out, grounder to short, throw home was bang bang, "
        "catcher blocked the plate, runner came in hard, and the ump punched him out to end the game."
    ),
    (
        "Two seamers running arm side all night, hitters couldn't square anything up, painted the black at will, went "
        "seven innings of one run ball, quality start turned into a masterpiece, and the bullpen closed it out."
    ),
]

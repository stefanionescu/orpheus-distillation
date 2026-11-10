"""Sports prompts about cricket, rugby, volleyball, swimming, athletics, gymnastics, skating, skiing, and cycling."""

from __future__ import annotations

DISCIPLINES: list[str] = [
    # CRICKET
    (
        "Edged it to first slip off the away swinger, nicked off for a duck on the first ball of the innings, golden "
        "duck in a crucial match situation."
    ),
    (
        "Reverse swept the spinner over the infield for a boundary, paddle sweep execution was immaculate, rotating "
        "the strike beautifully in the middle overs."
    ),
    (
        "Yorker right in the blockhole, toe crusher cleaned up the stumps, death bowling masterclass from the quick "
        "with that unplayable delivery."
    ),
    (
        "Googly deceived the batsman completely, wrong footed on the crease, bowled through the gate between bat and "
        "pad for a crucial breakthrough."
    ),
    (
        "Doosra turned the other way and took the outside edge, keeper took a sharp catch diving to his left, leg "
        "spinner creating havoc."
    ),
    (
        "Slogged it over cow corner for a massive six, agricultural shot but effective, clearing the ropes in the "
        "powerplay for momentum."
    ),
    (
        "Knuckle ball slower delivery completely fooled the batsman, through the shot too early, top edged the pull "
        "and caught at fine leg."
    ),
    (
        "Pulling the short ball from outside off stump, hooked it into the stands over deep backward square, fearless "
        "batting against the pace attack."
    ),
    (
        "Night watchman surviving the final session, dead bat defense on everything, blocking out for the draw in the "
        "test match."
    ),
    (
        "Mankad dismissal causing controversy, backing up too far at the non striker's end, within the laws but still "
        "debated endlessly."
    ),
    (
        "LBW shout turned down on field, DRS review taken and ball tracking showed three reds, hitting leg stump, "
        "decision overturned and out."
    ),
    (
        "Cover driven through the gap for four runs, timing was exquisite, classical stroke play from the number three "
        "batsman this morning."
    ),
    (
        "Bouncer followed by the full delivery, set him up perfectly with the short ball then got him driving at one "
        "that wasn't there."
    ),
    (
        "Batting collapse in the final session, lost five wickets in thirty deliveries, capitulation under pressure "
        "that cost them the match."
    ),
    (
        "Power play field restrictions exploited, boundary rope brought in, smashing it through the vacant cover "
        "region repeatedly for easy runs."
    ),
    # RUGBY
    (
        "Crash ball through the midfield channel, straightened the defensive line, offload in the tackle kept the "
        "continuity going for the try."
    ),
    (
        "Grubber kick into the in goal area, chased it down and grounded it before the dead ball line, perfectly "
        "weighted kick."
    ),
    (
        "Scrum collapsed on the loosehead side, reset ordered by the referee, front row battle going badly for the "
        "visiting pack."
    ),
    (
        "Maul set up off the lineout, drove it fifteen meters before the try line, unstoppable forward momentum from "
        "the pack."
    ),
    (
        "Chip and chase over the top of the rush defense, regathered his own kick and scored in the corner, brilliant "
        "individual effort."
    ),
    (
        "Garryowen bomb from the fullback, chasers applied pressure, opposition spilled the high ball under the aerial "
        "challenge."
    ),
    (
        "Jackal at the breakdown, got hands on the ball, penalty won for not releasing, crucial turnover inside their "
        "own twenty two."
    ),
    (
        "Pop pass to the blindside flanker, short linebreak through the tight channel, support runners recycled "
        "quickly for the next phase."
    ),
    (
        "Cross field kick to the winger, perfectly weighted, one on one with the fullback, stepped inside and dotted "
        "down under the posts."
    ),
    (
        "Yellow card for repeated infringements, cynical penalties at the ruck, ten minutes in the sin bin at a "
        "crucial time."
    ),
    (
        "Conversion from the touchline, swirling wind making it tricky, nailed the difficult kick to extend the lead "
        "to seven points."
    ),
    (
        "Breakdown penalty for sealing off, bodies everywhere at the ruck, referee pinged them for preventing access "
        "to the ball."
    ),
    "Dummy switch fooled the defense, sliced through the gap, inside pass to the supporting lock for a forward's try.",
    (
        "High tackle resulting in a red card, shoulder contact to the head, no mitigation available, team down to "
        "fourteen men."
    ),
    (
        "Up and under from the restart, contestable kick, won the aerial battle, immediate pressure back on the "
        "receiving team."
    ),
    # VOLLEYBALL
    "Pipe attack from the back row, quick tempo set to the middle back, hammered it through the block for a kill.",
    (
        "Pancake dig on the hard driven spike, kept the ball alive with one hand flat on the floor, incredible "
        "defensive effort."
    ),
    (
        "Setter dump on two, tipped it over the block when they weren't expecting it, smart play caught the defense "
        "sleeping."
    ),
    (
        "Float serve aced them down the sideline, no spin made it wobble unpredictably, three aces in a row from the "
        "service line."
    ),
    (
        "Slide attack behind the setter, quick set to the opposite, one on one with the middle blocker, tooled the "
        "block for the point."
    ),
    (
        "Block touch off the antenna, ball went out, point to the attacking team, roof job attempt went wrong for the "
        "blocker."
    ),
    (
        "Roll shot over the block, soft touch change of pace, defense wasn't ready for anything off speed after all "
        "the swings."
    ),
    (
        "Double contact called on the setter, hands weren't clean on the overhead pass, side out awarded to the other "
        "team."
    ),
    (
        "Libero subbing in for the middle back, serve receive specialist taking the court, looking to stabilize the "
        "passing."
    ),
    (
        "Joust at the net, both players contacted simultaneously, ball fell on their side, our point on the fifty "
        "fifty play."
    ),
    "Cut shot angle kill, sharp cross court attack, extreme angle that the defense had no chance of reaching in time.",
    (
        "Five one rotation, setter running the show, six attackers available with the libero stabilizing the back row "
        "defense."
    ),
    "Service error into the net, easy point given away, momentum killer right when they were making a comeback run.",
    (
        "Back row attack from position one, outside hitter taking off behind the three meter line, absolute bomb "
        "straight down."
    ),
    "Overpass opportunity, setter in trouble, free ball turned into a swinging approach, easy kill on the broken play.",
    # SWIMMING
    (
        "Negative split on the back half, went out conservative and brought it home faster, textbook distance racing "
        "strategy."
    ),
    (
        "Underwater dolphin kicks off the wall, stayed submerged for the legal fifteen meters, breakout into stroke "
        "with momentum."
    ),
    (
        "Flip turn executed perfectly, somersault and push off in one fluid motion, streamlined off the wall to "
        "maintain speed."
    ),
    (
        "False start DQ in the final, jumped the gun by a hundredth, devastating end to years of preparation for this "
        "moment."
    ),
    (
        "Touch pad controversy, both swimmers thought they won, photo finish review showed a hundredth of a second "
        "difference."
    ),
    "IM transition from fly to back, smooth rollover at the wall, picked up speed on the backstroke leg of the medley.",
    "Relay exchange was legal, takeover verified by the touchpad timing, anchor leg went out with a slight advantage.",
    "Stroke judge raised the flag, possible dolphin kick on the breaststroke turn, DQ under review by the referee.",
    (
        "Pulled away on the third fifty, opened up a body length lead, nobody could match the closing speed on the "
        "freestyle."
    ),
    (
        "Lane line splash going into the finish, turbulence from the swimmer in the next lane, still got hand on the "
        "wall first."
    ),
    (
        "Split time at the hundred was blazing, world record pace through the first half, question is whether it's "
        "sustainable."
    ),
    (
        "Tech suit controversy before the meet, legal fabric composition verified, approved for competition after "
        "inspection."
    ),
    (
        "Breathing pattern shifted in the final fifty, every two strokes instead of three, oxygen debt catching up "
        "quickly."
    ),
    (
        "Block start reaction time was elite, coiled spring explosion off the platform, first to enter the water by a "
        "margin."
    ),
    "Open water navigation error, swam extra distance around the buoy, cost valuable seconds in the pack finish.",
    # TRACK & FIELD
    "Staggered start on the two hundred meters, running in lane eight, needs to catch the field on the turn.",
    "Photo finish in the sprint, dip at the line, torso across first determines the winner, leaning technique matters.",
    "False start sensor triggered, red card shown, one strike rule means immediate disqualification from the race.",
    "Rabbit set the pace through six hundred meters, pulled off as planned, allowed the kickers to battle it out.",
    "Steeplechase water jump technique, hurdle clearance before the pit, splashing through and maintaining rhythm.",
    "Exchange zone violation on the relay, baton passed outside the legal area, disqualification for the entire team.",
    "Fosbury flop clearance at two meters, arched back over the bar, landed safely in the pit for a new personal best.",
    "Foul throw in the shot put, toe over the circle edge, red flag raised, attempt doesn't count in the series.",
    "Wind legal for the sprint, plus one point nine meters per second, time will count for records and rankings.",
    "Pole plant was late, couldn't get inverted properly, brushed the bar off on the way down, failed attempt.",
    "Heptathlon points leader going into the eight hundred, just needs to finish within range to secure gold overall.",
    "Kick came too late on the final lap, left too much in the tank, got out leaned at the tape by three spots.",
    "Lane infringement on the curve, stepped on the inside line, video review confirmed, moved to last place.",
    "Sector foul in the javelin, throw traveled eighty meters but landed outside the legal zone, no mark recorded.",
    "Marathon wall at mile twenty, glycogen depleted, shuffle step survival mode just to reach the finish line.",
    # GYMNASTICS
    "Tkachev release on the high bar, catch and swing through, connected immediately into a pak salto for difficulty.",
    "Amanar vault attempt, two and a half twisting Yurchenko, slight hop on the landing deducted from the score.",
    "Switch leap series on the beam, connected elements for bonus, stayed on despite a slight balance check.",
    "Manna hold on the parallel bars, strength element maintained for three seconds, judges confirmed the hold.",
    "Tour jete half turn, dance element executed with artistry, deductions come from leg separation issues.",
    "Stuck the landing cold, no movement whatsoever, arms raised for the judges, crowd went absolutely insane.",
    "Inquiry filed on the difficulty score, coach thinks they missed a connection, judges reviewing the video now.",
    "Front aerial walkover on the beam, no hand touch required, execution deduction for insufficient split.",
    "Triple back dismount from the high bar, huge amplitude on the release, full rotation with controlled landing.",
    "Kip cast to handstand, basic element but flawless technique, shoulders past vertical without any arch.",
    "Back tuck stepout into immediate punch front, tumbling pass connected beautifully, big difficulty value.",
    "Bail to handstand on the uneven bars, release move between the rails, caught the low bar perfectly.",
    "Giant swing with one arm, technique showcase on the high bar, strength and control on full display.",
    "Sheep jump on the balance beam, backward leap with feet touching head, flexibility element executed cleanly.",
    "Yurchenko entry off the vault table, roundoff back handspring onto the apparatus, standard technique.",
    # FIGURE SKATING
    "Triple axel attempt, forward outside edge takeoff, three and a half rotations, under rotated by a quarter turn.",
    "Sit spin variation, pancake position with leg extended, level four features including difficult variation.",
    "Death spiral in the pairs program, inside edge backward spiral, head nearly touching the ice, terrifying beauty.",
    "Quad salchow landed clean, back inside edge takeoff, four rotations with solid landing on the outside edge.",
    "Step sequence traveling the full length of the ice, intricate footwork hitting the music, level four difficulty.",
    "Throw quad loop attempt, pairs element with massive amplitude, partner landed slightly two footed on the exit.",
    "Flying camel spin entry, jump into the camel position, rotational speed increased through the element.",
    "Biellmann spin pulling the free leg overhead, flexibility required is insane, centered perfectly throughout.",
    "Triple lutz triple toe combination, connected without a turn, second element credit fully awarded.",
    "Choreographic sequence in the free skate, interpretive movement expressing the music, program component scores.",
    "Edge call on the flip, inside edge instead of outside, wrong edge deduction applied to the base value.",
    "Lift rotation traveling the full ice surface, pairs element sustained for the required time, difficult exit.",
    "Spread eagle transition, inside edges gliding, connecting elements with artistry and flow between jumps.",
    "Pattern dance element, required steps and turns, key points evaluated for edge quality and timing.",
    "Layback spin with haircutter variation, catch foot position, difficult feature counted for level requirements.",
    # SKIING & SNOWBOARDING
    "Double cork 1440 landed clean, two off axis flips with four rotations, huge amplitude off the jump.",
    "Carving turns on the race course, angulation at extreme angles, knee almost touching the snow on the apex.",
    "Straddled the gate on the giant slalom, missed the panel, DNF in the second run after a solid first.",
    "Tucked through the flats, aerodynamic position, gliding efficiently between the technical sections of the course.",
    "Backside rodeo off the kicker, inverted rotation with style, grabbed the board throughout for extra points.",
    "Edge hold on the icy course, fighting for grip on the hardpack, equipment tuning critical for conditions.",
    "Yard sale crash at high speed, skis and poles scattered everywhere, equipment ejected in all directions.",
    "Method grab with bone out extension, stylish execution on the hip hit, tweaked for maximum steez.",
    "Split time at the interval, fastest in the field, maintaining tuck position through the speed section.",
    "Butter tricks on the flat, pressing the nose and tail, jibbing without any features just on the groomers.",
    "Sluff management on the steep face, outrunning the debris, staying ahead of the snow sliding behind.",
    "Switch stance landing, riding fakie after the rotation, comfortable both ways for competitive versatility.",
    "Gates rattling on the way through, aggressive line brushing every panel, attacking the fall line directly.",
    "Powder turn spray, deep snow face shot, untracked lines through the trees, blower conditions today.",
    "Halfpipe amplitude measured from the lip, height out of the transition, bigger air means bigger tricks.",
    # CYCLING
    "Attacked on the final climb, dancing on the pedals out of the saddle, gap opened up on the peloton.",
    "Leadout train perfectly executed, positioning the sprinter at two hundred meters to go, textbook teamwork.",
    "Dropped on the cobbles, couldn't hold the wheel, gap opened and never closed, race over for the contender.",
    "Echelons formed in the crosswinds, gutter riding required, half the peloton caught behind the split.",
    "Puncture at the worst possible moment, quick wheel change from the team car, chasing back through traffic.",
    "Sitting on wheels all day, saving energy in the slipstream, fresh legs for the final sprint.",
    "Burned all his matches on the early attacks, nothing left in the tank for the steep finishing ramp.",
    "Time trial specialist, individual effort against the clock, aerodynamic equipment and pacing perfection.",
    "Gruppetto forming on the mountain stage, survival mode for the sprinters, just making the time cut.",
    "Chain dropped on the gear change, mechanical issue at a critical moment, soft pedaling to get it back on.",
    "Aero tuck on the descent, nose on the stem, hitting seventy miles per hour on the mountain road.",
    (
        "Intermediate sprint points contested, green jersey battle heating up, points classification coming down to "
        "details."
    ),
    "Bonked on the final climb, glycogen depleted, the hunger knock hitting hard at the worst possible time.",
    "Drafting behind the motorcycle, illegal assistance allegation, race jury reviewing the footage now.",
    "Polka dot jersey on the line, king of the mountains classification, climbing points at every categorized summit.",
]

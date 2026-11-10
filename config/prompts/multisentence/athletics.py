"""Multi-sentence prompts: natural talk about sports, shopping, relationships, and work."""

from __future__ import annotations

ATHLETICS: list[str] = [
    # SPORTS & FITNESS - NATURAL
    (
        "The marathon training plan gradually increases weekly mileage. The long runs on weekends are mentally "
        "challenging but necessary."
    ),
    (
        "Her tennis serve has become much more consistent lately. The coach adjusted her toss and the improvement was "
        "immediate."
    ),
    (
        "The climbing gym recently installed new bouldering routes. Several of them are rated well above my current "
        "skill level."
    ),
    "Our rowing team practices on the river before dawn daily. The water is calmest during those early morning hours.",
    (
        "The personal trainer designed a program targeting my weaknesses. Unilateral exercises have helped correct my "
        "muscle imbalances."
    ),
    (
        "His golf handicap has dropped five strokes this season. The new swing mechanics finally clicked after months "
        "of practice."
    ),
    (
        "The yoga instructor emphasizes proper alignment over flexibility. She'd rather we use blocks than compromise "
        "our form."
    ),
    (
        "Our cycling group rides sixty miles every Saturday morning. The camaraderie makes the challenging routes more "
        "enjoyable."
    ),
    (
        "The recovery period between weight training sessions is crucial. Muscles actually grow during rest, not "
        "during the workout itself."
    ),
    (
        "Her swimming technique was analyzed using underwater cameras. The footage revealed inefficiencies in her "
        "stroke mechanics."
    ),
    (
        "The crossfit competition tested endurance, strength, and agility. Athletes had to complete seven different "
        "events over two days."
    ),
    "My running shoes have over four hundred miles on them. The cushioning has degraded and I'm risking injury now.",
    (
        "The basketball court's hardwood floor was recently refinished. The improved grip has noticeably reduced slip "
        "related injuries."
    ),
    (
        "Our soccer league plays year round on artificial turf fields. The surface is more forgiving than natural "
        "grass in some ways."
    ),
    (
        "The physiotherapy exercises strengthen the muscles around my knee. Building that stability prevents future "
        "ligament injuries."
    ),
    (
        "His powerlifting total has increased by fifty kilograms this year. The periodized training program has been "
        "incredibly effective."
    ),
    (
        "The triathlon transitions require as much practice as the events. Efficiently switching between swim, bike, "
        "and run saves minutes."
    ),
    (
        "Our hiking group tackled a peak with significant elevation gain. The thin air at altitude made the final push "
        "exhausting."
    ),
    (
        "The fencing club meets three times weekly for practice sessions. Footwork drills are surprisingly demanding "
        "on the legs."
    ),
    (
        "My interval training alternates between high intensity and recovery periods. The approach has significantly "
        "improved my cardiovascular fitness."
    ),
    # SHOPPING & RETAIL - NATURAL
    "The clearance section had some incredible finds today. I scored designer jeans for less than twenty dollars.",
    "This boutique sources all their inventory from local artisans. The craftsmanship is exceptional on every piece.",
    "The return policy requires the original receipt and tags attached. I hope I kept everything from that purchase.",
    (
        "Their customer service representative was incredibly helpful and patient. She tracked down the item at "
        "another location."
    ),
    (
        "The fitting rooms have great lighting which is honestly rare. Most stores seem designed to make you look "
        "terrible."
    ),
    "I've been on the waitlist for that handbag for six months. They only produce a limited quantity each year.",
    "The vintage shop has an amazing selection of mid century furniture. The prices are reasonable for the quality.",
    "Our loyalty program points finally added up to a free item. The rewards accumulate faster than I expected.",
    (
        "The farmers market vendor remembers our usual order every week. The fresh produce quality is consistently "
        "excellent."
    ),
    (
        "That online retailer's size chart was completely inaccurate unfortunately. Everything I ordered needs to be "
        "exchanged."
    ),
    "The holiday shopping rush was absolutely chaotic this year. Next time I'm definitely ordering everything online.",
    (
        "Their price matching policy saved me almost fifty dollars today. I just showed them the competitor's "
        "advertisement."
    ),
    "The cashier applied a coupon I didn't even know existed. It was a pleasant surprise at checkout.",
    "This consignment shop only accepts items in excellent condition. Their curation standards keep the quality high.",
    "The checkout line wrapped around the entire store yesterday. I abandoned my cart and left empty handed.",
    "Their subscription box includes samples customized to my preferences. It's a great way to discover new products.",
    "The warranty covers repairs for up to five years. Considering the price, that guarantee was worth it.",
    "I prefer shopping during weekday mornings when it's quieter. The staff has more time to assist with questions.",
    "The pop up shop is only open through the end of the month. Their unique merchandise won't be available elsewhere.",
    (
        "That antique dealer has an encyclopedic knowledge of porcelain. He authenticated the piece immediately upon "
        "inspection."
    ),
    # RELATIONSHIPS & SOCIAL - NATURAL
    "We've been friends for over twenty years now. She knows me better than I know myself sometimes.",
    "The conversation flowed naturally without any awkward silences. We talked for hours without noticing the time.",
    "My neighbor always brings over extra vegetables from her garden. The community here is genuinely welcoming.",
    (
        "We're trying to maintain the long distance friendship with regular calls. The time zone difference makes "
        "scheduling difficult."
    ),
    "His apology seemed sincere but actions speak louder than words. I need to see consistent change over time.",
    (
        "The dinner party brought together people from different social circles. The conversations were surprisingly "
        "engaging and diverse."
    ),
    "She has this gift for making everyone feel included and valued. Her emotional intelligence is truly remarkable.",
    (
        "Our book club has become more about friendship than literature. The discussions always meander into personal "
        "stories."
    ),
    "I reconnected with my college roommate after fifteen years apart. We picked up right where we left off.",
    "The miscommunication caused unnecessary tension between us for weeks. We should have talked it out much sooner.",
    "His loyalty during my difficult times meant everything to me. True friends reveal themselves during hardship.",
    "We agreed to disagree on politics and preserve our friendship. Some topics are better left unexplored together.",
    (
        "The grief support group connected me with others who understand. Shared experiences create profound bonds "
        "between strangers."
    ),
    (
        "Her networking skills have opened doors I never knew existed. She genuinely enjoys connecting people with "
        "opportunities."
    ),
    (
        "Our weekly coffee dates have become sacred and non negotiable. That consistent time together strengthens our "
        "bond."
    ),
    (
        "The intervention was difficult but came from a place of love. Sometimes caring means having uncomfortable "
        "conversations."
    ),
    "My mentor's guidance shaped my career trajectory significantly. Her advice was always practical and thoughtful.",
    "We established healthy boundaries to improve our relationship. The dynamic has improved dramatically since then.",
    (
        "The surprise party planning required coordinating with so many people. Keeping the secret was surprisingly "
        "challenging."
    ),
    "Their wedding vows were personal and deeply moving. You could feel the authenticity in every word spoken.",
    # WORK & CAREER - NATURAL
    (
        "The performance review highlighted areas for professional development. My manager provided actionable "
        "feedback and clear goals."
    ),
    (
        "Our team's quarterly objectives were ambitious but achievable. Cross functional collaboration was essential "
        "for success."
    ),
    (
        "The job interview process included three rounds and a presentation. The rigorous evaluation shows they're "
        "selective about hiring."
    ),
    (
        "My mentor recommended pursuing certification in project management. The credential should open up advancement "
        "opportunities."
    ),
    (
        "The company's parental leave policy is exceptionally generous. They genuinely support work life balance for "
        "employees."
    ),
    (
        "Our department's budget was unfortunately reduced this fiscal year. We need to prioritize initiatives more "
        "carefully now."
    ),
    (
        "The promotion came with significant additional responsibilities. The salary increase barely compensates for "
        "the workload."
    ),
    (
        "Remote work has fundamentally changed how our team collaborates. Asynchronous communication requires more "
        "intentional effort."
    ),
    (
        "The networking event connected me with potential industry contacts. Several promising conversations may lead "
        "somewhere valuable."
    ),
    (
        "Our annual retreat focuses on team building and strategic planning. The off site location encourages creative "
        "thinking."
    ),
    (
        "The layoffs affected nearly fifteen percent of the workforce. Morale has understandably been quite low since "
        "then."
    ),
    (
        "Her negotiation skills secured better contract terms for everyone. She advocated strongly on behalf of the "
        "entire team."
    ),
    (
        "The onboarding process for new hires takes approximately three weeks. Thorough training reduces mistakes and "
        "confusion later."
    ),
    (
        "My sabbatical allowed time for reflection and skill development. I returned with renewed energy and fresh "
        "perspectives."
    ),
    (
        "The company culture emphasizes continuous learning and innovation. They actually invest in employee "
        "professional growth."
    ),
    (
        "Our stakeholder meeting clarified priorities and resolved conflicting demands. Alignment across departments "
        "is finally improving."
    ),
    (
        "The exit interview provided an opportunity for honest feedback. Hopefully the organization learns from "
        "departing employees."
    ),
    (
        "His presentation to the board was concise and well received. The data visualization made complex information "
        "accessible."
    ),
    (
        "The freelance arrangement offers flexibility but lacks stability. Finding consistent clients requires "
        "constant networking effort."
    ),
    (
        "Our workflow automation reduced manual data entry significantly. The efficiency gains freed time for more "
        "strategic work."
    ),
]

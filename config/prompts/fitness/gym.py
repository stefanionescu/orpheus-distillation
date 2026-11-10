"""Fitness prompts about gym talk, nutrition, exercises, programs, machines, muscle groups, and cardio."""

from __future__ import annotations

GYM: list[str] = [
    # ULTRA SHORT - GYM REACTIONS
    "PR baby!",
    "Chest day!",
    "Leg day!",
    "Back and bi's!",
    "Push day!",
    "Pull day!",
    "Rest day.",
    "Deload week.",
    "Gains!",
    "Pump is insane!",
    "Feel the burn!",
    "One more rep!",
    "Lock it out!",
    "Squeeze!",
    "Full ROM!",
    "No ego lifting!",
    "Mind muscle connection!",
    "Time under tension!",
    "Drop set!",
    "Superset!",
    "Giant set!",
    "AMRAP!",
    "EMOM!",
    "RPE eight!",
    "Two plates!",
    "Three plates!",
    "Four plates!",
    "Bodyweight!",
    "Progressive overload!",
    "Volume day!",
    # SHORT - GYM TALK
    "Just hit a new deadlift PR, two twenty five for five!",
    "Bro, my quads are absolutely destroyed after that leg session.",
    "Finally benched two plates for reps, been chasing that forever.",
    "The pump in my biceps is ridiculous right now.",
    "Skipped leg day again, I know, I know.",
    "That pre workout is hitting different today.",
    "Gotta get my protein in within the anabolic window.",
    "Foam rolling these IT bands is pure torture.",
    "My grip gave out before my back did on those rows.",
    "Wearing my lifting belt for anything over eighty percent now.",
    "These resistance bands are great for warming up the shoulders.",
    "Can't walk after that Bulgarian split squat workout.",
    "Hit failure on the last set, couldn't lock out the rep.",
    "Time for some light cardio, just twenty minutes on the stairmaster.",
    "Using straps today because my calluses are wrecked.",
    "That muscle up took me six months to finally get.",
    "Chalk makes such a difference on heavy pulling days.",
    "My hip flexors are so tight from sitting all day.",
    "Adding chains to the bar for accommodating resistance.",
    "Switched to low bar squat and it feels way better.",
    # SHORT - NUTRITION TALK
    "Tracking my macros religiously, hitting that protein goal every day.",
    "Started intermittent fasting, sixteen eight protocol works best for me.",
    "My meal prep Sundays save me so much time during the week.",
    "Hitting two hundred grams of protein is harder than it sounds.",
    "Creatine monohydrate is the only supplement that actually works.",
    "Bulking season starts now, time to eat in a surplus.",
    "Cutting for summer, sitting at a five hundred calorie deficit.",
    "Carb cycling around my training days for better performance.",
    "My protein shake is just whey, banana, and peanut butter.",
    "Greek yogurt is a cheat code for hitting protein macros.",
    "Chicken and rice gets boring but it's cheap and effective.",
    "Tried keto for three months, not sustainable for my training.",
    "Caffeine before fasted cardio really helps with fat oxidation.",
    "BCAAs are pointless if you're already eating enough protein.",
    "Refeed day today, carbing up to restore glycogen.",
    "My TDEE is around twenty eight hundred, eating twenty three for the cut.",
    "That post workout meal hits different after a brutal session.",
    "Eating clean but still getting my calories in, no dirty bulk.",
    "Water intake is key, aiming for a gallon a day minimum.",
    "Sodium is actually important for performance, don't avoid it.",
    # QUESTIONS - GYM
    "How many sets are you doing for chest today?",
    "What's your training split looking like right now?",
    "Are you running a PPL or an upper lower split?",
    "How long have you been lifting for?",
    "What's your one rep max on bench?",
    "Do you prefer dumbbells or barbell for pressing?",
    "Are you doing any accessory work after compounds?",
    "How much rest are you taking between sets?",
    "What program are you running, is it linear progression?",
    "Do you squat high bar or low bar?",
    "Are those Olympic lifting shoes or regular trainers?",
    "How often do you train legs per week?",
    "What's your warm up routine look like?",
    "Are you going to failure on every set?",
    "Do you do cardio on lifting days or separate?",
    "What's in that shaker bottle, pre or post workout?",
    "Are you natural or are you enhanced?",
    "How long until you compete, are you prepping?",
    "What weight class are you going for?",
    "Do you work with a coach or program yourself?",
    # QUESTIONS - NUTRITION
    "How many calories are you eating on training days?",
    "What's your protein intake per pound of bodyweight?",
    "Are you tracking everything or just eyeballing portions?",
    "Do you count vegetables towards your carb macros?",
    "What time do you break your fast usually?",
    "Are you using MyFitnessPal or a different app?",
    "How strict are you about hitting macros exactly?",
    "What's your go to post workout meal look like?",
    "Do you take any supplements besides protein and creatine?",
    "How much water weight did you drop in the first week?",
    "What's your maintenance calories at your current weight?",
    "Are you reverse dieting out of this cut?",
    "How long have you been in a deficit for?",
    "What percentage of your diet is protein?",
    "Do you have a cheat meal scheduled or eat clean always?",
    # MEDIUM - EXERCISES & TECHNIQUES
    "Romanian deadlifts absolutely torch my hamstrings, feeling it for days after.",
    "Paused reps at the bottom of the squat really build strength out of the hole.",
    "Face pulls should be in everyone's routine for shoulder health, three sets daily.",
    "Hip thrusts are the best glute builder, nothing else even comes close.",
    "Deficit deadlifts improved my speed off the floor more than anything else.",
    "Close grip bench is underrated for tricep development and lockout strength.",
    "Pendlay rows keep you honest, no momentum cheating when you reset each rep.",
    "Front squats are humbling, can't move nearly as much as back squat.",
    "Incline dumbbell press hits the upper chest way better than flat bench.",
    "Lat pulldowns with a slow eccentric really fry the lats.",
    "Cable crossovers at the end of chest day for that final pump.",
    "Hack squats take the lower back out of it so you can really load the quads.",
    "Dips are the upper body squat, compound movement that builds mass.",
    "Meadows rows hit the lats from a different angle, John Meadows was a genius.",
    "Leg press is great for volume after squats when you're already fatigued.",
    "Skull crushers were giving me elbow pain so I switched to overhead extensions.",
    "Hammer curls for the brachialis, makes the arms look thicker from the side.",
    "Belt squats are amazing if you have lower back issues, all legs no spine.",
    "Farmer carries improve grip and core stability like nothing else.",
    "Turkish get ups are a full body movement, great for mobility and stability.",
    # MEDIUM - PROGRAMS & METHODS
    "Running 5/3/1 with BBB accessories, the volume is brutal but effective.",
    "GZCL method is perfect for intermediate lifters who stalled on linear progression.",
    "Starting Strength got me to a three plate squat in my first year.",
    "nSuns is insane volume but my bench went up twenty pounds in eight weeks.",
    "Conjugate method with max effort and dynamic effort days, Westside style.",
    "Push pull legs is the perfect split, hit everything twice a week with enough recovery.",
    "Upper lower four days a week fits my schedule and allows for progressive overload.",
    "Bro split hitting each muscle once a week isn't optimal but people still grow.",
    "Full body three times a week is underrated for naturals who need frequency.",
    "Doing a strength block before transitioning to hypertrophy focus.",
    "Periodization matters more than the specific program you're running.",
    "Auto regulation based on how I feel, adjusting RPE targets daily.",
    "Running a peaking cycle for my meet in eight weeks, tapering volume.",
    "Deload every fourth week, drop to sixty percent of normal volume.",
    "Greasing the groove for pull ups, multiple sets throughout the day.",
    # MEDIUM - NUTRITION DETAILS
    "One gram of protein per pound of bodyweight is the gold standard recommendation.",
    "Eating in a two hundred calorie deficit for slow and sustainable fat loss.",
    "High protein low calorie snacks like cottage cheese and beef jerky are clutch.",
    "Pre workout meal is usually rice and chicken about two hours before training.",
    "Intra workout carbs help me maintain intensity during longer sessions.",
    "IIFYM works but food quality still matters for health and satiety.",
    "Diet breaks every eight weeks of dieting to restore metabolic rate.",
    "Flexible dieting lets me fit treats in as long as I hit my macros.",
    "Meal timing doesn't matter that much, total daily intake is what counts.",
    "Protein timing is less important than total protein, but I still prioritize post workout.",
    "Fat should be at least twenty percent of calories for hormonal health.",
    "Fiber intake is the forgotten macro, shooting for thirty grams daily.",
    "Eating the same meals every day makes tracking so much easier.",
    "Sodium manipulation for the last week of prep, dry out for the stage.",
    "Peak week is all about glycogen loading and water manipulation.",
    # LONG - GYM EXPERIENCES
    (
        "Finally hit a four plate deadlift after three years of grinding, started with just the bar and couldn't even "
        "do one thirty five, now I'm pulling four oh five for singles and it feels unreal."
    ),
    (
        "Switched from a bro split to push pull legs and my recovery improved so much, hitting each muscle twice a "
        "week with less volume per session but more frequency overall, gains have been better than ever."
    ),
    (
        "Blew out my lower back last year doing ego lifting on deadlifts, spent six months rehabbing with a physical "
        "therapist, now I'm back to pulling heavy but with way better form and bracing."
    ),
    (
        "The mind muscle connection thing sounded like bro science until I actually tried slowing down my reps and "
        "focusing on the contraction, chest day feels completely different now."
    ),
    (
        "Morning fasted training took some getting used to but now I actually prefer it, caffeine and a banana is all "
        "I need, save the big meal for post workout when I'm actually hungry."
    ),
    (
        "Competition prep is no joke, sixteen weeks of dieting down, cardio twice a day the last month, hitting poses "
        "in the mirror constantly, all for five minutes on stage but worth every second."
    ),
    (
        "Home gym during lockdown was the best investment, power rack, barbell, enough plates for everything I need, "
        "never going back to a commercial gym again, train whenever I want."
    ),
    (
        "Tried Olympic lifting for a year, the snatch and clean and jerk are so technical, completely different from "
        "powerlifting, gave me a new appreciation for athleticism and mobility."
    ),
    (
        "Deload weeks feel like you're losing gains but you always come back stronger, the fatigue masks your fitness, "
        "once it dissipates you realize how much progress you actually made."
    ),
    (
        "Getting stapled by a squat is terrifying, had to dump the bar behind me for the first time last week, learned "
        "my lesson about setting up the safeties properly every single time."
    ),
    # LONG - NUTRITION EXPERIENCES
    (
        "Tracking macros seemed obsessive until I realized I was massively under eating protein, thought I was getting "
        "enough but was barely hitting a hundred grams when I needed one eighty."
    ),
    (
        "The reverse diet after my cut was harder than the cut itself, mentally difficult to add calories back slowly "
        "when you just want to eat everything, but it preserved my results."
    ),
    (
        "Tried every diet under the sun, keto, paleo, carnivore, vegan, and ended up just counting calories and eating "
        "mostly whole foods, nothing fancy but it actually works."
    ),
    (
        "Meal prepping twelve pounds of chicken breast on Sunday sounds excessive but it sets up my whole week, just "
        "grab a container and go, no decisions no excuses."
    ),
    (
        "Intermittent fasting isn't magic for fat loss, it just helps me eat less by having a smaller eating window, "
        "if you're not in a deficit you won't lose weight regardless."
    ),
    (
        "Learning to cook made my fitness journey so much easier, knowing how to make chicken taste good without "
        "adding a bunch of calories is an underrated skill for anyone serious about this."
    ),
    (
        "The thermic effect of food is real, eating more protein means you burn more calories just digesting it, plus "
        "it's way more satiating than carbs or fat gram for gram."
    ),
    (
        "Flexible dieting saved my relationship with food, used to think certain foods were off limits, now I fit "
        "whatever I want as long as it fits my macros for the day."
    ),
    (
        "Hydration is so overlooked, I was chronically dehydrated for years, started drinking a gallon a day and my "
        "performance in the gym improved noticeably within a week."
    ),
    (
        "The scale lies, my weight stayed the same for a month but my waist measurement went down an inch, body "
        "recomposition is real especially for newer lifters."
    ),
    # MACHINES & EQUIPMENT
    "Switched from machines to free weights and saw way more progress.",
    "The cable machine is so versatile, endless exercise variations.",
    "Smith machine squats are fine for hypertrophy, just different stimulus.",
    "Love the leg extension machine for isolating the quads after squats.",
    "Hammer Strength chest press hits different than barbell bench.",
    "The pec deck gives an insane stretch and contraction on the chest.",
    "Using the assisted pull up machine until I can do bodyweight reps.",
    "Seated cable rows with the V grip handle for that thick back.",
    "The hack squat machine is my favorite for quad focused work.",
    "Leg curl machine for hammies, both lying and seated versions work.",
    "Tricep rope pushdowns, squeeze and spread at the bottom for peak contraction.",
    "Using the ab wheel for core, way harder than it looks.",
    "Battle ropes for conditioning, brutal on the shoulders and grip.",
    "Rowing machine for low impact cardio that actually works.",
    "Assault bike is a torture device, nothing spikes heart rate faster.",
    "Trap bar deadlifts are easier on the back, more quad dominant too.",
    "Safety squat bar takes stress off the shoulders and wrists.",
    "Cambered bar for bench helps with shoulder mobility issues.",
    "Bands and chains for accommodating resistance on the big lifts.",
    "Fractional plates for microloading, half pound increases add up.",
    # BODY PARTS & MUSCLE GROUPS
    "My lagging body part is definitely calves, genetics are brutal.",
    "Rear delts need more work, they make the shoulders look three dimensional.",
    "Forearms growing from just doing heavy pulling movements.",
    "Upper chest needs more incline work, it's flat compared to the lower.",
    "Side delts are what give that capped shoulder look.",
    "Lower back pumps from squats and deadlifts are crippling.",
    "Glutes firing properly now after doing activation work before squats.",
    "Serratus anterior is an underrated muscle for aesthetics.",
    "My traps have always been my strongest muscle group genetically.",
    "Hip flexors are constantly tight, need to stretch more.",
    "Adductors are sore from going wider on my squat stance.",
    "Brachialis development makes arms look bigger from the front.",
    "Long head of the tricep needs overhead work to fully develop.",
    "Short head of the bicep for the peak, long head for thickness.",
    "Transverse abdominis is key for that vacuum pose look.",
    "Obliques respond well to loaded carries and rotational work.",
    "Rhomboids are always tight, need to roll them out constantly.",
    "Spinal erectors are worked on every compound lift basically.",
    "VMO development helps with knee tracking on squats.",
    "Infraspinatus work for rotator cuff health and injury prevention.",
    # CARDIO & CONDITIONING
    "LISS cardio for fat loss, just walking on an incline for forty five minutes.",
    "HIIT sessions twice a week, sprints on the bike for twenty seconds on ten off.",
    "Steady state cardio is boring but it works, zone two heart rate training.",
    "The stairmaster is brutal, twenty minutes feels like an hour.",
    "Jump rope is underrated cardio, good for coordination and calf development.",
    "Prowler pushes are the worst, but they build insane conditioning.",
    "Sled drags for recovery, light weight high volume, gets blood flowing.",
    "Swimming is great for active recovery, zero impact on the joints.",
    "Rucking with a weighted vest, just walking but harder.",
    "Tabata protocol is four minutes of hell, eight rounds twenty on ten off.",
    "Metabolic conditioning with kettlebell swings, heart rate through the roof.",
    "Doing cardio kills my gains is a myth, just eat enough to compensate.",
    "Fasted cardio isn't magic but I prefer training on an empty stomach.",
    "The echo bike is somehow worse than the assault bike.",
    "Jogging is the worst cardio for body composition, just walk or sprint.",
]

"""Therapy prompts about anxiety, mood, relationships, families, and mindfulness."""

from __future__ import annotations

MINDFULNESS: list[str] = [
    # LONG PROMPTS - ANXIETY & MOOD DISORDERS
    (
        "Generalized anxiety disorder involves persistent excessive worry about multiple domains, accompanied by "
        "physical tension, restlessness, concentration difficulties, and sleep disturbance."
    ),
    (
        "Panic disorder features recurrent unexpected panic attacks followed by persistent concern about future "
        "attacks or maladaptive behavioral changes to avoid them."
    ),
    (
        "Social anxiety disorder involves marked fear of social situations where scrutiny and negative evaluation are "
        "possible, leading to avoidance or intense distress."
    ),
    (
        "Specific phobias involve marked fear or anxiety about specific objects or situations that is out of "
        "proportion to actual danger and leads to avoidance."
    ),
    (
        "Agoraphobia involves anxiety about situations where escape might be difficult or help unavailable during "
        "panic-like symptoms, often severely limiting activity."
    ),
    (
        "Separation anxiety in adults involves excessive fear concerning separation from attachment figures, with "
        "worry about harm and reluctance to be apart."
    ),
    (
        "Illness anxiety disorder involves preoccupation with having or acquiring serious illness despite minimal "
        "symptoms and appropriate medical evaluation and reassurance."
    ),
    (
        "Major depressive disorder features depressed mood or anhedonia accompanied by sleep, appetite, energy, "
        "concentration, and psychomotor changes with suicidal ideation possible."
    ),
    (
        "Persistent depressive disorder involves chronic depressed mood lasting at least two years with additional "
        "depressive symptoms, often seen as characterological."
    ),
    (
        "Bipolar one disorder includes manic episodes with elevated mood, decreased sleep need, grandiosity, pressured "
        "speech, and impaired judgment causing significant impairment."
    ),
    (
        "Bipolar two disorder features hypomanic episodes less severe than full mania alongside major depressive "
        "episodes that often cause more impairment."
    ),
    (
        "Cyclothymic disorder involves chronic fluctuating mood with numerous hypomanic and depressive periods not "
        "meeting full episode criteria over at least two years."
    ),
    (
        "Mixed features specify mood episodes with simultaneous symptoms of opposite polarity, complicating treatment "
        "and increasing suicide risk."
    ),
    (
        "Rapid cycling involves four or more mood episodes within twelve months, often associated with worse prognosis "
        "and treatment resistance."
    ),
    (
        "Seasonal pattern describes mood episodes occurring at characteristic times of year, typically winter "
        "depression and spring or summer improvement."
    ),
    (
        "Peripartum onset specifies mood episodes occurring during pregnancy or within four weeks of delivery, "
        "requiring careful treatment consideration."
    ),
    (
        "Melancholic features include loss of pleasure, worse mood in morning, early awakening, psychomotor changes, "
        "and excessive guilt in depressive episodes."
    ),
    (
        "Atypical features involve mood reactivity, increased sleep, leaden paralysis, interpersonal rejection "
        "sensitivity, and increased appetite in depressive presentations."
    ),
    (
        "Anxious distress as specifier indicates prominent anxiety symptoms accompanying mood episodes, associated "
        "with worse outcomes and suicide risk."
    ),
    (
        "Treatment-resistant depression fails to respond to adequate trials of multiple antidepressant medications, "
        "requiring alternative approaches like augmentation or neuromodulation."
    ),
    # LONG PROMPTS - RELATIONSHIP & FAMILY THERAPY
    (
        "Emotionally focused therapy identifies negative interaction cycles maintained by attachment insecurity, "
        "helping partners access underlying attachment needs and respond more responsively."
    ),
    (
        "The Gottman method identifies four horsemen predicting relationship dissolution: criticism, contempt, "
        "defensiveness, and stonewalling, while building friendship and conflict management skills."
    ),
    (
        "Pursuer-distancer dynamics describe the common pattern where one partner seeks connection while the other "
        "withdraws, creating escalating cycles of pursuit and distance."
    ),
    (
        "Attachment injuries are specific incidents of abandonment or betrayal that damage trust and require explicit "
        "processing for relationship repair."
    ),
    (
        "Structural family therapy examines family organization including hierarchies, boundaries, and subsystems, "
        "intervening to create more functional family structures."
    ),
    (
        "Strategic family therapy focuses on specific problems and uses directives, reframing, and paradoxical "
        "interventions to disrupt problematic interaction patterns."
    ),
    (
        "Narrative family therapy externalizes problems and helps families construct alternative stories that "
        "highlight competence and preferred ways of relating."
    ),
    (
        "Multigenerational patterns transmit through families, with genograms revealing repetitive themes across "
        "generations that inform current relational difficulties."
    ),
    (
        "Differentiation describes the capacity to maintain self while remaining connected to others, balancing "
        "autonomy and intimacy in close relationships."
    ),
    (
        "Triangulation occurs when dyadic tension is managed by involving a third party, creating unstable alliances "
        "that often worsen underlying issues."
    ),
    (
        "The identified patient carries symptoms that serve homeostatic function in the family system, often "
        "distracting from other family problems."
    ),
    (
        "Enmeshment describes overly close boundaries where family members lack adequate autonomy and individual "
        "differences are threatening to cohesion."
    ),
    (
        "Disengagement represents overly rigid boundaries with little connection between family members and limited "
        "response to others' emotional needs."
    ),
    (
        "Parentification occurs when children assume adult caretaking responsibilities inappropriately, often in "
        "response to parental dysfunction or absence."
    ),
    (
        "The double bind places someone in impossible situations where any response is wrong, potentially contributing "
        "to confusion and symptoms."
    ),
    (
        "Circular causality recognizes that family interactions are mutually influencing rather than linearly caused, "
        "with each member's behavior affecting others."
    ),
    (
        "Joining techniques help therapists become accepted by the family system through tracking, mimesis, and "
        "acknowledging family strengths."
    ),
    (
        "Enactment invites families to demonstrate problematic interactions in session, allowing direct observation "
        "and intervention in real-time dynamics."
    ),
    (
        "Reframing offers alternative interpretations of behavior that change meaning and open possibilities for "
        "different responses."
    ),
    (
        "Positive connotation attributes positive motivation to symptomatic behavior, reducing defensiveness and "
        "paradoxically freeing change possibilities."
    ),
    # LONG PROMPTS - MINDFULNESS & ACCEPTANCE
    (
        "Mindfulness involves paying attention on purpose, in the present moment, and non-judgmentally, cultivating "
        "awareness that creates space between stimulus and response."
    ),
    (
        "Non-judgmental observation notices experiences without evaluating them as good or bad, reducing the secondary "
        "suffering created by resistance to experience."
    ),
    (
        "Beginner's mind approaches each moment with fresh curiosity rather than preconceptions, remaining open to "
        "what is actually present."
    ),
    (
        "Acceptance is active embrace of experience without unnecessary attempts to change its frequency or form, "
        "distinct from resignation or approval."
    ),
    (
        "Present-moment awareness anchors attention in immediate experience rather than ruminating about the past or "
        "worrying about the future."
    ),
    (
        "The observing self is the aspect of consciousness that notices thoughts and feelings without being identical "
        "to them."
    ),
    (
        "Automatic pilot describes habitual responding without awareness, where familiar routines run without "
        "conscious attention or choice."
    ),
    (
        "Decentering involves seeing thoughts as mental events rather than facts, creating perspective that reduces "
        "their emotional impact."
    ),
    (
        "Mindfulness-based cognitive therapy prevents depression relapse by teaching mindful awareness of depression "
        "warning signs and decentering from ruminative thinking."
    ),
    (
        "Mindfulness-based stress reduction applies mindfulness meditation to chronic pain and illness, changing "
        "relationships to suffering rather than eliminating symptoms."
    ),
    (
        "The body scan systematically moves attention through bodily sensations, cultivating interoceptive awareness "
        "and present-moment focus."
    ),
    (
        "Loving-kindness meditation cultivates compassionate wishes for self and others, counteracting self-criticism "
        "and building positive emotional capacities."
    ),
    (
        "Compassion-focused therapy specifically targets shame and self-criticism through developing the soothing "
        "system and self-compassionate inner voice."
    ),
    "Self-compassion involves treating oneself with the same kindness offered to a good friend during difficult times.",
    (
        "Common humanity recognizes that suffering and imperfection are shared human experiences rather than isolating "
        "personal failures."
    ),
    (
        "The three components of self-compassion include self-kindness, common humanity, and mindful awareness of "
        "suffering without overidentification."
    ),
    (
        "Backdraft describes the initial intensification of difficult emotions when extending compassion to oneself "
        "after long self-criticism."
    ),
    (
        "Equanimity maintains balanced awareness amid changing experiences, neither pushing away nor grasping at any "
        "particular state."
    ),
    (
        "Interoceptive awareness involves sensing internal bodily states including heart rate, breathing, and visceral "
        "sensations that inform emotional experience."
    ),
    (
        "Urge surfing applies mindful awareness to cravings, observing them rise and fall without acting, building "
        "distress tolerance."
    ),
]

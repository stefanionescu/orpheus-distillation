"""Therapy prompts: short terms, observations, and questions, then cognitive and psychodynamic therapy."""

from __future__ import annotations

COGNITIVE: list[str] = [
    # ULTRA SHORT - THERAPEUTIC TERMS
    "Transference observed.",
    "Countertransference activated.",
    "Attachment rupture.",
    "Schema triggered.",
    "Cognitive distortion.",
    "Defense mechanism.",
    "Dissociation present.",
    "Hypervigilance noted.",
    "Affect dysregulation.",
    "Somatic experiencing.",
    "Ego depletion.",
    "Resistance emerging.",
    "Projection identified.",
    "Splitting behavior.",
    "Enmeshment patterns.",
    "Boundaries violated.",
    "Rapport established.",
    "Therapeutic alliance.",
    "Holding environment.",
    "Containment provided.",
    # SHORT STATEMENTS - THERAPEUTIC OBSERVATIONS
    "The client presents with significant affect dysregulation.",
    "I notice some resistance emerging in our session today.",
    "Your attachment style appears to be anxious-preoccupied.",
    "This sounds like a core maladaptive schema activating.",
    "The therapeutic alliance seems to be strengthening nicely.",
    "I'm sensing some countertransference arising within myself.",
    "Your defense mechanisms are working overtime right now.",
    "This pattern reflects early relational trauma quite clearly.",
    "The somatic symptoms suggest unprocessed emotional material.",
    "Your window of tolerance appears quite narrow currently.",
    "I observe significant dissociative symptoms emerging here.",
    "The intrusive thoughts seem to follow an obsessive pattern.",
    "Your hyperarousal response indicates sympathetic nervous activation.",
    "This avoidance behavior serves a protective function.",
    "The cognitive distortions are reinforcing depressive symptoms.",
    "I notice catastrophizing in your thought patterns.",
    "Your emotional flashback response was just triggered.",
    "The shame spiral seems to be intensifying rapidly.",
    "This relational pattern repeats across multiple relationships.",
    "Your inner critic voice sounds particularly harsh today.",
    "The self-sabotaging behavior serves an unconscious purpose.",
    "I sense deep grief underlying the presented anger.",
    "Your nervous system appears to be in freeze response.",
    "The abandonment wound seems to drive this anxiety.",
    "This perfectionism masks underlying feelings of inadequacy.",
    # SHORT QUESTIONS - THERAPEUTIC INQUIRIES
    "What emotions are you noticing in your body right now?",
    "Can you tell me more about that feeling?",
    "Where do you feel that sensation physically?",
    "What thoughts accompany this emotional state?",
    "How did that experience affect you growing up?",
    "What would your younger self need to hear?",
    "Can you stay with that feeling for a moment?",
    "What defense mechanism might be activating here?",
    "How does this pattern show up in relationships?",
    "What core belief is being triggered right now?",
    "Can you identify the cognitive distortion present?",
    "What would healthy boundaries look like here?",
    "How might we challenge this automatic thought?",
    "What evidence contradicts this belief you hold?",
    "Can you practice self-compassion in this moment?",
    "What does your inner child need right now?",
    "How does perfectionism serve you currently?",
    "What would acceptance of this feeling look like?",
    "Can you notice the judgment without attaching?",
    "What early experience does this remind you of?",
    "How might we reframe this situation together?",
    "What values align with your authentic self?",
    "Can you identify the trigger for this response?",
    "What safety do you need to feel grounded?",
    "How does avoidance maintain this anxiety cycle?",
    # SHORT EXCLAMATIONS - THERAPEUTIC MOMENTS
    "That's a significant breakthrough moment!",
    "You're showing remarkable self-awareness here!",
    "That insight is incredibly valuable!",
    "Your courage in sharing this is admirable!",
    "What a powerful realization you've just had!",
    "The progress you've made is truly remarkable!",
    "That's an excellent example of self-compassion!",
    "You're really challenging those cognitive distortions!",
    "Your emotional regulation skills are improving!",
    "That boundary you set was incredibly healthy!",
    "You've just accessed some deep material here!",
    "The therapeutic alliance feels very strong today!",
    "Your window of tolerance has expanded significantly!",
    "That's genuine integration happening right now!",
    "You're developing secure attachment patterns!",
    "The schema healing work is paying off!",
    "Your nervous system is finding regulation!",
    "That was authentic emotional expression!",
    "You've reclaimed your voice so powerfully!",
    "The trauma processing is really progressing!",
    # LONG PROMPTS - CBT & COGNITIVE APPROACHES
    (
        "Cognitive behavioral therapy identifies the automatic negative thoughts that trigger emotional distress, "
        "examining the cognitive distortions present and developing more balanced alternative thoughts through "
        "systematic cognitive restructuring techniques."
    ),
    (
        "The cognitive triad in depression involves negative views of self, world, and future, creating a "
        "self-reinforcing cycle of maladaptive cognitions that maintain depressive symptomatology."
    ),
    (
        "Behavioral activation addresses depression by scheduling pleasurable and mastery activities that counteract "
        "the avoidance and withdrawal patterns maintaining low mood and anhedonia symptoms."
    ),
    (
        "Cognitive restructuring involves identifying automatic thoughts, examining evidence for and against these "
        "thoughts, and generating more balanced alternative cognitions that reduce emotional distress."
    ),
    (
        "The downward arrow technique uncovers core beliefs by repeatedly asking what a thought means about the "
        "person, revealing underlying schemas driving surface-level cognitive distortions."
    ),
    (
        "Thought records document triggering situations, automatic thoughts, emotions, cognitive distortions, balanced "
        "alternative thoughts, and resulting emotional changes to develop metacognitive awareness and cognitive "
        "flexibility."
    ),
    (
        "Socratic questioning guides clients toward their own insights through open-ended questions that examine "
        "evidence, consider alternative perspectives, and evaluate the utility of beliefs."
    ),
    (
        "Behavioral experiments test the validity of maladaptive beliefs through structured real-world experiences "
        "that often disconfirm catastrophic predictions and build self-efficacy."
    ),
    (
        "Exposure and response prevention treats obsessive-compulsive disorder by systematically confronting feared "
        "situations while preventing compulsive rituals, allowing habituation and extinction of anxiety responses."
    ),
    (
        "The cognitive model of anxiety posits that overestimation of threat and underestimation of coping resources "
        "maintain anxious states through catastrophic interpretations of ambiguous stimuli."
    ),
    (
        "Interoceptive exposure for panic disorder involves deliberately inducing feared physical sensations to reduce "
        "catastrophic misinterpretations of benign bodily experiences and break the panic cycle."
    ),
    (
        "Safety behaviors paradoxically maintain anxiety by preventing disconfirmation of feared outcomes and "
        "attributing non-occurrence to the safety behavior rather than actual safety."
    ),
    (
        "Metacognitive therapy targets beliefs about thinking itself, addressing worry about worry and attentional "
        "strategies that maintain psychological distress through cognitive attentional syndrome."
    ),
    (
        "Acceptance and commitment therapy promotes psychological flexibility through acceptance of difficult "
        "experiences, cognitive defusion from unhelpful thoughts, and committed action toward valued directions."
    ),
    (
        "Values clarification helps clients identify what truly matters to them, providing motivation for behavioral "
        "change and direction for committed action in acceptance-based approaches."
    ),
    (
        "Cognitive defusion techniques create distance from thoughts, recognizing them as mental events rather than "
        "literal truths, reducing their behavioral impact and emotional intensity."
    ),
    (
        "The observing self represents the transcendent awareness that can notice thoughts and feelings without being "
        "defined by them, facilitating acceptance and psychological flexibility."
    ),
    (
        "Experiential avoidance maintains psychological distress by preventing processing of difficult emotions and "
        "reinforcing beliefs that internal experiences are dangerous or intolerable."
    ),
    (
        "Rumination involves repetitive passive focus on distress symptoms and their causes, maintaining depressive "
        "episodes and preventing active problem-solving and behavioral engagement."
    ),
    (
        "Worry serves as cognitive avoidance of more distressing imagery and emotions, maintaining anxiety through "
        "verbal linguistic processing that prevents emotional processing."
    ),
    # LONG PROMPTS - PSYCHODYNAMIC & DEPTH PSYCHOLOGY
    (
        "Psychoanalytic theory posits that unconscious conflicts originating in early childhood drive current "
        "psychological symptoms, with insight into these dynamics facilitating symptom resolution and personality "
        "change."
    ),
    (
        "Transference occurs when clients unconsciously project feelings and expectations from past significant "
        "relationships onto the therapist, providing valuable material for understanding relational patterns."
    ),
    (
        "Countertransference involves the therapist's emotional reactions to the client, which may reflect the "
        "therapist's own unresolved issues or provide important information about the client's relational impact."
    ),
    (
        "Defense mechanisms are unconscious psychological strategies that protect the ego from anxiety-provoking "
        "thoughts and feelings, including repression, projection, rationalization, and reaction formation."
    ),
    (
        "Object relations theory examines how early relationships with caregivers create internal representations that "
        "shape subsequent relational patterns and expectations throughout the lifespan."
    ),
    (
        "The holding environment describes the therapist's capacity to contain and metabolize the client's difficult "
        "emotions, providing safety for exploration of previously overwhelming experiences."
    ),
    (
        "Projective identification occurs when one person unconsciously projects disowned aspects onto another, who "
        "then identifies with and enacts these projected qualities in the relationship."
    ),
    (
        "The repetition compulsion describes the unconscious tendency to recreate early traumatic relational patterns "
        "in current relationships, seeking mastery but often reinforcing maladaptive dynamics."
    ),
    (
        "Working through involves repeatedly examining unconscious material from multiple angles until emotional "
        "insight produces lasting change in symptoms and relational patterns."
    ),
    (
        "Resistance in psychodynamic therapy represents unconscious opposition to bringing repressed material into "
        "awareness, often manifesting as missed sessions, topic changes, or therapeutic impasses."
    ),
    (
        "The therapeutic frame encompasses the consistent structure of therapy including time, place, fee, and "
        "boundaries that creates safety for deep psychological exploration."
    ),
    (
        "Mentalization is the capacity to understand behavior in terms of underlying mental states, both in oneself "
        "and others, developing through secure early attachment experiences."
    ),
    (
        "Attachment theory describes how early caregiver relationships create internal working models of self and "
        "others that organize expectations and behaviors in subsequent relationships."
    ),
    (
        "Secure attachment develops when caregivers consistently respond sensitively to infant needs, creating "
        "internal models of self as worthy and others as reliably available."
    ),
    (
        "Anxious attachment forms when caregivers are inconsistently available, leading to hyperactivation of "
        "attachment behaviors and preoccupation with relationship security and partner availability."
    ),
    (
        "Avoidant attachment develops from consistently unresponsive caregiving, leading to deactivation of attachment "
        "needs and defensive self-reliance that limits emotional intimacy."
    ),
    (
        "Disorganized attachment results from frightening or frightened caregiver behavior, creating contradictory "
        "approach-avoid responses and difficulty regulating emotions in close relationships."
    ),
    (
        "Earned secure attachment describes the integration of difficult early experiences through reflection and "
        "therapeutic work, developing coherent narratives and secure relational capacities."
    ),
    (
        "The internal critic represents internalized harsh parental or societal judgments that generate shame and "
        "self-attack, often operating outside conscious awareness."
    ),
    (
        "Shame involves a global negative evaluation of self as fundamentally flawed or unworthy, differing from guilt "
        "which focuses on specific behaviors."
    ),
    (
        "The false self develops as adaptation to caregiver expectations, hiding authentic needs and feelings behind a "
        "compliant facade that maintains relationships."
    ),
    (
        "Individuation describes the developmental process of becoming a differentiated self while maintaining "
        "connection with others, balancing autonomy and intimacy needs."
    ),
    (
        "Splitting is a primitive defense that divides experience into all-good or all-bad categories, protecting "
        "against ambivalence but distorting reality and relationships."
    ),
    (
        "The paranoid-schizoid position involves persecutory anxiety and splitting, while the depressive position "
        "integrates good and bad, enabling guilt, concern, and reparation."
    ),
    (
        "Projective processes evacuate intolerable aspects of self into others, temporarily relieving internal "
        "distress but creating interpersonal difficulties and identity confusion."
    ),
]

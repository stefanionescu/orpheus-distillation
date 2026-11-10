"""Therapy prompts about humanistic therapy, assessment, and personality disorders."""

from __future__ import annotations

HUMANISTIC: list[str] = [
    # LONG PROMPTS - HUMANISTIC & EXISTENTIAL
    (
        "Person-centered therapy emphasizes the actualizing tendency, trusting that given the right relational "
        "conditions, clients naturally move toward growth, integration, and optimal functioning."
    ),
    (
        "Unconditional positive regard involves accepting clients fully without judgment, communicating that their "
        "worth does not depend on meeting conditions or expectations."
    ),
    (
        "Empathic understanding requires accurately sensing the client's inner world and communicating this "
        "understanding, creating the safety for deeper self-exploration."
    ),
    (
        "Congruence means the therapist is genuinely present, transparent, and authentic, not hiding behind "
        "professional facade while remaining appropriate to the therapeutic relationship."
    ),
    (
        "The actualizing tendency is the inherent drive toward growth, development, and fulfillment that exists in all "
        "living organisms and guides therapeutic change."
    ),
    (
        "Conditions of worth are internalized external standards for self-acceptance that create incongruence between "
        "organismic experience and self-concept."
    ),
    (
        "Organismic valuing describes the innate ability to evaluate experiences based on their contribution to growth "
        "and well-being, often suppressed by conditions of worth."
    ),
    (
        "Existential anxiety confronts fundamental human concerns including death, freedom, isolation, and "
        "meaninglessness that underlie many psychological symptoms and life struggles."
    ),
    (
        "Authentic living involves acknowledging existential realities and making choices aligned with personal values "
        "rather than avoiding awareness through bad faith."
    ),
    (
        "Freedom and responsibility are inseparable in existential thought, with awareness of choice creating anxiety "
        "but also enabling meaningful self-directed living."
    ),
    (
        "Existential isolation recognizes the unbridgeable gap between individuals, where even in closest connection, "
        "each person remains fundamentally alone in their experience."
    ),
    (
        "The search for meaning represents a primary human motivation, with meaninglessness contributing to "
        "depression, addiction, and various forms of psychological distress."
    ),
    (
        "Logotherapy helps clients find meaning through creative work, experiencing values, and attitudes toward "
        "unavoidable suffering, addressing the existential vacuum."
    ),
    (
        "Death awareness can motivate authentic living by highlighting finitude and the preciousness of time, shifting "
        "priorities toward what truly matters."
    ),
    (
        "Bad faith involves self-deception about freedom and responsibility, pretending that circumstances determine "
        "choices rather than acknowledging authentic possibilities."
    ),
    (
        "Gestalt therapy focuses on present-moment awareness, integrating disowned aspects of experience through "
        "experiments that heighten contact with immediate experience."
    ),
    (
        "The empty chair technique invites dialogue with absent others, disowned parts of self, or conflicting aspects "
        "of experience to promote integration."
    ),
    (
        "Unfinished business refers to unexpressed emotions and incomplete experiences from the past that continue "
        "affecting present functioning and relationships."
    ),
    (
        "Contact and withdrawal describe the natural rhythm of engaging with and retreating from environment and "
        "others, with disturbances creating symptoms."
    ),
    (
        "The here and now focus in Gestalt intensifies present experience, believing that awareness itself is curative "
        "and change occurs through becoming."
    ),
    # LONG PROMPTS - ASSESSMENT & DIAGNOSIS
    (
        "The mental status examination systematically assesses appearance, behavior, speech, mood, affect, thought "
        "process, thought content, perception, cognition, insight, and judgment."
    ),
    (
        "DSM five uses dimensional approaches alongside categorical diagnoses, recognizing that psychological distress "
        "exists on continua rather than discrete categories."
    ),
    (
        "Differential diagnosis involves systematically considering and ruling out alternative explanations for "
        "presenting symptoms to arrive at accurate diagnostic formulations."
    ),
    (
        "Structured clinical interviews increase diagnostic reliability by standardizing questions and decision rules, "
        "reducing variability in how clinicians assess symptoms."
    ),
    (
        "Psychological testing provides standardized assessment of personality, cognitive functioning, and symptom "
        "severity through validated instruments with normative comparison data."
    ),
    (
        "The biopsychosocial model integrates biological, psychological, and social factors in understanding the "
        "development, presentation, and treatment of psychological disorders."
    ),
    (
        "Comorbidity is common in mental health, with multiple disorders frequently co-occurring and complicating "
        "treatment planning and prognosis."
    ),
    (
        "Functional impairment assesses how symptoms affect daily living, relationships, work, and other important "
        "life domains beyond mere symptom presence."
    ),
    (
        "Protective factors buffer against psychopathology and promote resilience, including social support, coping "
        "skills, and meaning-making capacities."
    ),
    (
        "Risk assessment evaluates likelihood of harm to self or others, considering historical, clinical, and "
        "contextual factors in safety planning."
    ),
    (
        "Suicide assessment examines ideation, intent, plan, means, and protective factors to determine appropriate "
        "level of care and intervention."
    ),
    (
        "Cultural formulation considers how cultural background influences symptom expression, help-seeking, "
        "explanatory models, and therapeutic relationship dynamics."
    ),
    (
        "Diagnostic overshadowing occurs when symptoms are attributed to one diagnosis while another condition goes "
        "unrecognized and untreated."
    ),
    (
        "Atypical presentations may indicate underlying medical conditions, trauma histories, cultural factors, or "
        "developmental differences requiring careful assessment."
    ),
    (
        "Longitudinal assessment tracks symptom patterns over time, revealing episodic versus chronic conditions and "
        "informing treatment and prognosis."
    ),
    (
        "Collateral information from family, partners, or previous providers enriches understanding when clients have "
        "limited insight or recall."
    ),
    (
        "Baseline assessment establishes pre-treatment symptom levels and functioning for measuring treatment response "
        "and outcomes over time."
    ),
    (
        "Outcome measures track therapeutic progress through standardized instruments administered repeatedly "
        "throughout treatment to guide clinical decisions."
    ),
    (
        "The therapeutic assessment model makes assessment itself therapeutic by collaborating with clients in "
        "understanding their difficulties and building motivation."
    ),
    (
        "Formulation integrates assessment information into coherent understanding of how problems developed, what "
        "maintains them, and how therapy might help."
    ),
    # LONG PROMPTS - PERSONALITY DISORDERS
    (
        "Borderline personality organization involves identity diffusion, primitive defenses, and reality testing "
        "impairment under stress, creating instability across relationships, self-image, and emotions."
    ),
    (
        "Narcissistic vulnerability underlies grandiose presentations, with fragile self-esteem requiring constant "
        "validation and reacting intensely to perceived criticism or failure."
    ),
    (
        "Avoidant personality pattern involves pervasive social inhibition, feelings of inadequacy, and "
        "hypersensitivity to negative evaluation that limits relationships and opportunities."
    ),
    (
        "Dependent personality features include excessive need for care and support, difficulty making decisions "
        "independently, and fear of separation driving submissive behavior."
    ),
    (
        "Obsessive-compulsive personality differs from OCD in its ego-syntonic preoccupation with order, "
        "perfectionism, and control that pervades multiple life domains."
    ),
    (
        "Antisocial personality involves persistent disregard for others' rights, lack of remorse, impulsivity, and "
        "deceitfulness often beginning with conduct disorder in adolescence."
    ),
    (
        "Schizoid patterns reflect detachment from social relationships with restricted emotional range, preferring "
        "solitary activities without apparent desire for connection."
    ),
    (
        "Schizotypal features include social anxiety, odd beliefs and magical thinking, unusual perceptual "
        "experiences, and eccentric behavior approaching psychotic spectrum."
    ),
    (
        "Histrionic presentation involves excessive emotionality and attention-seeking, with shifting shallow emotions "
        "and relationships characterized by perceived greater intimacy than exists."
    ),
    (
        "Paranoid personality patterns include pervasive distrust, suspicion of others' motives, hypervigilance for "
        "hidden meanings, and reluctance to confide in others."
    ),
    (
        "Personality disorder treatment requires longer-term approaches addressing enduring patterns rather than acute "
        "symptoms, with strong therapeutic alliance as foundation."
    ),
    (
        "Mentalization-based treatment improves reflective functioning in personality disorders, developing capacity "
        "to understand behavior in terms of mental states."
    ),
    (
        "Transference-focused psychotherapy uses the therapeutic relationship to examine and modify the distorted "
        "internal object relations underlying personality pathology."
    ),
    (
        "Schema therapy integrates cognitive-behavioral, attachment, and experiential approaches to address early "
        "maladaptive schemas and modes in personality disorders."
    ),
    (
        "The alternative model for personality disorders in DSM five emphasizes impairments in self and interpersonal "
        "functioning alongside pathological traits."
    ),
    (
        "Identity disturbance in borderline presentation involves unstable self-image, chronic emptiness, and "
        "difficulty maintaining consistent sense of self across contexts."
    ),
    (
        "Emotional dysregulation represents the core feature of borderline pathology, with intense rapidly shifting "
        "emotions and difficulty returning to baseline."
    ),
    (
        "Idealization and devaluation cycles characterize borderline relationships, with partners alternately seen as "
        "perfect or terrible based on perceived abandonment cues."
    ),
    (
        "Self-destructive behaviors in borderline presentations often regulate overwhelming emotions, communicate "
        "distress, or manage dissociative experiences through physical grounding."
    ),
    (
        "Chronic suicidality requires careful balance between taking risk seriously and avoiding inadvertent "
        "reinforcement of suicidal behavior as primary communication mode."
    ),
]

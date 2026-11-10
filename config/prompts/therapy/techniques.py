"""Therapy prompts about the therapeutic relationship, specific populations, and techniques."""

from __future__ import annotations

TECHNIQUES: list[str] = [
    # LONG PROMPTS - THERAPEUTIC RELATIONSHIP & PROCESS
    (
        "The therapeutic alliance encompasses agreement on goals, agreement on tasks, and the emotional bond between "
        "therapist and client, predicting outcomes across approaches."
    ),
    (
        "Rupture and repair in the alliance are inevitable and potentially growth-producing when addressed directly, "
        "modeling healthy relational conflict resolution."
    ),
    (
        "Empathy involves accurately understanding the client's internal frame of reference and communicating this "
        "understanding in a way that feels understood."
    ),
    (
        "Therapeutic presence means being fully in the moment with the client, bringing one's whole self while "
        "remaining focused on the client's experience."
    ),
    (
        "Boundaries in therapy protect the therapeutic frame and relationship, creating safety through predictability "
        "and appropriate limits on the relationship."
    ),
    (
        "Self-disclosure by therapists can enhance connection or burden clients, requiring careful consideration of "
        "purpose and likely impact."
    ),
    (
        "Parallel process occurs when dynamics from supervision or therapy replicate in the other relationship, "
        "providing useful clinical information."
    ),
    (
        "Resistance may signal that therapy is approaching important material, relationship rupture exists, or the "
        "approach needs adjustment."
    ),
    (
        "Therapeutic neutrality creates space for client material without therapist agenda, though contemporary views "
        "recognize neutrality as impossible and potentially harmful."
    ),
    (
        "The corrective emotional experience provides new relational experiences that disconfirm maladaptive "
        "expectations formed in earlier relationships."
    ),
    (
        "Therapist factors including warmth, genuineness, and skillful responsiveness contribute significantly to "
        "outcomes across theoretical orientations."
    ),
    (
        "Common factors shared across therapies include the alliance, expectancy effects, rituals and procedures, and "
        "extratherapeutic change factors."
    ),
    (
        "Deliberate practice improves therapist effectiveness through focused attention on skill development with "
        "feedback, challenging comfortable competence."
    ),
    (
        "Multicultural competence requires awareness of own biases, knowledge of diverse groups, and skills in "
        "culturally responsive intervention."
    ),
    (
        "Power dynamics in therapy require attention, particularly across differences in social identities and the "
        "inherent power imbalance in the helping relationship."
    ),
    (
        "Microaggressions in therapy cause harm through subtle communications of bias, requiring therapist "
        "self-awareness and willingness to address ruptures."
    ),
    (
        "Termination is a significant phase of therapy that activates attachment patterns and requires processing of "
        "gains, losses, and endings."
    ),
    (
        "Premature termination often indicates alliance rupture, practical barriers, or symptomatic improvement that "
        "may not be sustained."
    ),
    (
        "Therapy interfering behaviors obstruct treatment progress, requiring direct address and potentially becoming "
        "primary treatment focus."
    ),
    (
        "Treatment planning collaboratively establishes goals, identifies interventions, and creates measurable "
        "outcomes to guide therapeutic work."
    ),
    # LONG PROMPTS - SPECIALIZED POPULATIONS & ISSUES
    (
        "Adverse childhood experiences create dose-response relationships with adult health outcomes, with more ACE "
        "categories predicting greater physical and mental health problems."
    ),
    (
        "Developmental trauma in early childhood affects brain development, attachment, emotional regulation, and "
        "sense of self, requiring specialized treatment approaches."
    ),
    (
        "Complex grief involves prolonged intense mourning with yearning, identity confusion, and difficulty accepting "
        "death that impairs functioning beyond normal bereavement."
    ),
    (
        "Prolonged grief disorder now has diagnostic recognition in DSM five TR, validating the distinct clinical "
        "presentation requiring specific treatment."
    ),
    (
        "Eating disorder treatment addresses restrictive, binge, and compensatory behaviors alongside underlying "
        "emotional regulation, identity, and relational issues."
    ),
    (
        "Body dysmorphic disorder involves preoccupation with perceived appearance flaws not observable or slight to "
        "others, causing significant distress and ritualistic behaviors."
    ),
    (
        "Substance use disorders involve compulsive use despite consequences, with tolerance, withdrawal, and cravings "
        "disrupting functioning across life domains."
    ),
    (
        "Motivational interviewing enhances intrinsic motivation for change through expressing empathy, developing "
        "discrepancy, rolling with resistance, and supporting self-efficacy."
    ),
    (
        "The stages of change model describes precontemplation, contemplation, preparation, action, and maintenance as "
        "phases of behavior change, guiding intervention selection."
    ),
    (
        "Harm reduction approaches prioritize reducing negative consequences of behaviors rather than requiring "
        "abstinence, meeting clients where they are."
    ),
    (
        "Dual diagnosis treatment integrates mental health and substance use interventions, recognizing their "
        "bidirectional relationship and need for coordinated care."
    ),
    (
        "Chronic pain treatment addresses the biopsychosocial factors maintaining pain and disability, often using "
        "acceptance-based approaches to improve functioning."
    ),
    (
        "Pain catastrophizing involves rumination, magnification, and helplessness about pain that amplify suffering "
        "and disability beyond nociceptive input."
    ),
    (
        "Pediatric psychology addresses the psychological aspects of illness, treatment adherence, family adjustment, "
        "and developmental impacts of medical conditions in children."
    ),
    (
        "Health psychology applies psychological principles to health behavior change, chronic disease management, and "
        "the psychophysiology of stress and illness."
    ),
    (
        "Neuropsychological rehabilitation addresses cognitive, emotional, and behavioral changes following brain "
        "injury through compensation strategies and direct remediation."
    ),
    (
        "Geriatric psychology specializes in aging-related concerns including cognitive decline, late-life depression, "
        "grief, medical comorbidity, and end-of-life issues."
    ),
    (
        "Perinatal mental health addresses mood and anxiety disorders during pregnancy and postpartum, with "
        "implications for maternal and infant outcomes."
    ),
    (
        "Cultural adaptation of evidence-based treatments tailors interventions to client cultural backgrounds while "
        "maintaining core active ingredients."
    ),
    (
        "LGBTQ affirmative therapy validates diverse gender identities and sexual orientations while addressing "
        "minority stress and its psychological impacts."
    ),
    # LONG PROMPTS - THERAPEUTIC TECHNIQUES
    (
        "Grounding techniques bring attention to present sensory experience, helping clients return from dissociation, "
        "flashbacks, or overwhelming emotion to here-and-now awareness."
    ),
    (
        "The five-four-three-two-one technique engages all senses by noticing five things seen, four heard, three "
        "touched, two smelled, and one tasted."
    ),
    (
        "Progressive muscle relaxation systematically tenses and releases muscle groups, reducing physical tension and "
        "activating the parasympathetic nervous system relaxation response."
    ),
    (
        "Diaphragmatic breathing activates the vagus nerve and parasympathetic response through slow deep breaths that "
        "expand the belly rather than chest."
    ),
    (
        "Imagery rescripting transforms traumatic or distressing memories by introducing protective figures, different "
        "outcomes, or adult self intervention into visualized scenes."
    ),
    (
        "Safe place visualization creates an internal resource of imagined safety that can be accessed during distress "
        "or as preparation for trauma work."
    ),
    (
        "The affect bridge uses current emotional experience to access earlier memories when similar feelings "
        "occurred, connecting present reactions to past origins."
    ),
    (
        "Two-chair work in Gestalt therapy facilitates dialogue between conflicting parts of self or between self and "
        "others through externalization in empty chairs."
    ),
    (
        "Role reversal has clients take the perspective of significant others, promoting mentalization and "
        "understanding of different viewpoints in relational conflicts."
    ),
    (
        "Behavioral rehearsal practices new skills and responses in session before attempting them in real situations, "
        "building confidence and competence."
    ),
    (
        "Systematic desensitization pairs relaxation with progressively feared stimuli, counter-conditioning the "
        "anxiety response through graduated exposure."
    ),
    (
        "In vivo exposure confronts feared situations in real life, providing direct disconfirmation of catastrophic "
        "predictions and habituation of anxiety."
    ),
    (
        "Virtual reality exposure creates immersive simulations of feared situations for treatment of phobias, PTSD, "
        "and other anxiety conditions."
    ),
    (
        "The worry postponement technique schedules specific times for worry, training clients to set aside anxious "
        "thoughts and return to them later."
    ),
    (
        "Activity scheduling increases behavioral activation through planned activities, counteracting depressive "
        "withdrawal and building opportunities for mastery and pleasure."
    ),
    (
        "Pleasant event scheduling deliberately increases positive experiences to improve mood, recognizing the "
        "reciprocal relationship between activity and depression."
    ),
    (
        "Problem-solving therapy teaches structured approach to difficulties through defining problems, generating "
        "solutions, evaluating options, and implementing chosen approaches."
    ),
    (
        "Motivational enhancement develops discrepancy between current behavior and stated values, building intrinsic "
        "motivation for change through guided self-exploration."
    ),
    (
        "Miracle question invites clients to describe life without the problem, clarifying goals and identifying small "
        "steps toward preferred futures."
    ),
    (
        "Exception-finding identifies times when problems were absent or managed better, discovering existing "
        "strengths and solutions to amplify."
    ),
]

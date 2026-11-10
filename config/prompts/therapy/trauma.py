"""Therapy prompts about trauma treatment, dialectical behavior therapy, and parts work."""

from __future__ import annotations

TRAUMA: list[str] = [
    # LONG PROMPTS - TRAUMA & PTSD TREATMENT
    (
        "Post-traumatic stress disorder develops following exposure to actual or threatened death, serious injury, or "
        "sexual violence, manifesting through intrusions, avoidance, negative cognitions, and hyperarousal."
    ),
    (
        "Trauma-informed care recognizes the widespread impact of trauma and integrates knowledge about trauma into "
        "policies, procedures, and practices to avoid retraumatization."
    ),
    (
        "The window of tolerance describes the optimal zone of arousal where emotions can be experienced and processed "
        "without overwhelming the nervous system's regulatory capacity."
    ),
    (
        "Hyperarousal involves sympathetic nervous system activation with increased heart rate, hypervigilance, "
        "exaggerated startle response, and difficulty sleeping or concentrating following trauma."
    ),
    (
        "Hypoarousal represents parasympathetic dominance with emotional numbing, disconnection from body, decreased "
        "heart rate, and collapse responses following overwhelming threat."
    ),
    (
        "Emotional flashbacks involve intense emotional states from past trauma without visual imagery, often "
        "misidentified as current emotional reactions rather than trauma responses."
    ),
    (
        "Somatic experiencing addresses trauma through the body, completing interrupted defensive responses and "
        "discharging trapped survival energy through titrated pendulation and resourcing."
    ),
    (
        "EMDR therapy processes traumatic memories through bilateral stimulation while accessing the trauma network, "
        "facilitating adaptive information processing and reducing emotional disturbance."
    ),
    (
        "The adaptive information processing model suggests trauma memories become maladaptively stored, disconnected "
        "from adaptive memory networks, and EMDR facilitates proper integration."
    ),
    (
        "Titration in trauma therapy involves approaching traumatic material in small manageable doses, preventing "
        "overwhelm and maintaining the client within their window of tolerance."
    ),
    (
        "Resourcing establishes internal and external supports that enhance capacity for trauma processing, including "
        "positive memories, safe places, and protective figures."
    ),
    (
        "Pendulation involves moving attention between activation and resource states, building capacity to tolerate "
        "distressing material while maintaining nervous system regulation."
    ),
    (
        "Complex PTSD results from prolonged interpersonal trauma, particularly in childhood, adding disturbances in "
        "self-organization including affect dysregulation, negative self-concept, and relational difficulties."
    ),
    (
        "Developmental trauma disrupts the formation of secure attachment, emotional regulation, and coherent sense of "
        "self, often presenting as personality pathology rather than PTSD."
    ),
    (
        "The polyvagal theory describes three hierarchical nervous system states: ventral vagal social engagement, "
        "sympathetic fight-flight, and dorsal vagal freeze-collapse responses."
    ),
    (
        "Neuroception is the unconscious process by which the nervous system evaluates environmental safety or danger, "
        "triggering appropriate autonomic responses without conscious awareness."
    ),
    (
        "The ventral vagal state supports social engagement through regulated heart rate, facial expressiveness, and "
        "prosodic voice, enabling connection and collaborative communication."
    ),
    (
        "Dorsal vagal shutdown represents the most primitive survival response, involving immobilization, metabolic "
        "conservation, and dissociation when fight or flight is impossible."
    ),
    (
        "Co-regulation describes how regulated nervous systems help dysregulated ones return to balance through "
        "attuned presence, modeling, and interpersonal neurobiological synchrony."
    ),
    (
        "Intergenerational trauma transmits traumatic effects across generations through epigenetic changes, "
        "attachment patterns, parenting behaviors, and family narratives about historical events."
    ),
    (
        "Moral injury results from actions or inactions that violate deeply held moral beliefs, creating guilt, shame, "
        "and existential distress distinct from fear-based trauma."
    ),
    (
        "Traumatic grief combines trauma symptoms with bereavement, often following sudden violent death, complicating "
        "mourning through intrusions, avoidance, and ongoing threat perception."
    ),
    (
        "Dissociation serves a protective function during overwhelming experiences, separating aspects of experience "
        "from conscious awareness to preserve psychological functioning."
    ),
    (
        "Structural dissociation theory describes personality fragmentation following trauma, with apparently normal "
        "parts managing daily life and emotional parts holding traumatic memories."
    ),
    (
        "Parts work recognizes different aspects of self that developed to cope with difficult experiences, fostering "
        "internal communication, understanding, and integration."
    ),
    # LONG PROMPTS - DBT & EMOTION REGULATION
    (
        "Dialectical behavior therapy synthesizes change strategies with acceptance, addressing the dialectic between "
        "wanting to change and accepting oneself as fundamentally okay."
    ),
    (
        "The biosocial theory of borderline personality disorder describes emotional vulnerability interacting with "
        "invalidating environments, creating pervasive emotion dysregulation and identity disturbance."
    ),
    (
        "Emotion regulation skills help identify, understand, and modify emotional experiences through strategies like "
        "opposite action, checking facts, and building positive experiences."
    ),
    (
        "Distress tolerance skills help survive crisis situations without making them worse, using techniques like "
        "TIPP, distraction, self-soothing, and radical acceptance."
    ),
    (
        "Interpersonal effectiveness skills balance asking for needs, saying no, and maintaining relationships while "
        "preserving self-respect and relationship quality through assertive communication."
    ),
    (
        "Mindfulness in DBT involves observing, describing, and participating in present experience with "
        "non-judgmental awareness, effectiveness, and one-mindful attention."
    ),
    (
        "Wise mind integrates emotional mind and reasonable mind, accessing intuitive knowing that honors both logic "
        "and emotion in decision-making."
    ),
    (
        "Radical acceptance involves fully accepting reality as it is without judgment, not approving of it but "
        "acknowledging it to reduce suffering."
    ),
    (
        "The DEAR MAN skill teaches assertive communication through describing situations, expressing feelings, "
        "asserting needs, reinforcing compliance, staying mindful, appearing confident, and negotiating."
    ),
    (
        "Opposite action involves doing the opposite of emotion-driven urges when the emotion does not fit facts or "
        "acting on it is unhelpful."
    ),
    (
        "The PLEASE skill maintains physical health through treating physical illness, balanced eating, avoiding "
        "mood-altering substances, balanced sleep, and exercise."
    ),
    (
        "Chain analysis examines the sequence of events, vulnerabilities, thoughts, feelings, and behaviors leading to "
        "problematic outcomes, identifying intervention points."
    ),
    (
        "Validation in DBT involves acknowledging the client's experience as understandable given their history and "
        "current context, reducing emotional intensity."
    ),
    (
        "Irreverent communication uses unexpected or humorous responses to shift rigid thinking patterns and break "
        "therapeutic impasses with genuine but provocative interventions."
    ),
    (
        "Walking the middle path involves dialectical thinking that embraces both-and rather than either-or, "
        "validating while also encouraging change."
    ),
    (
        "Interpersonal sensitivity in borderline presentation involves intense fear of abandonment, unstable "
        "relationships, and difficulty reading social cues accurately."
    ),
    (
        "Emotion cascades describe rapid escalation of emotional intensity where one emotion triggers another in a "
        "self-amplifying spiral of distress."
    ),
    (
        "The ABC PLEASE skill builds mastery and positive emotions through accumulating positives, building mastery, "
        "coping ahead, and maintaining physical health."
    ),
    (
        "Self-invalidation involves dismissing, minimizing, or criticizing one's own emotional experiences, "
        "perpetuating the invalidating environment internally."
    ),
    (
        "Apparent competence describes the disconnect between seeming capable externally while experiencing "
        "significant internal distress and difficulty functioning."
    ),
    # LONG PROMPTS - IFS & PARTS WORK
    (
        "Internal Family Systems therapy views the psyche as containing multiple parts or subpersonalities, each with "
        "its own perspective, feelings, memories, and role in the system."
    ),
    (
        "The Self in IFS represents the core essence characterized by compassion, curiosity, clarity, calmness, "
        "confidence, courage, creativity, and connectedness that leads healing."
    ),
    (
        "Exiles are wounded parts carrying the pain of traumatic or difficult experiences, often young and frozen in "
        "time at the age of injury."
    ),
    (
        "Managers are protective parts that preemptively control and organize to prevent exile pain from emerging, "
        "often through perfectionism, caretaking, or intellectualizing."
    ),
    (
        "Firefighters are reactive protective parts that extinguish emotional pain through impulsive behaviors like "
        "substance use, self-harm, dissociation, or rage outbursts."
    ),
    (
        "Unburdening in IFS releases the extreme beliefs and feelings parts have carried, often through imagery of "
        "releasing into elements like light, water, or earth."
    ),
    (
        "Retrieval brings exiled parts out of the past traumatic scene into the present, where the Self can provide "
        "what was needed then."
    ),
    (
        "The protector-exile system describes how managers and firefighters work to contain exile pain, often creating "
        "symptoms that bring people to therapy."
    ),
    (
        "Blending occurs when a part's feelings and beliefs merge with Self-consciousness, losing the separateness "
        "needed for Self-leadership and healing."
    ),
    (
        "Unblending involves creating space between Self and parts, restoring the observer perspective necessary for "
        "compassionate curiosity toward internal experience."
    ),
    (
        "Trailheads are entry points into the internal system through body sensations, emotions, thoughts, or "
        "behaviors that lead to discovering parts."
    ),
    (
        "Direct access involves speaking to parts directly in imagery while in-sight accesses parts' perspectives "
        "through the client's felt sense."
    ),
    (
        "Polarization describes parts in conflict with each other, often a protector fighting another protector with "
        "the exile's pain driving both."
    ),
    (
        "Legacy burdens are beliefs and emotions passed down through families and cultures that parts carry without "
        "direct personal experience."
    ),
    (
        "Self-energy healing occurs when parts experience the Self's compassionate presence, often producing shifts in "
        "perspective and reduced protective extremity."
    ),
    (
        "The eight C's of Self-leadership include calm, curiosity, clarity, compassion, confidence, courage, "
        "creativity, and connectedness as qualities indicating Self-access."
    ),
    (
        "Parts detection involves noticing internal reactions, bodily sensations, and the multiplicity of responses to "
        "situations that indicate different parts activating."
    ),
    (
        "Protector fears often involve concerns that without their protective role, the system will be overwhelmed by "
        "exile pain or repeat past harm."
    ),
    (
        "Updating parts involves helping protectors and exiles recognize that circumstances have changed, the person "
        "has grown, and new options exist."
    ),
    (
        "Hope merchants are parts that promise exiles relief through behaviors that ultimately increase pain, "
        "requiring careful work to find alternatives."
    ),
]

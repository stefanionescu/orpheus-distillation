"""Biology prompts of thirty to thirty-seven words on senses, disease, plants, and development."""

from __future__ import annotations

ECOLOGY: list[str] = [
    (
        "Osteoporosis results from imbalance between bone resorption and formation, decreasing bone density and "
        "increasing fracture risk, especially postmenopausally."
    ),
    (
        "Hematopoiesis produces blood cells from multipotent stem cells in bone marrow, with lineage commitment "
        "directed by transcription factors and growth factors."
    ),
    (
        "Platelets are anucleate cell fragments from megakaryocytes that initiate hemostasis through adhesion, "
        "activation, and aggregation at sites of vascular injury."
    ),
    (
        "Erythropoiesis is stimulated by erythropoietin from kidneys in response to hypoxia, increasing red blood cell "
        "production to improve oxygen carrying capacity."
    ),
    (
        "Photoreception occurs in rod and cone cells of the retina, with rhodopsin and cone opsins initiating "
        "phototransduction cascades in response to light."
    ),
    (
        "Mechanoreception in the cochlea involves hair cell deflection by sound waves, generating receptor potentials "
        "transmitted by auditory nerve to brain."
    ),
    (
        "Olfactory receptors are G protein coupled receptors in nasal epithelium, with each neuron expressing one "
        "receptor type from over 400 genes."
    ),
    (
        "Taste reception involves five basic modalities detected by taste receptor cells in taste buds, signaling "
        "through ion channels and G protein receptors."
    ),
    (
        "Proprioception provides information about body position through muscle spindles, Golgi tendon organs, and "
        "joint receptors, essential for motor control."
    ),
    (
        "The vestibular system detects head position and movement through semicircular canals and otolith organs, "
        "essential for balance and gaze stabilization."
    ),
    (
        "Long term potentiation strengthens synaptic connections through repeated stimulation, involving NMDA receptor "
        "activation and AMPA receptor insertion in postsynaptic membranes."
    ),
    (
        "Memory consolidation transfers information from hippocampus to neocortex during sleep, with different systems "
        "mediating declarative and procedural memory storage."
    ),
    (
        "Neurodegenerative diseases like Alzheimer's and Parkinson's involve protein aggregation, neuronal death, and "
        "progressive cognitive or motor decline."
    ),
    (
        "Alzheimer's disease is characterized by amyloid plaques and neurofibrillary tangles, with progressive memory "
        "loss and cognitive decline affecting millions worldwide."
    ),
    (
        "Parkinson's disease results from dopaminergic neuron loss in substantia nigra, causing tremor, rigidity, and "
        "bradykinesia, with alpha synuclein aggregation."
    ),
    (
        "Multiple sclerosis involves autoimmune demyelination of central nervous system axons, causing relapsing "
        "remitting or progressive neurological symptoms."
    ),
    (
        "Stroke results from ischemic or hemorrhagic interruption of brain blood supply, causing neuronal death and "
        "neurological deficits requiring urgent treatment."
    ),
    (
        "Epilepsy involves recurrent seizures from abnormal synchronized neuronal activity, with various seizure types "
        "depending on affected brain regions."
    ),
    (
        "Plant hormones including auxin, cytokinin, gibberellin, abscisic acid, and ethylene regulate growth, "
        "development, and responses to environmental stimuli."
    ),
    (
        "Auxin promotes cell elongation and phototropism, synthesized in shoot tips and transported polarly to "
        "regulate apical dominance and root development."
    ),
    (
        "Phototropism involves asymmetric auxin distribution causing differential cell elongation, bending plant "
        "shoots toward light for optimal photosynthesis."
    ),
    (
        "Gravitropism orients plant growth relative to gravity, with statoliths in root cap cells detecting gravity "
        "and auxin redistribution directing growth."
    ),
    (
        "Photoperiodism regulates flowering in response to day length, with phytochrome detecting light quality and "
        "duration to trigger developmental transitions."
    ),
    (
        "Vernalization is cold treatment requirement for flowering in some plants, involving epigenetic silencing of "
        "flowering repressor genes."
    ),
    (
        "Abscission is programmed separation of leaves, flowers, and fruit, mediated by ethylene and auxin balance in "
        "the abscission zone."
    ),
    (
        "Senescence is programmed aging and death of plant organs, involving chlorophyll degradation, nutrient "
        "remobilization, and cell death pathways."
    ),
    (
        "Stomatal regulation controls gas exchange and water loss, with guard cells responding to light, carbon "
        "dioxide, and abscisic acid signals."
    ),
    (
        "The Casparian strip is a waterproof barrier in root endodermis, forcing water and solutes through symplastic "
        "pathway for selective uptake."
    ),
    (
        "Xylem transports water and minerals from roots to leaves through transpiration driven cohesion tension "
        "mechanism in dead vessel elements."
    ),
    (
        "Phloem transports sugars from source to sink tissues through pressure flow mechanism in living sieve tube "
        "elements with companion cells."
    ),
    (
        "Nitrogen assimilation converts nitrate to ammonia and incorporates it into amino acids through nitrate "
        "reductase and glutamine synthetase pathways."
    ),
    (
        "Secondary metabolites including alkaloids, terpenoids, and phenolics provide defense against herbivores and "
        "pathogens, with diverse pharmaceutical applications."
    ),
    (
        "Plant immunity involves pattern triggered immunity and effector triggered immunity, with hypersensitive "
        "response causing localized cell death to limit pathogen spread."
    ),
    (
        "Systemic acquired resistance provides whole plant immunity following local infection, mediated by salicylic "
        "acid signaling and pathogenesis related protein expression."
    ),
    (
        "Double fertilization in angiosperms produces zygote from egg and polar nuclei fusion produces triploid "
        "endosperm, providing nutrients for embryo development."
    ),
    (
        "Seed dormancy prevents germination under unfavorable conditions, with abscisic acid maintaining dormancy and "
        "gibberellin promoting germination when conditions improve."
    ),
    (
        "Fruit development involves ovary maturation after fertilization, with auxin and gibberellin promoting growth "
        "and ethylene triggering ripening in climacteric fruits."
    ),
    (
        "Alternation of generations in plants involves multicellular haploid gametophyte and diploid sporophyte "
        "stages, with relative dominance varying across plant groups."
    ),
    (
        "Bryophytes lack vascular tissue and are gametophyte dominant, requiring moist environments for flagellated "
        "sperm to swim to eggs."
    ),
    (
        "Pteridophytes have vascular tissue and are sporophyte dominant, with independent gametophytes producing "
        "swimming sperm requiring water for fertilization."
    ),
    (
        "Gymnosperms produce naked seeds in cones, with wind pollination and reduced gametophytes eliminating need for "
        "water in reproduction."
    ),
    (
        "Angiosperms produce seeds enclosed in fruits, with diverse floral adaptations for pollination by wind, water, "
        "insects, birds, and mammals."
    ),
    (
        "Pollination syndromes describe suites of floral traits attracting specific pollinators, with coevolution "
        "shaping flower color, scent, shape, and rewards."
    ),
    (
        "Seed dispersal mechanisms include wind, water, animal ingestion, animal attachment, and explosive dehiscence, "
        "enabling colonization of new habitats."
    ),
    (
        "Animal development proceeds through cleavage, gastrulation, and organogenesis, with cell fate determination "
        "by morphogen gradients and inductive interactions."
    ),
    (
        "Gastrulation establishes the three germ layers: ectoderm forming skin and nervous system, mesoderm forming "
        "muscle and skeleton, endoderm forming gut lining."
    ),
    (
        "Neural development involves neural tube formation, neuronal migration, axon guidance by chemoattractants and "
        "repellents, and synapse formation with target cells."
    ),
    (
        "Hox genes encode transcription factors that specify body segment identity along the anterior posterior axis, "
        "with colinear expression matching chromosomal order."
    ),
    (
        "Limb development involves apical ectodermal ridge, zone of polarizing activity, and signaling by FGF, Sonic "
        "hedgehog, and Wnt morphogens."
    ),
    (
        "Regeneration replaces lost body parts in some animals, with planarians, salamanders, and zebrafish having "
        "remarkable regenerative abilities involving dedifferentiation."
    ),
    (
        "Metamorphosis transforms larval to adult body plan, with hormone signaling triggering tissue remodeling, "
        "apoptosis, and new structure development."
    ),
    (
        "Arthropod molting involves ecdysone signaling, cuticle synthesis, and shedding of exoskeleton, enabling "
        "growth in animals with rigid external skeletons."
    ),
    (
        "Insect metamorphosis includes complete metamorphosis with distinct larva, pupa, and adult stages, and "
        "incomplete metamorphosis with gradual development."
    ),
    (
        "Sex determination mechanisms include chromosomal systems like XY and ZW, environmental determination in "
        "reptiles, and haplodiploidy in hymenopterans."
    ),
    (
        "Genomic imprinting silences genes based on parental origin through DNA methylation, with imprinted genes "
        "important in growth regulation."
    ),
    (
        "X chromosome inactivation equalizes gene dosage between sexes through random silencing of one X chromosome in "
        "female mammals, forming Barr bodies."
    ),
    (
        "Mosaicism results from mutations occurring during development, producing genetically distinct cell "
        "populations within a single organism."
    ),
    (
        "Teratogenesis is abnormal development caused by environmental agents including drugs, infections, and "
        "radiation, with critical periods of vulnerability."
    ),
]

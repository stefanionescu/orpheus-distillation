"""Biology prompts: short exclamations, then the first long prompts of thirty to thirty-seven words."""

from __future__ import annotations

PHYSIOLOGY: list[str] = [
    # SHORT EXCLAMATIONS
    "The cell is dividing rapidly!",
    "Incredible genetic diversity here!",
    "The enzyme activity is optimal!",
    "Photosynthesis is producing oxygen!",
    "The neuron just fired!",
    "Amazing bioluminescence display!",
    "The immune response is strong!",
    "Protein folding is complete!",
    "The mutation is beneficial!",
    "Symbiosis is thriving here!",
    "The ecosystem is balanced!",
    "Mitochondria are multiplying!",
    "The genome is fully sequenced!",
    "Evolution in action!",
    "The species is adapting!",
    "Camouflage is perfect!",
    "The population is growing exponentially!",
    "Metamorphosis is complete!",
    "The heart is beating strongly!",
    "Neural plasticity is remarkable!",
    "The antibody bound specifically!",
    "Gene expression is upregulated!",
    "The ribosome is translating!",
    "Chlorophyll is absorbing light!",
    "The action potential propagated!",
    "Meiosis produced four gametes!",
    "The zygote is developing!",
    "Stem cells are differentiating!",
    "The tumor is regressing!",
    "Homeostasis is maintained!",
    "The vaccine worked!",
    "Biodiversity is flourishing!",
    "The ecosystem recovered!",
    "Natural selection is occurring!",
    "The species diverged!",
    "Convergent evolution observed!",
    "The fossil record is complete!",
    "Transgenic organism created!",
    "CRISPR edit successful!",
    "The organism is bioluminescent!",
    "Endosymbiosis confirmed!",
    "The bacterium is nitrogen fixing!",
    "Horizontal gene transfer detected!",
    "The virus mutated!",
    "Antibiotic resistance emerged!",
    "The prion is infectious!",
    "Biofilm formation observed!",
    "Quorum sensing activated!",
    "The microbiome is diverse!",
    "Epigenetic modification confirmed!",
    # LONG PROMPTS 30-37 WORDS
    (
        "The mitochondrion is the powerhouse of the cell, generating ATP through oxidative phosphorylation in the "
        "inner membrane cristae, with its own circular DNA encoding essential respiratory chain components."
    ),
    (
        "DNA replication is semiconservative, with each strand serving as template for synthesis of a new "
        "complementary strand by DNA polymerase, proceeding bidirectionally from multiple origins."
    ),
    (
        "The central dogma of molecular biology describes information flow from DNA to RNA through transcription, and "
        "from RNA to protein through translation at ribosomes."
    ),
    (
        "Messenger RNA carries genetic information from nucleus to cytoplasm, where ribosomes read codons and transfer "
        "RNA brings corresponding amino acids for protein synthesis."
    ),
    (
        "The lac operon in Escherichia coli is regulated by the lac repressor protein, which binds the operator and "
        "blocks transcription until lactose induces conformational change."
    ),
    (
        "CRISPR Cas9 gene editing uses guide RNA to direct the Cas9 nuclease to specific DNA sequences, creating "
        "double strand breaks that enable precise genome modification."
    ),
    (
        "Epigenetic modifications like DNA methylation and histone acetylation alter gene expression without changing "
        "the underlying DNA sequence, and can be inherited across generations."
    ),
    (
        "Telomeres are repetitive sequences at chromosome ends that shorten with each cell division, with telomerase "
        "enzyme maintaining telomere length in stem cells and cancer cells."
    ),
    (
        "The cell cycle is regulated by cyclin dependent kinases and their cyclin partners, with checkpoints ensuring "
        "proper DNA replication and chromosome segregation before division."
    ),
    (
        "Apoptosis is programmed cell death mediated by caspase enzymes, eliminating damaged or unnecessary cells "
        "while avoiding inflammation that occurs during necrotic cell death."
    ),
    (
        "The sodium potassium ATPase pump maintains electrochemical gradients across cell membranes by transporting "
        "three sodium ions out and two potassium ions into cells."
    ),
    (
        "Action potentials propagate along neurons through voltage gated sodium and potassium channels, with "
        "depolarization triggering channel opening in adjacent membrane regions."
    ),
    (
        "Synaptic transmission involves calcium triggered neurotransmitter release from presynaptic vesicles, "
        "diffusion across the synaptic cleft, and binding to postsynaptic receptors."
    ),
    (
        "The blood brain barrier consists of tight junctions between endothelial cells, restricting passage of "
        "molecules from blood into brain tissue to maintain neural homeostasis."
    ),
    (
        "Hemoglobin exhibits cooperative binding of oxygen, with each bound oxygen molecule increasing affinity for "
        "subsequent oxygen molecules, producing the sigmoidal oxygen dissociation curve."
    ),
    (
        "The adaptive immune system generates specific responses through clonal selection of lymphocytes, with B cells "
        "producing antibodies and T cells mediating cellular immunity."
    ),
    (
        "Major histocompatibility complex molecules present peptide antigens on cell surfaces, with class I molecules "
        "presenting to cytotoxic T cells and class II to helper T cells."
    ),
    (
        "Antibodies are immunoglobulin proteins with variable regions that recognize specific epitopes, and constant "
        "regions that determine effector functions like complement activation and opsonization."
    ),
    (
        "Vaccines stimulate immune memory by presenting antigens without causing disease, enabling rapid secondary "
        "immune responses upon subsequent exposure to pathogens."
    ),
    (
        "Autoimmune diseases occur when the immune system attacks self tissues, with examples including rheumatoid "
        "arthritis, multiple sclerosis, type one diabetes, and lupus."
    ),
    (
        "The hypothalamus pituitary axis regulates endocrine function, with hypothalamic releasing hormones "
        "controlling pituitary hormone secretion that targets peripheral endocrine glands."
    ),
    (
        "Insulin and glucagon regulate blood glucose through opposing actions, with insulin promoting glucose uptake "
        "and storage while glucagon stimulates glycogenolysis and gluconeogenesis."
    ),
    (
        "Thyroid hormones regulate metabolism through nuclear receptors that control gene expression, with the "
        "hypothalamus pituitary thyroid axis maintaining homeostatic hormone levels."
    ),
    (
        "Steroid hormones are synthesized from cholesterol and act through intracellular receptors that function as "
        "transcription factors, regulating gene expression in target cells."
    ),
    (
        "The menstrual cycle is regulated by fluctuating levels of follicle stimulating hormone, luteinizing hormone, "
        "estrogen, and progesterone, controlling ovulation and uterine changes."
    ),
    (
        "Fertilization involves sperm capacitation, acrosome reaction, zona pellucida binding, and fusion with the "
        "oocyte membrane, triggering cortical reaction that prevents polyspermy."
    ),
    (
        "Embryonic development proceeds through cleavage, gastrulation, and organogenesis, with cell fate determined "
        "by morphogen gradients and differential gene expression patterns."
    ),
    (
        "Stem cells maintain self renewal capacity and pluripotency through expression of transcription factors like "
        "Oct4, Sox2, and Nanog, enabling differentiation into specialized cell types."
    ),
    (
        "Induced pluripotent stem cells are generated by reprogramming somatic cells through expression of Yamanaka "
        "factors, providing patient specific cells for regenerative medicine."
    ),
    (
        "Cancer results from accumulated mutations in oncogenes and tumor suppressor genes, enabling uncontrolled "
        "proliferation, evasion of apoptosis, angiogenesis, and metastasis."
    ),
    (
        "The tumor microenvironment includes stromal cells, immune cells, and extracellular matrix that interact with "
        "cancer cells to promote or inhibit tumor growth and metastasis."
    ),
    (
        "Angiogenesis is stimulated by vascular endothelial growth factor secreted by tumors, enabling blood vessel "
        "formation that supplies nutrients and oxygen for tumor growth."
    ),
    (
        "Metastasis involves cancer cell invasion through basement membrane, intravasation into blood vessels, "
        "survival in circulation, extravasation, and colonization of distant organs."
    ),
    (
        "Darwin's theory of evolution by natural selection explains how heritable variation and differential "
        "reproductive success lead to adaptation and speciation over generations."
    ),
    (
        "Phylogenetic trees represent evolutionary relationships inferred from morphological and molecular data, with "
        "branching patterns indicating common ancestry and divergence times."
    ),
    (
        "Molecular clocks use mutation rates in DNA sequences to estimate divergence times between species, calibrated "
        "with fossil evidence to construct evolutionary timelines."
    ),
    (
        "Homologous structures share common evolutionary origin despite different functions, while analogous "
        "structures have similar functions but evolved independently through convergent evolution."
    ),
    (
        "The endosymbiotic theory explains mitochondrial and chloroplast origins from ancient bacterial endosymbionts, "
        "supported by their double membranes, circular DNA, and bacterial ribosomes."
    ),
    (
        "Horizontal gene transfer enables genetic exchange between unrelated organisms, especially common in bacteria "
        "through transformation, transduction, and conjugation mechanisms."
    ),
    (
        "Population genetics studies allele frequency changes in populations, with Hardy Weinberg equilibrium "
        "describing conditions where frequencies remain stable across generations."
    ),
    (
        "Genetic drift causes random allele frequency changes in small populations, with founder effects and "
        "bottlenecks reducing genetic diversity and enabling fixation of alleles."
    ),
    (
        "Kin selection explains altruistic behavior through inclusive fitness, where organisms sacrifice individual "
        "fitness to increase reproductive success of genetically related individuals."
    ),
    (
        "Ecological succession describes community changes over time, from pioneer species colonization through "
        "intermediate stages to climax community establishment and stability."
    ),
    (
        "Keystone species have disproportionate effects on ecosystem structure relative to their abundance, with their "
        "removal causing cascading changes throughout the community."
    ),
    (
        "Trophic cascades occur when predator effects propagate down food chains, with classic examples including sea "
        "otter kelp forest and wolf Yellowstone ecosystem interactions."
    ),
    (
        "Nitrogen fixation converts atmospheric nitrogen to ammonia by nitrogenase enzyme in bacteria, with rhizobia "
        "forming symbiotic nodules on legume roots for mutual benefit."
    ),
    (
        "Eutrophication results from excess nutrient input to aquatic systems, causing algal blooms, oxygen depletion, "
        "and ecosystem disruption through altered species compositions."
    ),
    (
        "The greenhouse effect traps infrared radiation through atmospheric gases, with increasing carbon dioxide from "
        "fossil fuel combustion causing global climate change."
    ),
    (
        "Ocean acidification results from carbon dioxide absorption, decreasing pH and carbonate ion availability, "
        "threatening calcifying organisms like corals, mollusks, and foraminifera."
    ),
    (
        "Coral bleaching occurs when stressed corals expel symbiotic zooxanthellae algae, losing their color and "
        "primary energy source, often leading to mortality."
    ),
    (
        "The ozone layer absorbs ultraviolet radiation, with chlorofluorocarbons causing stratospheric ozone depletion "
        "and increased UV reaching Earth's surface, damaging DNA and causing cancer."
    ),
    (
        "Invasive species disrupt native ecosystems by outcompeting endemic organisms, with examples including zebra "
        "mussels, kudzu, cane toads, and brown tree snakes."
    ),
    (
        "Conservation biology applies ecological and genetic principles to protect biodiversity, including habitat "
        "preservation, population management, and captive breeding programs."
    ),
    (
        "The sixth mass extinction is driven by human activities including habitat destruction, overexploitation, "
        "pollution, invasive species, and climate change, threatening global biodiversity."
    ),
    (
        "Ecosystem services include provisioning of food and water, regulation of climate and disease, cultural "
        "benefits, and supporting services like nutrient cycling."
    ),
    (
        "The microbiome comprises trillions of microorganisms inhabiting the human body, influencing digestion, "
        "immunity, metabolism, and even brain function through the gut brain axis."
    ),
    (
        "Probiotics are beneficial bacteria that colonize the gut and provide health benefits, while prebiotics are "
        "dietary fibers that promote growth of beneficial microbes."
    ),
    (
        "Antibiotic resistance evolves through natural selection of bacteria with resistance genes, spread by "
        "horizontal gene transfer, creating multidrug resistant superbugs threatening public health."
    ),
    (
        "Bacteriophages are viruses that infect bacteria, with lytic cycles destroying host cells and lysogenic cycles "
        "integrating viral DNA into bacterial chromosomes."
    ),
    (
        "Prions are misfolded proteins that propagate by inducing normal proteins to adopt abnormal conformations, "
        "causing fatal neurodegenerative diseases like Creutzfeldt Jakob disease."
    ),
    (
        "Biofilms are structured microbial communities attached to surfaces, protected by extracellular polymeric "
        "substances that confer antibiotic resistance and persistence."
    ),
]

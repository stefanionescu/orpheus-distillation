"""Chemistry prompts of thirty to thirty-seven words on equilibria, biochemistry, and analysis."""

from __future__ import annotations

ANALYSIS: list[str] = [
    (
        "Enzymes are biological catalysts with remarkable specificity, lowering activation energies through substrate "
        "binding at active sites and following Michaelis Menten kinetics."
    ),
    (
        "Homogeneous catalysis occurs when catalyst and reactants are in the same phase, while heterogeneous catalysis "
        "involves catalysts in different phases, typically solid catalysts."
    ),
    (
        "The equilibrium constant Keq equals products over reactants at equilibrium, each raised to stoichiometric "
        "coefficients, with large values favoring products and small values favoring reactants."
    ),
    (
        "The reaction quotient Q has the same form as the equilibrium constant but applies to any concentrations, with "
        "comparison to Keq predicting reaction direction."
    ),
    (
        "Temperature affects equilibrium position according to Le Chatelier's principle, with exothermic reactions "
        "shifting left and endothermic reactions shifting right upon heating."
    ),
    (
        "The common ion effect suppresses ionization of weak electrolytes when a common ion is added, shifting "
        "equilibrium according to Le Chatelier's principle."
    ),
    (
        "Solubility product Ksp describes the equilibrium between a sparingly soluble salt and its dissolved ions, "
        "with precipitation occurring when ion product exceeds Ksp."
    ),
    (
        "Complex ion formation increases solubility of slightly soluble salts by removing metal ions from solution "
        "through coordination with ligands like ammonia or cyanide."
    ),
    (
        "Coordination compounds contain central metal ions bonded to ligands through coordinate covalent bonds, with "
        "geometries determined by coordination number and ligand arrangement."
    ),
    (
        "Crystal field theory explains colors and magnetic properties of transition metal complexes through d orbital "
        "splitting in ligand fields, with strong field ligands causing larger splitting."
    ),
    (
        "Chelating ligands like EDTA form multiple bonds to metal ions, creating highly stable complexes used in water "
        "treatment, medicine, and analytical chemistry applications."
    ),
    (
        "Isomerism in coordination compounds includes geometric isomers like cis and trans forms, optical isomers that "
        "are non superimposable mirror images, and linkage isomers."
    ),
    (
        "Organic chemistry studies carbon compounds, with carbon's ability to form four covalent bonds and catenate "
        "creating enormous structural diversity in organic molecules."
    ),
    (
        "Functional groups determine chemical reactivity in organic molecules, with alcohols, aldehydes, ketones, "
        "carboxylic acids, amines, and others having characteristic reactions."
    ),
    (
        "Nomenclature of organic compounds follows IUPAC rules, naming the longest carbon chain as the parent and "
        "numbering substituents to give lowest locant numbers."
    ),
    (
        "Stereochemistry describes the three dimensional arrangement of atoms in molecules, with chirality arising "
        "from asymmetric carbon centers bearing four different substituents."
    ),
    (
        "Enantiomers are non superimposable mirror images with identical physical properties except for optical "
        "rotation direction and different biological activities in chiral environments."
    ),
    (
        "Diastereomers are stereoisomers that are not mirror images, having different physical properties and arising "
        "from molecules with multiple stereocenters or geometric isomerism."
    ),
    (
        "Conformational analysis examines rotation around single bonds, with staggered conformations being more stable "
        "than eclipsed due to reduced torsional strain and steric interactions."
    ),
    (
        "Substitution reactions replace one atom or group with another, with SN1 proceeding through carbocation "
        "intermediates and SN2 through concerted backside attack mechanisms."
    ),
    (
        "Elimination reactions remove atoms or groups to form double bonds, with E1 proceeding through carbocations "
        "and E2 through concerted anti periplanar elimination."
    ),
    (
        "Addition reactions add atoms or groups across double or triple bonds, with Markovnikov addition placing "
        "hydrogen on the more substituted carbon in unsymmetrical alkenes."
    ),
    (
        "Electrophilic aromatic substitution replaces hydrogen on benzene rings with electrophiles, with the mechanism "
        "involving sigma complex intermediates and restoration of aromaticity."
    ),
    (
        "Nucleophilic acyl substitution at carbonyl groups proceeds through tetrahedral intermediates, converting "
        "carboxylic acid derivatives like esters, amides, and acid chlorides."
    ),
    (
        "Aldol condensation joins two carbonyl compounds through nucleophilic addition of an enolate to another "
        "carbonyl, forming beta hydroxy carbonyl compounds that can dehydrate."
    ),
    (
        "Grignard reagents are organomagnesium compounds that act as nucleophiles and strong bases, reacting with "
        "carbonyl compounds to form alcohols after aqueous workup."
    ),
    (
        "Diels Alder reactions are pericyclic cycloadditions between conjugated dienes and dienophiles, forming six "
        "membered rings with predictable stereochemistry in one concerted step."
    ),
    (
        "Polymerization joins monomers into long chain polymers, with addition polymerization of alkenes and "
        "condensation polymerization releasing small molecules like water."
    ),
    (
        "Thermoplastics soften when heated and can be remolded, while thermosets undergo irreversible crosslinking "
        "during curing and cannot be remelted after setting."
    ),
    (
        "Biopolymers include proteins built from amino acids, nucleic acids built from nucleotides, and "
        "polysaccharides built from monosaccharides, each with specific biological functions."
    ),
    (
        "Protein structure includes primary sequence, secondary alpha helices and beta sheets, tertiary three "
        "dimensional folding, and quaternary multi subunit arrangements."
    ),
    (
        "Enzymes exhibit specificity through complementary active site shapes, with competitive inhibitors blocking "
        "active sites and noncompetitive inhibitors binding elsewhere to reduce activity."
    ),
    (
        "DNA replication is semiconservative, with each strand serving as template for synthesis of a new "
        "complementary strand by DNA polymerase following base pairing rules."
    ),
    (
        "Transcription copies DNA sequences into messenger RNA, which is then translated into protein sequences at "
        "ribosomes according to the genetic code triplet codons."
    ),
    (
        "Metabolism includes catabolic pathways that break down molecules to release energy and anabolic pathways that "
        "build complex molecules using energy from ATP hydrolysis."
    ),
    (
        "Glycolysis breaks down glucose to pyruvate in the cytoplasm, generating two ATP and two NADH molecules per "
        "glucose through a ten step enzyme catalyzed pathway."
    ),
    (
        "The citric acid cycle oxidizes acetyl CoA to carbon dioxide in mitochondria, generating NADH and FADH2 that "
        "feed into the electron transport chain."
    ),
    (
        "Oxidative phosphorylation couples electron transport to ATP synthesis through the chemiosmotic mechanism, "
        "with proton gradients driving ATP synthase to produce most cellular ATP."
    ),
    (
        "Photosynthesis light reactions capture solar energy to split water and generate ATP and NADPH, while dark "
        "reactions fix carbon dioxide into glucose."
    ),
    (
        "The Calvin cycle fixes carbon dioxide using ribulose bisphosphate carboxylase, reducing it to glyceraldehyde "
        "3 phosphate through a series of enzyme catalyzed reactions using ATP and NADPH."
    ),
    (
        "Fatty acid oxidation breaks down fats through beta oxidation, removing two carbon acetyl CoA units that enter "
        "the citric acid cycle for complete oxidation."
    ),
    (
        "Amino acid catabolism removes nitrogen through transamination and deamination, with carbon skeletons entering "
        "central metabolic pathways and nitrogen excreted as urea."
    ),
    (
        "Electrochemistry relates chemical reactions to electrical energy, with galvanic cells generating electricity "
        "from spontaneous reactions and electrolytic cells using electricity to drive reactions."
    ),
    (
        "Standard electrode potentials measure the tendency of half reactions to occur as reductions, with more "
        "positive values indicating stronger oxidizing agents."
    ),
    (
        "The hydrogen electrode is the reference standard with potential defined as zero volts, against which all "
        "other electrode potentials are measured."
    ),
    (
        "Battery chemistry includes lead acid cells with lead dioxide and lead electrodes, lithium ion cells with "
        "lithium cobalt oxide cathodes, and nickel metal hydride cells."
    ),
    (
        "Fuel cells convert chemical energy directly to electricity through electrochemical oxidation of fuels like "
        "hydrogen, with water as the only emission product."
    ),
    (
        "Corrosion prevention methods include protective coatings, cathodic protection with sacrificial anodes, "
        "passivation through oxide layers, and corrosion resistant alloy selection."
    ),
    (
        "Environmental chemistry studies chemical processes in air, water, and soil, including pollution, ozone "
        "depletion, acid rain, and greenhouse gas effects on climate."
    ),
    (
        "The ozone layer absorbs ultraviolet radiation, with chlorofluorocarbons catalytically destroying ozone "
        "through radical chain reactions releasing chlorine atoms repeatedly."
    ),
    (
        "Acid rain forms when sulfur dioxide and nitrogen oxides dissolve in atmospheric water, forming sulfuric and "
        "nitric acids that damage ecosystems and structures."
    ),
    (
        "The greenhouse effect traps infrared radiation through absorption by carbon dioxide, methane, and other "
        "gases, with anthropogenic emissions causing global climate change."
    ),
    (
        "Green chemistry principles minimize waste, use renewable feedstocks, design safer chemicals, and improve "
        "energy efficiency to reduce environmental impact of chemical processes."
    ),
    (
        "Analytical chemistry develops methods to identify and quantify chemical species, with qualitative analysis "
        "determining what is present and quantitative analysis determining how much."
    ),
    (
        "Gravimetric analysis determines analyte mass through precipitation, filtration, and weighing, with careful "
        "attention to stoichiometry and complete precipitation of the analyte."
    ),
    (
        "Volumetric analysis uses titration to determine concentrations, with indicators or instrumental methods "
        "detecting endpoints where stoichiometric amounts have reacted completely."
    ),
    (
        "Spectrophotometric analysis uses Beer's law relating absorbance to concentration, with calibration curves "
        "enabling quantitative determination of colored or absorbing species."
    ),
    (
        "Electroanalytical methods include potentiometry measuring voltage, voltammetry measuring current voltage "
        "relationships, and coulometry measuring total charge for quantitative analysis."
    ),
    (
        "Separation techniques like extraction, distillation, and chromatography isolate components from mixtures "
        "based on differences in physical and chemical properties."
    ),
    (
        "Quality control in analytical chemistry includes calibration, blanks, standards, replicates, and statistical "
        "analysis to ensure accuracy and precision of measurements."
    ),
    (
        "Significant figures and error propagation quantify uncertainty in measurements and calculations, with proper "
        "reporting essential for scientific communication and reproducibility."
    ),
    (
        "The scientific method in chemistry involves observation, hypothesis formation, experimental testing, data "
        "analysis, and theory development through iterative refinement."
    ),
    (
        "Laboratory safety requires proper handling of chemicals, use of personal protective equipment, understanding "
        "of hazards, and emergency procedures for accidents."
    ),
    (
        "Chemical waste disposal must follow regulations for hazardous materials, with proper segregation, labeling, "
        "storage, and treatment to protect health and environment."
    ),
    (
        "Industrial chemistry scales up laboratory processes to manufacturing, considering economics, safety, "
        "environmental impact, and engineering requirements for commercial production."
    ),
    (
        "Pharmaceutical chemistry designs and synthesizes drug molecules, optimizing potency, selectivity, "
        "pharmacokinetics, and safety through structure activity relationship studies."
    ),
    (
        "Materials chemistry develops new materials with tailored properties, including polymers, ceramics, "
        "semiconductors, nanomaterials, and composites for technological applications."
    ),
    (
        "Nanotechnology manipulates matter at the nanometer scale, with unique properties arising from high surface to "
        "volume ratios and quantum effects in nanoparticles."
    ),
    (
        "Supramolecular chemistry studies non covalent interactions between molecules, including host guest chemistry, "
        "self assembly, and molecular recognition for sensors and devices."
    ),
    (
        "Computational chemistry uses quantum mechanics and molecular mechanics to model molecular structures, "
        "properties, and reactions, guiding experimental work and interpretation."
    ),
]

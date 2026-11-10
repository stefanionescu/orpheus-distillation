"""Biology prompts of twenty to thirty-seven words on neuroscience and genetics."""

from __future__ import annotations

NEUROSCIENCE: list[str] = [
    # EXPANDED NEUROSCIENCE - 20-37 WORD SENTENCES
    (
        "Long term potentiation at glutamatergic synapses requires NMDA receptor activation, calcium influx triggering "
        "CaMKII autophosphorylation, AMPA receptor phosphorylation and trafficking to increase synaptic strength."
    ),
    (
        "The default mode network shows coordinated activity during rest and self referential thought, with hubs in "
        "medial prefrontal cortex, posterior cingulate, and angular gyrus."
    ),
    (
        "Dopaminergic projections from ventral tegmental area to nucleus accumbens encode reward prediction errors, "
        "with phasic firing signaling unexpected rewards and pauses indicating omitted expected rewards."
    ),
    (
        "Chandelier cells are GABAergic interneurons that form axo axonic synapses on pyramidal cell axon initial "
        "segments, powerfully controlling action potential initiation through inhibition."
    ),
    (
        "Place cells in hippocampal CA1 fire at specific spatial locations, while grid cells in entorhinal cortex show "
        "hexagonal firing patterns providing metric spatial representation."
    ),
    (
        "Sharp wave ripples during slow wave sleep replay compressed sequential neural patterns from waking "
        "experience, supporting memory consolidation through hippocampal cortical dialogue."
    ),
    (
        "The tripartite synapse includes presynaptic terminal, postsynaptic density, and perisynaptic astrocyte "
        "processes that modulate transmission through gliotransmitter release and neurotransmitter uptake."
    ),
    (
        "Spike timing dependent plasticity strengthens synapses when presynaptic firing precedes postsynaptic spikes "
        "within milliseconds, while reverse timing induces long term depression."
    ),
    (
        "Microglial cells survey the brain parenchyma with motile processes, pruning synapses during development, "
        "phagocytosing debris, and becoming activated during neuroinflammation."
    ),
    (
        "The glymphatic system clears metabolic waste through perivascular spaces, with aquaporin 4 channels "
        "facilitating convective flow of cerebrospinal fluid through brain interstitium during sleep."
    ),
    (
        "Oligodendrocyte precursor cells differentiate into myelinating oligodendrocytes that wrap axons with lipid "
        "rich myelin sheaths, enabling saltatory conduction at nodes of Ranvier."
    ),
    (
        "The blood brain barrier restricts paracellular transport through endothelial tight junctions containing "
        "claudin 5 and occludin, while transcytosis mediates selective macromolecule transport."
    ),
    (
        "Excitotoxicity occurs when excessive glutamate release activates NMDA receptors, causing calcium overload "
        "that triggers mitochondrial dysfunction, oxidative stress, and neuronal death cascades."
    ),
    (
        "Spreading depolarization waves propagate slowly across cortex during migraine aura, with massive ionic "
        "shifts, glutamate release, and transient neuronal silencing."
    ),
    (
        "Alpha synuclein aggregates into Lewy bodies in Parkinson disease, with prion like propagation spreading "
        "pathology through connected brain regions over disease progression."
    ),
    (
        "The substantia nigra pars compacta contains dopaminergic neurons projecting to striatum, with their "
        "degeneration causing motor symptoms while ventral tegmental area involvement affects motivation."
    ),
    (
        "GABAergic medium spiny neurons comprise ninety five percent of striatal neurons, with D1 receptor expressing "
        "direct pathway neurons promoting movement and D2 indirect pathway inhibiting."
    ),
    (
        "Cerebellar Purkinje cells receive climbing fiber input from inferior olive and parallel fiber input from "
        "granule cells, integrating signals for motor learning and coordination."
    ),
    (
        "The suprachiasmatic nucleus contains the master circadian pacemaker, with clock gene transcription "
        "translation feedback loops generating roughly twenty four hour rhythms synchronized by light."
    ),
    (
        "Orexin neurons in lateral hypothalamus regulate sleep wake transitions, with their loss causing narcolepsy "
        "characterized by sudden sleep attacks and cataplexy."
    ),
    (
        "Nociceptive signals travel through unmyelinated C fibers and myelinated A delta fibers to dorsal horn, where "
        "substance P and glutamate transmit pain information."
    ),
    (
        "Mirror neurons in premotor cortex fire both when performing actions and observing others perform them, "
        "potentially contributing to action understanding and social cognition."
    ),
    (
        "The vestibular ocular reflex maintains stable gaze during head movement through semicircular canal input to "
        "vestibular nuclei projecting to extraocular motor nuclei."
    ),
    (
        "Critical period plasticity in visual cortex depends on maturation of parvalbumin positive interneurons and "
        "perineuronal nets, with ocular dominance shifts possible only during development."
    ),
    (
        "Adult neurogenesis occurs in subgranular zone of dentate gyrus, with newborn granule cells integrating into "
        "existing circuits and contributing to pattern separation memory functions."
    ),
    # EXPANDED GENETICS - 20-37 WORD SENTENCES
    (
        "Genome wide association studies identify single nucleotide polymorphisms associated with complex traits by "
        "comparing allele frequencies between cases and controls across millions of genetic variants."
    ),
    (
        "Polygenic risk scores aggregate effects of thousands of common variants weighted by effect sizes from GWAS, "
        "predicting disease liability with increasing accuracy as sample sizes grow."
    ),
    (
        "Expression quantitative trait loci mapping reveals genetic variants affecting gene expression levels, with "
        "cis eQTLs acting locally and trans eQTLs affecting distant genes through regulatory networks."
    ),
    (
        "Linkage disequilibrium describes non random association of alleles at different loci, decaying with "
        "recombination over generations and defining haplotype blocks for association studies."
    ),
    (
        "Chromatin immunoprecipitation sequencing identifies genome wide binding sites of transcription factors and "
        "histone modifications, revealing regulatory elements and epigenetic landscapes."
    ),
    (
        "Hi C and related chromosome conformation capture methods reveal three dimensional genome organization, "
        "including topologically associating domains, chromatin loops, and compartments affecting gene regulation."
    ),
    (
        "CRISPR interference and CRISPR activation use catalytically dead Cas9 fused to transcriptional repressors or "
        "activators, enabling programmable modulation of endogenous gene expression."
    ),
    (
        "Single cell RNA sequencing reveals transcriptional heterogeneity within cell populations, enabling "
        "identification of rare cell types and reconstruction of developmental trajectories."
    ),
    (
        "Trinucleotide repeat expansion disorders show genetic anticipation, with repeat length increasing across "
        "generations, correlating with earlier onset and more severe phenotypes in offspring."
    ),
    (
        "Genomic imprinting establishes parent of origin specific expression through differential DNA methylation at "
        "imprinting control regions, with disruption causing Prader Willi or Angelman syndromes."
    ),
    (
        "X chromosome inactivation randomly silences one X in female cells through Xist RNA coating, spreading "
        "heterochromatin marks, creating mosaicism for X linked traits."
    ),
    (
        "Structural variants including deletions, duplications, inversions, and translocations can disrupt genes, "
        "create fusions, or alter regulatory landscapes, contributing significantly to disease risk."
    ),
    (
        "Mitochondrial DNA mutations follow maternal inheritance patterns, with heteroplasmy levels determining "
        "disease severity as mutant load varies between tissues and individuals."
    ),
    (
        "Mosaicism arises from postzygotic mutations creating genetically distinct cell populations, with germline "
        "mosaicism enabling transmission of apparently de novo mutations to multiple offspring."
    ),
    (
        "The two hit hypothesis explains tumor suppressor inactivation requiring loss of both alleles, with inherited "
        "mutations providing the first hit and somatic loss completing tumorigenesis."
    ),
    (
        "Nonsense mediated decay degrades mRNAs containing premature termination codons, protecting cells from "
        "truncated proteins but also reducing expression from some disease alleles."
    ),
    (
        "Alternative splicing generates multiple protein isoforms from single genes, with tissue specific splicing "
        "factors recognizing cis elements to include or exclude exons."
    ),
    (
        "Long noncoding RNAs regulate gene expression through chromatin remodeling, transcriptional interference, and "
        "scaffolding of protein complexes, with thousands showing cell type specific expression."
    ),
    (
        "Enhancer RNAs are transcribed from active enhancer elements, potentially stabilizing chromatin loops between "
        "enhancers and promoters to facilitate transcriptional activation of target genes."
    ),
    (
        "Transposable elements comprise nearly half the human genome, with Alu and LINE elements still active and "
        "occasionally causing disease through insertional mutagenesis."
    ),
    (
        "Copy number variants affect large genomic segments, with recurrent deletions and duplications at segmental "
        "duplication flanked regions causing neurodevelopmental disorders through dosage imbalance."
    ),
    (
        "Pharmacogenomic variants in cytochrome P450 enzymes and drug transporters affect medication metabolism, "
        "guiding dosing decisions for warfarin, clopidogrel, codeine, and many other drugs."
    ),
    (
        "Carrier screening identifies heterozygotes for recessive disorders, enabling couples to assess reproductive "
        "risks for conditions like cystic fibrosis, spinal muscular atrophy, and hemoglobinopathies."
    ),
    (
        "Preimplantation genetic testing examines embryo biopsies for chromosomal abnormalities or specific mutations, "
        "enabling selection of unaffected embryos for transfer during assisted reproduction."
    ),
    (
        "Newborn screening programs detect treatable metabolic disorders through tandem mass spectrometry of dried "
        "blood spots, enabling early intervention before irreversible damage occurs."
    ),
]

"""Chemistry prompts of thirty to thirty-seven words on reactions, bonding, and electrochemistry."""

from __future__ import annotations

PRINCIPLES: list[str] = [
    # LONG PROMPTS 30-37 WORDS
    (
        "The complete combustion of methane gas in excess oxygen produces carbon dioxide and water vapor according to "
        "the balanced equation CH4 plus 2O2 yields CO2 plus 2H2O with significant heat release."
    ),
    (
        "When concentrated sulfuric acid is added to sodium chloride crystals, hydrogen chloride gas is evolved "
        "according to the reaction NaCl plus H2SO4 yields NaHSO4 plus HCl at elevated temperatures."
    ),
    (
        "The Haber Bosch process synthesizes ammonia from atmospheric nitrogen and hydrogen gas under high pressure "
        "and temperature using an iron catalyst: N2 plus 3H2 yields 2NH3 in equilibrium."
    ),
    (
        "Photosynthesis in green plants converts carbon dioxide and water into glucose and oxygen using sunlight "
        "energy: 6CO2 plus 6H2O plus light energy yields C6H12O6 plus 6O2."
    ),
    (
        "The thermite reaction between aluminum powder and iron three oxide produces molten iron and aluminum oxide "
        "with intense heat: 2Al plus Fe2O3 yields Al2O3 plus 2Fe."
    ),
    (
        "Electrolysis of molten sodium chloride produces sodium metal at the cathode and chlorine gas at the anode "
        "according to the overall reaction 2NaCl yields 2Na plus Cl2."
    ),
    (
        "The contact process manufactures sulfuric acid by oxidizing sulfur dioxide to sulfur trioxide over a vanadium "
        "pentoxide catalyst: 2SO2 plus O2 yields 2SO3 reversibly."
    ),
    (
        "When zinc metal is placed in copper sulfate solution, a single displacement reaction occurs: Zn plus CuSO4 "
        "yields ZnSO4 plus Cu, with copper metal depositing on the zinc."
    ),
    (
        "The decomposition of hydrogen peroxide into water and oxygen gas is catalyzed by manganese dioxide: 2H2O2 "
        "yields 2H2O plus O2, releasing oxygen bubbles rapidly."
    ),
    (
        "Neutralization of hydrochloric acid with sodium hydroxide produces sodium chloride and water in an exothermic "
        "reaction: HCl plus NaOH yields NaCl plus H2O with heat release."
    ),
    (
        "The Ostwald process oxidizes ammonia to nitric acid in three steps: first ammonia oxidizes to nitric oxide, "
        "then to nitrogen dioxide, finally dissolving in water."
    ),
    (
        "Le Chatelier's principle states that when a system at equilibrium is disturbed, it will shift to counteract "
        "the disturbance and establish a new equilibrium position."
    ),
    (
        "The ideal gas law PV equals nRT relates pressure, volume, amount, and temperature of an ideal gas, where R is "
        "the universal gas constant eight point three one four."
    ),
    (
        "Hess's law states that the total enthalpy change for a reaction is independent of the pathway taken, "
        "depending only on the initial and final states of the system."
    ),
    (
        "The Arrhenius equation k equals A times e to the negative Ea over RT describes how reaction rate constants "
        "increase exponentially with temperature due to activation energy."
    ),
    (
        "Gibbs free energy delta G equals delta H minus T times delta S determines reaction spontaneity, with negative "
        "values indicating thermodynamically favorable spontaneous processes at constant conditions."
    ),
    (
        "The Born Haber cycle calculates lattice energy of ionic compounds by applying Hess's law to formation "
        "reactions, ionization energies, electron affinities, and sublimation enthalpies."
    ),
    (
        "Molecular orbital theory describes bonding through the combination of atomic orbitals to form bonding and "
        "antibonding molecular orbitals, with electrons filling according to aufbau principle."
    ),
    (
        "The valence shell electron pair repulsion theory predicts molecular geometry by minimizing repulsion between "
        "electron pairs around the central atom, giving shapes like tetrahedral and trigonal planar."
    ),
    (
        "Hybridization theory explains bonding in molecules like methane through sp3 hybrid orbitals, ethene through "
        "sp2 hybridization, and ethyne through sp hybridization with varying geometries."
    ),
    (
        "The Schrödinger equation describes the wave function of electrons in atoms, with solutions giving atomic "
        "orbitals characterized by principal, angular momentum, magnetic, and spin quantum numbers."
    ),
    (
        "Heisenberg's uncertainty principle states that the position and momentum of a particle cannot both be "
        "precisely determined simultaneously, fundamentally limiting measurement precision in quantum mechanics."
    ),
    (
        "The aufbau principle states that electrons fill orbitals starting from lowest energy, following the order 1s, "
        "2s, 2p, 3s, 3p, 4s, 3d, and so on."
    ),
    (
        "Hund's rule states that electrons occupy degenerate orbitals singly with parallel spins before pairing, "
        "maximizing total spin and minimizing electron electron repulsion in the atom."
    ),
    (
        "The Pauli exclusion principle states that no two electrons in an atom can have the same set of four quantum "
        "numbers, limiting orbital occupancy to two electrons."
    ),
    (
        "Electronegativity measures an atom's ability to attract shared electrons in a covalent bond, with fluorine "
        "being most electronegative at three point nine eight on Pauling scale."
    ),
    (
        "The periodic law states that physical and chemical properties of elements are periodic functions of their "
        "atomic numbers, explaining the organization of the periodic table."
    ),
    (
        "Ionization energy is the minimum energy required to remove an electron from a gaseous atom, generally "
        "increasing across a period and decreasing down a group."
    ),
    (
        "Electron affinity measures the energy change when an electron is added to a gaseous atom, with halogens "
        "having the most negative values due to achieving noble gas configuration."
    ),
    (
        "The octet rule states that atoms tend to gain, lose, or share electrons to achieve eight valence electrons, "
        "mimicking the stable electron configuration of noble gases."
    ),
    (
        "Ionic bonds form through electrostatic attraction between oppositely charged ions, typically between metals "
        "that lose electrons and nonmetals that gain electrons to form stable compounds."
    ),
    (
        "Covalent bonds form when atoms share electron pairs to achieve stable electron configurations, with bond "
        "strength depending on orbital overlap and electronegativity differences between atoms."
    ),
    (
        "Metallic bonding involves delocalized electrons shared among a lattice of metal cations, explaining "
        "properties like electrical conductivity, malleability, and characteristic metallic luster in metals."
    ),
    (
        "Hydrogen bonding is a strong intermolecular force between hydrogen bonded to nitrogen, oxygen, or fluorine "
        "and lone pairs on nearby electronegative atoms, explaining water's unique properties."
    ),
    (
        "Van der Waals forces include London dispersion forces arising from temporary dipoles in all molecules and "
        "dipole dipole interactions between polar molecules, affecting boiling points and solubility."
    ),
    (
        "The kinetic molecular theory describes gases as particles in constant random motion, with temperature "
        "proportional to average kinetic energy and pressure from wall collisions."
    ),
    (
        "Graham's law of effusion states that the rate of effusion of a gas is inversely proportional to the square "
        "root of its molar mass, separating isotopes industrially."
    ),
    (
        "Dalton's law of partial pressures states that total pressure of a gas mixture equals the sum of partial "
        "pressures of individual gases, important in respiratory physiology."
    ),
    (
        "Henry's law states that the solubility of a gas in a liquid is directly proportional to the partial pressure "
        "of the gas above the liquid at constant temperature."
    ),
    (
        "Raoult's law states that the vapor pressure of a solution component equals its mole fraction times the vapor "
        "pressure of the pure component, describing ideal solutions."
    ),
    (
        "Colligative properties like boiling point elevation, freezing point depression, and osmotic pressure depend "
        "only on the number of solute particles, not their chemical identity."
    ),
    (
        "The van't Hoff factor accounts for dissociation or association of solutes in solution, modifying colligative "
        "property calculations for electrolytes that produce multiple ions."
    ),
    (
        "Buffer solutions resist pH changes upon addition of small amounts of acid or base, consisting of a weak acid "
        "and its conjugate base or weak base and conjugate acid."
    ),
    (
        "The Henderson Hasselbalch equation pH equals pKa plus log of conjugate base over acid concentration allows "
        "calculation of buffer pH and design of buffer systems."
    ),
    (
        "Acid base titration determines unknown concentrations by reacting with standard solutions until the "
        "equivalence point, detected by indicators or pH meters showing sharp changes."
    ),
    (
        "Strong acids like hydrochloric, nitric, and sulfuric acid completely dissociate in water, while weak acids "
        "like acetic acid only partially ionize, establishing equilibrium."
    ),
    (
        "The pH scale measures hydrogen ion concentration logarithmically, with pH equals negative log of hydrogen ion "
        "concentration, ranging from zero to fourteen in aqueous solutions."
    ),
    (
        "Oxidation involves loss of electrons and increase in oxidation state, while reduction involves gain of "
        "electrons and decrease in oxidation state, always occurring together."
    ),
    (
        "The electrochemical series ranks metals by their standard reduction potentials, predicting which metals will "
        "displace others from solution and the direction of electron flow."
    ),
    (
        "Galvanic cells convert chemical energy to electrical energy through spontaneous redox reactions, with the "
        "anode undergoing oxidation and cathode undergoing reduction in separate half cells."
    ),
    (
        "Electrolytic cells use electrical energy to drive non spontaneous redox reactions, with the anode positive "
        "and cathode negative, opposite to galvanic cell conventions."
    ),
    (
        "Faraday's laws of electrolysis relate the amount of substance deposited to the quantity of electricity "
        "passed, with one mole of electrons equaling ninety six thousand coulombs."
    ),
    (
        "The Nernst equation calculates cell potential under non standard conditions: E equals E standard minus RT "
        "over nF times natural log of reaction quotient Q."
    ),
    (
        "Corrosion is the electrochemical oxidation of metals, with iron rusting through formation of hydrated iron "
        "three oxide in the presence of oxygen and water."
    ),
    (
        "Sacrificial anodes protect iron structures by providing a more reactive metal like zinc or magnesium that "
        "preferentially oxidizes, preventing iron corrosion through cathodic protection."
    ),
    (
        "Nuclear fission splits heavy nuclei like uranium 235 into smaller fragments, releasing enormous energy and "
        "neutrons that can sustain chain reactions in reactors and weapons."
    ),
    (
        "Nuclear fusion combines light nuclei like hydrogen isotopes to form helium, releasing even more energy per "
        "mass than fission but requiring extreme temperatures to overcome repulsion."
    ),
    (
        "Radioactive decay follows first order kinetics with characteristic half lives, with alpha decay emitting "
        "helium nuclei, beta decay emitting electrons, and gamma decay emitting photons."
    ),
    (
        "Carbon 14 dating determines the age of organic materials by measuring the ratio of carbon 14 to carbon 12, "
        "with the five thousand seven hundred year half life."
    ),
    (
        "Mass spectrometry determines molecular masses and structures by ionizing molecules, separating ions by mass "
        "to charge ratio, and detecting relative abundances to identify compounds."
    ),
    (
        "Infrared spectroscopy identifies functional groups through characteristic absorption frequencies, with "
        "carbonyl groups absorbing around seventeen hundred wavenumbers and hydroxyl groups around thirty four hundred."
    ),
    (
        "Nuclear magnetic resonance spectroscopy determines molecular structure through the interaction of nuclear "
        "spins with magnetic fields, with chemical shifts indicating electronic environment."
    ),
    (
        "Ultraviolet visible spectroscopy measures electronic transitions in molecules, with conjugated systems "
        "absorbing at longer wavelengths and molar absorptivity quantifying absorption strength."
    ),
    (
        "Chromatography separates mixtures based on differential partitioning between mobile and stationary phases, "
        "with gas chromatography for volatiles and liquid chromatography for solutions."
    ),
    (
        "X ray crystallography determines three dimensional molecular structures by analyzing diffraction patterns of "
        "X rays passing through crystalline samples, revealing atomic positions precisely."
    ),
    (
        "The rate law expresses reaction rate as a function of reactant concentrations raised to powers called orders, "
        "determined experimentally rather than from stoichiometry."
    ),
    (
        "The rate determining step is the slowest step in a reaction mechanism, controlling the overall reaction rate "
        "and determining the form of the rate law."
    ),
    (
        "Collision theory explains reaction rates through the frequency and energy of molecular collisions, with only "
        "properly oriented collisions exceeding activation energy being successful."
    ),
    (
        "Transition state theory describes reactions passing through an activated complex at the energy maximum, with "
        "the activation energy being the barrier height on the reaction coordinate."
    ),
    (
        "Catalysts increase reaction rates by providing alternative pathways with lower activation energies, remaining "
        "unchanged after the reaction and not affecting equilibrium position."
    ),
]

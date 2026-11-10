"""Physics prompts: short relativity, nuclear physics, questions, and exclamations, then the first long prompts."""

from __future__ import annotations

RELATIVITY: list[str] = [
    # SHORT STATEMENTS - RELATIVITY
    "The principle of relativity states physics laws are identical in all inertial frames.",
    "The constancy of light speed in all inertial frames underlies special relativity.",
    "Time dilation causes moving clocks to tick slower by the Lorentz factor.",
    "Length contraction shrinks moving objects along direction of motion by Lorentz factor.",
    "The Lorentz factor equals one over square root of one minus velocity squared over c squared.",
    (
        "The relativistic energy momentum relation states energy squared equals momentum squared times c squared plus "
        "rest mass squared times c to the fourth."
    ),
    "Mass energy equivalence declares energy equals mass times speed of light squared.",
    "The four vector formalism unifies space and time in Minkowski spacetime geometry.",
    "Proper time is the invariant interval measured by clock traveling along worldline.",
    "The twin paradox demonstrates asymmetric aging between traveling and stationary observers.",
    "The equivalence principle equates gravitational and inertial mass effects locally.",
    "General relativity describes gravity as spacetime curvature caused by mass energy.",
    "The Einstein field equations relate spacetime curvature tensor to stress energy tensor.",
    "The Schwarzschild metric describes spacetime geometry around spherically symmetric mass.",
    "Gravitational time dilation slows clocks in stronger gravitational fields.",
    "Gravitational lensing bends light paths around massive objects distorting background images.",
    "Frame dragging causes inertial frames to rotate near spinning massive objects.",
    "Gravitational waves are ripples in spacetime propagating at light speed from accelerating masses.",
    "The Kerr metric describes rotating black hole spacetime geometry and ergosphere.",
    "Hawking radiation predicts black holes emit thermal radiation and slowly evaporate.",
    # SHORT STATEMENTS - NUCLEAR & PARTICLE PHYSICS
    "The strong force binds quarks into hadrons through gluon exchange.",
    "Quantum chromodynamics describes strong interaction using color charge and gluons.",
    "Asymptotic freedom means strong coupling decreases at high energies.",
    "Quark confinement prevents isolated quarks from existing at low energies.",
    "The weak force mediates beta decay through W and Z boson exchange.",
    "Electroweak unification combines electromagnetic and weak forces at high energies.",
    "The Higgs mechanism gives mass to W and Z bosons through symmetry breaking.",
    "Leptons include electrons, muons, taus, and their corresponding neutrinos.",
    "Quarks come in six flavors: up, down, charm, strange, top, and bottom.",
    "Antimatter has opposite quantum numbers and annihilates with corresponding matter particles.",
    "The Standard Model describes fundamental particles and their electromagnetic, weak, and strong interactions.",
    "Fermions have half integer spin and obey Fermi Dirac statistics.",
    "Bosons have integer spin and obey Bose Einstein statistics.",
    "The Pauli exclusion principle applies only to fermions, not bosons.",
    "Conservation of baryon number forbids proton decay in Standard Model.",
    "Conservation of lepton number restricts allowed particle reactions and decays.",
    "CP violation explains matter antimatter asymmetry in weak interactions.",
    "Neutrino oscillations prove neutrinos have mass and flavor mixing occurs.",
    "The nuclear binding energy curve peaks at iron with maximum stability.",
    "Radioactive decay follows exponential law with characteristic half life.",
    "Alpha decay tunnels helium nucleus through Coulomb barrier.",
    "Beta minus decay converts neutron to proton, electron, and antineutrino.",
    "Beta plus decay converts proton to neutron, positron, and neutrino.",
    "Gamma decay releases energy as high frequency photons from excited nuclei.",
    "Nuclear fission splits heavy nuclei releasing neutrons and binding energy.",
    "Nuclear fusion combines light nuclei releasing enormous energy at stellar cores.",
    "The liquid drop model treats nucleus as incompressible fluid with surface tension.",
    "The shell model explains magic numbers through nuclear quantum energy levels.",
    "Cross section measures probability of nuclear reaction in barn units.",
    "The Bethe Weizsäcker formula calculates nuclear binding energy semi empirically.",
    # SHORT QUESTIONS
    "What is the physical meaning of the wave function?",
    "How does the uncertainty principle limit measurements?",
    "Why does entropy always increase in isolated systems?",
    "What causes the photoelectric effect threshold frequency?",
    "How do black holes emit Hawking radiation?",
    "Why is the speed of light constant in all frames?",
    "What determines the fine structure constant value?",
    "How does quantum tunneling enable nuclear fusion?",
    "Why do neutron stars have such extreme density?",
    "What causes superconductivity below critical temperature?",
    "How does the Higgs field give particles mass?",
    "Why is antimatter so rare in the universe?",
    "What determines the lifetime of radioactive isotopes?",
    "How do lasers achieve coherent light emission?",
    "Why does the Coriolis force deflect moving objects?",
    "What causes the precession of Mercury's orbit?",
    "How does gravitational lensing magnify distant objects?",
    "Why is helium superfluidity observed only below lambda point?",
    "What determines the color of heated objects?",
    "How do semiconductors conduct current selectively?",
    "Why does diffraction limit optical resolution?",
    "What causes the Casimir effect between plates?",
    "How do atomic clocks achieve nanosecond precision?",
    "Why is the cosmological constant so small?",
    "What determines the critical mass for fission?",
    "How does the double slit experiment show wave particle duality?",
    "Why do electrons form standing waves in atoms?",
    "What causes the Lamb shift in hydrogen spectrum?",
    "How does quantum entanglement enable teleportation?",
    "Why is the proton heavier than the sum of its quarks?",
    "What determines the Chandrasekhar limit for white dwarfs?",
    "How do pulsars maintain such precise rotation periods?",
    "Why does the cosmic microwave background exist?",
    "What causes the anomalous magnetic moment of the electron?",
    "How do phonons carry heat through solids?",
    "Why is the strong force confined to nuclear scales?",
    "What determines the degeneracy pressure in neutron stars?",
    "How does pair production create particles from photons?",
    "Why do muons decay into electrons and neutrinos?",
    "What causes the Meissner effect in superconductors?",
    "How do quasicrystals exhibit forbidden symmetries?",
    "Why is the electron apparently point like?",
    "What determines the Curie temperature for ferromagnets?",
    "How do Cooper pairs enable superconductivity?",
    "Why does the sun produce energy through fusion?",
    "What causes gravitational waves from merging black holes?",
    "How do transistors amplify electrical signals?",
    "Why is the vacuum not truly empty?",
    "What determines the de Haas van Alphen oscillations?",
    "How does the Aharonov Bohm effect demonstrate electromagnetic potentials?",
    # SHORT EXCLAMATIONS
    "The particle tunneled through the barrier!",
    "Perfect superconducting levitation achieved!",
    "The laser beam is perfectly coherent!",
    "Gravitational waves detected from binary merger!",
    "The Bose Einstein condensate formed!",
    "Quantum entanglement confirmed across continents!",
    "The Higgs boson was discovered!",
    "Nuclear fusion ignition accomplished!",
    "Antimatter successfully trapped and stored!",
    "The black hole shadow was imaged!",
    "Superfluidity observed in helium three!",
    "The quark gluon plasma created!",
    "Time dilation measured with atomic clocks!",
    "The neutrino oscillation confirmed!",
    "Quantum supremacy demonstrated computationally!",
    "The gravitational redshift verified!",
    "Hawking radiation theoretically predicted!",
    "The Casimir force measured precisely!",
    "Topological insulators discovered!",
    "Majorana fermions potentially observed!",
    "The cosmic microwave background mapped!",
    "Dark matter halo detected indirectly!",
    "The proton radius puzzle solved!",
    "Quantum teleportation achieved experimentally!",
    "The muon anomaly exceeds predictions!",
    "Exoplanet atmospheres spectroscopically analyzed!",
    "Pulsar timing reveals gravitational waves!",
    "The electron spin resonance peak sharp!",
    "Phonon coherence maintained at low temperatures!",
    "The Hall conductance quantized exactly!",
    "Plasma confinement duration record broken!",
    "The interference pattern beautifully visible!",
    "Relativistic jets observed from quasar!",
    "The crystal lattice vibrates harmonically!",
    "Magnetar flare detected across galaxy!",
    "The photon antibunching confirmed single emission!",
    "Quantum coherence preserved in noisy environment!",
    "The soliton propagated without dispersion!",
    "Sonoluminescence produced visible light!",
    "The Josephson junction oscillated precisely!",
    "Atom interferometry measured gravity gradient!",
    "The optical lattice trapped ultracold atoms!",
    "Squeezed light reduced quantum noise!",
    "The neutron star merger observed multi messenger!",
    "Chaos emerged from deterministic equations!",
    "The strange attractor revealed beautiful fractal!",
    "Quasiparticle excitations observed in solid!",
    "The phonon laser successfully demonstrated!",
    "Polariton condensation achieved at room temperature!",
    "The terahertz gap finally bridged!",
    # LONG PROMPTS 30-37 WORDS
    (
        "The time dependent Schrödinger equation states that i times reduced Planck constant times partial derivative "
        "of wave function with respect to time equals Hamiltonian operator acting on wave function."
    ),
    (
        "Einstein's mass energy equivalence E equals m c squared demonstrates that mass and energy are "
        "interchangeable, with rest mass containing enormous energy equal to mass times speed of light squared."
    ),
    (
        "The Heisenberg uncertainty principle states that the product of position uncertainty and momentum uncertainty "
        "must be greater than or equal to reduced Planck constant divided by two."
    ),
    (
        "Newton's law of universal gravitation states that gravitational force equals gravitational constant times "
        "product of masses divided by distance squared, acting along the line connecting centers."
    ),
    (
        "The Lorentz transformation relates space and time coordinates between inertial frames moving at relative "
        "velocity, mixing space and time through the Lorentz factor gamma."
    ),
    (
        "Maxwell's equations unify electricity and magnetism: Gauss's laws for electric and magnetic fields, Faraday's "
        "induction law, and Ampere's law with Maxwell's displacement current correction."
    ),
    (
        "The Stefan Boltzmann law states that total radiated power per unit area equals Stefan Boltzmann constant "
        "times absolute temperature raised to the fourth power for blackbody radiators."
    ),
    (
        "The de Broglie hypothesis assigns wavelength equal to Planck constant divided by momentum to all matter, "
        "predicting electron diffraction later confirmed by Davisson Germer experiment."
    ),
    (
        "The photoelectric effect demonstrates that electrons are ejected from metals when photon energy exceeds work "
        "function, with maximum kinetic energy equal to photon energy minus work function."
    ),
    (
        "The Compton effect shows X ray photon momentum transfer to electrons, with wavelength shift equal to Compton "
        "wavelength times one minus cosine of scattering angle."
    ),
    (
        "Fermat's principle of least time states that light travels between points along paths that extremize optical "
        "path length, explaining reflection and refraction through variational principles."
    ),
    (
        "The Navier Stokes equations describe viscous fluid motion, relating acceleration to pressure gradient, "
        "viscous forces, and body forces through partial differential equations for velocity field."
    ),
    (
        "The Reynolds number characterizes flow regime as ratio of inertial to viscous forces, with turbulent flow "
        "occurring above critical Reynolds number for given geometry."
    ),
    (
        "The Bernoulli equation states that sum of pressure, kinetic energy density, and gravitational potential "
        "energy density remains constant along streamlines for inviscid incompressible flow."
    ),
    (
        "The Boltzmann entropy formula S equals k ln W relates thermodynamic entropy to the natural logarithm of the "
        "number of accessible microstates weighted by Boltzmann constant."
    ),
    (
        "The partition function Z equals sum over states of exponential of negative energy over k T, encoding all "
        "thermodynamic information through derivatives of its logarithm."
    ),
    (
        "The Planck distribution gives spectral energy density as frequency cubed over exponential of photon energy "
        "over thermal energy minus one, times appropriate constants."
    ),
    (
        "The Fermi energy is the highest occupied electron energy at absolute zero, determining electronic properties "
        "of metals through density of states at Fermi level."
    ),
    (
        "The BCS theory explains superconductivity through Cooper pairs of electrons with opposite spin and momentum, "
        "mediated by phonon exchange creating energy gap at Fermi surface."
    ),
    (
        "The Josephson effect predicts supercurrent flow across insulating barrier between superconductors, with AC "
        "current oscillating at frequency proportional to applied voltage."
    ),
    (
        "The Aharonov Bohm effect demonstrates that electromagnetic potentials affect quantum phases even where "
        "electric and magnetic fields vanish, showing potentials are physically significant."
    ),
    (
        "The Lamb shift is the small energy difference between hydrogen two S one half and two P one half levels, "
        "caused by vacuum fluctuation interactions with electron."
    ),
    (
        "The anomalous magnetic moment of electron exceeds Dirac prediction by approximately one part in thousand, "
        "explained by quantum electrodynamic radiative corrections involving virtual photon loops."
    ),
    (
        "The Casimir effect produces attractive force between parallel conducting plates from vacuum fluctuation mode "
        "exclusion, with force inversely proportional to fourth power of plate separation."
    ),
    (
        "The Chandrasekhar limit of approximately one point four solar masses is maximum mass for white dwarf before "
        "electron degeneracy pressure cannot prevent gravitational collapse."
    ),
    (
        "The Schwarzschild radius equals two times gravitational constant times mass divided by speed of light "
        "squared, defining event horizon size for nonrotating black holes."
    ),
    (
        "Hawking radiation temperature equals reduced Planck constant times c cubed divided by eight pi times "
        "gravitational constant times mass times Boltzmann constant for Schwarzschild black holes."
    ),
    (
        "The cosmological redshift z relates observed wavelength to emitted wavelength through scale factor ratio, "
        "measuring universe expansion since light emission from distant galaxies."
    ),
    (
        "The Friedmann equations describe homogeneous isotropic universe expansion from Einstein field equations, "
        "relating Hubble parameter to matter density, curvature, and cosmological constant."
    ),
    (
        "The cosmic microwave background temperature of two point seven Kelvin is remnant radiation from recombination "
        "epoch, redshifted from approximately three thousand Kelvin by cosmic expansion."
    ),
    (
        "The nucleosynthesis of light elements in the early universe produced hydrogen, helium, and trace lithium "
        "abundances that match observations, supporting hot Big Bang cosmology."
    ),
    (
        "The inflationary epoch exponentially expanded space by factor exceeding ten to the twenty sixth, explaining "
        "horizon, flatness, and monopole problems in standard cosmology."
    ),
    (
        "The dark energy density of approximately ten to the negative twenty nine grams per cubic centimeter causes "
        "accelerating expansion detected through type Ia supernovae distance measurements."
    ),
    (
        "The WIMP miracle suggests weakly interacting massive particles with electroweak scale masses and couplings "
        "naturally produce observed dark matter relic density from thermal freeze out."
    ),
    (
        "The seesaw mechanism explains tiny neutrino masses through mixing with very heavy right handed neutrinos, "
        "naturally suppressing left handed neutrino mass by their mass ratio."
    ),
]

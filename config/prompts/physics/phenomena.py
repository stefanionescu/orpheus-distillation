"""Physics prompts of thirty to thirty-seven words across physics."""

from __future__ import annotations

PHENOMENA: list[str] = [
    (
        "The strong CP problem asks why QCD theta parameter is extremely small, with Peccei Quinn symmetry and axion "
        "particles proposed as elegant dynamical solution."
    ),
    (
        "The hierarchy problem questions why Higgs mass is stable against quadratically divergent radiative "
        "corrections, motivating supersymmetry or compositeness to cancel divergences naturally."
    ),
    (
        "The measurement problem in quantum mechanics asks how definite outcomes emerge from superposition states, "
        "with decoherence, many worlds, and collapse interpretations proposed."
    ),
    (
        "The holographic principle suggests three dimensional physics is encoded on two dimensional boundary, with "
        "entropy scaling as area rather than volume for black holes."
    ),
    (
        "The AdS CFT correspondence relates gravitational theories in anti de Sitter space to conformal field theories "
        "on the boundary, providing nonperturbative quantum gravity insights."
    ),
    (
        "The renormalization group describes how physical parameters change with energy scale, explaining universality "
        "of critical phenomena and asymptotic freedom of strong interaction."
    ),
    (
        "The path integral formulation sums over all possible trajectories weighted by exponential of action divided "
        "by reduced Planck constant, giving quantum transition amplitudes."
    ),
    (
        "Feynman diagrams graphically represent terms in perturbation expansion, with vertices for interactions and "
        "propagators connecting particles, systematizing quantum field theory calculations."
    ),
    (
        "The optical theorem relates total cross section to imaginary part of forward scattering amplitude, connecting "
        "absorption to interference between incident and scattered waves."
    ),
    (
        "The fluctuation dissipation theorem relates system response to equilibrium fluctuations, connecting damping "
        "coefficients to correlation functions through Boltzmann constant times temperature."
    ),
    (
        "The Kubo formula expresses linear response coefficients in terms of equilibrium correlation functions, "
        "enabling calculation of transport properties from microscopic Hamiltonians."
    ),
    (
        "The Landau theory describes phase transitions through order parameter expansion of free energy, predicting "
        "critical exponents and symmetry breaking patterns near transition points."
    ),
    (
        "The Ginzburg Landau theory adds gradient terms to Landau expansion, describing spatial variations of order "
        "parameter and predicting vortex structures in type II superconductors."
    ),
    (
        "The topological insulators have insulating bulk but conducting surface states protected by time reversal "
        "symmetry, with spin momentum locking from strong spin orbit coupling."
    ),
    (
        "The quantum Hall effect quantizes Hall conductance in units of electron charge squared over Planck constant, "
        "with robust plateaus insensitive to disorder and sample geometry."
    ),
    (
        "The fractional quantum Hall effect exhibits plateaus at fractional filling factors, explained by Laughlin "
        "wave function describing incompressible quantum liquid with fractionally charged quasiparticles."
    ),
    (
        "The Berry phase is geometric phase acquired by quantum state during adiabatic parameter variation, with Berry "
        "curvature acting as effective magnetic field in parameter space."
    ),
    (
        "The Bloch theorem states electron wave functions in periodic potentials are plane waves modulated by periodic "
        "functions, with energy bands separated by forbidden gaps."
    ),
    (
        "The tight binding model describes electrons hopping between localized atomic orbitals, giving band structure "
        "from overlap integrals with applications to graphene and topological materials."
    ),
    (
        "The Hubbard model adds on site Coulomb repulsion to tight binding Hamiltonian, capturing Mott insulator "
        "physics and antiferromagnetic ordering in strongly correlated electron systems."
    ),
    (
        "The Kondo effect screens magnetic impurity spin through conduction electron cloud below Kondo temperature, "
        "producing resistance minimum and enhanced density of states at Fermi level."
    ),
    (
        "The Anderson localization prevents electron diffusion in disordered systems when mean free path becomes "
        "comparable to wavelength, with wave function exponentially localized in space."
    ),
    (
        "The Kosterlitz Thouless transition occurs in two dimensional XY model through vortex pair unbinding, with "
        "algebraic rather than long range order above transition temperature."
    ),
    (
        "The Ising model describes ferromagnetism through nearest neighbor spin interactions, with exact Onsager "
        "solution in two dimensions showing second order phase transition."
    ),
    (
        "The Monte Carlo method samples configuration space with Boltzmann weighted probability, enabling numerical "
        "calculation of thermodynamic averages for complex interacting systems."
    ),
    (
        "The density functional theory maps interacting electron problem to noninteracting electrons in effective "
        "potential, enabling practical first principles calculation of electronic structure."
    ),
    (
        "The Born Oppenheimer approximation separates electronic and nuclear motion based on mass ratio, with "
        "electrons responding instantaneously to nuclear configuration changes."
    ),
    (
        "The variational principle states that expectation value of Hamiltonian in any trial wave function provides "
        "upper bound on true ground state energy."
    ),
    (
        "The WKB approximation constructs semiclassical wave functions from classical action, valid when de Broglie "
        "wavelength varies slowly compared to potential length scale."
    ),
    (
        "The sudden approximation applies when perturbation changes faster than system response time, with transition "
        "probabilities given by overlap integrals between initial and final states."
    ),
    (
        "The adiabatic theorem states slowly varying Hamiltonian keeps system in instantaneous eigenstate, with "
        "geometric phase accumulated during cyclic parameter evolution."
    ),
    (
        "The Fermi golden rule gives transition rate as two pi over reduced Planck constant times squared matrix "
        "element times density of final states."
    ),
    (
        "The Dyson equation relates full Green's function to noninteracting Green's function through self energy, "
        "enabling systematic treatment of interactions in many body systems."
    ),
    (
        "The Lehmann representation expresses Green's function spectral function through excited state matrix "
        "elements, connecting single particle properties to many body excitation spectrum."
    ),
    (
        "The linear response theory relates measurable susceptibilities to equilibrium correlation functions, with "
        "Kramers Kronig relations connecting real and imaginary parts through causality."
    ),
    (
        "The Boltzmann transport equation describes nonequilibrium distribution evolution through streaming and "
        "collision terms, giving electrical and thermal conductivity from scattering rates."
    ),
    (
        "The Drude model treats electrons as classical particles with momentum relaxation, predicting frequency "
        "dependent conductivity with plasma frequency setting optical absorption edge."
    ),
    (
        "The Lindhard function describes electron gas dielectric response, with Thomas Fermi screening at long "
        "wavelengths and Friedel oscillations from Fermi surface effects."
    ),
    (
        "The plasmon is collective longitudinal oscillation of electron density, with plasma frequency proportional to "
        "square root of electron density over effective mass."
    ),
    (
        "The magnon is quantized spin wave excitation in ordered magnets, with dispersion relation determined by "
        "exchange coupling and magnetic anisotropy energies."
    ),
    (
        "The exciton is bound electron hole pair in semiconductors, with binding energy reduced from hydrogen by "
        "dielectric screening and effective mass ratio."
    ),
    (
        "The polaron is electron dressed by phonon cloud in polar materials, with effective mass enhanced and mobility "
        "reduced by strong electron phonon coupling."
    ),
    (
        "The phonon bottleneck slows electron cooling when phonon emission rate exceeds phonon decay rate, limiting "
        "hot carrier relaxation in nanostructures."
    ),
    (
        "The Raman scattering inelastically shifts photon frequency by phonon energy, probing vibrational modes with "
        "selection rules determined by symmetry and polarization."
    ),
    (
        "The Brillouin scattering couples photons to acoustic phonons, measuring sound velocity and elastic constants "
        "through frequency shift of scattered light."
    ),
    (
        "The neutron scattering directly probes phonon and magnon dispersions through energy and momentum "
        "conservation, with magnetic cross section sensitive to spin correlations."
    ),
    (
        "The X ray absorption spectroscopy probes unoccupied electronic states above Fermi level, with edge structure "
        "revealing local bonding geometry and oxidation state."
    ),
    (
        "The angle resolved photoemission spectroscopy maps occupied band structure by measuring electron energy and "
        "momentum, directly imaging Fermi surface topology."
    ),
    (
        "The scanning tunneling microscopy achieves atomic resolution through exponential dependence of tunneling "
        "current on tip sample separation, imaging electronic density of states."
    ),
    (
        "The atomic force microscopy measures surface topography through cantilever deflection, with various modes "
        "detecting electrostatic, magnetic, and chemical forces at nanoscale."
    ),
    (
        "The nuclear magnetic resonance detects spin precession in magnetic field, with chemical shifts and relaxation "
        "times probing local electronic environment and dynamics."
    ),
    (
        "The electron spin resonance measures paramagnetic center transitions, with g factor and hyperfine splitting "
        "revealing spin Hamiltonian parameters and molecular structure."
    ),
    (
        "The Mössbauer spectroscopy uses recoilless nuclear gamma emission and absorption, with isomer shift and "
        "quadrupole splitting probing local charge density and symmetry."
    ),
    (
        "The muon spin rotation implants polarized muons as local magnetic probes, with precession frequency and "
        "relaxation mapping internal magnetic fields and fluctuations."
    ),
    (
        "The positron annihilation spectroscopy detects vacancy defects through lifetime and momentum distribution, "
        "with Doppler broadening revealing local electron momentum distribution."
    ),
    (
        "The gravitational wave strain amplitude scales as chirp mass to five thirds power over luminosity distance, "
        "with frequency sweeping upward as binary inspirals."
    ),
    (
        "The matched filtering extracts gravitational wave signals from detector noise by correlating data with "
        "template waveforms computed from general relativistic binary dynamics."
    ),
    (
        "The LIGO interferometers detect gravitational waves through differential arm length changes of order ten to "
        "the negative twenty one, limited by quantum shot noise."
    ),
    (
        "The pulsar timing arrays detect nanohertz gravitational waves from supermassive black hole binaries through "
        "correlated timing residuals across millisecond pulsar network."
    ),
    (
        "The gravitational wave memory is permanent spacetime deformation after wave passage, potentially detectable "
        "through pulsar timing or future space based interferometers."
    ),
    (
        "The primordial gravitational wave background from inflation would imprint B mode polarization on cosmic "
        "microwave background, probing physics at grand unified theory scales."
    ),
    (
        "The stochastic gravitational wave background from unresolved binary sources creates correlated signal across "
        "detector network, with Hellings Downs angular correlation pattern."
    ),
    (
        "The extreme mass ratio inspiral of stellar mass object into supermassive black hole tests strong field "
        "gravity through precisely measured orbital evolution."
    ),
]

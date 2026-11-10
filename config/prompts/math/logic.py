"""Math prompts on category theory, logic, dynamical systems, and mathematical physics."""

from __future__ import annotations

LOGIC: list[str] = [
    # NOVEL MATH CONCEPTS - Part 6 (Category Theory and Logic)
    (
        "A functor is a structure preserving map between categories that sends objects to objects and morphisms to "
        "morphisms compatibly."
    ),
    (
        "The Yoneda lemma states that a category is faithfully embedded in its category of presheaves, a fundamental "
        "result in category theory."
    ),
    (
        "A natural transformation is a morphism between functors that commutes with the action of the functors on "
        "morphisms."
    ),
    (
        "The adjunction between two functors means one is left adjoint to the other, with a universal property "
        "relating their hom sets."
    ),
    (
        "A topos is a category that behaves like the category of sets, with a subobject classifier and all finite "
        "limits and colimits."
    ),
    (
        "The Curry Howard correspondence identifies proofs with programs and propositions with types, connecting logic "
        "and computer science."
    ),
    (
        "A monad in category theory consists of an endofunctor with unit and multiplication satisfying associativity "
        "and unit laws."
    ),
    (
        "The Kan extension is a universal construction that extends functors along other functors, appearing "
        "throughout category theory."
    ),
    (
        "A model category provides a framework for doing homotopy theory abstractly, with fibrations, cofibrations, "
        "and weak equivalences."
    ),
    (
        "The Grothendieck construction builds a category from a functor to the category of categories, creating the "
        "total category of a fibration."
    ),
    (
        "An infinity category generalizes ordinary categories by allowing higher morphisms between morphisms at all "
        "levels."
    ),
    (
        "The nerve of a category is a simplicial set encoding the category's structure, connecting category theory to "
        "algebraic topology."
    ),
    (
        "A derived category is obtained from an abelian category by formally inverting quasi isomorphisms, central to "
        "homological algebra."
    ),
    (
        "The Gödel incompleteness theorems show that sufficiently strong consistent formal systems cannot prove their "
        "own consistency."
    ),
    (
        "A sheaf on a topological space assigns data to open sets that can be glued together, generalizing functions "
        "to more abstract settings."
    ),
    (
        "The Löwenheim Skolem theorem states that if a first order theory has an infinite model, it has models of "
        "every infinite cardinality."
    ),
    (
        "A forcing extension adds new sets to a model of set theory, used to prove independence results like the "
        "continuum hypothesis."
    ),
    (
        "The compactness theorem for first order logic states that a set of sentences is satisfiable if every finite "
        "subset is satisfiable."
    ),
    (
        "A ultraproduct constructs new structures from families of structures using an ultrafilter, preserving first "
        "order properties."
    ),
    (
        "The Tarski Vaught test provides a criterion for when a substructure is an elementary substructure of a larger "
        "structure."
    ),
    # NOVEL MATH CONCEPTS - Part 7 (Dynamical Systems and Chaos)
    (
        "A strange attractor is a fractal set toward which a chaotic dynamical system evolves, exhibiting sensitive "
        "dependence on initial conditions."
    ),
    (
        "The Lyapunov exponent measures the rate of separation of infinitesimally close trajectories, quantifying "
        "chaos in dynamical systems."
    ),
    (
        "A bifurcation occurs when a small change in a parameter causes a qualitative change in the behavior of a "
        "dynamical system."
    ),
    (
        "The Mandelbrot set is the set of complex numbers c for which the iteration z squared plus c remains bounded "
        "starting from zero."
    ),
    (
        "A horseshoe map is a canonical example of a chaotic map, stretching and folding a region like a horseshoe to "
        "create complex dynamics."
    ),
    (
        "The Poincaré recurrence theorem states that almost every point in a measure preserving system returns "
        "arbitrarily close to its starting position."
    ),
    (
        "A Julia set is the boundary between points that escape to infinity and those that remain bounded under "
        "iteration of a complex function."
    ),
    (
        "The KAM theorem describes the persistence of quasi periodic orbits in nearly integrable Hamiltonian systems "
        "under small perturbations."
    ),
    (
        "A period doubling cascade is a route to chaos where the period of stable orbits doubles repeatedly as a "
        "parameter is varied."
    ),
    (
        "The Feigenbaum constants are universal numbers appearing in the period doubling route to chaos across many "
        "different dynamical systems."
    ),
    (
        "An ergodic system has the property that time averages equal space averages, meaning orbits explore the whole "
        "space uniformly."
    ),
    (
        "The Lorenz attractor is a famous strange attractor arising from a simplified model of atmospheric convection, "
        "exhibiting butterfly shaped dynamics."
    ),
    (
        "A Smale horseshoe demonstrates how stretching and folding creates infinitely many periodic orbits and "
        "sensitive dependence on initial conditions."
    ),
    (
        "The Sharkovskii ordering of positive integers determines which periods of periodic orbits imply the existence "
        "of other periods."
    ),
    (
        "A homoclinic orbit connects a fixed point to itself, and its presence often implies chaotic behavior in the "
        "dynamical system."
    ),
    (
        "The Ruelle Takens scenario describes how quasi periodic motion can become chaotic after just a few "
        "bifurcations in fluid systems."
    ),
    (
        "A Markov partition divides a chaotic system into regions that map to unions of regions, enabling symbolic "
        "dynamics analysis."
    ),
    (
        "The topological entropy measures the complexity of a dynamical system by counting distinguishable orbits at "
        "increasingly fine scales."
    ),
    (
        "A heteroclinic connection links two different fixed points and can organize global dynamics in systems with "
        "multiple equilibria."
    ),
    "The Melnikov method detects chaos in perturbed Hamiltonian systems by measuring the splitting of separatrices.",
    # NOVEL MATH CONCEPTS - Part 8 (Mathematical Physics)
    (
        "A gauge theory describes physics in terms of connections on fiber bundles, with the gauge group acting as "
        "structure group."
    ),
    (
        "The Yang Mills equations generalize Maxwell's equations to non abelian gauge groups, fundamental to the "
        "standard model of particle physics."
    ),
    (
        "A conformal field theory is invariant under angle preserving transformations and plays a central role in "
        "string theory and statistical mechanics."
    ),
    (
        "The Dirac equation describes relativistic spin one half particles, predicting antimatter and unifying quantum "
        "mechanics with special relativity."
    ),
    (
        "A path integral sums over all possible histories weighted by the exponential of the action, providing an "
        "alternative formulation of quantum mechanics."
    ),
    (
        "The Chern Simons theory is a topological quantum field theory in three dimensions, related to knot invariants "
        "and the Jones polynomial."
    ),
    (
        "A supersymmetry relates bosons and fermions through a symmetry that exchanges particles of different spin, "
        "extending the Poincaré group."
    ),
    (
        "The Wess Zumino Witten model is a conformal field theory based on a Lie group, with applications to string "
        "theory and condensed matter."
    ),
    (
        "A instanton is a solution to the Yang Mills equations in Euclidean space, contributing to non perturbative "
        "effects in quantum field theory."
    ),
    (
        "The Bethe ansatz is a method for finding exact solutions to integrable quantum systems, particularly spin "
        "chains and related models."
    ),
    (
        "A topological insulator is a material that is insulating in its bulk but conducts on its surface due to "
        "topological properties of its band structure."
    ),
    (
        "The Sachdev Ye Kitaev model is a solvable model of strongly interacting fermions with connections to quantum "
        "gravity and black holes."
    ),
    (
        "A modular tensor category provides the algebraic structure underlying topological quantum computation and "
        "anyonic systems."
    ),
    (
        "The AdS CFT correspondence conjectures an equivalence between gravity in anti de Sitter space and conformal "
        "field theory on its boundary."
    ),
    (
        "A Bogomolny bound is a lower bound on the energy of a field configuration that is saturated by solutions to "
        "first order equations."
    ),
    (
        "The Witten index counts the difference between bosonic and fermionic ground states in a supersymmetric "
        "quantum mechanical system."
    ),
    (
        "A Berry phase is a geometric phase acquired by a quantum state when parameters are varied adiabatically "
        "around a closed loop."
    ),
    (
        "The Laughlin wavefunction describes the fractional quantum Hall effect, where electrons form an "
        "incompressible quantum liquid."
    ),
    (
        "A monopole in gauge theory is a topological soliton carrying magnetic charge, predicted by Dirac and realized "
        "in grand unified theories."
    ),
    (
        "The Seiberg Witten equations are first order partial differential equations on four manifolds that provide "
        "smooth structure invariants."
    ),
]

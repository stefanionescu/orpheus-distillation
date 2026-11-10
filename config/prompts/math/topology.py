"""Math prompts on geometry, topology, number theory, and combinatorics."""

from __future__ import annotations

TOPOLOGY: list[str] = [
    # NOVEL MATH CONCEPTS - Part 3 (Geometry and Topology)
    (
        "A symplectic manifold has a closed non degenerate two form, providing the geometric framework for Hamiltonian "
        "mechanics and classical physics."
    ),
    (
        "The Poincaré duality theorem relates the homology and cohomology groups of a closed orientable manifold in a "
        "symmetric way."
    ),
    (
        "A Kähler manifold is simultaneously a complex manifold, a Riemannian manifold, and a symplectic manifold with "
        "compatible structures."
    ),
    (
        "The Atiyah Singer index theorem computes the index of an elliptic differential operator in terms of "
        "topological data of the manifold."
    ),
    (
        "A Calabi Yau manifold has vanishing first Chern class and admits Ricci flat metrics, playing a central role "
        "in string theory compactifications."
    ),
    (
        "The Thurston geometrization conjecture, now proven, classifies three manifolds into eight geometric types "
        "including hyperbolic and spherical."
    ),
    (
        "A spin manifold admits a spin structure allowing the definition of spinor fields, essential for describing "
        "fermions in physics."
    ),
    (
        "The Chern classes are topological invariants of complex vector bundles that obstruct the existence of certain "
        "geometric structures."
    ),
    (
        "A contact manifold has a maximally non integrable hyperplane distribution, serving as the odd dimensional "
        "counterpart to symplectic manifolds."
    ),
    (
        "The Floer homology is an infinite dimensional version of Morse homology, providing powerful invariants for "
        "three manifolds and symplectic geometry."
    ),
    (
        "A hyperbolic manifold has constant negative sectional curvature and exhibits rich geometry related to "
        "discrete groups and number theory."
    ),
    (
        "The Pontryagin classes are characteristic classes of real vector bundles, related to Chern classes through "
        "complexification."
    ),
    (
        "A foliation partitions a manifold into immersed submanifolds called leaves, generalizing the level sets of a "
        "submersion."
    ),
    (
        "The Stiefel Whitney classes are mod two characteristic classes that measure the orientability and other "
        "properties of real vector bundles."
    ),
    (
        "A orbifold is a generalization of a manifold that allows mild singularities modeled on quotients of Euclidean "
        "space by finite groups."
    ),
    (
        "The Thom isomorphism theorem relates the cohomology of a vector bundle's total space to the cohomology of its "
        "base space."
    ),
    (
        "A stratified space is decomposed into manifold pieces called strata, with controlled conditions on how the "
        "strata fit together."
    ),
    (
        "The Lefschetz fixed point theorem counts fixed points of a continuous map using the alternating sum of traces "
        "on homology groups."
    ),
    (
        "A CR manifold has a complex structure on a subbundle of its tangent bundle, generalizing the boundary of a "
        "complex domain."
    ),
    (
        "The Gauss map sends each point of a surface to the unit normal vector, encoding curvature information in its "
        "derivative."
    ),
    # NOVEL MATH CONCEPTS - Part 4 (Number Theory and Arithmetic)
    (
        "The Riemann zeta function encodes information about prime numbers and has zeros whose locations are the "
        "subject of the famous Riemann hypothesis."
    ),
    (
        "An algebraic number field is a finite extension of the rational numbers, generalizing the rationals while "
        "retaining arithmetic properties."
    ),
    (
        "The class number measures how far the ring of integers in a number field is from being a unique factorization "
        "domain."
    ),
    (
        "A modular form is a holomorphic function on the upper half plane with special symmetry properties under the "
        "modular group."
    ),
    (
        "The Birch and Swinnerton Dyer conjecture relates the rank of an elliptic curve to the order of vanishing of "
        "its L function at one."
    ),
    (
        "An automorphic form generalizes modular forms to other Lie groups, playing a central role in the Langlands "
        "program."
    ),
    (
        "The Mordell Weil theorem states that the group of rational points on an elliptic curve over the rationals is "
        "finitely generated."
    ),
    (
        "A Diophantine equation asks for integer or rational solutions, with famous examples including Fermat's last "
        "theorem and the Pell equation."
    ),
    (
        "The quadratic reciprocity law describes when a prime p is a quadratic residue modulo another prime q in terms "
        "of their residue classes."
    ),
    (
        "An Artin L function generalizes the Riemann zeta function to representations of Galois groups, encoding "
        "arithmetic information."
    ),
    (
        "The ABC conjecture relates the radical of a product of coprime integers to their sum, with deep implications "
        "for Diophantine equations."
    ),
    (
        "A Galois representation encodes arithmetic information in a homomorphism from a Galois group to a matrix "
        "group over a field."
    ),
    (
        "The Taniyama Shimura conjecture, now proven, states that every elliptic curve over the rationals is modular, "
        "implying Fermat's last theorem."
    ),
    "A p adic number extends the rationals using a different notion of distance based on divisibility by a prime p.",
    (
        "The Langlands program is a vast web of conjectures connecting number theory, representation theory, and "
        "harmonic analysis."
    ),
    (
        "An adele is an element of the restricted product of all completions of a number field, providing a unified "
        "framework for local and global analysis."
    ),
    (
        "The Hasse principle asks whether a Diophantine equation has rational solutions if and only if it has "
        "solutions in all completions."
    ),
    (
        "A cyclotomic field is obtained by adjoining roots of unity to the rationals, with Galois group isomorphic to "
        "a group of units."
    ),
    (
        "The Selmer group is an approximation to the group of rational points on an elliptic curve, computable through "
        "Galois cohomology."
    ),
    (
        "A Dedekind zeta function generalizes the Riemann zeta function to algebraic number fields, encoding "
        "information about prime ideals."
    ),
    # NOVEL MATH CONCEPTS - Part 5 (Combinatorics and Discrete Math)
    (
        "A matroid abstracts the notion of linear independence, capturing combinatorial properties shared by vector "
        "configurations and graphs."
    ),
    (
        "The Ramsey number R of m, n is the minimum number of vertices needed to guarantee a complete subgraph of size "
        "m or an independent set of size n."
    ),
    (
        "A Young tableau is a filling of a Young diagram with positive integers, central to the representation theory "
        "of symmetric groups."
    ),
    (
        "The chromatic polynomial counts the number of proper colorings of a graph using at most k colors, encoding "
        "structural information."
    ),
    (
        "A Catalan number counts many combinatorial objects including Dyck paths, non crossing partitions, and full "
        "binary trees with n internal nodes."
    ),
    (
        "The Tutte polynomial is a two variable graph invariant that specializes to the chromatic polynomial and the "
        "flow polynomial."
    ),
    (
        "A Sperner family is an antichain in the power set of a finite set, with maximum size given by the middle "
        "binomial coefficient."
    ),
    (
        "The Möbius function on a poset allows inversion of sums over order ideals, generalizing the number theoretic "
        "Möbius function."
    ),
    (
        "A Latin square is an n by n array filled with n different symbols where each symbol appears exactly once in "
        "each row and column."
    ),
    (
        "The Lovász local lemma provides conditions under which a collection of rare events has positive probability "
        "of all being avoided."
    ),
    (
        "A Steiner system is a combinatorial design where every t subset of points is contained in exactly one block "
        "of size k."
    ),
    "The Erdős Ko Rado theorem gives the maximum size of an intersecting family of k subsets of an n element set.",
    (
        "A perfect matching in a graph is a set of edges covering every vertex exactly once, counted by the permanent "
        "of the adjacency matrix."
    ),
    (
        "The Szemerédi regularity lemma approximates any large graph by a bounded complexity structure, fundamental in "
        "extremal graph theory."
    ),
    (
        "A parking function is a sequence where cars can park according to preferences, counted by the formula n plus "
        "one to the power n minus one."
    ),
    (
        "The Robinson Schensted correspondence bijectively maps permutations to pairs of standard Young tableaux of "
        "the same shape."
    ),
    (
        "A hyperplane arrangement is a finite collection of affine hyperplanes, with rich combinatorics encoded in its "
        "intersection poset."
    ),
    (
        "The Turán number is the maximum number of edges in a graph on n vertices that contains no complete subgraph "
        "of size k."
    ),
    (
        "A chip firing game on a graph models discrete diffusion, with the critical group measuring how the game "
        "reaches stable configurations."
    ),
    (
        "The Stanley Reisner ring associates a graded ring to a simplicial complex, connecting combinatorics to "
        "commutative algebra."
    ),
]

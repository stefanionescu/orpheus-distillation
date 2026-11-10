"""Math prompts on cryptography, computation, special functions, and transforms."""

from __future__ import annotations

CRYPTOGRAPHY: list[str] = [
    # NOVEL MATH CONCEPTS - Part 9 (Cryptography and Computation)
    (
        "The RSA cryptosystem relies on the difficulty of factoring large integers into primes, providing security for "
        "much of internet communication."
    ),
    (
        "A zero knowledge proof allows one party to prove knowledge of a secret without revealing any information "
        "about the secret itself."
    ),
    (
        "The discrete logarithm problem asks for the exponent k given g and g to the k in a group, underlying Diffie "
        "Hellman key exchange."
    ),
    (
        "An elliptic curve cryptosystem uses the group structure of points on an elliptic curve, providing security "
        "with smaller key sizes than RSA."
    ),
    (
        "The P versus NP problem asks whether every problem whose solution can be verified quickly can also be solved "
        "quickly."
    ),
    (
        "A hash function maps arbitrary data to fixed size outputs, with cryptographic versions resisting collision "
        "and preimage attacks."
    ),
    (
        "The Turing machine is a mathematical model of computation that defines what it means for a function to be "
        "computable."
    ),
    (
        "A quantum computer uses superposition and entanglement to perform certain computations exponentially faster "
        "than classical computers."
    ),
    (
        "The halting problem asks whether a given program will eventually halt, proven by Turing to be undecidable for "
        "general programs."
    ),
    (
        "A lattice based cryptosystem relies on the hardness of problems like finding short vectors in high "
        "dimensional lattices."
    ),
    "The Kolmogorov complexity of a string is the length of the shortest program that produces that string as output.",
    (
        "A homomorphic encryption scheme allows computation on encrypted data without decrypting it, enabling secure "
        "cloud computation."
    ),
    "The Church Turing thesis asserts that any effectively calculable function can be computed by a Turing machine.",
    (
        "A post quantum cryptosystem is designed to remain secure even against attacks by quantum computers running "
        "Shor's algorithm."
    ),
    (
        "The busy beaver function grows faster than any computable function, measuring the maximum productivity of "
        "halting Turing machines."
    ),
    (
        "A secure multiparty computation protocol allows parties to jointly compute a function without revealing their "
        "private inputs."
    ),
    "The polynomial hierarchy generalizes P and NP to a tower of complexity classes based on alternating quantifiers.",
    (
        "A verifiable random function produces outputs that are unpredictable but can be verified as correctly "
        "computed from the input."
    ),
    (
        "The complexity class BQP contains problems solvable by quantum computers in polynomial time with bounded "
        "error probability."
    ),
    (
        "A fully homomorphic encryption scheme supports arbitrary computations on ciphertexts, a breakthrough achieved "
        "by Craig Gentry."
    ),
    # NOVEL MATH CONCEPTS - Part 10 (Special Functions and Transforms)
    (
        "The gamma function extends the factorial to complex numbers, satisfying the functional equation gamma of z "
        "plus one equals z times gamma of z."
    ),
    (
        "A Bessel function arises in solutions to Laplace's equation in cylindrical coordinates, appearing in wave "
        "propagation and heat conduction."
    ),
    (
        "The Riemann theta function is a multivariable generalization of the Jacobi theta function, central to the "
        "theory of abelian varieties."
    ),
    (
        "A hypergeometric function is defined by a power series whose coefficients are ratios of products of "
        "Pochhammer symbols."
    ),
    (
        "The Mellin transform is an integral transform related to the Fourier and Laplace transforms, useful for "
        "Dirichlet series and number theory."
    ),
    (
        "A Whittaker function is a solution to a confluent hypergeometric equation, appearing in representation theory "
        "and automorphic forms."
    ),
    "The Weierstrass elliptic function is a doubly periodic meromorphic function that uniformizes elliptic curves.",
    (
        "A modular lambda function is a modular function that maps the upper half plane to the complex plane minus "
        "zero, one, and infinity."
    ),
    (
        "The Airy function solves the differential equation y double prime equals x y, describing diffraction patterns "
        "and quantum tunneling."
    ),
    (
        "A polylogarithm generalizes the logarithm to higher orders, appearing in quantum field theory and algebraic K "
        "theory."
    ),
    "The Hurwitz zeta function generalizes the Riemann zeta function by including a shift parameter in the summation.",
    (
        "A spherical harmonic is an eigenfunction of the Laplacian on the sphere, used to expand functions on spheres "
        "in physics."
    ),
    (
        "The Dedekind eta function is a modular form of weight one half, related to the partition function and string "
        "theory."
    ),
    (
        "A Mathieu function is a solution to a differential equation with periodic coefficients, describing elliptical "
        "vibrating membranes."
    ),
    (
        "The incomplete gamma function generalizes the gamma function by integrating only up to a finite limit rather "
        "than infinity."
    ),
    (
        "A Jacobi theta function is a quasi doubly periodic function appearing in elliptic functions, number theory, "
        "and statistical mechanics."
    ),
    (
        "The Painlevé transcendents are solutions to certain nonlinear second order differential equations that cannot "
        "be expressed in terms of classical functions."
    ),
    (
        "A Meijer G function is a very general function defined by a contour integral that includes most special "
        "functions as special cases."
    ),
    (
        "The digamma function is the logarithmic derivative of the gamma function, appearing in regularization and "
        "renormalization calculations."
    ),
    (
        "A Heun function solves a second order linear differential equation with four regular singular points on the "
        "Riemann sphere."
    ),
]

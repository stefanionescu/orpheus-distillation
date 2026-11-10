"""Math prompts on differential equations, complex analysis, number theory, algebra, topology, and statistics."""

from __future__ import annotations

ANALYSIS: list[str] = [
    # ADVANCED MATH - DIFFERENTIAL EQUATIONS
    "A first order linear differential equation has the form dy dx plus p of x times y equals q of x.",
    "What's the general solution to the differential equation dy dx equals two y?",
    "The method of separation of variables works when you can write the equation as f of y dy equals g of x dx.",
    (
        "A second order homogeneous differential equation with constant coefficients has solutions involving "
        "exponential functions."
    ),
    "What's the particular solution to y double prime plus four y equals zero?",
    "The Wronskian determines whether a set of solutions to a differential equation is linearly independent.",
    "To solve a nonhomogeneous differential equation, you find the complementary solution plus a particular solution.",
    "What's the Laplace transform of the function f of t equals e to the a t?",
    (
        "The method of undetermined coefficients works for finding particular solutions when the forcing function has "
        "a specific form."
    ),
    "A system of differential equations describes how multiple quantities change simultaneously over time.",
    (
        "What's the general solution to the differential equation x squared y double prime plus x y prime minus y "
        "equals zero?"
    ),
    "The characteristic equation for a second order linear differential equation gives you the form of the solution.",
    "To solve a differential equation using power series, you assume a solution of the form sum of a n x to the n.",
    "What's the solution to the initial value problem dy dx equals x y with y of zero equals one?",
    "Partial differential equations involve functions of multiple variables and their partial derivatives.",
    "The heat equation describes how temperature changes over time in a conducting medium.",
    "What's the wave equation? It's a second order partial differential equation describing wave propagation.",
    (
        "The method of variation of parameters finds particular solutions for nonhomogeneous linear differential "
        "equations."
    ),
    "A differential equation is exact if the left side can be written as the derivative of some function.",
    "What's the integrating factor for the differential equation dy dx plus two x y equals x?",
    # ADVANCED MATH - COMPLEX ANALYSIS
    "What's the complex conjugate of three plus four i?",
    "The modulus of a complex number z equals a plus b i is the square root of a squared plus b squared.",
    "Euler's formula states that e to the i theta equals cosine theta plus i sine theta.",
    "What's the argument of the complex number one plus i?",
    "A function is analytic if it's differentiable at every point in its domain.",
    "The Cauchy Riemann equations are necessary conditions for a function to be complex differentiable.",
    (
        "What's the residue of a function at a pole? It's the coefficient of one over z minus z zero in the Laurent "
        "series."
    ),
    "Cauchy's integral theorem states that the integral of an analytic function around a closed curve is zero.",
    "The maximum modulus principle says an analytic function's maximum occurs on the boundary of its domain.",
    "What's the value of i to the power of i? It's e to the negative pi over two.",
    "A Möbius transformation maps circles and lines to circles and lines in the complex plane.",
    "The fundamental theorem of algebra guarantees that every polynomial has at least one complex root.",
    "What's the Laurent series expansion of one over z minus one around z equals zero?",
    "The argument principle relates the number of zeros and poles of a function to an integral.",
    "A branch cut allows you to define a single valued function from a multi valued one.",
    "What's the contour integral of one over z around the unit circle?",
    "The residue theorem simplifies calculating complex integrals by summing residues at poles inside the contour.",
    "An entire function is analytic everywhere in the complex plane, like e to the z or sine z.",
    "What's the image of the unit circle under the mapping w equals z squared?",
    "The Schwarz lemma gives bounds on analytic functions mapping the unit disk to itself.",
    # ADVANCED MATH - NUMBER THEORY AND ABSTRACT ALGEBRA
    "What's the greatest common divisor of two numbers using the Euclidean algorithm?",
    (
        "Fermat's little theorem states that if p is prime and a is not divisible by p, then a to the p minus one is "
        "congruent to one modulo p."
    ),
    "A group is a set with an operation that's associative, has an identity element, and every element has an inverse.",
    (
        "What's a prime number? It's a natural number greater than one with no positive divisors other than one and "
        "itself."
    ),
    "The Chinese remainder theorem solves systems of simultaneous congruences when the moduli are pairwise coprime.",
    (
        "What's the order of an element in a group? It's the smallest positive integer n such that g to the n equals "
        "the identity."
    ),
    "A ring is a set with two operations, addition and multiplication, satisfying certain axioms.",
    "What's Euler's totient function phi of n? It counts the positive integers up to n that are coprime to n.",
    (
        "The fundamental theorem of arithmetic states that every integer greater than one has a unique prime "
        "factorization."
    ),
    "What's a field? It's a commutative ring where every nonzero element has a multiplicative inverse.",
    "A subgroup is a subset of a group that's closed under the group operation and contains inverses.",
    "What's the modular inverse of a modulo m? It's a number b such that a b is congruent to one modulo m.",
    "The isomorphism theorems describe relationships between groups, subgroups, and quotient groups.",
    "What's a cyclic group? It's a group generated by a single element.",
    (
        "Wilson's theorem states that p is prime if and only if p minus one factorial is congruent to negative one "
        "modulo p."
    ),
    "A normal subgroup is one where left and right cosets coincide, allowing you to form a quotient group.",
    "What's the order of the multiplicative group modulo n? It's phi of n, where phi is Euler's totient function.",
    "The Sylow theorems provide information about the number and structure of subgroups of prime power order.",
    "What's a homomorphism? It's a function between groups that preserves the group operation.",
    "Lagrange's theorem states that the order of a subgroup divides the order of the group.",
    # ADVANCED MATH - TOPOLOGY AND ADVANCED GEOMETRY
    "What's a topological space? It's a set equipped with a collection of open sets satisfying certain axioms.",
    "A manifold is a topological space that locally resembles Euclidean space near each point.",
    "The fundamental group of a space measures how many distinct ways you can loop around the space.",
    "What's a homeomorphism? It's a continuous bijection with a continuous inverse between topological spaces.",
    "A metric space is a set with a distance function satisfying the triangle inequality and other properties.",
    (
        "What's the Euler characteristic of a polyhedron? It's V minus E plus F, where V is vertices, E is edges, F is "
        "faces."
    ),
    "A compact set is one where every open cover has a finite subcover.",
    "What's a geodesic? It's the shortest path between two points on a curved surface.",
    "The Gauss Bonnet theorem relates the curvature of a surface to its topology.",
    "What's a Riemannian manifold? It's a manifold equipped with a metric tensor defining distances and angles.",
    "A simply connected space is one where every loop can be continuously contracted to a point.",
    "What's the genus of a surface? It's the number of holes or handles the surface has.",
    (
        "The Poincaré conjecture, now proven, states that every simply connected three dimensional manifold is "
        "homeomorphic to the three sphere."
    ),
    "What's a fiber bundle? It's a space that locally looks like a product space but may be twisted globally.",
    "A differential form is an object that can be integrated over manifolds, generalizing the concept of integration.",
    "What's the curvature tensor? It measures how much a manifold deviates from being flat.",
    "The Hodge star operator maps k forms to n minus k forms on an n dimensional manifold.",
    "What's a Lie group? It's a group that's also a smooth manifold where the group operations are smooth.",
    "A vector field on a manifold assigns a tangent vector to each point of the manifold.",
    "What's the de Rham cohomology? It measures the failure of closed forms to be exact on a manifold.",
    # ADVANCED MATH - ADVANCED STATISTICS AND PROBABILITY
    (
        "What's the central limit theorem? It states that the sum of many independent random variables approaches a "
        "normal distribution."
    ),
    "A confidence interval gives you a range of values likely to contain the true population parameter.",
    (
        "What's the p value? It's the probability of observing results at least as extreme as your data, assuming the "
        "null hypothesis is true."
    ),
    (
        "Bayes' theorem updates probabilities based on new evidence: P of A given B equals P of B given A times P of A "
        "divided by P of B."
    ),
    (
        "What's maximum likelihood estimation? It's a method for estimating parameters by maximizing the likelihood "
        "function."
    ),
    "The chi squared test determines whether observed frequencies differ significantly from expected frequencies.",
    (
        "What's a regression analysis? It models the relationship between a dependent variable and one or more "
        "independent variables."
    ),
    "A t test compares means between two groups to determine if the difference is statistically significant.",
    (
        "What's the law of large numbers? It states that as sample size increases, the sample mean converges to the "
        "population mean."
    ),
    (
        "The normal distribution has a probability density function proportional to e to the negative x minus mu "
        "squared over two sigma squared."
    ),
    (
        "What's ANOVA? Analysis of variance tests whether means of multiple groups are significantly different from "
        "each other."
    ),
    (
        "A random variable's expected value is the weighted average of all possible values, weighted by their "
        "probabilities."
    ),
    "What's the variance of a random variable? It measures how spread out the distribution is around the mean.",
    "The Poisson distribution models the number of events occurring in a fixed interval of time or space.",
    (
        "What's a hypothesis test? You formulate null and alternative hypotheses, then use data to decide whether to "
        "reject the null."
    ),
    "The exponential distribution models the time between events in a Poisson process.",
    (
        "What's correlation versus causation? Correlation measures association, but doesn't imply one variable causes "
        "the other."
    ),
    (
        "A confidence level of ninety five percent means that if you repeated the experiment many times, ninety five "
        "percent of intervals would contain the true parameter."
    ),
    "What's the standard error? It's the standard deviation of the sampling distribution of a statistic.",
    (
        "The binomial distribution models the number of successes in n independent Bernoulli trials with probability p "
        "of success."
    ),
]

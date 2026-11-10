"""Math prompts: spelled out equations, then algebraic structures, analysis, and measure theory."""

from __future__ import annotations

STRUCTURES: list[str] = [
    # SPELLED OUT EQUATIONS - Part 3
    (
        "When you factor the expression x squared minus nine, you recognize it as a difference of squares and write it "
        "as x plus three times x minus three."
    ),
    (
        "If you compute the sum of an arithmetic series with first term five, last term ninety five, and twenty terms, "
        "you get twenty times fifty, which is one thousand."
    ),
    (
        "The formula for the area of a sector is one half times r squared times theta, where theta is the central "
        "angle measured in radians."
    ),
    (
        "When you solve the logarithmic equation log base three of x equals four, you rewrite it as three to the "
        "fourth equals x, so x equals eighty one."
    ),
    (
        "If you differentiate the natural log of x squared plus one, you use the chain rule to get two x divided by x "
        "squared plus one."
    ),
    (
        "The equation of the tangent line to y equals x squared at the point three, nine has slope six and equation y "
        "minus nine equals six times x minus three."
    ),
    (
        "When you compute the expected value of a fair six sided die, you add one through six and divide by six to get "
        "three point five."
    ),
    (
        "If the radius of a sphere is doubled, the volume increases by a factor of eight because volume depends on "
        "radius cubed."
    ),
    "The integration by parts formula states that the integral of u dv equals u v minus the integral of v du.",
    (
        "When you solve the trigonometric equation two sine x equals one, you get sine x equals one half, so x equals "
        "thirty degrees or one hundred fifty degrees."
    ),
    (
        "If you compute the z score for a value of eighty five with mean seventy and standard deviation ten, you get "
        "eighty five minus seventy over ten equals one point five."
    ),
    (
        "The formula for compound interest is A equals P times one plus r over n raised to the power of n times t, "
        "where n is compounding frequency."
    ),
    (
        "When you evaluate the definite integral of x squared from one to four, you get x cubed over three evaluated, "
        "giving sixty four thirds minus one third equals twenty one."
    ),
    (
        "If you apply the product rule to differentiate x times e to the x, you get e to the x plus x times e to the "
        "x, which simplifies to e to the x times x plus one."
    ),
    (
        "The sum of a geometric series with first term two, ratio one half, and infinite terms is two divided by one "
        "minus one half, which equals four."
    ),
    (
        "When you solve the equation x to the fourth minus thirteen x squared plus thirty six equals zero, you "
        "substitute u equals x squared and factor."
    ),
    (
        "If the correlation coefficient between two variables is negative zero point eight five, there is a strong "
        "negative linear relationship between them."
    ),
    (
        "The formula for the surface area of a cylinder is two pi r squared plus two pi r h, accounting for both "
        "circular bases and the lateral surface."
    ),
    (
        "When you compute the probability of getting exactly three heads in five coin flips, you use five choose three "
        "times one half to the fifth power."
    ),
    (
        "If you solve the system using Cramer's rule, you compute determinants of matrices formed by replacing columns "
        "with the constant vector."
    ),
    (
        "The Maclaurin series for cosine x is one minus x squared over two factorial plus x to the fourth over four "
        "factorial minus x to the sixth over six factorial."
    ),
    (
        "When you find the inverse of the function f of x equals two x plus five, you swap x and y and solve to get f "
        "inverse of x equals x minus five over two."
    ),
    (
        "If you compute the work done by a force F of x equals three x squared from x equals zero to x equals four, "
        "you integrate to get sixty four joules."
    ),
    (
        "The formula for the moment of inertia of a thin rod about its center is one twelfth times mass times length "
        "squared."
    ),
    (
        "When you solve the recurrence relation a sub n equals two a sub n minus one with a sub zero equals three, the "
        "closed form is a sub n equals three times two to the n."
    ),
    (
        "If you compute the curl of the vector field F equals y i plus z j plus x k, you get the vector negative i "
        "minus j minus k."
    ),
    (
        "The formula for the nth term of a geometric sequence is a sub n equals a sub one times r to the power of n "
        "minus one."
    ),
    (
        "When you evaluate the triple integral of one over a rectangular box, you get the volume of the box, which is "
        "length times width times height."
    ),
    (
        "If the acceleration is constant at nine point eight meters per second squared, the velocity after five "
        "seconds starting from rest is forty nine meters per second."
    ),
    (
        "The formula for the electric field due to a point charge is k times q divided by r squared, where k is "
        "Coulomb's constant."
    ),
    # NOVEL MATH CONCEPTS - Part 1 (Algebraic Structures)
    (
        "A monoid is an algebraic structure with an associative binary operation and an identity element, but elements "
        "don't necessarily have inverses like in groups."
    ),
    (
        "The quaternions extend the complex numbers with three imaginary units i, j, and k, where multiplication is "
        "not commutative but is associative."
    ),
    (
        "A semigroup is simpler than a monoid because it only requires an associative binary operation without needing "
        "an identity element at all."
    ),
    (
        "The octonions are an eight dimensional algebra extending the quaternions, but they lose associativity while "
        "still being alternative and having a norm."
    ),
    (
        "A lattice in algebra is a partially ordered set where every two elements have a unique supremum and infimum, "
        "useful in order theory."
    ),
    (
        "The Weyl algebra is generated by elements x and d satisfying the relation d x minus x d equals one, modeling "
        "differential operators."
    ),
    (
        "A Boolean algebra is a complemented distributive lattice with operations meet, join, and complement, "
        "foundational to logic and set theory."
    ),
    (
        "The Clifford algebra generalizes complex numbers and quaternions, providing a framework for spinors and "
        "geometric transformations in physics."
    ),
    (
        "A Hopf algebra combines algebra and coalgebra structures with an antipode map, appearing naturally in quantum "
        "groups and topology."
    ),
    (
        "The exterior algebra of a vector space captures the algebraic properties of determinants and differential "
        "forms through the wedge product."
    ),
    (
        "A Kac Moody algebra is an infinite dimensional Lie algebra generalizing finite dimensional simple Lie "
        "algebras, important in string theory."
    ),
    (
        "The Steenrod algebra consists of stable cohomology operations and plays a central role in algebraic topology "
        "and homotopy theory."
    ),
    (
        "A Jordan algebra uses a commutative but non associative product satisfying the Jordan identity, arising in "
        "quantum mechanics and projective geometry."
    ),
    (
        "The Hecke algebra appears in representation theory and is related to symmetries of flag varieties and the "
        "Kazhdan Lusztig basis."
    ),
    (
        "A Frobenius algebra is a finite dimensional algebra with a non degenerate bilinear form, important in "
        "topological quantum field theory."
    ),
    (
        "The Temperley Lieb algebra describes planar diagrams with connections and is fundamental to knot theory and "
        "statistical mechanics."
    ),
    (
        "A vertex algebra formalizes the operator product expansion in conformal field theory, with applications to "
        "moonshine and string theory."
    ),
    (
        "The Yangian is a quantum group that deforms the universal enveloping algebra of a Lie algebra, appearing in "
        "integrable systems."
    ),
    (
        "A cluster algebra has a combinatorial structure with mutation operations, connected to Teichmüller theory and "
        "representation theory."
    ),
    (
        "The Nichols algebra is a braided Hopf algebra that appears in the classification of pointed Hopf algebras and "
        "quantum groups."
    ),
    # NOVEL MATH CONCEPTS - Part 2 (Analysis and Measure Theory)
    (
        "A Banach space is a complete normed vector space where every Cauchy sequence converges, fundamental to "
        "functional analysis and operator theory."
    ),
    (
        "The Lebesgue integral extends the Riemann integral to a much larger class of functions using measure theory "
        "rather than partitions."
    ),
    (
        "A Hilbert space is a complete inner product space that generalizes Euclidean space to infinite dimensions, "
        "essential for quantum mechanics."
    ),
    (
        "The Radon Nikodym theorem states that under certain conditions, one measure can be expressed as an integral "
        "with respect to another measure."
    ),
    (
        "A Sobolev space consists of functions with weak derivatives in Lebesgue spaces, crucial for studying partial "
        "differential equations."
    ),
    (
        "The Hahn Banach theorem guarantees extension of bounded linear functionals, a cornerstone result in "
        "functional analysis with many applications."
    ),
    (
        "A distribution or generalized function extends the notion of function to include objects like the Dirac "
        "delta, used in physics and analysis."
    ),
    (
        "The Riesz representation theorem identifies continuous linear functionals on certain function spaces with "
        "integration against measures."
    ),
    (
        "A Schwartz space consists of rapidly decreasing smooth functions, providing the natural domain for the "
        "Fourier transform on all of Euclidean space."
    ),
    (
        "The spectral theorem decomposes self adjoint operators on Hilbert spaces into simpler pieces, generalizing "
        "diagonalization of matrices."
    ),
    (
        "A Fréchet space is a complete metrizable locally convex topological vector space, generalizing Banach spaces "
        "with a weaker topology."
    ),
    (
        "The Baire category theorem states that complete metric spaces cannot be written as a countable union of "
        "nowhere dense sets."
    ),
    (
        "A Borel measure is defined on the sigma algebra generated by open sets, providing a framework for probability "
        "and integration theory."
    ),
    (
        "The Fubini theorem allows you to compute double integrals as iterated integrals when the integrand is "
        "absolutely integrable."
    ),
    (
        "A Hardy space consists of holomorphic functions on the unit disk with bounded mean oscillation, important in "
        "harmonic analysis."
    ),
    (
        "The dominated convergence theorem allows interchanging limits and integrals when functions are bounded by an "
        "integrable function."
    ),
    (
        "A Besov space interpolates between Sobolev spaces and provides fine regularity scales for functions, used in "
        "approximation theory."
    ),
    (
        "The monotone convergence theorem states that the integral of an increasing sequence of non negative functions "
        "equals the limit of their integrals."
    ),
    (
        "A Orlicz space generalizes Lebesgue spaces by replacing the power function with a more general convex "
        "function called an Orlicz function."
    ),
    (
        "The Vitali covering lemma provides a way to select a disjoint subcollection from a covering that still "
        "captures most of the measure."
    ),
]

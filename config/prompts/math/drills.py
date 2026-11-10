"""Math prompts: long expressions, practice problems, multivariable calculus, and linear algebra."""

from __future__ import annotations

DRILLS: list[str] = [
    # LONG EXPRESSIONS - Part 5
    (
        "To find the equation of a tangent line to a curve at a given point, you need the slope at that point and the "
        "point itself."
    ),
    (
        "The area of a sector of a circle equals the fraction of the circle times pi times the radius squared, where "
        "the fraction is the angle divided by three sixty."
    ),
    (
        "When solving systems of equations with three variables, you can use elimination or substitution methods, but "
        "it requires more steps than systems with two variables."
    ),
    (
        "The formula for finding the distance from a point to a line involves the absolute value of a x plus b y plus "
        "c divided by the square root of a squared plus b squared."
    ),
    (
        "To calculate the volume of a solid of revolution, you integrate pi times the function squared over the "
        "interval, which gives you the volume when rotating around the x axis."
    ),
    (
        "The area of a triangle using coordinates can be found using the determinant formula involving the three "
        "vertices, which gives you one half times the absolute value of the determinant."
    ),
    (
        "When working with complex numbers in polar form, you can multiply them by multiplying their magnitudes and "
        "adding their angles, which simplifies many calculations."
    ),
    (
        "The derivative of a parametric function requires finding the derivative of y with respect to t divided by the "
        "derivative of x with respect to t."
    ),
    (
        "To find the area of a region using double integration, you set up iterated integrals with appropriate limits "
        "based on the region's boundaries."
    ),
    (
        "The formula for the sum of a geometric series is the first term times one minus the common ratio to the nth "
        "power, all divided by one minus the common ratio."
    ),
    (
        "When calculating the work done by a variable force, you integrate the force function with respect to "
        "displacement over the distance traveled."
    ),
    (
        "The area of a regular pentagon can be found by dividing it into five isosceles triangles and calculating the "
        "area of one times five."
    ),
    (
        "To solve a logarithmic equation, you often need to convert it to exponential form or use properties of "
        "logarithms to combine or separate terms."
    ),
    (
        "The volume of a solid formed by rotating a region around the y axis requires using the method of cylindrical "
        "shells or washers, depending on the situation."
    ),
    (
        "When finding the area under a parametric curve, you integrate y times the derivative of x with respect to the "
        "parameter over the appropriate interval."
    ),
    (
        "The formula for finding the angle between two planes involves calculating the angle between their normal "
        "vectors using the dot product formula."
    ),
    (
        "To calculate the surface area of a surface of revolution, you integrate two pi times the function times the "
        "square root of one plus the derivative squared."
    ),
    (
        "The area of a region bounded by curves in polar coordinates requires integrating one half times r squared "
        "with respect to theta between the appropriate angles."
    ),
    (
        "When solving problems involving related rates, you use implicit differentiation to find how one quantity "
        "changes with respect to time when another quantity is changing."
    ),
    (
        "The formula for finding the volume of a tetrahedron involves one sixth times the absolute value of the scalar "
        "triple product of three edge vectors."
    ),
    # MORE BASIC ARITHMETIC AND OPERATIONS
    "What's thirty plus forty five?",
    "Seventy two minus thirty eight equals thirty four.",
    "Eight times nine equals seventy two.",
    "One hundred forty four divided by twelve is twelve.",
    "What's the sum of twenty five and thirty five?",
    "Ninety minus fifty five equals thirty five.",
    "Six times twelve equals seventy two.",
    "Eighty divided by five equals sixteen.",
    "What's fifteen plus twenty five plus ten?",
    "One hundred minus thirty seven equals sixty three.",
    "Seven times eight equals fifty six.",
    "Ninety nine divided by eleven equals nine.",
    "What's forty two plus eighteen?",
    "Eighty five minus twenty nine equals fifty six.",
    "Nine times six equals fifty four.",
    "One hundred twenty divided by eight equals fifteen.",
    "What's the total of thirty, forty, and fifty?",
    "Seventy minus twenty three equals forty seven.",
    "Eleven times five equals fifty five.",
    "One hundred eight divided by nine equals twelve.",
    # MORE FRACTIONS AND MIXED NUMBERS
    "What's one and a half plus two and a half?",
    "Three and three quarters minus one and a quarter equals two and a half.",
    "One and one third times three equals four.",
    "Five and a half divided by two equals two point seven five.",
    "What's two thirds plus one third?",
    "Four and a quarter minus two and three quarters equals one and a half.",
    "One and a half times four equals six.",
    "Seven and a half divided by three equals two point five.",
    "What's three fourths plus one fourth?",
    "Six and two thirds minus three and one third equals three and one third.",
    "Two and a half times two equals five.",
    "Nine divided by two equals four point five.",
    "What's five sixths minus one sixth?",
    "Three and three eighths plus two and five eighths equals six.",
    "One and a quarter times four equals five.",
    "Ten point five divided by two point one equals five.",
    "What's seven eighths plus one eighth?",
    "Four and three quarters minus one and a quarter equals three and a half.",
    "Two and two thirds times three equals eight.",
    "Twelve point six divided by three equals four point two.",
    # MORE PERCENTAGE PROBLEMS
    "What's twenty five percent of four hundred?",
    "Fifteen percent of sixty equals nine.",
    "What's thirty three point three percent of ninety?",
    "Eighty percent off means you pay twenty percent of the original price.",
    "What's twelve percent of two hundred fifty?",
    "A twenty percent increase on fifty dollars is sixty dollars.",
    "What's forty five percent of eighty?",
    "Seventy five percent of one hundred twenty is ninety.",
    "What's eight percent of one thousand?",
    "A fifteen percent tip on eighty dollars is twelve dollars.",
    "What's sixty six point six percent of thirty?",
    "Ninety percent of fifty equals forty five.",
    "What's thirty five percent of two hundred?",
    "A ten percent decrease means you multiply by zero point nine.",
    "What's twenty two percent of one hundred?",
    "Fifty five percent of eighty is forty four.",
    "What's eighteen percent of one hundred fifty?",
    "A thirty percent discount on one hundred dollars saves you thirty dollars.",
    "What's seven point five percent of eighty?",
    "Sixty percent of seventy five equals forty five.",
    # MORE ALGEBRA PROBLEMS
    "If two x plus three equals eleven, what is x?",
    "Solve for y: five y minus seven equals eighteen.",
    "What's the value of x if x squared equals thirty six?",
    "If a equals eight and b equals five, what's a times b?",
    "Solve the equation: three x plus four equals nineteen.",
    "What's x cubed when x equals three?",
    "If y equals three x minus five, what's y when x equals seven?",
    "Solve for z: four z plus nine equals twenty five.",
    "What's the square root of forty nine?",
    "If x squared equals eighty one, what are the possible values of x?",
    "What's three to the power of four?",
    "Solve for a: two a minus six equals ten.",
    "What's the value of x if x times five equals thirty five?",
    "If y equals x squared minus four, what's y when x equals six?",
    "What's the cube root of sixty four?",
    "Solve the equation: five x minus eight equals seventeen.",
    "What's four to the power of three?",
    "If a plus b equals fifteen and a equals nine, what's b?",
    "Solve for x: x divided by four equals eight.",
    # MORE GEOMETRY PROBLEMS
    "What's the area of a rectangle that's six feet by ten feet?",
    "A square with sides of eight inches has an area of sixty four square inches.",
    "What's the perimeter of a rectangle that's twelve by eighteen?",
    "The area of a circle with radius six is approximately one hundred thirteen point one.",
    "What's the area of a triangle with base ten and height eight?",
    "A circle's circumference with radius seven is approximately forty three point nine eight.",
    "What's the area of a square with sides of fifteen centimeters?",
    "The perimeter of a square with sides of nine is thirty six.",
    "What's the area of a rectangle that's eight meters by eleven meters?",
    "A triangle's area with base twelve and height nine equals fifty four.",
    "What's the circumference of a circle with diameter twelve?",
    "The area of a circle with radius four is approximately fifty point two seven.",
    "What's the perimeter of a triangle with sides six, eight, and ten?",
    "A rectangle's area that's five by thirteen is sixty five.",
    "What's the area of a circle with radius seven?",
    "The perimeter of a rectangle that's nine by fourteen is forty six.",
    "What's the area of a square with sides of eleven feet?",
    "A triangle with base fourteen and height ten has an area of seventy.",
    "What's the circumference of a circle with radius eight?",
    "The area of a rectangle that's six by fifteen is ninety.",
    # MORE WORD PROBLEMS
    "If Mary has twenty three apples and gives away seven, how many does she have left?",
    "A train travels seventy miles per hour for two and a half hours, how far does it go?",
    "If a pizza is cut into twelve slices and five are eaten, how many remain?",
    "David bought four books for fifteen dollars each, what's the total cost?",
    "If a recipe calls for three cups of flour and you're tripling it, how much do you need?",
    "A rectangle is fourteen feet long and eight feet wide, what's its area?",
    "If you have thirty dollars and spend twelve, how much money is left?",
    "Lisa runs six miles every day for ten days, how many miles total?",
    "If a class has forty two students and one quarter are absent, how many are present?",
    "A car uses three gallons of gas per hour, how much for four hours?",
    "If you need to divide thirty six cookies equally among nine people, how many each?",
    "A square garden has sides of fifteen feet, what's its perimeter?",
    "If a store has sixty items and sells twenty five, how many are left?",
    "James saves fifteen dollars per week, how much in eight months?",
    "If a triangle has sides of six, nine, and eleven, what's its perimeter?",
    "A recipe serves six people but you need to serve eighteen, how much to multiply?",
    "If you drive at sixty miles per hour for three hours, how far do you travel?",
    "A box holds thirty cans, if you have four boxes, how many cans total?",
    "If a shirt costs forty dollars and is twenty five percent off, what's the sale price?",
    "A circle has a radius of six inches, what's its approximate area?",
    # ADDITIONAL VARIETY
    "What's the greatest common factor of twelve and eighteen?",
    "The least common multiple of four and six is twelve.",
    "What's the prime factorization of twenty four?",
    "An isosceles triangle has two equal sides and two equal angles.",
    "What's the sum of the first ten positive integers?",
    "The formula for the area of a parallelogram is base times height.",
    "What's the volume of a rectangular prism that's three by four by five?",
    "To convert Celsius to Fahrenheit, multiply by nine fifths and add thirty two.",
    "What's the slope of a line that passes through points zero zero and three six?",
    "The distributive property states that a times b plus c equals a b plus a c.",
    "What's the median of the numbers five, eight, twelve, fifteen, and twenty?",
    "An equilateral triangle has all three sides equal and all three angles equal to sixty degrees.",
    "What's the range of the data set ten, fifteen, twenty, twenty five, and thirty?",
    "The commutative property of addition states that a plus b equals b plus a.",
    "What's the area of a circle with diameter ten?",
    "To find the mode, you look for the number that appears most frequently in the data set.",
    "What's the volume of a cube with edges of seven inches?",
    "The associative property states that a plus b plus c equals a plus the quantity b plus c.",
    "What's the perimeter of a regular hexagon with sides of five centimeters?",
    "The formula for the area of a triangle is one half times base times height.",
    # ADVANCED MATH - MULTIVARIABLE CALCULUS
    "To find the partial derivative of f with respect to x, you treat y as a constant and differentiate normally.",
    "The gradient of a function is a vector pointing in the direction of steepest ascent on the surface.",
    "What's the partial derivative of x squared y plus three x y squared with respect to y?",
    "A critical point occurs when all partial derivatives equal zero simultaneously.",
    "The double integral over a region gives you the volume under a surface above that region.",
    "To find the maximum or minimum of a multivariable function, you set all partial derivatives equal to zero.",
    "What's the gradient of the function f of x y equals x squared plus y squared?",
    "The second partial derivative test helps determine if a critical point is a maximum, minimum, or saddle point.",
    "When computing a double integral, you integrate with respect to one variable first, then the other.",
    "The divergence of a vector field measures how much the field spreads out or converges at a point.",
    "What's the curl of the vector field F equals x y, y z, z x?",
    "The line integral of a vector field along a curve gives you the work done by the field.",
    "Green's theorem relates a line integral around a closed curve to a double integral over the region.",
    "To find the area of a surface, you integrate the magnitude of the cross product of partial derivatives.",
    "The directional derivative tells you the rate of change of a function in a specific direction.",
    "What's the Laplacian of the function f of x y equals x squared y plus y cubed?",
    "Stokes' theorem generalizes Green's theorem to three dimensions, relating surface integrals to line integrals.",
    "The divergence theorem connects a triple integral over a volume to a surface integral over its boundary.",
    (
        "When finding extrema with constraints, you use Lagrange multipliers to incorporate the constraint into your "
        "optimization."
    ),
    "A Jacobian matrix contains all first order partial derivatives of a vector valued function.",
    # ADVANCED MATH - LINEAR ALGEBRA
    "What are the eigenvalues of the two by two matrix with rows one two and three four?",
    "An eigenvector is a nonzero vector that only changes by a scalar factor when a linear transformation is applied.",
    "The determinant of a matrix tells you how the transformation scales volumes in space.",
    "What's the rank of a matrix? It's the dimension of the column space or row space.",
    "A matrix is invertible if and only if its determinant is nonzero.",
    "The trace of a matrix is the sum of the elements on its main diagonal.",
    "What's the dot product of the vectors three four five and one two three?",
    "Two vectors are orthogonal if their dot product equals zero.",
    "The cross product of two vectors gives you a vector perpendicular to both original vectors.",
    "What's the matrix product of a two by three matrix and a three by two matrix?",
    "A basis for a vector space is a linearly independent set that spans the entire space.",
    "The dimension of a vector space equals the number of vectors in any basis for that space.",
    "What's the null space of a matrix? It's the set of all vectors that map to zero.",
    "The column space of a matrix is the span of its column vectors.",
    "A matrix is diagonalizable if it has n linearly independent eigenvectors for an n by n matrix.",
    "What's the characteristic polynomial of a matrix? It's the determinant of lambda I minus A.",
    "Singular value decomposition factors a matrix into three matrices, revealing its geometric structure.",
    "The Gram Schmidt process converts a set of linearly independent vectors into an orthogonal set.",
    "What's the inverse of a two by two matrix with elements a b c d?",
    "A linear transformation preserves vector addition and scalar multiplication.",
]

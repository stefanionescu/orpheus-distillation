"""Math prompts: long spoken expressions."""

from __future__ import annotations

EXPRESSIONS: list[str] = [
    # LONG EXPRESSIONS - Part 1
    (
        "When calculating compound interest, if you invest one thousand dollars at five percent annual interest "
        "compounded monthly for ten years, you'll end up with approximately one thousand six hundred and forty seven "
        "dollars."
    ),
    (
        "To find the area of a trapezoid, you need to add the lengths of the two parallel sides, multiply by the "
        "height, and then divide the result by two."
    ),
    (
        "The Pythagorean theorem states that in a right triangle, the square of the hypotenuse equals the sum of the "
        "squares of the other two sides."
    ),
    (
        "When solving a quadratic equation using the quadratic formula, you take negative b plus or minus the square "
        "root of b squared minus four a c, all divided by two a."
    ),
    (
        "To calculate the volume of a sphere, you multiply four thirds by pi and then multiply that result by the "
        "radius cubed."
    ),
    (
        "The derivative of a function tells you the rate of change at any given point, which is essential for "
        "understanding how quantities change over time."
    ),
    (
        "When working with percentages, remember that to find what percent one number is of another, you divide the "
        "first number by the second and multiply by one hundred."
    ),
    (
        "The area of a circle can be found by multiplying pi times the radius squared, which gives you the total space "
        "inside the circle."
    ),
    (
        "To solve a system of two equations with two unknowns, you can use substitution or elimination methods to find "
        "the values that satisfy both equations simultaneously."
    ),
    (
        "The sum of the angles in any triangle always equals one hundred eighty degrees, regardless of whether it's "
        "equilateral, isosceles, or scalene."
    ),
    (
        "When calculating the surface area of a rectangular prism, you need to find the area of all six faces and add "
        "them together."
    ),
    (
        "The quadratic formula is negative b plus or minus the square root of b squared minus four a c, all divided by "
        "two a."
    ),
    (
        "To find the midpoint between two points on a coordinate plane, you average the x coordinates and average the "
        "y coordinates separately."
    ),
    (
        "The slope of a line can be calculated by taking the change in y divided by the change in x between any two "
        "points on that line."
    ),
    (
        "When working with fractions, to add or subtract them you need to find a common denominator before performing "
        "the operation."
    ),
    (
        "The volume of a cylinder equals pi times the radius squared times the height, which gives you the total space "
        "inside the cylinder."
    ),
    (
        "To calculate compound interest, you multiply the principal by one plus the interest rate raised to the power "
        "of the number of compounding periods."
    ),
    (
        "The area of a parallelogram can be found by multiplying the base times the height, similar to finding the "
        "area of a rectangle."
    ),
    (
        "When solving exponential equations, you often need to use logarithms to isolate the variable that's in the "
        "exponent position."
    ),
    "The perimeter of any polygon is simply the sum of the lengths of all its sides added together.",
    # LONG EXPRESSIONS - Part 2
    (
        "To find the distance between two points in three dimensional space, you use the three dimensional version of "
        "the distance formula."
    ),
    (
        "The law of cosines states that c squared equals a squared plus b squared minus two a b times the cosine of "
        "angle C."
    ),
    (
        "When calculating the area of a sector of a circle, you multiply the fraction of the circle by pi times the "
        "radius squared."
    ),
    (
        "The integral of a function gives you the area under the curve between two points, which has many practical "
        "applications."
    ),
    (
        "To solve a right triangle when you know two sides, you can use the Pythagorean theorem or trigonometric "
        "functions depending on what you're looking for."
    ),
    (
        "The formula for finding the nth term of an arithmetic sequence is a sub n equals a sub one plus n minus one "
        "times d."
    ),
    (
        "When working with complex numbers, remember that i squared equals negative one, which allows you to work with "
        "square roots of negative numbers."
    ),
    "The surface area of a sphere can be calculated by multiplying four times pi times the radius squared.",
    (
        "To find the angle between two vectors, you use the dot product formula and divide by the product of their "
        "magnitudes."
    ),
    (
        "The chain rule in calculus states that the derivative of a composite function equals the derivative of the "
        "outer function times the derivative of the inner function."
    ),
    "When calculating the volume of a cone, you multiply one third times pi times the radius squared times the height.",
    (
        "The quadratic formula allows you to solve any quadratic equation by plugging the coefficients a, b, and c "
        "into the formula."
    ),
    (
        "To find the area of a triangle using Heron's formula, you first calculate the semi perimeter, then use that "
        "in the formula."
    ),
    (
        "The derivative of a position function gives you the velocity function, and the derivative of velocity gives "
        "you acceleration."
    ),
    "When working with logarithms, remember that the log base b of x equals y means that b to the power of y equals x.",
    "The area of a rhombus can be found by multiplying the lengths of the two diagonals and dividing by two.",
    (
        "To calculate the standard deviation of a data set, you find the mean, subtract it from each value, square "
        "those differences, find the average, and take the square root."
    ),
    (
        "The fundamental theorem of calculus connects differentiation and integration, showing that they are inverse "
        "operations of each other."
    ),
    (
        "When solving trigonometric equations, you often need to use identities like sine squared plus cosine squared "
        "equals one to simplify expressions."
    ),
    "The volume of a pyramid equals one third times the area of the base times the height of the pyramid.",
    # LONG EXPRESSIONS - Part 3
    (
        "To find the equation of a line when you know two points, you first calculate the slope, then use point slope "
        "form."
    ),
    (
        "The law of sines states that the ratio of a side to the sine of its opposite angle is constant for all three "
        "sides."
    ),
    (
        "When calculating the area under a curve using integration, you're essentially finding the sum of infinitely "
        "many infinitely small rectangles."
    ),
    "The product rule in calculus states that the derivative of f times g equals f prime times g plus f times g prime.",
    (
        "To solve a system of linear equations using matrices, you can use row operations to reduce the matrix to row "
        "echelon form."
    ),
    "The area of an ellipse can be found by multiplying pi times the semi major axis times the semi minor axis.",
    (
        "When working with limits in calculus, you're finding what value a function approaches as the input approaches "
        "a particular value."
    ),
    (
        "The quotient rule states that the derivative of f divided by g equals g times f prime minus f times g prime, "
        "all divided by g squared."
    ),
    (
        "To find the angle of elevation or depression in trigonometry, you use the inverse trigonometric functions "
        "like arc sine or arc tangent."
    ),
    (
        "The formula for finding the sum of an arithmetic series is n divided by two times the first term plus the "
        "last term."
    ),
    (
        "When calculating the area of a regular polygon, you multiply the apothem times the perimeter and then divide "
        "by two."
    ),
    (
        "The mean value theorem states that for a continuous function on a closed interval, there exists a point where "
        "the instantaneous rate of change equals the average rate of change."
    ),
    "To solve exponential growth or decay problems, you use the formula A equals P times e to the power of r times t.",
    "The area of a triangle can also be found using the formula one half times a times b times the sine of angle C.",
    (
        "When working with vectors, the magnitude can be found using the square root of the sum of the squares of the "
        "components."
    ),
    (
        "The intermediate value theorem states that if a continuous function takes on two values, it must take on "
        "every value between them."
    ),
    (
        "To find the equation of a circle given its center and radius, you use x minus h squared plus y minus k "
        "squared equals r squared."
    ),
    "The sum of the interior angles of any polygon with n sides equals n minus two times one hundred eighty degrees.",
    (
        "When calculating the volume of a frustum of a cone, you need to use a more complex formula involving both "
        "radii and the height."
    ),
    (
        "The derivative of the natural logarithm function equals one divided by x, which makes it useful for solving "
        "many types of problems."
    ),
    # LONG EXPRESSIONS - Part 4
    "To find the area of a segment of a circle, you subtract the area of the triangle from the area of the sector.",
    (
        "The binomial theorem allows you to expand expressions like x plus y raised to the nth power without having to "
        "multiply it out manually."
    ),
    (
        "When solving optimization problems in calculus, you find the critical points by setting the derivative equal "
        "to zero and then check which gives the maximum or minimum."
    ),
    (
        "The area of a trapezoid can be found by averaging the lengths of the two parallel sides and multiplying by "
        "the height."
    ),
    (
        "To calculate the distance traveled when you have a velocity function, you integrate the velocity function "
        "over the time interval you're interested in."
    ),
    (
        "The formula for finding the volume of a torus involves squaring the radius and multiplying by two pi squared "
        "times the major radius."
    ),
    (
        "When working with polar coordinates, you convert between rectangular and polar forms using x equals r cosine "
        "theta and y equals r sine theta."
    ),
    (
        "The squeeze theorem states that if one function is always less than or equal to another, and they both "
        "approach the same limit, then the middle function must also approach that limit."
    ),
    (
        "To find the area between two curves, you integrate the difference between the upper function and the lower "
        "function over the interval where they intersect."
    ),
    (
        "The formula for compound interest is A equals P times one plus r over n raised to the power of n times t, "
        "where n is the number of compounding periods per year."
    ),
    (
        "When calculating the surface area of a cone, you add the area of the circular base to the area of the lateral "
        "surface, which involves the slant height."
    ),
    (
        "The derivative of an inverse function can be found using the formula one divided by the derivative of the "
        "original function evaluated at the corresponding point."
    ),
    (
        "To solve a differential equation, you're finding a function whose derivative satisfies a given relationship, "
        "which often requires integration and applying initial conditions."
    ),
    (
        "The area of a regular hexagon can be found by dividing it into six equilateral triangles and calculating the "
        "area of one triangle times six."
    ),
    (
        "When working with sequences and series, an arithmetic sequence has a constant difference between terms, while "
        "a geometric sequence has a constant ratio between terms."
    ),
    (
        "The fundamental theorem of algebra states that every polynomial equation of degree n has exactly n complex "
        "roots, counting multiplicities."
    ),
    (
        "To find the angle between two lines, you use the formula involving the slopes of the lines and the tangent of "
        "the angle between them."
    ),
    (
        "The volume of a parallelepiped can be found using the scalar triple product of three vectors that define its "
        "edges."
    ),
    (
        "When calculating the area of a region bounded by polar curves, you integrate one half times r squared with "
        "respect to theta over the appropriate interval."
    ),
    (
        "The l'Hospital's rule allows you to evaluate limits that result in indeterminate forms like zero over zero or "
        "infinity over infinity by taking derivatives."
    ),
]

"""Math prompts: equations spelled out in words."""

from __future__ import annotations

EQUATIONS: list[str] = [
    # SPELLED OUT EQUATIONS - Part 1
    (
        "If you take seventeen plus twenty three and then subtract eight, you get thirty two as your final answer "
        "after doing the arithmetic."
    ),
    (
        "When you multiply fourteen by six and then add nineteen to that result, you end up with one hundred and three "
        "as your total."
    ),
    (
        "The equation three x squared plus five x minus twelve equals zero can be solved using the quadratic formula "
        "to find two solutions."
    ),
    (
        "If you divide one hundred forty four by twelve and then multiply by seven, your result is eighty four after "
        "completing both operations."
    ),
    (
        "Solving the system where two x plus three y equals thirteen and x minus y equals two gives you x equals three "
        "and y equals one."
    ),
    (
        "The expression forty five minus seventeen plus thirty two minus eight equals fifty two when you evaluate it "
        "from left to right."
    ),
    (
        "When you calculate nine squared plus four cubed, you get eighty one plus sixty four, which equals one hundred "
        "forty five total."
    ),
    "If x plus seven equals nineteen, then x equals twelve, and if you then compute x times three, you get thirty six.",
    (
        "The sum of the first five prime numbers, which are two, three, five, seven, and eleven, equals twenty eight "
        "in total."
    ),
    (
        "Evaluating the expression two times the quantity eight plus six gives you two times fourteen, which equals "
        "twenty eight."
    ),
    (
        "If you have the equation five y minus fifteen equals thirty five, solving for y gives you y equals ten as the "
        "answer."
    ),
    (
        "The product of negative three and negative seven equals positive twenty one because multiplying two negatives "
        "gives a positive result."
    ),
    (
        "When you compute the square root of one hundred sixty nine, you get thirteen, and thirteen squared gives you "
        "one hundred sixty nine."
    ),
    (
        "If a equals four and b equals nine, then a squared plus b squared equals sixteen plus eighty one, which is "
        "ninety seven."
    ),
    (
        "The expression twenty seven divided by three plus eighteen divided by two equals nine plus nine, giving you "
        "eighteen total."
    ),
    (
        "Solving four x plus eight equals thirty two means subtracting eight to get four x equals twenty four, so x "
        "equals six."
    ),
    (
        "When you calculate fifteen percent of two hundred forty, you multiply two forty by zero point one five to get "
        "thirty six."
    ),
    (
        "The cube of four is sixty four, and if you add the square of eight, which is also sixty four, you get one "
        "hundred twenty eight."
    ),
    (
        "If you take the absolute value of negative twenty three and add it to positive seventeen, your result is "
        "forty in total."
    ),
    (
        "The expression three to the fourth power equals three times three times three times three, which computes to "
        "eighty one."
    ),
    (
        "Solving the inequality two x minus five is greater than eleven gives you x is greater than eight after adding "
        "five and dividing by two."
    ),
    (
        "When you compute the factorial of five, you multiply five times four times three times two times one to get "
        "one hundred twenty."
    ),
    (
        "If the perimeter of a square is forty eight centimeters, each side is twelve centimeters, and the area is one "
        "hundred forty four square centimeters."
    ),
    (
        "The equation y equals three x minus seven passes through the point four, five because three times four minus "
        "seven equals five."
    ),
    (
        "When you simplify the fraction forty two over fifty six, you divide both by fourteen to get three over four "
        "in lowest terms."
    ),
    (
        "If you invest one thousand dollars at six percent simple interest for five years, you earn three hundred "
        "dollars in interest total."
    ),
    (
        "The sum of interior angles in a hexagon is calculated as six minus two times one hundred eighty, which equals "
        "seven hundred twenty degrees."
    ),
    (
        "Solving the proportion three over eight equals x over forty gives you x equals fifteen by cross multiplying "
        "and dividing."
    ),
    (
        "When you evaluate negative two cubed, you get negative eight, but negative two squared gives you positive "
        "four instead."
    ),
    (
        "The distance formula gives you the square root of the quantity x two minus x one squared plus y two minus y "
        "one squared."
    ),
    (
        "If you add one half plus two thirds plus one sixth, you get a common denominator of six and the sum is eight "
        "sixths or four thirds."
    ),
    (
        "The equation of a circle centered at three, negative two with radius five is x minus three squared plus y "
        "plus two squared equals twenty five."
    ),
    (
        "When you solve the quadratic x squared minus five x plus six equals zero, you factor it as x minus two times "
        "x minus three equals zero."
    ),
    (
        "If a triangle has angles measuring forty five, sixty, and seventy five degrees, the sum is one hundred eighty "
        "degrees as expected."
    ),
    (
        "The slope between points two, seven and six, fifteen is calculated as fifteen minus seven over six minus two, "
        "which equals two."
    ),
    # SPELLED OUT EQUATIONS - Part 2
    (
        "Evaluating the expression four factorial divided by two factorial gives you twenty four divided by two, which "
        "equals twelve."
    ),
    (
        "If you compute the arithmetic mean of twelve, eighteen, twenty four, and thirty, you add them to get eighty "
        "four and divide by four for twenty one."
    ),
    (
        "The quadratic formula states that x equals negative b plus or minus the square root of b squared minus four a "
        "c, all over two a."
    ),
    (
        "When you solve three to the x power equals eighty one, you recognize that eighty one is three to the fourth, "
        "so x equals four."
    ),
    (
        "If the hypotenuse of a right triangle is thirteen and one leg is five, the other leg is twelve by the "
        "Pythagorean theorem."
    ),
    "The expression log base two of thirty two equals five because two raised to the fifth power equals thirty two.",
    (
        "When you compute the determinant of the matrix with rows one, two and three, four, you get one times four "
        "minus two times three, which is negative two."
    ),
    (
        "If you solve the equation e to the x equals seven point three eight nine, then x equals approximately two "
        "since e squared is about seven point four."
    ),
    (
        "The binomial expansion of x plus y cubed equals x cubed plus three x squared y plus three x y squared plus y "
        "cubed."
    ),
    "When you integrate two x with respect to x, you get x squared plus a constant of integration, denoted as C.",
    (
        "If the discriminant b squared minus four a c equals zero, the quadratic equation has exactly one real "
        "solution, called a repeated root."
    ),
    (
        "The Taylor series for e to the x around zero is one plus x plus x squared over two factorial plus x cubed "
        "over three factorial and so on."
    ),
    (
        "When you differentiate x cubed plus four x squared minus seven x plus two, you get three x squared plus eight "
        "x minus seven."
    ),
    (
        "If you compute the dot product of vectors three, four and negative two, five, you get three times negative "
        "two plus four times five, which is fourteen."
    ),
    (
        "The formula for combinations is n factorial divided by k factorial times n minus k factorial, often written "
        "as n choose k."
    ),
    (
        "When you solve the matrix equation A X equals B, you multiply both sides by A inverse to get X equals A "
        "inverse times B."
    ),
    (
        "If the limit of f of x as x approaches three equals seven, the function approaches seven as the input gets "
        "arbitrarily close to three."
    ),
    (
        "The cross product of vectors i plus two j and three i minus j equals negative one times k minus six times k, "
        "giving negative seven k."
    ),
    (
        "When you compute the integral of sine x from zero to pi, you get negative cosine x evaluated from zero to pi, "
        "which equals two."
    ),
    (
        "If you apply the chain rule to differentiate sine of three x squared, you get cosine of three x squared times "
        "six x."
    ),
    (
        "The geometric series sum formula is a times one minus r to the n divided by one minus r, where a is the first "
        "term and r is the ratio."
    ),
    (
        "When you solve the differential equation dy dx equals y, the general solution is y equals C times e to the x "
        "for some constant C."
    ),
    (
        "If you compute the Laplacian of x squared plus y squared, you get the sum of the second partial derivatives, "
        "which is two plus two equals four."
    ),
    (
        "The formula for permutations is n factorial divided by n minus k factorial, giving the number of ordered "
        "arrangements of k items from n."
    ),
    (
        "When you evaluate the limit of sine x over x as x approaches zero, you get one by applying L'Hopital's rule "
        "or using the squeeze theorem."
    ),
    (
        "If you solve two x plus three y equals twelve and four x minus y equals five simultaneously, you get x equals "
        "two and y equals three."
    ),
    (
        "The volume of a cone with radius four and height nine is one third times pi times sixteen times nine, which "
        "equals forty eight pi."
    ),
    (
        "When you compute the standard deviation of the data set two, four, four, four, five, five, seven, nine, you "
        "first find the variance then take the square root."
    ),
    (
        "If the probability of event A is zero point four and event B is zero point three, and they're independent, P "
        "of A and B is zero point one two."
    ),
    (
        "The formula for arc length is the integral from a to b of the square root of one plus f prime of x squared, "
        "with respect to x."
    ),
]

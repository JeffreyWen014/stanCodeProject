"""
File: quadratic_solver.py
Name: JeffreyWen
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
    """
    This program allows the user to input
    the coefficients of a quadratic equation
    and calculates its real solutions.
    """

    # Print program header
    print("stanCode Quadratic Solver!")

    # Get user input for coefficients a, b, c
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))

    # If a is 0, it's not a quadratic equation
    if a == 0:
        print("This is not a quadratic equation.")
        return

    # Calculate the discriminant (b² - 4ac)
    discriminant = b * b - 4 * a * c

    # Case 1: Two distinct real roots
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Two roots: " + str(root1) + ", " + str(root2))

    # Case 2: One real root (discriminant = 0)
    elif discriminant == 0:
        root = -b / (2 * a)
        print("One root: " + str(root))

    # Case 3: No real roots (discriminant < 0)
    else:
        print("No real roots")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()

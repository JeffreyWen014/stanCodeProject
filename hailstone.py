"""
File: hailstone.py
Name: JeffreyWen
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program prompts the user for input and calls
    the Hailstone sequence function, which causes
    any integer eventually become 1.
    """

    # Print the program introduction
    print("This program computes Hailstone sequences.\n")

    # Ask the user for a starting number
    num = int(input("Enter a number: "))
    step = 0  # Initialize step counter

    # Repeat until the number reaches 1
    while num != 1:
        # If the number is odd
        if num % 2 == 1:
            print(str(num) + " is odd, so I make 3n+1: " + str(num * 3 + 1))
            num = num * 3 + 1

        else:
            # If the number is even
            print(str(num) + " is even, so I take half: " + str(num // 2))
            num = num // 2

        step += 1  # Count the step

    # Print the total number of steps
    print("It took " + str(step) + " steps to reach 1.")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()

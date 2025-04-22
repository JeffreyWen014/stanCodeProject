"""
File: extension2_number_checker.py
Name: JeffreyWen
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""

# Constant to signal user wants to exit the program
EXIT = -100


def main():
    print("Welcome to the number checker!")

    while True:
        # Ask user for input
        n = int(input("n: "))

        # Check for exit signal
        if n == EXIT:
            print("Have a good one!")
            break

        else:
            total_of_factors = 0  # Sum of all proper divisors
            count = 1  # Start checking from 1

            # Find and sum all proper divisors of n
            while count < n:
                if n % count == 0:
                    total_of_factors += count
                count += 1

            # Classify the number based on the sum of its divisors
            if total_of_factors > n:
                print(str(n) + " is an abundant number.")  # Sum > n
            elif total_of_factors == n:
                print(str(n) + " is a perfect number.")  # Sum == n
            else:
                print(str(n) + " is a deficient number.")  # Sum < n


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

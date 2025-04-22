"""
File: extension1_factorial.py
Name: JeffreyWen
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""

# Constant to signal user wants to exit the program
EXIT = -100


def main():
    # Print welcome message
    print("Welcome to stanCode factorial master!")

    while True:
        # Ask user for input
        n = int(input("Give me a number, and I will list the answer of factorial: "))

        # Check for exit signal
        if n == EXIT:
            print("- - - - - - See ya! - - - - - -")
            break

        else:
            count = 1         # Starting from 1
            answer = 1        # Initial value of factorial (1! = 1)

            # Compute factorial by multiplying 1 × 2 × 3 × ... × n
            while count < n:
                count += 1
                answer *= count  # Multiply current count to the total

            # Output the result
            print("Answer: " + str(answer))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

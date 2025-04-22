"""
File: prime_checker.py
Name: JeffreyWen
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

END = -100


def main():
    print("Welcome to the prime checker!")

    while True:
        # Ask the user for a number
        n = int(input("n: "))

        # If user enters the sentinel value, exit the loop
        if n == END:
            print("Have a good one!")
            break

        # Special case for 2 (the only even prime)
        if n == 2:
            print("2 is a prime number.")
        else:
            count = 2
            # Check if n has any factor between 2 and n-1
            while count < n:
                if n % count == 0:
                    print(str(n) + " is not a prime number.")
                    break
                count += 1
            else:
                # If loop completes without break, it's prime
                print(str(n) + " is a prime number.")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()

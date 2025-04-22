"""
File: extension3_triangular_checker.py
Name: JeffreyWen
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    print("Welcome to the triangular number checker!")

    while True:
        # Ask user for input
        n = int(input("n: "))

        # Check for exit signal
        if n == EXIT:
            print("Have a good one!")
            break

        else:
            count = 1  # Start checking from the first triangular number (1)
            t_n = 0  # t_n will store the current triangular number

            # Keep generating triangular numbers until t_n >= n
            while t_n < n:
                t_n = count * (count+1) / 2  # Formula for nth triangular number
                if n == t_n:
                    # If match is found, n is a triangular number
                    print(str(n) + " is a triangular number.")
                    break
                count += 1  # Try next triangular number

            # If we pass the number without finding an exact match
            if t_n > n:
                print(str(n) + " is not a triangular number.")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

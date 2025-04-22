"""
File: extension4_narcissistic_checker.py
Name: JeffreyWen
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    print("Welcome to the narcissistic number checker!")

    while True:
        # Ask user for input
        n = int(input("n: "))

        # Check for exit signal
        if n == EXIT:
            print("Have a good one!")
            break

        else:
            number_of_digits = 1  # Counter for how many digits in the number

            # Keep increasing the digit count until 10^digit_count exceeds n
            while 10 ** number_of_digits <= n:
                number_of_digits += 1

            narcissistic_total = 0  # To accumulate the sum of powered digits
            original = n  # Save the original number for comparison

            # Loop to extract each digit and raise it to the power of digit count
            while n > 0:
                digit = n % 10  # Get the last digit
                narcissistic_total += digit ** number_of_digits  # Add powered digit to total
                n //= 10  # Remove last digit

            # Check if the number equals the narcissistic total
            if narcissistic_total == original:
                print(str(original) + " is a narcissistic number.")
            else:
                print(str(original) + " is not a narcissistic number.")


if __name__ == '__main__':
    main()

"""
File: guess_my_number.py
Name: JeffreyWen
-----------------------------
This program plays a Console game
"Guess My Number" which asks user
to input a number until he/she gets it
"""

# This number controls when to stop the game
SECRET = 45


def main():
    upper_bound = 99
    lower_bound = 0
    print("Guess number between 0-99!")
    while True:
        guess_number = int(input("Your guess: "))
        if guess_number > SECRET:
            upper_bound = guess_number
            print("To high!", end="")
            print("Guess between " + str(lower_bound) + "-" + str(upper_bound) + ": ")
        elif guess_number < SECRET:
            lower_bound = guess_number
            print("Too low!", end="")
            print("Guess between " + str(lower_bound) + "-" + str(upper_bound) + ": ")
        else:
            break
    print("Congrats! The answer is " + str(SECRET))


"""
def main():
    print("Guess number between 0-99!")
    guess_number = int(input("Your guess: "))
    while guess_number != SECRET:
        if guess_number > SECRET:
            print("To high!")

        else:
            print("Too low!")
        guess_number = int(input("Your guess: "))
    print("Congrats! The answer is " + str(SECRET))
"""

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()

"""
File: StepUp.py
Name: JeffreyWen
------------------------
This file shows Karel picking up
the beeper at Street 1 Avenue 2,
putting it 99 times onto Street 2 Avenue 4.
Karel will be facing East at Street
2 Avenue 5 at the end of this program.
"""

from karel.stanfordkarel import *


def main():
    # algorithm
    move()  # move forward
    pick_beeper()  # pick up 'beeper'
    move()
    turn_left()
    move()
    turn_right()
    move()
    put_beeper_99()
    move()


def turn_right(): #define new function
    for i in range(3): #for loop
        turn_left()


def put_beeper_99():
    """
    put 99 beepers
    """
    for i in range(99):
        put_beeper()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)

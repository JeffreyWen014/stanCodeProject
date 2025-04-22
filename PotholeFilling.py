"""
File: PotholeFilling.py
Name: JeffreyWen
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *

from StepUp import *  # import code from another file


def main():
    for i in range(3):  # for loop
        go_in()
        put_beeper_99()
        go_out()


def go_in():
    """
    pre-condition:
    Karel is at the upper left
    of the pothhole facing East

    post-condition:
    Karel is in the pothhole
    facing South
    """
    move()
    turn_right()
    move()


def go_out():
    """
    pre-condition:
    Karel is in the pothhole
    facing South

    post-condition:
    Karel is at the upper left
    of the pothhole facing East
    """
    turn_left()
    turn_left()
    move()
    turn_right()
    move()


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)

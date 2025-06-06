"""
File: CollectNewspaperKarel.py
Name: JeffreyWen
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition & Post-condition:Karel is at (4,3) facing East
    """
    move_out()
    take_back_home()


def move_out():
    """
    Pre-condition:Karel is at (4,3), facing East
    Post-condition:Karel is at (3,6), facing East
    """
    for i in range(2):
        move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()


def take_back_home():
    """
    Pre-condition:Karel is at (3,6), facing East
    Post-condition:Karel is at (4,3), facing East
    """
    turn_left()
    turn_left()
    for i in range(3):
        move()
    turn_right()
    move()
    turn_right()
    put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)

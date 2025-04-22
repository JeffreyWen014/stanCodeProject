"""
File: Steeplechase.py
Name: JeffreyWen
---------------------------------
This program allows Karel to cross a finite
number of steeples
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(7):  # There are 7 steeples
        while front_is_clear():  # Check if there is a wall ahead
            move()
        jump()
        down()


def jump():
    """
    Pre-condition: Karel is at the bottom left of the wall, facing East
    Post-condition: Karel is at the upper left of the wall, facing East
    """
    if not front_is_clear():
        turn_left()
        while not right_is_clear():
            move()
        turn_right()


def down():
    """
    Pre-condition: Karel is at the upper left of the wall, facing East
    Post-condition: Karel is at the bottom right of the wall, facing East
    """
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)

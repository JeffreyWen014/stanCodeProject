"""
File: CheckerboardKarel.py
Name: JeffreyWen
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel paints the world like a checkerboard using
    beepers, no matter how big the world is.
    """
    while front_is_clear():
        fill_one_line()
        next_line()


def fill_one_line():
    """
    Karel places beepers in a spaced pattern on each row
    """
    while front_is_clear():
        put_beeper()
        move()
        if front_is_clear():  # Avoid hitting the wall
            move()
            if not front_is_clear():  # Avoid OBOB
                put_beeper()


def next_line():
    if facing_east():
        if not on_beeper():  # If the row has even number of squares
            turn_left()
            if front_is_clear():
                move()
                turn_left()
        else:  # If the row has odd number of squares
            turn_left()
            if front_is_clear():
                move()
                turn_left()
                move()
    else:
        if not on_beeper():  # If the row has even number of squares
            turn_right()
            if front_is_clear():
                move()
                turn_right()
        else:  # If the row has odd number of squares
            turn_right()
            if front_is_clear():
                move()
                turn_right()
                move()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)

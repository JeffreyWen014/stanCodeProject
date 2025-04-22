"""
File: MidpointKarel.py
Name: JeffreyWen
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    # Special case: 1x1 world, just place a beeper and stop
    if not front_is_clear():
        put_beeper()
        return

    move_to_end_and_mark()  # Mark both ends with beepers
    find_midpoint()  # Move beepers inward to find the center
    clean_side()  # Clean both left and right side beepers
    leave_one_beeper()  # Ensure only one beeper is left at the midpoint


def move_to_end_and_mark():
    # Place a beeper at the starting point
    put_beeper()
    # Move to the end of the street
    while front_is_clear():
        move()
    # Place a beeper at the end point
    put_beeper()
    # Turn around and move one step back to start midpoint search
    turn_around()
    move()


def find_midpoint():
    # Keep moving beepers inward until we reach the center
    while not on_beeper():
        put_beeper()
        if front_is_clear():
            move()
        move_to_beeper()
        turn_around()
        if front_is_clear():
            move()


def clean_side():
    # Clean one side
    if front_is_clear():
        move()
        while front_is_clear():
            pick_beeper()
            move()
        pick_beeper()
        turn_around()
        move_to_beeper()

    # Clean the other side
    if front_is_clear():
        move()
        while front_is_clear():
            pick_beeper()
            move()
        pick_beeper()
        turn_around()
        move_to_beeper()


def leave_one_beeper():
    # Ensure only one beeper remains at the midpoint
    turn_around()
    if front_is_clear():
        move()
        if on_beeper():
            pick_beeper()
    turn_around()
    move()


def move_to_beeper():
    # Move forward until standing on a beeper
    while not on_beeper():
        move()


def turn_around():
    # Turn 180 degrees
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)

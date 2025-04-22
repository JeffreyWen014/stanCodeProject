"""
File: StoneMasonKarel.py
Name: JeffreyWen
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *
from CollectNewspaperKarel import *


def main():
    """
    StoneMasonKarel builds several columns with beepers.
    """
    while front_is_clear():
        """
        StoneMasonKarel repairs the left column of each doorway.
        """
        fix_door()
        go_down()
        for i in range(4):  # Karel move to the next column
            move()
    fix_door()  # StoneMasonKarel repairs the right column of the last doorway eventually.
    go_down()


def fix_door():
    """
    Pre-condition:Karel is at the below of the column, facing East
    Post-condition:Karel is at the upper of the column, Facing North
    """
    turn_left()  # Karel turns his face up.
    for i in range(4):  # Karel repairs the columns as he moves upward.
        if not on_beeper():  # Check if there is a beeper underfoot.
            put_beeper()
        move()
    if not on_beeper():  # Avoid OBOB
        put_beeper()


def go_down():
    """
    Pre-condition:Karel is at the upper of the column, Facing North
    Post-condition:Karel is at the below of the column, facing East
    """
    turn_left()  # Karel turns his face down.
    turn_left()
    for i in range(4):  # Move down
        move()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)

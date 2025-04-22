"""
File: BeeperRow.py
Name: JeffreyWen
-------------------------
This program makes Karel fill up
Street 1 with beepers
(This program should be world insensitive)
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: Karel is at the far left of the street
    Post-condition: Karel is at the far right of the street
    """
    while front_is_clear():  # Indefinite loop
        put_beeper()
        move()
    put_beeper()  # Avoid OBOB


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)

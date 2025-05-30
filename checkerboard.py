"""
File: checkerboard.py
Name: JeffreyWen
------------------------
This program prints an alternating 
checkerboard pattern on Console
by nested for loop.
"""

# These constants control the size of the checkerboard
ROW = 5  # The number of rows
COL = 8  # The number of cols


def main():
    for i in range(ROW):
        for j in range(COL):
            if (i + j) % 2 == 0:  # i + j is even
                print("A", end="")
            else:  # i + j is odd
                print("*", end="")
        print("")


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()

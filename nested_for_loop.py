"""
File: nested_for_loop.py
Name: JeffreyWen
------------------------
This program shows students the basic
concepts of nested (double) for loop
by printing a 4-row-3-col rectangle
"""

# These constants control the diameter of the rectangle
ROW = 4  # The number of rows
COL = 3  # The number of cols


def main():
	for i in range(ROW):  # i == 0 1 2 3
		for j in range(COL):  # j == 0 1 2
			print("#", end="")
		print("")  # line break


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()

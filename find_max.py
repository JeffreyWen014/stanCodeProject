"""
File: find_max.py
Name: JeffreyWen
--------------------------
This program finds the maximum among
all the user inputs. Students can refer to
this file when they are doing Problem 4
in Assignment 2
"""

# This constant controls when to stop
EXIT = -1


def main():
    """
    This program finds the maximum among
    user inputs
    """
    print("This program finds the maximum (or -1 to quit)")
    data = int(input("data: "))
    if data == EXIT:
        print("No data.")
    else:
        maximum = data
        while True:
            data = int(input("data: "))
            if data == EXIT:
                break
            if data > maximum:
                maximum = data
        print("The maximum is " + str(maximum))


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()

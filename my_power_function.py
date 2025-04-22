"""
File: my_power_function.py
Name: JeffreyWen
-------------------------------
This program shows students how to 
make their own functions by defining
def my_power(a, b)
"""


def main():
	print('This program prints a to the power of b.')
	a = int(input('a: '))
	b = int(input('b: '))
	print(my_power(a, b))


def my_power(a, b):
	ans = 1
	for i in range(b):
		ans *= a
	return ans


"""
Alternative:

def my_power(a, b):  
	return a ** b
"""

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()

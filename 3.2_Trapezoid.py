"""
TRAPEZOID PROGRAM
-------------------
Create a new program that will ask the user for the information needed to find the area of a trapezoid, and then print the area.

Test with the following:

base 1: 2       base 2: 3    height: 4    area: 10
base 1: 5       base 2: 7    height: 2    area: 12
base 1: 1       base 2: 2    height: 3    area: 4.5
base 1: 7       base 2: 2    height: 4    area: 18
"""
print()
print("Welcome to the area of a trapezoid calculator")
print()
b1 = float(input("Please enter a base:"))
print()
b2 = float(input("Please enter another base:"))
print()
hei=float(input("Please enter a height:"))
area = ((b1+b2)/2*hei)
print()
print("The area of your trapezoid is", area)

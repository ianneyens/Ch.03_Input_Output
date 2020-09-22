'''
TEMPERATURE PROGRAM
-------------------
Create a program that asks the user for a temperature in Fahrenheit, and then prints the temperature in Celsius.

Test with the following:

In: 32  Out: 0
In: 212  Out: 100
In: 52  Out: 11.1
In: 25  Out: -3.9
In: -40  Out: -40 Please tell me what this output is!

'''

print()
print("Welcome to the Fahrenheit-Celsius Converter")
print()
cel=float(input("Please enter a temperature in Fahrenheit:"))
print("Your temperature in Celsius is", (cel-32)*5/9)

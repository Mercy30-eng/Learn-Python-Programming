#!/usr/bin/python3
from math import pi         # Import the 'pi' constant from the 'math' module to calculate the area of a circle
r = float(input("Enter the radius of the circle:"))
Area = pi * r ** 2
print("Area of the circle with radius " + str(r) + " is: " + str(Area))

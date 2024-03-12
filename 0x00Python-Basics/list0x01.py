#!/usr/bin/python3
# Prompt the user to input a sequence of comma-separated numbers and store it in the 'values' variable
values = input("Input some comma-separated numbers: ")
list = values.split(",")    # Split the 'values' string into a list using commas as separators and store it in the 'list' variable 
tuple = tuple(list)         # Convert the 'list' into a tuple and store it in the 'tuple' variable
print('List : ', list)      # Print the list
print('Tuple : ', tuple)    # Print the tuple

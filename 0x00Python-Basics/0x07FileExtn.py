#!/usr/bin/python3
# Prompt the user to input a filename and store it in the 'filename' variable
filename = input ("Enter the file name: ")
f_extn = filename.split(".")    # Split the 'filename' string into a list using the period (.) as a separator and store it in the 'f_extns' variable
print("The extension of the file is : " + repr(f_extn[-1]))    #the repr() function is used to obtain a string representation of the last element in the 'f_extn' list. i

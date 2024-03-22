#!/usr/bin/python3

#You can use the os module in Python to list all the files in a directory
import os                          
# Specify the directory path
directory_path = '/com.docker.devenvironments.code/Learn-Python-Programming/0x00Python-Basics'      #Replace this with your actual directory path
files = os.listdir(directory_path) # List all files in the specified directory using the 'os.listdir' function
for file in files:                  # Print the list of files
    print(file)

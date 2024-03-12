#!/usr/bin/python3
import datetime #Import the 'datetime' module to work with date and time
now = datetime.datetime.now() #Get the current date and time
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S")) # Use the 'strftime' method to format the datetime object as a string with the desired format

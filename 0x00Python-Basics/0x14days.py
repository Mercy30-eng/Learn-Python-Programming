#!/usr/bin/python3
#Python datetime.date(year, month, day) 
from datetime import date  # Import the 'date' class from the 'datetime' module

f_date = date(2014, 7, 2)   #Define a start date as July 2, 2014
l_date = date(2014, 7, 11)  # Define an end date as July 11, 2014

delta = l_date - f_date     # Calculate the difference between the end date and start date

print(delta.days)           # Print the number of days in the time difference

#  Write a Python program to display calendar.

import calendar

year = int(input("Enter the Year :"))
month = int(input("Enter the month:"))
 

cal = calendar.month(year, month)

print(cal)

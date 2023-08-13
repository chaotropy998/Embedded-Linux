#Write a script that prints the calendar of a certain month in a certain year

import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

print(calendar.month(year, month))

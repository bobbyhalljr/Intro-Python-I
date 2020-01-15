"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# month %B
# month = datetime.now()
# print(month.strftime("%B"))

# year %Y
# year = datetime.now()
# print(year.strftime("%Y"))

# cal_year = calendar.LocaleTextCalendar(calendar.SUNDAY)
# print(cal_year.formatyear(2020, 2, 1, 1, 3))

# cal_month = calendar.LocaleTextCalendar(locale='en_US')
# current_month = cal_month.prmonth(2020, 7)

# user input
# input('Enter a month and year: ')

# prints current month as calendar
def cal_month():
  month_locale = calendar.LocaleTextCalendar(locale='en_US')
  print(month_locale.prmonth(2020, 1))

# prints current year as calendar
def cal_year():
  year_locale = calendar.LocaleTextCalendar(calendar.SUNDAY)
  print(year_locale.formatyear(2020, 2, 1, 1, 3))

# user = input('please enter a month and year: ')

m = input('please enter a month: ')
y = int(input('please enter a year: '))

def show_cal(*args):
  if not args:
    print(cal_month())
  if args[0]:
    print(cal_month())
    return m
  elif m and y:
    print(cal_month(), cal_year())
    return m + y
  else:
    print('please provide a month and year {/month} {year}')

show_cal(m, y)
# if no input print current month/year
# if user passes 1 argument print month
# if user passes 2 arguments print month and year
# else print statement asking the user to type a month/year

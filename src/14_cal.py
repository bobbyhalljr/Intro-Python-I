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

# Get the arguments
args = sys.argv

today = datetime.now()
month = today.month
year = today.year

tc = calendar.TextCalendar()

# If there are no arguments,
if len(args) == 1:
    # print calendar for current month
    tc.prmonth(year, month)
# If there's 1 arg,
elif len(args) == 2:
    # assume it's the month and print cal for that month
    month = int(args[1])
    tc.prmonth(year, month)
# If there's 2 args, assume it's the month/year
elif len(args) == 3:
    # print cal for that month/year
    month = int(args[1])
    year = int(args[2])
    tc.prmonth(year, month)
else:
    print("Input should be in this format: `14_cal.py month [year]`")



#  old version 

# variables
# show_cal = sys.argv[0]
# arguments = sys.argv[1:]
# count = len(arguments)

# # user input
# input('please type in a month and year --> ')

# # if no input print current month
# if len(sys.argv) < 0:
#   month = datetime.now()
#   print(month.strftime("%B"))
# # if user passes 1 argument print month
# elif len(sys.argv) != 1:
#   cal_month = calendar.LocaleTextCalendar(locale='en_US')
#   print(cal_month.prmonth(2020, 1))
# # if user passes 2 arguments print month and year
# elif len(sys.argv) != 2:
#   # month
#   cal_month = calendar.LocaleTextCalendar(locale='en_US')
#   print(cal_month.prmonth(2020, 1))
#   # year
#   year_locale = calendar.LocaleTextCalendar(calendar.SUNDAY)
#   print(year_locale.formatyear(2020, 2, 1, 1, 3))
# # else print statement asking the user to type a month/year
# else:
#   print('please provide a month and year [month] [year]]')

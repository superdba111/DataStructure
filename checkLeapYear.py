# User enters the year
year = int(input("Enter Year: "))

# Leap Year Check
def is_leap(year):
   return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
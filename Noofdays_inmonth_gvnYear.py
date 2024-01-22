def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
# TODO: Add more code here 👇
def days_in_month(year,month):
    """takes in year and month and return 
    number of days in the given month"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year)==True:
        month_days[1]=29
    return month_days[month-1]
#🚨 Do NOT change any of the code below 
year = int(input("year\n")) # Enter a year
month = int(input("month\n")) # Enter a month
days = days_in_month(year, month)
print(days)
days_in_month()


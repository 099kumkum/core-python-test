'''
#calculatage
from datetime import date


def calculateAge(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))
age = calculateAge(date(year, month, day))
print(age, "years")


# CurrentDay,Month,Year
from datetime import date, timedelta

currentStatus = date.today()
print("Current date", currentStatus.day)
print("Current month", currentStatus.month)
print("Current year", currentStatus.year)

tomorrowDate = currentStatus + timedelta(days=1)
print("Tomorrow date", tomorrowDate)

aftertomorrow = tomorrowDate + timedelta(days=1)
print("After tomorrow date", aftertomorrow)

previousDate = currentStatus - timedelta(days=1)
print("Previous date", previousDate)


# currentTime
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current time", current_time)
print("Current hours", now.hour)
print("Current minutes", now.minute)
print("Current seconds", now.second)


import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

a = datetime.datetime(2003, 5, 31)
print(a.strftime("%B"))


# DifferenceDate
from datetime import date


def calculateAge(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

print("----Enter current date----")
print()
cyear = int(input("Enter current year: "))
cmonth = int(input("Enter current month: "))
cday = int(input("Enter current day: "))
age = calculateAge(date(year, month, day))
print(age, "years")
'''
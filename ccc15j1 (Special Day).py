month = int(input())
day = int(input())

date_month = 2
date_day = 18

if month > date_month:
    print("After")
elif month == date_month and day == date_day:
    print("Special")
elif month <= date_month and day < date_day:
    print("Before")
elif month == date_month and day > date_day:
    print("After")
else:
    print("Before")

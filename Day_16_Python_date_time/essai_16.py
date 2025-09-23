import datetime
print(dir(datetime))

from datetime import datetime
now = datetime.now()
print(now)

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp:', timestamp)
print(f"{day}/{month}/{year}, {hour}:{minute}")

'''Formating Date OutPut Using strftime'''
from datetime import datetime
new_year = datetime(2025, 9,23)
print(new_year)

day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute)
print(f"{day}/{month}/{year}, {hour}: {minute}")

from datetime import datetime
#current date and time

now = datetime.now()
t = now.strftime("%m/%d/%Y , %H:%M:%S") #m = month, d=day, Y= year et H= Heure , M=Minutes, S= second
print("Time:", t)
time_one = now.strftime("%d/%m/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("Time_one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S") # dd/mm/YY H:M:S format
print("time two:", time_two)

'''String to time Using strptime'''

from datetime import datetime
date_string = "23 September, 2025"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object=", date_object)

'''Using date from datetime'''
from datetime import date
d = date(2025, 9, 23)
print(d)
print('current_date:', d.today())
#date object of today's date

today = date.today()
print("current_year:", today.year)
print("current_month:", today.month)
print("current_day:", today.day)

'''Time Objects to Represent Time'''
from datetime import time
#time(hour = 0, minute = 0, second = 0)
a= time()
print("a=", a)
#time(hour, minute and second)
b = time(10, 30, 50)
print("b=",b)

'''Difference Between Two Points in Time Using'''
today = date(year = 2025, month = 12, day = 31)
new_year = date(year = 2026, month = 1, day = 1)
time_left_for_new_year = new_year - today
print('Time left for new year:', time_left_for_new_year)

'''Difference Between Two Points in Time Using timedelta'''
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)

















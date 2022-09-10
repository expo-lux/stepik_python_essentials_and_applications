import sys
import datetime

year, month, day = input().split()
dt = int(input())
d = datetime.date(int(year), int(month), int(day)) + datetime.timedelta(days=dt)
print(str(d.year) + ' ' + str(d.month) + ' ' + str(d.day))
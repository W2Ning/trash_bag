import time
import datetime
import calendar
from chinese_calendar import is_workday


year  = int(input(">>>>>>输入年: "))
month = int(input(">>>>>>输入月: "))

last_day = calendar.mdays[month]

c = []
for i in range(1,last_day+1):
    a = datetime.datetime(year,month,i)
    b = is_workday(a)
    if b:
        c.append(a)


print(*c,sep = '\n')

import time


now = time.gmtime()
print(now)

month = now.tm_mon
day = now.tm_mday
print(month)
print(day)

if (month == 3):
    if (day == 14):
        print('生日快乐')
if (month == 6):
    if (day == 21):
        print('父亲节快乐')
if (month == 5):
    if (day == 10):
        print('母亲节快乐')
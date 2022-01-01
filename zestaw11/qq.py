import datetime as dt

date = input('enter birthdate(ex. 1.11.1999):\n')

d = date.strip().split('.')

print(dt.datetime(int(d[2]),int(d[1]),int(d[0])).date())
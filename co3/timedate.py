import datetime
t=datetime.time(22,56,23,34)
print(t)
print("hour:",t.hour)
print("minute:",t.minute)
print("second:",t.second)
print("micro second:",t.microsecond)
d=datetime.date.today()
print("Today:",d)
print("day:",d.day)
print("month:",d.month)
print("year:",d.year)
d1=datetime.timedelta(days=2)
d2=d1+d
print("Day after 2 days:",d2)
dt=datetime.datetime.combine(d,t)
print(dt)

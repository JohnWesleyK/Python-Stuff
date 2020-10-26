import datetime
mytime = datetime.time(2,20)
# print(mytime)   #02:20:00
mytime = datetime.time(13,20,1,20)
# print(mytime)
today  = datetime.date.today()
# print(today)
# print(today.ctime())    # Thu Aug 20 00:00:00 2020

from datetime import datetime
mydatetime = datetime(2021,10,3,14,20,1,60)
print(mydatetime)
mydatetime = mydatetime.replace(year=2020)
print(mydatetime)

# DATE
from datetime import date
date1 = date(2021,12,1)
date2 = date(2020,11,3)
result = date1-date2
print(result)          # 393 days, 0:00:00
print(type(result))    # <class 'datetime.timedelta'>

datetime1 = datetime(2021,12,1,22,0)
datetime2 = datetime(2020,11,3,12,0)
result = datetime1 - datetime2
print(type(result))
print(result)

import datetime
import pytz
d = datetime.datetime.now()
timezone = pytz.timezone("America/Los_Angeles")
d_aware = timezone.localize(d)
datetime2 = datetime2.replace(tzinfo=timezone)
print(datetime2.tzinfo)
print(d_aware.tzinfo)

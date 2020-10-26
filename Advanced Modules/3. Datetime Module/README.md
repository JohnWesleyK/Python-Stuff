# datetime module
datetime module in Python helps to deal with timestamps in your code. Time values are represented with time class. Times have attributes for hour, minute, second, and microsecond, they can also include time zone information. The arguments to initialize a time instance are optional, but the default value will be 0.
## time
Let's create a timestamp by specifying datetime.time(hour,minute,second,microsecond)
```python
import datetime

time = datetime.time(4, 20, 1)

# Let's see the different components
print(time)
print('Hour  :', time.hour)
print('Minute:', time.minute)
print('Second:', time.second)
print('MicroSecond:', time.microsecond)
print('tzinfo:', time.tzinfo)
```
```text
04:20:01
Hour  : 4
Minute: 20
Second: 1
MicroSecond: 0
tzinfo: None
```
Note that only one concrete tzinfo class, the timezone class, is supplied by the datetime module. The timezone class can represent simple timezones with fixed offset from UTC, such as UTC itself or North American EST and EDT timezones. Supporting timezones at deeper levels of detail is up to the application.

Note: A time instance only holds values of time, and not a date associated with the time.
We can also find the min and max values a time of day can have
```python
print('Earliest  :', datetime.time.min)
print('Latest    :', datetime.time.max)
print('Resolution:', datetime.time.resolution)
```
```text
Earliest  : 00:00:00
Latest    : 23:59:59.999999
Resolution: 0:00:00.000001
```

## Dates
Calendar date values can be represented with the date class. Instances have attributes for year, month, and day. 
It is easy to create a date representing today’s date using the today() class method.
```python
today = datetime.date.today()
print(today)
print('ctime:', today.ctime())
print('tuple:', today.timetuple())
print('ordinal:', today.toordinal())
print('Year :', today.year)
print('Month:', today.month)
print('Day  :', today.day)
```
```text
2020-06-10
ctime: Wed Jun 10 00:00:00 2020
tuple: time.struct_time(tm_year=2020, tm_mon=6, tm_mday=10, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=162, tm_isdst=-1)
ordinal: 737586
Year : 2020
Month: 6
Day  : 10
```
We can find the range of these attributes
```python
print('Earliest  :', datetime.date.min)
print('Latest    :', datetime.date.max)
print('Resolution:', datetime.date.resolution)
```
```text
Earliest  : 0001-01-01
Latest    : 9999-12-31
Resolution: 1 day, 0:00:00
```
Another way to create new date instances uses the replace() method of an existing date i.e, you can change the year, leaving the day and month alone.
```python
d1 = datetime.date(2015, 3, 11)
print('d1:', d1)

d2 = d1.replace(year=1990)
print('d2:', d2)
```
```text
d1: 2015-03-11
d2: 1990-03-11
```
## Arithmetic
Arithmetic operations can be performed on date objects to check for time differences.
```python
d1
d2
d1-d2
```
This gives us the difference in days between the two dates. You can use the timedelta method to specify various units of times (days, minutes, hours, etc.)
```text
datetime.date(2015, 3, 11)
datetime.date(1990, 3, 11)
datetime.timedelta(9131)
```
One more example
```python
datetime1 = datetime(2021,12,1,22,0)
datetime2 = datetime(2020,11,3,12,0)
result = datetime1 - datetime2
print(type(result))
print(result)
```
```text
<class 'datetime.timedelta'>
393 days, 10:00:00
```
Note: Keep in mind when there are leap years in the calculations there might be tiny miscalculations.
# Getting present time
```python
import datetime
time_now = datetime.datetime.now()
```
### Using timezone info
Suggest a bit of research(googling) here 
```python
import datetime
import pytz

datetime2 = datetime(2020,11,3,12,0)

d = datetime.datetime.now()
timezone = pytz.timezone("America/Los_Angeles")
d_aware = timezone.localize(d)
datetime2 = datetime2.replace(tzinfo=timezone)
print(datetime2.tzinfo)
print(d_aware.tzinfo)
```
```text
America/Los_Angeles
America/Los_Angeles
```
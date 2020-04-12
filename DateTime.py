import datetime

today = datetime.date.today()
print(today) # output = 2020-04-09

birthday = datetime.date(1998, 7, 14)
print(birthday) # output = 1998-07-14
print(repr(birthday)) # output = datetime.date(1998, 7, 14)

days_since_birth = today - birthday
print(days_since_birth) # output = 7940 days, 0:00:00
print(days_since_birth.days) # output = 7940 (here just show days)

# adding 10 days to current day
tdelta = datetime.timedelta(days=10)
print(today + tdelta) # output = 2020-04-19 (2020-04-09 + 10days)
print(today - tdelta) # output = 2020-03-30 (here subtracting)

print(today.month) # output = 4
print(today.weekday()) # output = 3
print(today.day) # output = 9

# here computer calculate : monday = 0, sunday = 6

print(datetime.time(7, 2, 20, 15))  # output = 07:02:20.000015 (hour:minute:second:mili-second)
 
# datetime.date() show (Y, M, D)
# datetime.time() show (h, m, s, ms)
# datetime.time() show (Y, M, D, h, m, s, ms)

hour_delta = datetime.timedelta(hours = 10)
print(datetime.datetime.now()) # output = 2020-04-09 10:43:39.601000

# here given below the line add 10 hours add of the day 
print(datetime.datetime.now() + hour_delta) # output = 2020-04-09 20:46:01.383000 (here show in my computer local time)
datetime_today = datetime.datetime.now(tz = pytz.UTC)
datetime_pacific = datetime_today.astimezone(pytz.timezone('US/Pacific'))
print(datetime_pacific)

for tz in pytz.all_timezones :
    print(tz) # here show all time-zone in the world

# string formatting with dates
# 2020-09-04 -> April 9, 2020

print(datetime_pacific.strftime('%B %d, %Y')) # capital B define month, d defines day, capital Y difines year.
# here strftime = string formatting time
# Aprinl 09, 2020 -> datetime(2019, 3, 9)
# strptime (p = parsing

datetime_thing = datetime.datetime.strptime('March 09, 2019', '%B %d, %Y')
print(datetime_thing)
print(repr(datetime_thing))

# http://github.com/kennethreitz/maya (actually maya consider datetime for human life easier)

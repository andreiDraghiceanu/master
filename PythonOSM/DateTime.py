import datetime
import imp
import pytz

imp.reload(pytz)

'''Give a datetime'''
d = datetime.date(2017, 7, 23)
# print(d)

'''Generate today date'''
tday = datetime.date.today()
# print(tday)
# print()
# print(tday.day)
# print()
# print(tday.isoweekday()) # Monday 1 Sunday 7
# print()
# print(tday.weekday()) # Monday 0 Sunday 6

'''Add or substract days to a date'''
tdelta = datetime.timedelta(days=9995)
theday = tday - tdelta
print(theday)
talfa = datetime.timedelta(days=10000)
print(theday + talfa)

# date2 = dat1 + timedelta
# timedelta = date1 + date2

# bday = datetime.date(2018, 9, 24)
#
# till_bday = bday - tday
# print(till_bday)
# print(till_bday.days)
# print(till_bday.total_seconds())

# t = datetime.time(9, 30, 45, 10000)
# print(t)
# print(t.hour)

dt0 = datetime.datetime(2016, 7, 23, 9, 30, 45, 10000)
# print(dt0)

tbeta = datetime.timedelta(days=7, hours=12)
# print(dt0+tbeta)

# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.today()
#
# print(dt_today)
# print(dt_now)
# print(dt_utcnow)
print()

# dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
# print(dt)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow)
#
# dt_mtn = dt_utcnow.astimezone(pytz.timezone('Africa/Bamako'))
# print(dt_mtn)

for tz in pytz.all_timezones:
    print(tz)
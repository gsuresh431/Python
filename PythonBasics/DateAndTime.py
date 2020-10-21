import datetime
import pytz
'''
datetime.date - Y/M/D    - rarely used alone
datetime.time - H/m/s/ms - rarely used alone
datetime.datetime Y/M/D H/m/s/ms - most commonly used
'''

#Date manipulation
today = datetime.date.today()
birth_day = datetime.date(1985, 3, 24)
print(type(birth_day))   #<class 'datetime.date'>
print(birth_day)         #1985-03-24
print(today)             #2019-10-29
print(today - birth_day) #12637 days, 0:00:00

#Time manipulation
t = datetime.time(8, 8, 8)
print(type(t)) #<class 'datetime.time'>
print(t)       #08:08:08
print(t.hour, t.minute, t.second, t.microsecond) # 8 8 8 0

#DateTime manipulation
dt = datetime.datetime(1985, 3, 24, 8, 9, 10)
tdelta = datetime.timedelta(days=3, hours=4, minutes=5, seconds=12)
print(type(dt))     #<class 'datetime.datetime'>
print(type(tdelta)) #<class 'datetime.timedelta'>
print(dt)           #1985-03-24 08:09:10
print(dt+tdelta)    #1985-03-27 12:14:22

#Important constructs of datetime
dt_today = datetime.datetime.today()  # returns current local datetime with timezone=None
dt_now = datetime.datetime.now()      # gives the option to pass in a timezone. 
                                      # If nothing is provided, timezone=none - behaves same as above
dt_utcnow = datetime.datetime.utcnow()# Even though the method contains UTC in the name, 
                                      # it just gives the current time of UTC. However, TZINFO is still set to none

print(dt_today) #2019-10-29 01:16:35.186688
print(dt_now)   #2019-10-29 01:16:35.186688
print(dt_utcnow)#2019-10-28 19:46:35.186688

#Handling timezones - pytz - Timezone aware objectts
dt = datetime.datetime(1985, 3, 24, 8, 9 ,10, tzinfo=pytz.UTC)
print(type(dt)) #<class 'datetime.datetime'>
print(dt)       #1985-03-24 08:09:10+00:00
                # 00:00 is the UTC offset
import datetime
import pytz
print("time of now")

value = datetime.datetime(year=2020, month=2, day=2)
print(value)

iran = pytz.timezone('asia/tehran')
irant = datetime.datetime.now(iran)
print('iran', irant.strftime('%Y.%m.%d %H:%M:%S'))

us = pytz.timezone('America/New_York')
ust = irant.astimezone(us)
print('America', ust.strftime('%Y.%m.%d %H:%M:%S'))
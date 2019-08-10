import datetime
print(datetime.date(2020, 5, 5))

from datetime import datetime
print(datetime.now())              
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))   
print(datetime.today())           

from datetime import date
print(date.today())                     
print(date.today().isoweekday())       

print(date(2019, 9, 6).isoweekday())   


import time

tp = time.strptime("2020-05-05 00:00:00", '%Y-%m-%d %H:%M:%S')
print(time.mktime(tp))

print(time.strftime("%H:%M:%S", time.gmtime(1000)))

interval = time.mktime(tp) - time.time()
print(time.strftime("%H:%M:%S", time.gmtime(interval)))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(interval)))
print(time.strftime("%m-%d %H:%M:%S", time.gmtime(interval)))
print(time.strftime("%m-%d %H:%M:%S", time.gmtime(2000)))
print(time.strftime("%m-%d %H:%M:%S", time.gmtime(8000000)))

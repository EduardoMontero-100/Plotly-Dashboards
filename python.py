import datetime as dt

today_1 = dt.date.today()
today_3 = dt.date.today()+dt.timedelta(days=3)
print('Today: ' +str(today_1))
print('Today plus 3: ' +str(today_3))


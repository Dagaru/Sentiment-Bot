import datetime as DT
today = DT.date.today()
week_ago = today - DT.timedelta(days=7)
print(today)
print(week_ago)
import datetime as DT
today = DT.date.today()
week_ago = today - DT.timedelta(days=7)


def GetToday():
    today = DT.date.today()
    return today

def GetLastWeek():
    week_ago = GetToday() - DT.timedelta(days=7)
    return week_ago

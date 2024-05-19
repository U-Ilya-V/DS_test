import datetime

def funcTest3 (firstDate, secondDate):
    d1 = datetime.datetime.strptime(firstDate,'%d.%m.%Y')
    d2 = datetime.datetime.strptime(secondDate,'%d.%m.%Y')
    return abs(d1-d2).days

day1 = "7.6.2002"
day2 = "3.6.2002"

print(funcTest3(day1,day2))


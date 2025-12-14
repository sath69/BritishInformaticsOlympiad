#Rating of difficulty: 3/10, overall parts went smooth but it may seem like older papers looked way easier compared to now.
def computeMayanCalendar(baktun, katun, tun, uinal, kin):
 days_dict = {
    1: "Saturday",
    2: "Sunday",
    3: "Monday",
    4: "Tuesday",
    5: "Wednesday",
    6: "Thursday",
    7: "Friday",
 }
 mayan_calendar = [13,20,7,16,2]
 counter = 0
 dayCounter = 1
 while True:
   mayan_calendar[-1] += 1
   if mayan_calendar[-1] > 20:
      mayan_calendar[-1] = 1
      mayan_calendar[-2] += 1
   if mayan_calendar[-2] > 18:
      mayan_calendar[-2] = 1
      mayan_calendar[-3] += 1
   if mayan_calendar[-3] > 20:
      mayan_calendar[-3] = 1
      mayan_calendar[-4] += 1
   if mayan_calendar[-4] > 20:
      mayan_calendar[-4] = 1
      mayan_calendar[-5] += 1
   if mayan_calendar[-5] > 20:
      mayan_calendar[-5] = 1
   if mayan_calendar == [int(baktun),int(katun),int(tun),int(uinal),int(kin)]:
      return counter, days_dict[dayCounter]
   counter += 1
   dayCounter += 1
   if dayCounter > 7:
      dayCounter = 1
   
def computeGregorianCalendar(value):
    year = 2000
    month = 1
    days = 1
    months_dict = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    while value >= 31:
          for x in range(1, len(months_dict)+1):
              if x == 12 and value >= 31:
                 value -= 31
                 month = 1
                 year += 1
                 continue
              if months_dict[x] == 31 and value >= 31:
                 value -= 31
                 month += 1
              if x == 2 and year % 4 == 0 and value >= 29:
                 value -= 29
                 month += 1
              if x == 2 and year % 4 != 0 and value >= 28:
                 value -= 28
                 month += 1   
              if months_dict[x] == 30 and value >= 30:
                 value -= 30
                 month += 1
    days += value
    return days ,month ,year
    
"""
b) 1/02/2000: 13 20 7 17 14
   1/01/2001:  13 20 8 16 9
   
c) 2880000
   Thursday
"""



baktun,katun,tun,uinal,kin = input().split()
days, dayType = computeMayanCalendar(baktun, katun, tun, uinal, kin)
print(dayType)
print(computeGregorianCalendar(days))

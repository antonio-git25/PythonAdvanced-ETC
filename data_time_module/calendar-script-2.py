import calendar
from datetime import date

inside = date(2023, 1, 1)
print(inside.year)


calendar.prmonth(2008, 7)

print(calendar.weekday(2008, 7, 5))
print(calendar.weekday(2008, 7, 6))
print(calendar.weekday(2008, 7, 7))
print(calendar.weekday(2008, 7, 8))
print(calendar.weekday(2008, 7, 9))



c = calendar.TextCalendar()
c.prmonth(2024, 3)
days = c.monthdayscalendar(2024, 3)
#print(c.monthdayscalendar(2024, 3))
print(days)

count_days = 0

for day in days:
    print(day)
    for d in day:
        print(d)
        if d != 0: count_days += 1

print(f"count: {count_days}")
# print("\n")
# cal = calendar.Calendar()
# for d in cal.itermonthdays(2008, 7):
#     print(d)
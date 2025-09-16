import calendar

print(list(calendar.day_name))
print(list(calendar.day_abbr))
print(list(calendar.month_name))
print(list(calendar.month_abbr))


print("\n")
print(calendar.month(2024, 3))
#print(calendar.month(2024, 4, w=4))
#print(calendar.month(2024, 5, l=2))

calendar.prmonth(2024, 12)

#print(calendar.calendar(2023, m=3, c=4))


calendar.prmonth(2024, 3)
print('-' * 20)
days = calendar.monthcalendar(2024, 3)
print(*days, sep='\n')

print("\n hello")
print(calendar.monthrange(2024, 6))


print("\n *********!!!!***********")
cal = calendar.Calendar()
calendar.prmonth(2024, 2)
for d in cal.itermonthdays(2024, 2):
    print(calendar.weekday(2024, 2, d))
    #if d not in (calendar.SATURDAY, calendar.SUNDAY): print(d)


calendar.prmonth(2008, 7)

print(calendar.weekday(2024, 3, 5))
print(calendar.weekday(2024, 3, 6))
print(calendar.weekday(2024, 3, 7))
print(calendar.weekday(2024, 3, 8))
print(calendar.weekday(2024, 3, 9))
print(calendar.weekday(2024, 3, 10))
print(calendar.weekday(2024, 3, 11))
print(calendar.weekday(2024, 3, 12))
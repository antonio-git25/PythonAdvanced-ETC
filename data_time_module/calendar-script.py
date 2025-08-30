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
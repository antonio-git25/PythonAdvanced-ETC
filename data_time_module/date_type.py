from datetime import date, MAXYEAR, MINYEAR
import datetime


d1 = date(2020, 12, 31)
print(d1)
d2 = date(day=12, year=2010, month=10)
print(d2)
d3 = date(70, day=1, month=10)
print(d3)

print('\n')

a = date(2015, 8, 21)
print(a.year, type(a.year))
print(a.month, type(a.month))
print(a.day, type(a.day))
print(f'{a.month}/{a.day}/{a.year}')

print('\n')

notes = {
    date(2023, 4, 13): "Значение для 13 апреля 2023 года",
    date(2023, 4, 14): "Значение для 14 апреля 2023 года",
    date(2023, 4, 15): "Значение для 15 апреля 2023 года"
}
print(notes[date(2023, 4, 13)])

print('\n')

date1 = datetime.date(2023, 4, 22)
date2 = datetime.date(2023, 4, 14)

if date1 > date2:
    print(f"{date1} позже чем {date2}")
elif date1 < date2:
    print(f"{date1} раньше чем {date2}")
else:
    print(f"{date1} совпадает с {date2}")


print('\n')


date1 = date(2023, 4, 22)
date2 = date(2023, 4, 22)
date3 = date(2023, 4, 23)
print(date1 == date2)  # True
print(date2 == date3)  # False
print(date1 != date3)  # True


print("\n")

print(date.max) # 9999-12-31
print(f'Max year = {MAXYEAR}')  # Max year = 9999

a = date(2015, 8, 21)
print(a.max)  # 9999-12-31

print("\n")

print(date.min)  # 0001-01-01
print(f'Min year = {MINYEAR}')  # Min year = 1

a = date(2015, 8, 21)
print(a.min)  # 0001-01-01


now = date.today()
print('\nСегодня:', now)
print('День недели:', now.weekday())
print('День недели:', now.isoweekday())


print("\n")
a = date(2024, 10, 28)  # Понедельник 28.10.24
b = date(2024, 10, 29)  # Вторник 29.10.24
c = date(2024, 10, 27)  # Воскресенье 27.10.24
print(a.weekday())  # 0
print(b.weekday())  # 1
print(c.weekday())  # 6
print(a.isoweekday())  # 0
print(b.isoweekday())  # 1
print(c.isoweekday())  # 6


##Replace method
print("\n")
d = date(2023, 4, 13)
print(d)  # 2023-04-13

# метод replace не изменяет первоначальную дату
print(d.replace(day=1, month=2, year=2010), d)  # 2010-02-01 2023-04-13

# но вы можете перезатереть значение новой датой при помощи присваивания
new_date = d.replace(day=14, year=2014)
print(new_date)  # 2014-04-14

# еще один пример создания новой даты на основе имеющейся
d = d.replace(day=2)
print(d)  # 2023-04-02
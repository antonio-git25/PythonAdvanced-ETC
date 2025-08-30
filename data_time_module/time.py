from datetime import time, date, datetime

empty_time = time()
print(empty_time)  # 00:00:00

only_hours = time(22)
print(only_hours)  # 22:00:00

hours_and_min = time(10, 22)
print(hours_and_min)  # 10:22:00

hours_and_min_sec = time(8, 10, 22)
print(hours_and_min_sec)  # 08:10:22

full_time = time(4, 8, 10, 22)
print(full_time)  # 04:08:10.000022

print('\n')

only_hours = time(hour=22)
only_minutes = time(minute=22)
only_seconds = time(second=22)
print(only_hours, only_minutes, only_seconds)  # 22:00:00 00:22:00 00:00:22

hours_and_min = time(minute=10, hour=12)
hours_and_sec = time(hour=4, second=10)
print(hours_and_min, hours_and_sec)  # 12:10:00 04:00:10

hours_and_min_sec = time(hour=4, minute=7, second=10)
print(hours_and_min_sec)  # 04:07:10

full_time = time(minute=21, second=10, hour=4, microsecond=545)
print(full_time)  # 04:21:10.000545


print('\n')
time1 = time(11, 4, 15)
time2 = time(11, 4, 15)
time3 = time(11, 5, 16)
print(time1 == time2)  # True
print(time2 == time3)  # False
print(time1 != time3)  # True

time1 = time(11, 4, 15)
time2 = time(11, 4, 15)
if time1 == time2:
    print("Времена совпадают")
else:
    print("Времена не совпадают")



print('\n')
time1 = time(10, 4, 15)
time2 = time(9, 3, 14)
time3 = time(15, 2, 16)
max_time = max(time1, time2, time3)
min_time = min(time1, time2, time3)
print(max_time)
print(min_time)


print('\n')
my_date = date(2015, 8, 21)
my_time = time(10, 5, 30)
dt = datetime.combine(my_date, my_time)
print(dt, type(dt))
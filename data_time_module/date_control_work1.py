from datetime import date, datetime
import datetime as DT

date_vocal = {}
for i in range(1,32):
    date_list = []
    for dl in range(1, i+1):
        date_list.append(date(1945, 5, day = dl))

    date_vocal[date(1945, 5, day=i)] = date_list

for k,v in date_vocal.items():
    #print(k, ":", v)
    pass



def count_mondays():
    sum_count = 0
    for yr in range (2014, 2023):
        print("year: ", yr)
        current_year = []
        for sd in range(1,13):
            current_year.append(date(year=yr, month=sd, day=1))
        for sd in current_year:
            if sd.weekday() == 0: sum_count += 1

    print(f"All mondays is {sum_count}")


def sum_times():
    date_fmt = '%H:%M:%S'
    step = DT.timedelta(seconds=15)
    start_date = DT.datetime.strptime('00:00:00', date_fmt)
    last_date = DT.datetime.strptime('23:49:55', date_fmt)
    print(start_date)
    print(last_date)



def get_format_date(dt: datetime) -> str:
    my_date = dt
    return my_date.strftime("Today is %A, %d %B %Y")

# Проверки
dt_1 = datetime(2023, 9, 1, 18, 45, 30)
print(dt_1)
#assert get_format_date(dt_1) == 'Today is Friday, 01 September 2023'


def is_programmers_day(dt: date) -> bool:
    md = dt
    day = md.strftime("%j")
    print(day)

# Проверки
# Невисокосный год
is_programmers_day(date(2024, 9, 12))
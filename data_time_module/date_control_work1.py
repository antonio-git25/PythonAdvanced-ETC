from datetime import date


date_vocal = {}
for i in range(1,32):
    date_list = []
    for dl in range(1, i+1):
        date_list.append(date(1945, 5, day = dl))

    date_vocal[date(1945, 5, day=i)] = date_list

for k,v in date_vocal.items():
    print(k, ":", v)


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

count_mondays()
import os
import stat
import calendar
import time

new_dir_path = 'new-dir'
os.mkdir(new_dir_path) # создаст папку "new-dir" в текущем рабочем каталоге
print("directory is created", os.listdir())
time.sleep(2)
os.rmdir(new_dir_path)
print("directory is deleted", os.listdir())

print("\n")

os.makedirs('movies/comedy')
print("directories are created", os.listdir())
time.sleep(2)
# удаляем 'movies'
os.removedirs('movies/comedy')
print(os.listdir())









def generate_structure():
    print("\n \n \n")
    list_month = list(calendar.month_name)[1:]
    print(list_month)

    for i in range(2018, 2026):
        path = f"sales_{i}"
        os.mkdir(path)
        print(f"year folder is created: {path}")
        for lm in list_month:
            path_inner = f"{path}/{lm}_{str(i)[2:]}"
            os.mkdir(path_inner)
            print(f"   create current month: {path_inner}")
            mn_num = list_month.index(lm)
            days_in_mn = calendar.monthrange(i, int(mn_num) + 1)[1]
            for dd in range(1, days_in_mn + 1):
                if str(dd) in ('1','2','3','4','5','6','7','8','9'):
                    path_inner_days = f"{path_inner}/0{dd}_{lm[:3]}_{str(i)[2:]}"
                else:
                    path_inner_days = f"{path_inner}/{dd}_{lm[:3]}_{str(i)[2:]}"
                # 28_Feb_19
                os.mkdir(path_inner_days)

#generate_structure()


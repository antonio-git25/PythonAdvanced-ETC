import os
import time

current_directory = os.getcwd()
print("Текущая директория:", current_directory)

print(os.listdir())

print("Current working directory: ", os.getcwd())


print('-' * 25)
print(os.sep)
print(os.extsep)
print(os.pardir)
print(os.curdir)


print("\n")
print('File         :', __file__)
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Change time  :', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__))


print("\n")
def get_only_dirs(path: str) -> None:
    items = os.listdir(path)
    dirs = [item for item in items if os.path.isdir(os.path.join(path, item))]

    sort_dir = sorted(dirs)
    for dir in sort_dir:
        print(dir)

    print(len(dirs))


get_only_dirs('C:/Users/Antonio/Documents')
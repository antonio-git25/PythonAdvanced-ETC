import os
import stat




def get_only_dirs(path: str) -> None:
    items = os.listdir(path)
    dirs = [item for item in items if os.path.isdir(os.path.join(path, item))]

    sort_dir = sorted(dirs)
    for dir in sort_dir:
        print(dir)

    print(len(dirs))
    

get_only_dirs('C:/Users/Antonio/Documents')

print("\n")

print('Файл:', __file__)
print('Существует:', os.access(__file__, os.F_OK))
print('Право на чтение:', os.access(__file__, os.R_OK))
print('Право на запись:', os.access(__file__, os.W_OK))
print('Право на исполнение:', os.access(__file__, os.X_OK))
print('Чтение и исполнение:', os.access(__file__, os.R_OK | os.X_OK))
print('Чтение и запись:', os.access(__file__, os.R_OK | os.W_OK))

print("\n")

filename = 'hello.txt'
mode = os.stat(filename).st_mode
print(stat.filemode(mode))
os.chmod(filename, 0o777)
mode = os.stat(filename).st_mode
print(stat.filemode(mode))
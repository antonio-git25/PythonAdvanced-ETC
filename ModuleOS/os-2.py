import os



def get_only_dirs(path: str) -> None:
    items = os.listdir(path)
    dirs = [item for item in items if os.path.isdir(os.path.join(path, item))]

    sort_dir = sorted(dirs)
    for dir in sort_dir:
        print(dir)

    print(len(dirs))
    

get_only_dirs('C:/Users/Antonio/Documents')
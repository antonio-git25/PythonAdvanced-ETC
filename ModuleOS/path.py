from pathlib import Path

path_1 = Path("songs", "prodigy") # путь к каталогу
print(path_1)


path_2 = Path("songs", "prodigy", "voodoo people.mp3") # путь к файлу
print(path_2)


path_3 = Path(r'C:\Users\artem_egorov\requirements.txt')
print(path_3)


path_parts = ['path', 'to', 'your', 'file.txt']
path_from_parts = Path(*path_parts)

print(path_from_parts)
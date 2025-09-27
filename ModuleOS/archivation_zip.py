from zipfile import ZipFile
from datetime import datetime


with ZipFile("my_archive.zip", mode="r") as archive:
    info = archive.getinfo("test1.txt")
    print(info)
    print(info.filename)
    print(info.file_size)
    print(info.date_time)
    print(info.create_system)
    print("\n")

with ZipFile("my_archive.zip", mode="r") as archive:
    for info in archive.infolist():
        print(f"Filename: {info.filename}")
        print(f"Modified: {datetime(*info.date_time)}")
        print(f"Normal size: {info.file_size} bytes")
        print(f"Compressed size: {info.compress_size} bytes")
        print(f"Is directory: {info.is_dir()}")
        print("-" * 20)



with ZipFile('index.zip') as archive:
    archive.printdir()

with ZipFile("index.zip", mode="a") as archive:
    archive.write("cat.txt")
    print("archive is updated")

with ZipFile('index.zip') as archive:
    archive.printdir()


with ZipFile("my_archive.zip", "w") as my_zip:
    # Записываем текстовую строку в архив с указанными именами "hello.txt" и "world.txt"
    my_zip.writestr("test1.txt", "Hello")
    my_zip.writestr("test2.txt", "World")

    # Записываем байтовую строку в архив с указанным именем "hello_world.txt"
    binary_data = b"Hello world!"
    my_zip.writestr("test3.txt", binary_data)

print("ZIP-архив 'my_archive.zip' успешно создан.")

print("\n")


def compress_string(string: str) -> str:
    if not string:  # проверка на пустой ввод
        return ""

    init_str = string
    string = string.lower()

    result = []
    current_char = string[0]
    count = 1

    for char in string[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = char
            count = 1

            # добавляем последний символ и его количество
    result.append(current_char + str(count))

    if len(''.join(result)) >= len(string):
        print("initial string:", init_str)
        return init_str
    else:
        print("modified string:", ''.join(result))
        return ''.join(result)


assert compress_string("aaaabbbc") == "a4b3c1"

assert compress_string("AaBbCc") == "AaBbCc"



print("\n"*2)
size_count = 0
with ZipFile("my_archive.zip", mode="r") as archive:
    for info in archive.infolist():
        file_name = str({info.filename})
        mod_format = file_name[-6:]
        mod_format = mod_format[:4]
        print("filename: ", file_name, mod_format)
        if mod_format == ".txt":
            print("file with .txt", file_name)
            size = str({info.compress_size})
            print("size:", size)
            formatted_size = ""
            for i in size:
                if i.isdigit(): formatted_size += str(i)
            size_count += int(formatted_size)

print("sum of txt files:",size_count)

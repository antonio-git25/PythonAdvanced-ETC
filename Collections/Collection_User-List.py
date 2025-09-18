from collections import UserString
from collections import UserList

# Создание UserString из строки
us_from_str = UserString("Hello, UserString!")
print(us_from_str)
print(us_from_str.data)

# Создание UserString из числа (преобразуется в строку)
us_from_int = UserString(42)
print(us_from_int)
print(us_from_int.data)

# Создание UserString из списка (преобразуется в строку через str())
us_from_list = UserString([1, 2, 3])
print(us_from_list)
print(us_from_list.data)

# Создание через другой объект UserString
us_from_user_string = UserString(UserString("Another UserString"))
print(us_from_user_string)
print(us_from_user_string.data)




print("\n")
print("UserString next ..." * 2)
# Создание UserList из списка
ul_from_list = UserList([1, 2, 3, 4, 5])
print(ul_from_list)
print(ul_from_list.data)

# Создание UserList из кортежа
ul_from_tuple = UserList((6, 7, 8, 9, 10))
print(ul_from_tuple)
print(ul_from_tuple.data)

# Создание UserList из строки (каждый символ будет элементом списка)
ul_from_str = UserList("Hello")
print(ul_from_str)
print(ul_from_str.data)

# Создание UserList из другого объекта UserList
ul_from_user_list = UserList(UserList([11, 12, 13, 14, 15]))
print(ul_from_user_list)
print(ul_from_user_list.data)

# Создание UserList из диапазона чисел
ul_from_range = UserList(range(5))
print(ul_from_range)
print(ul_from_range.data)



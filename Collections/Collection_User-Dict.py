from collections import UserDict

# Создание непустого UserDict
d = {'a': 1, 'b': 2, 'c': 3}
user_dict = UserDict(d)
print(user_dict)
print(user_dict.data)

print('-' * 20)

user_dict_2 = UserDict(a=100, w=200)
print(user_dict_2)
print(user_dict_2.data)

print('+'*40)
d['a'] = 123
print(d)
print(user_dict)



print("\nGo next...")

my_dick = UserDict({'a': 1, 'b': 2, 'c': 3})
# Доступ к значению по ключу
print(my_dick['a'])  # Вывод: 1

# Проверка наличия ключа
print('b' in my_dick)  # Вывод: True
print('d' in my_dick)  # Вывод: False

# Получение списка ключей
keys = my_dick.keys()
print(keys)  # Вывод: KeysView({'a': 1, 'b': 2, 'c': 3})

# Получение списка значений
values = my_dick.values()
print(values)  # Вывод: ValuesView({'a': 1, 'b': 2, 'c': 3})
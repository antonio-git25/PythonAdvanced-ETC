from collections import Counter


s = 'abracadabra'
count = {}
for letter in s:
    count[letter] = count.get(letter, 0) + 1
print(count)


sad = 'zaratustra'
print(f"zaratustra: {Counter(sad)}")



count_from_str = Counter('gallahad')  # создание Counter из строки
print(f"gallahad: {count_from_str}")


words = ['Donald', 'Mickey', 'Donald', 'Mickey', 'Mickey']
names = Counter(words)
print(names)

count_from_dict = Counter({'red': 4, 'blue': 2})  # создание Counter из словаря
print(count_from_dict)
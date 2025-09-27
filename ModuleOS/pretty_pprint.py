from data_json import users
from pprint import pprint


#for user in users: print(user)

pprint(users, depth=2, indent=3)

print('\n-----------\n')

with open("output.txt", mode="w") as file:
    pprint(users, stream=file)
print('Процесс завершен, посмотрите содержимое файла output.txt')
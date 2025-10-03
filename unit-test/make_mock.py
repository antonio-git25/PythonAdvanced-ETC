from unittest.mock import Mock
from datetime import date

mock = Mock()
print(mock)

print(mock.current_time)
print(mock.total)
print(mock.get_average())
print(mock.find_max(1, 4, 5, 3))


print('\n')


mock.get_message.return_value = {
    'id': 5,
    'message': 'hello world'
}
print(mock.get_message)
print(mock.get_message())


print('\n')


os = Mock()
print(os.mkdir(r"F:\folder"))
print(os.mkdir(r"D:\another_folder"))
print(os.remove(r"F:\folder"))
print(os.listdir(r"F:\folder"))

print(os.mkdir.call_count)
print(os.mkdir.call_args)
print(os.mkdir.call_args_list)
print(os.mkdir)


print('\n')
# Создаем мок-объект
call = Mock()
# Вызываем его несколько раз
call()
call()
call.get_message()
# Проверяем количество вызовов
print(call.call_count)
print(call.get_message.call_count)


print('\n')
# Создаем мок-объект
boll = Mock()
# Вызываем его с аргументами
boll(42, sort='value')
# Получаем информацию о последнем вызове
print(boll.call_args)
# делаем следующий вызов
boll([1, 2, 3, 4], True)
print(boll.call_args)
# обращаемся к методу, который не вызывали до этого
print(boll.get_message.call_args)
# вызываем метод
boll.get_message('hello')
print(boll.get_message.call_args)


print('\n')
print(date.today())
date = Mock()
date.today.return_value = '1990-08-21'
print(date.today())


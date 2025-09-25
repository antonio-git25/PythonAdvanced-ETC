from queue import Queue
from queue import LifoQueue


q = Queue()
print(q)
print(q.queue)

q.put('Q')
q.put('W')
q.get()
q.put('E')
q.get()
q.put('R')
q.put('T')
q.get()
q.put('Y')

print("\n")
print(q.queue)

f = Queue()
print(f.queue)
for i in [100, 'Hello', False]:
    f.put(i)
print('Наполнили очередь', f.queue)

print('Начинаем доставать элементы')
print(f.get(), f.queue)
print(f.get(), f.queue)
print(f.get(), f.queue)

print("\n")



stack = LifoQueue()
print(stack.queue)
for i in [200, [1, 2, 4], 'Not bad']:
    stack.put(i)
print('Наполнили стек', stack.queue)

print('Начинаем доставать элементы')
print(stack.get(), stack.queue)
print(stack.get(), stack.queue)
print(stack.get(), stack.queue)

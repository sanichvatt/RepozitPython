# Функции высшего порядка
"""
def f(x):
    return x * x
print(f(5))  # 25
print(type(f)) # <class 'function'>
a = f
print(a(5)) # 25

"""
"""
def calk1(a, b):
    return a + b

def calk2(a, b):
    return a * b

def math(op, x, y):
    print(op(x, y))

math(calk1, 5, 45)
"""
# Лямбда функция
"""
# def calk1(a, b):
#     return a + b преобразуем в: ->
calk1 = lambda a, b: a + b

def calk2(a, b):
    return a * b

def math(op, x, y):
    print(op(x, y))

math(calk1, 5, 45)
math(lambda a, b: a + b, 5, 45)
"""
# ЗАДАЧА
# 1.В списке хранятся числа. Нужно 
# выбрать только четные числа и составить 
# список пар (число; квадрат числа)
# пример: 1 2 3 5 8 15 23 38 
# Получить: [(2, 4), (8, 64), (38, 1444)]
"""
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = list()

for i in data:
    if i % 2 == 0:
        res.append((i, i**2))

print(res)
"""
# ...а можно сделать так: 
"""
def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)
"""
# Функция "map":
# def select(f, col):
#    return [f(x) for x in col],
"""
list_1 = [x for x in range(1, 21)]
print(list_1)

list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)
"""
# Задача: С клавиатуры вводится некий набор чисел,
# в качестве разделителя используется пробел.
# Этот набор чисел будет считан в качестве строки.
# Как превратить list строк в list чисел?

".split(', ')" # функц преобразует строку в список
"""
data = '15 156 96 3 5 8 52 5'
print(data)

data = data.split()
print(data)
data = list(map(int, data))
print(data)
""" 
# А можно вот так:
"""
data = list(map(int, data.split()))
print(data)
"""

# Функция "filter":
# def where(f, col):
#    return [x for x in col if f(x)],
"""
data = [15, 65, 9, 36, 175]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)
"""

# Функция "zip":
"""
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
Print(data)# [('user1', 4), ('user2', 5), ('user3', 9)
# ('user4', 14), ('user5', 7)]

salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data)#[('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)
"""

# Функция "enumerate":
"""
enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
[(0,'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
# функция позволяет пронумеровать набор данных.
users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data)# [(0, 'user1), (1, 'user2), (2, 'user3)]
"""

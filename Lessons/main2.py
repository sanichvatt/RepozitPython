# СПИСОК
"""
list_1 = []
list_1 = list()
list_1 = [1, 2, 3, 8]
print(*list_1[-1])

list_1 = [1, 5]
print(list_1)
list_1.append(8)
print(list_1)
list_1.append(85)
print(list_1)


list_1 = list()
print(list_1)
for i in range(5):
    list_1.append(i)
    print(list_1)

"""

# Удаление последнего элемента списка.
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) # 0
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7]

# Удаление конкретного элемента списка.
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(1)) # 12
# print(list_1) # [7, -1, 21, 0]

# Добавление элемента на нужную позицию.
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11))
# print(list_1) # [12, 7, 11, -1, 21, 0]

"""
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0]) # [1]
# print(list_1[1]) # [2]
# print(list_1[len(list_1)-1]) # [10]
# print(list_1[-5]) # [6]
# print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2]) # [1, 2]
# print(list_1[len(list_1)-2:]) # [9, 10]
# print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18]) # []
# print(list_1[0:len(list_1):6]) # [1, 7]
# print(list_1[::6]) # [1, 7]
"""

# КОРТЕЖ
"""
t = ()
print(type(t))

t = (1, 5, 3,)
print(type(t))

v = [1, 8, 9]
print(v)
print(type(v))

v = tuple(v)
print(v)
print(type(v))

"""
"""
# Множественное присваивание.
a = 1
b = 2
# равносильно:
a, b = 1, 2

# еще такое есть:
a = b = 1
"""
# v = [1, 8, 9]
# v = tuple(v)
# a, b, c = v
# print(a, b, c)

# t = (1, 2, 3, 5,)
# t[0] = 2 # eror
# for i in t:
#     print(i)
# for i in range(len(t)):
#     print(t[i])


# СЛОВАРИ
"""
d = {}
d = dict()

d['q'] = 'qwerty'
print(d)

d['w'] = 'werty'
print(d['w'])
"""

# dictionary = {}
# dictionary = {'up': ''} # Дописать на тайминге 21:21


#МНОЖЕСТВО
"""
q = set()
colors = {'red', 'green', 'blue'}
print(colors)
colors.add('gray')
colors.remove('red')
colors.discard('red') # пропускает удаление если нет значения
colors.clear() # { }
"""
# Операции со множествами в Pyton
"""
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1,2,3,5,8,13,21}
i = a.intersection(b) # i = {8,2,5} пересечение множеств
d1 = a.difference(b) # d1 = {1, 3} вычитание
dr = b.difference(a) # dr = {13, 21}
q = a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}

a = {1, 8, 6}
b = frozenset(a) # замороженное множество
"""

# Создание списка чисел от 1 до 100

# list_1 = [i for i in range(1, 101)]
# Добавим условие четности
# list_1 = [i for i in range(1, 101) if i % 2 == 0]
# Создание пары каждому значению (кортежи)
# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]
# так же можно умножать, делить, прибавлять, вычитать
# list_1 = [i * 2 for i in range(1, 101) if i % 2 == 0]
# print(list_1)

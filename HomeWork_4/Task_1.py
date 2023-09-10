"""
Задача 22: 
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
 Выдать без повторений в порядке возрастания все те числа, которые встречаются 
 в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества.
 m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
 """

n = int(input(f"Введите n = "))
m = int(input(f"Введите m = "))
q1 = list()
q2 = list()
for i in range(n):
    q1.append(input(f"Введите значение первого N набора - "))
for i in range(m):
    q2.append(input(f"Введите значение второго M набора - "))
q1 = set(q1)
q2 = set(q2)
u = q1.union(q2)
u = list(u)
for i in range(len(u)):
    u[i] = int(u[i])

minU = int(u[0])
mini = 0
u1 = list()
l = len(u)
for i in range(l):
    for i in range(int(len(u))):
        if int(u[i]) < minU:
            minU = u[i]
            mini = i
    u1.append(u[mini])
    u = u.pop(mini)
print(u1)
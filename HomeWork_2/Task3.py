# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.
n = int(input("Введите число N = "))
for i in range(1,1000):
    s = 2 ** i
    print (f"2 в степени {i} = {s}")
    if (2 ** (i + 1)) > n:
        break

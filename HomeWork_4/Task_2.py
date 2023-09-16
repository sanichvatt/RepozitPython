"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт
 на круглой грядке, причём кусты высажены только по окружности. Таким образом, 
 у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло
 различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система
 состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один
   заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с
     двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один
 заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
"""
n = int(input("Введите кол-во кустов N = "))
a1 = list()
for i in range(n):
    a1.append(int(input(f"Введите кол-во ягод на кусте - ")))
maxA = 0
for i in range(n):
    if i == 0:
        if a1[i] + a1[n-1] + a1[i+1] > maxA:
            maxA = a1[i] + a1[n-1] + a1[i+1]
    elif i == n - 1:
        if a1[i] + a1[i-1] + a1[0] > maxA:
            maxA = a1[i] + a1[i-1] + a1[0]
    elif i == n - 1:
        if a1[i] + a1[i-1] + a1[i+1] > maxA:
            maxA = a1[i] + a1[i-1] + a1[i+1]
print(f"Максимальное число ягод = {maxA}")
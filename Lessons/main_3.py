# ФУНКЦИИ
"""
def sum_nambers(n, y = 'Hello'):
    print(y)
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa
    print('stop') # строка непрочтется ибо после оператора returne

a = sum_nambers(5)
a = sum_nambers(5, 'qwerty')
print(a)
"""
# Функция с неограниченным числом аргументов
"""
def sum_str(*args):
    res = ''
    for i in args:
        res += i
    return res
print(sum_str('q', 'e', 'l'))
print(sum_str('q', 'e', 'l', 'r', 'f'))
print(sum_str('1', '2', '3', '4', '5'))
"""
# Импорт функции из вспомогательного фала "modul1"

# import modul1
# print(modul1.max1(5, 9))

# from modul1 import max1
# print(max1(5, 9))

# from modul1 import *
# print(max1(5, 10))

# import modul1 as m1
# print(m1.max1(10, 9))

# РЕКУРСИЯ
"""
def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n-1) + fib(n-2)

list_1 = []
for i in range(1, 20):
    list_1.append(fib(i))
print(list_1)
"""

# БЫСТРАЯ СОРТИРОВКА "Разделяй и властвуй"
"""
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([14,5,9,6,3,58,7,5,2,7]))
"""

# СОРТИРОВКА СЛИЯНИЕМ
"""
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list1 = [1,5,6,9,8,7,3,2,1,55,2,4]
merge_sort(list1)
print(list1)
"""

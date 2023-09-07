# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму 
# этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

x = int(0)
y = int(0)

s = int(input('Введите сумму X + Y: '))
p = int(input('Введите произведение X * Y: '))

# x + y = s
# x * y = p
# y = s - x
# y = p / x

# s - x = p / x
# s*x - x*x = p
# x*x - s*x + p = 0

# ax2 + bx + c = a (x − x1) (x − x2) # Равенство теоремы Виетта 

# x1 = (-b+(((b^2)-4*a*c)^-2))/2*a   # Решение через 
# x2 = (-b-(((b^2)-4*a*c)^-2))/2*a   # дискриминант
# D = b^2 - 4ac
# if D<0:
#     print('нет решения')
# x = -b/2a
# x1 = (-b + D^(-2))/2a
# x2 = (-b - D^(-2))/2a


a = 1
b = -s
c = p

D = b**2 - 4*a*c
if D < 0:
    print('Нет решения')
elif D == 0:
    x = (-b) / (2*a)
    y = s - x
    print(f"x={x}, y={y}")
else:
    x1 = ((-b) + (D**(0.5)))/(2*a)
    x2 = ((-b) - (D**(0.5)))/(2*a)
    y1 = s - x1
    y2 = s - x2
    print(f"x1={x1}, y1={y1}")
    print(f"x2={x2}, y2={y2}")





# for i in range(1001):
#     sumArg = int(x + y)
#     genArg = int(x * y)
#     if sumArg != s and genArg != p:
#         for j in range(1001):
#             sumArg = int(x + y)
#             genArg = int(x * y)
#             if sumArg != s and genArg != p:
#                 y += 1
#             else:
#                 print(f"x={x}, y={y}")
#         x += 1
#     else:
#         print(f"x={x}, y={y}")      
# else:
#     print(f"x={x}, y={y}")





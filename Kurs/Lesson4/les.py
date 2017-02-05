# # ax^2+bx+c = 0
import math

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

d = (b**2 - 4*a*c)/2
if d > 0:
    x1 = (-b - math.sqrt(d))/(2*a)
    x2 = (-b + math.sqrt(d))/(2*a)
elif d == 0:
    x = -b/(2*a)
else:
    print('Корней нет')

# n = 1000
# lst = list(range(2, n+1))
# new_lst = []
# while lst:
#     Currant = lst[0]
#     new_lst.append(Currant)
#     # for i, el in enumerate(lst):
#     #     if not el % Currant:
#     #         del lst[i]
#     for i in range(len(lst) -1, -1, -1):
#         if lst[i] % Currant == 0:
#             del lst[i]
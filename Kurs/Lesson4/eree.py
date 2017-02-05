# import random
#
# lst = list(range(100))
# random.shuffle(lst)
# last = len(lst) -1
# while last > 0:
#     for i in range(last):
#         if lst[i] > last[i+1]:
#             lst[i], lst[i+1], = lst[i+1],lst[i]
#             last -= 1

# import math
#
# for t in range (1, 1000)
#     if t % 2 != 0:
#         y += 1
#
# x = -10
# if x > 0:
#     print(1)
# if x < 0:
#     print(-1)

n = 100
x1 = 0
x2 = 1
# print(x1)
while x2 < n:
    print('x1 = ' + str(x1))
    print('x2 = ' + str(x2))
    x1, x2 = x2, x1 + x2

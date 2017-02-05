# 2. import random
# random.randint(0, 10)
# Генерировать случайные числа от 0 до 10 до тех пор, пока не выпадет 0 или 10. Вывести числа, их сумму и количество

import random
count = 0
summa = 0

while True:
    randonio = random.randint(0, 10)
    print(randonio, end=' ')
    count += 1
    summa += randonio
    if randonio == 0 or randonio == 10:
        print('\nКоличество: ' + str(count))
        print('Сумма: ' + str(summa))
        break

try:
    х = 5/0
except ZeroDivisionError:
    print("Something happened")

# import random
#
# my_list = []
# summa = 0
#
# while True:
#     i = random.randint(0, 10)
#     if i == 0 or i == 10:
#         print("Элементы: " + str(my_list))
#         print("Число элементов: " + str(len(my_list)))
#         print("Сумма элементов: " + str(sum(my_list)))
#         break
#     my_list.append(i)
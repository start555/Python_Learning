# Задание 6
# Написать функцию, которая вычисляет число ПИ по формуле Лейбница:
# 1/1 – 1/3 + 1/5 – 1/7 + 1/9 - … = ПИ/4
# и протестировать эту функцию на вычислении длины окружности и площади круга,
# а также сравнить вычисленное значение числа ПИ с math.pi из стандартной библиотеки.

import math

def func(n):
    m = 1
    znak =1
    my_pi = 0
    for i in range(1, n+1):
        my_pi += znak/m
        m += 2
        znak *= -1
    return (my_pi*4)

r_kruga = 40
l1_kruga = str(func(800000)*2*r_kruga)
l2_kruga = str(math.pi*2*r_kruga)
print('L круга (ПИ из func): ' + l1_kruga)
print('L круга (ПИ из math.pi): '+ l2_kruga)
print('S круга (ПИ из func): ' + str(func(800000)*(r_kruga**2)))
print('S круга (ПИ из math.pi): ' + str(math.pi*(r_kruga**2)))
print('Дельта между ПИ:' + str(math.pi - func(800000)))

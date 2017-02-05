# 3. Известны площади круга и квадрата. Определить:
# a) уместится ли круг в квадрате?
# b) уместится ли квадрат в круге?

import math

kr = float(input('Введите площадь круга: '))
kv = float(input('Введите площадь квадрата: '))

diametrkr = (math.sqrt(kr/math.pi))*2
diagonalkv = math.sqrt(2*kv)

if diametrkr < diagonalkv:
    print('круг вписался в квадрат')
else:
    print('квадрат внутри круга')
# 3. Четные элементы
# Выведите все четные элементы списка. При этом используйте цикл for,
# перебирающий элементы последовательности,
# а не их индексы!
import math
my_list = [1, 15, -8, 6, 41, 0]
for el in my_list:
    if math.fmod(el, 2) == 0:
        print(el)
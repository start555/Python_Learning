# 5. Создать список из n случайных чисел от 0 до 10 и вывести его
import random
lst = list(range(0, 10))
random.shuffle(lst)
print(lst)
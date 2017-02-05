# 7. Создать множество из n случайных чисел от 0 до 10 и вывести его
import random
lst = list(range(0, 10))
random.shuffle(lst)
A = set(lst)
print(A)


for i in 'hello world':
    if i == 'o':
        continue
    print(i * 2, end=' ')
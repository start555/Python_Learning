# 2. Количество совпадающих чисел
# Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
# Примечание. Эту задачу на Питоне можно решить в одну строчку.

A = {5, 3, 2, 6, 1}
B = {8, 3, 1}
print(len(A.intersection(B)))
print(A.intersection(B))
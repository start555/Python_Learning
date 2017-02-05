# 1. Получить сумму кубов первых n натуральных чисел

n = 100
summa = 0
for i in range(1, n+1):
   summa += i ** 3
print(summa)
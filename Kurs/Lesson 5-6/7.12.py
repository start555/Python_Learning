# Найти сумму целых положительных чисел, больших 30 и меньших 100,
# кратных трем и оканчивающихся на 2, 4 и 8.

n = list(range(30, 101))
i = 0
sum = 0
while i < len(n):
    if n[i]%3 == 0 and (n[i]%10 == 2 or n[i]%10 == 4 or n[i]%10 == 8):
        sum += n[i]
    i += 1
print(sum)
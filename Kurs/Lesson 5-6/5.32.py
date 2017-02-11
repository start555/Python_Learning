# Вычислить сумму

def func(n):
    if n == 0:
        return "Число должно быть больше 0!!!"
    elif n == 1:
        return 1
    else:
        return 1/n + func(n-1)


n = int(input("Введите любое натуральное число: "))
print(func(n))
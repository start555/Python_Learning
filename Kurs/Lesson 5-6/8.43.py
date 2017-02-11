# Дано натуральное число n. Вычислить

def func(n):
    if n == 0:
        return "Число должно быть больше 0!!!"
    elif n == 1:
        return 1
    else:
        return n**n + func(n-1)


n = int(input("Введите любое натуральное число: "))
print(func(n))
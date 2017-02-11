# Найти:
# а) сумму кубов всех целых чисел от 20 до 40

# n = list(range(20, 41))
# i = 0
# sum = 0
# while i < len(n):
#     b = n[i]**3
#     sum = sum + b
#     i = i+1
# print(sum)

# б) сумму квадратов всех целых чисел от a до 50 (значение a вводится
# с клавиатуры; 0 <= a <= 50);

b = int(input('Введите чило <= 50: '))
n = list(range(b, 51))
i = 0
sum = 0
while i < len(n):
    b = n[i]**2
    sum = sum + b
    i = i+1
print(sum)

# в) сумму квадратов всех целых чисел от 1 до n (значение n вводится
# с клавиатуры; 1 n 100);

# b = int(input('Введите чило: '))
# n = list(range(1, b+1))
# i = 0
# sum = 0
# while i < len(n):
#     b = n[i]**2
#     sum = sum + b
#     i = i+1
# print(sum)

# г) сумму квадратов всех целых чисел от a до b (значения a и b вводятся с клавиатуры; b a)

# b = int(input('Введите чило от: '))
# c = int(input('Введите чило до: '))
# n = list(range(b, c+1))
# i = 0
# sum = 0
# while i < len(n):
#     b = n[i]**2
#     sum = sum + b
#     i = i+1
# print(sum)

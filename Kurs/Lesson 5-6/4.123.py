# 4.123. Даны вещественные положительные числа a, b, c.
# Если существует треугольник со сторонами a, b, c, то определить, является ли он прямоугольным.

from math import sqrt

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

if a+b < c or a+c < b or c+b < a:
    print('Треугольник не существует')
elif a == sqrt(b**2 + c**2) or b == sqrt(a**2+c**2) or c == sqrt(b**2 + a**2):
    print('Является ли он прямоугольным?: Yes')
else:
    print('Является ли он прямоугольным?: Nope')

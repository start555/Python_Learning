
class Square():
    def __init__(self, x):
        self.x = x
    def perim(self):
        return self.x*4
    def __str__(self):
        return "squre {t}x{t}".format(t=self.x)

s1 = Square(10)
print(s1.x)


class Treangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimetr(self):
        return (self.a + self.b + self.c)
    def perimt(self):
        return (self.a + self.b + self.c)/2
    def sq(self):
        return (self.perimt*(self.perimt - self.a)*(self.perimt - self.b)*(self.perimt - self.c))**0.5

per = Treangle(3, 3, 2)
print(per.perimetr())
print(per.sq())

# 1. Класс стакан
# Создать класс стакан с полем объем и методами: добавить воды, добавить молока, вылить часть смеси,
# вывести количество смеси. Реализовать проверки на добавление отрицательного количества и на переполнение.

class Stakan():
    def __init__(self, value, max_value):
        self.value = value
        self.max_value = max_value

    def add_water(self, water):
        self.value = self.value + water

    def add_milk(self, milk):
        self.value = self.value + milk

    def minus_part_smesi(self, minus_part):
        self.value = self.value - minus_part


    def perepolnenie(self):
        return (self.max_value - self.value) < 0





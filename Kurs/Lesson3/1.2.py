# 2. Даны объемы и массы двух тел из разных материалов. Материал какого из тел имеет большую плотность?


p1massa = float(input('Масса тела 1: '))
p1value = float(input('V тела 1: '))
p2massa = float(input('Масса тела 2: '))
p2value = float(input('V тела 2: '))

p1 = p1massa/p1value
p2 = p2massa/p2value

if p1 > p2:
    print('Плотность тела 1 больше чем тела 2')
elif p1 < p2:
    print('Плотность тела 1 меньше тела 2')
else:
    print('Плотность тела 1 и тела 2 равны')
# 4.64. Определить, является ли заданное шестизначное число счастливым.
# (Счастливым называют такое шестизначное число, что сумма его первых трех цифр
# равна сумме его последних трех цифр.)

n = list(input("Введите любое 6-значное число: "))
first_list = n[0:3:1]
second_list = n[-1:-4:-1]

first_sum = 0
for i in first_list:
    first_sum += int(i)

second_sum = 0
for i in second_list:
    second_sum += int(i)

if first_sum == second_sum:
    print("Счастливое число")
else:
    print("Несчастливое число")
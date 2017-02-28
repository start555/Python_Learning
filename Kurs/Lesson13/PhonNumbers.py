# Дан список телефонных номеров в произвольном формате.
# Преобразовать номера в формат +375 (17) 222-22-22 с помощью регулярных выражений

import re

phone_numbers = ["+37544-1474788", "+375-29-814-78-66", "375176120012", "+375(44)-557-63-70", "375(33)-271-33-00",
                 "375172333333", "+37517222-22-22", "375(17)3333333", "375(17)3333333", "375(17)3333333S",
                 "37517999999999999999"]

# удаляем все символы, чтобы иметь номера, состоящие из цифр
res = re.sub(r"[-()+]","", str(phone_numbers))
result = str(re.findall(r'\w{12}', res))

#преобразуем первую часть каждого номера
result = re.sub(r"37517", "+375 (17) ",  result)
result = re.sub(r"37544", "+375 (44) ",  result)
result = re.sub(r"37533", "+375 (33) ",  result)
result = re.sub(r"37529", "+375 (29) ",  result)
print("Начальная строка с номерами: " + result)

# удаляем открывающуюся и закрывающуюся скобки, и кавычки
result = re.sub(r"\[", "", result)
result = re.sub(r"\]", "", result)
result = re.sub(r"'", "", result)

# разбиваем строку на отдельные номера и сохраняем в список
my_list = result.split(", ")
print("Список номеров: " + str(my_list))

# функция преобразования номеров
def func(string):
    result = re.search(r" \d\d\d", string).group()
    new_result = result + "-"
    string = string.replace(result, new_result)

    result = re.search(r"-\d\d", string).group()
    new_result = result + "-"
    string = string.replace(result, new_result)
    return string

# применение функции к каждому номеру из списка
for i in my_list:
    print(func(i))


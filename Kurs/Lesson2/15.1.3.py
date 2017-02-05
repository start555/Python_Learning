# 3. Количество слов
# Дана строка, состоящая из слов, разделенных пробелами.
# Определите, сколько в ней слов. Используйте для решения задачи метод count.
# Циклы не использовать.


str1 = ' In  Python, the count method returns the count of ' \
       'how many times an object occurs in a list. ' \
       'The syntax for the count method is  really straightforward: '

# remove extra spaces in the row
str2 = str1.strip(' ')
str3 = str2.replace('  ', ' ')

# spaces count
str4 = str3.count(' ')
print(str4 + 1)


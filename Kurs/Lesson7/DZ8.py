#  В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
# Во второй строке дано одно число days -- число дней.
# Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней, равное days.
# Примечание:
# Для решения этой задачи используйте стандартный модуль datetime.
# Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta﻿ для прибавления дней к дате.

from datetime import datetime, timedelta

date_str = '2017-02-10'
delta_days_str = '15'

my_time = datetime.strptime(date_str, '%Y-%m-%d')
my_new_time = my_time.date()
my_new_time += timedelta(days = int(delta_days_str))
print("Новая дата в формате год-месяц-день: " + str(my_new_time))

 # объявляем функцию
def func(tpl, lst):
    if len(tpl) == len(lst):
        return dict(zip(tpl, lst))
    elif len(lst) > len(tpl):
        lst.pop()
        return func(tpl, lst)
    else:
        new_lst = list(tpl)    # преобразуем кортеж к списку, чтобы можно было вызвать метод удаление .pop
        new_lst.pop()
        tpl = tuple(new_lst)   # преобразуем список назад к кортежу
        return func(tpl, lst)



# вызываем функцию
my_tpl = (1, 2, 3, 8, 90, 0, 77)
my_lst = [4, 5, 6, 88, 9]

D = func(my_tpl, my_lst)
print(D)
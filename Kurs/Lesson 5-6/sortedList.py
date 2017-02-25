# Самосортирующийся список-множество
# Нужно реализовать класс-контейнер для хранения упорядоченного неповторяющегося набора целых и вещественных чисел, который будет содержать метод для добавления произвольного числа элементов (после добавления последовательность чисел должна оставаться отсортированной), методы для получения n максимальных или минимальных элементов и получения элемента по номеру, методы удаления элемента с начала, с конца или по номеру, метод изменения порядка сортировки. Порядок сортировки последовательности задается параметром конструктора и хранится в одном из полей объекта.
# Нужно создать два объекта этого класса с отличающимися направлениями сортировки элементов, заполнить их случайными числами и добавить элементы второго объекта в первый.
# Вывести сгенерированные объекты и объект полученный в результате добавления. Вывод произвести через метод класса-контейнера.

class SortedSetList():
    def __init__(self, sorted_order):
        self.container = []
        self.sorted_order = sorted_order

    # метод вывода
    def __repr__(self):
        print("[{0}]".format(", ".join(str(i) for i in self.container)))

    # метод добавления произвольного числа элементов (добавить можно список, множество, кортеж)
    def add_new_items(self, sequence):
        if type(sequence) is set or type(sequence) is list:
            n = len(sequence)
            while n > 0:
                n -= 1
                i = sequence.pop()
                if i not in self.container:
                    self.container.append(i)
        elif type(sequence) is tuple:
            n = len(sequence)
            while n > 0:
                n -= 1
                i = sequence.__getitem__(n)
                if i not in self.container:
                    self.container.append(i)
        elif type(sequence) is int or type(sequence) is float:
            if sequence not in self.container:
                self.container.append(sequence)
        elif type(sequence) is SortedSetList:
            print("Невозможно добавить объект класса SortedSetList")
        return self.container.sort(reverse=self.sorted_order)


    # метод смены порядка сортировки
    def change_sort_order(self):
        self.container.reverse()
        return self.container


    # метод вывода n максимальных элементов, которые собираются в новый список без изменения начального списка
    def get_some_max_elements(self, n):
        if n > len(self.container):
            print("Длина списка меньше, чем введенное число " + str(n))
        else:
            additional_list = self.container.copy()
            max_list = []
            while n > 0:
                n -= 1
                i = max(additional_list)
                additional_list.remove(i)
                max_list.append(i)
            print(str(len(max_list)) + " максимальн.знач.: " + " , ".join([str(i) for i in max_list]))


    # метод вывода n минимальных элементов, которые собираются в новый список без изменения начального списка
    def get_some_min_elements(self, n):
        if n > len(self.container):
            print("Длина списка меньше, чем введенное число " + str(n))
        else:
            additional_list = self.container.copy()
            min_list = []
            while n > 0:
                n -= 1
                i = min(additional_list)
                additional_list.remove(i)
                min_list.append(i)
            print(str(len(min_list)) + " минимальн.знач.: " + " , ".join([str(i) for i in min_list]))


    # вспомогательный метод для преобразования списка в словарь (необходимо для реализации метода получения элемента по индексу)
    def convert_list_to_dict(self):
        additional_list = []
        n = len(self.container)
        while n > 0:
            n -= 1
            additional_list.append(n+1)
        additional_list.reverse()
        my_dict = dict(zip(additional_list, self.container))
        return my_dict


    # метод получения элемента по индексу
    def get_element_by_index(self, n):
        if n > len(self.container):
            print("Номер превышает длину списка!!!")
        elif n == 0:
            print("Номер должен быть больше 0!!!")
        else:
            print(self.convert_list_to_dict().get(n))


    # метод удаления последнего элемента
    def delete_last_element(self):
        self.container.pop()


    # метод удаления первого элемента
    def delete_first_element(self):
        self.container.pop(0)

    # метод удаления элемента по индексу
    def delete_element_by_index(self, n):
        if n > len(self.container):
            print("Номер превышает длину списка!!!")
        elif n == 0:
            print("Номер должен быть больше 0!!!")
        else: self.container.pop(n-1)




# порядок сортировки задается параметром конструктора True/False
first_list = SortedSetList(True)
second_list = SortedSetList(False)
third_list = SortedSetList(False)

# добавляем элементы в виде чисел или коллекций (список, множество, кортеж). Получим
first_list.add_new_items({18, -4, 89, -100, -100, 6.863, 73, 15, -22})
second_list.add_new_items([11, 0.7, 23, -17, 1030, -2, 64.5])
third_list.add_new_items((66, 10, -7, 63, 7, 10, -2))

# вывод
first_list.__repr__()
second_list.__repr__()
third_list.__repr__()

# смена порядка сортировки
first_list.change_sort_order()
first_list.__repr__()

# удаление первого элемента, затем последнего, затем 2-го
first_list.delete_first_element()
first_list.__repr__()
first_list.delete_last_element()
first_list.__repr__()
first_list.delete_element_by_index(2)
first_list.__repr__()

# нахождение 2 минимальных значений
second_list.get_some_min_elements(2)

# нахождение 3 максимальных значений
third_list.get_some_max_elements(3)

# нахождение элемента по индексу
third_list.get_element_by_index(1)

# не выходит добавить объект класса-контейнера к другому объекту этого же класса
first_list.add_new_items(second_list)
first_list.__repr__()
# 1. Написать реализацию вычисления числа Фибоначчи через рекурсию с подсчетом
# количества произведенных вызовов функции.
# Подсчет количества вызовов функции реализовать через замыкание.

def init():
    count = 0

    def Fib(n):
        nonlocal count
        count += 1

        if n <= 1: res = n
        else: res = Fib(n - 1) + Fib(n - 2)
        return res

    def count_Fib():
        nonlocal count
        return count

    return Fib, count_Fib


if __name__ == "__main__":
    n = 29

    fibonachi, countFib = init()
    f = fibonachi(n)
    count = countFib()
    print('fibonachi', f, 'count', count)
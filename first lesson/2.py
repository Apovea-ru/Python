"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""


# 1 алгоритм
def onn(listone):
    mina = listone[0]
    for el in listone:
        for el2 in listone:
            if el2 < el:
                mina = el2
    return mina


# 2 алгоритм
def on(listtwo):
    minu = listtwo[0]
    for el in listtwo:
        if minu > el:
            minu = el
    return minu


arrayone = [0, 2, -2, 12, -25]
print(onn(arrayone))
print(on(arrayone))

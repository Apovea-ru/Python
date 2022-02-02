"""
Задание 3.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


def bestmoney(company):  # O(N^2)
    maximm = list(company.keys())  # O(1)
    maximm = maximm[0]  # O(1)
    for key, value in company.items():  # O(N)
        if value > company[maximm]:  # O(N)
            maximm = key  # O(1)
    return maximm  # O(1)


def bestbestmoney(companyy):  # O(N)
    maxis = list(companyy.keys())  # O(1)
    maxis = maxis[0]  # O(1)
    valueofcompany = companyy[maxis]  # O(N)
    for key, value in companyy.items():  # O(N)
        if value > valueofcompany:  # O(1)
            maxis = key  # O(1)
            valueofcompany = value  # O(1)
    return maxis  # O(1)


Companies = {'Google': 231421241231254, 'Yandex': 343252352352352367346, 'Mail': 34435436534634634625}

print(bestmoney(Companies))
print(bestbestmoney(Companies))

# Вывод: 2 алгоритм более эффективен, так как происходит меньше процедур по перебору элементов словаря.

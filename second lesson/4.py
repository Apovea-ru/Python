"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def findsum(n, numberone=1, Summa=1):
    if n == 1:
        return Summa
    elif n < 0 or n == 0:
        return 'Введите число перебора больше 0'
    elif numberone < 0 and n != 1:
        numberone = abs(numberone / 2)
        Summa = Summa + numberone
        print(numberone, Summa)
        n -= 1
        return findsum(n, numberone, Summa)
    elif numberone > 0 and n != 1:
        numberone = -numberone / 2
        Summa = Summa + numberone
        print(numberone, Summa)
        n -= 1
        return findsum(n, numberone, Summa)


print(findsum(3))

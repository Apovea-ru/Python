"""
Задание 2.	Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""
evennumber = int()
oddnumber = int()


def evenorodd(number):
    even = '02468'
    odd = '13579'
    if number in even:
        return 'even'
    elif number in odd:
        return 'odd'


def findnumber(number, even_number=0, odd_number=0):
    number = str(number)
    if len(number) == 1:
        if evenorodd(number) == 'even':
            even_number += 1
            return f"четных:{even_number} и нечетных:{odd_number}"
        elif evenorodd(number) == 'odd':
            odd_number += 1
            return f"нечетных:{odd_number} и четных: {even_number}"
    elif len(number) > 1:
        if evenorodd(str(int(number) % 10)) == 'even':
            even_number += 1
            return findnumber(str(int(number) // 10), even_number, odd_number)
        elif evenorodd(str(int(number) % 10)) == 'odd':
            odd_number += 1
            return findnumber(str(int(number) // 10), even_number, odd_number)



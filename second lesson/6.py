"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""

import random


def random_number(number_choise, n=10):
    human_choise = int(input('Введите число: '))
    if human_choise == number_choise and n >= 0:
        return f'Вы угадали, это число {human_choise}'
    elif human_choise > number_choise and n > 0:
        print('Число меньше')
        n -= 1
        return random_number(number_choise, n)
    elif human_choise < number_choise and n > 0:
        print('Число больше')
        n -= 1
        return random_number(number_choise, n)
    elif n == 0:
        return f'Вы не угадали, вот число {number_choise}'


random_choise_number = random.randint(0, 100)
print(random_number(random_choise_number))

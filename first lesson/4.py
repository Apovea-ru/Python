"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


def verification(dictone, user, passwordone):#O(N)
    for key, value in dictone.items():#O(N)
            if value['password'] == passwordone:#O(1)
                if value['registred'] == 'yes':#O(1)
                    return 'Можете заходить'#O(1)
                elif value['registred'] != 'yes':#O(1)
                    return 'Вам нужно пройти активацию'#O(1)
            elif value['password'] != passwordone:#O(1)
                return 'Не верный пароль'#O(1)
    return 'Нет такого пользователя'#O(1)


def verificationtwo(dicttwo, user, passwordtwo):#O(1)
    if dicttwo.get(user):#O(1)
        if dicttwo[user]['password'] == passwordtwo:#O(1)
            if dicttwo[user]['registred'] == 'yes':#O(1)
                return 'Можете заходить'#O(1)
            elif dicttwo[user]['registred'] != 'yes':#O(1)
                return 'Вам нужно пройти активацию'#O(1)
        elif dicttwo[user]['password'] != passwordtwo:#O(1)
            return 'Не верный пароль'#O(1)
    return 'Нет такого пользователя'#O(1)


dictofusers = {'user1': {'password': 1231234, 'registred': 'yes'},
               'user2': {'password': 123123, 'registred': 'not'}}

print(verification(dictofusers, 'user2', 123123))
print(verificationtwo(dictofusers, 'user1', 1231234))

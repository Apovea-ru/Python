"""
Задание 5. На закрепление навыков работы со стеком
Реализуйте структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим
стеком порогового значения.
После реализации структуры, проверьте ее работу на различных сценариях.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стека можно реализовать добавлением новой пустой стопки
в массив стопок (lst = [[], [], [], [],....]) либо созданием объекта
класса-стек в самом же классе.
"""


class StackOfPlates:
    def __init__(self, maxsize):
        self.elems = [[]]
        self.maxsize = maxsize

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == [[]]

    def first_among_equals(self, plate):
        if len(self.elems) == 0:
            self.elems[0].insert(0,[])
            self.elems.insert(0, plate)


        elif len(self.elems[0]) >= self.maxsize:
            self.elems.insert(0, [])
            self.elems[0].insert(0, plate)
        else:
            self.elems[0].insert(0, plate)


    def plateisout(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)

    def get_stack(self,i):
        return self.elems[i]

    def stack_count(self):
        return len(self.elems)

    def all_plates(self):
        summ=0
        for i in self.elems:
            summ+=len(i)
        return(summ)


if __name__ == '__main__':
    plates = StackOfPlates(3)
    plates.first_among_equals('Plate1')
    plates.first_among_equals('Plate2')
    plates.first_among_equals('Plate3')
    plates.first_among_equals('Plate4')




    print(plates.maxsize)
    print(plates.get_stack(1))
    print(plates.stack_count())
    print(plates.all_plates())
    print(plates.is_empty())

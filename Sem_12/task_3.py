# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.

from collections import deque

class FactorialGen:
    def __init__(self, *args):
        if len(args) == 1:
            self.start = 1
            self.stop = args[0]
            self.step = 1
        elif len(args) == 2:
            self.start, self.stop = args
            self.step = 1
        else:
            self.start, self.stop, self.step = args


    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.stop:
            factorial = 1
            for i in range(2, self.start + 1):
                factorial *= i
            self.start += self.step
            return factorial
        raise StopIteration



if __name__ == '__main__':
    fact1 = FactorialGen(5)
    fact2 = FactorialGen(2, 7)
    fact3 = FactorialGen(2, 8, 2)

    for fact in fact1, fact2, fact3:
        for el in fact:
            print(el, end=' ')
        print()





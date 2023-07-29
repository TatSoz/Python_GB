# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и их факториалов.

from collections import deque

class Factorial:
    def __init__(self, k: int):
        self.results = deque(maxlen=k)

    def __call__(self, number: int, *args, **kwargs):
        factorial = 1
        for i in range(2, number + 1):
            factorial *= i
        self.results.append({number: factorial})
        return self.results[-1]

    def previous_values(self):
        return self.results


if __name__ == '__main__':
    fact1 = Factorial(5)
    print(fact1(4))
    print(fact1(5))
    print(fact1(3))
    print(fact1(7))
    print(fact1(8))
    print(fact1(2))
    print(fact1.previous_values())
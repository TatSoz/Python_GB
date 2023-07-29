# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.

from collections import deque
import time
import json


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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        results_dict = dict()
        while self.results:
            results_dict.update(self.results.popleft())
        with open(f'file{time.time()}.json', 'w', encoding='utf-8') as f:
            json.dump(results_dict, f)



if __name__ == '__main__':
    fact1 = Factorial(5)
    print(fact1(4))
    print(fact1(5))
    print(fact1(3))
    print(fact1(7))
    print(fact1(8))
    print(fact1(2))
    print(fact1.previous_values())

    with fact1 as f1:
        print(f1)


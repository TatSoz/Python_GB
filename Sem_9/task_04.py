# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой функции.

from typing import Callable


def count_f(num: int = 1):
    def deco(func: Callable):
        results = []
        def wrapper(*args, **kwargs):
            for i in range(num):
                results.append(func(*args, **kwargs))

            return results

        return wrapper

    return deco


@count_f(5)
def get_summ(num1: int, num2: int, *args, **kwargs) -> int:
    return num1 + num2


if __name__ == '__main__':
    print(get_summ(6, 4))
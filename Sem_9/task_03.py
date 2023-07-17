# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.

from typing import Callable
import json
import os

def logger(func: Callable):
    file_name = f'{func.__name__}.json'
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []

    def wrapper(*args, **kwargs):
        json_dict = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        json_dict['result'] = result
        data.append(json_dict)

        with open(file_name, 'w', encoding='utf-8') as f1:
            json.dump(data, f1)

        return result

    return wrapper


@logger
def get_summ(num1: int, num2: int, *args, **kwargs) -> int:
    return num1 + num2



if __name__ == '__main__':
    summ = get_summ(4, 7, x = 10, y = 'Hello', z = True)
    print(summ)



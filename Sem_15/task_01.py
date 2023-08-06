# Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

import logging

def div_number(num_a: int, num_b: int) -> float:
    try:
        result = num_a / num_b
        return result
    except ZeroDivisionError as z:
        logging.basicConfig(level=logging.ERROR, filemode='a', filename='log_1.log', encoding='utf-8')
        logging.error('На ноль делить нельзя!')
        return float('inf') if num_a > 0 else float('-inf')


if __name__ == '__main__':
    print(div_number(10, 3))
    print(div_number(10, 0))
    print(div_number(-10, 0))



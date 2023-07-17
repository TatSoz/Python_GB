# Создайте функцию-замыкание, которая запрашивает два целых числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.

from typing import Callable

def gess_number(num: int, count: int) -> Callable[[], None]:

    def gess():

        for i in range(1, count + 1):
            num_input = int(input(f'Угадайте число от 1 до 100, у Вас {count + 1 - i} попыток: '))
            print(f'Попытка № {i}')
            if num_input == num:
                print('Вы угадали!')
                break
            elif num_input < num:
                print('Загаданное число больше')
            else:
                print('Загаданное число меньше')

    return gess



if __name__ == '__main__':
    game = gess_number(25, 5)
    game()




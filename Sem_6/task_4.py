# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

def guessing(text: str, variants: list[str], counts: int) ->int:
    print(f'Добрый день! Отгадайте загадку: \n{text}')

    for count in range(1, counts + 1):
        answer = input(f'Попытка № {count}... Введите отгадку: ')
        if answer.lower() in variants:
            print('Вы угадали!!!')
            return count

    print(f'Увы, Вы не угадали загадку за {count} попыток...')
    return 0

if __name__ == '__main__':
    guess = "Зимой и летом одним цветом"
    answer_vars = ['елка', 'ёлка', 'ель', 'ёлочка']
    answer_counts = 3

    res = guessing(guess, answer_vars, answer_counts)
    print(f'\nCode {res}')

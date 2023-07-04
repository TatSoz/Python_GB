#Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

def guessing(text: str, variants: list[str], counts: int) ->int:
    print(f'Добрый день! Отгадайте загадку: \n{text}')

    for count in range(1, counts + 1):
        answer = input(f'Попытка № {count}... Введите отгадку: ')
        if answer.lower() in variants:
            print('Вы угадали!!!')
            return count

    print(f'Увы, Вы не угадали загадку за {count} попыток...')
    return 0


def guesses_dict(g_dict: dict[str, list[str]], count: int = 3) -> None:
    for key, value in g_dict.items():
        res = guessing(key, value, count)
        print(f'\nCode {res}')

if __name__ == '__main__':
    guesses = {"Зимой и летом одним цветом": ['елка', 'ёлка', 'ель', 'ёлочка'],
               'Не лает, не кусает, в дом не пускает': ['замок', 'замочек'],
               'Сидит дед во сто шуб одет': ['лук', 'луковица'],
               'Что имеет ухо, но не слышит?': ['игла', 'Игла'],
               'Что всегда идет вперед, но никогда не движется?': ['время', 'Время']}

    guesses_dict(guesses)



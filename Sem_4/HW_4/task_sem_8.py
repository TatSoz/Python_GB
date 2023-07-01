# Задание 8
# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

def change_var() -> None:
    globals()
    change = {}
    for key, value in globals().items():
        if key == 's':
            continue
        if key.endswith('s'):
            change[key[:-1]] = globals()[key]
            globals()[key] = None
    for key, value in change.items():
        globals()[key] = value


if __name__ == '__main__':
    numbers = [2, 3, -2, -3]
    s = 77
    words = ('Привет', 'Hello', 'Bonjour')
    letter = ('a', 'b', 'c')

    print('Заданные переменные: ')
    print(f'{numbers = }')
    print(f'{s = }')
    print(f'{words = }')
    print(f'{letter = }')
    change_var()
    print('\nЗначения переменных после запуска функции: ')
    print(f'{numbers = }')
    print(f'{number = }')
    print(f'{s = }')
    print(f'{words = }')
    print(f'{word = }')
    print(f'{letter = }')

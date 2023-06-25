# Задание 9
# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

START = 2
END = 10
HALF = 2

print('                Таблица умножения:')
for i in range(START, END + 1):
    for j in range(START, END // HALF + 1):
        print(f'{j} X {i:2d} = {i * j:2d}', end="   ")
    print()
print()
for i in range(START, END + 1):
    for j in range(END // HALF + 1, END):
        print(f'{j} X {i:2d} = {i * j:2d}', end="   ")
    print()

#Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайногочисла используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1001
FIRST_TRY = 1
LAST_TRY = 11

num = randint(LOWER_LIMIT, UPPER_LIMIT)
for i in range(FIRST_TRY, LAST_TRY):
    n = int(input(f"Попытка номер {i}, попытайтесь отгадать число: "))
    turn = ""
    if n > num:
        turn = "Меньше"
    elif n < num:
        turn = "Больше"
    else:
        print("Победа!")
        break
    print(turn)
else:
    print("Попыток больше нет, вы проиграли.")


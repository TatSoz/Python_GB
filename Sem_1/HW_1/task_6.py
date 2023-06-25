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

print('Угадайте число от 0 до 1000. У Вас 10 попыток: ')
print('Удачи!')
num = randint(LOWER_LIMIT, UPPER_LIMIT)
for i in range(FIRST_TRY, LAST_TRY):
    n = int(input(f"Попытка номер {i}: "))
    turn = ""
    if n > num:
        turn = "Зададанное число меньше"
    elif n < num:
        turn = "Зададанное число больше"
    else:
        print("Победа!")
        break
    print(turn)
else:
    print("Попыток больше нет, вы проиграли.")


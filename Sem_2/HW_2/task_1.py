# (Задание 6) Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

import sys

MULT = 50
PERCENT = 0.015
EXTRA_PERCENT = 0.03
MIN_VALUE = 30
MAX_VALUE = 600
MAX_COUNT = 3
MAX_SCORE = 5_000_000
TOTAL_SCOPE = 0
START_OPERATIONS = 1



def check_input(message):
    while True:
        input_sum = int(input(message))
        if input_sum % MULT != 0:
            print("Недопустимая сумма. Сумма должна быть кратна 50!")
        else:
            return input_sum


def add_cash(bal, op):
    inc = check_input("Введите сумму для пополнения: ")
    if op % MAX_COUNT == 0:
        bal += bal * EXTRA_PERCENT
    bal += inc
    op += 1
    if bal > MAX_SCORE:
        bal -= bal // 10
    return bal, op


def withdrawal(bal, op):
    if bal > MAX_SCORE:
        bal -= bal // 10
    dec = check_input("Введите сумму для снятия: ")
    percent = dec * PERCENT
    if percent < MIN_VALUE:
        percent = MIN_VALUE
    elif percent > MAX_VALUE:
        percent = MAX_VALUE
    dec += percent
    if bal > dec:
        bal -= dec
    else:
        print("Недостаточно средств!")
    if op % MAX_COUNT == 0:
        bal += bal * EXTRA_PERCENT
    op += 1
    return bal, op


def start():
    balance = TOTAL_SCOPE
    operations = START_OPERATIONS
    while True:
        select = int(input(f"""Баланс: {balance}
Операции со счётом: {operations - 1}

Доступные действия:
1. Пополнить
2. Снять
3. Выход

Выберите действие: """))
        match select:
            case 1:
                balance, operations = add_cash(balance, operations)
            case 2:
                balance, operations = withdrawal(balance, operations)
            case 3:
                sys.exit()
            case _:
                print("Повторите попытку")


start()



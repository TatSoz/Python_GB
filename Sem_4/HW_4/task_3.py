# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

import sys


def check_input(message):
    while True:
        input_sum = int(input(message))
        if input_sum % MULT != 0:
            print("Недопустимая сумма. Сумма должна быть кратна 50!")
        else:
            return input_sum


def check_rich(bal, op, history_op):
    if bal > MAX_SCORE:
        nalog = (bal - MAX_SCORE) // RICH_NALOG
        history_op.append((op, 'Налог на богатство', nalog))
        bal -= nalog
    return bal


def add_cash(bal, op, history_op):
    inc = check_input("Введите сумму для пополнения: ")
    if op % MAX_COUNT == 0:
        bal += bal * EXTRA_PERCENT
    bal += inc
    history_op.append((op, 'Пополнение счёта', inc))
    op += 1
    bal = check_rich(bal, op, history_op)
    return bal, op


def withdrawal(bal, op, history_op):
    bal = check_rich(bal, op, history_op)
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
    history_op.append((op, 'Снятие со счёта', dec))
    history_op.append((op, 'Комиссия за снятие', percent))
    op += 1
    return bal, op


def start():
    balance = TOTAL_SCOPE
    operations = START_OPERATIONS
    operations_list = []
    while True:
        select = int(input(f"""Баланс: {balance}
Операции со счётом: {operations - 1}

Доступные действия:
1. Пополнить
2. Снять
3. История операций
4. Выход

Выберите действие: """))
        match select:
            case 1:
                balance, operations = add_cash(balance, operations, operations_list)
            case 2:
                balance, operations = withdrawal(balance, operations, operations_list)
            case 3:
                print('Выполненые операции: ', *operations_list, sep='\n')
            case 4:
                sys.exit()
            case _:
                print("Повторите попытку")


if __name__ == '__main__':
    MULT = 50
    PERCENT = 0.015
    EXTRA_PERCENT = 0.03
    RICH_NALOG = 10
    MIN_VALUE = 30
    MAX_VALUE = 600
    MAX_COUNT = 3
    MAX_SCORE = 5_000_000
    TOTAL_SCOPE = 0
    START_OPERATIONS = 1

    start()





# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить. В этом случае берётся первый в месяце день недели,
# текущий день недели и/или текущий месяц.
# *Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые, т.е не мая, а 5.


import argparse
from datetime import datetime
import logging


logging.basicConfig(filename='log_4.log', encoding='utf-8', level=logging.ERROR)
log = logging.getLogger(__name__)


def pars():
    parser = argparse.ArgumentParser(prog='Задача №5 семенара 15',
                                     epilog='Строка -> Дата',
                                     description='Данный модуль преобразует строки в дату')

    parser.add_argument('-c', '--count', default='1ый', help='День недели по счету')
    parser.add_argument('-w', '--week_day', default=datetime.now().weekday(), help='День недели')
    parser.add_argument('-m', '--month', default=datetime.now().month, help='Месяц года')

    args = parser.parse_args()
    return text_to_date(' '.join((args.count, args.week_day, args.month)))


def text_to_date(text: str) -> datetime | None:
    try:
        count, week_day, month = text.split()
    except ValueError as e:
        log.error('Неверный формат строки!')
        return None

    days_list = ('пон', 'вто', 'сре', 'чет', 'пят', 'суб', 'вос')
    months_list = ('янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек')

    count = int(count[:-2])
    week_day = days_list.index(week_day[:3])
    month = months_list.index(month[:3]) + 1

    day_count = 0
    for day in range(1, 32):
        date = datetime(day=day, month=month, year=datetime.now().year)
        if date.weekday() == week_day:
            day_count += 1
            if day_count == count:
                return date


if __name__ == '__main__':
    print(pars())




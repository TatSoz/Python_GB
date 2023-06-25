# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.
# с использованием тернального оператора

import sys

data = [1, 5.5, 'news', True, (2, 4, 3), 'new_str', True]

for i, item in enumerate(data, start=1):
    check_int = ', это целое число' if isinstance(item, int) else ''
    check_str = ', это строка' if isinstance(item, str) else ''

    print(f'Порядковый номер - {i},'
          f'Значение - {item}, '
          f'Адрес в памяти - {id(item)}, '
          f'Размер в памяти - {sys.getsizeof(item)},  '
          f'Хеш - {hash(item)}'
          f'{check_int}'
          f'{check_str}')




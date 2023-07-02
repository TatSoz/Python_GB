# ✔ Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного генератора,
# где каждый элемент генератора — отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт» без перехода на новую строку.

START = 2
END = 10
COLUMNS = 4
SEP = 2


table = (f'\t{num2:>{SEP}} X {num1:>{SEP}} = {(num1 * num2):>{SEP}}\t' if num2 != col + COLUMNS -1
         else f'{num2:>{SEP}} x {num1:{SEP}} = {(num1 * num2):>{SEP}}\n' if num1 != END
         else f'{num2:>{SEP}} x {num1:{SEP}} = {(num1 * num2):>{SEP}}\n\n'
         for col in range(START, END, COLUMNS)     #2, 6
         for num1 in range(START, END + 1)   #2, 3, 4, 5, 6, 7, 8, 9, 10
         for num2 in range(col, col + COLUMNS))
print(*table)



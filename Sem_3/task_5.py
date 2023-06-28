# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

int_list = [5, 2, 5, 5, 4, 2, 1, 1, 8, 7, 8, 4]
index_list = []
index_list2 = []
START = 1

print(int_list)

for i in range(len(int_list)):
    if int_list[i] % 2 == 1:
        index_list.append(f'{int_list[i]}: {i + 1}')

print(index_list)

for i, item in enumerate(int_list, START):  # Решение с семинара
    if item % 2 == 1:
        index_list2.append(f'{item}: {i}')

print(index_list2)
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

my_list = [5, 2, 5, 5, 4, 2, 1, 1, 8, 7, 8, 4]
new_list = []
COUNT = 2

print(my_list)

for i in range(len(my_list)):
    if my_list.count(my_list[i]) != COUNT:
        new_list.append(my_list[i])

print(new_list)

for item in set(my_list):  # решение с семинара
    if my_list.count(item) == COUNT:
        for i in range(COUNT):
            my_list.remove(item)

print(my_list)

# Вариант 3
sort_list = sorted(my_list)
for item in sort_list:
    if sort_list.count(item) == COUNT:
        my_list.remove(item)

print(my_list)
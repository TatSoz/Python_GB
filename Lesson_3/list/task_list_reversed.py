# Функция принимает на вход последовательность, которая поддерживает порядок
# элементов, возвращает функция объект итератор с обратным порядком элементов.

my_list = [4, 8, 2, 9, 1, 7, 2]
res = reversed(my_list)
print(type(res), res)
rev_list = list(reversed(my_list))
print(rev_list)

for item in reversed(my_list):
    print(item)


# Если нам нужно развёрнутая версия списка логичные и удобнее использовать встроенный метод reverse.(без создания копии)

my_list = [4, 8, 2, 9, 1, 7, 2]
my_list.reverse()
print(my_list)

# разворот с использованием среза  [::-1]

my_list = [4, 8, 2, 9, 1, 7, 2]
new_list = my_list[::-1]
print(my_list, new_list, sep='\n')




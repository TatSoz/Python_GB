# Метод split позволяет разбить строку на отдельные элементы в соответствии с
# разделителем и поместить результат в список.

link = 'https://habr.com/ru/users/dzhoker1/posts/'
urls = link.split('/')
print(urls)
a, b, c = input('Введите 3 числа через пробел: ').split()
print(c, b, a)

a, b, c, *_ = input('Введите не менее трёх чисел через пробел:  ').split()

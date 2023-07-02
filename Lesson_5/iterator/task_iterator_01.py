"""iter(object[, sentinel])"""

a = 42
#  iter(a)  # ошибка

data = [2, 4, 6, 8]
list_iter = iter(data)
print(list_iter)

data = [2, 4, 6, 8]
list_iter = iter(data)
print(*list_iter)
print(*list_iter)  # итератор распаковывается только один раз
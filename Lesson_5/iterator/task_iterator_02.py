import functools

data = [2, 4, 6, 8]
#  list_iter = iter(data. 6)  # ошибка

f = open('my_data.bin', 'rb')
for block in iter(functools.partial(f.read, 16), b''):
    print(block)
f.close()


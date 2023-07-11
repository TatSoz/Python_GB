#Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

from random import choices, randint
from string import ascii_lowercase, digits

def gen_ext(ext: str, min_len: int = 6, max_len: int = 30, min_bytes: int = 256, max_bytes: int = 4096, num_files: int = 42) -> None:

    for _ in range(num_files):
        name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_len, max_len)))
        data = bytes(randint(0, 255) for _ in range(randint(min_bytes, max_bytes)))
        with open(f'{name}.{ext}', 'wb') as f:
            f.write(data)


if __name__ == '__main__':
    gen_ext('txt')



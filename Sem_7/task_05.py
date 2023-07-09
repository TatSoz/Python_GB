# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.


from random import choices, randint
from string import ascii_lowercase, digits

def gen_ext(ext: str, min_len: int = 6, max_len: int = 30, min_bytes: int = 256, max_bytes: int = 4096, num_files: int = 42) -> None:

    for _ in range(num_files):
        name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_len, max_len)))
        data = bytes(randint(0, 255) for _ in range(randint(min_bytes, max_bytes)))
        with open(f'{name}.{ext}', 'wb') as f:
            f.write(data)


def create_files_updated(**kwargs):
    for k, v in kwargs.items():
        gen_ext(ext=k, num_files=v)



if __name__ == '__main__':
    create_files_updated(txt=2, bin=3, jpeg=2)



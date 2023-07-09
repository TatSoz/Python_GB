# Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.


import os.path
from random import choices, randint
from string import ascii_lowercase, digits

def gen_ext(ext: str, min_len: int = 6, max_len: int = 30, min_bytes: int = 256, max_bytes: int = 4096, num_files: int = 42) -> None:
    folder_name = 'Files'
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    for _ in range(num_files):
        name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_len, max_len)))
        data = bytes(randint(0, 255) for _ in range(randint(min_bytes, max_bytes)))
        with open(f'{folder_name}/{name}.{ext}', 'wb') as f:
            f.write(data)


def create_files_updated(**kwargs):
    for k, v in kwargs.items():
        gen_ext(ext=k, num_files=v)



if __name__ == '__main__':
    create_files_updated(png=2, pdf=3, doc=2, jpeg=3, bin=1)




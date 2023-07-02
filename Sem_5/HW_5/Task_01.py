# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def split_path(path: str) -> tuple:
    *path, file_name, file_extension = path.replace('.', '\\').split('\\')
    path = '/'.join(path)
    return path, file_name, file_extension


if __name__ == '__main__':
    abs_path = 'D:\Tatyana\GB\Python_GB\Sem_5\HW_5\Task_01.py'
    print(split_path(abs_path))


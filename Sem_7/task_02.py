# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

from random import choice, randint

LETTERS_VOVS = 'aeyuio'
LETTERS_CONS = 'qwrtpsdfghjklzxcvbnm'
MIN_LENGHT = 4
MAX_LENGHT = 7

def pseudo_gen(num_names: int, file_name: str) -> None:
    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(num_names):
            name = ''.join(choice(LETTERS_VOVS) if i in (1, 4, 6) else choice(LETTERS_CONS)
                           for i in range(randint(MIN_LENGHT, MAX_LENGHT)))
            f.write(name.capitalize() + '\n')


if __name__ == '__main__':
    pseudo_gen(10, 'task_02.txt')




            



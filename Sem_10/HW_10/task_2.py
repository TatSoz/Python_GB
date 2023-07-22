# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства.
# Задачи должны решаться через вызов методов экземпляра.

from random import choice, randint


class FileName:

    def __init__(self, file_name: str, quantity: int):
        self.file_name = file_name
        self.quantity = quantity


    def pseudo_gen(self):
        LETTERS_VOVS = 'aeyuio'
        LETTERS_CONS = 'qwrtpsdfghjklzxcvbnm'
        MIN_LENGHT = 4
        MAX_LENGHT = 7
        with open(self.file_name, 'a', encoding='utf-8') as f:
            for _ in range(self.quantity):
                name = ''.join(choice(LETTERS_VOVS) if i in (1, 4, 6) else choice(LETTERS_CONS)
                               for i in range(randint(MIN_LENGHT, MAX_LENGHT)))
                f.write(name.capitalize() + '\n')



if __name__ == '__main__':
    example = FileName('task_02.txt', 10)
    example.pseudo_gen()

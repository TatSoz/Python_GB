# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста и для пользователя.

class Archive:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.num_list = []
            cls.__instance.text_list = []
        else:
            cls.__instance.num_list.append(cls.__instance.num)
            cls.__instance.text_list.append(cls.__instance.text)
        return cls.__instance

    def __init__(self, num: int, text: str):
        self.text = text
        self.num = num

    def __str__(self):
        return f'Текст = {self.text}, число = {self.num}, архив текст = {self.text_list}, архив чисел = {self.num_list}'

    def __repr__(self):
        return f'Текст = {self.text}, число = {self.num}'



if __name__ == '__main__':
    new_arch = Archive(1, 'test')
    # print(new_arch.num_list)
    # print(new_arch.text_list)
    print(new_arch)
    print(repr(new_arch))


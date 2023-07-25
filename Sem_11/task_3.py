# Добавьте к задачам 1 и 2 строки документации для классов.

class Archive:
    """Archive class"""
    __instance = None

    def __new__(cls, *args, **kwargs):
        """Переопределение класса"""
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.num_list = []
            cls.__instance.text_list = []
        else:
            cls.__instance.num_list.append(cls.__instance.num)
            cls.__instance.text_list.append(cls.__instance.text)
        return cls.__instance

    def __init__(self, num: int, text: str):
        """Инициализация параметров экземпляра класса"""
        self.text = text
        self.num = num


if __name__ == '__main__':
    new_arch = Archive(1, 'test')
    # help(Archive)     # Вывод всей справочной информации о классе
    print(Archive.__doc__)    # Выводит документацию к указанному классу



# Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

from task_6 import Fish, Bird, Mammal

class AnimalFactory:
    def __init__(self, class_name: str, **kwargs):
        self.class_name = class_name

        for key, value in kwargs.items():
            if key == 'name':
                self.name = value
            if key == 'depth':
                self.depth = value
            if key == 'wings':
                self.wings = value
            if key == 'weigth':
                self.weigth = value

    def get_info_animal(self):
        if self.class_name == 'Fish':
            return Fish(self.name, self.depth)
        elif self.class_name == 'Bird':
            return Bird(self.name, self.wings)
        elif self.class_name == 'Mammal':
            return Mammal(self.name, self.weigth)
        else:
            return f'Нет такого животного'




if __name__ == '__main__':
    animal1 = AnimalFactory(class_name='Bird', name='Тетерев', wings=1).get_info_animal()
    print(animal1.special_info())
    animal2 = AnimalFactory(class_name='Fish', name='Щука', depth=20).get_info_animal()
    print(animal2.special_info())
    animal3 = AnimalFactory(class_name='Mammal', name='Собака', weigth=6).get_info_animal()
    print(animal3.special_info())







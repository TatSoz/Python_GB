# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.


class Animal:
    def __init__(self, name: str):
        self.name = name


class Fish(Animal):
    LITTLE = 10
    HIGHT = 100

    def __init__(self, name: str, depth: int):
        super().__init__(name)
        self.depth = depth

    def fish_type(self):
        if self.depth < self.LITTLE:
            return 'Мелководная рыба'
        elif self.depth > self.HIGHT:
            return 'Глубоководная рыба'
        else:
            return 'Средне-глубоководная рыба'


    def special_info(self):
        return f'{self.name} , глубина обитания {self.depth}, {self.fish_type()}'


class Bird(Animal):
    SHORT = 1
    lONG = 2
    def __init__(self, name: str, wings: int):
        super().__init__(name)
        self.wings = wings

    def bird_type(self):
        if self.wings < self.SHORT:
            return 'маленькя птичка'
        elif self.SHORT <= self.wings <= self.lONG:
            return 'средняя птичка'
        else:
            return 'крупная птичка'

    def special_info(self):
        return f'{self.name} , размах крыльев {self.wings}, {self.bird_type()}'


class Mammal(Animal):
    SMALL = 5
    BIG = 25
    def __init__(self, name: str, weight: int):
        super().__init__(name)
        self.weight = weight

    def mammal_type(self):
        if self.weight < self.SMALL:
            return 'маленькое животное'
        elif self.SMALL <= self.weight <= self.BIG:
            return 'среднее животное'
        else:
            return 'крупное животное'

    def special_info(self):
        return f'{self.name} , вес {self.weight}, {self.mammal_type()}'



if __name__ == '__main__':
    fish = Fish('Окунь', 12)
    bird = Bird('Орел', 7)
    mammal = Mammal('Росомаха', 15)
    print(mammal.special_info())
    print(fish.special_info())
    print(bird.special_info())





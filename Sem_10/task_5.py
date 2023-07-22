# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

class Fish:
    LITTLE = 10
    HIGHT = 100
    def __init__(self, name: str, depth: int):
        self.name = name
        self.depth = depth

    def get_info_fish(self):
        if self.depth < self.LITTLE:
            return 'Мелководная рыба'
        elif self.depth > self.HIGHT:
            return 'Глубоководная рыба'
        else:
            return 'Средне-глубоководная рыба'


class Bird:
    def __init__(self, name: str, length: int):
        self.name = name
        self.length = length

    def wing_span(self):
        return self.length * 2


if __name__ == '__main__':
    fish = Fish('Окунь', 12)
    print(fish.get_info_fish())
    bird = Bird('Орел', 15)
    print(bird.wing_span())


# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат


class Rectangle:

    def __init__(self, width: float, height: float = None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def calc_perimeter(self):
        return (self.height + self.width) * 2

    def calc_area(self):
        return self.width * self.height


if __name__ == '__main__':
    new_rec = Rectangle(10, 20)
    print(new_rec.calc_area())
    print(new_rec.calc_perimeter())

    new_square = Rectangle(10)
    print(new_square.calc_area())
    print(new_square.calc_perimeter())

    

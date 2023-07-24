# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длину и ширину.
# При вычитании не допускайте отрицательных значений.

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

    def __add__(self, other):
        new_perimeter = self.calc_perimeter() + other.calc_perimeter()
        width = self.width + other.width
        height = new_perimeter / 2 - width
        return Rectangle(width, height)


    def __sub__(self, other):
        if self.calc_perimeter() < other.calc_perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        new_perimeter = self.calc_perimeter() - other.calc_perimeter()
        height = new_perimeter / 2 - width
        return Rectangle(width, height)


    def __str__(self):
        return f'Периметр = {self.calc_perimeter()}, длина = {self.width}, высота {self.height}'


if __name__ == '__main__':
    new_rec = Rectangle(1, 2)

    new_rec_1 = Rectangle(5, 4)
    print(new_rec + new_rec_1)
    print(new_rec - new_rec_1)


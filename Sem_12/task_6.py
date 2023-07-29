# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.


class RectangleRanges:
    def __set_name__(self, owner, name):
        self.param_name = f'_{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError('Значение должно быть положительным')
        setattr(instance, self.param_name, value)


class Rectangle:
    """Класс Прямоугольник."""
    _width = RectangleRanges()
    _height = RectangleRanges()


    def __init__(self, width: float, height: float = None):
        """Инициализация нового экземпляра."""

        self._width = width
        if height is None:
            self._height = width
        else:
            self._height = height

    def calc_perimeter(self):
        """Расчет периметра прямоугольника."""

        return (self._height + self._width) * 2

    def calc_area(self):
        """Расчет площади прямоугольника."""

        return self._width * self._height

    def __add__(self, other):
        """Сложение двух прямоугольников."""

        new_perimeter = self.calc_perimeter() + other.calc_perimeter()
        width = self._width + other.width
        height = new_perimeter / 2 - width
        return Rectangle(width, height)


    def __sub__(self, other):
        """Вычитание прямоугольников"""

        if self.calc_perimeter() < other.calc_perimeter():
            self, other = other, self
        width = abs(self._width - other.width)
        new_perimeter = self.calc_perimeter() - other.calc_perimeter()
        height = new_perimeter / 2 - width
        return Rectangle(width, height)


    def __str__(self):
        return f'Периметр = {self.calc_perimeter()}, длина = {self._width}, высота {self._height}'

    def __eq__(self, other: object) -> bool:
        """Сравнение площадей двух прямоугольников на равенство"""

        return self.calc_area() == other.calc_area()

    def __lt__(self, other: object) -> bool:
        """Сравнение площадей двух прямоугольников на строго меньше"""

        return self.calc_area() < other.calc_area()

    def __le__(self, other: object) -> bool:
        """Сравнение площадей двух прямоугольников на меньше или равно"""

        return self.calc_area() <= other.calc_area()


if __name__ == '__main__':
    rect = Rectangle(5, 10)


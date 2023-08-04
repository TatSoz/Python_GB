# На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.

from rectangle import Rectangle
import unittest

class Testrect(unittest.TestCase):
    def setUp(self) -> None:
        self.rec1 = Rectangle(10, 10)
        self.rec2 = Rectangle(10)
        self.rec3 = Rectangle(15, 20)
        self.rec4 = Rectangle(1, 1)


    def test_created(self):
        self.assertEqual(self.rec1, Rectangle(10, 10))

    def test_perimeter(self):
        self.assertEqual(self.rec2. calc_perimeter(), 40)


    def test_area(self):
        self.assertEqual(self.rec3.calc_area(), 300)


    def test_eq_perimeter(self):
        self.assertEqual(self.rec1.calc_perimeter(), self.rec2.calc_perimeter())

    def test_eq_area(self):
        self.assertNotEqual(self.rec1.calc_area(), self.rec3.calc_area())

    def test_sum(self):
        self.assertEqual(self.rec2 + self.rec3, Rectangle(25, 30))

    def test_sub(self):
        self.assertEqual(self.rec1 - self.rec4, Rectangle(9, 9))


if __name__ == '__main__':
    unittest.main(verbosity=2)



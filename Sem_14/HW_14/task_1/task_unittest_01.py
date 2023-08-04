import unittest

class TestCaseName(unittest.TestCase):

    def test_2_bin(self):
        self.assertEqual('10', dec_to_n(2, 2))

    def test_2_oct(self):
        self.assertEqual('2', dec_to_n(2, 8))

    def test_8_bin(self):
        self.assertEqual('1000', dec_to_n(8, 2))

    def test_8_oct(self):
        self.assertEqual('10', dec_to_n(8, 8))

    def test_10_bin(self):
        self.assertEqual('1010', dec_to_n(10, 2))

    def test_10_oct(self):
        self.assertEqual('12', dec_to_n(10, 8))



def dec_to_n(number: int, system: int) -> str:
    l = []
    while number > 0:
        number, f = divmod(number, system)
        l.append(str(f))
    return ''.join(l[::-1])



if __name__ == '__main__':
    unittest.main(verbosity=2)
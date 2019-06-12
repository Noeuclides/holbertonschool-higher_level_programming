#!/usr/bin/python3

from models.square import Square
import unittest


class Test_Square_methods(unittest.TestCase):
    """
    unittest Square
    """
    def setUp(self):
        self.sq1 = Square(1)
        self.sq2 = Square(5)

    def test_square(self):
        self.assertEqual(self.sq1.width, 1)
        self.assertEqual(self.sq1.height, 1)
        self.assertEqual(self.sq1.x, 0)
        self.assertEqual(self.sq1.y, 0)

    def test_square_id(self):
        self.assertEqual(self.sq1.id, 3)

    def test_update_square(self):
        self.sq2.update(10, 1)
        self.assertEqual(self.sq2.size, 1)
        self.assertEqual(self.sq2.id, 10)

    def test_update_square2(self):
        self.sq2.update(10, 2, 1)
        self.assertEqual(self.sq2.id, 10)
        self.assertEqual(self.sq2.size, 2)
        self.assertEqual(self.sq2.x, 1)

    def test_update_square3(self):
        self.sq2.update(size=7, y=1)
        self.assertEqual(self.sq2.size, 7)
        self.assertEqual(self.sq2.y, 1)

if __name__ == '__main__':
    unittest.main()

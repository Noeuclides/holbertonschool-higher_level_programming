#!/usr/bin/python3

from models.square import Square
import unittest


class Test_Square_methods(unittest.TestCase):

    def test_square(self):
        self.assertEqual(Square(1).width, 1)
        self.assertEqual(Square(1).height, 1)
        self.assertEqual(Square(1).x, 0)
        self.assertEqual(Square(1).y, 0)

    def test_square_id(self):
        self.assertEqual(Square(1).id, 5)

    def test_update_square(self):
        s = Square(5)
        s.update(10, 1)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.id, 10)

    def test_update_square2(self):
        s = Square(5)
        s.update(10, 2, 1)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 1)

    def test_update_square3(self):
        s = Square(5)
        s.update(size=7, y=1)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.y, 1)

if __name__ == '__main__':
    unittest.main()

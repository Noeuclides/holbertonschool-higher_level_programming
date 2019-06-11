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
       self.assertEqual(Square(1).id, 1)


if __name__ == '__main__':
    unittest.main()

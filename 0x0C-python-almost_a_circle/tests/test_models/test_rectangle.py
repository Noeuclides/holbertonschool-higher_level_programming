#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle


class Test_Rectangle_Methods(unittest.TestCase):
    """
    unittest Rectangle
    """

    def setUp(self):
        self.r1 = Rectangle(1, 1)
        self.r2 = Rectangle(5, 8)
        self.r3 = Rectangle(4, 6, 2, 1, 12)

    def test_x_y(self):
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r3.x, 2)
        self.assertEqual(self.r3.y, 1)

    def test_width_height(self):
        self.assertEqual(self.r2.width, 5)
        self.assertEqual(self.r2.height, 8)
        self.assertEqual(self.r3.width, 4)
        self.assertEqual(self.r3.height, 6)
        with self.assertRaises(TypeError):
            self.r2.width = '5'
        with self.assertRaises(TypeError):
            self.r2.height = 8.9
        with self.assertRaises(TypeError):
            self.r3.x = {}
        with self.assertRaises(ValueError):
            self.r2.width = 0
        with self.assertRaises(ValueError):
            self.r2.height = -1
        with self.assertRaises(ValueError):
            self.r3.y = -10

    def test_id(self):
        self.assertEqual(self.r1.id, 5)

    def test_area(self):
        self.assertEqual(self.r2.area(), 40)

    """def test_display(self):
        self.assertEqual(str(Rectangle(2, 1).display()), '##')"""

    def test_update(self):
        self.r1.update(89)
        self.assertEqual(self.r1.id, 89)

    def test_update2(self):
        self.r1.update(89, 2, 3, 4)
        self.assertEqual(self.r1.x, 4)

    def test_update1(self):
        self.r2.update(x=1, height=2, y=3, width=4)
        self.assertEqual(self.r2.width, 4)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

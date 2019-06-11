#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle


class Test_Rectangle_Methods(unittest.TestCase):

    def test_x_y(self):
        self.assertEqual(Rectangle(1, 1).x, 0)
        self.assertEqual(Rectangle(1, 4).y, 0)

    def test_width_height(self):
        self.assertEqual(Rectangle(5, 8).width, 5)
        self.assertEqual(Rectangle(5, 8).height, 8)
        with self.assertRaises(TypeError):
            Rectangle('5', 8)
        with self.assertRaises(TypeError):
            Rectangle(5, 8.9)
        with self.assertRaises(TypeError):
            Rectangle(5, 8.9, {}, 'as')
        with self.assertRaises(ValueError):
            Rectangle(0, 0)
        with self.assertRaises(ValueError):
            Rectangle(5, 8, -1)
        with self.assertRaises(ValueError):
            Rectangle(5, 8, 1, -1)

    def test_id(self):
        self.assertEqual(Rectangle(5, 8).id, 2)

    def test_area(self):
        self.assertEqual(Rectangle(5, 8).area(), 40)

    def test_display(self):
        self.assertEqual(str(Rectangle(2, 1).display()), '##')

    def test__str__(self):
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update2(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual(r.x, 4)

    def test_update1(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r.width, 4)

if __name__ == '__main__':
    unittest.main()

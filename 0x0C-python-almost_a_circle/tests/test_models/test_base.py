#!/usr/bin/python3

import unittest
from models.base import Base


class test_Base_methods(unittest.TestCase):
    """
    unittest base
    """
    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(-5)
        self.b4 = Base(10)
        self.b5 = Base(4.5)

    def tearDown(self):
        self.__nb_objects = None

    def test_id(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, -5)
        self.assertEqual(self.b4.id, 10)
        self.assertEqual(self.b5.id, 4.5)


if __name__ == '__main__':
    unittest.main()

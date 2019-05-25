#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_types(self):
        l = ['a', 'holb', 10, -70, [23,3], 0]
        with self.assertRaises(TypeError):
            max_integer(l)

    def test_none(self):
        l = []
        self.assertEqual(None, max_integer(l))

    def test_integer(self):
        l = [2, 3, 80, 345, 0]
        self.assertEqual(345, max_integer(l))

    def test_negative(self):
        l = [-2, -3, -80, -345]
        self.assertEqual(-2, max_integer(l))


if __name__ == '__main__':
    unittest.main()

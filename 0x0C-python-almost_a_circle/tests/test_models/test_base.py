#!/usr/bin/python3

import unittest
from models.base import Base

class test_Base_methods(unittest.TestCase):

    val = 0

    def setUp(self):
        self.Base = Base()

    def test_class_attribute(self):
        val +=1
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_none(self):
        self.assertIsNotNone(Base().id)

    def test_nne(self):
        Base()
        val += 1
        self.assertEqual(Base._Base__nb_objects, val)



if __name__ == '__main__':
    unittest.main()

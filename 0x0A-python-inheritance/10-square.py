#!/usr/bin/python3
"""
module that
contains
a square
"""

Rectange = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    def __init__(self, size):
        super().integer_validator("size", size)
        self.___size = size
        super().area(self.__size, self.__size)
        
    def __str__(self):
        return("[Rectangle] {}/{}".format(size, size))

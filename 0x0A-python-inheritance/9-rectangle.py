#!/usr/bin/python3
"""
module with the class
BaseGeometry
"""


class BaseGeometry:
    """
    empty class
    """
    pass

    def area(self):
        """
        area of
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function that validates integers
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    class with an heritance of BaseGeometry
    """
    def __init__(self, width, height):
        """
        constructor of the class Rectangle
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        return(self.__width * self.__height)

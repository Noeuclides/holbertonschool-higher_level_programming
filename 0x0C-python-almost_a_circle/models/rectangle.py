#!/usr/bin/python3
"""
module that has Rectangle class methods
"""
from models.base import Base


class Rectangle(Base):
    """
    class that inheritance from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        constructor of Rectangle
        """
        super().__init__(id)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def area(self):
        """
        method that calculate the rectangle area
        """
        return(self.width * self.height)

    def display(self):
        """
        method that displays the rectangle
        """
        for i in range(self.y):
            print()
        for i in range(self.__height):
            print(' ' * self.x + '#' * self.__width)

    def __str__(self):
        """
        print information of the rectangle
        """
        i = self.id
        x = self.x
        y = self.y
        w = self.width
        h = self.height
        return("[Rectangle] ({}) {}/{} - {}/{}".format(i, x, y, w, h))

    def update(self, *args, **kwargs):
        """
        update attribute values
        """
        if args:
            d = ['id', 'width', 'height', 'x', 'y']
            i = 0
            for arg in args:
                setattr(self, d[i], arg)
                i += 1
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """
        rectangle attributes in dictionary
        """
        i = self.id
        x = self.x
        y = self.y
        w = self.width
        h = self.height
        dict = {"id":i, "width":w, "height":h, "x":x, "y":y}
        return(dict)

    @property
    def width(self):
        """
        getter
        """
        return(self.__width)

    @width.setter
    def width(self, value):
        """
        setter
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format("width"))
        elif value <= 0:
            raise ValueError("{:s} must be > 0".format("width"))
        else:
            self.__width = value

    @property
    def height(self):
        """
        height's getter
        """
        return(self.__height)

    @height.setter
    def height(self, value):
        """
        setter
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format("height"))
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        x's getter
        """
        return(self.__x)

    @x.setter
    def x(self, value):
        """
        setter
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format("x"))
        elif value < 0:
            raise ValueError("{:s} must be >= 0".format("x"))
        else:
            self.__x = value

    @property
    def y(self):
        """
        y getter
        """
        return(self.__y)

    @y.setter
    def y(self, value):
        """
        x setter
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format("y"))
        elif value < 0:
            raise ValueError("{:s} must be >= 0".format("y"))
        else:
            self.__y = value

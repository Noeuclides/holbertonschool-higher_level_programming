#!/usr/bin/python3
"""
"""
from models.base import Base


class Rectangle(Base):
    """
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        """
        super().__init__(id)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def area(self):
        """
        """
        return(self.width * self.height)

    def display(self):
        """
        """
        for i in range(self.y):
            print()
        for i in range(self.__height):
            print(' ' * self.x + '#' * self.__width)

    def __str__(self):
        """
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
        if args is not None:
            d = ['id', 'width', 'height', 'x', 'y']
            i = 0
            for arg in args:
                setattr(self, d[i], arg)
                i += 1
        else:
            for key, value in kwargs:
                key = value

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format("width"))
        elif value <= 0:
            raise ValueError("{:s} must be > 0".format("width"))
        else:
            self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format("height"))
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return(self.__x)

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format("x"))
        elif value < 0:
            raise ValueError("{:s} must be >= 0".format("x"))
        else:
            self.__x = value

    @property
    def y(self):
        return(self.__y)

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format("y"))
        elif value < 0:
            raise ValueError("{:s} must be >= 0".format("y"))
        else:
            self.__y = value

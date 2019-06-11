#!/usr/bin/python3

from models.rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size

    def __str__(self):
        """
        """
        i = self.id
        x = self.x
        y = self.y
        s = self.width
        return("[Square] ({}) {}/{} - {}".format(i, x, y, s))

    @property
    def size(self):
        return(self.width)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format("width"))
        elif value <= 0:
            raise ValueError("{:s} must be > 0".format("width"))
        else:
            self.width = value
            self.height = value

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

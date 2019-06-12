#!/usr/bin/python3
"""
module with square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    square that inheritance from Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        constructor of the class
        """
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size

    def __str__(self):
        """
        print class information
        """
        i = self.id
        x = self.x
        y = self.y
        s = self.width
        return("[Square] ({}) {}/{} - {}".format(i, x, y, s))

    @property
    def size(self):
        """
        size getter
        """
        return(self.width)

    @size.setter
    def size(self, value):
        """
        size setter
        """
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
        if len(args) > 2:
            args = list(args)
            args.insert(2, args[1])
        super().update(*args, **kwargs)

    def to_dictionary(self):
        """dictionary inheritance from Rectangle"""
        dict_sq = {}
        dict_sq = super().to_dictionary()
        dict_sq["size"] = dict_sq["width"]
        del dict_sq["width"]
        del dict_sq["height"]
        print(dict_sq)
        return(dict_sq)

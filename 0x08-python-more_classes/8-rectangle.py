#!/usr/bin/python3
class Rectangle:

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return(self._width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @width.deleter
    def width(self, value):
        print("Bye rectangle...")
        del self._width

    @property
    def height(self):
        return(self._height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._height = value

    @height.deleter
    def height(self, value):
        print("Bye rectangle...")
        del self._height

    def area(self):
        return(self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return(0)
        return(2*self.width + 2*self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return("")
        r = []
        m = self.width
        for i in range(self.height):
            r.append("{}".format(self.print_symbol*m) + '\n')
        return("".join(r))

    def __repr__(self):
        rec = type(self).__name__
        m = "{}({}, {})"
        return(m.format(rec, self.width, self.height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) == Rectangle.area(rect_2):
            return(rect_1)
        elif Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return(rect_1)
        else:
            return(rect_2)
